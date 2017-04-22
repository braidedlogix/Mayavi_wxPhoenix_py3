# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui.item import Item, spring
from traitsui.group import HGroup
from traitsui.view import View

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk


def InstanceEditor(*args, **kw):
    from traitsui.editors.api import InstanceEditor as Editor
    return Editor(view_name="handler.view")

try:
    long
except NameError:
    # Silly workaround for Python3.
    long = int

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class FeatureEdges(PolyDataAlgorithm):
    """
    FeatureEdges - extract boundary, non-manifold, and/or sharp edges
    from polygonal data
    
    Superclass: PolyDataAlgorithm
    
    FeatureEdges is a filter to extract special types of edges from
    input polygonal data. These edges are either 1) boundary (used by one
    polygon) or a line cell; 2) non-manifold (used by three or more
    polygons); 3) feature edges (edges used by two triangles and whose
    dihedral angle > feature_angle); or 4) manifold edges (edges used by
    exactly two polygons). These edges may be extracted in any
    combination. Edges may also be "colored" (i.e., scalar values
    assigned) based on edge type. The cell coloring is assigned to the
    cell data of the extracted edges.
    
    @warning
    To see the coloring of the liens you may have to set the scalar_mode
    instance variable of the mapper to set_scalar_mode_to_use_cell_data().
    (This is only a problem if there are point data scalars.)
    
    @sa
    ExtractEdges
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFeatureEdges, obj, update, **traits)
    
    boundary_edges = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the extraction of boundary edges.
        """
    )

    def _boundary_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoundaryEdges,
                        self.boundary_edges_)

    coloring = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the coloring of edges by type.
        """
    )

    def _coloring_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColoring,
                        self.coloring_)

    feature_edges = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the extraction of feature edges.
        """
    )

    def _feature_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFeatureEdges,
                        self.feature_edges_)

    manifold_edges = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the extraction of manifold edges.
        """
    )

    def _manifold_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetManifoldEdges,
                        self.manifold_edges_)

    non_manifold_edges = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the extraction of non-manifold edges.
        """
    )

    def _non_manifold_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNonManifoldEdges,
                        self.non_manifold_edges_)

    feature_angle = traits.Trait(30.0, traits.Range(0.0, 180.0, enter_set=True, auto_set=False), help=\
        """
        Specify the feature angle for extracting feature edges.
        """
    )

    def _feature_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFeatureAngle,
                        self.feature_angle)

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Set / get a spatial locator for merging points. By default an
        instance of MergePoints is used.
        """
    )

    output_points_precision = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set/get the desired precision for the output types. See the
        documentation for the Algorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def create_default_locator(self):
        """
        V.create_default_locator()
        C++: void CreateDefaultLocator()
        Create default locator. Used to create one when none is
        specified.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

    _updateable_traits_ = \
    (('boundary_edges', 'GetBoundaryEdges'), ('coloring', 'GetColoring'),
    ('feature_edges', 'GetFeatureEdges'), ('manifold_edges',
    'GetManifoldEdges'), ('non_manifold_edges', 'GetNonManifoldEdges'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('feature_angle', 'GetFeatureAngle'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'boundary_edges', 'coloring', 'debug',
    'feature_edges', 'global_warning_display', 'manifold_edges',
    'non_manifold_edges', 'release_data_flag', 'feature_angle',
    'output_points_precision', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FeatureEdges, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FeatureEdges properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['boundary_edges', 'coloring', 'feature_edges',
            'manifold_edges', 'non_manifold_edges'], [], ['feature_angle',
            'output_points_precision']),
            title='Edit FeatureEdges properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FeatureEdges properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


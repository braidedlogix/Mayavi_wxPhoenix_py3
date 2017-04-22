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


class PolyDataNormals(PolyDataAlgorithm):
    """
    PolyDataNormals - compute normals for polygonal mesh
    
    Superclass: PolyDataAlgorithm
    
    PolyDataNormals is a filter that computes point and/or cell
    normals for a polygonal mesh. The user specifies if they would like
    the point and/or cell normals to be computed by setting the
    compute_cell_normals and compute_point_normals flags.
    
    The computed normals (a FloatArray) are set to be the active
    normals (using set_normals()) of the point_data and/or the cell_data
    (respectively) of the output poly_data. The name of these arrays is
    "Normals", so they can be retrieved either with
    ArrayDownCast(output->GetPointData()->GetNormals()) or with
    ArrayDownCast(output->GetPointData()->GetArray("Normals"))
    
    The filter can reorder polygons to insure consistent orientation
    across polygon neighbors. Sharp edges can be split and points
    duplicated with separate normals to give crisp (rendered) surface
    definition. It is also possible to globally flip the normal
    orientation.
    
    The algorithm works by determining normals for each polygon and then
    averaging them at shared points. When sharp edges are present, the
    edges are split and new points generated to prevent blurry edges (due
    to Gouraud shading).
    
    @warning
    Normals are computed only for polygons and triangle strips. Normals
    are not computed for lines or vertices.
    
    @warning
    Triangle strips are broken up into triangle polygons. You may want to
    restrip the triangles.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyDataNormals, obj, update, **traits)
    
    auto_orient_normals = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the automatic determination of correct normal
        orientation. NOTE: This assumes a completely closed surface (i.e.
        no boundary edges) and no non-manifold edges. If these
        constraints do not hold, all bets are off. This option adds some
        computational complexity, and is useful if you don't want to have
        to inspect the rendered image to determine whether to turn on the
        flip_normals flag. However, this flag can work with the
        flip_normals flag, and if both are set, all the normals in the
        output will point "inward".
        """
    )

    def _auto_orient_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoOrientNormals,
                        self.auto_orient_normals_)

    compute_cell_normals = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the computation of cell normals.
        """
    )

    def _compute_cell_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeCellNormals,
                        self.compute_cell_normals_)

    compute_point_normals = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the computation of point normals.
        """
    )

    def _compute_point_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputePointNormals,
                        self.compute_point_normals_)

    consistency = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the enforcement of consistent polygon ordering.
        """
    )

    def _consistency_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConsistency,
                        self.consistency_)

    flip_normals = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the global flipping of normal orientation. Flipping
        reverves the meaning of front and back for Frontface and Backface
        culling in Property.  Flipping modifies both the normal
        direction and the order of a cell's points.
        """
    )

    def _flip_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFlipNormals,
                        self.flip_normals_)

    non_manifold_traversal = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off traversal across non-manifold edges. This will
        prevent problems where the consistency of polygonal ordering is
        corrupted due to topological loops.
        """
    )

    def _non_manifold_traversal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNonManifoldTraversal,
                        self.non_manifold_traversal_)

    splitting = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the splitting of sharp edges.
        """
    )

    def _splitting_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSplitting,
                        self.splitting_)

    feature_angle = traits.Trait(30.0, traits.Range(0.0, 180.0, enter_set=True, auto_set=False), help=\
        """
        Specify the angle that defines a sharp edge. If the difference in
        angle across neighboring polygons is greater than this value, the
        shared edge is considered "sharp".
        """
    )

    def _feature_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFeatureAngle,
                        self.feature_angle)

    output_points_precision = traits.Trait(2, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
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

    _updateable_traits_ = \
    (('auto_orient_normals', 'GetAutoOrientNormals'),
    ('compute_cell_normals', 'GetComputeCellNormals'),
    ('compute_point_normals', 'GetComputePointNormals'), ('consistency',
    'GetConsistency'), ('flip_normals', 'GetFlipNormals'),
    ('non_manifold_traversal', 'GetNonManifoldTraversal'), ('splitting',
    'GetSplitting'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('feature_angle', 'GetFeatureAngle'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_orient_normals', 'compute_cell_normals',
    'compute_point_normals', 'consistency', 'debug', 'flip_normals',
    'global_warning_display', 'non_manifold_traversal',
    'release_data_flag', 'splitting', 'feature_angle',
    'output_points_precision', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyDataNormals, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyDataNormals properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_orient_normals', 'compute_cell_normals',
            'compute_point_normals', 'consistency', 'flip_normals',
            'non_manifold_traversal', 'splitting'], [], ['feature_angle',
            'output_points_precision']),
            title='Edit PolyDataNormals properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyDataNormals properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


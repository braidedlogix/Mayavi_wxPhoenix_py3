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


class AdaptiveSubdivisionFilter(PolyDataAlgorithm):
    """
    AdaptiveSubdivisionFilter - subdivide triangles based on edge
    and/or area metrics
    
    Superclass: PolyDataAlgorithm
    
    AdaptiveSubdivisionFilter is a filter that subdivides triangles
    based on maximum edge length and/or triangle area. It uses a simple
    case-based, multi-pass approach to repeatedly subdivide the input
    triangle mesh to meet the area and/or edge length criteria. New
    points may be inserted only on edges; depending on the number of
    edges to be subdivided a different number of triangles are inserted
    ranging from two (i.e., two triangles replace the original one) to
    four.
    
    Triangle subdivision is controlled by specifying a maximum edge
    length and/or triangle area that any given triangle may have.
    Subdivision proceeds until there criteria are satisified. Note that
    using excessively small criteria values can produce enormous meshes
    with the possibility of exhausting system memory. Also, if you want
    to ignore a particular criterion value (e.g., triangle area) then
    simply set the criterion value to a very large value (e.g.,
    VTK_DOUBLE_MAX).
    
    An incremental point locator is used because as new points are
    created, a search is made to ensure that a point has not already been
    created. This ensures that the mesh remains compatible (watertight)
    as long as certain criteria are not used (triangle area limit, and
    number of triangles limit).
    
    To prevent overly large triangle meshes from being created, it is
    possible to set a limit on the number of triangles created. By
    default this number is a very large number (i.e., no limit). Further,
    a limit on the number of passes can also be set, this is mostly
    useful to generated animations of the algorithm.
    
    Finally, the attribute data (point and cell data) is treated as
    follows. The cell data from a parent triangle is assigned to its
    subdivided children.  Point data is interpolated along edges as the
    edges are subdivided.
    
    @warning
    The subdivision is linear along edges. Thus do not expect smoothing
    or blending effects to occur. If you need to smooth the resulting
    mesh use an algorithm like WindowedSincPolyDataFilter or
    SmoothPolyDataFilter.
    
    The filter retains mesh compatibility (watertightness) if the mesh
    was originally compatible; and the area, max triangles criteria are
    not used.
    
    @warning
    The filter requires a triangle mesh. Use TriangleFilter to
    tessellate the mesh if necessary.
    
    @sa
    InterpolatingSubdivisionFilter LinearSubdivisionFilter
    ButterflySubdivisionFilter TriangleFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAdaptiveSubdivisionFilter, obj, update, **traits)
    
    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Set / get a spatial locator for merging points. By default, an
        instance of MergePoints is used. This is used to merge
        coincident points during subdivision.
        """
    )

    maximum_edge_length = traits.Trait(1.0, traits.Range(1e-06, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Specify the maximum edge length that a triangle may have. Edges
        longer than this value are split in half and the associated
        triangles are modified accordingly.
        """
    )

    def _maximum_edge_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumEdgeLength,
                        self.maximum_edge_length)

    maximum_number_of_passes = traits.Trait(9223372036854775807, traits.Range(1, 9223372036854775807, enter_set=True, auto_set=False), help=\
        """
        Set a limit on the number of passes (i.e., levels of
        subdivision).  If the limit is hit, then the subdivision process
        stops and additional passes (needed to meet other criteria) are
        aborted. The default limit is set to a very large number (i.e.,
        no effective limit).
        """
    )

    def _maximum_number_of_passes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfPasses,
                        self.maximum_number_of_passes)

    maximum_number_of_triangles = traits.Trait(9223372036854775807, traits.Range(1, 9223372036854775807, enter_set=True, auto_set=False), help=\
        """
        Set a limit on the maximum number of triangles that can be
        created.  If the limit is hit, it may result in premature
        termination of the algorithm and the results may be less than
        satisfactory (for example non-watertight meshes may be created).
        By default, the limit is set to a very large number (i.e., no
        effective limit).
        """
    )

    def _maximum_number_of_triangles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfTriangles,
                        self.maximum_number_of_triangles)

    maximum_triangle_area = traits.Trait(1.0, traits.Range(1e-06, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Specify the maximum area that a triangle may have. Triangles
        larger than this value are subdivided to meet this threshold.
        Note that if this criterion is used it may produce non-watertight
        meshes as a result.
        """
    )

    def _maximum_triangle_area_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumTriangleArea,
                        self.maximum_triangle_area)

    output_points_precision = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set/get the desired precision for the output types. See the
        documentation for the Algorithm::Precision enum for an
        explanation of the available precision settings.
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
        Create a default locator. Used to create one when none is
        specified.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_edge_length', 'GetMaximumEdgeLength'),
    ('maximum_number_of_passes', 'GetMaximumNumberOfPasses'),
    ('maximum_number_of_triangles', 'GetMaximumNumberOfTriangles'),
    ('maximum_triangle_area', 'GetMaximumTriangleArea'),
    ('output_points_precision', 'GetOutputPointsPrecision'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'maximum_edge_length',
    'maximum_number_of_passes', 'maximum_number_of_triangles',
    'maximum_triangle_area', 'output_points_precision', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AdaptiveSubdivisionFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AdaptiveSubdivisionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['maximum_edge_length', 'maximum_number_of_passes',
            'maximum_number_of_triangles', 'maximum_triangle_area',
            'output_points_precision']),
            title='Edit AdaptiveSubdivisionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AdaptiveSubdivisionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


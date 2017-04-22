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

from tvtk.tvtk_classes.point_cloud_filter import PointCloudFilter


class RadiusOutlierRemoval(PointCloudFilter):
    """
    RadiusOutlierRemoval - remove isolated points
    
    Superclass: PointCloudFilter
    
    RadiusOutlierRemoval removes isolated points; i.e., those points
    that have few neighbors within a specified radius. The user must
    specify the radius defining the local region, as well as the
    isolation threshold (i.e., number of neighboring points required for
    the point to be considered isolated). Optionally, users can specify a
    point locator to accelerate local neighborhood search operations. (By
    default a StaticPointLocator will be created.)
    
    Note that while any PointSet type can be provided as input, the
    output is represented by an explicit representation of points via a
    PolyData. This output polydata will populate its instance of
    Points, but no cells will be defined (i.e., no Vertex or
    PolyVertex are contained in the output). Also, after filter
    execution, the user can request a IdType* map which indicates how
    the input points were mapped to the output. A value of map[i] (where
    i is the ith input point) less than 0 means that the ith input point
    was removed. (See also the superclass documentation for accessing the
    removed points through the filter's second output.)
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    PointCloudFilter StatisticalOutlierRemoval ExtractPoints
    ThresholdPoints ImplicitFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRadiusOutlierRemoval, obj, update, **traits)
    
    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Specify a point locator. By default a StaticPointLocator is
        used. The locator performs efficient searches to locate near a
        specified interpolation position.
        """
    )

    number_of_neighbors = traits.Trait(2, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the number of neighbors that a point must have, within
        the specified radius, for the point to not be considered
        isolated.
        """
    )

    def _number_of_neighbors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfNeighbors,
                        self.number_of_neighbors)

    radius = traits.Trait(1.0, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Specify the local search radius.
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

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
    (('generate_outliers', 'GetGenerateOutliers'), ('generate_vertices',
    'GetGenerateVertices'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_neighbors', 'GetNumberOfNeighbors'), ('radius',
    'GetRadius'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_outliers', 'generate_vertices',
    'global_warning_display', 'release_data_flag', 'number_of_neighbors',
    'progress_text', 'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RadiusOutlierRemoval, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RadiusOutlierRemoval properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_outliers', 'generate_vertices'], [],
            ['number_of_neighbors', 'radius']),
            title='Edit RadiusOutlierRemoval properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RadiusOutlierRemoval properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


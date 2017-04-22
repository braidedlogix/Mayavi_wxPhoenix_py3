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


class PointCloudFilter(PolyDataAlgorithm):
    """
    PointCloudFilter - abstract class for filtering a point cloud
    
    Superclass: PolyDataAlgorithm
    
    PointCloudFilter serves as a base for classes that filter point
    clouds. It takes as input any PointSet (which represents points
    explicitly using Points) and produces as output an explicit
    representation of filtered points via a PolyData. This output
    PolyData will populate its instance of Points, and typically no
    cells will be defined (i.e., no Vertex or PolyVertex are
    contained in the output unless explicitly requested). Also, after
    filter execution, the user can request a IdType* point map which
    indicates how the input points were mapped to the output. A value of
    point_map[i] < 0 (where i is the ith input point) means that the ith
    input point was removed. Otherwise point_map[i] indicates the position
    in the output Points array (point cloud).
    
    Optionally the filter may produce a second output. This second output
    is another PolyData with a Points that contains the points that
    were removed during processing. To produce this second output, you
    must enable generate_outliers. If this optional, second output is
    created, then the contents of the point_map are modified as well. In
    this case, a point_map[i] < 0 means that the ith input point has been
    mapped to the (-_point_map[i])-_1 position in the second output's
    Points.
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @warning
    The filter copies point attributes from input to output consistent
    with the filtering operation.
    
    @warning
    It is convenient to use PointGaussianMapper to render the points
    (since this mapper does not require cells to be defined, and it is
    quite fast).
    
    @sa
    RadiusOutlierRemoval PointGaussianMapper ThresholdPoints
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointCloudFilter, obj, update, **traits)
    
    generate_outliers = tvtk_base.false_bool_trait(help=\
        """
        If this method is enabled (true), then a second output will be
        created that contains the outlier points. By default this is off
        (false).  Note that if enabled, the point_map is modified as well:
        the outlier points are listed as well, with similar meaning,
        except their value is negated and shifted by -1.
        """
    )

    def _generate_outliers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateOutliers,
                        self.generate_outliers_)

    generate_vertices = tvtk_base.false_bool_trait(help=\
        """
        If this method is enabled (true), then the outputs will contain a
        vertex cells (i.e., a PolyVertex for each output). This takes
        a lot more memory but some VTK filters need cells to function
        properly. By default this is off (false).
        """
    )

    def _generate_vertices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateVertices,
                        self.generate_vertices_)

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

    def _get_number_of_points_removed(self):
        return self._vtk_obj.GetNumberOfPointsRemoved()
    number_of_points_removed = traits.Property(_get_number_of_points_removed, help=\
        """
        Return the number of points removed after filter execution. The
        information retuned is valid only after the filter executes.
        """
    )

    def _get_point_map(self):
        return self._vtk_obj.GetPointMap()
    point_map = traits.Property(_get_point_map, help=\
        """
        Retrieve a map which indicates, on a point-by-point basis, where
        each input point was placed into the output. In other words,
        map[i] indicates where the ith input point is located in the
        output array of points. If map[i] < 0, then the ith input point
        was removed during filter execution.  This method returns valid
        information only after the filter executes.
        """
    )

    _updateable_traits_ = \
    (('generate_outliers', 'GetGenerateOutliers'), ('generate_vertices',
    'GetGenerateVertices'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_outliers', 'generate_vertices',
    'global_warning_display', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointCloudFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PointCloudFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_outliers', 'generate_vertices'], [], []),
            title='Edit PointCloudFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointCloudFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


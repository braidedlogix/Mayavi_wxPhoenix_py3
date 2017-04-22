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


class StatisticalOutlierRemoval(PointCloudFilter):
    """
    StatisticalOutlierRemoval - remove sparse outlier points
    
    Superclass: PointCloudFilter
    
    The StatisticalOutlierRemoval filter removes sparse outlier points
    through statistical analysis. The average (mean) distance between
    points in the point cloud is computed (taking a local sample size
    around each point); followed by computation of the global standard
    deviation of distances between points. This global, statistical
    information is compared against the mean separation distance for each
    point; those points whose average separation is greater than the
    user-specified variation in a multiple of standard deviation are
    removed.
    
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
    PointCloudFilter RadiusOutlierRemoval ExtractPoints
    ThresholdPoints
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStatisticalOutlierRemoval, obj, update, **traits)
    
    computed_mean = traits.Trait(0.0, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        After execution, return the value of the computed mean. Before
        execution the value returned is invalid.
        """
    )

    def _computed_mean_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputedMean,
                        self.computed_mean)

    computed_standard_deviation = traits.Trait(0.0, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        After execution, return the value of the computed sigma (standard
        deviation). Before execution the value returned is invalid.
        """
    )

    def _computed_standard_deviation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputedStandardDeviation,
                        self.computed_standard_deviation)

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
        used. The locator performs efficient searches to locate points
        surroinding a sample point.
        """
    )

    sample_size = traits.Trait(25, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        For each point sampled, specify the number of the closest,
        surrounding points used to compute statistics. By default 25
        points are used. Smaller numbers may speed performance.
        """
    )

    def _sample_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleSize,
                        self.sample_size)

    standard_deviation_factor = traits.Trait(1.0, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        The filter uses this specified standard deviation factor to
        extract points. By default, points within 1.0 standard deviations
        (i.e., a standard_deviation_factor=_1._0) of the mean distance to
        neighboring points are retained.
        """
    )

    def _standard_deviation_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStandardDeviationFactor,
                        self.standard_deviation_factor)

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
    ('computed_mean', 'GetComputedMean'), ('computed_standard_deviation',
    'GetComputedStandardDeviation'), ('sample_size', 'GetSampleSize'),
    ('standard_deviation_factor', 'GetStandardDeviationFactor'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_outliers', 'generate_vertices',
    'global_warning_display', 'release_data_flag', 'computed_mean',
    'computed_standard_deviation', 'progress_text', 'sample_size',
    'standard_deviation_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StatisticalOutlierRemoval, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StatisticalOutlierRemoval properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_outliers', 'generate_vertices'], [],
            ['computed_mean', 'computed_standard_deviation', 'sample_size',
            'standard_deviation_factor']),
            title='Edit StatisticalOutlierRemoval properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StatisticalOutlierRemoval properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


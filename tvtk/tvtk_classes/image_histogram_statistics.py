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

from tvtk.tvtk_classes.image_histogram import ImageHistogram


class ImageHistogramStatistics(ImageHistogram):
    """
    ImageHistogramStatistics - Compute statistics for an image
    
    Superclass: ImageHistogram
    
    ImageHistogramStatistics computes statistics such as mean, median,
    and standard deviation.  These statistics are computed from the
    histogram of the image, rather than from the image itself, because
    this is more efficient than computing the statistics while traversing
    the pixels. If the input image is of type float or double, then the
    precision of the Mean, Median, and standard_deviation will depend on
    the number of histogram bins.  By default, 65536 bins are used for
    float data, giving at least 16 bits of precision.@par Thanks: Thanks
    to David Gobbi at the Seaman Family MR Centre and Dept. of Clinical
    Neurosciences, Foothills Medical Centre, Calgary, for providing this
    class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageHistogramStatistics, obj, update, **traits)
    
    auto_range_expansion_factors = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.1, 0.1), cols=2, help=\
        """
        
        """
    )

    def _auto_range_expansion_factors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoRangeExpansionFactors,
                        self.auto_range_expansion_factors)

    auto_range_percentiles = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(1.0, 99.0), cols=2, help=\
        """
        
        """
    )

    def _auto_range_percentiles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoRangePercentiles,
                        self.auto_range_percentiles)

    def _get_auto_range(self):
        return self._vtk_obj.GetAutoRange()
    auto_range = traits.Property(_get_auto_range, help=\
        """
        
        """
    )

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get a data object for one of the input port connections.  The use
        of this method is strongly discouraged, but some filters that
        were written a long time ago still use this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_maximum(self):
        return self._vtk_obj.GetMaximum()
    maximum = traits.Property(_get_maximum, help=\
        """
        Get the maximum value present in the image.  This value is
        computed when Update() is called.
        """
    )

    def _get_mean(self):
        return self._vtk_obj.GetMean()
    mean = traits.Property(_get_mean, help=\
        """
        Get the mean value of the image.  This value is computed when
        Update() is called.
        """
    )

    def _get_median(self):
        return self._vtk_obj.GetMedian()
    median = traits.Property(_get_median, help=\
        """
        Get the median value.  This is computed when Update() is called.
        """
    )

    def _get_minimum(self):
        return self._vtk_obj.GetMinimum()
    minimum = traits.Property(_get_minimum, help=\
        """
        Get the minimum value present in the image.  This value is
        computed when Update() is called.
        """
    )

    def _get_standard_deviation(self):
        return self._vtk_obj.GetStandardDeviation()
    standard_deviation = traits.Property(_get_standard_deviation, help=\
        """
        Get the standard deviation of the values in the image.  This is
        computed when Update() is called.
        """
    )

    _updateable_traits_ = \
    (('automatic_binning', 'GetAutomaticBinning'),
    ('generate_histogram_image', 'GetGenerateHistogramImage'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('histogram_image_scale', 'GetHistogramImageScale'), ('split_mode',
    'GetSplitMode'), ('auto_range_expansion_factors',
    'GetAutoRangeExpansionFactors'), ('auto_range_percentiles',
    'GetAutoRangePercentiles'), ('active_component',
    'GetActiveComponent'), ('bin_origin', 'GetBinOrigin'), ('bin_spacing',
    'GetBinSpacing'), ('histogram_image_size', 'GetHistogramImageSize'),
    ('maximum_number_of_bins', 'GetMaximumNumberOfBins'),
    ('number_of_bins', 'GetNumberOfBins'), ('desired_bytes_per_piece',
    'GetDesiredBytesPerPiece'), ('enable_smp', 'GetEnableSMP'),
    ('global_default_enable_smp', 'GetGlobalDefaultEnableSMP'),
    ('minimum_piece_size', 'GetMinimumPieceSize'), ('number_of_threads',
    'GetNumberOfThreads'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'automatic_binning', 'debug',
    'generate_histogram_image', 'global_warning_display',
    'release_data_flag', 'histogram_image_scale', 'split_mode',
    'active_component', 'auto_range_expansion_factors',
    'auto_range_percentiles', 'bin_origin', 'bin_spacing',
    'desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
    'histogram_image_size', 'maximum_number_of_bins',
    'minimum_piece_size', 'number_of_bins', 'number_of_threads',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageHistogramStatistics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageHistogramStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic_binning', 'generate_histogram_image'],
            ['histogram_image_scale', 'split_mode'], ['active_component',
            'auto_range_expansion_factors', 'auto_range_percentiles',
            'bin_origin', 'bin_spacing', 'desired_bytes_per_piece', 'enable_smp',
            'global_default_enable_smp', 'histogram_image_size',
            'maximum_number_of_bins', 'minimum_piece_size', 'number_of_bins',
            'number_of_threads']),
            title='Edit ImageHistogramStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageHistogramStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


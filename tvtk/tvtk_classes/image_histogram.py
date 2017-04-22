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

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageHistogram(ThreadedImageAlgorithm):
    """
    ImageHistogram - Compute the histogram for an image.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageHistogram generates a histogram from its input, and
    optionally produces a 2d black-and-white image of the histogram as
    its output. Unlike the class ImageAccumulate, a multi-component
    image does not result in a multi-dimensional histogram.  Instead, the
    resulting histogram will be the sum of the histograms of each of the
    individual components, unless set_active_component is used to choose a
    single component.@par Thanks: Thanks to David Gobbi at the Seaman
    Family MR Centre and Dept. of Clinical Neurosciences, Foothills
    Medical Centre, Calgary, for providing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageHistogram, obj, update, **traits)
    
    automatic_binning = tvtk_base.false_bool_trait(help=\
        """
        If this is On, then the histogram binning will be done
        automatically. For char and unsigned char data, there will be 256
        bins with unit spacing.  For data of type short and larger, there
        will be between 256 and maximum_number_of_bins, depending on the
        range of the data, and the bin_origin will be set to zero if no
        negative values are present, or to the smallest negative value if
        negative values are present. For float data, the
        maximum_number_of_bins will always be used. The bin_origin and
        bin_spacing will be set so that they provide a mapping from bin
        index to scalar value.
        """
    )

    def _automatic_binning_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutomaticBinning,
                        self.automatic_binning_)

    generate_histogram_image = tvtk_base.true_bool_trait(help=\
        """
        If this is On, then a histogram image will be produced as the
        output. Regardless of this setting, the histogram is always
        available as a IdTypeArray from the get_histogram method.
        """
    )

    def _generate_histogram_image_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateHistogramImage,
                        self.generate_histogram_image_)

    histogram_image_scale = traits.Trait('linear',
    tvtk_base.TraitRevPrefixMap({'linear': 0, 'log': 1, 'sqrt': 2}), help=\
        """
        Set the scale to use for the histogram image.  The default is a
        linear scale, but sqrt and log provide better visualization.
        """
    )

    def _histogram_image_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHistogramImageScale,
                        self.histogram_image_scale_)

    active_component = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the component for which to generate a histogram.  The default
        value is -1, which produces a histogram that is the sum of the
        histograms of the individual components.
        """
    )

    def _active_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetActiveComponent,
                        self.active_component)

    bin_origin = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        The value for the center of the first bin (default 0).  This is
        automatically computed unless automatic_binning is Off.
        """
    )

    def _bin_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBinOrigin,
                        self.bin_origin)

    bin_spacing = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The bin spacing (default 1).  This is automatically computed
        unless automatic_binning is Off.
        """
    )

    def _bin_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBinSpacing,
                        self.bin_spacing)

    histogram_image_size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(256, 256), cols=2, help=\
        """
        
        """
    )

    def _histogram_image_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHistogramImageSize,
                        self.histogram_image_size)

    maximum_number_of_bins = traits.Int(65536, enter_set=True, auto_set=False, help=\
        """
        The maximum number of bins to use when automatic_binning is On.
        When automatic_binning is On, the size of the output histogram
        will be set to the full range of the input data values, unless
        the full range is greater than this value.  By default, the max
        value is 65536, which is large enough to capture the full range
        of 16-bit integers.
        """
    )

    def _maximum_number_of_bins_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfBins,
                        self.maximum_number_of_bins)

    number_of_bins = traits.Int(256, enter_set=True, auto_set=False, help=\
        """
        The number of bins in histogram (default 256).  This is
        automatically computed unless automatic_binning is Off.
        """
    )

    def _number_of_bins_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfBins,
                        self.number_of_bins)

    def _get_histogram(self):
        return wrap_vtk(self._vtk_obj.GetHistogram())
    histogram = traits.Property(_get_histogram, help=\
        """
        Get the histogram as a IdTypeArray.  You must call Update()
        before calling this method.
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

    def _get_stencil(self):
        return wrap_vtk(self._vtk_obj.GetStencil())
    stencil = traits.Property(_get_stencil, help=\
        """
        Use a stencil to compute the histogram for just a part of the
        image.
        """
    )

    def _get_total(self):
        return self._vtk_obj.GetTotal()
    total = traits.Property(_get_total, help=\
        """
        Get the total count of the histogram.  This will be the number of
        voxels times the number of components.
        """
    )

    def set_stencil_connection(self, *args):
        """
        V.set_stencil_connection(AlgorithmOutput)
        C++: void SetStencilConnection(AlgorithmOutput *algOutput)
        Equivalent to set_input_connection(_1, alg_output).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetStencilConnection, *my_args)
        return ret

    def set_stencil_data(self, *args):
        """
        V.set_stencil_data(ImageStencilData)
        C++: void SetStencilData(ImageStencilData *stencil)
        Use a stencil to compute the histogram for just a part of the
        image.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetStencilData, *my_args)
        return ret

    _updateable_traits_ = \
    (('automatic_binning', 'GetAutomaticBinning'),
    ('generate_histogram_image', 'GetGenerateHistogramImage'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('histogram_image_scale', 'GetHistogramImageScale'), ('split_mode',
    'GetSplitMode'), ('active_component', 'GetActiveComponent'),
    ('bin_origin', 'GetBinOrigin'), ('bin_spacing', 'GetBinSpacing'),
    ('histogram_image_size', 'GetHistogramImageSize'),
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
    'active_component', 'bin_origin', 'bin_spacing',
    'desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
    'histogram_image_size', 'maximum_number_of_bins',
    'minimum_piece_size', 'number_of_bins', 'number_of_threads',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageHistogram, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageHistogram properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic_binning', 'generate_histogram_image'],
            ['histogram_image_scale', 'split_mode'], ['active_component',
            'bin_origin', 'bin_spacing', 'desired_bytes_per_piece', 'enable_smp',
            'global_default_enable_smp', 'histogram_image_size',
            'maximum_number_of_bins', 'minimum_piece_size', 'number_of_bins',
            'number_of_threads']),
            title='Edit ImageHistogram properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageHistogram properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


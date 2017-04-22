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


class ImageShrink3D(ThreadedImageAlgorithm):
    """
    ImageShrink3D - Subsamples an image.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageShrink3D shrinks an image by sub sampling on a uniform grid
    (integer multiples).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageShrink3D, obj, update, **traits)
    
    averaging = tvtk_base.true_bool_trait(help=\
        """
        Choose Mean, Minimum, Maximum, Median or sub sampling. The
        neighborhood operations are not centered on the sampled pixel.
        This may cause a half pixel shift in your output image. You can
        changed "Shift" to get around this. ImageGaussianSmooth or
        ImageMean with strides.
        """
    )

    def _averaging_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAveraging,
                        self.averaging_)

    maximum = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _maximum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximum,
                        self.maximum_)

    mean = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )

    def _mean_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMean,
                        self.mean_)

    median = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _median_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMedian,
                        self.median_)

    minimum = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _minimum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimum,
                        self.minimum_)

    shift = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(0, 0, 0), cols=3, help=\
        """
        
        """
    )

    def _shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShift,
                        self.shift)

    shrink_factors = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(1, 1, 1), cols=3, help=\
        """
        
        """
    )

    def _shrink_factors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShrinkFactors,
                        self.shrink_factors)

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

    _updateable_traits_ = \
    (('averaging', 'GetAveraging'), ('maximum', 'GetMaximum'), ('mean',
    'GetMean'), ('median', 'GetMedian'), ('minimum', 'GetMinimum'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('split_mode',
    'GetSplitMode'), ('shift', 'GetShift'), ('shrink_factors',
    'GetShrinkFactors'), ('desired_bytes_per_piece',
    'GetDesiredBytesPerPiece'), ('enable_smp', 'GetEnableSMP'),
    ('global_default_enable_smp', 'GetGlobalDefaultEnableSMP'),
    ('minimum_piece_size', 'GetMinimumPieceSize'), ('number_of_threads',
    'GetNumberOfThreads'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'averaging', 'debug', 'global_warning_display',
    'maximum', 'mean', 'median', 'minimum', 'release_data_flag',
    'split_mode', 'desired_bytes_per_piece', 'enable_smp',
    'global_default_enable_smp', 'minimum_piece_size',
    'number_of_threads', 'progress_text', 'shift', 'shrink_factors'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageShrink3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageShrink3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['averaging', 'maximum', 'mean', 'median', 'minimum'],
            ['split_mode'], ['desired_bytes_per_piece', 'enable_smp',
            'global_default_enable_smp', 'minimum_piece_size',
            'number_of_threads', 'shift', 'shrink_factors']),
            title='Edit ImageShrink3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageShrink3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


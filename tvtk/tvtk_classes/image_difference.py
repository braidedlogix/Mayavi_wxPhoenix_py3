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


class ImageDifference(ThreadedImageAlgorithm):
    """
    ImageDifference - Compares images for regression tests.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageDifference takes two rgb unsigned char images and compares
    them. It allows the images to be slightly different.  If allow_shift
    is on, then each pixel can be shifted by one pixel. Threshold is the
    allowable error for each pixel.
    
    This is not a symetric filter and the difference computed is not
    symetric when allow_shift is on. Specifically in that case a pixel in
    set_image input will be compared to the matching pixel in the input as
    well as to the input's eight connected neighbors. BUT... the opposite
    is not true. So for example if a valid image (_set_image) has a single
    white pixel in it, it will not find a match in the input image if the
    input image is black (because none of the nine suspect pixels are
    white). In contrast, if there is a single white pixel in the input
    image and the valid image (_set_image) is all black it will match with
    no error because all it has to do is find black pixels and even
    though the input image has a white pixel, its neighbors are not
    white.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageDifference, obj, update, **traits)
    
    allow_shift = tvtk_base.true_bool_trait(help=\
        """
        Specify whether the comparison will allow a shift of one pixel
        between the images.  If set, then the minimum difference between
        input images will be used to determine the difference. Otherwise,
        the difference is computed directly between pixels of identical
        row/column values.
        """
    )

    def _allow_shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllowShift,
                        self.allow_shift_)

    averaging = tvtk_base.true_bool_trait(help=\
        """
        Specify whether the comparison will include comparison of
        averaged 3x3 data between the images. For graphics renderings you
        normally would leave this on. For imaging operations it should be
        off.
        """
    )

    def _averaging_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAveraging,
                        self.averaging_)

    threshold = traits.Int(16, enter_set=True, auto_set=False, help=\
        """
        Specify a threshold tolerance for pixel differences.
        """
    )

    def _threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThreshold,
                        self.threshold)

    def _get_error(self):
        return self._vtk_obj.GetError()
    error = traits.Property(_get_error, help=\
        """
        Return the total error in comparing the two images.
        """
    )

    def _get_image(self):
        return wrap_vtk(self._vtk_obj.GetImage())
    image = traits.Property(_get_image, help=\
        """
        Specify the Image to compare the input to.
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

    def _get_thresholded_error(self):
        return self._vtk_obj.GetThresholdedError()
    thresholded_error = traits.Property(_get_thresholded_error, help=\
        """
        Return the total thresholded error in comparing the two images.
        The thresholded error is the error for a given pixel minus the
        threshold and clamped at a minimum of zero.
        """
    )

    def set_image_connection(self, *args):
        """
        V.set_image_connection(AlgorithmOutput)
        C++: void SetImageConnection(AlgorithmOutput *output)
        Specify the Image to compare the input to.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetImageConnection, *my_args)
        return ret

    def set_image_data(self, *args):
        """
        V.set_image_data(DataObject)
        C++: void SetImageData(DataObject *image)
        Specify the Image to compare the input to.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetImageData, *my_args)
        return ret

    _updateable_traits_ = \
    (('allow_shift', 'GetAllowShift'), ('averaging', 'GetAveraging'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('split_mode',
    'GetSplitMode'), ('threshold', 'GetThreshold'),
    ('desired_bytes_per_piece', 'GetDesiredBytesPerPiece'), ('enable_smp',
    'GetEnableSMP'), ('global_default_enable_smp',
    'GetGlobalDefaultEnableSMP'), ('minimum_piece_size',
    'GetMinimumPieceSize'), ('number_of_threads', 'GetNumberOfThreads'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'allow_shift', 'averaging', 'debug',
    'global_warning_display', 'release_data_flag', 'split_mode',
    'desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
    'minimum_piece_size', 'number_of_threads', 'progress_text',
    'threshold'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageDifference, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageDifference properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['allow_shift', 'averaging'], ['split_mode'],
            ['desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
            'minimum_piece_size', 'number_of_threads', 'threshold']),
            title='Edit ImageDifference properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageDifference properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


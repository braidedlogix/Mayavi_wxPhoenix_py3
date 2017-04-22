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


class ImageMask(ThreadedImageAlgorithm):
    """
    ImageMask - Combines a mask and an image.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageMask combines a mask with an image.  Non zero mask implies
    the output pixel will be the same as the image. If a mask pixel is
    zero,  then the output pixel is set to "_masked_value".  The filter
    also has the option to pass the mask through a boolean not operation
    before processing the image. This reverses the passed and replaced
    pixels. The two inputs should have the same "_whole_extent". The mask
    input should be unsigned char, and the image scalar type is the same
    as the output scalar type.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMask, obj, update, **traits)
    
    not_mask = tvtk_base.false_bool_trait(help=\
        """
        When Not Mask is on, the mask is passed through a boolean not
        before it is used to mask the image.  The effect is to pass the
        pixels where the input mask is zero, and replace the pixels where
        the input value is non zero.
        """
    )

    def _not_mask_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNotMask,
                        self.not_mask_)

    mask_alpha = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the alpha blending value for the mask The input image is
        assumed to be at alpha = 1.0 and the mask image uses this alpha
        to blend using an over operator.
        """
    )

    def _mask_alpha_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaskAlpha,
                        self.mask_alpha)

    def get_masked_output_value(self):
        """
        V.get_masked_output_value() -> (float, ...)
        C++: double *GetMaskedOutputValue()"""
        ret = self._vtk_obj.GetMaskedOutputValue()
        return ret
        

    def set_masked_output_value(self, *args):
        """
        V.set_masked_output_value(int, [float, ...])
        C++: void SetMaskedOutputValue(int num, double *v)
        V.set_masked_output_value(float)
        C++: void SetMaskedOutputValue(double v)
        V.set_masked_output_value(float, float)
        C++: void SetMaskedOutputValue(double v1, double v2)
        V.set_masked_output_value(float, float, float)
        C++: void SetMaskedOutputValue(double v1, double v2, double v3)
        set_get the value of the output pixel replaced by mask.
        """
        ret = self._wrap_call(self._vtk_obj.SetMaskedOutputValue, *args)
        return ret

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

    def _get_masked_output_value_length(self):
        return self._vtk_obj.GetMaskedOutputValueLength()
    masked_output_value_length = traits.Property(_get_masked_output_value_length, help=\
        """
        
        """
    )

    def set_image_input_data(self, *args):
        """
        V.set_image_input_data(ImageData)
        C++: void SetImageInputData(ImageData *in)
        Set the input to be masked.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetImageInputData, *my_args)
        return ret

    def set_input1data(self, *args):
        """
        V.set_input1data(DataObject)
        C++: virtual void SetInput1Data(DataObject *in)
        Set the two inputs to this filter
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput1Data, *my_args)
        return ret

    def set_input2data(self, *args):
        """
        V.set_input2data(DataObject)
        C++: virtual void SetInput2Data(DataObject *in)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput2Data, *my_args)
        return ret

    def set_mask_input_data(self, *args):
        """
        V.set_mask_input_data(ImageData)
        C++: void SetMaskInputData(ImageData *in)
        Set the mask to be used.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetMaskInputData, *my_args)
        return ret

    _updateable_traits_ = \
    (('not_mask', 'GetNotMask'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('split_mode',
    'GetSplitMode'), ('mask_alpha', 'GetMaskAlpha'),
    ('desired_bytes_per_piece', 'GetDesiredBytesPerPiece'), ('enable_smp',
    'GetEnableSMP'), ('global_default_enable_smp',
    'GetGlobalDefaultEnableSMP'), ('minimum_piece_size',
    'GetMinimumPieceSize'), ('number_of_threads', 'GetNumberOfThreads'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'not_mask',
    'release_data_flag', 'split_mode', 'desired_bytes_per_piece',
    'enable_smp', 'global_default_enable_smp', 'mask_alpha',
    'minimum_piece_size', 'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageMask, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMask properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['not_mask'], ['split_mode'], ['desired_bytes_per_piece',
            'enable_smp', 'global_default_enable_smp', 'mask_alpha',
            'minimum_piece_size', 'number_of_threads']),
            title='Edit ImageMask properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMask properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


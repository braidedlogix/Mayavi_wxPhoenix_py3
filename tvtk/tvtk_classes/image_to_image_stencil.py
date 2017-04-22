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

from tvtk.tvtk_classes.image_stencil_algorithm import ImageStencilAlgorithm


class ImageToImageStencil(ImageStencilAlgorithm):
    """
    ImageToImageStencil - clip an image with a mask image
    
    Superclass: ImageStencilAlgorithm
    
    ImageToImageStencil will convert a ImageData into an stencil
    that can be used with ImageStecil or other vtk classes that apply
    a stencil to an image.
    @sa
    ImageStencil ImplicitFunctionToImageStencil
    PolyDataToImageStencil
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageToImageStencil, obj, update, **traits)
    
    lower_threshold = traits.Float(-9.999999680285692e+37, enter_set=True, auto_set=False, help=\
        """
        Get the Upper and Lower thresholds.
        """
    )

    def _lower_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLowerThreshold,
                        self.lower_threshold)

    upper_threshold = traits.Float(9.999999680285692e+37, enter_set=True, auto_set=False, help=\
        """
        Get the Upper and Lower thresholds.
        """
    )

    def _upper_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUpperThreshold,
                        self.upper_threshold)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Specify the image data to convert into a stencil.
        """
    )

    def set_input_data(self, *args):
        """
        V.set_input_data(ImageData)
        C++: void SetInputData(ImageData *input)
        Specify the image data to convert into a stencil.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    def threshold_between(self, *args):
        """
        V.threshold_between(float, float)
        C++: void ThresholdBetween(double lower, double upper)
        The values in a range (inclusive) match
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdBetween, *args)
        return ret

    def threshold_by_lower(self, *args):
        """
        V.threshold_by_lower(float)
        C++: void ThresholdByLower(double thresh)
        The values less than or equal to the value match.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdByLower, *args)
        return ret

    def threshold_by_upper(self, *args):
        """
        V.threshold_by_upper(float)
        C++: void ThresholdByUpper(double thresh)
        The values greater than or equal to the value match.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdByUpper, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('lower_threshold', 'GetLowerThreshold'), ('upper_threshold',
    'GetUpperThreshold'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'lower_threshold', 'progress_text',
    'upper_threshold'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageToImageStencil, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageToImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['lower_threshold', 'upper_threshold']),
            title='Edit ImageToImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageToImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


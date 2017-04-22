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


class ImageConvolve(ThreadedImageAlgorithm):
    """
    ImageConvolve - Convolution of an image with a kernel.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageConvolve convolves the image with a 3d nx_nx_n kernel or a 2d
    nx_n kernal.  The output image is cropped to the same size as the
    input.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageConvolve, obj, update, **traits)
    
    kernel3x3 = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(9,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Set the kernel to be a given 3x3 or 5x5 or 7x7 kernel.
        """
    )

    def _kernel3x3_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKernel3x3,
                        self.kernel3x3)

    kernel3x3x3 = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(27,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Set the kernel to be a 3x3x3 or 5x5x5 or 7x7x7 kernel.
        """
    )

    def _kernel3x3x3_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKernel3x3x3,
                        self.kernel3x3x3)

    kernel5x5 = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(25,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Set the kernel to be a given 3x3 or 5x5 or 7x7 kernel.
        """
    )

    def _kernel5x5_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKernel5x5,
                        self.kernel5x5)

    kernel5x5x5 = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(125,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _kernel5x5x5_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKernel5x5x5,
                        self.kernel5x5x5)

    kernel7x7 = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(49,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _kernel7x7_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKernel7x7,
                        self.kernel7x7)

    def _get_kernel7x7x7(self):
        return self._vtk_obj.GetKernel7x7x7()
    def _set_kernel7x7x7(self, arg):
        old_val = self._get_kernel7x7x7()
        self._wrap_call(self._vtk_obj.SetKernel7x7x7,
                        arg)
        self.trait_property_changed('kernel7x7x7', old_val, arg)
    kernel7x7x7 = traits.Property(_get_kernel7x7x7, _set_kernel7x7x7, help=\
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

    def _get_kernel_size(self):
        return self._vtk_obj.GetKernelSize()
    kernel_size = traits.Property(_get_kernel_size, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('split_mode',
    'GetSplitMode'), ('desired_bytes_per_piece',
    'GetDesiredBytesPerPiece'), ('enable_smp', 'GetEnableSMP'),
    ('global_default_enable_smp', 'GetGlobalDefaultEnableSMP'),
    ('minimum_piece_size', 'GetMinimumPieceSize'), ('number_of_threads',
    'GetNumberOfThreads'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'split_mode', 'desired_bytes_per_piece',
    'enable_smp', 'global_default_enable_smp', 'minimum_piece_size',
    'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageConvolve, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageConvolve properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['split_mode'], ['desired_bytes_per_piece', 'enable_smp',
            'global_default_enable_smp', 'minimum_piece_size',
            'number_of_threads']),
            title='Edit ImageConvolve properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageConvolve properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


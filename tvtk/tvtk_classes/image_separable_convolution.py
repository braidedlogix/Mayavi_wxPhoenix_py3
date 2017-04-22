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

from tvtk.tvtk_classes.image_decompose_filter import ImageDecomposeFilter


class ImageSeparableConvolution(ImageDecomposeFilter):
    """
    ImageSeparableConvolution - 3 1d convolutions on an image
    
    Superclass: ImageDecomposeFilter
    
    ImageSeparableConvolution performs a convolution along the X, Y,
    and Z axes of an image, based on the three different 1d convolution
    kernels.  The kernels must be of odd size, and are considered to be
    centered at (int)((kernelsize - 1) / 2.0 ).  If a kernel is NULL,
    that dimension is skipped.  This filter is designed to efficiently
    convolve separable filters that can be decomposed into 1 or more 1d
    convolutions.  It also handles arbitrarly large kernel sizes, and
    uses edge replication to handle boundaries.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageSeparableConvolution, obj, update, **traits)
    
    def _get_x_kernel(self):
        return wrap_vtk(self._vtk_obj.GetXKernel())
    def _set_x_kernel(self, arg):
        old_val = self._get_x_kernel()
        my_arg = deref_array([arg], [['vtkFloatArray']])
        self._wrap_call(self._vtk_obj.SetXKernel,
                        my_arg[0])
        self.trait_property_changed('x_kernel', old_val, arg)
    x_kernel = traits.Property(_get_x_kernel, _set_x_kernel, help=\
        """
        
        """
    )

    def _get_y_kernel(self):
        return wrap_vtk(self._vtk_obj.GetYKernel())
    def _set_y_kernel(self, arg):
        old_val = self._get_y_kernel()
        my_arg = deref_array([arg], [['vtkFloatArray']])
        self._wrap_call(self._vtk_obj.SetYKernel,
                        my_arg[0])
        self.trait_property_changed('y_kernel', old_val, arg)
    y_kernel = traits.Property(_get_y_kernel, _set_y_kernel, help=\
        """
        
        """
    )

    def _get_z_kernel(self):
        return wrap_vtk(self._vtk_obj.GetZKernel())
    def _set_z_kernel(self, arg):
        old_val = self._get_z_kernel()
        my_arg = deref_array([arg], [['vtkFloatArray']])
        self._wrap_call(self._vtk_obj.SetZKernel,
                        my_arg[0])
        self.trait_property_changed('z_kernel', old_val, arg)
    z_kernel = traits.Property(_get_z_kernel, _set_z_kernel, help=\
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

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('split_mode',
    'GetSplitMode'), ('dimensionality', 'GetDimensionality'),
    ('desired_bytes_per_piece', 'GetDesiredBytesPerPiece'), ('enable_smp',
    'GetEnableSMP'), ('global_default_enable_smp',
    'GetGlobalDefaultEnableSMP'), ('minimum_piece_size',
    'GetMinimumPieceSize'), ('number_of_threads', 'GetNumberOfThreads'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'split_mode', 'desired_bytes_per_piece',
    'dimensionality', 'enable_smp', 'global_default_enable_smp',
    'minimum_piece_size', 'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageSeparableConvolution, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageSeparableConvolution properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['split_mode'], ['desired_bytes_per_piece',
            'dimensionality', 'enable_smp', 'global_default_enable_smp',
            'minimum_piece_size', 'number_of_threads']),
            title='Edit ImageSeparableConvolution properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageSeparableConvolution properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


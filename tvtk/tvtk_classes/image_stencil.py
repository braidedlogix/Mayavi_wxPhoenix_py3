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


class ImageStencil(ThreadedImageAlgorithm):
    """
    ImageStencil - combine images via a cookie-cutter operation
    
    Superclass: ThreadedImageAlgorithm
    
    ImageStencil will combine two images together using a stencil. The
    stencil should be provided in the form of a ImageStencilData,
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageStencil, obj, update, **traits)
    
    reverse_stencil = tvtk_base.false_bool_trait(help=\
        """
        Reverse the stencil.
        """
    )

    def _reverse_stencil_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReverseStencil,
                        self.reverse_stencil_)

    background_color = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(1.0, 1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _background_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundColor,
                        self.background_color)

    background_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the default output value to use when the second input is not
        set.
        """
    )

    def _background_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundValue,
                        self.background_value)

    def _get_background_input(self):
        return wrap_vtk(self._vtk_obj.GetBackgroundInput())
    background_input = traits.Property(_get_background_input, help=\
        """
        Set the second input.  This image will be used for the 'outside'
        of the stencil.  If not set, the output voxels will be filled
        with background_value instead.
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
        Specify the stencil to use.  The stencil can be created from a
        ImplicitFunction or a PolyData. This function does not
        setup a pipeline connection.
        """
    )

    def set_background_input_data(self, *args):
        """
        V.set_background_input_data(ImageData)
        C++: virtual void SetBackgroundInputData(ImageData *input)
        Set the second input.  This image will be used for the 'outside'
        of the stencil.  If not set, the output voxels will be filled
        with background_value instead.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetBackgroundInputData, *my_args)
        return ret

    def set_stencil_connection(self, *args):
        """
        V.set_stencil_connection(AlgorithmOutput)
        C++: void SetStencilConnection(AlgorithmOutput *outputPort)
        Specify the stencil to use. This sets up a pipeline connection.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetStencilConnection, *my_args)
        return ret

    def set_stencil_data(self, *args):
        """
        V.set_stencil_data(ImageStencilData)
        C++: virtual void SetStencilData(ImageStencilData *stencil)
        Specify the stencil to use.  The stencil can be created from a
        ImplicitFunction or a PolyData. This function does not
        setup a pipeline connection.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetStencilData, *my_args)
        return ret

    _updateable_traits_ = \
    (('reverse_stencil', 'GetReverseStencil'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('split_mode', 'GetSplitMode'),
    ('background_color', 'GetBackgroundColor'), ('background_value',
    'GetBackgroundValue'), ('desired_bytes_per_piece',
    'GetDesiredBytesPerPiece'), ('enable_smp', 'GetEnableSMP'),
    ('global_default_enable_smp', 'GetGlobalDefaultEnableSMP'),
    ('minimum_piece_size', 'GetMinimumPieceSize'), ('number_of_threads',
    'GetNumberOfThreads'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'reverse_stencil', 'split_mode',
    'background_color', 'background_value', 'desired_bytes_per_piece',
    'enable_smp', 'global_default_enable_smp', 'minimum_piece_size',
    'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageStencil, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['reverse_stencil'], ['split_mode'], ['background_color',
            'background_value', 'desired_bytes_per_piece', 'enable_smp',
            'global_default_enable_smp', 'minimum_piece_size',
            'number_of_threads']),
            title='Edit ImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


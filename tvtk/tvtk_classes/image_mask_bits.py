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


class ImageMaskBits(ThreadedImageAlgorithm):
    """
    ImageMaskBits - applies a bit-mask pattern to each component.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageMaskBits applies a bit-mask pattern to each component.  The
    bit-mask can be applied using a variety of boolean bitwise operators.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMaskBits, obj, update, **traits)
    
    operation = traits.Trait('and_',
    tvtk_base.TraitRevPrefixMap({'and_': 0, 'nand': 3, 'nor': 4, 'or_': 1, 'xor': 2}), help=\
        """
        Set/Get the boolean operator. Default is AND.
        """
    )

    def _operation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOperation,
                        self.operation_)

    masks = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=int, value=(4294967295, 4294967295, 4294967295, 4294967295), cols=3, help=\
        """
        
        """
    )

    def _masks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMasks,
                        self.masks)

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

    def set_mask(self, *args):
        """
        V.set_mask(int)
        C++: void SetMask(unsigned int mask)
        Set/Get the bit-masks. Default is 0xffffffff.
        """
        ret = self._wrap_call(self._vtk_obj.SetMask, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('operation',
    'GetOperation'), ('split_mode', 'GetSplitMode'), ('masks',
    'GetMasks'), ('desired_bytes_per_piece', 'GetDesiredBytesPerPiece'),
    ('enable_smp', 'GetEnableSMP'), ('global_default_enable_smp',
    'GetGlobalDefaultEnableSMP'), ('minimum_piece_size',
    'GetMinimumPieceSize'), ('number_of_threads', 'GetNumberOfThreads'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'operation', 'split_mode',
    'desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
    'masks', 'minimum_piece_size', 'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageMaskBits, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMaskBits properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['operation', 'split_mode'], ['desired_bytes_per_piece',
            'enable_smp', 'global_default_enable_smp', 'masks',
            'minimum_piece_size', 'number_of_threads']),
            title='Edit ImageMaskBits properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMaskBits properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


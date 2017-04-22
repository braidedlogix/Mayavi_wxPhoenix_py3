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

from tvtk.tvtk_classes.object import Object


class OutputStream(Object):
    """
    OutputStream - Wraps a binary output stream with a VTK interface.
    
    Superclass: Object
    
    OutputStream provides a VTK-style interface wrapping around a
    standard output stream.  The access methods are virtual so that
    subclasses can transparently provide encoding of the output.  Data
    lengths for Write calls refer to the length of the data in memory.
    The actual length in the stream may differ for subclasses that
    implement an encoding scheme.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOutputStream, obj, update, **traits)
    
    def end_writing(self):
        """
        V.end_writing() -> int
        C++: virtual int EndWriting()
        Called after all desired calls to Write have been made.  After
        this call, the caller is free to change the position of the
        stream.  Additional writes should not be done until after another
        call to start_writing.
        """
        ret = self._vtk_obj.EndWriting()
        return ret
        

    def start_writing(self):
        """
        V.start_writing() -> int
        C++: virtual int StartWriting()
        Called after the stream position has been set by the caller, but
        before any Write calls.  The stream position should not be
        adjusted by the caller until after an end_writing call.
        """
        ret = self._vtk_obj.StartWriting()
        return ret
        

    def write(self, *args):
        """
        V.write(void, int) -> int
        C++: virtual int Write(void const *data, size_t length)
        Write output data of the given length.
        """
        ret = self._wrap_call(self._vtk_obj.Write, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OutputStream, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OutputStream properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit OutputStream properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OutputStream properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


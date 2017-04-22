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


class OpenGLBufferObject(Object):
    """
    OpenGLBufferObject - open_gl buffer object
    
    Superclass: Object
    
    open_gl buffer object to store index, geometry and/or attribute data
    on the GPU.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLBufferObject, obj, update, **traits)
    
    def _get_error(self):
        return self._vtk_obj.GetError()
    error = traits.Property(_get_error, help=\
        """
        Return a string describing errors.
        """
    )

    def _get_handle(self):
        return self._vtk_obj.GetHandle()
    handle = traits.Property(_get_handle, help=\
        """
        Get the handle of the buffer object.
        """
    )

    def bind(self):
        """
        V.bind() -> bool
        C++: bool Bind()
        Bind the buffer object ready for rendering.
        
        ote Only one ARRAY_BUFFER and one ELEMENT_ARRAY_BUFFER may be
        bound at any time.
        """
        ret = self._vtk_obj.Bind()
        return ret
        

    def generate_buffer(self, *args):
        """
        V.generate_buffer(ObjectType) -> bool
        C++: bool GenerateBuffer(ObjectType type)
        Generate the the opengl buffer for this Handle
        """
        ret = self._wrap_call(self._vtk_obj.GenerateBuffer, *args)
        return ret

    def is_ready(self):
        """
        V.is_ready() -> bool
        C++: bool IsReady()
        Determine if the buffer object is ready to be used.
        """
        ret = self._vtk_obj.IsReady()
        return ret
        

    def release(self):
        """
        V.release() -> bool
        C++: bool Release()
        Release the buffer. This should be done after rendering is
        complete.
        """
        ret = self._vtk_obj.Release()
        return ret
        

    def release_graphics_resources(self):
        """
        V.release_graphics_resources()
        C++: void ReleaseGraphicsResources()
        Release any graphics resources that are being consumed by this
        class.
        """
        ret = self._vtk_obj.ReleaseGraphicsResources()
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
            return super(OpenGLBufferObject, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit OpenGLBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


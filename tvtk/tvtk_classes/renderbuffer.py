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


class Renderbuffer(Object):
    """
    Renderbuffer - Storage for FBO's
    
    Superclass: Object
    
    Lightweight API to open_gl Framebuffer Object EXT renderbuffers.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderbuffer, obj, update, **traits)
    
    def _get_context(self):
        return wrap_vtk(self._vtk_obj.GetContext())
    def _set_context(self, arg):
        old_val = self._get_context()
        self._wrap_call(self._vtk_obj.SetContext,
                        deref_vtk(arg))
        self.trait_property_changed('context', old_val, arg)
    context = traits.Property(_get_context, _set_context, help=\
        """
        Setting the context has the side affect of initializing open_gl
        required extensions and allocates an open_gl name(handle) that is
        released when the object is destroyed. NOTE: the reference count
        to the passed in object is not incremented. Contex must be set
        prior to other use.
        """
    )

    def _get_handle(self):
        return self._vtk_obj.GetHandle()
    handle = traits.Property(_get_handle, help=\
        """
        Get the name of the buffer for use opengl code.
        """
    )

    def create(self, *args):
        """
        V.create(int, int, int) -> int
        C++: int Create(unsigned int format, unsigned int width,
            unsigned int height)
        Sets up an renderbufffer. Use mode to control READ or DRAW
        operation and format to control the internal format. (see open_gl
        doc for more info)
        """
        ret = self._wrap_call(self._vtk_obj.Create, *args)
        return ret

    def create_color_attachment(self, *args):
        """
        V.create_color_attachment(int, int) -> int
        C++: int CreateColorAttachment(unsigned int width,
            unsigned int height)
        Sets up an RGBAF renderbufffer for use as a color attachment. Use
        mode to control READ or DRAW operation.
        """
        ret = self._wrap_call(self._vtk_obj.CreateColorAttachment, *args)
        return ret

    def create_depth_attachment(self, *args):
        """
        V.create_depth_attachment(int, int) -> int
        C++: int CreateDepthAttachment(unsigned int width,
            unsigned int height)
        Sets up an DEPTH renderbufffer for use as a color attachment. Use
        mode to control READ or DRAW operation.
        """
        ret = self._wrap_call(self._vtk_obj.CreateDepthAttachment, *args)
        return ret

    def is_supported(self, *args):
        """
        V.is_supported(RenderWindow) -> bool
        C++: static bool IsSupported(RenderWindow *renWin)
        Returns if the context supports the required extensions.
        Extension will be loaded when the conetxt is set.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsSupported, *my_args)
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
            return super(Renderbuffer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Renderbuffer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit Renderbuffer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Renderbuffer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class AbstractRenderDevice(Object):
    """
    AbstractRenderDevice - no description provided.
    
    Superclass: Object
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractRenderDevice, obj, update, **traits)
    
    def create_new_window(self, *args):
        """
        V.create_new_window(Recti, string) -> bool
        C++: virtual bool CreateNewWindow(const Recti &geometry,
            const std::string &name)
        Create a window with the desired geometry.
        @param geometry The geometry in screen coordinates for the
            window.
        @return True on success, false on failure.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CreateNewWindow, *my_args)
        return ret

    def make_current(self):
        """
        V.make_current()
        C++: virtual void MakeCurrent()
        Make the context current so that it can be used by open_gl. This
            is
        an expensive call, and so its use should be minimized to once per
        render ideally.
        """
        ret = self._vtk_obj.MakeCurrent()
        return ret
        

    def set_requested_gl_version(self, *args):
        """
        V.set_requested_gl_version(int, int)
        C++: void SetRequestedGLVersion(int major, int minor)
        Set the context that should be requested (must be set before the
        widget is rendered for the first time.
        @param major Major GL version, default is 2.
        @param minor Minor GL version, default is 1.
        """
        ret = self._wrap_call(self._vtk_obj.SetRequestedGLVersion, *args)
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
            return super(AbstractRenderDevice, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractRenderDevice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit AbstractRenderDevice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractRenderDevice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


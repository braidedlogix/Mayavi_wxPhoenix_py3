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


class RenderWidget(Object):
    """
    RenderWidget - no description provided.
    
    Superclass: Object
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderWidget, obj, update, **traits)
    
    name = traits.String('New VTK RenderWidget!!!', enter_set=True, auto_set=False, help=\
        """
        Set the name of the widget.
        @param name The name to set to the window.
        """
    )

    def _name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetName,
                        self.name)

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()"""
        ret = self._vtk_obj.Initialize()
        return ret
        

    def make_current(self):
        """
        V.make_current()
        C++: virtual void MakeCurrent()
        Make the widget's context current, this will defer to the OS
        specific methods, and calls should be kept to a minimum as they
        are quite expensive.
        """
        ret = self._vtk_obj.MakeCurrent()
        return ret
        

    def render(self):
        """
        V.render()
        C++: virtual void Render()
        Render everything in the current widget.
        """
        ret = self._vtk_obj.Render()
        return ret
        

    def start(self):
        """
        V.start()
        C++: void Start()"""
        ret = self._vtk_obj.Start()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('name', 'GetName'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['name']),
            title='Edit RenderWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


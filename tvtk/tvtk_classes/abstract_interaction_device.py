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


class AbstractInteractionDevice(Object):
    """
    AbstractInteractionDevice - no description provided.
    
    Superclass: Object
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractInteractionDevice, obj, update, **traits)
    
    def _get_render_device(self):
        return wrap_vtk(self._vtk_obj.GetRenderDevice())
    def _set_render_device(self, arg):
        old_val = self._get_render_device()
        self._wrap_call(self._vtk_obj.SetRenderDevice,
                        deref_vtk(arg))
        self.trait_property_changed('render_device', old_val, arg)
    render_device = traits.Property(_get_render_device, _set_render_device, help=\
        """
        
        """
    )

    def _get_render_widget(self):
        return wrap_vtk(self._vtk_obj.GetRenderWidget())
    def _set_render_widget(self, arg):
        old_val = self._get_render_widget()
        self._wrap_call(self._vtk_obj.SetRenderWidget,
                        deref_vtk(arg))
        self.trait_property_changed('render_widget', old_val, arg)
    render_widget = traits.Property(_get_render_widget, _set_render_widget, help=\
        """
        
        """
    )

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()
        Initialize the interaction device.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def process_events(self):
        """
        V.process_events()
        C++: virtual void ProcessEvents()
        Process any pending events, this can be used to process OS level
        events without running a full event loop.
        """
        ret = self._vtk_obj.ProcessEvents()
        return ret
        

    def start(self):
        """
        V.start()
        C++: virtual void Start()
        Start the event loop.
        """
        ret = self._vtk_obj.Start()
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
            return super(AbstractInteractionDevice, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractInteractionDevice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit AbstractInteractionDevice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractInteractionDevice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


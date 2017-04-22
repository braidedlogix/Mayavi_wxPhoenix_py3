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

from tvtk.tvtk_classes.command import Command


class EventForwarderCommand(Command):
    """
    EventForwarderCommand - a simple event forwarder command
    
    Superclass: Command
    
    Use EventForwarderCommand to forward an event to a new object.
    This command will intercept the event, and use invoke_event on a
    'target' as if that object was the one that invoked the event instead
    of the object this commmand was attached to using add_observer.
    
    @sa
    Command
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEventForwarderCommand, obj, update, **traits)
    
    def _get_target(self):
        return self._vtk_obj.GetTarget()
    def _set_target(self, arg):
        old_val = self._get_target()
        self._wrap_call(self._vtk_obj.SetTarget,
                        deref_vtk(arg))
        self.trait_property_changed('target', old_val, arg)
    target = traits.Property(_get_target, _set_target, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('abort_flag', 'GetAbortFlag'), ('passive_observer',
    'GetPassiveObserver'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_flag', 'passive_observer'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EventForwarderCommand, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit EventForwarderCommand properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['abort_flag', 'passive_observer'], [], []),
            title='Edit EventForwarderCommand properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EventForwarderCommand properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


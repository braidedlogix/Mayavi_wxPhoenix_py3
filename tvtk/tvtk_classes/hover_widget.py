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

from tvtk.tvtk_classes.abstract_widget import AbstractWidget


class HoverWidget(AbstractWidget):
    """
    HoverWidget - invoke a TimerEvent when hovering
    
    Superclass: AbstractWidget
    
    The HoverWidget is used to invoke an event when hovering in a
    render window. Hovering occurs when mouse motion (in the render
    window) does not occur for a specified amount of time (i.e.,
    timer_duration). This class can be used as is (by observing
    timer_events) or for class derivation for those classes wishing to do
    more with the hover event.
    
    To use this widget, specify an instance of HoverWidget and specify
    the time (in milliseconds) defining the hover period. Unlike most
    widgets, this widget does not require a representation (although
    subclasses like BalloonWidget do require a representation).
    
    @par Event Bindings: By default, the widget observes the following
    VTK events (i.e., it watches the RenderWindowInteractor for these
    events):
    
    
      mouse_move_event - manages a timer used to determine whether the
    mouse
                       is hovering.
      timer_event - when the time between events (e.g., mouse move), then
    a
                   timer event is invoked.
      key_press_event - when the "Enter" key is pressed after the balloon
    appears,
                      a callback is activated (e.g.,
    widget_activate_event). 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's WidgetEventTranslator. This class
    translates VTK events into the HoverWidget's widget events:
    
    
      WidgetEvent::Move -- start (or reset) the timer
      WidgetEvent::TimedOut -- when enough time is elapsed between
    defined
                                  VTK events the hover event is invoked.
      WidgetEvent::SelectAction -- activate any callbacks associated
                                      with the balloon. 
    
    @par Event Bindings: This widget invokes the following VTK events on
    itself when the widget determines that it is hovering. Note that
    observers of this widget can listen for these events and take
    appropriate action.
    
    
      Command::TimerEvent (when hovering is determined to occur)
      Command::EndInteractionEvent (after a hover has occurred and the
                                       mouse begins moving again).
      Command::WidgetActivateEvent (when the balloon is selected with
    a
                                       keypress). 
    
    @sa
    AbstractWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHoverWidget, obj, update, **traits)
    
    timer_duration = traits.Trait(250, traits.Range(1, 100000, enter_set=True, auto_set=False), help=\
        """
        Specify the hovering interval (in milliseconds). If after moving
        the mouse the pointer stays over a Prop for this duration,
        then a TimerEvent::TimerEvent is invoked.
        """
    )

    def _timer_duration_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimerDuration,
                        self.timer_duration)

    _updateable_traits_ = \
    (('manages_cursor', 'GetManagesCursor'), ('process_events',
    'GetProcessEvents'), ('enabled', 'GetEnabled'),
    ('key_press_activation', 'GetKeyPressActivation'), ('picking_managed',
    'GetPickingManaged'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('timer_duration', 'GetTimerDuration'), ('priority', 'GetPriority'),
    ('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'manages_cursor', 'picking_managed',
    'process_events', 'key_press_activation_value', 'priority',
    'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HoverWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HoverWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'manages_cursor',
            'picking_managed', 'process_events'], [],
            ['key_press_activation_value', 'priority', 'timer_duration']),
            title='Edit HoverWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HoverWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


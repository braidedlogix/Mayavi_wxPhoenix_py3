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


class FinitePlaneWidget(AbstractWidget):
    """
    FinitePlaneWidget - 3d widget for manipulating a finite plane
    
    Superclass: AbstractWidget
    
    This 3d widget interacts with a FinitePlaneRepresentation class
    (i.e., it handles the events that drive its corresponding
    representation). This 3d widget defines a finite plane that can be
    interactively placed in a scene. The widget is assumed to consist of
    four parts: 1) a plane with 2) a normal and 3) three handles that can
    be moused on and manipulated. The green and red handles represent the
    semi finite plane definition, the third is in the center of the
    plane. Operation like rotation of the plane (using normal), origin
    translation and geometry plane modification using green and red
    handles are availables.
    
    To use this widget, you generally pair it with a
    FinitePlaneRepresentation (or a subclass). Various options are
    available in the representation for controlling how the widget
    appears, and how the widget reacts.
    
    @par Event Bindings: By default, the widget responds to the following
    VTK events (i.e., it watches the RenderWindowInteractor for these
    events):
    
    If one of the 3 handles are selected:
      left_button_press_event - select the appropriate handle
      left_button_release_event - release the currently selected handle
      mouse_move_event - move the handle In all the cases, independent of
    what is picked, the widget responds to the following VTK events:
      left_button_press_event - start select action
      left_button_release_event - stop select action 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's WidgetEventTranslator. This class
    translates VTK events into the FinitePlaneWidget's widget events:
    
    
      WidgetEvent::Select -- some part of the widget has been selected
      WidgetEvent::EndSelect -- the selection process has completed
      WidgetEvent::Move -- a request for motion has been invoked 
    
    @par Event Bindings: In turn, when these widget events are processed,
    the FinitePlaneWidget invokes the following VTK events on itself
    (which observers can listen for):
    
    
      Command::StartInteractionEvent (on WidgetEvent::Select)
      Command::EndInteractionEvent (on WidgetEvent::EndSelect)
      Command::InteractionEvent (on WidgetEvent::Move) 
    @sa
    FinitePlaneRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFinitePlaneWidget, obj, update, **traits)
    
    def _get_representation(self):
        return wrap_vtk(self._vtk_obj.GetRepresentation())
    def _set_representation(self, arg):
        old_val = self._get_representation()
        self._wrap_call(self._vtk_obj.SetRepresentation,
                        deref_vtk(arg))
        self.trait_property_changed('representation', old_val, arg)
    representation = traits.Property(_get_representation, _set_representation, help=\
        """
        Return an instance of WidgetRepresentation used to represent
        this widget in the scene. Note that the representation is a
        subclass of Prop (typically a subclass of
        WidgetRepresenation) so it can be added to the renderer
        independent of the widget.
        """
    )

    _updateable_traits_ = \
    (('manages_cursor', 'GetManagesCursor'), ('process_events',
    'GetProcessEvents'), ('enabled', 'GetEnabled'),
    ('key_press_activation', 'GetKeyPressActivation'), ('picking_managed',
    'GetPickingManaged'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('priority',
    'GetPriority'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'manages_cursor', 'picking_managed',
    'process_events', 'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FinitePlaneWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FinitePlaneWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'manages_cursor',
            'picking_managed', 'process_events'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit FinitePlaneWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FinitePlaneWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


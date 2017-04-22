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


class AngleWidget(AbstractWidget):
    """
    AngleWidget - measure the angle between two rays (defined by three
    points)
    
    Superclass: AbstractWidget
    
    The AngleWidget is used to measure the angle between two rays
    (defined by three points). The three points (two end points and a
    center) can be positioned independently, and when they are released,
    a special place_point_event is invoked so that special operations may
    be take to reposition the point (snap to grid, etc.) The widget has
    two different modes of interaction: when initially defined (i.e.,
    placing the three points) and then a manipulate mode (adjusting the
    position of the three points).
    
    To use this widget, specify an instance of AngleWidget and a
    representation (a subclass of AngleRepresentation). The widget is
    implemented using three instances of HandleWidget which are used
    to position the three points. The representations for these handle
    widgets are provided by the AngleRepresentation.
    
    @par Event Bindings: By default, the widget responds to the following
    VTK events (i.e., it watches the RenderWindowInteractor for these
    events):
    
    
      left_button_press_event - add a point or select a handle
      mouse_move_event - position the second or third point, or move a
    handle
      left_button_release_event - release the selected handle 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's WidgetEventTranslator. This class
    translates VTK events into the AngleWidget's widget events:
    
    
      WidgetEvent::AddPoint -- add one point; depending on the state
                                  it may the first, second or third point
                                  added. Or, if near a handle, select the
    handle.
      WidgetEvent::Move -- position the second or third point, or move
    the
                              handle depending on the state.
      WidgetEvent::EndSelect -- the handle manipulation process has
    completed. 
    
    @par Event Bindings: This widget invokes the following VTK events on
    itself (which observers can listen for):
    
    
      Command::StartInteractionEvent (beginning to interact)
      Command::EndInteractionEvent (completing interaction)
      Command::InteractionEvent (moving a handle)
      Command::PlacePointEvent (after a point is positioned;
                                   call data includes handle id (0,1,2)) 
    
    @sa
    HandleWidget DistanceWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAngleWidget, obj, update, **traits)
    
    def get_widget_state(self):
        """
        V.get_widget_state() -> int
        C++: virtual int GetWidgetState()
        Return the current widget state.
        """
        ret = self._vtk_obj.GetWidgetState()
        return ret
        

    def set_widget_state_to_manipulate(self):
        """
        V.set_widget_state_to_manipulate()
        C++: virtual void SetWidgetStateToManipulate()
        Set the state of the widget. If the state is set to "Manipulate"
        then it is assumed that the widget and its representation will be
        initialized programmatically and is not interactively placed.
        Initially the widget state is set to "Start" which means nothing
        will appear and the user must interactively place the widget with
        repeated mouse selections. Set the state to "Start" if you want
        interactive placement. Generally state changes must be followed
        by a Render() for things to visually take effect.
        """
        self._vtk_obj.SetWidgetStateToManipulate()

    def set_widget_state_to_start(self):
        """
        V.set_widget_state_to_start()
        C++: virtual void SetWidgetStateToStart()
        Set the state of the widget. If the state is set to "Manipulate"
        then it is assumed that the widget and its representation will be
        initialized programmatically and is not interactively placed.
        Initially the widget state is set to "Start" which means nothing
        will appear and the user must interactively place the widget with
        repeated mouse selections. Set the state to "Start" if you want
        interactive placement. Generally state changes must be followed
        by a Render() for things to visually take effect.
        """
        self._vtk_obj.SetWidgetStateToStart()

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

    def _get_angle_representation(self):
        return wrap_vtk(self._vtk_obj.GetAngleRepresentation())
    angle_representation = traits.Property(_get_angle_representation, help=\
        """
        Return the representation as a AngleRepresentation.
        """
    )

    def is_angle_valid(self):
        """
        V.is_angle_valid() -> int
        C++: int IsAngleValid()
        A flag indicates whether the angle is valid. The angle value only
        becomes valid after two of the three points are placed.
        """
        ret = self._vtk_obj.IsAngleValid()
        return ret
        

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
            return super(AngleWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AngleWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'manages_cursor',
            'picking_managed', 'process_events'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit AngleWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AngleWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


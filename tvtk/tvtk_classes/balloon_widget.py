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

from tvtk.tvtk_classes.hover_widget import HoverWidget


class BalloonWidget(HoverWidget):
    """
    BalloonWidget - popup text balloons above instance of Prop when
    hovering occurs
    
    Superclass: HoverWidget
    
    The BalloonWidget is used to popup text and/or an image when the
    mouse hovers over an instance of Prop. The widget keeps track of
    (vtk_prop,vtk_balloon) pairs (where the internal Balloon class is
    defined by a pair of StdString and ImageData), and when the
    mouse stops moving for a user-specified period of time over the
    Prop, then the Balloon is drawn nearby the Prop. Note that
    an instance of BalloonRepresentation is used to draw the balloon.
    
    To use this widget, specify an instance of BalloonWidget and a
    representation (e.g., BalloonRepresentation). Then list all
    instances of Prop, a text string, and/or an instance of
    ImageData to be associated with each Prop. (Note that you can
    specify both text and an image, or just one or the other.) You may
    also wish to specify the hover delay (i.e., set in the superclass
    HoverWidget).
    
    @par Event Bindings: By default, the widget observes the following
    VTK events (i.e., it watches the RenderWindowInteractor for these
    events):
    
    
      mouse_move_event - occurs when mouse is moved in render window.
      timer_event - occurs when the time between events (e.g., mouse move)
                   is greater than timer_duration.
      key_press_event - when the "Enter" key is pressed after the balloon
    appears,
                      a callback is activated (e.g.,
    widget_activate_event). 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's WidgetEventTranslator. This class
    translates VTK events into the BalloonWidget's widget events:
    
    
      WidgetEvent::Move -- start the timer
      WidgetEvent::TimedOut -- when hovering occurs,
      WidgetEvent::SelectAction -- activate any callbacks associated
                                      with the balloon. 
    
    @par Event Bindings: This widget invokes the following VTK events on
    itself (which observers can listen for):
    
    
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
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBalloonWidget, obj, update, **traits)
    
    def _get_picker(self):
        return wrap_vtk(self._vtk_obj.GetPicker())
    def _set_picker(self, arg):
        old_val = self._get_picker()
        self._wrap_call(self._vtk_obj.SetPicker,
                        deref_vtk(arg))
        self.trait_property_changed('picker', old_val, arg)
    picker = traits.Property(_get_picker, _set_picker, help=\
        """
        Set/Get the object used to perform pick operations. Since the
        BalloonWidget operates on Props, the picker must be a
        subclass of AbstractPropPicker. (Note: if not specified, an
        instance of PropPicker is used.)
        """
    )

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

    def get_balloon_image(self, *args):
        """
        V.get_balloon_image(Prop) -> ImageData
        C++: ImageData *GetBalloonImage(Prop *prop)
        Methods to retrieve the information associated with each Prop
        (i.e., the information that makes up each balloon). A NULL will
        be returned if the Prop does not exist, or if a string or
        image have not been associated with the specified Prop.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetBalloonImage, *my_args)
        return wrap_vtk(ret)

    def _get_balloon_representation(self):
        return wrap_vtk(self._vtk_obj.GetBalloonRepresentation())
    balloon_representation = traits.Property(_get_balloon_representation, help=\
        """
        Return the representation as a BalloonRepresentation.
        """
    )

    def get_balloon_string(self, *args):
        """
        V.get_balloon_string(Prop) -> string
        C++: const char *GetBalloonString(Prop *prop)
        Methods to retrieve the information associated with each Prop
        (i.e., the information that makes up each balloon). A NULL will
        be returned if the Prop does not exist, or if a string or
        image have not been associated with the specified Prop.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetBalloonString, *my_args)
        return ret

    def _get_current_prop(self):
        return wrap_vtk(self._vtk_obj.GetCurrentProp())
    current_prop = traits.Property(_get_current_prop, help=\
        """
        Return the current Prop that is being hovered over. Note that
        the value may be NULL (if hovering over nothing or the mouse is
        moving).
        """
    )

    def add_balloon(self, *args):
        """
        V.add_balloon(Prop, string, ImageData)
        C++: void AddBalloon(Prop *prop, const char *str,
            ImageData *img)
        V.add_balloon(Prop, string)
        C++: void AddBalloon(Prop *prop, const char *str)
        Add and remove text and/or an image to be associated with a
        Prop. You may add one or both of them.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddBalloon, *my_args)
        return ret

    def remove_balloon(self, *args):
        """
        V.remove_balloon(Prop)
        C++: void RemoveBalloon(Prop *prop)
        Add and remove text and/or an image to be associated with a
        Prop. You may add one or both of them.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveBalloon, *my_args)
        return ret

    def update_balloon_image(self, *args):
        """
        V.update_balloon_image(Prop, ImageData)
        C++: void UpdateBalloonImage(Prop *prop, ImageData *image)
        Update the balloon string or image. If the specified prop does
        not exist, then nothing is added not changed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UpdateBalloonImage, *my_args)
        return ret

    def update_balloon_string(self, *args):
        """
        V.update_balloon_string(Prop, string)
        C++: void UpdateBalloonString(Prop *prop, const char *str)
        Update the balloon string or image. If the specified prop does
        not exist, then nothing is added not changed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UpdateBalloonString, *my_args)
        return ret

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
            return super(BalloonWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BalloonWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'manages_cursor',
            'picking_managed', 'process_events'], [],
            ['key_press_activation_value', 'priority', 'timer_duration']),
            title='Edit BalloonWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BalloonWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


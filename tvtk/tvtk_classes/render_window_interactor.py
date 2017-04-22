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


class RenderWindowInteractor(Object):
    """
    RenderWindowInteractor - platform-independent render window
    interaction including picking and frame rate control.
    
    Superclass: Object
    
    RenderWindowInteractor provides a platform-independent interaction
    mechanism for mouse/key/time events. It serves as a base class for
    platform-dependent implementations that handle routing of
    mouse/key/timer messages to InteractorObserver and its subclasses.
    RenderWindowInteractor also provides controls for picking,
    rendering frame rate, and headlights.
    
    RenderWindowInteractor has changed from previous implementations
    and now serves only as a shell to hold user preferences and route
    messages to InteractorStyle. Callbacks are available for many
    events.  Platform specific subclasses should provide methods for
    manipulating timers, terminate_app, and an event loop if required via
    Initialize/Start/Enable/Disable.
    
    @warning
    RenderWindowInteractor routes events through VTK's
    command/observer design pattern. That is, when
    RenderWindowInteractor (actually, one of its subclasses) sees a
    platform-dependent event, it translates this into a VTK event using
    the invoke_event() method. Then any InteractorObservers registered
    for that event are expected to respond as appropriate.
    
    @sa
    InteractorObserver
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderWindowInteractor, obj, update, **traits)
    
    enable_render = tvtk_base.true_bool_trait(help=\
        """
        Enable/Disable whether RenderWindowInteractor::Render() calls
        this->_render_window->_render().
        """
    )

    def _enable_render_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableRender,
                        self.enable_render_)

    light_follow_camera = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the automatic repositioning of lights as the camera
        moves. Default is On.
        """
    )

    def _light_follow_camera_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLightFollowCamera,
                        self.light_follow_camera_)

    alt_key = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get whether alt modifier key was pressed.
        """
    )

    def _alt_key_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAltKey,
                        self.alt_key)

    control_key = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get whether control modifier key was pressed.
        """
    )

    def _control_key_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetControlKey,
                        self.control_key)

    desired_update_rate = traits.Trait(15.0, traits.Range(0.0001, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Set/Get the desired update rate. This is used by LODActor's to
        tell them how quickly they need to render.  This update is in
        effect only when the camera is being rotated, or zoomed.  When
        the interactor is still, the still_update_rate is used instead. The
        default is 15.
        """
    )

    def _desired_update_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDesiredUpdateRate,
                        self.desired_update_rate)

    dolly = traits.Float(0.3, enter_set=True, auto_set=False, help=\
        """
        Set the total Dolly value to use when flying to (_fly_to()) a
        specified point. Negative values fly away from the point.
        """
    )

    def _dolly_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDolly,
                        self.dolly)

    event_position = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        Set/Get information about the current event. The current x,y
        position is in the event_position, and the previous event position
        is in last_event_position, updated automatically each time
        event_position is set using its Set() method. Mouse positions are
        measured in pixels. The other information is about key board
        input.
        """
    )

    def _event_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEventPosition,
                        self.event_position)

    event_size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _event_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEventSize,
                        self.event_size)

    def _get_interactor_style(self):
        return wrap_vtk(self._vtk_obj.GetInteractorStyle())
    def _set_interactor_style(self, arg):
        old_val = self._get_interactor_style()
        self._wrap_call(self._vtk_obj.SetInteractorStyle,
                        deref_vtk(arg))
        self.trait_property_changed('interactor_style', old_val, arg)
    interactor_style = traits.Property(_get_interactor_style, _set_interactor_style, help=\
        """
        External switching between joystick/trackball/new? modes. Initial
        value is a InteractorStyleSwitch object.
        """
    )

    key_code = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Set/get the key code for the key that was pressed.
        """
    )

    def _key_code_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeyCode,
                        self.key_code)

    key_sym = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/get the key symbol for the key that was pressed. This is the
        key symbol as defined by the relevant X headers. On X based
        platforms this corresponds to the installed X sevrer, whereas on
        other platforms the native key codes are translated into a string
        representation.
        """
    )

    def _key_sym_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeySym,
                        self.key_sym)

    last_event_position = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _last_event_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLastEventPosition,
                        self.last_event_position)

    number_of_fly_frames = traits.Trait(15, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the number of frames to fly to when fly_to is invoked.
        """
    )

    def _number_of_fly_frames_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfFlyFrames,
                        self.number_of_fly_frames)

    def _get_picker(self):
        return wrap_vtk(self._vtk_obj.GetPicker())
    def _set_picker(self, arg):
        old_val = self._get_picker()
        self._wrap_call(self._vtk_obj.SetPicker,
                        deref_vtk(arg))
        self.trait_property_changed('picker', old_val, arg)
    picker = traits.Property(_get_picker, _set_picker, help=\
        """
        Set/Get the object used to perform pick operations. In order to
        pick instances of Prop, the picker must be a subclass of
        AbstractPropPicker, meaning that it can identify a particular
        instance of Prop.
        """
    )

    def _get_picking_manager(self):
        return wrap_vtk(self._vtk_obj.GetPickingManager())
    def _set_picking_manager(self, arg):
        old_val = self._get_picking_manager()
        self._wrap_call(self._vtk_obj.SetPickingManager,
                        deref_vtk(arg))
        self.trait_property_changed('picking_manager', old_val, arg)
    picking_manager = traits.Property(_get_picking_manager, _set_picking_manager, help=\
        """
        Set the picking manager. Set/Get the object used to perform
        operations through the interactor By default, a valid but
        disabled picking manager is instantiated.
        """
    )

    pointer_index = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get the index of the most recent pointer to have an event
        """
    )

    def _pointer_index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointerIndex,
                        self.pointer_index)

    recognize_gestures = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Convert multitouch events into gestures. When this is on (its
        default) multitouch events received by this interactor will be
        converted into gestures by VTK. If turned off the raw multitouch
        events will be passed down.
        """
    )

    def _recognize_gestures_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRecognizeGestures,
                        self.recognize_gestures)

    def _get_render_window(self):
        return wrap_vtk(self._vtk_obj.GetRenderWindow())
    def _set_render_window(self, arg):
        old_val = self._get_render_window()
        self._wrap_call(self._vtk_obj.SetRenderWindow,
                        deref_vtk(arg))
        self.trait_property_changed('render_window', old_val, arg)
    render_window = traits.Property(_get_render_window, _set_render_window, help=\
        """
        Set/Get the rendering window being controlled by this object.
        """
    )

    repeat_count = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get the repear count for the key or mouse event. This
        specifies how many times a key has been pressed.
        """
    )

    def _repeat_count_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRepeatCount,
                        self.repeat_count)

    rotation = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/get the rotation for the gesture in degrees, update
        last_rotation
        """
    )

    def _rotation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRotation,
                        self.rotation)

    scale = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/get the scale for the gesture, updates last_scale
        """
    )

    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale)

    shift_key = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get whether shift modifier key was pressed.
        """
    )

    def _shift_key_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShiftKey,
                        self.shift_key)

    size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSize,
                        self.size)

    still_update_rate = traits.Trait(0.0001, traits.Range(0.0001, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Set/Get the desired update rate when movement has stopped. For
        the non-still update rate, see the set_desired_update_rate method.
        The default is 0.0001
        """
    )

    def _still_update_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStillUpdateRate,
                        self.still_update_rate)

    timer_duration = traits.Trait(10, traits.Range(1, 100000, enter_set=True, auto_set=False), help=\
        """
        Specify the default timer interval (in milliseconds). (This is
        used in conjunction with the timer methods described previously,
        e.g., create_timer() uses this value; and
        create_repeating_timer(duration) and create_one_shot_timer(duration)
        use the default value if the parameter "duration" is less than or
        equal to zero.) Care must be taken when adjusting the timer
        interval from the default value of 10 milliseconds--it may
        adversely affect the interactors.
        """
    )

    def _timer_duration_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimerDuration,
                        self.timer_duration)

    timer_event_duration = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        These methods are used to communicate information about the
        currently firing create_timer_event or destroy_timer_event. The
        caller of create_timer_event sets up timer_event_id, timer_event_type
        and timer_event_duration. The observer of create_timer_event should
        set up an appropriate platform specific timer based on those
        values and set the timer_event_platform_id before returning. The
        caller of destroy_timer_event sets up timer_event_platform_id. The
        observer of destroy_timer_event should simply destroy the platform
        specific timer created by create_timer_event. See
        GenericRenderWindowInteractor's internal_create_timer and
        internal_destroy_timer for an example.
        """
    )

    def _timer_event_duration_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimerEventDuration,
                        self.timer_event_duration)

    timer_event_id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        These methods are used to communicate information about the
        currently firing create_timer_event or destroy_timer_event. The
        caller of create_timer_event sets up timer_event_id, timer_event_type
        and timer_event_duration. The observer of create_timer_event should
        set up an appropriate platform specific timer based on those
        values and set the timer_event_platform_id before returning. The
        caller of destroy_timer_event sets up timer_event_platform_id. The
        observer of destroy_timer_event should simply destroy the platform
        specific timer created by create_timer_event. See
        GenericRenderWindowInteractor's internal_create_timer and
        internal_destroy_timer for an example.
        """
    )

    def _timer_event_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimerEventId,
                        self.timer_event_id)

    timer_event_platform_id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        These methods are used to communicate information about the
        currently firing create_timer_event or destroy_timer_event. The
        caller of create_timer_event sets up timer_event_id, timer_event_type
        and timer_event_duration. The observer of create_timer_event should
        set up an appropriate platform specific timer based on those
        values and set the timer_event_platform_id before returning. The
        caller of destroy_timer_event sets up timer_event_platform_id. The
        observer of destroy_timer_event should simply destroy the platform
        specific timer created by create_timer_event. See
        GenericRenderWindowInteractor's internal_create_timer and
        internal_destroy_timer for an example.
        """
    )

    def _timer_event_platform_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimerEventPlatformId,
                        self.timer_event_platform_id)

    timer_event_type = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        These methods are used to communicate information about the
        currently firing create_timer_event or destroy_timer_event. The
        caller of create_timer_event sets up timer_event_id, timer_event_type
        and timer_event_duration. The observer of create_timer_event should
        set up an appropriate platform specific timer based on those
        values and set the timer_event_platform_id before returning. The
        caller of destroy_timer_event sets up timer_event_platform_id. The
        observer of destroy_timer_event should simply destroy the platform
        specific timer created by create_timer_event. See
        GenericRenderWindowInteractor's internal_create_timer and
        internal_destroy_timer for an example.
        """
    )

    def _timer_event_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimerEventType,
                        self.timer_event_type)

    translation = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(5.77538072896742e+228, 4.0700540951768473e+180), cols=2, help=\
        """
        Set/get the tranlation for pan/swipe gestures, update
        last_translation
        """
    )

    def _translation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslation,
                        self.translation)

    use_t_dx = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Use a 3d_connexion device. Initial value is false. If VTK is not
        build with the TDx option, this is no-op. If VTK is build with
        the TDx option, and a device is not connected, a warning is
        emitted. It is must be called before the first Render to be
        effective, otherwise it is ignored.
        """
    )

    def _use_t_dx_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseTDx,
                        self.use_t_dx)

    def _get_enabled(self):
        return self._vtk_obj.GetEnabled()
    enabled = traits.Property(_get_enabled, help=\
        """
        
        """
    )

    def get_event_positions(self, *args):
        """
        V.get_event_positions(int) -> (int, ...)
        C++: virtual int *GetEventPositions(int pointerIndex)"""
        ret = self._wrap_call(self._vtk_obj.GetEventPositions, *args)
        return ret

    def _get_initialized(self):
        return self._vtk_obj.GetInitialized()
    initialized = traits.Property(_get_initialized, help=\
        """
        See whether interactor has been initialized yet. Default is 0.
        """
    )

    def get_last_event_positions(self, *args):
        """
        V.get_last_event_positions(int) -> (int, ...)
        C++: virtual int *GetLastEventPositions(int pointerIndex)"""
        ret = self._wrap_call(self._vtk_obj.GetLastEventPositions, *args)
        return ret

    def _get_last_rotation(self):
        return self._vtk_obj.GetLastRotation()
    last_rotation = traits.Property(_get_last_rotation, help=\
        """
        Set/get the rotation for the gesture in degrees, update
        last_rotation
        """
    )

    def _get_last_scale(self):
        return self._vtk_obj.GetLastScale()
    last_scale = traits.Property(_get_last_scale, help=\
        """
        Set/get the scale for the gesture, updates last_scale
        """
    )

    def _get_last_translation(self):
        return self._vtk_obj.GetLastTranslation()
    last_translation = traits.Property(_get_last_translation, help=\
        """
        
        """
    )

    def get_mouse_position(self, *args):
        """
        V.get_mouse_position([int, ...], [int, ...])
        C++: virtual void GetMousePosition(int *x, int *y)
        Get the current position of the mouse.
        """
        ret = self._wrap_call(self._vtk_obj.GetMousePosition, *args)
        return ret

    def _get_observer_mediator(self):
        return wrap_vtk(self._vtk_obj.GetObserverMediator())
    observer_mediator = traits.Property(_get_observer_mediator, help=\
        """
        Return the object used to mediate between InteractorObservers
        contending for resources. Multiple interactor observers will
        often request different resources (e.g., cursor shape); the
        mediator uses a strategy to provide the resource based on
        priority of the observer plus the particular request (default
        versus non-default cursor shape).
        """
    )

    def get_pointer_index_for_contact(self, *args):
        """
        V.get_pointer_index_for_contact(int) -> int
        C++: int GetPointerIndexForContact(size_t contactID)
        Most multitouch systems use persistent contact/pointer ids to
        track events/motion during multitouch events. We keep an array
        that maps these system dependent contact ids to our pointer index
        These functions return -1 if the ID is not found or if there is
        no more room for contacts
        """
        ret = self._wrap_call(self._vtk_obj.GetPointerIndexForContact, *args)
        return ret

    def get_pointer_index_for_existing_contact(self, *args):
        """
        V.get_pointer_index_for_existing_contact(int) -> int
        C++: int GetPointerIndexForExistingContact(size_t contactID)
        Most multitouch systems use persistent contact/pointer ids to
        track events/motion during multitouch events. We keep an array
        that maps these system dependent contact ids to our pointer index
        These functions return -1 if the ID is not found or if there is
        no more room for contacts
        """
        ret = self._wrap_call(self._vtk_obj.GetPointerIndexForExistingContact, *args)
        return ret

    def _get_pointers_down_count(self):
        return self._vtk_obj.GetPointersDownCount()
    pointers_down_count = traits.Property(_get_pointers_down_count, help=\
        """
        When handling gestures you can query this value to determine how
        many pointers are down for the gesture this is useful for pan
        gestures for example
        """
    )

    def get_vtk_timer_id(self, *args):
        """
        V.get_vtk_timer_id(int) -> int
        C++: virtual int GetVTKTimerId(int platformTimerId)
        Get the VTK timer ID that corresponds to the supplied platform
        ID.
        """
        ret = self._wrap_call(self._vtk_obj.GetVTKTimerId, *args)
        return ret

    def char_event(self):
        """
        V.char_event()
        C++: virtual void CharEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.CharEvent()
        return ret
        

    def clear_contact(self, *args):
        """
        V.clear_contact(int)
        C++: void ClearContact(size_t contactID)
        Most multitouch systems use persistent contact/pointer ids to
        track events/motion during multitouch events. We keep an array
        that maps these system dependent contact ids to our pointer index
        These functions return -1 if the ID is not found or if there is
        no more room for contacts
        """
        ret = self._wrap_call(self._vtk_obj.ClearContact, *args)
        return ret

    def clear_pointer_index(self, *args):
        """
        V.clear_pointer_index(int)
        C++: void ClearPointerIndex(int i)
        Most multitouch systems use persistent contact/pointer ids to
        track events/motion during multitouch events. We keep an array
        that maps these system dependent contact ids to our pointer index
        These functions return -1 if the ID is not found or if there is
        no more room for contacts
        """
        ret = self._wrap_call(self._vtk_obj.ClearPointerIndex, *args)
        return ret

    def configure_event(self):
        """
        V.configure_event()
        C++: virtual void ConfigureEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.ConfigureEvent()
        return ret
        

    def create_default_picker(self):
        """
        V.create_default_picker() -> AbstractPropPicker
        C++: virtual AbstractPropPicker *CreateDefaultPicker()
        Create default picker. Used to create one when none is specified.
        Default is an instance of PropPicker.
        """
        ret = wrap_vtk(self._vtk_obj.CreateDefaultPicker())
        return ret
        

    def create_one_shot_timer(self, *args):
        """
        V.create_one_shot_timer(int) -> int
        C++: int CreateOneShotTimer(unsigned long duration)
        Create a one shot timer, with the specified duretion (in
        milliseconds).
        \return the timer id.
        """
        ret = self._wrap_call(self._vtk_obj.CreateOneShotTimer, *args)
        return ret

    def create_repeating_timer(self, *args):
        """
        V.create_repeating_timer(int) -> int
        C++: int CreateRepeatingTimer(unsigned long duration)
        Create a repeating timer, with the specified duration (in
        milliseconds).
        \return the timer id.
        """
        ret = self._wrap_call(self._vtk_obj.CreateRepeatingTimer, *args)
        return ret

    def create_timer(self, *args):
        """
        V.create_timer(int) -> int
        C++: virtual int CreateTimer(int timerType)
        This class provides two groups of methods for manipulating
        timers.  The first group (_create_timer(timer_type) and
        destroy_timer()) implicitly use an internal timer id (and are
        present for backward compatibility). The second group
        (_create_repeating_timer(long),_create_one_shot_timer(long),
        reset_timer(int),_destroy_timer(int)) use timer ids so multiple
        timers can be independently managed. In the first group, the
        create_timer() method takes an argument indicating whether the
        timer is created the first time (timer_type==_vtki__timer__first) or
        whether it is being reset (timer_type==_vtki__timer__update). (In
        initial implementations of VTK this was how one shot and
        repeating timers were managed.) In the second group, the create
        methods take a timer duration argument (in milliseconds) and
        return a timer id. Thus the reset_timer(timer_id) and
        destroy_timer(timer_id) methods take this timer id and operate on
        the timer as appropriate. Methods are also available for
        determining
        """
        ret = self._wrap_call(self._vtk_obj.CreateTimer, *args)
        return ret

    def destroy_timer(self, *args):
        """
        V.destroy_timer() -> int
        C++: virtual int DestroyTimer()
        V.destroy_timer(int) -> int
        C++: int DestroyTimer(int timerId)"""
        ret = self._wrap_call(self._vtk_obj.DestroyTimer, *args)
        return ret

    def disable(self):
        """
        V.disable()
        C++: virtual void Disable()"""
        ret = self._vtk_obj.Disable()
        return ret
        

    def enable(self):
        """
        V.enable()
        C++: virtual void Enable()
        Enable/Disable interactions.  By default interactors are enabled
        when initialized.  Initialize() must be called prior to
        enabling/disabling interaction. These methods are used when a
        window/widget is being shared by multiple renderers and
        interactors.  This allows a "modal" display where one interactor
        is active when its data is to be displayed and all other
        interactors associated with the widget are disabled when their
        data is not displayed.
        """
        ret = self._vtk_obj.Enable()
        return ret
        

    def end_pan_event(self):
        """
        V.end_pan_event()
        C++: virtual void EndPanEvent()
        Fire various gesture based events.  These methods will Invoke the
        corresponding vtk event.
        """
        ret = self._vtk_obj.EndPanEvent()
        return ret
        

    def end_pick_callback(self):
        """
        V.end_pick_callback()
        C++: virtual void EndPickCallback()
        These methods correspond to the the Exit, User and Pick
        callbacks. They allow for the Style to invoke them.
        """
        ret = self._vtk_obj.EndPickCallback()
        return ret
        

    def end_pinch_event(self):
        """
        V.end_pinch_event()
        C++: virtual void EndPinchEvent()
        Fire various gesture based events.  These methods will Invoke the
        corresponding vtk event.
        """
        ret = self._vtk_obj.EndPinchEvent()
        return ret
        

    def end_rotate_event(self):
        """
        V.end_rotate_event()
        C++: virtual void EndRotateEvent()
        Fire various gesture based events.  These methods will Invoke the
        corresponding vtk event.
        """
        ret = self._vtk_obj.EndRotateEvent()
        return ret
        

    def enter_event(self):
        """
        V.enter_event()
        C++: virtual void EnterEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.EnterEvent()
        return ret
        

    def exit_callback(self):
        """
        V.exit_callback()
        C++: virtual void ExitCallback()
        These methods correspond to the the Exit, User and Pick
        callbacks. They allow for the Style to invoke them.
        """
        ret = self._vtk_obj.ExitCallback()
        return ret
        

    def exit_event(self):
        """
        V.exit_event()
        C++: virtual void ExitEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.ExitEvent()
        return ret
        

    def expose_event(self):
        """
        V.expose_event()
        C++: virtual void ExposeEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.ExposeEvent()
        return ret
        

    def find_poked_renderer(self, *args):
        """
        V.find_poked_renderer(int, int) -> Renderer
        C++: virtual Renderer *FindPokedRenderer(int, int)
        When an event occurs, we must determine which Renderer the event
        occurred within, since one render_window may contain multiple
        renderers.
        """
        ret = self._wrap_call(self._vtk_obj.FindPokedRenderer, *args)
        return wrap_vtk(ret)

    def fly_to(self, *args):
        """
        V.fly_to(Renderer, float, float, float)
        C++: void FlyTo(Renderer *ren, double x, double y, double z)
        V.fly_to(Renderer, [float, ...])
        C++: void FlyTo(Renderer *ren, double *x)
        Given a position x, move the current camera's focal point to x.
        The movement is animated over the number of frames specified in
        number_of_fly_frames. The LOD desired frame rate is used.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FlyTo, *my_args)
        return ret

    def fly_to_image(self, *args):
        """
        V.fly_to_image(Renderer, float, float)
        C++: void FlyToImage(Renderer *ren, double x, double y)
        V.fly_to_image(Renderer, [float, ...])
        C++: void FlyToImage(Renderer *ren, double *x)
        Given a position x, move the current camera's focal point to x.
        The movement is animated over the number of frames specified in
        number_of_fly_frames. The LOD desired frame rate is used.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FlyToImage, *my_args)
        return ret

    def hide_cursor(self):
        """
        V.hide_cursor()
        C++: void HideCursor()
        Hide or show the mouse cursor, it is nice to be able to hide the
        default cursor if you want VTK to display a 3d cursor instead.
        """
        ret = self._vtk_obj.HideCursor()
        return ret
        

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()
        Prepare for handling events and set the Enabled flag to true.
        This will be called automatically by Start() if the interactor is
        not initialized, but it can be called manually if you need to
        perform any operations between initialization and the start of
        the event loop.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def is_one_shot_timer(self, *args):
        """
        V.is_one_shot_timer(int) -> int
        C++: int IsOneShotTimer(int timerId)
        Query whether the specified timer_id is a one shot timer.
        \return 1 if the timer is a one shot timer.
        """
        ret = self._wrap_call(self._vtk_obj.IsOneShotTimer, *args)
        return ret

    def is_pointer_index_set(self, *args):
        """
        V.is_pointer_index_set(int) -> bool
        C++: bool IsPointerIndexSet(int i)
        Most multitouch systems use persistent contact/pointer ids to
        track events/motion during multitouch events. We keep an array
        that maps these system dependent contact ids to our pointer index
        These functions return -1 if the ID is not found or if there is
        no more room for contacts
        """
        ret = self._wrap_call(self._vtk_obj.IsPointerIndexSet, *args)
        return ret

    def key_press_event(self):
        """
        V.key_press_event()
        C++: virtual void KeyPressEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.KeyPressEvent()
        return ret
        

    def key_release_event(self):
        """
        V.key_release_event()
        C++: virtual void KeyReleaseEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.KeyReleaseEvent()
        return ret
        

    def leave_event(self):
        """
        V.leave_event()
        C++: virtual void LeaveEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.LeaveEvent()
        return ret
        

    def left_button_press_event(self):
        """
        V.left_button_press_event()
        C++: virtual void LeftButtonPressEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.LeftButtonPressEvent()
        return ret
        

    def left_button_release_event(self):
        """
        V.left_button_release_event()
        C++: virtual void LeftButtonReleaseEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.LeftButtonReleaseEvent()
        return ret
        

    def long_tap_event(self):
        """
        V.long_tap_event()
        C++: virtual void LongTapEvent()
        Fire various gesture based events.  These methods will Invoke the
        corresponding vtk event.
        """
        ret = self._vtk_obj.LongTapEvent()
        return ret
        

    def middle_button_press_event(self):
        """
        V.middle_button_press_event()
        C++: virtual void MiddleButtonPressEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.MiddleButtonPressEvent()
        return ret
        

    def middle_button_release_event(self):
        """
        V.middle_button_release_event()
        C++: virtual void MiddleButtonReleaseEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.MiddleButtonReleaseEvent()
        return ret
        

    def mouse_move_event(self):
        """
        V.mouse_move_event()
        C++: virtual void MouseMoveEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.MouseMoveEvent()
        return ret
        

    def mouse_wheel_backward_event(self):
        """
        V.mouse_wheel_backward_event()
        C++: virtual void MouseWheelBackwardEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.MouseWheelBackwardEvent()
        return ret
        

    def mouse_wheel_forward_event(self):
        """
        V.mouse_wheel_forward_event()
        C++: virtual void MouseWheelForwardEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.MouseWheelForwardEvent()
        return ret
        

    def pan_event(self):
        """
        V.pan_event()
        C++: virtual void PanEvent()
        Fire various gesture based events.  These methods will Invoke the
        corresponding vtk event.
        """
        ret = self._vtk_obj.PanEvent()
        return ret
        

    def pinch_event(self):
        """
        V.pinch_event()
        C++: virtual void PinchEvent()
        Fire various gesture based events.  These methods will Invoke the
        corresponding vtk event.
        """
        ret = self._vtk_obj.PinchEvent()
        return ret
        

    def re_initialize(self):
        """
        V.re_initialize()
        C++: void ReInitialize()
        Prepare for handling events and set the Enabled flag to true.
        This will be called automatically by Start() if the interactor is
        not initialized, but it can be called manually if you need to
        perform any operations between initialization and the start of
        the event loop.
        """
        ret = self._vtk_obj.ReInitialize()
        return ret
        

    def render(self):
        """
        V.render()
        C++: virtual void Render()
        Render the scene. Just pass the render call on to the associated
        RenderWindow.
        """
        ret = self._vtk_obj.Render()
        return ret
        

    def reset_timer(self, *args):
        """
        V.reset_timer(int) -> int
        C++: int ResetTimer(int timerId)
        Reset the specified timer.
        """
        ret = self._wrap_call(self._vtk_obj.ResetTimer, *args)
        return ret

    def right_button_press_event(self):
        """
        V.right_button_press_event()
        C++: virtual void RightButtonPressEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.RightButtonPressEvent()
        return ret
        

    def right_button_release_event(self):
        """
        V.right_button_release_event()
        C++: virtual void RightButtonReleaseEvent()
        Fire various events. set_event_information should be called just
        prior to calling any of these methods. These methods will Invoke
        the corresponding vtk event.
        """
        ret = self._vtk_obj.RightButtonReleaseEvent()
        return ret
        

    def rotate_event(self):
        """
        V.rotate_event()
        C++: virtual void RotateEvent()
        Fire various gesture based events.  These methods will Invoke the
        corresponding vtk event.
        """
        ret = self._vtk_obj.RotateEvent()
        return ret
        

    def set_event_information(self, *args):
        """
        V.set_event_information(int, int, int, int, char, int, string, int)
        C++: void SetEventInformation(int x, int y, int ctrl, int shift,
            char keycode, int repeatcount, const char *keysym,
            int pointerIndex)
        V.set_event_information(int, int, int, int, char, int, string)
        C++: void SetEventInformation(int x, int y, int ctrl=0,
            int shift=0, char keycode=0, int repeatcount=0,
            const char *keysym=0)
        Set all the event information in one call.
        """
        ret = self._wrap_call(self._vtk_obj.SetEventInformation, *args)
        return ret

    def set_event_information_flip_y(self, *args):
        """
        V.set_event_information_flip_y(int, int, int, int, char, int, string,
            int)
        C++: void SetEventInformationFlipY(int x, int y, int ctrl,
            int shift, char keycode, int repeatcount, const char *keysym,
            int pointerIndex)
        V.set_event_information_flip_y(int, int, int, int, char, int, string)
        C++: void SetEventInformationFlipY(int x, int y, int ctrl=0,
            int shift=0, char keycode=0, int repeatcount=0,
            const char *keysym=0)
        Calls set_event_information, but flips the Y based on the current
        Size[1] value (i.e. y = this->Size[1] - y - 1).
        """
        ret = self._wrap_call(self._vtk_obj.SetEventInformationFlipY, *args)
        return ret

    def set_event_position_flip_y(self, *args):
        """
        V.set_event_position_flip_y(int, int)
        C++: virtual void SetEventPositionFlipY(int x, int y)
        V.set_event_position_flip_y([int, int])
        C++: virtual void SetEventPositionFlipY(int pos[2])
        V.set_event_position_flip_y(int, int, int)
        C++: virtual void SetEventPositionFlipY(int x, int y,
            int pointerIndex)
        V.set_event_position_flip_y([int, int], int)
        C++: virtual void SetEventPositionFlipY(int pos[2],
            int pointerIndex)
        Set/Get information about the current event. The current x,y
        position is in the event_position, and the previous event position
        is in last_event_position, updated automatically each time
        event_position is set using its Set() method. Mouse positions are
        measured in pixels. The other information is about key board
        input.
        """
        ret = self._wrap_call(self._vtk_obj.SetEventPositionFlipY, *args)
        return ret

    def set_key_event_information(self, *args):
        """
        V.set_key_event_information(int, int, char, int, string)
        C++: void SetKeyEventInformation(int ctrl=0, int shift=0,
            char keycode=0, int repeatcount=0, const char *keysym=0)
        Set all the keyboard-related event information in one call.
        """
        ret = self._wrap_call(self._vtk_obj.SetKeyEventInformation, *args)
        return ret

    def show_cursor(self):
        """
        V.show_cursor()
        C++: void ShowCursor()
        Hide or show the mouse cursor, it is nice to be able to hide the
        default cursor if you want VTK to display a 3d cursor instead.
        """
        ret = self._vtk_obj.ShowCursor()
        return ret
        

    def start(self):
        """
        V.start()
        C++: virtual void Start()
        Start the event loop. This is provided so that you do not have to
        implement your own event loop. You still can use your own event
        loop if you want.
        """
        ret = self._vtk_obj.Start()
        return ret
        

    def start_pan_event(self):
        """
        V.start_pan_event()
        C++: virtual void StartPanEvent()
        Fire various gesture based events.  These methods will Invoke the
        corresponding vtk event.
        """
        ret = self._vtk_obj.StartPanEvent()
        return ret
        

    def start_pick_callback(self):
        """
        V.start_pick_callback()
        C++: virtual void StartPickCallback()
        These methods correspond to the the Exit, User and Pick
        callbacks. They allow for the Style to invoke them.
        """
        ret = self._vtk_obj.StartPickCallback()
        return ret
        

    def start_pinch_event(self):
        """
        V.start_pinch_event()
        C++: virtual void StartPinchEvent()
        Fire various gesture based events.  These methods will Invoke the
        corresponding vtk event.
        """
        ret = self._vtk_obj.StartPinchEvent()
        return ret
        

    def start_rotate_event(self):
        """
        V.start_rotate_event()
        C++: virtual void StartRotateEvent()
        Fire various gesture based events.  These methods will Invoke the
        corresponding vtk event.
        """
        ret = self._vtk_obj.StartRotateEvent()
        return ret
        

    def swipe_event(self):
        """
        V.swipe_event()
        C++: virtual void SwipeEvent()
        Fire various gesture based events.  These methods will Invoke the
        corresponding vtk event.
        """
        ret = self._vtk_obj.SwipeEvent()
        return ret
        

    def tap_event(self):
        """
        V.tap_event()
        C++: virtual void TapEvent()
        Fire various gesture based events.  These methods will Invoke the
        corresponding vtk event.
        """
        ret = self._vtk_obj.TapEvent()
        return ret
        

    def terminate_app(self):
        """
        V.terminate_app()
        C++: virtual void TerminateApp(void)
        This function is called on 'q','e' keypress if exitmethod is not
        specified and should be overridden by platform dependent
        subclasses to provide a termination procedure if one is required.
        """
        ret = self._vtk_obj.TerminateApp()
        return ret
        

    def update_size(self, *args):
        """
        V.update_size(int, int)
        C++: virtual void UpdateSize(int x, int y)
        Event loop notification member for window size change. Window
        size is measured in pixels.
        """
        ret = self._wrap_call(self._vtk_obj.UpdateSize, *args)
        return ret

    def user_callback(self):
        """
        V.user_callback()
        C++: virtual void UserCallback()
        These methods correspond to the the Exit, User and Pick
        callbacks. They allow for the Style to invoke them.
        """
        ret = self._vtk_obj.UserCallback()
        return ret
        

    _updateable_traits_ = \
    (('enable_render', 'GetEnableRender'), ('light_follow_camera',
    'GetLightFollowCamera'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('alt_key',
    'GetAltKey'), ('control_key', 'GetControlKey'),
    ('desired_update_rate', 'GetDesiredUpdateRate'), ('dolly',
    'GetDolly'), ('event_position', 'GetEventPosition'), ('event_size',
    'GetEventSize'), ('key_code', 'GetKeyCode'), ('key_sym', 'GetKeySym'),
    ('last_event_position', 'GetLastEventPosition'),
    ('number_of_fly_frames', 'GetNumberOfFlyFrames'), ('pointer_index',
    'GetPointerIndex'), ('recognize_gestures', 'GetRecognizeGestures'),
    ('repeat_count', 'GetRepeatCount'), ('rotation', 'GetRotation'),
    ('scale', 'GetScale'), ('shift_key', 'GetShiftKey'), ('size',
    'GetSize'), ('still_update_rate', 'GetStillUpdateRate'),
    ('timer_duration', 'GetTimerDuration'), ('timer_event_duration',
    'GetTimerEventDuration'), ('timer_event_id', 'GetTimerEventId'),
    ('timer_event_platform_id', 'GetTimerEventPlatformId'),
    ('timer_event_type', 'GetTimerEventType'), ('translation',
    'GetTranslation'), ('use_t_dx', 'GetUseTDx'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'enable_render', 'global_warning_display',
    'light_follow_camera', 'alt_key', 'control_key',
    'desired_update_rate', 'dolly', 'event_position', 'event_size',
    'key_code', 'key_sym', 'last_event_position', 'number_of_fly_frames',
    'pointer_index', 'recognize_gestures', 'repeat_count', 'rotation',
    'scale', 'shift_key', 'size', 'still_update_rate', 'timer_duration',
    'timer_event_duration', 'timer_event_id', 'timer_event_platform_id',
    'timer_event_type', 'translation', 'use_t_dx'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderWindowInteractor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enable_render', 'light_follow_camera'], [], ['alt_key',
            'control_key', 'desired_update_rate', 'dolly', 'event_position',
            'event_size', 'key_code', 'key_sym', 'last_event_position',
            'number_of_fly_frames', 'pointer_index', 'recognize_gestures',
            'repeat_count', 'rotation', 'scale', 'shift_key', 'size',
            'still_update_rate', 'timer_duration', 'timer_event_duration',
            'timer_event_id', 'timer_event_platform_id', 'timer_event_type',
            'translation', 'use_t_dx']),
            title='Edit RenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


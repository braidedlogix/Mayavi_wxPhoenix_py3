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

from tvtk.tvtk_classes.render_window_interactor import RenderWindowInteractor


class GenericRenderWindowInteractor(RenderWindowInteractor):
    """
    GenericRenderWindowInteractor - platform-independent programmable
    render window interactor.
    
    Superclass: RenderWindowInteractor
    
    GenericRenderWindowInteractor provides a way to translate native
    mouse and keyboard events into vtk Events.   By calling the methods
    on this class, vtk events will be invoked.   This will allow
    scripting languages to use InteractorStyles and 3d widgets.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericRenderWindowInteractor, obj, update, **traits)
    
    timer_event_resets_timer = tvtk_base.true_bool_trait(help=\
        """
        Flag that indicates whether the timer_event method should call
        reset_timer to simulate repeating timers with an endless stream of
        one shot timers. By default this flag is on and all repeating
        timers are implemented as a stream of sequential one shot timers.
        If the observer of create_timer_event actually creates a "natively
        repeating" timer, setting this flag to off will prevent (perhaps
        many many) unnecessary calls to reset_timer. Having the flag on by
        default means that "natively one shot" timers can be either one
        shot or repeating timers with no additional work. Also, "natively
        repeating" timers still work with the default setting, but with
        potentially many create and destroy calls.
        """
    )

    def _timer_event_resets_timer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimerEventResetsTimer,
                        self.timer_event_resets_timer_)

    def timer_event(self):
        """
        V.timer_event()
        C++: virtual void TimerEvent()
        Fire timer_event. set_event_information should be called just prior
        to calling any of these methods. These methods will Invoke the
        corresponding vtk event.
        """
        ret = self._vtk_obj.TimerEvent()
        return ret
        

    _updateable_traits_ = \
    (('timer_event_resets_timer', 'GetTimerEventResetsTimer'),
    ('enable_render', 'GetEnableRender'), ('light_follow_camera',
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
    'light_follow_camera', 'timer_event_resets_timer', 'alt_key',
    'control_key', 'desired_update_rate', 'dolly', 'event_position',
    'event_size', 'key_code', 'key_sym', 'last_event_position',
    'number_of_fly_frames', 'pointer_index', 'recognize_gestures',
    'repeat_count', 'rotation', 'scale', 'shift_key', 'size',
    'still_update_rate', 'timer_duration', 'timer_event_duration',
    'timer_event_id', 'timer_event_platform_id', 'timer_event_type',
    'translation', 'use_t_dx'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericRenderWindowInteractor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericRenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enable_render', 'light_follow_camera',
            'timer_event_resets_timer'], [], ['alt_key', 'control_key',
            'desired_update_rate', 'dolly', 'event_position', 'event_size',
            'key_code', 'key_sym', 'last_event_position', 'number_of_fly_frames',
            'pointer_index', 'recognize_gestures', 'repeat_count', 'rotation',
            'scale', 'shift_key', 'size', 'still_update_rate', 'timer_duration',
            'timer_event_duration', 'timer_event_id', 'timer_event_platform_id',
            'timer_event_type', 'translation', 'use_t_dx']),
            title='Edit GenericRenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericRenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


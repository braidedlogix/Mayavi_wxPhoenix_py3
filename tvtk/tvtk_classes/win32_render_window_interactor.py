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


class Win32RenderWindowInteractor(RenderWindowInteractor):
    """
    Win32RenderWindowInteractor - implements Win32 specific functions
    required by RenderWindowInteractor.
    
    Superclass: RenderWindowInteractor
    
    By default the interactor installs a message_proc callback which
    intercepts windows' messages to the window and controls interactions
    by routing them to the interacto_style classes. MFC or BCB programs
    can prevent this and instead directly route any mouse/key messages
    into the event bindings by setting install_message_proc to false. This
    provides a minimal "Mapped" mode of interaction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWin32RenderWindowInteractor, obj, update, **traits)
    
    install_message_proc = tvtk_base.true_bool_trait(help=\
        """
        By default the interactor installs a message_proc callback which
        intercepts windows messages to the window and controls
        interactions. MFC or BCB programs can prevent this and instead
        directly route any mouse/key messages into the event bindings by
        setting install_messge_proc to false.
        """
    )

    def _install_message_proc_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInstallMessageProc,
                        self.install_message_proc_)

    def set_class_exit_method(self, *args):
        """
        V.set_class_exit_method(function)
        C++: static void SetClassExitMethod(void (*f)(void *), void *arg)
        Methods to set the default exit method for the class. This method
        is only used if no instance level exit_method has been defined. 
        It is provided as a means to control how an interactor is exited
        given the various language bindings (tcl, Win32, etc.).
        """
        ret = self._wrap_call(self._vtk_obj.SetClassExitMethod, *args)
        return ret

    _updateable_traits_ = \
    (('install_message_proc', 'GetInstallMessageProc'), ('enable_render',
    'GetEnableRender'), ('light_follow_camera', 'GetLightFollowCamera'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('alt_key', 'GetAltKey'), ('control_key',
    'GetControlKey'), ('desired_update_rate', 'GetDesiredUpdateRate'),
    ('dolly', 'GetDolly'), ('event_position', 'GetEventPosition'),
    ('event_size', 'GetEventSize'), ('key_code', 'GetKeyCode'),
    ('key_sym', 'GetKeySym'), ('last_event_position',
    'GetLastEventPosition'), ('number_of_fly_frames',
    'GetNumberOfFlyFrames'), ('pointer_index', 'GetPointerIndex'),
    ('recognize_gestures', 'GetRecognizeGestures'), ('repeat_count',
    'GetRepeatCount'), ('rotation', 'GetRotation'), ('scale', 'GetScale'),
    ('shift_key', 'GetShiftKey'), ('size', 'GetSize'),
    ('still_update_rate', 'GetStillUpdateRate'), ('timer_duration',
    'GetTimerDuration'), ('timer_event_duration',
    'GetTimerEventDuration'), ('timer_event_id', 'GetTimerEventId'),
    ('timer_event_platform_id', 'GetTimerEventPlatformId'),
    ('timer_event_type', 'GetTimerEventType'), ('translation',
    'GetTranslation'), ('use_t_dx', 'GetUseTDx'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'enable_render', 'global_warning_display',
    'install_message_proc', 'light_follow_camera', 'alt_key',
    'control_key', 'desired_update_rate', 'dolly', 'event_position',
    'event_size', 'key_code', 'key_sym', 'last_event_position',
    'number_of_fly_frames', 'pointer_index', 'recognize_gestures',
    'repeat_count', 'rotation', 'scale', 'shift_key', 'size',
    'still_update_rate', 'timer_duration', 'timer_event_duration',
    'timer_event_id', 'timer_event_platform_id', 'timer_event_type',
    'translation', 'use_t_dx'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Win32RenderWindowInteractor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Win32RenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enable_render', 'install_message_proc',
            'light_follow_camera'], [], ['alt_key', 'control_key',
            'desired_update_rate', 'dolly', 'event_position', 'event_size',
            'key_code', 'key_sym', 'last_event_position', 'number_of_fly_frames',
            'pointer_index', 'recognize_gestures', 'repeat_count', 'rotation',
            'scale', 'shift_key', 'size', 'still_update_rate', 'timer_duration',
            'timer_event_duration', 'timer_event_id', 'timer_event_platform_id',
            'timer_event_type', 'translation', 'use_t_dx']),
            title='Edit Win32RenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Win32RenderWindowInteractor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.interactor_style import InteractorStyle


class InteractorStyleFlight(InteractorStyle):
    """
    InteractorStyleFlight - provides flight motion routines
    
    Superclass: InteractorStyle
    
    Left  mouse button press produces forward motion. Right mouse button
    press produces reverse motion. Moving mouse during motion steers user
    in desired direction. Keyboard controls are: Left/Right/Up/Down
    Arrows for steering direction 'A' forward, 'Z' reverse motion Ctrl
    Key causes sidestep instead of steering in mouse and key modes Shift
    key is accelerator in mouse and key modes Ctrl and Shift together
    causes Roll in mouse and key modes
    
    By default, one "step" of motion corresponds to 1/250th of the
    diagonal of bounding box of visible actors, '+' and '-' keys allow
    user to increase or decrease step size.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleFlight, obj, update, **traits)
    
    disable_motion = tvtk_base.false_bool_trait(help=\
        """
        Disable motion (temporarily - for viewing etc)
        """
    )

    def _disable_motion_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisableMotion,
                        self.disable_motion_)

    restore_up_vector = tvtk_base.true_bool_trait(help=\
        """
        When flying, apply a restorative force to the "Up" vector. This
        is activated when the current 'up' is close to the actual 'up'
        (as defined in default_up_vector). This prevents excessive twisting
        forces when viewing from arbitrary angles, but keep the horizon
        level when the user is flying over terrain.
        """
    )

    def _restore_up_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRestoreUpVector,
                        self.restore_up_vector_)

    angle_acceleration_factor = traits.Float(5.0, enter_set=True, auto_set=False, help=\
        """
        Set angular acceleration when shift key is applied : default 5
        """
    )

    def _angle_acceleration_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAngleAccelerationFactor,
                        self.angle_acceleration_factor)

    angle_step_size = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the basic angular unit for turning : default 1 degree
        """
    )

    def _angle_step_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAngleStepSize,
                        self.angle_step_size)

    default_up_vector = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _default_up_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultUpVector,
                        self.default_up_vector)

    motion_acceleration_factor = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set acceleration factor when shift key is applied : default 10
        """
    )

    def _motion_acceleration_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMotionAccelerationFactor,
                        self.motion_acceleration_factor)

    motion_step_size = traits.Float(0.004, enter_set=True, auto_set=False, help=\
        """
        Set the basic unit step size : by default 1/250 of bounding
        diagonal
        """
    )

    def _motion_step_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMotionStepSize,
                        self.motion_step_size)

    def end_forward_fly(self):
        """
        V.end_forward_fly()
        C++: virtual void EndForwardFly()"""
        ret = self._vtk_obj.EndForwardFly()
        return ret
        

    def end_reverse_fly(self):
        """
        V.end_reverse_fly()
        C++: virtual void EndReverseFly()"""
        ret = self._vtk_obj.EndReverseFly()
        return ret
        

    def forward_fly(self):
        """
        V.forward_fly()
        C++: virtual void ForwardFly()"""
        ret = self._vtk_obj.ForwardFly()
        return ret
        

    def jump_to(self, *args):
        """
        V.jump_to([float, float, float], [float, float, float])
        C++: void JumpTo(double campos[3], double focpos[3])
        Move the Eye/Camera to a specific location (no intermediate steps
        are taken
        """
        ret = self._wrap_call(self._vtk_obj.JumpTo, *args)
        return ret

    def reverse_fly(self):
        """
        V.reverse_fly()
        C++: virtual void ReverseFly()"""
        ret = self._vtk_obj.ReverseFly()
        return ret
        

    def start_forward_fly(self):
        """
        V.start_forward_fly()
        C++: virtual void StartForwardFly()"""
        ret = self._vtk_obj.StartForwardFly()
        return ret
        

    def start_reverse_fly(self):
        """
        V.start_reverse_fly()
        C++: virtual void StartReverseFly()"""
        ret = self._vtk_obj.StartReverseFly()
        return ret
        

    _updateable_traits_ = \
    (('disable_motion', 'GetDisableMotion'), ('restore_up_vector',
    'GetRestoreUpVector'), ('auto_adjust_camera_clipping_range',
    'GetAutoAdjustCameraClippingRange'), ('handle_observers',
    'GetHandleObservers'), ('use_timers', 'GetUseTimers'), ('enabled',
    'GetEnabled'), ('key_press_activation', 'GetKeyPressActivation'),
    ('picking_managed', 'GetPickingManaged'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('angle_acceleration_factor', 'GetAngleAccelerationFactor'),
    ('angle_step_size', 'GetAngleStepSize'), ('default_up_vector',
    'GetDefaultUpVector'), ('motion_acceleration_factor',
    'GetMotionAccelerationFactor'), ('motion_step_size',
    'GetMotionStepSize'), ('mouse_wheel_motion_factor',
    'GetMouseWheelMotionFactor'), ('pick_color', 'GetPickColor'),
    ('timer_duration', 'GetTimerDuration'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('priority', 'GetPriority'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['auto_adjust_camera_clipping_range', 'debug', 'disable_motion',
    'enabled', 'global_warning_display', 'handle_observers',
    'key_press_activation', 'picking_managed', 'restore_up_vector',
    'use_timers', 'angle_acceleration_factor', 'angle_step_size',
    'default_up_vector', 'key_press_activation_value',
    'motion_acceleration_factor', 'motion_step_size',
    'mouse_wheel_motion_factor', 'pick_color', 'priority',
    'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorStyleFlight, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleFlight properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_adjust_camera_clipping_range', 'disable_motion',
            'enabled', 'handle_observers', 'key_press_activation',
            'picking_managed', 'restore_up_vector', 'use_timers'], [],
            ['angle_acceleration_factor', 'angle_step_size', 'default_up_vector',
            'key_press_activation_value', 'motion_acceleration_factor',
            'motion_step_size', 'mouse_wheel_motion_factor', 'pick_color',
            'priority', 'timer_duration']),
            title='Edit InteractorStyleFlight properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleFlight properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


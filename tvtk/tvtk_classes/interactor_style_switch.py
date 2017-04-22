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

from tvtk.tvtk_classes.interactor_style_switch_base import InteractorStyleSwitchBase


class InteractorStyleSwitch(InteractorStyleSwitchBase):
    """
    InteractorStyleSwitch - class to swap between interactory styles
    
    Superclass: InteractorStyleSwitchBase
    
    The class InteractorStyleSwitch allows handles interactively
    switching between four interactor styles -- joystick actor, joystick
    camera, trackball actor, and trackball camera.  Type 'j' or 't' to
    select joystick or trackball, and type 'c' or 'a' to select camera or
    actor. The default interactor style is joystick camera.
    @sa
    InteractorStyleJoystickActor InteractorStyleJoystickCamera
    InteractorStyleTrackballActor InteractorStyleTrackballCamera
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleSwitch, obj, update, **traits)
    
    def get_current_style(self):
        """
        V.get_current_style() -> InteractorStyle
        C++: InteractorStyle *GetCurrentStyle()
        Set/Get current style
        """
        ret = wrap_vtk(self._vtk_obj.GetCurrentStyle())
        return ret
        

    def set_current_style_to_joystick_camera(self):
        """
        V.set_current_style_to_joystick_camera()
        C++: void SetCurrentStyleToJoystickCamera()
        Set/Get current style
        """
        self._vtk_obj.SetCurrentStyleToJoystickCamera()

    def set_current_style_to_multi_touch_camera(self):
        """
        V.set_current_style_to_multi_touch_camera()
        C++: void SetCurrentStyleToMultiTouchCamera()
        Set/Get current style
        """
        self._vtk_obj.SetCurrentStyleToMultiTouchCamera()

    def set_current_style_to_trackball_actor(self):
        """
        V.set_current_style_to_trackball_actor()
        C++: void SetCurrentStyleToTrackballActor()
        Set/Get current style
        """
        self._vtk_obj.SetCurrentStyleToTrackballActor()

    def set_current_style_to_trackball_camera(self):
        """
        V.set_current_style_to_trackball_camera()
        C++: void SetCurrentStyleToTrackballCamera()
        Set/Get current style
        """
        self._vtk_obj.SetCurrentStyleToTrackballCamera()

    def _get_current_renderer(self):
        return wrap_vtk(self._vtk_obj.GetCurrentRenderer())
    def _set_current_renderer(self, arg):
        old_val = self._get_current_renderer()
        self._wrap_call(self._vtk_obj.SetCurrentRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('current_renderer', old_val, arg)
    current_renderer = traits.Property(_get_current_renderer, _set_current_renderer, help=\
        """
        Set/Get the current renderer. Normally when the widget is
        activated (_set_enabled(_1) or when keypress activation takes
        place), the renderer over which the mouse pointer is positioned
        is used and assigned to this Ivar. Alternatively, you might want
        to set the current_renderer explicitly. This is especially true
        with multiple viewports (renderers). WARNING: note that if the
        default_renderer Ivar is set (see above), it will always override
        the parameter passed to set_current_renderer, unless it is NULL.
        (i.e., set_current_renderer(foo) =
        set_current_renderer(_default_renderer).
        """
    )

    def _get_default_renderer(self):
        return wrap_vtk(self._vtk_obj.GetDefaultRenderer())
    def _set_default_renderer(self, arg):
        old_val = self._get_default_renderer()
        self._wrap_call(self._vtk_obj.SetDefaultRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('default_renderer', old_val, arg)
    default_renderer = traits.Property(_get_default_renderer, _set_default_renderer, help=\
        """
        Set/Get the default renderer to use when activating the
        interactor observer. Normally when the widget is activated
        (_set_enabled(_1) or when keypress activation takes place), the
        renderer over which the mouse pointer is positioned is used.
        Alternatively, you can specify the renderer to bind the
        interactor to when the interactor observer is activated.
        """
    )

    def _get_interactor(self):
        return wrap_vtk(self._vtk_obj.GetInteractor())
    def _set_interactor(self, arg):
        old_val = self._get_interactor()
        self._wrap_call(self._vtk_obj.SetInteractor,
                        deref_vtk(arg))
        self.trait_property_changed('interactor', old_val, arg)
    interactor = traits.Property(_get_interactor, _set_interactor, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('auto_adjust_camera_clipping_range',
    'GetAutoAdjustCameraClippingRange'), ('handle_observers',
    'GetHandleObservers'), ('use_timers', 'GetUseTimers'), ('enabled',
    'GetEnabled'), ('key_press_activation', 'GetKeyPressActivation'),
    ('picking_managed', 'GetPickingManaged'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('mouse_wheel_motion_factor', 'GetMouseWheelMotionFactor'),
    ('pick_color', 'GetPickColor'), ('timer_duration',
    'GetTimerDuration'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('priority', 'GetPriority'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['auto_adjust_camera_clipping_range', 'debug', 'enabled',
    'global_warning_display', 'handle_observers', 'key_press_activation',
    'picking_managed', 'use_timers', 'key_press_activation_value',
    'mouse_wheel_motion_factor', 'pick_color', 'priority',
    'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorStyleSwitch, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleSwitch properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'picking_managed',
            'use_timers'], [], ['key_press_activation_value',
            'mouse_wheel_motion_factor', 'pick_color', 'priority',
            'timer_duration']),
            title='Edit InteractorStyleSwitch properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleSwitch properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


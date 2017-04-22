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


class InteractorStyleTerrain(InteractorStyle):
    """
    InteractorStyleTerrain - manipulate camera in scene with natural
    view up (e.g., terrain)
    
    Superclass: InteractorStyle
    
    InteractorStyleTerrain is used to manipulate a camera which is
    viewing a scene with a natural view up, e.g., terrain. The camera in
    such a scene is manipulated by specifying azimuth (angle around the
    view up vector) and elevation (the angle from the horizon).
    
    The mouse binding for this class is as follows. Left mouse click
    followed rotates the camera around the focal point using both
    elevation and azimuth invocations on the camera. Left mouse motion in
    the horizontal direction results in azimuth motion; left mouse motion
    in the vertical direction results in elevation motion. Therefore,
    diagonal motion results in a combination of azimuth and elevation.
    (If the shift key is held during motion, then only one of elevation
    or azimuth is invoked, depending on the whether the mouse motion is
    primarily horizontal or vertical.) Middle mouse button pans the
    camera across the scene (again the shift key has a similar effect on
    limiting the motion to the vertical or horizontal direction. The
    right mouse is used to dolly (e.g., a type of zoom) towards or away
    from the focal point.
    
    The class also supports some keypress events. The "r" key resets the
    camera.  The "e" key invokes the exit callback and by default exits
    the program. The "f" key sets a new camera focal point and flys
    towards that point. The "u" key invokes the user event. The "3" key
    toggles between stereo and non-stero mode. The "l" key toggles on/off
    a latitude/longitude markers that can be used to estimate/control
    position.
    
    @sa
    InteractorObserver InteractorStyle ThreeDWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleTerrain, obj, update, **traits)
    
    lat_long_lines = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the latitude/longitude lines.
        """
    )

    def _lat_long_lines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLatLongLines,
                        self.lat_long_lines_)

    _updateable_traits_ = \
    (('lat_long_lines', 'GetLatLongLines'),
    ('auto_adjust_camera_clipping_range',
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
    'lat_long_lines', 'picking_managed', 'use_timers',
    'key_press_activation_value', 'mouse_wheel_motion_factor',
    'pick_color', 'priority', 'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorStyleTerrain, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleTerrain properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'lat_long_lines',
            'picking_managed', 'use_timers'], [], ['key_press_activation_value',
            'mouse_wheel_motion_factor', 'pick_color', 'priority',
            'timer_duration']),
            title='Edit InteractorStyleTerrain properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleTerrain properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


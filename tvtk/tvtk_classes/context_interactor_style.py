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


class ContextInteractorStyle(InteractorStyle):
    """
    ContextInteractorStyle - An interactor for chart views.
    
    Superclass: InteractorStyle
    
    It observes the user events (mouse events) and propagates them to the
    scene. If the scene doesn't eat the event, it is propagated to the
    interactor style superclass.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContextInteractorStyle, obj, update, **traits)
    
    def _get_scene(self):
        return wrap_vtk(self._vtk_obj.GetScene())
    def _set_scene(self, arg):
        old_val = self._get_scene()
        self._wrap_call(self._vtk_obj.SetScene,
                        deref_vtk(arg))
        self.trait_property_changed('scene', old_val, arg)
    scene = traits.Property(_get_scene, _set_scene, help=\
        """
        Return the observed scene.
        """
    )

    def on_scene_modified(self):
        """
        V.on_scene_modified()
        C++: virtual void OnSceneModified()
        Called when the scene is modified. Refresh the scene if needed.
        """
        ret = self._vtk_obj.OnSceneModified()
        return ret
        

    def on_selection(self, *args):
        """
        V.on_selection([int, int, int, int, int])
        C++: virtual void OnSelection(unsigned int rect[5])
        Place holder for future implementation. Default behavior forwards
        the event to the observed scene.
        """
        ret = self._wrap_call(self._vtk_obj.OnSelection, *args)
        return ret

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
            return super(ContextInteractorStyle, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ContextInteractorStyle properties', scrollable=True, resizable=True,
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
            title='Edit ContextInteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContextInteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


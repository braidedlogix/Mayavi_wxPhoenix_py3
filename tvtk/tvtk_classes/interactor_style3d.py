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


class InteractorStyle3D(InteractorStyle):
    """
    InteractorStyle3D - extends interaction to support 3d input
    
    Superclass: InteractorStyle
    
    InteractorStyle3D allows the user to interact with (rotate, pan,
    etc.) objects in the scene indendent of each other. It is designed to
    use 3d positions and orientations instead of 2d.
    
    The following interactions are specified by default.
    
    A click and hold in 3d within the bounding box of a prop will pick up
    that prop allowing you to translate and orient that prop as desired
    with the 3d controller.
    
    Click/dragging two controllers and pulling them apart or pushing them
    together will initial a scale gesture that will scale the world
    larger or smaller.
    
    Click/dragging two controllers and translating them in the same
    direction will translate the camera/world pushing them together will
    initial a scale gesture that will scale the world larger or smaller.
    
    If a controller is right clicked (push touchpad on Vive) then it
    starts a fly motion where the camer moves in the direction the
    controller is pointing. It moves at a speed scaled by the position of
    your thumb on the trackpad. Higher moves faster forward. Lower moves
    faster backwards.
    
    For the Vive left click is mapped to the trigger and right click is
    mapped to pushing the trackpad down.
    
    @sa
    RenderWindowInteractor3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyle3D, obj, update, **traits)
    
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
            return super(InteractorStyle3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyle3D properties', scrollable=True, resizable=True,
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
            title='Edit InteractorStyle3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyle3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


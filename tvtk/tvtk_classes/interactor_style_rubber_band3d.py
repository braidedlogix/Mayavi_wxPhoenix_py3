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

from tvtk.tvtk_classes.interactor_style_trackball_camera import InteractorStyleTrackballCamera


class InteractorStyleRubberBand3D(InteractorStyleTrackballCamera):
    """
    InteractorStyleRubberBand3D - A rubber band interactor for a 3d
    view
    
    Superclass: InteractorStyleTrackballCamera
    
    InteractorStyleRubberBand3D manages interaction in a 3d view. The
    style also allows draws a rubber band using the left button. All
    camera changes invoke start_interaction_event when the button is
    pressed, interaction_event when the mouse (or wheel) is moved, and
    end_interaction_event when the button is released.  The bindings are as
    follows: Left mouse - Select (invokes a selection_changed_event). Right
    mouse - Rotate. Shift + right mouse - Zoom. Middle mouse - Pan.
    Scroll wheel - Zoom.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleRubberBand3D, obj, update, **traits)
    
    render_on_mouse_move = tvtk_base.false_bool_trait(help=\
        """
        Whether to invoke a render when the mouse moves.
        """
    )

    def _render_on_mouse_move_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRenderOnMouseMove,
                        self.render_on_mouse_move_)

    def _get_end_position(self):
        return self._vtk_obj.GetEndPosition()
    end_position = traits.Property(_get_end_position, help=\
        """
        
        """
    )

    def _get_interaction(self):
        return self._vtk_obj.GetInteraction()
    interaction = traits.Property(_get_interaction, help=\
        """
        Current interaction state
        """
    )

    def _get_start_position(self):
        return self._vtk_obj.GetStartPosition()
    start_position = traits.Property(_get_start_position, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('render_on_mouse_move', 'GetRenderOnMouseMove'),
    ('auto_adjust_camera_clipping_range',
    'GetAutoAdjustCameraClippingRange'), ('handle_observers',
    'GetHandleObservers'), ('use_timers', 'GetUseTimers'), ('enabled',
    'GetEnabled'), ('key_press_activation', 'GetKeyPressActivation'),
    ('picking_managed', 'GetPickingManaged'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('motion_factor', 'GetMotionFactor'), ('mouse_wheel_motion_factor',
    'GetMouseWheelMotionFactor'), ('pick_color', 'GetPickColor'),
    ('timer_duration', 'GetTimerDuration'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('priority', 'GetPriority'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['auto_adjust_camera_clipping_range', 'debug', 'enabled',
    'global_warning_display', 'handle_observers', 'key_press_activation',
    'picking_managed', 'render_on_mouse_move', 'use_timers',
    'key_press_activation_value', 'motion_factor',
    'mouse_wheel_motion_factor', 'pick_color', 'priority',
    'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorStyleRubberBand3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleRubberBand3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'picking_managed',
            'render_on_mouse_move', 'use_timers'], [],
            ['key_press_activation_value', 'motion_factor',
            'mouse_wheel_motion_factor', 'pick_color', 'priority',
            'timer_duration']),
            title='Edit InteractorStyleRubberBand3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleRubberBand3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


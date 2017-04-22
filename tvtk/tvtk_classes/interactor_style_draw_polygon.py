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


class InteractorStyleDrawPolygon(InteractorStyle):
    """
    InteractorStyleDrawPolygon - draw polygon during mouse move
    
    Superclass: InteractorStyle
    
    This interactor style allows the user to draw a polygon in the render
    window using the left mouse button while mouse is moving. When the
    mouse button is released, a selection_changed_event will be fired.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleDrawPolygon, obj, update, **traits)
    
    draw_polygon_pixels = tvtk_base.true_bool_trait(help=\
        """
        Whether to draw polygon in screen pixels. Default is ON
        """
    )

    def _draw_polygon_pixels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawPolygonPixels,
                        self.draw_polygon_pixels_)

    _updateable_traits_ = \
    (('draw_polygon_pixels', 'GetDrawPolygonPixels'),
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
    (['auto_adjust_camera_clipping_range', 'debug', 'draw_polygon_pixels',
    'enabled', 'global_warning_display', 'handle_observers',
    'key_press_activation', 'picking_managed', 'use_timers',
    'key_press_activation_value', 'mouse_wheel_motion_factor',
    'pick_color', 'priority', 'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorStyleDrawPolygon, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleDrawPolygon properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_adjust_camera_clipping_range', 'draw_polygon_pixels',
            'enabled', 'handle_observers', 'key_press_activation',
            'picking_managed', 'use_timers'], [], ['key_press_activation_value',
            'mouse_wheel_motion_factor', 'pick_color', 'priority',
            'timer_duration']),
            title='Edit InteractorStyleDrawPolygon properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleDrawPolygon properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


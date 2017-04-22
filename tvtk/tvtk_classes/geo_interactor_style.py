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


class GeoInteractorStyle(InteractorStyleTrackballCamera):
    """
    GeoInteractorStyle - Interaction for a globe
    
    Superclass: InteractorStyleTrackballCamera
    
    GeoInteractorStyle contains interaction capabilities for a
    geographic view including orbit, zoom, and tilt. It also includes a
    compass widget for changing view parameters.
    
    @sa
    CompassWidget InteractorStyle
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoInteractorStyle, obj, update, **traits)
    
    lock_heading = tvtk_base.false_bool_trait(help=\
        """
        Whether to lock the heading a particular value during pan.
        """
    )

    def _lock_heading_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLockHeading,
                        self.lock_heading_)

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

    def _get_interactor(self):
        return wrap_vtk(self._vtk_obj.GetInteractor())
    def _set_interactor(self, arg):
        old_val = self._get_interactor()
        self._wrap_call(self._vtk_obj.SetInteractor,
                        deref_vtk(arg))
        self.trait_property_changed('interactor', old_val, arg)
    interactor = traits.Property(_get_interactor, _set_interactor, help=\
        """
        This method is used to associate the widget with the render
        window interactor.  Observers of the appropriate events invoked
        in the render window interactor are set up as a result of this
        method invocation. The set_interactor() method must be invoked
        prior to enabling the InteractorObserver. It automatically
        registers available pickers to the Picking Manager.
        """
    )

    def _get_geo_camera(self):
        return wrap_vtk(self._vtk_obj.GetGeoCamera())
    geo_camera = traits.Property(_get_geo_camera, help=\
        """
        
        """
    )

    def get_ray_intersection(self, *args):
        """
        V.get_ray_intersection([float, float, float], [float, float, float],
             [float, float, float]) -> int
        C++: int GetRayIntersection(double origin[3], double direction[3],
             double intersection[3])"""
        ret = self._wrap_call(self._vtk_obj.GetRayIntersection, *args)
        return ret

    def redraw_rectangle(self):
        """
        V.redraw_rectangle()
        C++: void RedrawRectangle()"""
        ret = self._vtk_obj.RedrawRectangle()
        return ret
        

    def reset_camera(self):
        """
        V.reset_camera()
        C++: void ResetCamera()
        This can be used to set the camera to the standard view of the
        earth.
        """
        ret = self._vtk_obj.ResetCamera()
        return ret
        

    def reset_camera_clipping_range(self):
        """
        V.reset_camera_clipping_range()
        C++: void ResetCameraClippingRange()
        Called after camera properties are modified
        """
        ret = self._vtk_obj.ResetCameraClippingRange()
        return ret
        

    def rubber_band_zoom(self):
        """
        V.rubber_band_zoom()
        C++: virtual void RubberBandZoom()"""
        ret = self._vtk_obj.RubberBandZoom()
        return ret
        

    def viewport_to_long_lat(self, *args):
        """
        V.viewport_to_long_lat(float, float, float, float)
        C++: void ViewportToLongLat(double x, double y, double &lon,
            double &lat)"""
        ret = self._wrap_call(self._vtk_obj.ViewportToLongLat, *args)
        return ret

    def viewport_to_world(self, *args):
        """
        V.viewport_to_world(float, float, float, float, float) -> int
        C++: int ViewportToWorld(double x, double y, double &wx,
            double &wy, double &wz)"""
        ret = self._wrap_call(self._vtk_obj.ViewportToWorld, *args)
        return ret

    def widget_interaction(self, *args):
        """
        V.widget_interaction(Object)
        C++: void WidgetInteraction(Object *caller)
        Called when the sub widgets have an interaction
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.WidgetInteraction, *my_args)
        return ret

    def world_to_long_lat(self, *args):
        """
        V.world_to_long_lat(float, float, float, float, float)
        C++: void WorldToLongLat(double wx, double wy, double wz,
            double &lon, double &lat)"""
        ret = self._wrap_call(self._vtk_obj.WorldToLongLat, *args)
        return ret

    _updateable_traits_ = \
    (('lock_heading', 'GetLockHeading'),
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
    'lock_heading', 'picking_managed', 'use_timers',
    'key_press_activation_value', 'motion_factor',
    'mouse_wheel_motion_factor', 'pick_color', 'priority',
    'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoInteractorStyle, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoInteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'lock_heading',
            'picking_managed', 'use_timers'], [], ['key_press_activation_value',
            'motion_factor', 'mouse_wheel_motion_factor', 'pick_color',
            'priority', 'timer_duration']),
            title='Edit GeoInteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoInteractorStyle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


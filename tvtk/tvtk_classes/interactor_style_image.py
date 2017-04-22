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


class InteractorStyleImage(InteractorStyleTrackballCamera):
    """
    InteractorStyleImage - interactive manipulation of the camera
    specialized for images
    
    Superclass: InteractorStyleTrackballCamera
    
    InteractorStyleImage allows the user to interactively manipulate
    (rotate, pan, zoom etc.) the camera. InteractorStyleImage is
    specially designed to work with images that are being rendered with
    ImageActor. Several events are overloaded from its superclass
    InteractorStyle, hence the mouse bindings are different. (The
    bindings keep the camera's view plane normal perpendicular to the x-y
    plane.) In summary the mouse events for 2d image interaction are as
    follows:
    - Left Mouse button triggers window level events
    - CTRL Left Mouse spins the camera around its view plane normal
    - SHIFT Left Mouse pans the camera
    - CTRL SHIFT Left Mouse dollys (a positional zoom) the camera
    - Middle mouse button pans the camera
    - Right mouse button dollys the camera.
    - SHIFT Right Mouse triggers pick events
    
    If set_interaction_mode_to_image_slicing() is called, then some of the
    mouse events are changed as follows:
    - CTRL Left Mouse slices through the image
    - SHIFT Middle Mouse slices through the image
    - CTRL Right Mouse spins the camera
    
    If set_interaction_mode_to_image3d() is called, then some of the mouse
    events are changed as follows:
    - SHIFT Left Mouse rotates the camera for oblique slicing
    - SHIFT Middle Mouse slices through the image
    - CTRL Right Mouse also slices through the image
    
    In all modes, the following key bindings are in effect:
    - R Reset the Window/Level
    - X Reset to a sagittal view
    - Y Reset to a coronal view
    - Z Reset to an axial view
    
    Note that the renderer's actors are not moved; instead the camera is
    moved.
    
    @sa
    InteractorStyle InteractorStyleTrackballActor
    InteractorStyleJoystickCamera InteractorStyleJoystickActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleImage, obj, update, **traits)
    
    interaction_mode = traits.Trait('image2d',
    tvtk_base.TraitRevPrefixMap({'image2d': 2, 'image3d': 3, 'image_slicing': 4}), help=\
        """
        Set/Get current mode to 2d or 3d.  The default is 2d.  In 3d
        mode, it is possible to rotate the camera to view oblique slices.
         In Slicing mode, it is possible to slice through the data, but
        not to generate oblique views by rotating the camera.
        """
    )

    def _interaction_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteractionMode,
                        self.interaction_mode_)

    current_image_number = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the image to use for window_level interaction. Any images for
        which the Pickable flag is off are ignored. Images are counted
        back-to-front, so 0 is the rearmost image. Negative values can be
        used to count front-to-back, so -1 is the frontmost image, -2 is
        the image behind that one, etc. The default is to use the
        frontmost image for interaction. If the specified image does not
        exist, then no window_level interaction will take place.
        """
    )

    def _current_image_number_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCurrentImageNumber,
                        self.current_image_number)

    x_view_right_vector = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 1.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _x_view_right_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXViewRightVector,
                        self.x_view_right_vector)

    x_view_up_vector = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, -1.0), cols=3, help=\
        """
        
        """
    )

    def _x_view_up_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXViewUpVector,
                        self.x_view_up_vector)

    y_view_right_vector = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _y_view_right_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYViewRightVector,
                        self.y_view_right_vector)

    y_view_up_vector = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, -1.0), cols=3, help=\
        """
        
        """
    )

    def _y_view_up_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYViewUpVector,
                        self.y_view_up_vector)

    z_view_right_vector = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _z_view_right_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZViewRightVector,
                        self.z_view_right_vector)

    z_view_up_vector = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 1.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _z_view_up_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZViewUpVector,
                        self.z_view_up_vector)

    def _get_current_image_property(self):
        return wrap_vtk(self._vtk_obj.GetCurrentImageProperty())
    current_image_property = traits.Property(_get_current_image_property, help=\
        """
        Get the current image property, which is set when
        start_window_level is called immediately before
        start_window_level_event is generated. This is the image property of
        the topmost ImageSlice in the renderer or NULL if no image
        actors are present.
        """
    )

    def _get_window_level_current_position(self):
        return self._vtk_obj.GetWindowLevelCurrentPosition()
    window_level_current_position = traits.Property(_get_window_level_current_position, help=\
        """
        
        """
    )

    def _get_window_level_start_position(self):
        return self._vtk_obj.GetWindowLevelStartPosition()
    window_level_start_position = traits.Property(_get_window_level_start_position, help=\
        """
        
        """
    )

    def end_pick(self):
        """
        V.end_pick()
        C++: virtual void EndPick()"""
        ret = self._vtk_obj.EndPick()
        return ret
        

    def end_slice(self):
        """
        V.end_slice()
        C++: virtual void EndSlice()"""
        ret = self._vtk_obj.EndSlice()
        return ret
        

    def end_window_level(self):
        """
        V.end_window_level()
        C++: virtual void EndWindowLevel()"""
        ret = self._vtk_obj.EndWindowLevel()
        return ret
        

    def pick(self):
        """
        V.pick()
        C++: virtual void Pick()"""
        ret = self._vtk_obj.Pick()
        return ret
        

    def set_image_orientation(self, *args):
        """
        V.set_image_orientation((float, float, float), (float, float, float)
            )
        C++: void SetImageOrientation(const double leftToRight[3],
            const double bottomToTop[3])
        Set the view orientation, in terms of the horizontal and vertical
        directions of the computer screen.  The first vector gives the
        direction that will correspond to moving horizontally
        left-to-right across the screen, and the second vector gives the
        direction that will correspond to moving bottom-to-top up the
        screen.  This method changes the position of the camera to
        provide the desired view.
        """
        ret = self._wrap_call(self._vtk_obj.SetImageOrientation, *args)
        return ret

    def slice(self):
        """
        V.slice()
        C++: virtual void Slice()"""
        ret = self._vtk_obj.Slice()
        return ret
        

    def start_pick(self):
        """
        V.start_pick()
        C++: virtual void StartPick()"""
        ret = self._vtk_obj.StartPick()
        return ret
        

    def start_slice(self):
        """
        V.start_slice()
        C++: virtual void StartSlice()"""
        ret = self._vtk_obj.StartSlice()
        return ret
        

    def start_window_level(self):
        """
        V.start_window_level()
        C++: virtual void StartWindowLevel()"""
        ret = self._vtk_obj.StartWindowLevel()
        return ret
        

    def window_level(self):
        """
        V.window_level()
        C++: virtual void WindowLevel()"""
        ret = self._vtk_obj.WindowLevel()
        return ret
        

    _updateable_traits_ = \
    (('auto_adjust_camera_clipping_range',
    'GetAutoAdjustCameraClippingRange'), ('handle_observers',
    'GetHandleObservers'), ('use_timers', 'GetUseTimers'), ('enabled',
    'GetEnabled'), ('key_press_activation', 'GetKeyPressActivation'),
    ('picking_managed', 'GetPickingManaged'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('interaction_mode', 'GetInteractionMode'), ('current_image_number',
    'GetCurrentImageNumber'), ('x_view_right_vector',
    'GetXViewRightVector'), ('x_view_up_vector', 'GetXViewUpVector'),
    ('y_view_right_vector', 'GetYViewRightVector'), ('y_view_up_vector',
    'GetYViewUpVector'), ('z_view_right_vector', 'GetZViewRightVector'),
    ('z_view_up_vector', 'GetZViewUpVector'), ('motion_factor',
    'GetMotionFactor'), ('mouse_wheel_motion_factor',
    'GetMouseWheelMotionFactor'), ('pick_color', 'GetPickColor'),
    ('timer_duration', 'GetTimerDuration'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('priority', 'GetPriority'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['auto_adjust_camera_clipping_range', 'debug', 'enabled',
    'global_warning_display', 'handle_observers', 'key_press_activation',
    'picking_managed', 'use_timers', 'interaction_mode',
    'current_image_number', 'key_press_activation_value', 'motion_factor',
    'mouse_wheel_motion_factor', 'pick_color', 'priority',
    'timer_duration', 'x_view_right_vector', 'x_view_up_vector',
    'y_view_right_vector', 'y_view_up_vector', 'z_view_right_vector',
    'z_view_up_vector'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorStyleImage, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'picking_managed',
            'use_timers'], ['interaction_mode'], ['current_image_number',
            'key_press_activation_value', 'motion_factor',
            'mouse_wheel_motion_factor', 'pick_color', 'priority',
            'timer_duration', 'x_view_right_vector', 'x_view_up_vector',
            'y_view_right_vector', 'y_view_up_vector', 'z_view_right_vector',
            'z_view_up_vector']),
            title='Edit InteractorStyleImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


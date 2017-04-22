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


class RenderWindowInteractor3D(RenderWindowInteractor):
    """
    RenderWindowInteractor3D - adds support for 3d events to
    RenderWindowInteractor.
    
    Superclass: RenderWindowInteractor
    
    RenderWindowInteractor3D provides a platform-independent
    interaction support for 3d events including 3d clicks and 3d
    controller orientations. It follows the same basic model as
    RenderWindowInteractor but adds methods to set and get 3d event
    locations and orientations. VR systems will subclass this class to
    provide the code to set these values based on events from their VR
    controllers.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderWindowInteractor3D, obj, update, **traits)
    
    def get_physical_translation(self, *args):
        """
        V.get_physical_translation(Camera) -> (float, ...)
        C++: virtual double *GetPhysicalTranslation(Camera *)
        Set/Get the optional translation to map world coordinates into
        the 3d physical space (meters, 0,0,0).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPhysicalTranslation, *my_args)
        return ret

    def set_physical_translation(self, *args):
        """
        V.set_physical_translation(Camera, float, float, float)
        C++: virtual void SetPhysicalTranslation(Camera *, double,
            double, double)
        Set/Get the optional translation to map world coordinates into
        the 3d physical space (meters, 0,0,0).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPhysicalTranslation, *my_args)
        return ret

    touch_pad_position = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(-6280072658944.0, 8.674037494170618e-43), cols=2, help=\
        """
        
        """
    )

    def _touch_pad_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTouchPadPosition,
                        self.touch_pad_position)

    translation3d = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.315278590464e-311, 1.315274863387e-311, 1.3152785340616e-311), cols=3, help=\
        """
        Set/get the tranlation for pan/swipe gestures, update
        last_translation
        """
    )

    def _translation3d_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslation3D,
                        self.translation3d)

    def get_world_event_orientation(self, *args):
        """
        V.get_world_event_orientation(int) -> (float, ...)
        C++: virtual double *GetWorldEventOrientation(int pointerIndex)
        With VR we know the world coordinate positions and orientations
        of events. These methods support querying them instead of going
        through a display X,Y coordinate approach as is standard for
        mouse/touch events
        """
        ret = self._wrap_call(self._vtk_obj.GetWorldEventOrientation, *args)
        return ret

    def set_world_event_orientation(self, *args):
        """
        V.set_world_event_orientation(float, float, float, float, int)
        C++: virtual void SetWorldEventOrientation(double w, double x,
            double y, double z, int pointerIndex)
        With VR we know the world coordinate positions and orientations
        of events. These methods support setting them.
        """
        ret = self._wrap_call(self._vtk_obj.SetWorldEventOrientation, *args)
        return ret

    def get_world_event_position(self, *args):
        """
        V.get_world_event_position(int) -> (float, ...)
        C++: virtual double *GetWorldEventPosition(int pointerIndex)
        With VR we know the world coordinate positions and orientations
        of events. These methods support querying them instead of going
        through a display X,Y coordinate approach as is standard for
        mouse/touch events
        """
        ret = self._wrap_call(self._vtk_obj.GetWorldEventPosition, *args)
        return ret

    def set_world_event_position(self, *args):
        """
        V.set_world_event_position(float, float, float, int)
        C++: virtual void SetWorldEventPosition(double x, double y,
            double z, int pointerIndex)
        With VR we know the world coordinate positions and orientations
        of events. These methods support setting them.
        """
        ret = self._wrap_call(self._vtk_obj.SetWorldEventPosition, *args)
        return ret

    def _get_last_translation3d(self):
        return self._vtk_obj.GetLastTranslation3D()
    last_translation3d = traits.Property(_get_last_translation3d, help=\
        """
        
        """
    )

    def get_last_world_event_orientation(self, *args):
        """
        V.get_last_world_event_orientation(int) -> (float, ...)
        C++: virtual double *GetLastWorldEventOrientation(
            int pointerIndex)
        With VR we know the world coordinate positions and orientations
        of events. These methods support querying them instead of going
        through a display X,Y coordinate approach as is standard for
        mouse/touch events
        """
        ret = self._wrap_call(self._vtk_obj.GetLastWorldEventOrientation, *args)
        return ret

    def get_last_world_event_position(self, *args):
        """
        V.get_last_world_event_position(int) -> (float, ...)
        C++: virtual double *GetLastWorldEventPosition(int pointerIndex)
        With VR we know the world coordinate positions and orientations
        of events. These methods support querying them instead of going
        through a display X,Y coordinate approach as is standard for
        mouse/touch events
        """
        ret = self._wrap_call(self._vtk_obj.GetLastWorldEventPosition, *args)
        return ret

    def set_physical_event_position(self, *args):
        """
        V.set_physical_event_position(float, float, float, int)
        C++: virtual void SetPhysicalEventPosition(double x, double y,
            double z, int pointerIndex)
        With VR we know the physical/room coordinate positions and
        orientations of events. These methods support setting them.
        """
        ret = self._wrap_call(self._vtk_obj.SetPhysicalEventPosition, *args)
        return ret

    _updateable_traits_ = \
    (('enable_render', 'GetEnableRender'), ('light_follow_camera',
    'GetLightFollowCamera'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('touch_pad_position', 'GetTouchPadPosition'), ('translation3d',
    'GetTranslation3D'), ('alt_key', 'GetAltKey'), ('control_key',
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
    'light_follow_camera', 'alt_key', 'control_key',
    'desired_update_rate', 'dolly', 'event_position', 'event_size',
    'key_code', 'key_sym', 'last_event_position', 'number_of_fly_frames',
    'pointer_index', 'recognize_gestures', 'repeat_count', 'rotation',
    'scale', 'shift_key', 'size', 'still_update_rate', 'timer_duration',
    'timer_event_duration', 'timer_event_id', 'timer_event_platform_id',
    'timer_event_type', 'touch_pad_position', 'translation',
    'translation3d', 'use_t_dx'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderWindowInteractor3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderWindowInteractor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enable_render', 'light_follow_camera'], [], ['alt_key',
            'control_key', 'desired_update_rate', 'dolly', 'event_position',
            'event_size', 'key_code', 'key_sym', 'last_event_position',
            'number_of_fly_frames', 'pointer_index', 'recognize_gestures',
            'repeat_count', 'rotation', 'scale', 'shift_key', 'size',
            'still_update_rate', 'timer_duration', 'timer_event_duration',
            'timer_event_id', 'timer_event_platform_id', 'timer_event_type',
            'touch_pad_position', 'translation', 'translation3d', 'use_t_dx']),
            title='Edit RenderWindowInteractor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderWindowInteractor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


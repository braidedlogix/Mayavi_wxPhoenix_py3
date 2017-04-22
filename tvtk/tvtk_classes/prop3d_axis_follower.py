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

from tvtk.tvtk_classes.prop3d_follower import Prop3DFollower


class Prop3DAxisFollower(Prop3DFollower):
    """
    Prop3DAxisFollower - a subclass of Prop3DFollower that ensures
    that data is always parallel to the axis defined by a AxisActor.
    
    Superclass: Prop3DFollower
    
    Prop3DAxisFollower is a subclass of Prop3DFollower that always
    follows its specified axis. More specifically it will not change its
    position or scale, but it will continually update its orientation so
    that it is aligned with the axis and facing at angle to the camera to
    provide maximum visibilty. This is typically used for text labels for
    3d plots.
    @sa
    Follower AxisFollower Prop3DFollower
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProp3DAxisFollower, obj, update, **traits)
    
    auto_center = tvtk_base.true_bool_trait(help=\
        """
        Set/Get state of auto center mode where additional translation
        will be added to make sure the underlying geometry has its pivot
        point at the center of its bounds.
        """
    )

    def _auto_center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoCenter,
                        self.auto_center_)

    def _get_axis(self):
        return wrap_vtk(self._vtk_obj.GetAxis())
    def _set_axis(self, arg):
        old_val = self._get_axis()
        self._wrap_call(self._vtk_obj.SetAxis,
                        deref_vtk(arg))
        self.trait_property_changed('axis', old_val, arg)
    axis = traits.Property(_get_axis, _set_axis, help=\
        """
        Set axis that needs to be followed.
        """
    )

    distance_lod_threshold = traits.Trait(0.8, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set distance LOD threshold (0.0 - 1.0).This determines at what
        fraction of camera far clip range, actor is not visible. Default
        is 0.80.
        """
    )

    def _distance_lod_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistanceLODThreshold,
                        self.distance_lod_threshold)

    enable_distance_lod = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Enable / disable use of distance based LOD. If enabled the actor
        will not be visible at a certain distance from the camera.
        Default is false.
        """
    )

    def _enable_distance_lod_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableDistanceLOD,
                        self.enable_distance_lod)

    enable_view_angle_lod = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Enable / disable use of view angle based LOD. If enabled the
        actor will not be visible at a certain view angle. Default is
        true.
        """
    )

    def _enable_view_angle_lod_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableViewAngleLOD,
                        self.enable_view_angle_lod)

    screen_offset = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the desired screen vertical offset from the axis.
        Convenience method, using a zero horizontal offset
        """
    )

    def _screen_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScreenOffset,
                        self.screen_offset)

    screen_offset_vector = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 10.0), cols=2, help=\
        """
        
        """
    )

    def _screen_offset_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScreenOffsetVector,
                        self.screen_offset_vector)

    view_angle_lod_threshold = traits.Trait(0.34, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set view angle LOD threshold (0.0 - 1.0).This determines at what
        view angle to geometry will make the geometry not visibile.
        Default is 0.34.
        """
    )

    def _view_angle_lod_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetViewAngleLODThreshold,
                        self.view_angle_lod_threshold)

    def _get_viewport(self):
        return wrap_vtk(self._vtk_obj.GetViewport())
    def _set_viewport(self, arg):
        old_val = self._get_viewport()
        self._wrap_call(self._vtk_obj.SetViewport,
                        deref_vtk(arg))
        self.trait_property_changed('viewport', old_val, arg)
    viewport = traits.Property(_get_viewport, _set_viewport, help=\
        """
        
        """
    )

    def auto_scale(self, *args):
        """
        V.auto_scale(Viewport, Camera, float, [float, float, float])
            -> float
        C++: static double AutoScale(Viewport *viewport,
            Camera *camera, double screenSize, double position[3])
        Calculate scale factor to maintain same size of a object on the
        screen.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AutoScale, *my_args)
        return ret

    _updateable_traits_ = \
    (('auto_center', 'GetAutoCenter'), ('dragable', 'GetDragable'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('distance_lod_threshold', 'GetDistanceLODThreshold'),
    ('enable_distance_lod', 'GetEnableDistanceLOD'),
    ('enable_view_angle_lod', 'GetEnableViewAngleLOD'), ('screen_offset',
    'GetScreenOffset'), ('screen_offset_vector', 'GetScreenOffsetVector'),
    ('view_angle_lod_threshold', 'GetViewAngleLODThreshold'),
    ('orientation', 'GetOrientation'), ('origin', 'GetOrigin'),
    ('position', 'GetPosition'), ('scale', 'GetScale'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['auto_center', 'debug', 'dragable', 'global_warning_display',
    'pickable', 'use_bounds', 'visibility', 'distance_lod_threshold',
    'enable_distance_lod', 'enable_view_angle_lod',
    'estimated_render_time', 'orientation', 'origin', 'position',
    'render_time_multiplier', 'scale', 'screen_offset',
    'screen_offset_vector', 'view_angle_lod_threshold'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Prop3DAxisFollower, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Prop3DAxisFollower properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_center', 'use_bounds', 'visibility'], [],
            ['distance_lod_threshold', 'enable_distance_lod',
            'enable_view_angle_lod', 'estimated_render_time', 'orientation',
            'origin', 'position', 'render_time_multiplier', 'scale',
            'screen_offset', 'screen_offset_vector', 'view_angle_lod_threshold']),
            title='Edit Prop3DAxisFollower properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Prop3DAxisFollower properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


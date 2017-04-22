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

from tvtk.tvtk_classes.handle_representation import HandleRepresentation


class PointHandleRepresentation3D(HandleRepresentation):
    """
    PointHandleRepresentation3D - represent the position of a point in
    3d space
    
    Superclass: HandleRepresentation
    
    This class is used to represent a HandleWidget. It represents a
    position in 3d world coordinates using a x-y-z cursor. The cursor can
    be configured to show a bounding box and/or shadows.
    
    @sa
    HandleRepresentation HandleWidget Cursor3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointHandleRepresentation3D, obj, update, **traits)
    
    outline = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the wireframe bounding box.
        """
    )

    def _outline_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutline,
                        self.outline_)

    smooth_motion = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off smooth motion of the handle. See the documentation of
        move_focus_request for details. By default, smooth_motion is ON.
        However, in certain applications the user may want to turn it
        off. For instance when using certain specific point_placer's with
        the representation such as the CellCentersPointPlacer, which
        causes the representation to snap to the center of cells, or
        using a PolygonalSurfacePointPlacer which constrains the
        widget to the surface of a mesh. In such cases, inherent
        restrictions on handle placement might conflict with a request
        for smooth motion of the handles.
        """
    )

    def _smooth_motion_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSmoothMotion,
                        self.smooth_motion_)

    translation_mode = tvtk_base.true_bool_trait(help=\
        """
        If translation mode is on, as the widget is moved the bounding
        box, shadows, and cursor are all translated and sized
        simultaneously as the point moves (i.e., the left and middle
        mouse buttons act the same). If translation mode is off, the
        cursor does not scale itself (based on the specified handle
        size), and the bounding box and shadows do not move or size
        themselves as the cursor focal point moves, which is constrained
        by the bounds of the point representation. (Note that the bounds
        can be scaled up using the right mouse button, and the bounds can
        be manually set with the set_bounds() method.)
        """
    )

    def _translation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslationMode,
                        self.translation_mode_)

    x_shadows = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the wireframe x-shadows.
        """
    )

    def _x_shadows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXShadows,
                        self.x_shadows_)

    y_shadows = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the wireframe y-shadows.
        """
    )

    def _y_shadows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYShadows,
                        self.y_shadows_)

    z_shadows = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the wireframe z-shadows.
        """
    )

    def _z_shadows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZShadows,
                        self.z_shadows_)

    display_position = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set the position of the point in world and display coordinates.
        Note that if the position is set outside of the bounding box, it
        will be clamped to the boundary of the bounding box. This method
        overloads the superclasses' set_world_position() and
        set_display_position() in order to set the focal point of the
        cursor properly.
        """
    )

    def _display_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayPosition,
                        self.display_position)

    handle_size = traits.Float(15.0, enter_set=True, auto_set=False, help=\
        """
        Overload the superclasses set_handle_size() method to update
        internal variables.
        """
    )

    def _handle_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleSize,
                        self.handle_size)

    hot_spot_size = traits.Trait(0.05, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set the "hot spot" size; i.e., the region around the focus, in
        which the motion vector is used to control the constrained
        sliding action. Note the size is specified as a fraction of the
        length of the diagonal of the point widget's bounding box.
        """
    )

    def _hot_spot_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHotSpotSize,
                        self.hot_spot_size)

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    def _set_property(self, arg):
        old_val = self._get_property()
        self._wrap_call(self._vtk_obj.SetProperty,
                        deref_vtk(arg))
        self.trait_property_changed('property', old_val, arg)
    property = traits.Property(_get_property, _set_property, help=\
        """
        Set/Get the handle properties when unselected and selected.
        """
    )

    def _get_selected_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedProperty())
    def _set_selected_property(self, arg):
        old_val = self._get_selected_property()
        self._wrap_call(self._vtk_obj.SetSelectedProperty,
                        deref_vtk(arg))
        self.trait_property_changed('selected_property', old_val, arg)
    selected_property = traits.Property(_get_selected_property, _set_selected_property, help=\
        """
        Set/Get the handle properties when unselected and selected.
        """
    )

    world_position = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set the position of the point in world and display coordinates.
        Note that if the position is set outside of the bounding box, it
        will be clamped to the boundary of the bounding box. This method
        overloads the superclasses' set_world_position() and
        set_display_position() in order to set the focal point of the
        cursor properly.
        """
    )

    def _world_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWorldPosition,
                        self.world_position)

    def all_off(self):
        """
        V.all_off()
        C++: void AllOff()
        Convenience methods to turn outline and shadows on and off.
        """
        ret = self._vtk_obj.AllOff()
        return ret
        

    def all_on(self):
        """
        V.all_on()
        C++: void AllOn()
        Convenience methods to turn outline and shadows on and off.
        """
        ret = self._vtk_obj.AllOn()
        return ret
        

    _updateable_traits_ = \
    (('outline', 'GetOutline'), ('smooth_motion', 'GetSmoothMotion'),
    ('translation_mode', 'GetTranslationMode'), ('x_shadows',
    'GetXShadows'), ('y_shadows', 'GetYShadows'), ('z_shadows',
    'GetZShadows'), ('active_representation', 'GetActiveRepresentation'),
    ('constrained', 'GetConstrained'), ('need_to_render',
    'GetNeedToRender'), ('picking_managed', 'GetPickingManaged'),
    ('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('display_position',
    'GetDisplayPosition'), ('handle_size', 'GetHandleSize'),
    ('hot_spot_size', 'GetHotSpotSize'), ('world_position',
    'GetWorldPosition'), ('interaction_state', 'GetInteractionState'),
    ('tolerance', 'GetTolerance'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['active_representation', 'constrained', 'debug', 'dragable',
    'global_warning_display', 'need_to_render', 'outline', 'pickable',
    'picking_managed', 'smooth_motion', 'translation_mode', 'use_bounds',
    'visibility', 'x_shadows', 'y_shadows', 'z_shadows',
    'display_position', 'estimated_render_time', 'handle_size',
    'hot_spot_size', 'interaction_state', 'place_factor',
    'render_time_multiplier', 'tolerance', 'world_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointHandleRepresentation3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PointHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['active_representation', 'constrained', 'need_to_render',
            'outline', 'picking_managed', 'smooth_motion', 'translation_mode',
            'use_bounds', 'visibility', 'x_shadows', 'y_shadows', 'z_shadows'],
            [], ['display_position', 'estimated_render_time', 'handle_size',
            'hot_spot_size', 'interaction_state', 'place_factor',
            'render_time_multiplier', 'tolerance', 'world_position']),
            title='Edit PointHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


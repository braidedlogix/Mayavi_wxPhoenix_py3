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

from tvtk.tvtk_classes.widget_representation import WidgetRepresentation


class ImplicitPlaneRepresentation(WidgetRepresentation):
    """
    ImplicitPlaneRepresentation - a class defining the representation
    for a ImplicitPlaneWidget2
    
    Superclass: WidgetRepresentation
    
    This class is a concrete representation for the
    ImplicitPlaneWidget2. It represents an infinite plane defined by a
    normal and point in the context of a bounding box. Through
    interaction with the widget, the plane can be manipulated by
    adjusting the plane normal or moving the origin point.
    
    To use this representation, you normally define a (plane) origin and
    (plane) normal. The place_widget() method is also used to initially
    position the representation.
    
    @warning
    This class, and ImplicitPlaneWidget2, are next generation VTK
    widgets. An earlier version of this functionality was defined in the
    class ImplicitPlaneWidget.
    
    @sa
    ImplicitPlaneWidget2 ImplicitPlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitPlaneRepresentation, obj, update, **traits)
    
    constrain_to_widget_bounds = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off whether the plane should be constrained to the widget
        bounds. If on, the origin will not be allowed to move outside the
        set widget bounds. This is the default behaviour. If off, the
        origin can be freely moved and the widget outline will change
        accordingly.
        """
    )

    def _constrain_to_widget_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConstrainToWidgetBounds,
                        self.constrain_to_widget_bounds_)

    draw_plane = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable the drawing of the plane. In some cases the plane
        interferes with the object that it is operating on (i.e., the
        plane interferes with the cut surface it produces producing
        z-buffer artifacts.)
        """
    )

    def _draw_plane_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawPlane,
                        self.draw_plane_)

    lock_normal_to_camera = tvtk_base.false_bool_trait(help=\
        """
        If enabled, and a Camera is available through the renderer,
        then lock_normal_to_camera will cause the normal to follow the
        camera's normal.
        """
    )

    def _lock_normal_to_camera_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLockNormalToCamera,
                        self.lock_normal_to_camera_)

    normal_to_x_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a modified_event is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
        """
    )

    def _normal_to_x_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalToXAxis,
                        self.normal_to_x_axis_)

    normal_to_y_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a modified_event is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
        """
    )

    def _normal_to_y_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalToYAxis,
                        self.normal_to_y_axis_)

    normal_to_z_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a modified_event is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
        """
    )

    def _normal_to_z_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalToZAxis,
                        self.normal_to_z_axis_)

    outline_translation = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the ability to translate the bounding box by grabbing
        it with the left mouse button.
        """
    )

    def _outline_translation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutlineTranslation,
                        self.outline_translation_)

    outside_bounds = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the ability to move the widget outside of the bounds
        specified in the initial place_widget() invocation.
        """
    )

    def _outside_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutsideBounds,
                        self.outside_bounds_)

    scale_enabled = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the ability to scale the widget with the mouse.
        """
    )

    def _scale_enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleEnabled,
                        self.scale_enabled_)

    tubing = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off tubing of the wire outline of the plane. The tube
        thickens the line by wrapping with a TubeFilter.
        """
    )

    def _tubing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTubing,
                        self.tubing_)

    normal = traits.Trait('camera',
    tvtk_base.TraitRevPrefixMap({'camera': (1.0, 0.0, 0.0)}), help=\
        """
        Get the normal to the plane.
        """
    )

    def _normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormal,
                        self.normal_)

    bump_distance = traits.Trait(0.01, traits.Range(1e-06, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify a translation distance used by the bump_plane() method.
        Note that the distance is normalized; it is the fraction of the
        length of the bounding box of the wire outline.
        """
    )

    def _bump_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBumpDistance,
                        self.bump_distance)

    interaction_state = traits.Trait(0, traits.Range(0, 6, enter_set=True, auto_set=False), help=\
        """
        The interaction state may be set from a widget (e.g.,
        ImplicitPlaneWidget2) or other object. This controls how the
        interaction with the widget proceeds. Normally this method is
        used as part of a handshaking process with the widget: First
        compute_interaction_state() is invoked that returns a state based
        on geometric considerations (i.e., cursor near a widget feature),
        then based on events, the widget may modify this further.
        """
    )

    def _interaction_state_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteractionState,
                        self.interaction_state)

    origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Get the origin of the plane.
        """
    )

    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    def get_plane(self, *args):
        """
        V.get_plane(Plane)
        C++: void GetPlane(Plane *plane)
        Get the implicit function for the plane by copying the origin and
        normal of the cut plane into the provided Plane. The user must
        provide the instance of the class Plane. Note that Plane is
        a subclass of ImplicitFunction, meaning that it can be used by
        a variety of filters to perform clipping, cutting, and selection
        of data.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPlane, *my_args)
        return ret

    def set_plane(self, *args):
        """
        V.set_plane(Plane)
        C++: void SetPlane(Plane *plane)
        Alternative way to define the cutting plane. The normal and
        origin of the plane provided is copied into the internal instance
        of the class cutting Plane.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPlane, *my_args)
        return ret

    representation_state = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Sets the visual appearance of the representation based on the
        state it is in. This state is usually the same as
        interaction_state.
        """
    )

    def _representation_state_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRepresentationState,
                        self.representation_state)

    widget_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(-0.25, 0.25, -0.25, 0.25, -0.25, 0.25), cols=3, help=\
        """
        
        """
    )

    def _widget_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWidgetBounds,
                        self.widget_bounds)

    def _get_edges_property(self):
        return wrap_vtk(self._vtk_obj.GetEdgesProperty())
    edges_property = traits.Property(_get_edges_property, help=\
        """
        Get the property of the intersection edges. (This property also
        applies to the edges when tubed.)
        """
    )

    def _get_normal_property(self):
        return wrap_vtk(self._vtk_obj.GetNormalProperty())
    normal_property = traits.Property(_get_normal_property, help=\
        """
        Get the properties on the normal (line and cone).
        """
    )

    def _get_outline_property(self):
        return wrap_vtk(self._vtk_obj.GetOutlineProperty())
    outline_property = traits.Property(_get_outline_property, help=\
        """
        Get the property of the outline.
        """
    )

    def _get_plane_property(self):
        return wrap_vtk(self._vtk_obj.GetPlaneProperty())
    plane_property = traits.Property(_get_plane_property, help=\
        """
        Get the plane properties. The properties of the plane when
        selected and unselected can be manipulated.
        """
    )

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: void GetPolyData(PolyData *pd)
        Grab the polydata that defines the plane. The polydata contains a
        single polygon that is clipped by the bounding box.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_poly_data_algorithm(self):
        return wrap_vtk(self._vtk_obj.GetPolyDataAlgorithm())
    poly_data_algorithm = traits.Property(_get_poly_data_algorithm, help=\
        """
        Satisfies superclass API.  This returns a pointer to the
        underlying poly_data (which represents the plane).
        """
    )

    def _get_selected_normal_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedNormalProperty())
    selected_normal_property = traits.Property(_get_selected_normal_property, help=\
        """
        Get the properties on the normal (line and cone).
        """
    )

    def _get_selected_outline_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedOutlineProperty())
    selected_outline_property = traits.Property(_get_selected_outline_property, help=\
        """
        Get the property of the outline.
        """
    )

    def _get_selected_plane_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedPlaneProperty())
    selected_plane_property = traits.Property(_get_selected_plane_property, help=\
        """
        Get the plane properties. The properties of the plane when
        selected and unselected can be manipulated.
        """
    )

    def bump_plane(self, *args):
        """
        V.bump_plane(int, float)
        C++: void BumpPlane(int dir, double factor)
        Translate the plane in the direction of the normal by the
        specified bump_distance.  The dir parameter controls which
        direction the pushing occurs, either in the same direction as the
        normal, or when negative, in the opposite direction. The factor
        controls whether what percentage of the bump is used.
        """
        ret = self._wrap_call(self._vtk_obj.BumpPlane, *args)
        return ret

    def push_plane(self, *args):
        """
        V.push_plane(float)
        C++: void PushPlane(double distance)
        Push the plane the distance specified along the normal. Positive
        values are in the direction of the normal; negative values are in
        the opposite direction of the normal. The distance value is
        expressed in world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.PushPlane, *args)
        return ret

    def set_edge_color(self, *args):
        """
        V.set_edge_color(LookupTable)
        C++: void SetEdgeColor(LookupTable *)
        V.set_edge_color(float, float, float)
        C++: void SetEdgeColor(double, double, double)
        V.set_edge_color([float, float, float])
        C++: void SetEdgeColor(double x[3])
        Set color to the edge
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetEdgeColor, *my_args)
        return ret

    def update_placement(self):
        """
        V.update_placement()
        C++: void UpdatePlacement(void)
        Satisfies the superclass API.  This will change the state of the
        widget to match changes that have been made to the underlying
        poly_data_source
        """
        ret = self._vtk_obj.UpdatePlacement()
        return ret
        

    _updateable_traits_ = \
    (('constrain_to_widget_bounds', 'GetConstrainToWidgetBounds'),
    ('draw_plane', 'GetDrawPlane'), ('lock_normal_to_camera',
    'GetLockNormalToCamera'), ('normal_to_x_axis', 'GetNormalToXAxis'),
    ('normal_to_y_axis', 'GetNormalToYAxis'), ('normal_to_z_axis',
    'GetNormalToZAxis'), ('outline_translation', 'GetOutlineTranslation'),
    ('outside_bounds', 'GetOutsideBounds'), ('scale_enabled',
    'GetScaleEnabled'), ('tubing', 'GetTubing'), ('need_to_render',
    'GetNeedToRender'), ('picking_managed', 'GetPickingManaged'),
    ('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('normal', 'GetNormal'), ('bump_distance',
    'GetBumpDistance'), ('interaction_state', 'GetInteractionState'),
    ('origin', 'GetOrigin'), ('representation_state',
    'GetRepresentationState'), ('widget_bounds', 'GetWidgetBounds'),
    ('handle_size', 'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['constrain_to_widget_bounds', 'debug', 'dragable', 'draw_plane',
    'global_warning_display', 'lock_normal_to_camera', 'need_to_render',
    'normal_to_x_axis', 'normal_to_y_axis', 'normal_to_z_axis',
    'outline_translation', 'outside_bounds', 'pickable',
    'picking_managed', 'scale_enabled', 'tubing', 'use_bounds',
    'visibility', 'normal', 'bump_distance', 'estimated_render_time',
    'handle_size', 'interaction_state', 'origin', 'place_factor',
    'render_time_multiplier', 'representation_state', 'widget_bounds'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitPlaneRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitPlaneRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['constrain_to_widget_bounds', 'draw_plane',
            'lock_normal_to_camera', 'need_to_render', 'normal_to_x_axis',
            'normal_to_y_axis', 'normal_to_z_axis', 'outline_translation',
            'outside_bounds', 'picking_managed', 'scale_enabled', 'tubing',
            'use_bounds', 'visibility'], ['normal'], ['bump_distance',
            'estimated_render_time', 'handle_size', 'interaction_state', 'origin',
            'place_factor', 'render_time_multiplier', 'representation_state',
            'widget_bounds']),
            title='Edit ImplicitPlaneRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitPlaneRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


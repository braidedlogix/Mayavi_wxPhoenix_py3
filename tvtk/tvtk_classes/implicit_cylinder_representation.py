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


class ImplicitCylinderRepresentation(WidgetRepresentation):
    """
    ImplicitCylinderRepresentation - defining the representation for a
    ImplicitCylinderWidget
    
    Superclass: WidgetRepresentation
    
    This class is a concrete representation for the
    ImplicitCylinderWidget. It represents an infinite cylinder defined
    by a radius, a center, and an axis. The cylinder is placed within its
    associated bounding box and the intersection of the cylinder with the
    bounding box is shown to visually indicate the orientation and
    position of the representation. This cylinder representation can be
    manipulated by using the ImplicitCylinderWidget to adjust the
    cylinder radius, axis, and/or center point. (Note that the bounding
    box is defined during invocation of the superclass' place_widget()
    method.)
    
    To use this representation, you normally specify a radius, center,
    and axis. Optionally you can specify a minimum and maximum radius,
    and a resolution for the cylinder. Finally, place the widget and its
    representation in the scene using place_widget().
    
    @sa
    ImplicitCylinderWidget ImplicitPlaneWidget
    ImplicitPlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitCylinderRepresentation, obj, update, **traits)
    
    along_x_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the cylinder widget to be aligned with one of the x-y-z
        axes. If one axis is set on, the other two will be set off.
        Remember that when the state changes, a modified_event is invoked.
        This can be used to snap the cylinder to the axes if it is
        originally not aligned.
        """
    )

    def _along_x_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlongXAxis,
                        self.along_x_axis_)

    along_y_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the cylinder widget to be aligned with one of the x-y-z
        axes. If one axis is set on, the other two will be set off.
        Remember that when the state changes, a modified_event is invoked.
        This can be used to snap the cylinder to the axes if it is
        originally not aligned.
        """
    )

    def _along_y_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlongYAxis,
                        self.along_y_axis_)

    along_z_axis = tvtk_base.false_bool_trait(help=\
        """
        Force the cylinder widget to be aligned with one of the x-y-z
        axes. If one axis is set on, the other two will be set off.
        Remember that when the state changes, a modified_event is invoked.
        This can be used to snap the cylinder to the axes if it is
        originally not aligned.
        """
    )

    def _along_z_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlongZAxis,
                        self.along_z_axis_)

    constrain_to_widget_bounds = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off whether the cylinder should be constrained to the
        widget bounds. If on, the center will not be allowed to move
        outside the set widget bounds and the radius will be limited by
        min_radius and max_radius. This is the default behaviour. If off,
        the center can be freely moved and the radius can be set to
        arbitrary values. The widget outline will change accordingly.
        """
    )

    def _constrain_to_widget_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConstrainToWidgetBounds,
                        self.constrain_to_widget_bounds_)

    draw_cylinder = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable the drawing of the cylinder. In some cases the
        cylinder interferes with the object that it is operating on
        (e.g., the cylinder interferes with the cut surface it produces
        resulting in z-buffer artifacts.) By default it is off.
        """
    )

    def _draw_cylinder_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawCylinder,
                        self.draw_cylinder_)

    outline_translation = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the ability to translate the bounding box by moving
        it with the mouse.
        """
    )

    def _outline_translation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutlineTranslation,
                        self.outline_translation_)

    outside_bounds = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the ability to move the widget outside of the bounds
        specified in the place_widget() invocation.
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
        Turn on/off tubing of the wire outline of the cylinder
        intersecton (against the bounding box). The tube thickens the
        line by wrapping with a TubeFilter.
        """
    )

    def _tubing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTubing,
                        self.tubing_)

    axis = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 0.0, 0.0), cols=3, help=\
        """
        Set/Get the axis of rotation for the cylinder. If the axis is not
        specified as a unit vector, it will be normalized.
        """
    )

    def _axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxis,
                        self.axis)

    bump_distance = traits.Trait(0.01, traits.Range(1e-06, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify a translation distance used by the bump_cylinder() method.
        Note that the distance is normalized; it is the fraction of the
        length of the bounding box of the wire outline.
        """
    )

    def _bump_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBumpDistance,
                        self.bump_distance)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Get the center of the cylinder. The center is located along the
        cylinder axis.
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    interaction_state = traits.Trait(0, traits.Range(0, 7, enter_set=True, auto_set=False), help=\
        """
        The interaction state may be set from a widget (e.g.,
        ImplicitCylinderWidget) or other object. This controls how the
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

    max_radius = traits.Trait(1.0, traits.Range(0.25, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Set/Get the minimum and maximum radius of the cylinder. This
        helps prevent the cylinder from "disappearing" during
        interaction.  Note that the minimum and maximum radius is
        specified as a fraction of the diagonal length of the widget
        bounding box.
        """
    )

    def _max_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxRadius,
                        self.max_radius)

    min_radius = traits.Trait(0.01, traits.Range(0.001, 0.25, enter_set=True, auto_set=False), help=\
        """
        Set/Get the minimum and maximum radius of the cylinder. This
        helps prevent the cylinder from "disappearing" during
        interaction.  Note that the minimum and maximum radius is
        specified as a fraction of the diagonal length of the widget
        bounding box.
        """
    )

    def _min_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinRadius,
                        self.min_radius)

    radius = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the radius of the cylinder. Note that if the radius is
        too big the cylinder will be outside of the bounding box.
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

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

    resolution = traits.Trait(128, traits.Range(8, 2048, enter_set=True, auto_set=False), help=\
        """
        Set/Get the resolution of the cylinder. This is the number of
        polygonal facets used to approximate the curved cylindrical
        surface (for rendering purposes). An Cylinder is used under
        the hood to provide an exact surface representation.
        """
    )

    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

    widget_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(-0.25, 0.25, -0.25, 0.25, -0.25, 0.25), cols=3, help=\
        """
        
        """
    )

    def _widget_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWidgetBounds,
                        self.widget_bounds)

    def _get_axis_property(self):
        return wrap_vtk(self._vtk_obj.GetAxisProperty())
    axis_property = traits.Property(_get_axis_property, help=\
        """
        Get the properties on the axis (line and cone).
        """
    )

    def get_cylinder(self, *args):
        """
        V.get_cylinder(Cylinder)
        C++: void GetCylinder(Cylinder *cyl)
        Get the implicit function for the cylinder. The user must provide
        the instance of the class Cylinder. Note that Cylinder is a
        subclass of ImplicitFunction, meaning that it can be used by a
        variety of filters to perform clipping, cutting, and selection of
        data.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetCylinder, *my_args)
        return ret

    def _get_cylinder_property(self):
        return wrap_vtk(self._vtk_obj.GetCylinderProperty())
    cylinder_property = traits.Property(_get_cylinder_property, help=\
        """
        Get the cylinder properties. The properties of the cylinder when
        selected and unselected can be manipulated.
        """
    )

    def _get_edges_property(self):
        return wrap_vtk(self._vtk_obj.GetEdgesProperty())
    edges_property = traits.Property(_get_edges_property, help=\
        """
        Get the property of the intersection edges. (This property also
        applies to the edges when tubed.)
        """
    )

    def _get_outline_property(self):
        return wrap_vtk(self._vtk_obj.GetOutlineProperty())
    outline_property = traits.Property(_get_outline_property, help=\
        """
        Get the property of the outline.
        """
    )

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: void GetPolyData(PolyData *pd)
        Grab the polydata that defines the cylinder. The polydata
        contains polygons that are clipped by the bounding box.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_selected_axis_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedAxisProperty())
    selected_axis_property = traits.Property(_get_selected_axis_property, help=\
        """
        Get the properties on the axis (line and cone).
        """
    )

    def _get_selected_cylinder_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedCylinderProperty())
    selected_cylinder_property = traits.Property(_get_selected_cylinder_property, help=\
        """
        Get the cylinder properties. The properties of the cylinder when
        selected and unselected can be manipulated.
        """
    )

    def _get_selected_outline_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedOutlineProperty())
    selected_outline_property = traits.Property(_get_selected_outline_property, help=\
        """
        Get the property of the outline.
        """
    )

    def bump_cylinder(self, *args):
        """
        V.bump_cylinder(int, float)
        C++: void BumpCylinder(int dir, double factor)
        Translate the cylinder in the direction of the view vector by the
        specified bump_distance. The dir parameter controls which
        direction the pushing occurs, either in the same direction as the
        view vector, or when negative, in the opposite direction.  The
        factor controls what percentage of the bump is used.
        """
        ret = self._wrap_call(self._vtk_obj.BumpCylinder, *args)
        return ret

    def push_cylinder(self, *args):
        """
        V.push_cylinder(float)
        C++: void PushCylinder(double distance)
        Push the cylinder the distance specified along the view vector.
        Positive values are in the direction of the view vector; negative
        values are in the opposite direction. The distance value is
        expressed in world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.PushCylinder, *args)
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
        poly_data_source.
        """
        ret = self._vtk_obj.UpdatePlacement()
        return ret
        

    _updateable_traits_ = \
    (('along_x_axis', 'GetAlongXAxis'), ('along_y_axis', 'GetAlongYAxis'),
    ('along_z_axis', 'GetAlongZAxis'), ('constrain_to_widget_bounds',
    'GetConstrainToWidgetBounds'), ('draw_cylinder', 'GetDrawCylinder'),
    ('outline_translation', 'GetOutlineTranslation'), ('outside_bounds',
    'GetOutsideBounds'), ('scale_enabled', 'GetScaleEnabled'), ('tubing',
    'GetTubing'), ('need_to_render', 'GetNeedToRender'),
    ('picking_managed', 'GetPickingManaged'), ('dragable', 'GetDragable'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('axis',
    'GetAxis'), ('bump_distance', 'GetBumpDistance'), ('center',
    'GetCenter'), ('interaction_state', 'GetInteractionState'),
    ('max_radius', 'GetMaxRadius'), ('min_radius', 'GetMinRadius'),
    ('radius', 'GetRadius'), ('representation_state',
    'GetRepresentationState'), ('resolution', 'GetResolution'),
    ('widget_bounds', 'GetWidgetBounds'), ('handle_size',
    'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['along_x_axis', 'along_y_axis', 'along_z_axis',
    'constrain_to_widget_bounds', 'debug', 'dragable', 'draw_cylinder',
    'global_warning_display', 'need_to_render', 'outline_translation',
    'outside_bounds', 'pickable', 'picking_managed', 'scale_enabled',
    'tubing', 'use_bounds', 'visibility', 'axis', 'bump_distance',
    'center', 'estimated_render_time', 'handle_size', 'interaction_state',
    'max_radius', 'min_radius', 'place_factor', 'radius',
    'render_time_multiplier', 'representation_state', 'resolution',
    'widget_bounds'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitCylinderRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitCylinderRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['along_x_axis', 'along_y_axis', 'along_z_axis',
            'constrain_to_widget_bounds', 'draw_cylinder', 'need_to_render',
            'outline_translation', 'outside_bounds', 'picking_managed',
            'scale_enabled', 'tubing', 'use_bounds', 'visibility'], [], ['axis',
            'bump_distance', 'center', 'estimated_render_time', 'handle_size',
            'interaction_state', 'max_radius', 'min_radius', 'place_factor',
            'radius', 'render_time_multiplier', 'representation_state',
            'resolution', 'widget_bounds']),
            title='Edit ImplicitCylinderRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitCylinderRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


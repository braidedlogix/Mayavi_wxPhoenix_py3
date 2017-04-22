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


class FinitePlaneRepresentation(WidgetRepresentation):
    """
    FinitePlaneRepresentation - represent the FinitePlaneWidget.
    
    Superclass: WidgetRepresentation
    
    This class is a concrete representation for the FinitePlaneWidget.
    It represents a plane with three handles: one on two faces, plus a
    center handle. Through interaction with the widget, the plane
    representation can be arbitrarily positioned and modified in the 3d
    space.
    
    To use this representation, you normally use the place_widget() method
    to position the widget at a specified region in space.
    
    @sa
    FinitePlaneWidget ImplicitPlaneWidget2
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFinitePlaneRepresentation, obj, update, **traits)
    
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

    tubing = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off tubing of the wire outline of the plane. The tube
        thickens the line by wrapping with a TubeFilter.
        """
    )

    def _tubing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTubing,
                        self.tubing_)

    interaction_state = traits.Trait(0, traits.Range(0, 6, enter_set=True, auto_set=False), help=\
        """
        
        """
    )

    def _interaction_state_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteractionState,
                        self.interaction_state)

    normal = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 1.0), cols=3, help=\
        """
        Set/Get the normal to the plane.
        """
    )

    def _normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormal,
                        self.normal)

    origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set/Get the origin of the plane.
        """
    )

    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

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

    v1 = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.5, 0.0), cols=2, help=\
        """
        Set/Get the v1 vector of the plane.
        """
    )

    def _v1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetV1,
                        self.v1)

    v2 = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 0.5), cols=2, help=\
        """
        Set/Get the v2 vector of the plane.
        """
    )

    def _v2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetV2,
                        self.v2)

    def _get_normal_property(self):
        return wrap_vtk(self._vtk_obj.GetNormalProperty())
    normal_property = traits.Property(_get_normal_property, help=\
        """
        Get the properties on the normal (line and cone).
        """
    )

    def _get_plane_property(self):
        return wrap_vtk(self._vtk_obj.GetPlaneProperty())
    plane_property = traits.Property(_get_plane_property, help=\
        """
        Get the plane properties. The properties of the plane when
        selected and normal can be set.
        """
    )

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: void GetPolyData(PolyData *pd)
        Grab the polydata that defines the plane. The polydata contains a
        single polygon.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_selected_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedHandleProperty())
    selected_handle_property = traits.Property(_get_selected_handle_property, help=\
        """
        Get the handle properties (the little balls are the handles). The
        properties of the handles, when selected or normal, can be
        specified.
        """
    )

    def _get_selected_normal_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedNormalProperty())
    selected_normal_property = traits.Property(_get_selected_normal_property, help=\
        """
        Get the properties on the normal (line and cone).
        """
    )

    def _get_selected_plane_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedPlaneProperty())
    selected_plane_property = traits.Property(_get_selected_plane_property, help=\
        """
        Get the plane properties. The properties of the plane when
        selected and normal can be set.
        """
    )

    def _get_v1_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetV1HandleProperty())
    v1_handle_property = traits.Property(_get_v1_handle_property, help=\
        """
        Get the handle properties (the little balls are the handles). The
        properties of the handles, when selected or normal, can be
        specified.
        """
    )

    def _get_v2_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetV2HandleProperty())
    v2_handle_property = traits.Property(_get_v2_handle_property, help=\
        """
        Get the handle properties (the little balls are the handles). The
        properties of the handles, when selected or normal, can be
        specified.
        """
    )

    def handles_off(self):
        """
        V.handles_off()
        C++: virtual void HandlesOff()
        Switches handles (the spheres) on or off by manipulating the
        underlying actor visibility.
        """
        ret = self._vtk_obj.HandlesOff()
        return ret
        

    def handles_on(self):
        """
        V.handles_on()
        C++: virtual void HandlesOn()
        Switches handles (the spheres) on or off by manipulating the
        underlying actor visibility.
        """
        ret = self._vtk_obj.HandlesOn()
        return ret
        

    def move_point1(self, *args):
        """
        V.move_point1([float, ...], [float, ...])
        C++: void MovePoint1(double *p1, double *p2)"""
        ret = self._wrap_call(self._vtk_obj.MovePoint1, *args)
        return ret

    def move_point2(self, *args):
        """
        V.move_point2([float, ...], [float, ...])
        C++: void MovePoint2(double *p1, double *p2)"""
        ret = self._wrap_call(self._vtk_obj.MovePoint2, *args)
        return ret

    def push(self, *args):
        """
        V.push([float, ...], [float, ...])
        C++: void Push(double *p1, double *p2)"""
        ret = self._wrap_call(self._vtk_obj.Push, *args)
        return ret

    def rotate(self, *args):
        """
        V.rotate(int, int, [float, ...], [float, ...], [float, ...])
        C++: void Rotate(int X, int Y, double *p1, double *p2,
            double *vpn)"""
        ret = self._wrap_call(self._vtk_obj.Rotate, *args)
        return ret

    def set_handles(self, *args):
        """
        V.set_handles(bool)
        C++: void SetHandles(bool handles)
        Switches handles (the spheres) on or off by manipulating the
        underlying actor visibility.
        """
        ret = self._wrap_call(self._vtk_obj.SetHandles, *args)
        return ret

    def translate_origin(self, *args):
        """
        V.translate_origin([float, ...], [float, ...])
        C++: void TranslateOrigin(double *p1, double *p2)"""
        ret = self._wrap_call(self._vtk_obj.TranslateOrigin, *args)
        return ret

    _updateable_traits_ = \
    (('draw_plane', 'GetDrawPlane'), ('tubing', 'GetTubing'),
    ('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interaction_state',
    'GetInteractionState'), ('normal', 'GetNormal'), ('origin',
    'GetOrigin'), ('representation_state', 'GetRepresentationState'),
    ('v1', 'GetV1'), ('v2', 'GetV2'), ('handle_size', 'GetHandleSize'),
    ('place_factor', 'GetPlaceFactor'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'draw_plane', 'global_warning_display',
    'need_to_render', 'pickable', 'picking_managed', 'tubing',
    'use_bounds', 'visibility', 'estimated_render_time', 'handle_size',
    'interaction_state', 'normal', 'origin', 'place_factor',
    'render_time_multiplier', 'representation_state', 'v1', 'v2'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FinitePlaneRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FinitePlaneRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['draw_plane', 'need_to_render', 'picking_managed', 'tubing',
            'use_bounds', 'visibility'], [], ['estimated_render_time',
            'handle_size', 'interaction_state', 'normal', 'origin',
            'place_factor', 'render_time_multiplier', 'representation_state',
            'v1', 'v2']),
            title='Edit FinitePlaneRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FinitePlaneRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


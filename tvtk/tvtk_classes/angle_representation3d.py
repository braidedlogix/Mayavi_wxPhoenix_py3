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

from tvtk.tvtk_classes.angle_representation import AngleRepresentation


class AngleRepresentation3D(AngleRepresentation):
    """
    AngleRepresentation3D - represent the AngleWidget
    
    Superclass: AngleRepresentation
    
    The AngleRepresentation3D is a representation for the
    AngleWidget. This representation consists of two rays and three
    HandleRepresentations to place and manipulate the three points
    defining the angle representation. (Note: the three points are
    referred to as Point1, Center, and Point2, at the two end points
    (Point1 and Point2) and Center (around which the angle is measured).
    This particular implementation is a 3d representation, meaning that
    it draws in the overlay plane.
    
    @sa
    AngleWidget HandleRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAngleRepresentation3D, obj, update, **traits)
    
    def get_center_display_position(self, *args):
        """
        V.get_center_display_position([float, float, float])
        C++: virtual void GetCenterDisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetCenterDisplayPosition, *args)
        return ret

    def set_center_display_position(self, *args):
        """
        V.set_center_display_position([float, float, float])
        C++: virtual void SetCenterDisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetCenterDisplayPosition, *args)
        return ret

    def get_center_world_position(self, *args):
        """
        V.get_center_world_position([float, float, float])
        C++: virtual void GetCenterWorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetCenterWorldPosition, *args)
        return ret

    def set_center_world_position(self, *args):
        """
        V.set_center_world_position([float, float, float])
        C++: virtual void SetCenterWorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetCenterWorldPosition, *args)
        return ret

    def get_point1display_position(self, *args):
        """
        V.get_point1display_position([float, float, float])
        C++: virtual void GetPoint1DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint1DisplayPosition, *args)
        return ret

    def set_point1display_position(self, *args):
        """
        V.set_point1display_position([float, float, float])
        C++: virtual void SetPoint1DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint1DisplayPosition, *args)
        return ret

    def get_point1_world_position(self, *args):
        """
        V.get_point1_world_position([float, float, float])
        C++: virtual void GetPoint1WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint1WorldPosition, *args)
        return ret

    def set_point1_world_position(self, *args):
        """
        V.set_point1_world_position([float, float, float])
        C++: virtual void SetPoint1WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint1WorldPosition, *args)
        return ret

    def get_point2display_position(self, *args):
        """
        V.get_point2display_position([float, float, float])
        C++: virtual void GetPoint2DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint2DisplayPosition, *args)
        return ret

    def set_point2display_position(self, *args):
        """
        V.set_point2display_position([float, float, float])
        C++: virtual void SetPoint2DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint2DisplayPosition, *args)
        return ret

    def get_point2_world_position(self, *args):
        """
        V.get_point2_world_position([float, float, float])
        C++: virtual void GetPoint2WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint2WorldPosition, *args)
        return ret

    def set_point2_world_position(self, *args):
        """
        V.set_point2_world_position([float, float, float])
        C++: virtual void SetPoint2WorldPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint2WorldPosition, *args)
        return ret

    text_actor_scale = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Scale text.
        """
    )

    def _text_actor_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextActorScale,
                        self.text_actor_scale)

    def _get_arc(self):
        return wrap_vtk(self._vtk_obj.GetArc())
    arc = traits.Property(_get_arc, help=\
        """
        Set/Get the three leaders used to create this representation. By
        obtaining these leaders the user can set the appropriate
        properties, etc.
        """
    )

    def _get_ray1(self):
        return wrap_vtk(self._vtk_obj.GetRay1())
    ray1 = traits.Property(_get_ray1, help=\
        """
        Set/Get the three leaders used to create this representation. By
        obtaining these leaders the user can set the appropriate
        properties, etc.
        """
    )

    def _get_ray2(self):
        return wrap_vtk(self._vtk_obj.GetRay2())
    ray2 = traits.Property(_get_ray2, help=\
        """
        Set/Get the three leaders used to create this representation. By
        obtaining these leaders the user can set the appropriate
        properties, etc.
        """
    )

    def _get_text_actor(self):
        return wrap_vtk(self._vtk_obj.GetTextActor())
    text_actor = traits.Property(_get_text_actor, help=\
        """
        Set/Get the three leaders used to create this representation. By
        obtaining these leaders the user can set the appropriate
        properties, etc.
        """
    )

    _updateable_traits_ = \
    (('arc_visibility', 'GetArcVisibility'), ('ray1_visibility',
    'GetRay1Visibility'), ('ray2_visibility', 'GetRay2Visibility'),
    ('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('label_format', 'GetLabelFormat'),
    ('tolerance', 'GetTolerance'), ('handle_size', 'GetHandleSize'),
    ('place_factor', 'GetPlaceFactor'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['arc_visibility', 'debug', 'dragable', 'global_warning_display',
    'need_to_render', 'pickable', 'picking_managed', 'ray1_visibility',
    'ray2_visibility', 'use_bounds', 'visibility',
    'estimated_render_time', 'handle_size', 'label_format',
    'place_factor', 'render_time_multiplier', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AngleRepresentation3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AngleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['arc_visibility', 'need_to_render', 'picking_managed',
            'ray1_visibility', 'ray2_visibility', 'use_bounds', 'visibility'], [],
            ['estimated_render_time', 'handle_size', 'label_format',
            'place_factor', 'render_time_multiplier', 'tolerance']),
            title='Edit AngleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AngleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


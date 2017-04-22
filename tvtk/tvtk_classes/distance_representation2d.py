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

from tvtk.tvtk_classes.distance_representation import DistanceRepresentation


class DistanceRepresentation2D(DistanceRepresentation):
    """
    DistanceRepresentation2D - represent the DistanceWidget
    
    Superclass: DistanceRepresentation
    
    The DistanceRepresentation2D is a representation for the
    DistanceWidget. This representation consists of a measuring line
    (axis) and two HandleWidgets to place the end points of the line.
    Note that this particular widget draws its representation in the
    overlay plane, and the handles also operate in the 2d overlay plane.
    (If you desire to use the distance widget for 3d measurements, use
    the DistanceRepresentation3D.)
    
    @sa
    DistanceWidget DistanceRepresentation
    DistanceRepresentation3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDistanceRepresentation2D, obj, update, **traits)
    
    def get_point1display_position(self, *args):
        """
        V.get_point1display_position([float, float, float])
        C++: void GetPoint1DisplayPosition(double pos[3])"""
        ret = self._wrap_call(self._vtk_obj.GetPoint1DisplayPosition, *args)
        return ret

    def set_point1display_position(self, *args):
        """
        V.set_point1display_position([float, float, float])
        C++: void SetPoint1DisplayPosition(double pos[3])"""
        ret = self._wrap_call(self._vtk_obj.SetPoint1DisplayPosition, *args)
        return ret

    point1_world_position = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
    )

    def _point1_world_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1WorldPosition,
                        self.point1_world_position)

    def get_point2display_position(self, *args):
        """
        V.get_point2display_position([float, float, float])
        C++: void GetPoint2DisplayPosition(double pos[3])"""
        ret = self._wrap_call(self._vtk_obj.GetPoint2DisplayPosition, *args)
        return ret

    def set_point2display_position(self, *args):
        """
        V.set_point2display_position([float, float, float])
        C++: void SetPoint2DisplayPosition(double pos[3])"""
        ret = self._wrap_call(self._vtk_obj.SetPoint2DisplayPosition, *args)
        return ret

    point2_world_position = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
    )

    def _point2_world_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2WorldPosition,
                        self.point2_world_position)

    def _get_axis(self):
        return wrap_vtk(self._vtk_obj.GetAxis())
    axis = traits.Property(_get_axis, help=\
        """
        Retrieve the AxisActor2D used to draw the measurement axis.
        With this properties can be set and so on. There is also a
        convenience method to get the axis property.
        """
    )

    def _get_axis_property(self):
        return wrap_vtk(self._vtk_obj.GetAxisProperty())
    axis_property = traits.Property(_get_axis_property, help=\
        """
        Retrieve the AxisActor2D used to draw the measurement axis.
        With this properties can be set and so on. There is also a
        convenience method to get the axis property.
        """
    )

    _updateable_traits_ = \
    (('ruler_mode', 'GetRulerMode'), ('need_to_render',
    'GetNeedToRender'), ('picking_managed', 'GetPickingManaged'),
    ('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('label_format', 'GetLabelFormat'),
    ('number_of_ruler_ticks', 'GetNumberOfRulerTicks'), ('ruler_distance',
    'GetRulerDistance'), ('scale', 'GetScale'), ('tolerance',
    'GetTolerance'), ('handle_size', 'GetHandleSize'), ('place_factor',
    'GetPlaceFactor'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'picking_managed', 'ruler_mode', 'use_bounds',
    'visibility', 'estimated_render_time', 'handle_size', 'label_format',
    'number_of_ruler_ticks', 'place_factor', 'render_time_multiplier',
    'ruler_distance', 'scale', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DistanceRepresentation2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DistanceRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['need_to_render', 'picking_managed', 'ruler_mode',
            'use_bounds', 'visibility'], [], ['estimated_render_time',
            'handle_size', 'label_format', 'number_of_ruler_ticks',
            'place_factor', 'render_time_multiplier', 'ruler_distance', 'scale',
            'tolerance']),
            title='Edit DistanceRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DistanceRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


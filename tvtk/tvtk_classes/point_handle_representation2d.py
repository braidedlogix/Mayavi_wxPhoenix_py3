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


class PointHandleRepresentation2D(HandleRepresentation):
    """
    PointHandleRepresentation2D - represent the position of a point in
    display coordinates
    
    Superclass: HandleRepresentation
    
    This class is used to represent a HandleWidget. It represents a
    position in 2d world coordinates using a x-y cursor (the cursor
    defined by an instance of PolyData and generated by a
    PolyDataAlgorithm).
    
    @sa
    HandleRepresentation HandleWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointHandleRepresentation2D, obj, update, **traits)
    
    def _get_cursor_shape(self):
        return wrap_vtk(self._vtk_obj.GetCursorShape())
    def _set_cursor_shape(self, arg):
        old_val = self._get_cursor_shape()
        self._wrap_call(self._vtk_obj.SetCursorShape,
                        deref_vtk(arg))
        self.trait_property_changed('cursor_shape', old_val, arg)
    cursor_shape = traits.Property(_get_cursor_shape, _set_cursor_shape, help=\
        """
        Specify the cursor shape with an instance of PolyData. Note
        that shape is assumed to be defined in the display coordinate
        system. By default a Cursor2D shape is used.
        """
    )

    display_position = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set/Get the position of the point in display coordinates.  This
        overloads the superclasses set_display_position in order to set the
        focal point of the cursor.
        """
    )

    def _display_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayPosition,
                        self.display_position)

    def _get_point_placer(self):
        return wrap_vtk(self._vtk_obj.GetPointPlacer())
    def _set_point_placer(self, arg):
        old_val = self._get_point_placer()
        self._wrap_call(self._vtk_obj.SetPointPlacer,
                        deref_vtk(arg))
        self.trait_property_changed('point_placer', old_val, arg)
    point_placer = traits.Property(_get_point_placer, _set_point_placer, help=\
        """
        Set/Get the point placer. Point placers can be used to dictate
        constraints on the placement of handles. As an example, see
        BoundedPlanePointPlacer (constrains the placement of handles
        to a set of bounded planes) FocalPlanePointPlacer (constrains
        placement on the focal plane) etc. The default point placer is
        PointPlacer (which does not apply any constraints, so the
        handles are free to move anywhere).
        """
    )

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

    _updateable_traits_ = \
    (('active_representation', 'GetActiveRepresentation'), ('constrained',
    'GetConstrained'), ('need_to_render', 'GetNeedToRender'),
    ('picking_managed', 'GetPickingManaged'), ('dragable', 'GetDragable'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('display_position', 'GetDisplayPosition'), ('interaction_state',
    'GetInteractionState'), ('tolerance', 'GetTolerance'),
    ('world_position', 'GetWorldPosition'), ('handle_size',
    'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['active_representation', 'constrained', 'debug', 'dragable',
    'global_warning_display', 'need_to_render', 'pickable',
    'picking_managed', 'use_bounds', 'visibility', 'display_position',
    'estimated_render_time', 'handle_size', 'interaction_state',
    'place_factor', 'render_time_multiplier', 'tolerance',
    'world_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointHandleRepresentation2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PointHandleRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['active_representation', 'constrained', 'need_to_render',
            'picking_managed', 'use_bounds', 'visibility'], [],
            ['display_position', 'estimated_render_time', 'handle_size',
            'interaction_state', 'place_factor', 'render_time_multiplier',
            'tolerance', 'world_position']),
            title='Edit PointHandleRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointHandleRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class BorderRepresentation(WidgetRepresentation):
    """
    BorderRepresentation - represent a BorderWidget
    
    Superclass: WidgetRepresentation
    
    This class is used to represent and render a vt_border_widget. To use
    this class, you need to specify the two corners of a rectangular
    region.
    
    The class is typically subclassed so that specialized representations
    can be created.  The class defines an API and a default
    implementation that the BorderRepresentation interacts with to
    render itself in the scene.
    
    @warning
    The separation of the widget event handling (e.g., BorderWidget)
    from the representation (vtk_border_representation) enables users and
    developers to create new appearances for the widget. It also
    facilitates parallel processing, where the client application handles
    events, and remote representations of the widget are slaves to the
    client (and do not handle events).
    
    @sa
    BorderWidget TextWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBorderRepresentation, obj, update, **traits)
    
    moving = tvtk_base.false_bool_trait(help=\
        """
        This is a modifier of the interaction state. When set, widget
        interaction allows the border (and stuff inside of it) to be
        translated with mouse motion.
        """
    )

    def _moving_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMoving,
                        self.moving_)

    proportional_resize = tvtk_base.false_bool_trait(help=\
        """
        Indicate whether resizing operations should keep the x-y
        directions proportional to one another. Also, if
        proportional_resize is on, then the rectangle (Position,Position2)
        is a bounding rectangle, and the representation will be placed in
        the rectangle in such a way as to preserve the aspect ratio of
        the representation.
        """
    )

    def _proportional_resize_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProportionalResize,
                        self.proportional_resize_)

    show_border = traits.Trait('on',
    tvtk_base.TraitRevPrefixMap({'on': 1, 'active': 2, 'off': 0}), help=\
        """
        Specify when and if the border should appear. If show_border is
        "on", then the border will always appear. If show_border is "off"
        then the border will never appear.  If show_border is "active"
        then the border will appear when the mouse pointer enters the
        region bounded by the border widget. This method is provided as
        conveniency to set both horizontal and vertical borders.
        BORDER_ON by default. See Also: set_show_horizontal_border(),
        set_show_vertical_border()
        """
    )

    def _show_border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowBorder,
                        self.show_border_)

    maximum_size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(100000, 100000), cols=2, help=\
        """
        
        """
    )

    def _maximum_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumSize,
                        self.maximum_size)

    minimum_size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(1, 1), cols=2, help=\
        """
        
        """
    )

    def _minimum_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumSize,
                        self.minimum_size)

    position = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.05, 0.05), cols=2, help=\
        """
        Specify opposite corners of the box defining the boundary of the
        widget. By default, these coordinates are in the normalized
        viewport coordinate system, with Position the lower left of the
        outline, and Position2 relative to Position. Note that using
        these methods are affected by the proportional_resize flag. That
        is, if the aspect ratio of the representation is to be preserved
        (e.g., proportional_resize is on), then the rectangle
        (Position,Position2) is a bounding rectangle.
        """
    )

    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    position2 = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.1, 0.1), cols=2, help=\
        """
        Specify opposite corners of the box defining the boundary of the
        widget. By default, these coordinates are in the normalized
        viewport coordinate system, with Position the lower left of the
        outline, and Position2 relative to Position. Note that using
        these methods are affected by the proportional_resize flag. That
        is, if the aspect ratio of the representation is to be preserved
        (e.g., proportional_resize is on), then the rectangle
        (Position,Position2) is a bounding rectangle.
        """
    )

    def _position2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition2,
                        self.position2)

    show_horizontal_border = traits.Trait(1, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Specify when and if the horizontal border should appear. See
        Also: set_show_border(), set_show_vertical_border()
        """
    )

    def _show_horizontal_border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowHorizontalBorder,
                        self.show_horizontal_border)

    show_vertical_border = traits.Trait(1, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Specify when and if the vertical border should appear. See Also:
        set_show_border(), set_show_horizontal_border()
        """
    )

    def _show_vertical_border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowVerticalBorder,
                        self.show_vertical_border)

    tolerance = traits.Trait(3, traits.Range(1, 10, enter_set=True, auto_set=False), help=\
        """
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered to be on the widget, or on a
        widget feature (e.g., a corner point or edge).
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def _get_border_property(self):
        return wrap_vtk(self._vtk_obj.GetBorderProperty())
    border_property = traits.Property(_get_border_property, help=\
        """
        Specify the properties of the border.
        """
    )

    def _get_position2_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPosition2Coordinate())
    position2_coordinate = traits.Property(_get_position2_coordinate, help=\
        """
        Specify opposite corners of the box defining the boundary of the
        widget. By default, these coordinates are in the normalized
        viewport coordinate system, with Position the lower left of the
        outline, and Position2 relative to Position. Note that using
        these methods are affected by the proportional_resize flag. That
        is, if the aspect ratio of the representation is to be preserved
        (e.g., proportional_resize is on), then the rectangle
        (Position,Position2) is a bounding rectangle.
        """
    )

    def _get_position_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPositionCoordinate())
    position_coordinate = traits.Property(_get_position_coordinate, help=\
        """
        Specify opposite corners of the box defining the boundary of the
        widget. By default, these coordinates are in the normalized
        viewport coordinate system, with Position the lower left of the
        outline, and Position2 relative to Position. Note that using
        these methods are affected by the proportional_resize flag. That
        is, if the aspect ratio of the representation is to be preserved
        (e.g., proportional_resize is on), then the rectangle
        (Position,Position2) is a bounding rectangle.
        """
    )

    def _get_selection_point(self):
        return self._vtk_obj.GetSelectionPoint()
    selection_point = traits.Property(_get_selection_point, help=\
        """
        After a selection event within the region interior to the border;
        the normalized selection coordinates may be obtained.
        """
    )

    def get_size(self, *args):
        """
        V.get_size([float, float])
        C++: virtual void GetSize(double size[2])
        Subclasses should implement these methods. See the superclasses'
        documentation for more information.
        """
        ret = self._wrap_call(self._vtk_obj.GetSize, *args)
        return ret

    _updateable_traits_ = \
    (('moving', 'GetMoving'), ('proportional_resize',
    'GetProportionalResize'), ('need_to_render', 'GetNeedToRender'),
    ('picking_managed', 'GetPickingManaged'), ('dragable', 'GetDragable'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('show_border',
    'GetShowBorder'), ('maximum_size', 'GetMaximumSize'), ('minimum_size',
    'GetMinimumSize'), ('position', 'GetPosition'), ('position2',
    'GetPosition2'), ('show_horizontal_border',
    'GetShowHorizontalBorder'), ('show_vertical_border',
    'GetShowVerticalBorder'), ('tolerance', 'GetTolerance'),
    ('handle_size', 'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'moving',
    'need_to_render', 'pickable', 'picking_managed',
    'proportional_resize', 'use_bounds', 'visibility', 'show_border',
    'estimated_render_time', 'handle_size', 'maximum_size',
    'minimum_size', 'place_factor', 'position', 'position2',
    'render_time_multiplier', 'show_horizontal_border',
    'show_vertical_border', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BorderRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BorderRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['moving', 'need_to_render', 'picking_managed',
            'proportional_resize', 'use_bounds', 'visibility'], ['show_border'],
            ['estimated_render_time', 'handle_size', 'maximum_size',
            'minimum_size', 'place_factor', 'position', 'position2',
            'render_time_multiplier', 'show_horizontal_border',
            'show_vertical_border', 'tolerance']),
            title='Edit BorderRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BorderRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


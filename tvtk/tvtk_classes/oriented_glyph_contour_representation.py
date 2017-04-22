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

from tvtk.tvtk_classes.contour_representation import ContourRepresentation


class OrientedGlyphContourRepresentation(ContourRepresentation):
    """
    OrientedGlyphContourRepresentation - Default representation for
    the contour widget
    
    Superclass: ContourRepresentation
    
    This class provides the default concrete representation for the
    ContourWidget. It works in conjunction with the
    ContourLineInterpolator and PointPlacer. See ContourWidget
    for details.
    @sa
    ContourRepresentation ContourWidget PointPlacer
    ContourLineInterpolator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOrientedGlyphContourRepresentation, obj, update, **traits)
    
    always_on_top = tvtk_base.false_bool_trait(help=\
        """
        Controls whether the contour widget should always appear on top
        of other actors in the scene. (In effect, this will disable
        open_gl Depth buffer tests while rendering the contour). Default
        is to set it to false.
        """
    )

    def _always_on_top_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlwaysOnTop,
                        self.always_on_top_)

    def _get_active_cursor_shape(self):
        return wrap_vtk(self._vtk_obj.GetActiveCursorShape())
    def _set_active_cursor_shape(self, arg):
        old_val = self._get_active_cursor_shape()
        self._wrap_call(self._vtk_obj.SetActiveCursorShape,
                        deref_vtk(arg))
        self.trait_property_changed('active_cursor_shape', old_val, arg)
    active_cursor_shape = traits.Property(_get_active_cursor_shape, _set_active_cursor_shape, help=\
        """
        Specify the shape of the cursor (handle) when it is active. This
        is the geometry that will be used when the mouse is close to the
        handle or if the user is manipulating the handle.
        """
    )

    def _get_cursor_shape(self):
        return wrap_vtk(self._vtk_obj.GetCursorShape())
    def _set_cursor_shape(self, arg):
        old_val = self._get_cursor_shape()
        self._wrap_call(self._vtk_obj.SetCursorShape,
                        deref_vtk(arg))
        self.trait_property_changed('cursor_shape', old_val, arg)
    cursor_shape = traits.Property(_get_cursor_shape, _set_cursor_shape, help=\
        """
        Specify the cursor shape. Keep in mind that the shape will be
        aligned with the constraining plane by orienting it such that the
        x axis of the geometry lies along the normal of the plane.
        """
    )

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        Subclasses of WidgetRepresentation must implement these
        methods. This is considered the minimum API for a widget
        representation.
        
        set_renderer() - the renderer in which the representations draws
        itself. Typically the renderer is set by the associated widget.
        Use the widget's set_current_renderer() method in most cases;
        otherwise there is a risk of inconsistent behavior as events and
        drawing may be performed in different viewports.
        build_representation() - update the geometry of the widget based
        on its current state.  WARNING: The renderer is NOT reference
        counted by the representation, in order to avoid reference loops.
         Be sure that the representation lifetime does not extend beyond
        the renderer lifetime.
        """
    )

    def _get_active_property(self):
        return wrap_vtk(self._vtk_obj.GetActiveProperty())
    active_property = traits.Property(_get_active_property, help=\
        """
        This is the property used when the user is interacting with the
        handle.
        """
    )

    def _get_lines_property(self):
        return wrap_vtk(self._vtk_obj.GetLinesProperty())
    lines_property = traits.Property(_get_lines_property, help=\
        """
        This is the property used by the lines.
        """
    )

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    property = traits.Property(_get_property, help=\
        """
        This is the property used when the handle is not active (the
        mouse is not near the handle)
        """
    )

    def set_line_color(self, *args):
        """
        V.set_line_color(float, float, float)
        C++: void SetLineColor(double r, double g, double b)
        Convenience method to set the line color. Ideally one should use
        get_lines_property()->_set_color().
        """
        ret = self._wrap_call(self._vtk_obj.SetLineColor, *args)
        return ret

    _updateable_traits_ = \
    (('always_on_top', 'GetAlwaysOnTop'), ('closed_loop',
    'GetClosedLoop'), ('show_selected_nodes', 'GetShowSelectedNodes'),
    ('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('current_operation',
    'GetCurrentOperation'), ('pixel_tolerance', 'GetPixelTolerance'),
    ('world_tolerance', 'GetWorldTolerance'), ('handle_size',
    'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['always_on_top', 'closed_loop', 'debug', 'dragable',
    'global_warning_display', 'need_to_render', 'pickable',
    'picking_managed', 'show_selected_nodes', 'use_bounds', 'visibility',
    'current_operation', 'estimated_render_time', 'handle_size',
    'pixel_tolerance', 'place_factor', 'render_time_multiplier',
    'world_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OrientedGlyphContourRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OrientedGlyphContourRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['always_on_top', 'closed_loop', 'need_to_render',
            'picking_managed', 'show_selected_nodes', 'use_bounds', 'visibility'],
            ['current_operation'], ['estimated_render_time', 'handle_size',
            'pixel_tolerance', 'place_factor', 'render_time_multiplier',
            'world_tolerance']),
            title='Edit OrientedGlyphContourRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OrientedGlyphContourRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


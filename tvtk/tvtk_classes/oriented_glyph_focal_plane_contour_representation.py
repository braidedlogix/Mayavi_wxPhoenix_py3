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

from tvtk.tvtk_classes.focal_plane_contour_representation import FocalPlaneContourRepresentation


class OrientedGlyphFocalPlaneContourRepresentation(FocalPlaneContourRepresentation):
    """
    OrientedGlyphFocalPlaneContourRepresentation - Contours
    constrained to a focal plane.
    
    Superclass: FocalPlaneContourRepresentation
    
    This class is used to represent a contour drawn on the focal plane
    (usually overlayed on top of an image or volume widget). The class
    was written in order to be able to draw contours on a volume widget
    and have the contours overlayed on the focal plane in order to do
    contour segmentation.
    
    @sa
    OrientedGlyphContourRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOrientedGlyphFocalPlaneContourRepresentation, obj, update, **traits)
    
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
        aligned with the  constraining plane by orienting it such that
        the x axis of the geometry lies along the normal of the plane.
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

    def get_contour_plane_direction_cosines(self, *args):
        """
        V.get_contour_plane_direction_cosines((float, float, float))
            -> Matrix4x4
        C++: Matrix4x4 *GetContourPlaneDirectionCosines(
            const double origin[3])
        Direction cosines of the plane on which the contour lies on in
        world co-ordinates. This would be the same matrix that would be
        set in ImageReslice or ImagePlaneWidget if there were a
        plane passing through the contour points. The origin must be the
        origin of the data under the contour.
        """
        ret = self._wrap_call(self._vtk_obj.GetContourPlaneDirectionCosines, *args)
        return wrap_vtk(ret)

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

    _updateable_traits_ = \
    (('closed_loop', 'GetClosedLoop'), ('show_selected_nodes',
    'GetShowSelectedNodes'), ('need_to_render', 'GetNeedToRender'),
    ('picking_managed', 'GetPickingManaged'), ('dragable', 'GetDragable'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('current_operation', 'GetCurrentOperation'), ('pixel_tolerance',
    'GetPixelTolerance'), ('world_tolerance', 'GetWorldTolerance'),
    ('handle_size', 'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['closed_loop', 'debug', 'dragable', 'global_warning_display',
    'need_to_render', 'pickable', 'picking_managed',
    'show_selected_nodes', 'use_bounds', 'visibility',
    'current_operation', 'estimated_render_time', 'handle_size',
    'pixel_tolerance', 'place_factor', 'render_time_multiplier',
    'world_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OrientedGlyphFocalPlaneContourRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OrientedGlyphFocalPlaneContourRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['closed_loop', 'need_to_render', 'picking_managed',
            'show_selected_nodes', 'use_bounds', 'visibility'],
            ['current_operation'], ['estimated_render_time', 'handle_size',
            'pixel_tolerance', 'place_factor', 'render_time_multiplier',
            'world_tolerance']),
            title='Edit OrientedGlyphFocalPlaneContourRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OrientedGlyphFocalPlaneContourRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


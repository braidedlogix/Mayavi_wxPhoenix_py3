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

from tvtk.tvtk_classes.polygonal_handle_representation3d import PolygonalHandleRepresentation3D


class FixedSizeHandleRepresentation3D(PolygonalHandleRepresentation3D):
    """
    FixedSizeHandleRepresentation3D - no description provided.
    
    Superclass: PolygonalHandleRepresentation3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFixedSizeHandleRepresentation3D, obj, update, **traits)
    
    handle_size_in_pixels = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the required handle size in pixels. Defaults to a width
        of 10 pixels.
        """
    )

    def _handle_size_in_pixels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleSizeInPixels,
                        self.handle_size_in_pixels)

    handle_size_tolerance_in_pixels = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Specify the acceptable handle size tolerance. During each render,
        the handle 3d source will be updated to automatically match a
        display size as specified by handle_size_in_pixels. This update will
        be done if the handle size is larger than a tolerance. Default
        value of this tolerance is half a pixel.
        """
    )

    def _handle_size_tolerance_in_pixels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleSizeToleranceInPixels,
                        self.handle_size_tolerance_in_pixels)

    def _get_sphere_source(self):
        return wrap_vtk(self._vtk_obj.GetSphereSource())
    sphere_source = traits.Property(_get_sphere_source, help=\
        """
        Get the object used to render the spherical handle marker
        """
    )

    _updateable_traits_ = \
    (('handle_visibility', 'GetHandleVisibility'), ('label_visibility',
    'GetLabelVisibility'), ('smooth_motion', 'GetSmoothMotion'),
    ('active_representation', 'GetActiveRepresentation'), ('constrained',
    'GetConstrained'), ('need_to_render', 'GetNeedToRender'),
    ('picking_managed', 'GetPickingManaged'), ('dragable', 'GetDragable'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('handle_size_in_pixels', 'GetHandleSizeInPixels'),
    ('handle_size_tolerance_in_pixels', 'GetHandleSizeToleranceInPixels'),
    ('offset', 'GetOffset'), ('world_position', 'GetWorldPosition'),
    ('display_position', 'GetDisplayPosition'), ('label_text',
    'GetLabelText'), ('interaction_state', 'GetInteractionState'),
    ('tolerance', 'GetTolerance'), ('handle_size', 'GetHandleSize'),
    ('place_factor', 'GetPlaceFactor'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['active_representation', 'constrained', 'debug', 'dragable',
    'global_warning_display', 'handle_visibility', 'label_visibility',
    'need_to_render', 'pickable', 'picking_managed', 'smooth_motion',
    'use_bounds', 'visibility', 'display_position',
    'estimated_render_time', 'handle_size', 'handle_size_in_pixels',
    'handle_size_tolerance_in_pixels', 'interaction_state', 'label_text',
    'offset', 'place_factor', 'render_time_multiplier', 'tolerance',
    'world_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FixedSizeHandleRepresentation3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FixedSizeHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['active_representation', 'constrained', 'handle_visibility',
            'label_visibility', 'need_to_render', 'picking_managed',
            'smooth_motion', 'use_bounds', 'visibility'], [], ['display_position',
            'estimated_render_time', 'handle_size', 'handle_size_in_pixels',
            'handle_size_tolerance_in_pixels', 'interaction_state', 'label_text',
            'offset', 'place_factor', 'render_time_multiplier', 'tolerance',
            'world_position']),
            title='Edit FixedSizeHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FixedSizeHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


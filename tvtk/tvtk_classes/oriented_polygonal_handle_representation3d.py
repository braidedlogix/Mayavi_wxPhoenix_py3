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

from tvtk.tvtk_classes.abstract_polygonal_handle_representation3d import AbstractPolygonalHandleRepresentation3D


class OrientedPolygonalHandleRepresentation3D(AbstractPolygonalHandleRepresentation3D):
    """
    OrientedPolygonalHandleRepresentation3D - represent a user defined
    handle geometry in 3d while maintaining a fixed orientation w.r.t the
    camera.
    
    Superclass: AbstractPolygonalHandleRepresentation3D
    
    This class serves as the geometrical representation of a
    HandleWidget. The handle can be represented by an arbitrary
    polygonal data (vtk_poly_data), set via set_handle(vtk_poly_data *). The
    actual position of the handle will be initially assumed to be
    (0,0,0). You can specify an offset from this position if desired.
    This class differs from PolygonalHandleRepresentation3D in that
    the handle will always remain front facing, ie it maintains a fixed
    orientation with respect to the camera. This is done by using
    Followers internally to render the actors.
    @sa
    PolygonalHandleRepresentation3D HandleRepresentation
    HandleWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOrientedPolygonalHandleRepresentation3D, obj, update, **traits)
    
    _updateable_traits_ = \
    (('handle_visibility', 'GetHandleVisibility'), ('label_visibility',
    'GetLabelVisibility'), ('smooth_motion', 'GetSmoothMotion'),
    ('active_representation', 'GetActiveRepresentation'), ('constrained',
    'GetConstrained'), ('need_to_render', 'GetNeedToRender'),
    ('picking_managed', 'GetPickingManaged'), ('dragable', 'GetDragable'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('display_position', 'GetDisplayPosition'), ('label_text',
    'GetLabelText'), ('world_position', 'GetWorldPosition'),
    ('interaction_state', 'GetInteractionState'), ('tolerance',
    'GetTolerance'), ('handle_size', 'GetHandleSize'), ('place_factor',
    'GetPlaceFactor'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['active_representation', 'constrained', 'debug', 'dragable',
    'global_warning_display', 'handle_visibility', 'label_visibility',
    'need_to_render', 'pickable', 'picking_managed', 'smooth_motion',
    'use_bounds', 'visibility', 'display_position',
    'estimated_render_time', 'handle_size', 'interaction_state',
    'label_text', 'place_factor', 'render_time_multiplier', 'tolerance',
    'world_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OrientedPolygonalHandleRepresentation3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OrientedPolygonalHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['active_representation', 'constrained', 'handle_visibility',
            'label_visibility', 'need_to_render', 'picking_managed',
            'smooth_motion', 'use_bounds', 'visibility'], [], ['display_position',
            'estimated_render_time', 'handle_size', 'interaction_state',
            'label_text', 'place_factor', 'render_time_multiplier', 'tolerance',
            'world_position']),
            title='Edit OrientedPolygonalHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OrientedPolygonalHandleRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


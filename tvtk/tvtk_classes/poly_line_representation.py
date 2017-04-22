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

from tvtk.tvtk_classes.curve_representation import CurveRepresentation


class PolyLineRepresentation(CurveRepresentation):
    """
    PolyLineRepresentation - WidgetRepresentation for a poly line.
    
    Superclass: CurveRepresentation
    
    PolyLineRepresentation is a CurveRepresentation for a poly
    line. This 3d widget defines a poly line that can be interactively
    placed in a scene. The poly line has handles, the number of which can
    be changed, plus the widget can be picked on the poly line itself to
    translate or rotate it in the scene. Based on CurveRepresentation
    @sa
    SplineRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyLineRepresentation, obj, update, **traits)
    
    number_of_handles = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        Set the number of handles for this widget.
        """
    )

    def _number_of_handles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfHandles,
                        self.number_of_handles)

    _updateable_traits_ = \
    (('closed', 'GetClosed'), ('project_to_plane', 'GetProjectToPlane'),
    ('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('projection_normal',
    'GetProjectionNormal'), ('number_of_handles', 'GetNumberOfHandles'),
    ('interaction_state', 'GetInteractionState'), ('projection_position',
    'GetProjectionPosition'), ('handle_size', 'GetHandleSize'),
    ('place_factor', 'GetPlaceFactor'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['closed', 'debug', 'dragable', 'global_warning_display',
    'need_to_render', 'pickable', 'picking_managed', 'project_to_plane',
    'use_bounds', 'visibility', 'projection_normal',
    'estimated_render_time', 'handle_size', 'interaction_state',
    'number_of_handles', 'place_factor', 'projection_position',
    'render_time_multiplier'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyLineRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyLineRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['closed', 'need_to_render', 'picking_managed',
            'project_to_plane', 'use_bounds', 'visibility'],
            ['projection_normal'], ['estimated_render_time', 'handle_size',
            'interaction_state', 'number_of_handles', 'place_factor',
            'projection_position', 'render_time_multiplier']),
            title='Edit PolyLineRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyLineRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


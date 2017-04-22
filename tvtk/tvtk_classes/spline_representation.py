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


class SplineRepresentation(CurveRepresentation):
    """
    SplineRepresentation - representation for a spline.
    
    Superclass: CurveRepresentation
    
    SplineRepresentation is a WidgetRepresentation for a spline.
    This 3d widget defines a spline that can be interactively placed in a
    scene. The spline has handles, the number of which can be changed,
    plus it can be picked on the spline itself to translate or rotate it
    in the scene. This is based on SplineWidget.
    @sa
    SplineWidget, SplineWidget2
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSplineRepresentation, obj, update, **traits)
    
    number_of_handles = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        Set the number of handles for this widget.
        """
    )

    def _number_of_handles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfHandles,
                        self.number_of_handles)

    def _get_parametric_spline(self):
        return wrap_vtk(self._vtk_obj.GetParametricSpline())
    def _set_parametric_spline(self, arg):
        old_val = self._get_parametric_spline()
        self._wrap_call(self._vtk_obj.SetParametricSpline,
                        deref_vtk(arg))
        self.trait_property_changed('parametric_spline', old_val, arg)
    parametric_spline = traits.Property(_get_parametric_spline, _set_parametric_spline, help=\
        """
        Set the parametric spline object. Through ParametricSpline's
        API, the user can supply and configure one of two types of
        spline: CardinalSpline, KochanekSpline. The widget controls
        the open or closed configuration of the spline. WARNING: The
        widget does not enforce internal consistency so that all three
        are of the same type.
        """
    )

    resolution = traits.Int(499, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of line segments representing the spline for
        this widget.
        """
    )

    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

    _updateable_traits_ = \
    (('closed', 'GetClosed'), ('project_to_plane', 'GetProjectToPlane'),
    ('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('projection_normal',
    'GetProjectionNormal'), ('number_of_handles', 'GetNumberOfHandles'),
    ('resolution', 'GetResolution'), ('interaction_state',
    'GetInteractionState'), ('projection_position',
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
    'render_time_multiplier', 'resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SplineRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SplineRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['closed', 'need_to_render', 'picking_managed',
            'project_to_plane', 'use_bounds', 'visibility'],
            ['projection_normal'], ['estimated_render_time', 'handle_size',
            'interaction_state', 'number_of_handles', 'place_factor',
            'projection_position', 'render_time_multiplier', 'resolution']),
            title='Edit SplineRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SplineRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


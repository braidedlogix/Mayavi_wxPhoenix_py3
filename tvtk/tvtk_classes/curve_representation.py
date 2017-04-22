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


class CurveRepresentation(WidgetRepresentation):
    """
    CurveRepresentation - WidgetRepresentation base class for a
    widget that represents an curve that connects control points.
    
    Superclass: WidgetRepresentation
    
    Base class for widgets used to define curves from points, such as
    PolyLineRepresentation and SplineRepresentation.  This class
    uses handles, the number of which can be changed, to represent the
    points that define the curve. The handles can be picked can be picked
    on the curve itself to translate or rotate it in the scene.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCurveRepresentation, obj, update, **traits)
    
    closed = tvtk_base.false_bool_trait(help=\
        """
        Control whether the curve is open or closed. A closed forms a
        continuous loop: the first and last points are the same.  A
        minimum of 3 handles are required to form a closed loop.
        """
    )

    def _closed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClosed,
                        self.closed_)

    project_to_plane = tvtk_base.false_bool_trait(help=\
        """
        Force the widget to be projected onto one of the orthogonal
        planes.  Remember that when the interaction_state changes, a
        modified_event is invoked.  This can be used to snap the curve to
        the plane if it is originally not aligned.  The normal in
        set_projection_normal is 0,1,2 for YZ,XZ,XY planes respectively and
        3 for arbitrary oblique planes when the widget is tied to a
        PlaneSource.
        """
    )

    def _project_to_plane_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectToPlane,
                        self.project_to_plane_)

    projection_normal = traits.Trait('x_axes',
    tvtk_base.TraitRevPrefixMap({'x_axes': 0, 'oblique': 3, 'y_axes': 1, 'z_axes': 2}), help=\
        """
        
        """
    )

    def _projection_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectionNormal,
                        self.projection_normal_)

    def get_handle_position(self, *args):
        """
        V.get_handle_position(int, [float, float, float])
        C++: virtual void GetHandlePosition(int handle, double xyz[3])
        V.get_handle_position(int) -> (float, ...)
        C++: virtual double *GetHandlePosition(int handle)
        Set/Get the position of the handles. Call get_number_of_handles to
        determine the valid range of handle indices.
        """
        ret = self._wrap_call(self._vtk_obj.GetHandlePosition, *args)
        return ret

    def set_handle_position(self, *args):
        """
        V.set_handle_position(int, float, float, float)
        C++: virtual void SetHandlePosition(int handle, double x,
            double y, double z)
        V.set_handle_position(int, [float, float, float])
        C++: virtual void SetHandlePosition(int handle, double xyz[3])
        Set/Get the position of the handles. Call get_number_of_handles to
        determine the valid range of handle indices.
        """
        ret = self._wrap_call(self._vtk_obj.SetHandlePosition, *args)
        return ret

    interaction_state = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the interaction state
        """
    )

    def _interaction_state_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteractionState,
                        self.interaction_state)

    number_of_handles = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of handles for this widget.
        """
    )

    def _number_of_handles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfHandles,
                        self.number_of_handles)

    projection_position = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the position of poly line handles and points in terms of a
        plane's position. i.e., if projection_normal is 0, all of the
        x-coordinate values of the points are set to position. Any value
        can be passed (and is ignored) to update the poly line points
        when Projection normal is set to 3 for arbritrary plane
        orientations.
        """
    )

    def _projection_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectionPosition,
                        self.projection_position)

    def _get_handle_positions(self):
        return wrap_vtk(self._vtk_obj.GetHandlePositions())
    handle_positions = traits.Property(_get_handle_positions, help=\
        """
        Set/Get the position of the handles. Call get_number_of_handles to
        determine the valid range of handle indices.
        """
    )

    def _get_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetHandleProperty())
    handle_property = traits.Property(_get_handle_property, help=\
        """
        Set/Get the handle properties (the spheres are the handles). The
        properties of the handles when selected and unselected can be
        manipulated.
        """
    )

    def _get_line_property(self):
        return wrap_vtk(self._vtk_obj.GetLineProperty())
    line_property = traits.Property(_get_line_property, help=\
        """
        Set/Get the line properties. The properties of the line when
        selected and unselected can be manipulated.
        """
    )

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: virtual void GetPolyData(PolyData *pd)
        Grab the polydata (including points) that defines the
        interpolating curve. Points are guaranteed to be up-to-date when
        either the interaction_event or end_interaction events are invoked.
        The user provides the PolyData and the points and polyline are
        added to it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_selected_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedHandleProperty())
    selected_handle_property = traits.Property(_get_selected_handle_property, help=\
        """
        Set/Get the handle properties (the spheres are the handles). The
        properties of the handles when selected and unselected can be
        manipulated.
        """
    )

    def _get_selected_line_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedLineProperty())
    selected_line_property = traits.Property(_get_selected_line_property, help=\
        """
        Set/Get the line properties. The properties of the line when
        selected and unselected can be manipulated.
        """
    )

    def _get_summed_length(self):
        return self._vtk_obj.GetSummedLength()
    summed_length = traits.Property(_get_summed_length, help=\
        """
        Get the approximate vs. the true arc length of the curve.
        Calculated as the summed lengths of the individual straight line
        segments. Use set_resolution to control the accuracy.
        """
    )

    def initialize_handles(self, *args):
        """
        V.initialize_handles(Points)
        C++: virtual void InitializeHandles(Points *points)
        Convenience method to allocate and set the handles from a
        Points instance.  If the first and last points are the same,
        the curve sets Closed to the on interaction_state and disregards
        the last point, otherwise Closed remains unchanged.
        """
        my_args = deref_array(args, [['vtkPoints']])
        ret = self._wrap_call(self._vtk_obj.InitializeHandles, *my_args)
        return ret

    def is_closed(self):
        """
        V.is_closed() -> int
        C++: int IsClosed()
        Convenience method to determine whether the curve is closed in a
        geometric sense.  The widget may be set "closed" but still be
        geometrically open (e.g., a straight line).
        """
        ret = self._vtk_obj.IsClosed()
        return ret
        

    def set_line_color(self, *args):
        """
        V.set_line_color(float, float, float)
        C++: void SetLineColor(double r, double g, double b)
        Convenience method to set the line color. Ideally one should use
        get_line_property()->_set_color().
        """
        ret = self._wrap_call(self._vtk_obj.SetLineColor, *args)
        return ret

    def set_plane_source(self, *args):
        """
        V.set_plane_source(PlaneSource)
        C++: void SetPlaneSource(PlaneSource *plane)
        Set up a reference to a PlaneSource that could be from another
        widget object, e.g. a PolyDataSourceWidget.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPlaneSource, *my_args)
        return ret

    _updateable_traits_ = \
    (('closed', 'GetClosed'), ('project_to_plane', 'GetProjectToPlane'),
    ('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('projection_normal',
    'GetProjectionNormal'), ('interaction_state', 'GetInteractionState'),
    ('number_of_handles', 'GetNumberOfHandles'), ('projection_position',
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
            return super(CurveRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CurveRepresentation properties', scrollable=True, resizable=True,
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
            title='Edit CurveRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CurveRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


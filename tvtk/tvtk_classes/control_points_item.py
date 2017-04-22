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

from tvtk.tvtk_classes.plot import Plot


class ControlPointsItem(Plot):
    """
    ControlPointsItem - Abstract class for control points items.
    
    Superclass: Plot
    
    ControlPointsItem provides control point painting and management
    for subclasses that provide points (typically control points of a
    transfer function)
    @sa
    ScalarsToColorsItem PiecewiseControlPointsItem
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkControlPointsItem, obj, update, **traits)
    
    def get_control_point(self, *args):
        """
        V.get_control_point(int, [float, ...])
        C++: virtual void GetControlPoint(IdType index, double *point)
        Returns the x and y coordinates as well as the midpoint and
        sharpness of the control point corresponding to the index. point
        must be a double array of size 4.
        """
        ret = self._wrap_call(self._vtk_obj.GetControlPoint, *args)
        return ret

    def set_control_point(self, *args):
        """
        V.set_control_point(int, [float, ...])
        C++: virtual void SetControlPoint(IdType index, double *point)
        Sets the x and y coordinates as well as the midpoint and
        sharpness of the control point corresponding to the index.
        """
        ret = self._wrap_call(self._vtk_obj.SetControlPoint, *args)
        return ret

    current_point = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Sets the current point selected.
        """
    )

    def _current_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCurrentPoint,
                        self.current_point)

    end_points_removable = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        If end_points_removable is false, the two end points will not be be
        removed. True by default.
        """
    )

    def _end_points_removable_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndPointsRemovable,
                        self.end_points_removable)

    end_points_x_movable = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        If end_points_movable is false, the two end points will not be
        moved. True by default.
        """
    )

    def _end_points_x_movable_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndPointsXMovable,
                        self.end_points_x_movable)

    end_points_y_movable = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        If end_points_movable is false, the two end points will not be
        moved. True by default.
        """
    )

    def _end_points_y_movable_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndPointsYMovable,
                        self.end_points_y_movable)

    label_format = traits.String('%.3f, %.3f', enter_set=True, auto_set=False, help=\
        """
        Get/Set the label format. Default is "%.4f, %.4f".
        """
    )

    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    screen_point_radius = traits.Float(6.0, enter_set=True, auto_set=False, help=\
        """
        Get/set the radius for screen points. Default is 6.f
        """
    )

    def _screen_point_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScreenPointRadius,
                        self.screen_point_radius)

    show_labels = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        When set to true, labels are shown on the current control point
        and the end points. Default is false.
        """
    )

    def _show_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowLabels,
                        self.show_labels)

    switch_points_mode = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        If draw_points is false, switch_points controls the behavior when a
        control point is dragged past another point. The crossed point
        becomes current (true) or the current point is blocked/stopped
        (false). False by default.
        """
    )

    def _switch_points_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSwitchPointsMode,
                        self.switch_points_mode)

    user_bounds = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, -1.0, 0.0, -1.0), cols=3, help=\
        """
        
        """
    )

    def _user_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUserBounds,
                        self.user_bounds)

    valid_bounds = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, -1.0, 0.0, -1.0), cols=3, help=\
        """
        
        """
    )

    def _valid_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValidBounds,
                        self.valid_bounds)

    def get_control_point_id(self, *args):
        """
        V.get_control_point_id([float, ...]) -> int
        C++: IdType GetControlPointId(double *pos)
        Returns the id of the control point exactly matching pos, -1 if
        not found.
        """
        ret = self._wrap_call(self._vtk_obj.GetControlPointId, *args)
        return ret

    def get_control_points_ids(self, *args):
        """
        V.get_control_points_ids(IdTypeArray, bool)
        C++: void GetControlPointsIds(IdTypeArray *ids,
            bool excludeFirstAndLast=false)
        Utility function that returns an array of all the control points
        IDs Typically: [0, 1, 2, ... n -1] where n is the point count Can
        exclude the first and last point ids from the array.
        """
        my_args = deref_array(args, [('vtkIdTypeArray', 'bool')])
        ret = self._wrap_call(self._vtk_obj.GetControlPointsIds, *my_args)
        return ret

    def _get_end_points_movable(self):
        return self._vtk_obj.GetEndPointsMovable()
    end_points_movable = traits.Property(_get_end_points_movable, help=\
        """
        If end_points_movable is false, the two end points will not be
        moved. True by default.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input table used by the plot.
        """
    )

    def _get_number_of_points(self):
        return self._vtk_obj.GetNumberOfPoints()
    number_of_points = traits.Property(_get_number_of_points, help=\
        """
        Returns the total number of points
        """
    )

    def _get_number_of_selected_points(self):
        return self._vtk_obj.GetNumberOfSelectedPoints()
    number_of_selected_points = traits.Property(_get_number_of_selected_points, help=\
        """
        Return the number of selected points.
        """
    )

    def _get_selected_point_brush(self):
        return wrap_vtk(self._vtk_obj.GetSelectedPointBrush())
    selected_point_brush = traits.Property(_get_selected_point_brush, help=\
        """
        Depending on the control points item, the brush might not be
        taken into account.
        """
    )

    def _get_selected_point_pen(self):
        return wrap_vtk(self._vtk_obj.GetSelectedPointPen())
    selected_point_pen = traits.Property(_get_selected_point_pen, help=\
        """
        Gets the selected point pen and brush.
        """
    )

    def _get_stroke_mode(self):
        return self._vtk_obj.GetStrokeMode()
    stroke_mode = traits.Property(_get_stroke_mode, help=\
        """
        Controls whether or not control points are drawn (true) or
        clicked and moved (false). False by default.
        """
    )

    def add_point(self, *args):
        """
        V.add_point([float, ...]) -> int
        C++: virtual IdType AddPoint(double *newPos)
        Add a point to the function. Returns the index of the point (0
        based), or -1 on error. Subclasses should reimplement this
        function to do the actual work.
        """
        ret = self._wrap_call(self._vtk_obj.AddPoint, *args)
        return ret

    def deselect_all_points(self):
        """
        V.deselect_all_points()
        C++: void DeselectAllPoints()
        Unselect all the previously selected points
        """
        ret = self._vtk_obj.DeselectAllPoints()
        return ret
        

    def deselect_point(self, *args):
        """
        V.deselect_point(int)
        C++: void DeselectPoint(IdType pointId)
        V.deselect_point([float, ...])
        C++: void DeselectPoint(double *currentPoint)
        Unselect a point by its ID
        """
        ret = self._wrap_call(self._vtk_obj.DeselectPoint, *args)
        return ret

    def find_point(self, *args):
        """
        V.find_point([float, ...]) -> int
        C++: IdType FindPoint(double *pos)
        Returns the IdType of the point given its coordinates and a
        tolerance based on the screen point size.
        """
        ret = self._wrap_call(self._vtk_obj.FindPoint, *args)
        return ret

    def is_over_point(self, *args):
        """
        V.is_over_point([float, ...], int) -> bool
        C++: bool IsOverPoint(double *pos, IdType pointId)
        Returns true if pos is above the point_id point, false otherwise.
        It uses the size of the drawn point. To search what point is
        under the pos, use the more efficient \sa find_point() instead.
        """
        ret = self._wrap_call(self._vtk_obj.IsOverPoint, *args)
        return ret

    def move_points(self, *args):
        """
        V.move_points(Vector2f, IdTypeArray)
        C++: void MovePoints(const Vector2f &translation,
            IdTypeArray *pointIds)
        V.move_points(Vector2f, bool)
        C++: void MovePoints(const Vector2f &translation,
            bool dontMoveFirstAndLast=false)
        Move the points referred by point_ids by a given translation. The
        new positions won't be outside the bounds. move_points is
        typically called with get_control_points_ids() or get_selection().
        Warning: if you pass this->_get_selection(), the array is deleted
        after each individual point move. Increase the reference count of
        the array. See also move_all_points()
        """
        my_args = deref_array(args, [('vtkVector2f', 'vtkIdTypeArray'), ('vtkVector2f', 'bool')])
        ret = self._wrap_call(self._vtk_obj.MovePoints, *my_args)
        return ret

    def remove_current_point(self):
        """
        V.remove_current_point()
        C++: void RemoveCurrentPoint()
        Remove the current point.
        """
        ret = self._vtk_obj.RemoveCurrentPoint()
        return ret
        

    def remove_point(self, *args):
        """
        V.remove_point([float, ...]) -> int
        C++: virtual IdType RemovePoint(double *pos)
        V.remove_point(int) -> int
        C++: IdType RemovePoint(IdType pointId)
        Remove a point of the function. Returns the index of the point (0
        based), or -1 on error. Subclasses should reimplement this
        function to do the actual work.
        """
        ret = self._wrap_call(self._vtk_obj.RemovePoint, *args)
        return ret

    def reset_bounds(self):
        """
        V.reset_bounds()
        C++: void ResetBounds()
        Recompute the bounds next time they are requested. You shouldn't
        have to call it but it is provided for rare cases.
        """
        ret = self._vtk_obj.ResetBounds()
        return ret
        

    def select_all_points(self):
        """
        V.select_all_points()
        C++: void SelectAllPoints()
        Select all the points
        """
        ret = self._vtk_obj.SelectAllPoints()
        return ret
        

    def select_point(self, *args):
        """
        V.select_point(int)
        C++: void SelectPoint(IdType pointId)
        V.select_point([float, ...])
        C++: void SelectPoint(double *currentPoint)
        Select a point by its ID
        """
        ret = self._wrap_call(self._vtk_obj.SelectPoint, *args)
        return ret

    def spread_points(self, *args):
        """
        V.spread_points(float, IdTypeArray)
        C++: void SpreadPoints(float factor, IdTypeArray *pointIds)
        V.spread_points(float, bool)
        C++: void SpreadPoints(float factor,
            bool dontSpreadFirstAndLast=false)
        Spread the points referred by point_ids If factor > 0, points are
        moved away from each other. If factor < 0, points are moved
        closer to each other spread_points is typically called with
        get_control_points_ids() or get_selection(). Warning: if you pass
        this->_get_selection(), the array is deleted after each individual
        point move. Increase the reference count of the array.
        """
        my_args = deref_array(args, [('float', 'vtkIdTypeArray'), ('float', 'bool')])
        ret = self._wrap_call(self._vtk_obj.SpreadPoints, *my_args)
        return ret

    def toggle_select_point(self, *args):
        """
        V.toggle_select_point(int)
        C++: void ToggleSelectPoint(IdType pointId)
        V.toggle_select_point([float, ...])
        C++: void ToggleSelectPoint(double *currentPoint)
        Toggle the selection of a point by its ID. If the point was
        selected then unselect it, otherwise select it.
        """
        ret = self._wrap_call(self._vtk_obj.ToggleSelectPoint, *args)
        return ret

    _updateable_traits_ = \
    (('legend_visibility', 'GetLegendVisibility'), ('selectable',
    'GetSelectable'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('current_point', 'GetCurrentPoint'),
    ('end_points_removable', 'GetEndPointsRemovable'),
    ('end_points_x_movable', 'GetEndPointsXMovable'),
    ('end_points_y_movable', 'GetEndPointsYMovable'), ('label_format',
    'GetLabelFormat'), ('screen_point_radius', 'GetScreenPointRadius'),
    ('show_labels', 'GetShowLabels'), ('switch_points_mode',
    'GetSwitchPointsMode'), ('user_bounds', 'GetUserBounds'),
    ('valid_bounds', 'GetValidBounds'), ('label', 'GetLabel'),
    ('tooltip_label_format', 'GetTooltipLabelFormat'),
    ('tooltip_notation', 'GetTooltipNotation'), ('tooltip_precision',
    'GetTooltipPrecision'), ('use_index_for_x_series',
    'GetUseIndexForXSeries'), ('width', 'GetWidth'), ('opacity',
    'GetOpacity'), ('interactive', 'GetInteractive'), ('visible',
    'GetVisible'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'legend_visibility',
    'selectable', 'current_point', 'end_points_removable',
    'end_points_x_movable', 'end_points_y_movable', 'interactive',
    'label', 'label_format', 'opacity', 'screen_point_radius',
    'show_labels', 'switch_points_mode', 'tooltip_label_format',
    'tooltip_notation', 'tooltip_precision', 'use_index_for_x_series',
    'user_bounds', 'valid_bounds', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ControlPointsItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ControlPointsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['legend_visibility', 'selectable'], [], ['current_point',
            'end_points_removable', 'end_points_x_movable',
            'end_points_y_movable', 'interactive', 'label', 'label_format',
            'opacity', 'screen_point_radius', 'show_labels', 'switch_points_mode',
            'tooltip_label_format', 'tooltip_notation', 'tooltip_precision',
            'use_index_for_x_series', 'user_bounds', 'valid_bounds', 'visible',
            'width']),
            title='Edit ControlPointsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ControlPointsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


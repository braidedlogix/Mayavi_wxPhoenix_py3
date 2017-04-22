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

from tvtk.tvtk_classes.chart import Chart


class ChartXY(Chart):
    """
    ChartXY - Factory class for drawing XY charts
    
    Superclass: Chart
    
    This class implements an XY chart.
    
    @sa
    BarChartActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkChartXY, obj, update, **traits)
    
    adjust_lower_bound_for_log_plot = tvtk_base.false_bool_trait(help=\
        """
        Adjust the minimum of a logarithmic axis to be greater than 0,
        regardless of the minimum data value. False by default.
        """
    )

    def _adjust_lower_bound_for_log_plot_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAdjustLowerBoundForLogPlot,
                        self.adjust_lower_bound_for_log_plot_)

    auto_axes = tvtk_base.true_bool_trait(help=\
        """
        If true then the axes will be turned on and off depending upon
        whether any plots are in that corner. Defaults to true.
        """
    )

    def _auto_axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoAxes,
                        self.auto_axes_)

    draw_axes_at_origin = tvtk_base.false_bool_trait(help=\
        """
        If true then the axes will be drawn at the origin (scientific
        style).
        """
    )

    def _draw_axes_at_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawAxesAtOrigin,
                        self.draw_axes_at_origin_)

    force_axes_to_bounds = tvtk_base.false_bool_trait(help=\
        """
        Force the axes to have their Minimum and Maximum properties
        inside the plot boundaries. It constrains pan and zoom
        interaction. False by default.
        """
    )

    def _force_axes_to_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForceAxesToBounds,
                        self.force_axes_to_bounds_)

    zoom_with_mouse_wheel = tvtk_base.true_bool_trait(help=\
        """
        Set the behavior of the mouse wheel.  If true, the mouse wheel
        zooms in/out on the chart.  Otherwise, unless mouse_wheel_event is
        overridden by a subclass the mouse wheel does nothing. The
        default value is true.
        """
    )

    def _zoom_with_mouse_wheel_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZoomWithMouseWheel,
                        self.zoom_with_mouse_wheel_)

    bar_width_fraction = traits.Float(0.800000011920929, enter_set=True, auto_set=False, help=\
        """
        Set the width fraction for any bar charts drawn in this chart. It
        is assumed that all bar plots will use the same array for the X
        axis, and that this array is regularly spaced. The delta between
        the first two x values is used to calculated the width of the
        bars, and subdivided between each bar. The default value is 0.8,
        1.0 would lead to bars that touch.
        """
    )

    def _bar_width_fraction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBarWidthFraction,
                        self.bar_width_fraction)

    hidden_axis_border = traits.Int(20, enter_set=True, auto_set=False, help=\
        """
        Border size of the axes that are hidden (vtk_axis::_get_visible())
        """
    )

    def _hidden_axis_border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHiddenAxisBorder,
                        self.hidden_axis_border)

    def get_plot_corner(self, *args):
        """
        V.get_plot_corner(Plot) -> int
        C++: int GetPlotCorner(Plot *plot)
        Figure out which quadrant the plot is in.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPlotCorner, *my_args)
        return ret

    def set_plot_corner(self, *args):
        """
        V.set_plot_corner(Plot, int)
        C++: void SetPlotCorner(Plot *plot, int corner)
        Figure out which quadrant the plot is in.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPlotCorner, *my_args)
        return ret

    selection_method = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the selection method, which controls how selections are
        handled by the chart. The default is SELECTION_ROWS which selects
        all points in all plots in a chart that have values in the rows
        selected. SELECTION_PLOTS allows for finer-grained selections
        specific to each plot, and so to each XY column pair.
        """
    )

    def _selection_method_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionMethod,
                        self.selection_method)

    show_legend = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Set whether the chart should draw a legend.
        """
    )

    def _show_legend_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowLegend,
                        self.show_legend)

    def _get_tooltip(self):
        return wrap_vtk(self._vtk_obj.GetTooltip())
    def _set_tooltip(self, arg):
        old_val = self._get_tooltip()
        self._wrap_call(self._vtk_obj.SetTooltip,
                        deref_vtk(arg))
        self.trait_property_changed('tooltip', old_val, arg)
    tooltip = traits.Property(_get_tooltip, _set_tooltip, help=\
        """
        Get the TooltipItem object that will be displayed by the
        chart.
        """
    )

    def get_plot_index(self, *args):
        """
        V.get_plot_index(Plot) -> int
        C++: virtual IdType GetPlotIndex(Plot *)
        Get the index of the specified plot, returns -1 if the plot does
        not belong to the chart.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPlotIndex, *my_args)
        return ret

    def lower_plot(self, *args):
        """
        V.lower_plot(Plot) -> int
        C++: IdType LowerPlot(Plot *plot)
        Lowers the plot to the bottom of the plot's stack.
        \return The new index of the plot
        \sa stack_plot_under(), raise_plot(), stack_plot_above()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.LowerPlot, *my_args)
        return ret

    def raise_plot(self, *args):
        """
        V.raise_plot(Plot) -> int
        C++: IdType RaisePlot(Plot *plot)
        Raises the plot to the top of the plot's stack.
        \return The new index of the plot
        \sa stack_plot_above(), lower_plot(), stack_plot_under()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RaisePlot, *my_args)
        return ret

    def set_tooltip_info(self, *args):
        """
        V.set_tooltip_info(ContextMouseEvent, Vector2d, int, Plot,
            int)
        C++: virtual void SetTooltipInfo(const ContextMouseEvent &,
            const Vector2d &, IdType, Plot *,
            IdType segmentIndex=-1)
        Set the information passed to the tooltip.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTooltipInfo, *my_args)
        return ret

    def stack_plot_above(self, *args):
        """
        V.stack_plot_above(Plot, Plot) -> int
        C++: virtual IdType StackPlotAbove(Plot *plot,
            Plot *under)
        Raises the plot above the under plot. If under is null, the plot
        is raised to the top of the plot's stack.
        \return The new index of the plot
        \sa raise_plot(), lower_plot(), stack_plot_under()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.StackPlotAbove, *my_args)
        return ret

    def stack_plot_under(self, *args):
        """
        V.stack_plot_under(Plot, Plot) -> int
        C++: virtual IdType StackPlotUnder(Plot *plot,
            Plot *above)
        Lowers the plot under the above plot. If above is null, the plot
        is lowered to the bottom of the plot's stack
        \return The new index of the plot
        \sa stack_plot_under(), raise_plot(), stack_plot_above()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.StackPlotUnder, *my_args)
        return ret

    _updateable_traits_ = \
    (('adjust_lower_bound_for_log_plot', 'GetAdjustLowerBoundForLogPlot'),
    ('auto_axes', 'GetAutoAxes'), ('draw_axes_at_origin',
    'GetDrawAxesAtOrigin'), ('force_axes_to_bounds',
    'GetForceAxesToBounds'), ('zoom_with_mouse_wheel',
    'GetZoomWithMouseWheel'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('bar_width_fraction', 'GetBarWidthFraction'), ('hidden_axis_border',
    'GetHiddenAxisBorder'), ('selection_method', 'GetSelectionMethod'),
    ('show_legend', 'GetShowLegend'), ('auto_size', 'GetAutoSize'),
    ('geometry', 'GetGeometry'), ('layout_strategy', 'GetLayoutStrategy'),
    ('point1', 'GetPoint1'), ('point2', 'GetPoint2'), ('render_empty',
    'GetRenderEmpty'), ('selection_mode', 'GetSelectionMode'), ('title',
    'GetTitle'), ('opacity', 'GetOpacity'), ('interactive',
    'GetInteractive'), ('visible', 'GetVisible'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['adjust_lower_bound_for_log_plot', 'auto_axes', 'debug',
    'draw_axes_at_origin', 'force_axes_to_bounds',
    'global_warning_display', 'zoom_with_mouse_wheel', 'auto_size',
    'bar_width_fraction', 'geometry', 'hidden_axis_border', 'interactive',
    'layout_strategy', 'opacity', 'point1', 'point2', 'render_empty',
    'selection_method', 'selection_mode', 'show_legend', 'title',
    'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ChartXY, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ChartXY properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['adjust_lower_bound_for_log_plot', 'auto_axes',
            'draw_axes_at_origin', 'force_axes_to_bounds',
            'zoom_with_mouse_wheel'], [], ['auto_size', 'bar_width_fraction',
            'geometry', 'hidden_axis_border', 'interactive', 'layout_strategy',
            'opacity', 'point1', 'point2', 'render_empty', 'selection_method',
            'selection_mode', 'show_legend', 'title', 'visible']),
            title='Edit ChartXY properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ChartXY properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


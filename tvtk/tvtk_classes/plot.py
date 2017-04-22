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

from tvtk.tvtk_classes.context_item import ContextItem


class Plot(ContextItem):
    """
    Plot - Abstract class for 2d plots.
    
    Superclass: ContextItem
    
    The base class for all plot types used in Chart derived charts.
    
    @sa
    PlotPoints PlotLine PlotBar Chart ChartXY
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlot, obj, update, **traits)
    
    legend_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set whether the plot renders an entry in the legend. Default is
        true. Plot::PaintLegend will get called to render the legend
        marker on when this is true.
        """
    )

    def _legend_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLegendVisibility,
                        self.legend_visibility_)

    selectable = tvtk_base.true_bool_trait(help=\
        """
        Set whether the plot can be selected. True by default. If not,
        then set_selection(), select_points() or select_points_in_polygon()
        won't have any effect.
        \sa set_selection(), select_points(), select_points_in_polygon()
        """
    )

    def _selectable_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectable,
                        self.selectable_)

    def _get_brush(self):
        return wrap_vtk(self._vtk_obj.GetBrush())
    def _set_brush(self, arg):
        old_val = self._get_brush()
        self._wrap_call(self._vtk_obj.SetBrush,
                        deref_vtk(arg))
        self.trait_property_changed('brush', old_val, arg)
    brush = traits.Property(_get_brush, _set_brush, help=\
        """
        Set/get the Brush object that controls how this plot fills
        shapes.
        """
    )

    def get_color(self, *args):
        """
        V.get_color([float, float, float])
        C++: virtual void GetColor(double rgb[3])
        V.get_color([int, int, int])
        C++: void GetColor(unsigned char rgb[3])
        Set the plot color
        """
        ret = self._wrap_call(self._vtk_obj.GetColor, *args)
        return ret

    def set_color(self, *args):
        """
        V.set_color(int, int, int, int)
        C++: virtual void SetColor(unsigned char r, unsigned char g,
            unsigned char b, unsigned char a)
        V.set_color(float, float, float)
        C++: virtual void SetColor(double r, double g, double b)
        Set the plot color
        """
        ret = self._wrap_call(self._vtk_obj.SetColor, *args)
        return ret

    def _get_indexed_labels(self):
        return wrap_vtk(self._vtk_obj.GetIndexedLabels())
    def _set_indexed_labels(self, arg):
        old_val = self._get_indexed_labels()
        my_arg = deref_array([arg], [['vtkStringArray']])
        self._wrap_call(self._vtk_obj.SetIndexedLabels,
                        my_arg[0])
        self.trait_property_changed('indexed_labels', old_val, arg)
    indexed_labels = traits.Property(_get_indexed_labels, _set_indexed_labels, help=\
        """
        Get the indexed labels array.
        """
    )

    label = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Set the label of this plot.
        """
    )

    def _label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabel,
                        self.label)

    def _get_labels(self):
        return wrap_vtk(self._vtk_obj.GetLabels())
    def _set_labels(self, arg):
        old_val = self._get_labels()
        my_arg = deref_array([arg], [['vtkStringArray']])
        self._wrap_call(self._vtk_obj.SetLabels,
                        my_arg[0])
        self.trait_property_changed('labels', old_val, arg)
    labels = traits.Property(_get_labels, _set_labels, help=\
        """
        Get the plot labels. If this array has a length greater than 1
        the index refers to the stacked objects in the plot. See
        PlotBar for example.
        """
    )

    def _get_pen(self):
        return wrap_vtk(self._vtk_obj.GetPen())
    def _set_pen(self, arg):
        old_val = self._get_pen()
        self._wrap_call(self._vtk_obj.SetPen,
                        deref_vtk(arg))
        self.trait_property_changed('pen', old_val, arg)
    pen = traits.Property(_get_pen, _set_pen, help=\
        """
        Set/get the Pen object that controls how this plot draws
        (out)lines.
        """
    )

    def get_property(self, *args):
        """
        V.get_property(string) -> Variant
        C++: virtual Variant GetProperty(const StdString &property)
        A General setter/getter that should be overridden. It can
        silently drop options, case is important
        """
        ret = self._wrap_call(self._vtk_obj.GetProperty, *args)
        return wrap_vtk(ret)

    def set_property(self, *args):
        """
        V.set_property(string, Variant)
        C++: virtual void SetProperty(const StdString &property,
            const Variant &var)
        A General setter/getter that should be overridden. It can
        silently drop options, case is important
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetProperty, *my_args)
        return ret

    def _get_selection(self):
        return wrap_vtk(self._vtk_obj.GetSelection())
    def _set_selection(self, arg):
        old_val = self._get_selection()
        my_arg = deref_array([arg], [['vtkIdTypeArray']])
        self._wrap_call(self._vtk_obj.SetSelection,
                        my_arg[0])
        self.trait_property_changed('selection', old_val, arg)
    selection = traits.Property(_get_selection, _set_selection, help=\
        """
        Sets the list of points that must be selected. If Selectable is
        false, then this method does nothing.
        \sa set_selectable()
        """
    )

    def _get_selection_brush(self):
        return wrap_vtk(self._vtk_obj.GetSelectionBrush())
    def _set_selection_brush(self, arg):
        old_val = self._get_selection_brush()
        self._wrap_call(self._vtk_obj.SetSelectionBrush,
                        deref_vtk(arg))
        self.trait_property_changed('selection_brush', old_val, arg)
    selection_brush = traits.Property(_get_selection_brush, _set_selection_brush, help=\
        """
        Set/get the Brush object that controls how this plot fills
        selected shapes.
        """
    )

    def _get_selection_pen(self):
        return wrap_vtk(self._vtk_obj.GetSelectionPen())
    def _set_selection_pen(self, arg):
        old_val = self._get_selection_pen()
        self._wrap_call(self._vtk_obj.SetSelectionPen,
                        deref_vtk(arg))
        self.trait_property_changed('selection_pen', old_val, arg)
    selection_pen = traits.Property(_get_selection_pen, _set_selection_pen, help=\
        """
        Set/get the Brush object that controls how this plot fills
        selected shapes.
        """
    )

    tooltip_label_format = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Sets/gets a printf-style string to build custom tooltip labels
        from. An empty string generates the default tooltip labels. The
        following case-sensitive format tags (without quotes) are
        recognized: '%x' The X value of the plot element '%y' The Y value
        of the plot element '%i' The indexed_labels entry for the plot
        element '%l' The value of the plot's get_label() function '%s'
        (vtk_plot_bar only) The Labels entry for the bar segment Any other
        characters or unrecognized format tags are printed in the tooltip
        label verbatim.
        """
    )

    def _tooltip_label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTooltipLabelFormat,
                        self.tooltip_label_format)

    tooltip_notation = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Sets/gets the tooltip notation style.
        """
    )

    def _tooltip_notation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTooltipNotation,
                        self.tooltip_notation)

    tooltip_precision = traits.Int(6, enter_set=True, auto_set=False, help=\
        """
        Sets/gets the tooltip precision.
        """
    )

    def _tooltip_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTooltipPrecision,
                        self.tooltip_precision)

    use_index_for_x_series = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Use the Y array index for the X value. If true any X column
        setting will be ignored, and the X values will simply be the
        index of the Y column.
        """
    )

    def _use_index_for_x_series_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseIndexForXSeries,
                        self.use_index_for_x_series)

    width = traits.Float(2.0, enter_set=True, auto_set=False, help=\
        """
        Set the width of the line.
        """
    )

    def _width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWidth,
                        self.width)

    def _get_x_axis(self):
        return wrap_vtk(self._vtk_obj.GetXAxis())
    def _set_x_axis(self, arg):
        old_val = self._get_x_axis()
        self._wrap_call(self._vtk_obj.SetXAxis,
                        deref_vtk(arg))
        self.trait_property_changed('x_axis', old_val, arg)
    x_axis = traits.Property(_get_x_axis, _set_x_axis, help=\
        """
        Get/set the X axis associated with this plot.
        """
    )

    def _get_y_axis(self):
        return wrap_vtk(self._vtk_obj.GetYAxis())
    def _set_y_axis(self, arg):
        old_val = self._get_y_axis()
        self._wrap_call(self._vtk_obj.SetYAxis,
                        deref_vtk(arg))
        self.trait_property_changed('y_axis', old_val, arg)
    y_axis = traits.Property(_get_y_axis, _set_y_axis, help=\
        """
        Get/set the Y axis associated with this plot.
        """
    )

    def get_bounds(self, *args):
        """
        V.get_bounds([float, float, float, float])
        C++: virtual void GetBounds(double bounds[4])
        Get the bounds for this plot as (Xmin, Xmax, Ymin, Ymax).
        
        * See get_unscaled_input_bounds for more information.
        """
        ret = self._wrap_call(self._vtk_obj.GetBounds, *args)
        return ret

    def _get_data(self):
        return wrap_vtk(self._vtk_obj.GetData())
    data = traits.Property(_get_data, help=\
        """
        Get the data object that the plot will draw.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input table used by the plot.
        """
    )

    def _get_number_of_labels(self):
        return self._vtk_obj.GetNumberOfLabels()
    number_of_labels = traits.Property(_get_number_of_labels, help=\
        """
        Get the number of labels associated with this plot.
        """
    )

    def get_tooltip_label(self, *args):
        """
        V.get_tooltip_label(Vector2d, int, int) -> string
        C++: virtual StdString GetTooltipLabel(
            const Vector2d &plotPos, IdType seriesIndex,
            IdType segmentIndex)
        Generate and return the tooltip label string for this plot The
        segment_index parameter is ignored, except for PlotBar
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetTooltipLabel, *my_args)
        return ret

    def get_unscaled_input_bounds(self, *args):
        """
        V.get_unscaled_input_bounds([float, float, float, float])
        C++: virtual void GetUnscaledInputBounds(double bounds[4])
        Provide un-log-scaled bounds for the plot inputs.
        
        * This function is analogous to get_bounds() with 2 exceptions:
        * 1. It will never return log-scaled bounds even when the
        * x- and/or y-axes are log-scaled.
        * 2. It will always return the bounds along the *input* axes
        * rather than the output chart coordinates. Thus get_x_axis()
        * returns the axis associated with the first 2 bounds entries
        * and get_y_axis() returns the axis associated with the next 2
        * bounds entries.
        
        * For example, PlotBar's get_bounds() method
        * will swap axis bounds when its orientation is vertical while
        * its get_unscaled_input_bounds() will not swap axis bounds.
        
        * This method is provided so user interfaces can determine
        * whether or not to allow log-scaling of a particular Axis.
        
        * Subclasses of Plot are responsible for implementing this
        * function to transform input plot data.
        
        * The returned bounds are stored as (Xmin, Xmax, Ymin, Ymax).
        """
        ret = self._wrap_call(self._vtk_obj.GetUnscaledInputBounds, *args)
        return ret

    def paint_legend(self, *args):
        """
        V.paint_legend(Context2D, Rectf, int) -> bool
        C++: virtual bool PaintLegend(Context2D *painter,
            const Rectf &rect, int legendIndex)
        Paint legend event for the plot, called whenever the legend needs
        the plot items symbol/mark/line drawn. A rect is supplied with
        the lower left corner of the rect (elements 0 and 1) and with
        width x height (elements 2 and 3). The plot can choose how to
        fill the space supplied. The index is used by Plots that return
        more than one label.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PaintLegend, *my_args)
        return ret

    def select_points(self, *args):
        """
        V.select_points(Vector2f, Vector2f) -> bool
        C++: virtual bool SelectPoints(const Vector2f &min,
            const Vector2f &max)
        Select all points in the specified rectangle.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SelectPoints, *my_args)
        return ret

    def select_points_in_polygon(self, *args):
        """
        V.select_points_in_polygon(ContextPolygon) -> bool
        C++: virtual bool SelectPointsInPolygon(
            const ContextPolygon &polygon)
        Select all points in the specified polygon.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SelectPointsInPolygon, *my_args)
        return ret

    def set_input_array(self, *args):
        """
        V.set_input_array(int, string)
        C++: virtual void SetInputArray(int index,
            const StdString &name)
        Convenience function to set the input arrays. For most plots
        index 0 is the x axis, and index 1 is the y axis. The name is the
        name of the column in the Table.
        """
        ret = self._wrap_call(self._vtk_obj.SetInputArray, *args)
        return ret

    def set_input_data(self, *args):
        """
        V.set_input_data(Table)
        C++: virtual void SetInputData(Table *table)
        V.set_input_data(Table, string, string)
        C++: virtual void SetInputData(Table *table,
            const StdString &xColumn, const StdString &yColumn)
        V.set_input_data(Table, int, int)
        C++: void SetInputData(Table *table, IdType xColumn,
            IdType yColumn)
        This is a convenience function to set the input table and the x,
        y column for the plot.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    def update_cache(self):
        """
        V.update_cache()
        C++: virtual void UpdateCache()
        Subclasses that build data caches to speed up painting should
        override this method to update such caches. This is called on
        each Paint, hence subclasses must add checks to avoid rebuilding
        of cache, unless necessary. Default implementation is empty.
        """
        ret = self._vtk_obj.UpdateCache()
        return ret
        

    _updateable_traits_ = \
    (('legend_visibility', 'GetLegendVisibility'), ('selectable',
    'GetSelectable'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('label', 'GetLabel'),
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
    'selectable', 'interactive', 'label', 'opacity',
    'tooltip_label_format', 'tooltip_notation', 'tooltip_precision',
    'use_index_for_x_series', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Plot, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Plot properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['legend_visibility', 'selectable'], [], ['interactive',
            'label', 'opacity', 'tooltip_label_format', 'tooltip_notation',
            'tooltip_precision', 'use_index_for_x_series', 'visible', 'width']),
            title='Edit Plot properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Plot properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


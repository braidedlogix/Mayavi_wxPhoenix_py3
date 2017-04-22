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


class ChartBox(Chart):
    """
    ChartBox - Factory class for drawing box plot charts
    
    Superclass: Chart
    
    This defines the interface for a box plot chart.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkChartBox, obj, update, **traits)
    
    def get_column_visibility(self, *args):
        """
        V.get_column_visibility(string) -> bool
        C++: bool GetColumnVisibility(const StdString &name)
        V.get_column_visibility(int) -> bool
        C++: bool GetColumnVisibility(IdType column)
        Get the visibility of the specified column.
        """
        ret = self._wrap_call(self._vtk_obj.GetColumnVisibility, *args)
        return ret

    def set_column_visibility(self, *args):
        """
        V.set_column_visibility(string, bool)
        C++: void SetColumnVisibility(const StdString &name,
            bool visible)
        V.set_column_visibility(int, bool)
        C++: void SetColumnVisibility(IdType column, bool visible)
        Set the visibility of the specified column.
        """
        ret = self._wrap_call(self._vtk_obj.SetColumnVisibility, *args)
        return ret

    def get_plot(self, *args):
        """
        V.get_plot(int) -> Plot
        C++: virtual Plot *GetPlot(IdType index)
        Get the plot at the specified index, returns null if the index is
        invalid.
        """
        ret = self._wrap_call(self._vtk_obj.GetPlot, *args)
        return wrap_vtk(ret)

    def set_plot(self, *args):
        """
        V.set_plot(PlotBox)
        C++: virtual void SetPlot(PlotBox *plot)
        Set plot to use for the chart. Since this type of chart can only
        contain one plot, this will replace the previous plot.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPlot, *my_args)
        return ret

    selected_column = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _selected_column_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectedColumn,
                        self.selected_column)

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

    def get_column_id(self, *args):
        """
        V.get_column_id(string) -> int
        C++: IdType GetColumnId(const StdString &name)
        Get the input table column id of a column by its name.
        """
        ret = self._wrap_call(self._vtk_obj.GetColumnId, *args)
        return ret

    def _get_number_of_visible_columns(self):
        return self._vtk_obj.GetNumberOfVisibleColumns()
    number_of_visible_columns = traits.Property(_get_number_of_visible_columns, help=\
        """
        Get the number of visible box plots in the current chart.
        """
    )

    def _get_visible_columns(self):
        return wrap_vtk(self._vtk_obj.GetVisibleColumns())
    visible_columns = traits.Property(_get_visible_columns, help=\
        """
        Get a list of the columns, and the order in which they are
        displayed.
        """
    )

    def get_x_position(self, *args):
        """
        V.get_x_position(int) -> float
        C++: virtual float GetXPosition(int index)
        Get the column X position by index in the visible set.
        """
        ret = self._wrap_call(self._vtk_obj.GetXPosition, *args)
        return ret

    def _get_y_axis(self):
        return wrap_vtk(self._vtk_obj.GetYAxis())
    y_axis = traits.Property(_get_y_axis, help=\
        """
        Get the chart Y axis
        """
    )

    def set_column_visibility_all(self, *args):
        """
        V.set_column_visibility_all(bool)
        C++: void SetColumnVisibilityAll(bool visible)
        Set the visibility of all columns (true will make them all
        visible, false will remove all visible columns).
        """
        ret = self._wrap_call(self._vtk_obj.SetColumnVisibilityAll, *args)
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

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('selected_column', 'GetSelectedColumn'),
    ('auto_size', 'GetAutoSize'), ('geometry', 'GetGeometry'),
    ('layout_strategy', 'GetLayoutStrategy'), ('point1', 'GetPoint1'),
    ('point2', 'GetPoint2'), ('render_empty', 'GetRenderEmpty'),
    ('selection_method', 'GetSelectionMethod'), ('selection_mode',
    'GetSelectionMode'), ('show_legend', 'GetShowLegend'), ('title',
    'GetTitle'), ('opacity', 'GetOpacity'), ('interactive',
    'GetInteractive'), ('visible', 'GetVisible'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'auto_size', 'geometry',
    'interactive', 'layout_strategy', 'opacity', 'point1', 'point2',
    'render_empty', 'selected_column', 'selection_method',
    'selection_mode', 'show_legend', 'title', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ChartBox, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ChartBox properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['auto_size', 'geometry', 'interactive',
            'layout_strategy', 'opacity', 'point1', 'point2', 'render_empty',
            'selected_column', 'selection_method', 'selection_mode',
            'show_legend', 'title', 'visible']),
            title='Edit ChartBox properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ChartBox properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


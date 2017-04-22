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

from tvtk.tvtk_classes.chart_matrix import ChartMatrix


class ScatterPlotMatrix(ChartMatrix):
    """
    ScatterPlotMatrix - container for a matrix of charts.
    
    Superclass: ChartMatrix
    
    This class contains a matrix of charts. These charts will be of type
    ChartXY by default, but this can be overridden. The class will
    manage their layout and object lifetime.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScatterPlotMatrix, obj, update, **traits)
    
    def get_axis_color(self, *args):
        """
        V.get_axis_color(int) -> Color4ub
        C++: Color4ub GetAxisColor(int plotType)
        Sets the color for the axes given a plot type, which refers to
        ScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM, ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.GetAxisColor, *args)
        return wrap_vtk(ret)

    def set_axis_color(self, *args):
        """
        V.set_axis_color(int, Color4ub)
        C++: void SetAxisColor(int plotType, const Color4ub &color)
        Sets the color for the axes given a plot type, which refers to
        ScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM, ACTIVEPLOT}.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetAxisColor, *my_args)
        return ret

    def get_axis_label_notation(self, *args):
        """
        V.get_axis_label_notation(int) -> int
        C++: int GetAxisLabelNotation(int plotType)
        Sets the axis label notation for the axes given a plot type,
        which refers to ScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.GetAxisLabelNotation, *args)
        return ret

    def set_axis_label_notation(self, *args):
        """
        V.set_axis_label_notation(int, int)
        C++: void SetAxisLabelNotation(int plotType, int notation)
        Sets the axis label notation for the axes given a plot type,
        which refers to ScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.SetAxisLabelNotation, *args)
        return ret

    def get_axis_label_precision(self, *args):
        """
        V.get_axis_label_precision(int) -> int
        C++: int GetAxisLabelPrecision(int plotType)
        Sets the axis label precision for the axes given a plot type,
        which refers to ScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.GetAxisLabelPrecision, *args)
        return ret

    def set_axis_label_precision(self, *args):
        """
        V.set_axis_label_precision(int, int)
        C++: void SetAxisLabelPrecision(int plotType, int precision)
        Sets the axis label precision for the axes given a plot type,
        which refers to ScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.SetAxisLabelPrecision, *args)
        return ret

    def get_axis_label_properties(self, *args):
        """
        V.get_axis_label_properties(int) -> TextProperty
        C++: TextProperty *GetAxisLabelProperties(int plotType)
        Set/get the text property for the axis labels of the given plot
        type, possible types are ScatterPlotMatrix::{SCATTERPLOT,
        HISTOGRAM, ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.GetAxisLabelProperties, *args)
        return wrap_vtk(ret)

    def set_axis_label_properties(self, *args):
        """
        V.set_axis_label_properties(int, TextProperty)
        C++: void SetAxisLabelProperties(int plotType,
            TextProperty *prop)
        Set/get the text property for the axis labels of the given plot
        type, possible types are ScatterPlotMatrix::{SCATTERPLOT,
        HISTOGRAM, ACTIVEPLOT}.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetAxisLabelProperties, *my_args)
        return ret

    def get_axis_label_visibility(self, *args):
        """
        V.get_axis_label_visibility(int) -> bool
        C++: bool GetAxisLabelVisibility(int plotType)
        Sets whether or not the labels for the axes are visible, given a
        plot type, which refers to ScatterPlotMatrix::{SCATTERPLOT,
        HISTOGRAM, ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.GetAxisLabelVisibility, *args)
        return ret

    def set_axis_label_visibility(self, *args):
        """
        V.set_axis_label_visibility(int, bool)
        C++: void SetAxisLabelVisibility(int plotType, bool visible)
        Sets whether or not the labels for the axes are visible, given a
        plot type, which refers to ScatterPlotMatrix::{SCATTERPLOT,
        HISTOGRAM, ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.SetAxisLabelVisibility, *args)
        return ret

    def get_background_color(self, *args):
        """
        V.get_background_color(int) -> Color4ub
        C++: Color4ub GetBackgroundColor(int plotType)
        Sets the background color for the chart given a plot type, which
        refers to ScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.GetBackgroundColor, *args)
        return wrap_vtk(ret)

    def set_background_color(self, *args):
        """
        V.set_background_color(int, Color4ub)
        C++: void SetBackgroundColor(int plotType,
            const Color4ub &color)
        Sets the background color for the chart given a plot type, which
        refers to ScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetBackgroundColor, *my_args)
        return ret

    def get_column_visibility(self, *args):
        """
        V.get_column_visibility(string) -> bool
        C++: bool GetColumnVisibility(const StdString &name)
        Get the visibility of the specified column.
        """
        ret = self._wrap_call(self._vtk_obj.GetColumnVisibility, *args)
        return ret

    def set_column_visibility(self, *args):
        """
        V.set_column_visibility(string, bool)
        C++: void SetColumnVisibility(const StdString &name,
            bool visible)
        Set the visibility of the specified column.
        """
        ret = self._wrap_call(self._vtk_obj.SetColumnVisibility, *args)
        return ret

    def get_grid_color(self, *args):
        """
        V.get_grid_color(int) -> Color4ub
        C++: Color4ub GetGridColor(int plotType)
        Sets the color for the axes given a plot type, which refers to
        ScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM, ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.GetGridColor, *args)
        return wrap_vtk(ret)

    def set_grid_color(self, *args):
        """
        V.set_grid_color(int, Color4ub)
        C++: void SetGridColor(int plotType, const Color4ub &color)
        Sets the color for the axes given a plot type, which refers to
        ScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM, ACTIVEPLOT}.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGridColor, *my_args)
        return ret

    def get_grid_visibility(self, *args):
        """
        V.get_grid_visibility(int) -> bool
        C++: bool GetGridVisibility(int plotType)
        Sets whether or not the grid for the given axis is visible given
        a plot type, which refers to ScatterPlotMatrix::{SCATTERPLOT,
        HISTOGRAM, ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.GetGridVisibility, *args)
        return ret

    def set_grid_visibility(self, *args):
        """
        V.set_grid_visibility(int, bool)
        C++: void SetGridVisibility(int plotType, bool visible)
        Sets whether or not the grid for the given axis is visible given
        a plot type, which refers to ScatterPlotMatrix::{SCATTERPLOT,
        HISTOGRAM, ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.SetGridVisibility, *args)
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

    number_of_bins = traits.Int(10, enter_set=True, auto_set=False, help=\
        """
        Set the number of bins in the histograms along the central
        diagonal of the scatter plot matrix.
        """
    )

    def _number_of_bins_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfBins,
                        self.number_of_bins)

    number_of_frames = traits.Int(25, enter_set=True, auto_set=False, help=\
        """
        Set the number of animation frames in each transition. Default is
        25, and 0 means to animations between axes.
        """
    )

    def _number_of_frames_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfFrames,
                        self.number_of_frames)

    def _get_scene(self):
        return wrap_vtk(self._vtk_obj.GetScene())
    def _set_scene(self, arg):
        old_val = self._get_scene()
        self._wrap_call(self._vtk_obj.SetScene,
                        deref_vtk(arg))
        self.trait_property_changed('scene', old_val, arg)
    scene = traits.Property(_get_scene, _set_scene, help=\
        """
        Get the ContextScene for the item, always set for an item in a
        scene.
        """
    )

    selection_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get the Selection Mode that will be used by the chart while
        doing selection. The only valid enums are
        ContextScene::SELECTION_NONE, SELECTION_DEFAULT,
        SELECTION_ADDITION, SELECTION_SUBTRACTION, SELECTION_TOGGLE
        """
    )

    def _selection_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionMode,
                        self.selection_mode)

    title = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Set/get the scatter plot title.
        """
    )

    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    def _get_title_properties(self):
        return wrap_vtk(self._vtk_obj.GetTitleProperties())
    def _set_title_properties(self, arg):
        old_val = self._get_title_properties()
        self._wrap_call(self._vtk_obj.SetTitleProperties,
                        deref_vtk(arg))
        self.trait_property_changed('title_properties', old_val, arg)
    title_properties = traits.Property(_get_title_properties, _set_title_properties, help=\
        """
        Set/get the text properties for the chart title, i.e. color,
        font, size.
        """
    )

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
        active chart.
        """
    )

    def get_tooltip_notation(self, *args):
        """
        V.get_tooltip_notation(int) -> int
        C++: int GetTooltipNotation(int plotType)
        Set chart's tooltip notation and precision, given a plot type,
        which refers to ScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.GetTooltipNotation, *args)
        return ret

    def set_tooltip_notation(self, *args):
        """
        V.set_tooltip_notation(int, int)
        C++: void SetTooltipNotation(int plotType, int notation)
        Set chart's tooltip notation and precision, given a plot type,
        which refers to ScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.SetTooltipNotation, *args)
        return ret

    def get_tooltip_precision(self, *args):
        """
        V.get_tooltip_precision(int) -> int
        C++: int GetTooltipPrecision(int plotType)
        Set chart's tooltip notation and precision, given a plot type,
        which refers to ScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.GetTooltipPrecision, *args)
        return ret

    def set_tooltip_precision(self, *args):
        """
        V.set_tooltip_precision(int, int)
        C++: void SetTooltipPrecision(int plotType, int precision)
        Set chart's tooltip notation and precision, given a plot type,
        which refers to ScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ret = self._wrap_call(self._vtk_obj.SetTooltipPrecision, *args)
        return ret

    def _get_visible_columns(self):
        return wrap_vtk(self._vtk_obj.GetVisibleColumns())
    def _set_visible_columns(self, arg):
        old_val = self._get_visible_columns()
        my_arg = deref_array([arg], [['vtkStringArray']])
        self._wrap_call(self._vtk_obj.SetVisibleColumns,
                        my_arg[0])
        self.trait_property_changed('visible_columns', old_val, arg)
    visible_columns = traits.Property(_get_visible_columns, _set_visible_columns, help=\
        """
        Get a list of the columns, and the order in which they are
        displayed.
        """
    )

    def get_animation_path_element(self, *args):
        """
        V.get_animation_path_element(int) -> Vector2i
        C++: Vector2i GetAnimationPathElement(IdType i)
        Get the element specified from the animation path.
        """
        ret = self._wrap_call(self._vtk_obj.GetAnimationPathElement, *args)
        return wrap_vtk(ret)

    def _get_annotation_link(self):
        return wrap_vtk(self._vtk_obj.GetAnnotationLink())
    annotation_link = traits.Property(_get_annotation_link, help=\
        """
        Get the annotation_link for the scatter plot matrix, this gives
        you access to the currently selected points in the scatter plot
        matrix.
        """
    )

    def get_column_name(self, *args):
        """
        V.get_column_name(int) -> string
        C++: StdString GetColumnName(int column)
        Get the column name for the supplied index.
        """
        ret = self._wrap_call(self._vtk_obj.GetColumnName, *args)
        return ret

    def _get_main_chart(self):
        return wrap_vtk(self._vtk_obj.GetMainChart())
    main_chart = traits.Property(_get_main_chart, help=\
        """
        Get the main plot (the one in the top-right of the matrix.
        """
    )

    def _get_number_of_animation_path_elements(self):
        return self._vtk_obj.GetNumberOfAnimationPathElements()
    number_of_animation_path_elements = traits.Property(_get_number_of_animation_path_elements, help=\
        """
        Get the number of elements (transitions) in the animation path.
        """
    )

    def get_plot_type(self, *args):
        """
        V.get_plot_type(Vector2i) -> int
        C++: int GetPlotType(const Vector2i &pos)
        V.get_plot_type(int, int) -> int
        C++: int GetPlotType(int row, int column)
        Returns the type of the plot at the given position. The return
        value is one of: SCATTERPLOT, HISTOGRAM, ACTIVEPLOT, or NOPLOT.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPlotType, *my_args)
        return ret

    def get_row_name(self, *args):
        """
        V.get_row_name(int) -> string
        C++: StdString GetRowName(int row)
        Get the column name for the supplied index.
        """
        ret = self._wrap_call(self._vtk_obj.GetRowName, *args)
        return ret

    def add_animation_path(self, *args):
        """
        V.add_animation_path(Vector2i) -> bool
        C++: bool AddAnimationPath(const Vector2i &move)
        Add a move to the animation path. Note that a move can only
        change i or j, not both. If the proposed move does not satisfy
        those criteria it will be rejected and the animation path will
        not be extended.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddAnimationPath, *my_args)
        return ret

    def advance_animation(self):
        """
        V.advance_animation()
        C++: virtual void AdvanceAnimation()
        Advance the animation in response to the timer events. This is
        public to allow the animation to be manually advanced when timers
        are not a
        """
        ret = self._vtk_obj.AdvanceAnimation()
        return ret
        

    def begin_animation_path(self, *args):
        """
        V.begin_animation_path(RenderWindowInteractor) -> bool
        C++: bool BeginAnimationPath(
            RenderWindowInteractor *interactor)
        Trigger the animation of the scatter plot matrix to begin.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.BeginAnimationPath, *my_args)
        return ret

    def clear_animation_path(self):
        """
        V.clear_animation_path()
        C++: void ClearAnimationPath()
        Clear the animation path.
        """
        ret = self._vtk_obj.ClearAnimationPath()
        return ret
        

    def insert_visible_column(self, *args):
        """
        V.insert_visible_column(string, int)
        C++: void InsertVisibleColumn(const StdString &name, int index)
        Insert the specified column at the index position of the visible
        columns.
        """
        ret = self._wrap_call(self._vtk_obj.InsertVisibleColumn, *args)
        return ret

    def set_column_visibility_all(self, *args):
        """
        V.set_column_visibility_all(bool)
        C++: void SetColumnVisibilityAll(bool visible)
        Set the visibility of all columns (true will make them all
        visible, false will remove all visible columns).
        """
        ret = self._wrap_call(self._vtk_obj.SetColumnVisibilityAll, *args)
        return ret

    def set_input(self, *args):
        """
        V.set_input(Table)
        C++: virtual void SetInput(Table *table)
        Set the input table for the scatter plot matrix. This will cause
        all columns to be plotted against each other - a square scatter
        plot matrix.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    def set_plot_color(self, *args):
        """
        V.set_plot_color(int, Color4ub)
        C++: void SetPlotColor(int plotType, const Color4ub &color)
        Set the color for the specified plot_type.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPlotColor, *my_args)
        return ret

    def set_plot_marker_size(self, *args):
        """
        V.set_plot_marker_size(int, float)
        C++: void SetPlotMarkerSize(int plotType, float size)
        Sets the marker size for the specified plot_type.
        """
        ret = self._wrap_call(self._vtk_obj.SetPlotMarkerSize, *args)
        return ret

    def set_plot_marker_style(self, *args):
        """
        V.set_plot_marker_style(int, int)
        C++: void SetPlotMarkerStyle(int plotType, int style)
        Sets the marker style for the specified plot_type.
        """
        ret = self._wrap_call(self._vtk_obj.SetPlotMarkerStyle, *args)
        return ret

    def update_chart_settings(self, *args):
        """
        V.update_chart_settings(int)
        C++: void UpdateChartSettings(int plotType)
        Update charts based on settings given the plot type
        """
        ret = self._wrap_call(self._vtk_obj.UpdateChartSettings, *args)
        return ret

    def update_settings(self):
        """
        V.update_settings()
        C++: void UpdateSettings()
        Convenient method to update all the chart settings
        """
        ret = self._vtk_obj.UpdateSettings()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_bins', 'GetNumberOfBins'),
    ('number_of_frames', 'GetNumberOfFrames'), ('selection_mode',
    'GetSelectionMode'), ('title', 'GetTitle'), ('interactive',
    'GetInteractive'), ('visible', 'GetVisible'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'interactive', 'number_of_bins',
    'number_of_frames', 'selection_mode', 'title', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScatterPlotMatrix, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ScatterPlotMatrix properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['interactive', 'number_of_bins', 'number_of_frames',
            'selection_mode', 'title', 'visible']),
            title='Edit ScatterPlotMatrix properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScatterPlotMatrix properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.rendered_representation import RenderedRepresentation


class ParallelCoordinatesRepresentation(RenderedRepresentation):
    """
    ParallelCoordinatesRepresentation - Data representation that
     takes generic multivariate data and produces a parallel coordinates
    plot.
    
    Superclass: RenderedRepresentation
    
    A parallel coordinates plot represents each variable in a
    multivariate
     data set as a separate axis.  Individual samples of that data set
    are
     represented as a polyline that pass through each variable axis at
     positions that correspond to data values. 
    ParallelCoordinatesRepresentation
     generates this plot when added to a ParallelCoordinatesView,
    which handles
     interaction and highlighting.  Sample polylines can alternatively
     be represented as s-curves by enabling the use_curves flag.
    
    
     There are three selection modes: lasso, angle, and function. Lasso
    selection
     picks sample lines that pass through a polyline.  Angle selection
    picks sample
     lines that have similar slope to a line segment.  Function selection
    picks
     sample lines that are near a linear function defined on two
    variables.  This
     function specified by passing two (x,y) variable value pairs.
    
    
     All primitives are plotted in normalized view coordinates [0,1].
    
    @sa
     ParallelCoordinatesView
    ParallelCoordinatesHistogramRepresentation
     SCurveSpline
    
    @par Thanks:
     Developed by David Feng at Sandia National Laboratories
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParallelCoordinatesRepresentation, obj, update, **traits)
    
    use_curves = tvtk_base.false_bool_trait(help=\
        """
        Whether or not to display using curves
        """
    )

    def _use_curves_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseCurves,
                        self.use_curves_)

    angle_brush_threshold = traits.Float(0.03, enter_set=True, auto_set=False, help=\
        """
        Maximum angle difference (in degrees) of selection using
        angle/function brushes
        """
    )

    def _angle_brush_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAngleBrushThreshold,
                        self.angle_brush_threshold)

    axis_color = tvtk_base.vtk_color_trait((1.0, 0.8, 0.3), help=\
        """
        
        """
    )

    def _axis_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisColor,
                        self.axis_color, False)

    axis_label_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )

    def _axis_label_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisLabelColor,
                        self.axis_label_color, False)

    curve_resolution = traits.Int(20, enter_set=True, auto_set=False, help=\
        """
        Resolution of the curves displayed, enabled by setting use_curves
        """
    )

    def _curve_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCurveResolution,
                        self.curve_resolution)

    font_size = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Access plot properties
        """
    )

    def _font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFontSize,
                        self.font_size)

    function_brush_threshold = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Maximum angle difference (in degrees) of selection using
        angle/function brushes
        """
    )

    def _function_brush_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFunctionBrushThreshold,
                        self.function_brush_threshold)

    line_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )

    def _line_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineColor,
                        self.line_color, False)

    line_opacity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Access plot properties
        """
    )

    def _line_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineOpacity,
                        self.line_opacity)

    number_of_axis_labels = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of labels to display on each axis
        """
    )

    def _number_of_axis_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfAxisLabels,
                        self.number_of_axis_labels)

    def get_position_and_size(self, *args):
        """
        V.get_position_and_size([float, ...], [float, ...]) -> int
        C++: int GetPositionAndSize(double *position, double *size)
        Change the position of the plot
        """
        ret = self._wrap_call(self._vtk_obj.GetPositionAndSize, *args)
        return ret

    def set_position_and_size(self, *args):
        """
        V.set_position_and_size([float, ...], [float, ...]) -> int
        C++: int SetPositionAndSize(double *position, double *size)
        Change the position of the plot
        """
        ret = self._wrap_call(self._vtk_obj.SetPositionAndSize, *args)
        return ret

    def get_range_at_position(self, *args):
        """
        V.get_range_at_position(int, [float, float]) -> int
        C++: int GetRangeAtPosition(int position, double range[2])
        Set/get the value range of the axis at a particular screen
        position
        """
        ret = self._wrap_call(self._vtk_obj.GetRangeAtPosition, *args)
        return ret

    def set_range_at_position(self, *args):
        """
        V.set_range_at_position(int, [float, float]) -> int
        C++: virtual int SetRangeAtPosition(int position, double range[2])
        Set/get the value range of the axis at a particular screen
        position
        """
        ret = self._wrap_call(self._vtk_obj.SetRangeAtPosition, *args)
        return ret

    def get_x_coordinate_of_position(self, *args):
        """
        V.get_x_coordinate_of_position(int) -> float
        C++: double GetXCoordinateOfPosition(int axis)
        Move an axis to a particular screen position.  Using these
        methods requires an Update() before they will work properly.
        """
        ret = self._wrap_call(self._vtk_obj.GetXCoordinateOfPosition, *args)
        return ret

    def set_x_coordinate_of_position(self, *args):
        """
        V.set_x_coordinate_of_position(int, float) -> int
        C++: int SetXCoordinateOfPosition(int position, double xcoord)
        Move an axis to a particular screen position.  Using these
        methods requires an Update() before they will work properly.
        """
        ret = self._wrap_call(self._vtk_obj.SetXCoordinateOfPosition, *args)
        return ret

    def get_hover_text(self, *args):
        """
        V.get_hover_text(View, int, int) -> string
        C++: virtual const char *GetHoverText(View *view, int x, int y)
        Returns the hover text at an x,y location.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetHoverText, *my_args)
        return ret

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def _get_number_of_axes(self):
        return self._vtk_obj.GetNumberOfAxes()
    number_of_axes = traits.Property(_get_number_of_axes, help=\
        """
        Get the number of axes in the plot
        """
    )

    def _get_number_of_samples(self):
        return self._vtk_obj.GetNumberOfSamples()
    number_of_samples = traits.Property(_get_number_of_samples, help=\
        """
        Get the number of samples in the plot
        """
    )

    def get_position_near_x_coordinate(self, *args):
        """
        V.get_position_near_x_coordinate(float) -> int
        C++: int GetPositionNearXCoordinate(double xcoord)
        Move an axis to a particular screen position.  Using these
        methods requires an Update() before they will work properly.
        """
        ret = self._wrap_call(self._vtk_obj.GetPositionNearXCoordinate, *args)
        return ret

    def get_x_coordinates_of_positions(self, *args):
        """
        V.get_x_coordinates_of_positions([float, ...])
        C++: void GetXCoordinatesOfPositions(double *coords)
        Move an axis to a particular screen position.  Using these
        methods requires an Update() before they will work properly.
        """
        ret = self._wrap_call(self._vtk_obj.GetXCoordinatesOfPositions, *args)
        return ret

    def angle_select(self, *args):
        """
        V.angle_select(int, int, [float, ...], [float, ...])
        C++: virtual void AngleSelect(int brushClass, int brushOperator,
            double *p1, double *p2)
        Do a selection of the lines.  See the main description for how to
        use these functions. range_select is currently stubbed out.
        """
        ret = self._wrap_call(self._vtk_obj.AngleSelect, *args)
        return ret

    def function_select(self, *args):
        """
        V.function_select(int, int, [float, ...], [float, ...], [float,
            ...], [float, ...])
        C++: virtual void FunctionSelect(int brushClass,
            int brushOperator, double *p1, double *p2, double *q1,
            double *q2)
        Do a selection of the lines.  See the main description for how to
        use these functions. range_select is currently stubbed out.
        """
        ret = self._wrap_call(self._vtk_obj.FunctionSelect, *args)
        return ret

    def lasso_select(self, *args):
        """
        V.lasso_select(int, int, Points)
        C++: virtual void LassoSelect(int brushClass, int brushOperator,
            Points *brushPoints)
        Do a selection of the lines.  See the main description for how to
        use these functions. range_select is currently stubbed out.
        """
        my_args = deref_array(args, [('int', 'int', 'vtkPoints')])
        ret = self._wrap_call(self._vtk_obj.LassoSelect, *my_args)
        return ret

    def range_select(self, *args):
        """
        V.range_select(int, int, [float, ...], [float, ...])
        C++: virtual void RangeSelect(int brushClass, int brushOperator,
            double *p1, double *p2)
        Do a selection of the lines.  See the main description for how to
        use these functions. range_select is currently stubbed out.
        """
        ret = self._wrap_call(self._vtk_obj.RangeSelect, *args)
        return ret

    def reset_axes(self):
        """
        V.reset_axes()
        C++: void ResetAxes()
        Reset the axes to their default positions and orders
        """
        ret = self._vtk_obj.ResetAxes()
        return ret
        

    def set_axis_titles(self, *args):
        """
        V.set_axis_titles(StringArray)
        C++: void SetAxisTitles(StringArray *)
        V.set_axis_titles(AlgorithmOutput)
        C++: void SetAxisTitles(AlgorithmOutput *)
        Set/Get the axis titles
        """
        my_args = deref_array(args, [['vtkStringArray'], ['vtkAlgorithmOutput']])
        ret = self._wrap_call(self._vtk_obj.SetAxisTitles, *my_args)
        return ret

    def set_plot_title(self, *args):
        """
        V.set_plot_title(string)
        C++: void SetPlotTitle(const char *)
        Set the title for the entire plot
        """
        ret = self._wrap_call(self._vtk_obj.SetPlotTitle, *args)
        return ret

    def swap_axis_positions(self, *args):
        """
        V.swap_axis_positions(int, int) -> int
        C++: virtual int SwapAxisPositions(int position1, int position2)
        Move an axis to a particular screen position.  Using these
        methods requires an Update() before they will work properly.
        """
        ret = self._wrap_call(self._vtk_obj.SwapAxisPositions, *args)
        return ret

    _updateable_traits_ = \
    (('use_curves', 'GetUseCurves'), ('selectable', 'GetSelectable'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('angle_brush_threshold', 'GetAngleBrushThreshold'), ('axis_color',
    'GetAxisColor'), ('axis_label_color', 'GetAxisLabelColor'),
    ('curve_resolution', 'GetCurveResolution'), ('font_size',
    'GetFontSize'), ('function_brush_threshold',
    'GetFunctionBrushThreshold'), ('line_color', 'GetLineColor'),
    ('line_opacity', 'GetLineOpacity'), ('number_of_axis_labels',
    'GetNumberOfAxisLabels'), ('label_render_mode', 'GetLabelRenderMode'),
    ('selection_array_name', 'GetSelectionArrayName'), ('selection_type',
    'GetSelectionType'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'selectable', 'use_curves',
    'angle_brush_threshold', 'axis_color', 'axis_label_color',
    'curve_resolution', 'font_size', 'function_brush_threshold',
    'label_render_mode', 'line_color', 'line_opacity',
    'number_of_axis_labels', 'progress_text', 'selection_array_name',
    'selection_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParallelCoordinatesRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ParallelCoordinatesRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['selectable', 'use_curves'], [], ['angle_brush_threshold',
            'axis_color', 'axis_label_color', 'curve_resolution', 'font_size',
            'function_brush_threshold', 'label_render_mode', 'line_color',
            'line_opacity', 'number_of_axis_labels', 'selection_array_name',
            'selection_type']),
            title='Edit ParallelCoordinatesRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParallelCoordinatesRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


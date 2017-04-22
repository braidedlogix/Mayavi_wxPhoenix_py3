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


class Axis(ContextItem):
    """
    Axis - takes care of drawing 2d axes
    
    Superclass: ContextItem
    
    The Axis is drawn in screen coordinates. It is usually one of the
    last elements of a chart to be drawn. It renders the axis label, tick
    marks and tick labels. The tick marks and labels span the range of
    values between_minimum and Maximum. The Minimum and Maximum values are
    not allowed to extend beyond the_minimum_limit and maximum_limit values,
    respectively.
    
    Note that many other chart elements (e.g., PlotPoints) refer to
    Axis instances to determine how to scale raw data for
    presentation. In particular, care must be taken with logarithmic
    scaling. The axis Minimum, Maximum, and Limit values are stored both
    unscaled and scaled (with log(x) applied when get_log_scale_active()
    returns true). User interfaces will most likely present the unscaled
    values as they represent the values provided by the user. Other chart
    elements may need the scaled values in order to draw in the same
    coordinate system.
    
    Just because log_scale is set to true does not guarantee that the axis
    will use logarithmic scaling -- the Minimum and Maximum values for
    the axis must both lie to the same side of origin (and not include
    the origin). Also, this switch from linear- to log-scaling may occur
    during a rendering pass if autoscaling is enabled. Because the log
    and pow functions are not invertible and the axis itself decides when
    to switch between them without offering any external class managing
    the axis a chance to save the old values, it saves old Limit values
    in non_log_unscaled{_min,_max}_limit so that behavior is consistent when
    log_scale is changed from false to true and back again.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAxis, obj, update, **traits)
    
    log_scale = tvtk_base.false_bool_trait(help=\
        """
        Get/set whether the axis should attemptto use a log scale.
        
        * The default is false.
        * \sa{_log_scale_active}.
        """
    )

    def _log_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLogScale,
                        self.log_scale_)

    axis_visible = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Get/set whether the axis line should be visible.
        """
    )

    def _axis_visible_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisVisible,
                        self.axis_visible)

    behavior = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/set the behavior of the axis (auto or fixed). The default is
        0 (auto).
        """
    )

    def _behavior_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBehavior,
                        self.behavior)

    grid_visible = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Get/set whether the axis grid lines should be drawn, default is
        true.
        """
    )

    def _grid_visible_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridVisible,
                        self.grid_visible)

    label_format = traits.String('%g', enter_set=True, auto_set=False, help=\
        """
        Get/Set the printf-style format string used when
        tick_label_algorithm is TICK_SIMPLE and Notation is
        PRINTF_NOTATION. The default is "%g".
        """
    )

    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    label_offset = traits.Float(7.0, enter_set=True, auto_set=False, help=\
        """
        Get/set the offset (in pixels) of the label text position from
        the axis
        """
    )

    def _label_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelOffset,
                        self.label_offset)

    labels_visible = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Get/set whether the axis labels should be visible.
        """
    )

    def _labels_visible_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelsVisible,
                        self.labels_visible)

    margins = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(15, 5), cols=2, help=\
        """
        
        """
    )

    def _margins_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMargins,
                        self.margins)

    maximum = traits.Float(6.66, enter_set=True, auto_set=False, help=\
        """
        Set the logical maximum value of the axis, in plot coordinates.
        If log_scale_active is true (not just log_scale), then this sets the
        maximum base-10 exponent.
        """
    )

    def _maximum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximum,
                        self.maximum)

    maximum_limit = traits.Float(1.7976931348623157e+308, enter_set=True, auto_set=False, help=\
        """
        Set the logical highest possible value for Maximum, in plot
        coordinates.
        """
    )

    def _maximum_limit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumLimit,
                        self.maximum_limit)

    minimum = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the logical minimum value of the axis, in plot coordinates.
        If log_scale_active is true (not just log_scale), then this sets the
        minimum base-10 exponent.
        """
    )

    def _minimum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimum,
                        self.minimum)

    minimum_limit = traits.Float(-1.7976931348623157e+308, enter_set=True, auto_set=False, help=\
        """
        Set the logical lowest possible value for Minimum, in plot
        coordinates.
        """
    )

    def _minimum_limit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumLimit,
                        self.minimum_limit)

    notation = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/set the numerical notation, standard, scientific, fixed, or a
        printf-style format string.
        \sa set_precision set_label_format
        """
    )

    def _notation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNotation,
                        self.notation)

    number_of_ticks = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the number of tick marks for this axis. Default is -1, which
        leads to automatic calculation of nicely spaced tick marks.
        """
    )

    def _number_of_ticks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTicks,
                        self.number_of_ticks)

    point1 = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 10.0), cols=2, help=\
        """
        Set point 1 of the axis (in pixels), this is usually the origin.
        """
    )

    def _point1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1,
                        self.point1)

    point2 = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 10.0), cols=2, help=\
        """
        Set point 2 of the axis (in pixels), this is usually the
        terminus.
        """
    )

    def _point2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2,
                        self.point2)

    position = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/set the position of the axis (LEFT, BOTTOM, RIGHT, TOP,
        PARALLEL).
        """
    )

    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    precision = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Get/set the numerical precision to use, default is 2. This is
        ignored when Notation is STANDARD_NOTATION or PRINTF_NOTATION.
        """
    )

    def _precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPrecision,
                        self.precision)

    def get_range(self, *args):
        """
        V.get_range([float, ...])
        C++: virtual void GetRange(double *range)
        Get the logical range of the axis, in plot coordinates.
        
        * The unscaled range will always be in the same coordinate system
        of
        * the data being plotted, regardless of whether log_scale is true
          or false.
        * Calling get_range() when log_scale is true will return the
          log10({min, max}).
        """
        ret = self._wrap_call(self._vtk_obj.GetRange, *args)
        return ret

    def set_range(self, *args):
        """
        V.set_range(float, float)
        C++: virtual void SetRange(double minimum, double maximum)
        V.set_range([float, float])
        C++: virtual void SetRange(double range[2])
        Set the logical range of the axis, in plot coordinates.
        
        * The unscaled range will always be in the same coordinate system
        of
        * the data being plotted, regardless of whether log_scale is true
          or false.
        * When calling set_range() and log_scale is true, the range must be
        specified
        * in logarithmic coordinates.
        * Using set_unscaled_range(), you may ignore the value of log_scale.
        """
        ret = self._wrap_call(self._vtk_obj.SetRange, *args)
        return ret

    range_label_format = traits.String('%g', enter_set=True, auto_set=False, help=\
        """
        Get/Set the printf-style format string used for range labels.
        This format is always used regardless of tick_label_algorithm and
        Notation. Default is "%g".
        """
    )

    def _range_label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRangeLabelFormat,
                        self.range_label_format)

    range_labels_visible = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Get/set whether the labels for the range should be visible.
        """
    )

    def _range_labels_visible_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRangeLabelsVisible,
                        self.range_labels_visible)

    scaling_factor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Get/set the scaling factor used for the axis, this defaults to
        1.0 (no scaling), and is used to coordinate scaling with the
        plots, charts, etc.
        """
    )

    def _scaling_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalingFactor,
                        self.scaling_factor)

    shift = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get/set the scaling factor used for the axis, this defaults to
        1.0 (no scaling), and is used to coordinate scaling with the
        plots, charts, etc.
        """
    )

    def _shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShift,
                        self.shift)

    tick_label_algorithm = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/set the tick label algorithm that is used to calculate the
        min, max and tick spacing. There are currently two algoriths,
        Axis::TICK_SIMPLE is the default and uses a simple algorithm.
        The second option is Axis::TICK_WILKINSON which uses an
        extended Wilkinson algorithm to find the optimal range, spacing
        and font parameters.
        """
    )

    def _tick_label_algorithm_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTickLabelAlgorithm,
                        self.tick_label_algorithm)

    ticks_visible = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Get/set whether the tick marks should be visible.
        """
    )

    def _ticks_visible_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTicksVisible,
                        self.ticks_visible)

    title = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Get/set the title text of the axis.
        """
    )

    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    unscaled_maximum = traits.Float(6.66, enter_set=True, auto_set=False, help=\
        """
        Set the logical maximum value of the axis, in plot coordinates.
        """
    )

    def _unscaled_maximum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUnscaledMaximum,
                        self.unscaled_maximum)

    unscaled_maximum_limit = traits.Float(1.7976931348623157e+308, enter_set=True, auto_set=False, help=\
        """
        Set the logical highest possible value for Maximum, in plot
        coordinates.
        """
    )

    def _unscaled_maximum_limit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUnscaledMaximumLimit,
                        self.unscaled_maximum_limit)

    unscaled_minimum = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the logical, unscaled minimum value of the axis, in plot
        coordinates. Use this instead of set_minimum() if you wish to
        provide the actual minimum instead of log10(the minimum) as part
        of the axis scale.
        """
    )

    def _unscaled_minimum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUnscaledMinimum,
                        self.unscaled_minimum)

    unscaled_minimum_limit = traits.Float(-1.7976931348623157e+308, enter_set=True, auto_set=False, help=\
        """
        Set the logical lowest possible value for Minimum, in plot
        coordinates.
        """
    )

    def _unscaled_minimum_limit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUnscaledMinimumLimit,
                        self.unscaled_minimum_limit)

    def get_unscaled_range(self, *args):
        """
        V.get_unscaled_range([float, ...])
        C++: virtual void GetUnscaledRange(double *range)
        Get the logical range of the axis, in plot coordinates.
        
        * The unscaled range will always be in the same coordinate system
        of
        * the data being plotted, regardless of whether log_scale is true
          or false.
        * Calling get_range() when log_scale is true will return the
          log10({min, max}).
        """
        ret = self._wrap_call(self._vtk_obj.GetUnscaledRange, *args)
        return ret

    def set_unscaled_range(self, *args):
        """
        V.set_unscaled_range(float, float)
        C++: virtual void SetUnscaledRange(double minimum, double maximum)
        V.set_unscaled_range([float, float])
        C++: virtual void SetUnscaledRange(double range[2])
        Set the logical range of the axis, in plot coordinates.
        
        * The unscaled range will always be in the same coordinate system
        of
        * the data being plotted, regardless of whether log_scale is true
          or false.
        * When calling set_range() and log_scale is true, the range must be
        specified
        * in logarithmic coordinates.
        * Using set_unscaled_range(), you may ignore the value of log_scale.
        """
        ret = self._wrap_call(self._vtk_obj.SetUnscaledRange, *args)
        return ret

    def get_bounding_rect(self, *args):
        """
        V.get_bounding_rect(Context2D) -> Rectf
        C++: Rectf GetBoundingRect(Context2D *painter)
        Request the space the axes require to be drawn. This is returned
        as a Rectf, with the corner being the offset from Point1, and
        the width/ height being the total width/height required by the
        axis. In order to ensure the numbers are correct, Update() should
        be called on the axis.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetBoundingRect, *my_args)
        return wrap_vtk(ret)

    def _get_grid_pen(self):
        return wrap_vtk(self._vtk_obj.GetGridPen())
    grid_pen = traits.Property(_get_grid_pen, help=\
        """
        Get a pointer to the Pen object that controls the way this
        axis is drawn.
        """
    )

    def _get_label_properties(self):
        return wrap_vtk(self._vtk_obj.GetLabelProperties())
    label_properties = traits.Property(_get_label_properties, help=\
        """
        Get the TextProperty that governs how the axis lables are
        displayed. Note that the alignment properties are not used.
        """
    )

    def _get_log_scale_active(self):
        return self._vtk_obj.GetLogScaleActive()
    log_scale_active = traits.Property(_get_log_scale_active, help=\
        """
        Get whether the axis is using a log scale. This will always be
        false when log_scale is false. It is only true when log_scale is
        true andthe unscaled_range does not cross or include the origin
        (zero).
        
        * The limits ( minimum_limit, maximum_limit, and their
        * unscaled counterparts) do not prevent log_scale_active from
          becoming
        * true; they are adjusted if they cross or include the origin
        * and the original limits are preserved for when log_scale_active
        * becomes false again.
        """
    )

    def _get_pen(self):
        return wrap_vtk(self._vtk_obj.GetPen())
    pen = traits.Property(_get_pen, help=\
        """
        Get a pointer to the Pen object that controls the way this
        axis is drawn.
        """
    )

    def _get_position1(self):
        return wrap_vtk(self._vtk_obj.GetPosition1())
    position1 = traits.Property(_get_position1, help=\
        """
        Get point 1 of the axis (in pixels), this is usually the origin.
        """
    )

    def _get_position2(self):
        return wrap_vtk(self._vtk_obj.GetPosition2())
    position2 = traits.Property(_get_position2, help=\
        """
        Get point 2 of the axis (in pixels), this is usually the
        terminus.
        """
    )

    def _get_tick_labels(self):
        return wrap_vtk(self._vtk_obj.GetTickLabels())
    tick_labels = traits.Property(_get_tick_labels, help=\
        """
        A string array containing the tick labels for the axis.
        """
    )

    def _get_tick_positions(self):
        return wrap_vtk(self._vtk_obj.GetTickPositions())
    tick_positions = traits.Property(_get_tick_positions, help=\
        """
        An array with the positions of the tick marks along the axis
        line. The positions are specified in the plot coordinates of the
        axis.
        """
    )

    def _get_tick_scene_positions(self):
        return wrap_vtk(self._vtk_obj.GetTickScenePositions())
    tick_scene_positions = traits.Property(_get_tick_scene_positions, help=\
        """
        An array with the positions of the tick marks along the axis
        line. The positions are specified in scene coordinates.
        """
    )

    def _get_title_properties(self):
        return wrap_vtk(self._vtk_obj.GetTitleProperties())
    title_properties = traits.Property(_get_title_properties, help=\
        """
        Get the TextProperty that governs how the axis title is
        displayed.
        """
    )

    def auto_scale(self):
        """
        V.auto_scale()
        C++: virtual void AutoScale()
        Use this function to autoscale the axes after setting the minimum
        and maximum values. This will cause the axes to select the nicest
        numbers that enclose the minimum and maximum values, and to
        select an appropriate number of tick marks.
        """
        ret = self._vtk_obj.AutoScale()
        return ret
        

    def generate_simple_label(self, *args):
        """
        V.generate_simple_label(float) -> string
        C++: StdString GenerateSimpleLabel(double val)
        Generate a single label using the current settings when
        tick_label_algorithm is TICK_SIMPLE.
        """
        ret = self._wrap_call(self._vtk_obj.GenerateSimpleLabel, *args)
        return ret

    def nice_min_max(self, *args):
        """
        V.nice_min_max(float, float, float, float) -> float
        C++: static double NiceMinMax(double &min, double &max,
            float pixelRange, float tickPixelSpacing)
        Static function to calculate "nice" minimum, maximum, and tick
        spacing values.
        """
        ret = self._wrap_call(self._vtk_obj.NiceMinMax, *args)
        return ret

    def nice_number(self, *args):
        """
        V.nice_number(float, bool) -> float
        C++: static double NiceNumber(double number, bool roundUp)
        Return a "nice number", often defined as 1, 2 or 5. If round_up is
        true then the nice number will be rounded up, false it is rounded
        down. The supplied number should be between 0.0 and 9.9.
        """
        ret = self._wrap_call(self._vtk_obj.NiceNumber, *args)
        return ret

    def recalculate_tick_spacing(self):
        """
        V.recalculate_tick_spacing()
        C++: virtual void RecalculateTickSpacing()
        Recalculate the spacing of the tick marks - typically useful to
        do after scaling the axis.
        """
        ret = self._vtk_obj.RecalculateTickSpacing()
        return ret
        

    def set_custom_tick_positions(self, *args):
        """
        V.set_custom_tick_positions(DoubleArray, StringArray) -> bool
        C++: virtual bool SetCustomTickPositions(
            DoubleArray *positions, StringArray *labels=0)
        Set the tick positions, and optionally custom tick labels. If the
        labels and positions are null then automatic tick labels will be
        assigned. If only positions are supplied then appropriate labels
        will be generated according to the axis settings. If positions
        and labels are supplied they must be of the same length. Returns
        true on success, false on failure.
        """
        my_args = deref_array(args, [('vtkDoubleArray', 'vtkStringArray')])
        ret = self._wrap_call(self._vtk_obj.SetCustomTickPositions, *my_args)
        return ret

    _updateable_traits_ = \
    (('log_scale', 'GetLogScale'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('axis_visible', 'GetAxisVisible'), ('behavior', 'GetBehavior'),
    ('grid_visible', 'GetGridVisible'), ('label_format',
    'GetLabelFormat'), ('label_offset', 'GetLabelOffset'),
    ('labels_visible', 'GetLabelsVisible'), ('margins', 'GetMargins'),
    ('maximum', 'GetMaximum'), ('maximum_limit', 'GetMaximumLimit'),
    ('minimum', 'GetMinimum'), ('minimum_limit', 'GetMinimumLimit'),
    ('notation', 'GetNotation'), ('number_of_ticks', 'GetNumberOfTicks'),
    ('point1', 'GetPoint1'), ('point2', 'GetPoint2'), ('position',
    'GetPosition'), ('precision', 'GetPrecision'), ('range_label_format',
    'GetRangeLabelFormat'), ('range_labels_visible',
    'GetRangeLabelsVisible'), ('scaling_factor', 'GetScalingFactor'),
    ('shift', 'GetShift'), ('tick_label_algorithm',
    'GetTickLabelAlgorithm'), ('ticks_visible', 'GetTicksVisible'),
    ('title', 'GetTitle'), ('unscaled_maximum', 'GetUnscaledMaximum'),
    ('unscaled_maximum_limit', 'GetUnscaledMaximumLimit'),
    ('unscaled_minimum', 'GetUnscaledMinimum'), ('unscaled_minimum_limit',
    'GetUnscaledMinimumLimit'), ('opacity', 'GetOpacity'), ('interactive',
    'GetInteractive'), ('visible', 'GetVisible'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'log_scale', 'axis_visible',
    'behavior', 'grid_visible', 'interactive', 'label_format',
    'label_offset', 'labels_visible', 'margins', 'maximum',
    'maximum_limit', 'minimum', 'minimum_limit', 'notation',
    'number_of_ticks', 'opacity', 'point1', 'point2', 'position',
    'precision', 'range_label_format', 'range_labels_visible',
    'scaling_factor', 'shift', 'tick_label_algorithm', 'ticks_visible',
    'title', 'unscaled_maximum', 'unscaled_maximum_limit',
    'unscaled_minimum', 'unscaled_minimum_limit', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Axis, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Axis properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['log_scale'], [], ['axis_visible', 'behavior', 'grid_visible',
            'interactive', 'label_format', 'label_offset', 'labels_visible',
            'margins', 'maximum', 'maximum_limit', 'minimum', 'minimum_limit',
            'notation', 'number_of_ticks', 'opacity', 'point1', 'point2',
            'position', 'precision', 'range_label_format', 'range_labels_visible',
            'scaling_factor', 'shift', 'tick_label_algorithm', 'ticks_visible',
            'title', 'unscaled_maximum', 'unscaled_maximum_limit',
            'unscaled_minimum', 'unscaled_minimum_limit', 'visible']),
            title='Edit Axis properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Axis properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


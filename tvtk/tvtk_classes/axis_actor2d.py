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

from tvtk.tvtk_classes.actor2d import Actor2D


class AxisActor2D(Actor2D):
    """
    AxisActor2D - Create an axis with tick marks and labels
    
    Superclass: Actor2D
    
    AxisActor2D creates an axis with tick marks, labels, and/or a
    title, depending on the particular instance variable settings.
    AxisActor2D is a 2d actor; that is, it is drawn on the overlay
    plane and is not occluded by 3d geometry. To use this class, you
    typically specify two points defining the start and end points of the
    line (x-y definition using Coordinate class), the number of
    labels, and the data range (min,max). You can also control what parts
    of the axis are visible including the line, the tick marks, the
    labels, and the title.  You can also specify the label format (a
    printf style format).
    
    This class decides what font size to use and how to locate the
    labels. It also decides how to create reasonable tick marks and
    labels. The number of labels and the range of values may not match
    the number specified, but should be close.
    
    Labels are drawn on the "right" side of the axis. The "right" side is
    the side of the axis on the right as you move from Position to
    Position2. The way the labels and title line up with the axis and
    tick marks depends on whether the line is considered horizontal or
    vertical.
    
    The Actor2D instance variables Position and Position2 are
    instances of Coordinate. Note that the Position2 is an absolute
    position in that class (it was by default relative to Position in
    Actor2D).
    
    What this means is that you can specify the axis in a variety of
    coordinate systems. Also, the axis does not have to be either
    horizontal or vertical. The tick marks are created so that they are
    perpendicular to the axis.
    
    Set the text property/attributes of the title and the labels through
    the TextProperty objects associated to this actor.
    
    @sa
    CubeAxesActor2D can be used to create axes in world coordinate
    space.
    
    @sa
    Actor2D TextMapper PolyDataMapper2D ScalarBarActor
    Coordinate TextProperty
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAxisActor2D, obj, update, **traits)
    
    adjust_labels = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flag that controls whether the labels and ticks are
        adjusted for "nice" numerical values to make it easier to read
        the labels. The adjustment is based in the Range instance
        variable. Call get_adjusted_range and get_adjusted_number_of_labels to
        get the adjusted range and number of labels. Note that if
        ruler_mode is on, then the number of labels is a function of the
        range and ruler distance.
        """
    )

    def _adjust_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAdjustLabels,
                        self.adjust_labels_)

    axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get visibility of the axis line.
        """
    )

    def _axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisVisibility,
                        self.axis_visibility_)

    label_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get visibility of the axis labels.
        """
    )

    def _label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelVisibility,
                        self.label_visibility_)

    ruler_mode = tvtk_base.false_bool_trait(help=\
        """
        Specify whether this axis should act like a measuring tape (or
        ruler) with specified major tick spacing. If enabled, the
        distance between major ticks is controlled by the ruler_distance
        ivar.
        """
    )

    def _ruler_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRulerMode,
                        self.ruler_mode_)

    size_font_relative_to_axis = tvtk_base.false_bool_trait(help=\
        """
        Specify whether to size the fonts relative to the viewport or
        relative to length of the axis. By default, fonts are resized
        relative to the viewport.
        """
    )

    def _size_font_relative_to_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSizeFontRelativeToAxis,
                        self.size_font_relative_to_axis_)

    tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get visibility of the axis tick marks.
        """
    )

    def _tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTickVisibility,
                        self.tick_visibility_)

    title_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get visibility of the axis title.
        """
    )

    def _title_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitleVisibility,
                        self.title_visibility_)

    font_factor = traits.Trait(1.0, traits.Range(0.1, 2.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the factor that controls the overall size of the fonts
        used to label and title the axes. This ivar used in conjunction
        with the label_factor can be used to control font sizes.
        """
    )

    def _font_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFontFactor,
                        self.font_factor)

    label_factor = traits.Trait(0.75, traits.Range(0.1, 2.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the factor that controls the relative size of the axis
        labels to the axis title.
        """
    )

    def _label_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFactor,
                        self.label_factor)

    label_format = traits.String('%-#6.3g', enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels on the scalar
        bar.
        """
    )

    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    def _get_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetLabelTextProperty())
    def _set_label_text_property(self, arg):
        old_val = self._get_label_text_property()
        self._wrap_call(self._vtk_obj.SetLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('label_text_property', old_val, arg)
    label_text_property = traits.Property(_get_label_text_property, _set_label_text_property, help=\
        """
        Set/Get the labels text property.
        """
    )

    minor_tick_length = traits.Trait(3, traits.Range(0, 100, enter_set=True, auto_set=False), help=\
        """
        Set/Get the length of the minor tick marks (expressed in pixels
        or display coordinates).
        """
    )

    def _minor_tick_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinorTickLength,
                        self.minor_tick_length)

    number_of_labels = traits.Trait(5, traits.Range(2, 25, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of annotation labels to show. This also
        controls the number of major ticks shown. Note that this ivar
        only holds meaning if the ruler_mode is off.
        """
    )

    def _number_of_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfLabels,
                        self.number_of_labels)

    number_of_minor_ticks = traits.Trait(0, traits.Range(0, 20, enter_set=True, auto_set=False), help=\
        """
        Number of minor ticks to be displayed between each tick. Default
        is 0.
        """
    )

    def _number_of_minor_ticks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfMinorTicks,
                        self.number_of_minor_ticks)

    point1 = traits.Trait((traits.Undefined, traits.Undefined), traits.Array(shape=(2,), dtype=float, value=(0.0, 0.0), cols=2), enter_set=True, auto_set=False, help=\
        """
        Specify the position of the first point defining the axis. Note:
        backward compatibility only, use Actor2D's Position instead.
        """
    )

    def _point1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1,
                        self.point1)

    point2 = traits.Trait((traits.Undefined, traits.Undefined), traits.Array(shape=(2,), dtype=float, value=(0.0, 0.0), cols=2), enter_set=True, auto_set=False, help=\
        """
        Specify the position of the second point defining the axis. Note
        that the order from Point1 to Point2 controls which side the tick
        marks are drawn on (ticks are drawn on the right, if visible).
        Note: backward compatibility only, use Actor2D's Position2
        instead.
        """
    )

    def _point2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2,
                        self.point2)

    range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 1.0), cols=2, help=\
        """
        
        """
    )

    def _range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRange,
                        self.range)

    ruler_distance = traits.Trait(1.0, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Specify the ruler_distance which indicates the spacing of the
        major ticks. This ivar only has effect when the ruler_mode is on.
        """
    )

    def _ruler_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRulerDistance,
                        self.ruler_distance)

    tick_length = traits.Trait(5, traits.Range(0, 100, enter_set=True, auto_set=False), help=\
        """
        Set/Get the length of the tick marks (expressed in pixels or
        display coordinates).
        """
    )

    def _tick_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTickLength,
                        self.tick_length)

    tick_offset = traits.Trait(2, traits.Range(0, 100, enter_set=True, auto_set=False), help=\
        """
        Set/Get the offset of the labels (expressed in pixels or display
        coordinates). The offset is the distance of labels from tick
        marks or other objects.
        """
    )

    def _tick_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTickOffset,
                        self.tick_offset)

    title = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the title of the scalar bar actor,
        """
    )

    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    title_position = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get position of the axis title. 0 is at the start of the axis
        whereas 1 is at the end.
        """
    )

    def _title_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitlePosition,
                        self.title_position)

    def _get_title_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTitleTextProperty())
    def _set_title_text_property(self, arg):
        old_val = self._get_title_text_property()
        self._wrap_call(self._vtk_obj.SetTitleTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('title_text_property', old_val, arg)
    title_text_property = traits.Property(_get_title_text_property, _set_title_text_property, help=\
        """
        Set/Get the title text property.
        """
    )

    def _get_adjusted_number_of_labels(self):
        return self._vtk_obj.GetAdjustedNumberOfLabels()
    adjusted_number_of_labels = traits.Property(_get_adjusted_number_of_labels, help=\
        """
        Set/Get the flag that controls whether the labels and ticks are
        adjusted for "nice" numerical values to make it easier to read
        the labels. The adjustment is based in the Range instance
        variable. Call get_adjusted_range and get_adjusted_number_of_labels to
        get the adjusted range and number of labels. Note that if
        ruler_mode is on, then the number of labels is a function of the
        range and ruler distance.
        """
    )

    def _get_adjusted_range(self):
        return self._vtk_obj.GetAdjustedRange()
    adjusted_range = traits.Property(_get_adjusted_range, help=\
        """
        Set/Get the flag that controls whether the labels and ticks are
        adjusted for "nice" numerical values to make it easier to read
        the labels. The adjustment is based in the Range instance
        variable. Call get_adjusted_range and get_adjusted_number_of_labels to
        get the adjusted range and number of labels. Note that if
        ruler_mode is on, then the number of labels is a function of the
        range and ruler distance.
        """
    )

    def _get_point1_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPoint1Coordinate())
    point1_coordinate = traits.Property(_get_point1_coordinate, help=\
        """
        Specify the position of the first point defining the axis. Note:
        backward compatibility only, use Actor2D's Position instead.
        """
    )

    def _get_point2_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPoint2Coordinate())
    point2_coordinate = traits.Property(_get_point2_coordinate, help=\
        """
        Specify the position of the second point defining the axis. Note
        that the order from Point1 to Point2 controls which side the tick
        marks are drawn on (ticks are drawn on the right, if visible).
        Note: backward compatibility only, use Actor2D's Position2
        instead.
        """
    )

    def compute_range(self, *args):
        """
        V.compute_range([float, float], [float, float], int, int, float)
        C++: static void ComputeRange(double inRange[2],
            double outRange[2], int inNumTicks, int &outNumTicks,
            double &interval)
        This method computes the range of the axis given an input range.
        It also computes the number of tick marks given a suggested
        number. (The number of tick marks includes end ticks as well.)
        The number of tick marks computed (in conjunction with the output
        range) will yield "nice" tick values. For example, if the input
        range is (0.25,96.7) and the number of ticks requested is 10, the
        output range will be (0,100) with the number of computed ticks to
        11 to yield tick values of (0,10,20,...,100).
        """
        ret = self._wrap_call(self._vtk_obj.ComputeRange, *args)
        return ret

    _updateable_traits_ = \
    (('adjust_labels', 'GetAdjustLabels'), ('axis_visibility',
    'GetAxisVisibility'), ('label_visibility', 'GetLabelVisibility'),
    ('ruler_mode', 'GetRulerMode'), ('size_font_relative_to_axis',
    'GetSizeFontRelativeToAxis'), ('tick_visibility',
    'GetTickVisibility'), ('title_visibility', 'GetTitleVisibility'),
    ('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('font_factor', 'GetFontFactor'),
    ('label_factor', 'GetLabelFactor'), ('label_format',
    'GetLabelFormat'), ('minor_tick_length', 'GetMinorTickLength'),
    ('number_of_labels', 'GetNumberOfLabels'), ('number_of_minor_ticks',
    'GetNumberOfMinorTicks'), ('range', 'GetRange'), ('ruler_distance',
    'GetRulerDistance'), ('tick_length', 'GetTickLength'), ('tick_offset',
    'GetTickOffset'), ('title', 'GetTitle'), ('title_position',
    'GetTitlePosition'), ('height', 'GetHeight'), ('layer_number',
    'GetLayerNumber'), ('position', 'GetPosition'), ('position2',
    'GetPosition2'), ('width', 'GetWidth'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['adjust_labels', 'axis_visibility', 'debug', 'dragable',
    'global_warning_display', 'label_visibility', 'pickable',
    'ruler_mode', 'size_font_relative_to_axis', 'tick_visibility',
    'title_visibility', 'use_bounds', 'visibility',
    'estimated_render_time', 'font_factor', 'height', 'label_factor',
    'label_format', 'layer_number', 'minor_tick_length',
    'number_of_labels', 'number_of_minor_ticks', 'position', 'position2',
    'range', 'render_time_multiplier', 'ruler_distance', 'tick_length',
    'tick_offset', 'title', 'title_position', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AxisActor2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AxisActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['adjust_labels', 'axis_visibility', 'label_visibility',
            'ruler_mode', 'size_font_relative_to_axis', 'tick_visibility',
            'title_visibility', 'use_bounds', 'visibility'], [],
            ['estimated_render_time', 'font_factor', 'height', 'label_factor',
            'label_format', 'layer_number', 'minor_tick_length',
            'number_of_labels', 'number_of_minor_ticks', 'position', 'position2',
            'range', 'render_time_multiplier', 'ruler_distance', 'tick_length',
            'tick_offset', 'title', 'title_position', 'width']),
            title='Edit AxisActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AxisActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


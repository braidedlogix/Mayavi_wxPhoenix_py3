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

from tvtk.tvtk_classes.actor import Actor


class AxisActor(Actor):
    """
    AxisActor - Create an axis with tick marks and labels
    
    Superclass: Actor
    
    AxisActor creates an axis with tick marks, labels, and/or a title,
    depending on the particular instance variable settings. It is assumed
    that the axes is part of a bounding box and is orthoganal to one of
    the coordinate axes.  To use this class, you typically specify two
    points defining the start and end points of the line (xyz definition
    using Coordinate class), the axis type (X, Y or Z), the axis
    location in relation to the bounding box, the bounding box, the
    number of labels, and the data range (min,max). You can also control
    what parts of the axis are visible including the line, the tick
    marks, the labels, and the title. It is also possible to control
    gridlines, and specifiy on which 'side' the tickmarks are drawn
    (again with respect to the underlying assumed bounding box). You can
    also specify the label format (a printf style format).
    
    This class decides how to locate the labels, and how to create
    reasonable tick marks and labels.
    
    Labels follow the camera so as to be legible from any viewpoint.
    
    The instance variables Point1 and Point2 are instances of
    Coordinate. All calculations and references are in World
    Coordinates.
    
    @par Thanks: This class was written by: Hank Childs, Kathleen
    Bonnell, Amy Squillacote, Brad Whitlock, Eric Brugger, Claire
    Guilbaud, Nicolas Dolegieviez, Will Schroeder, Karthik Krishnan,
    Aashish Chaudhary, Philippe Pebay, David Gobbi, David Partyka,
    Utkarsh Ayachit David Cole, Francois Bertel, and Mark Olesen Part of
    this work was supported by CEA/DIF - Commissariat a l'Energie
    Atomique, Centre DAM Ile-De-France, BP12, F-91297 Arpajon, France.
    
    @sa
    Actor VectorText PolyDataMapper AxisActor2D Coordinate
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAxisActor, obj, update, **traits)
    
    axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get visibility of the axis line.
        """
    )

    def _axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisVisibility,
                        self.axis_visibility_)

    calculate_label_offset = tvtk_base.false_bool_trait(help=\
        """
        Set/Get flag whether to calculate label offset. Default is true.
        """
    )

    def _calculate_label_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCalculateLabelOffset,
                        self.calculate_label_offset_)

    calculate_title_offset = tvtk_base.false_bool_trait(help=\
        """
        Set/Get flag whether to calculate title offset. Default is true.
        """
    )

    def _calculate_title_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCalculateTitleOffset,
                        self.calculate_title_offset_)

    draw_gridlines = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether gridlines should be drawn.
        """
    )

    def _draw_gridlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawGridlines,
                        self.draw_gridlines_)

    draw_gridlines_only = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether ONLY the gridlines should be drawn. This will
        only draw grid_lines and will skip any other part of the rendering
        such as Axis/Tick/Title/...
        """
    )

    def _draw_gridlines_only_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawGridlinesOnly,
                        self.draw_gridlines_only_)

    draw_gridpolys = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether gridpolys should be drawn.
        """
    )

    def _draw_gridpolys_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawGridpolys,
                        self.draw_gridpolys_)

    draw_inner_gridlines = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether inner gridlines should be drawn.
        """
    )

    def _draw_inner_gridlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawInnerGridlines,
                        self.draw_inner_gridlines_)

    exponent_visibility = tvtk_base.false_bool_trait(help=\
        """
        Set/Get visibility of the axis detached exponent.
        """
    )

    def _exponent_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExponentVisibility,
                        self.exponent_visibility_)

    label_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get visibility of the axis labels.
        """
    )

    def _label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelVisibility,
                        self.label_visibility_)

    log = tvtk_base.false_bool_trait(help=\
        """
        Set/Get The type of scale, enable logarithmic scale or linear by
        default
        """
    )

    def _log_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLog,
                        self.log_)

    minor_ticks_visible = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the flag that controls whether the minor ticks are
        visible.
        """
    )

    def _minor_ticks_visible_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinorTicksVisible,
                        self.minor_ticks_visible_)

    tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        Set/Get visibility of the axis major tick marks.
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

    axis_position = traits.Trait('min_min',
    tvtk_base.TraitRevPrefixMap({'min_min': 0, 'max_max': 2, 'max_min': 3, 'min_max': 1}), help=\
        """
        Set/Get the position of this axis (in relation to an an assumed
        bounding box).  For an x-type axis, MINMIN corresponds to the
        x-edge in the bounding box where Y values are minimum and Z
        values are minimum. For a y-type axis, MAXMIN corresponds to the
        y-edge where X values are maximum and Z values are minimum.
        """
    )

    def _axis_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisPosition,
                        self.axis_position_)

    axis_type = traits.Trait('x',
    tvtk_base.TraitRevPrefixMap({'x': 0, 'y': 1, 'z': 2}), help=\
        """
        Set/Get the type of this axis.
        """
    )

    def _axis_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisType,
                        self.axis_type_)

    tick_location = traits.Trait('inside',
    tvtk_base.TraitRevPrefixMap({'inside': 0, 'both': 2, 'outside': 1}), help=\
        """
        Set/Get the location of the ticks. Inside: tick end toward
        positive direction of perpendicular axes. Outside: tick end
        toward negative direction of perpendicular axes.
        """
    )

    def _tick_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTickLocation,
                        self.tick_location_)

    axis_base_for_x = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _axis_base_for_x_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisBaseForX,
                        self.axis_base_for_x)

    axis_base_for_y = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 1.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _axis_base_for_y_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisBaseForY,
                        self.axis_base_for_y)

    axis_base_for_z = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _axis_base_for_z_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisBaseForZ,
                        self.axis_base_for_z)

    def _get_axis_lines_property(self):
        return wrap_vtk(self._vtk_obj.GetAxisLinesProperty())
    def _set_axis_lines_property(self, arg):
        old_val = self._get_axis_lines_property()
        self._wrap_call(self._vtk_obj.SetAxisLinesProperty,
                        deref_vtk(arg))
        self.trait_property_changed('axis_lines_property', old_val, arg)
    axis_lines_property = traits.Property(_get_axis_lines_property, _set_axis_lines_property, help=\
        """
        Get/Set axis actor property (axis and its ticks) (kept for
        compatibility)
        """
    )

    def _get_axis_main_line_property(self):
        return wrap_vtk(self._vtk_obj.GetAxisMainLineProperty())
    def _set_axis_main_line_property(self, arg):
        old_val = self._get_axis_main_line_property()
        self._wrap_call(self._vtk_obj.SetAxisMainLineProperty,
                        deref_vtk(arg))
        self.trait_property_changed('axis_main_line_property', old_val, arg)
    axis_main_line_property = traits.Property(_get_axis_main_line_property, _set_axis_main_line_property, help=\
        """
        Get/Set main line axis actor property
        """
    )

    def _get_axis_major_ticks_property(self):
        return wrap_vtk(self._vtk_obj.GetAxisMajorTicksProperty())
    def _set_axis_major_ticks_property(self, arg):
        old_val = self._get_axis_major_ticks_property()
        self._wrap_call(self._vtk_obj.SetAxisMajorTicksProperty,
                        deref_vtk(arg))
        self.trait_property_changed('axis_major_ticks_property', old_val, arg)
    axis_major_ticks_property = traits.Property(_get_axis_major_ticks_property, _set_axis_major_ticks_property, help=\
        """
        Get/Set axis actor property (axis and its ticks)
        """
    )

    def _get_axis_minor_ticks_property(self):
        return wrap_vtk(self._vtk_obj.GetAxisMinorTicksProperty())
    def _set_axis_minor_ticks_property(self, arg):
        old_val = self._get_axis_minor_ticks_property()
        self._wrap_call(self._vtk_obj.SetAxisMinorTicksProperty,
                        deref_vtk(arg))
        self.trait_property_changed('axis_minor_ticks_property', old_val, arg)
    axis_minor_ticks_property = traits.Property(_get_axis_minor_ticks_property, _set_axis_minor_ticks_property, help=\
        """
        Get/Set axis actor property (axis and its ticks)
        """
    )

    axis_on_origin = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Notify the axes that is not part of a cube anymore
        """
    )

    def _axis_on_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisOnOrigin,
                        self.axis_on_origin)

    bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), cols=3, help=\
        """
        Set or get the bounds for this Actor as
        (Xmin,Xmax,Ymin,Ymax,Zmin,Zmax).
        """
    )

    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    def _get_camera(self):
        return wrap_vtk(self._vtk_obj.GetCamera())
    def _set_camera(self, arg):
        old_val = self._get_camera()
        self._wrap_call(self._vtk_obj.SetCamera,
                        deref_vtk(arg))
        self.trait_property_changed('camera', old_val, arg)
    camera = traits.Property(_get_camera, _set_camera, help=\
        """
        Set/Get the camera for this axis.  The camera is used by the
        labels to 'follow' the camera and be legible from any viewpoint.
        """
    )

    def get_delta_major(self, *args):
        """
        V.get_delta_major(int) -> float
        C++: double GetDeltaMajor(int axis)"""
        ret = self._wrap_call(self._vtk_obj.GetDeltaMajor, *args)
        return ret

    def set_delta_major(self, *args):
        """
        V.set_delta_major(int, float)
        C++: void SetDeltaMajor(int axis, double value)"""
        ret = self._wrap_call(self._vtk_obj.SetDeltaMajor, *args)
        return ret

    delta_minor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _delta_minor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeltaMinor,
                        self.delta_minor)

    delta_range_major = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the starting position for minor and major tick points on
        the range and the delta values that determine their spacing. The
        range and the position need not be identical. ie the displayed
        values need not match the actual positions in 3d space.
        """
    )

    def _delta_range_major_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeltaRangeMajor,
                        self.delta_range_major)

    delta_range_minor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the starting position for minor and major tick points on
        the range and the delta values that determine their spacing. The
        range and the position need not be identical. ie the displayed
        values need not match the actual positions in 3d space.
        """
    )

    def _delta_range_minor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeltaRangeMinor,
                        self.delta_range_minor)

    draw_gridlines_location = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _draw_gridlines_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawGridlinesLocation,
                        self.draw_gridlines_location)

    exponent = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the common exponent of the labels values
        """
    )

    def _exponent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExponent,
                        self.exponent)

    exponent_location = traits.Trait(3, traits.Range(0, 3, enter_set=True, auto_set=False), help=\
        """
        Get/Set the location of the Detached Exponent related to the
        axis. Possible Location: VTK_ALIGN_TOP, VTK_ALIGN_BOTTOM,
        VTK_ALIGN_POINT1, VTK_ALIGN_POINT2
        """
    )

    def _exponent_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExponentLocation,
                        self.exponent_location)

    exponent_offset = traits.Float(20.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the offsets used to position texts.
        """
    )

    def _exponent_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExponentOffset,
                        self.exponent_offset)

    gridline_x_length = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the length to use when drawing gridlines.
        """
    )

    def _gridline_x_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridlineXLength,
                        self.gridline_x_length)

    gridline_y_length = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the length to use when drawing gridlines.
        """
    )

    def _gridline_y_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridlineYLength,
                        self.gridline_y_length)

    gridline_z_length = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the length to use when drawing gridlines.
        """
    )

    def _gridline_z_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridlineZLength,
                        self.gridline_z_length)

    def _get_gridlines_property(self):
        return wrap_vtk(self._vtk_obj.GetGridlinesProperty())
    def _set_gridlines_property(self, arg):
        old_val = self._get_gridlines_property()
        self._wrap_call(self._vtk_obj.SetGridlinesProperty,
                        deref_vtk(arg))
        self.trait_property_changed('gridlines_property', old_val, arg)
    gridlines_property = traits.Property(_get_gridlines_property, _set_gridlines_property, help=\
        """
        Get/Set gridlines actor property (outer grid lines)
        """
    )

    def _get_gridpolys_property(self):
        return wrap_vtk(self._vtk_obj.GetGridpolysProperty())
    def _set_gridpolys_property(self, arg):
        old_val = self._get_gridpolys_property()
        self._wrap_call(self._vtk_obj.SetGridpolysProperty,
                        deref_vtk(arg))
        self.trait_property_changed('gridpolys_property', old_val, arg)
    gridpolys_property = traits.Property(_get_gridpolys_property, _set_gridpolys_property, help=\
        """
        Get/Set grid_polys actor property (grid quads)
        """
    )

    horizontal_offset_y_title2d = traits.Float(-50.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the 2d mode the horizontal offset for Y title in 2d mode
        """
    )

    def _horizontal_offset_y_title2d_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHorizontalOffsetYTitle2D,
                        self.horizontal_offset_y_title2d)

    def _get_inner_gridlines_property(self):
        return wrap_vtk(self._vtk_obj.GetInnerGridlinesProperty())
    def _set_inner_gridlines_property(self, arg):
        old_val = self._get_inner_gridlines_property()
        self._wrap_call(self._vtk_obj.SetInnerGridlinesProperty,
                        deref_vtk(arg))
        self.trait_property_changed('inner_gridlines_property', old_val, arg)
    inner_gridlines_property = traits.Property(_get_inner_gridlines_property, _set_inner_gridlines_property, help=\
        """
        Get/Set inner gridlines actor property
        """
    )

    label_format = traits.String('%-#6.3g', enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels on the axis.
        """
    )

    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    label_offset = traits.Float(30.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the offsets used to position texts.
        """
    )

    def _label_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelOffset,
                        self.label_offset)

    def _get_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetLabelTextProperty())
    def _set_label_text_property(self, arg):
        old_val = self._get_label_text_property()
        self._wrap_call(self._vtk_obj.SetLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('label_text_property', old_val, arg)
    label_text_property = traits.Property(_get_label_text_property, _set_label_text_property, help=\
        """
        Set/Get the axis labels text property.
        """
    )

    major_range_start = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the starting position for minor and major tick points on
        the range and the delta values that determine their spacing. The
        range and the position need not be identical. ie the displayed
        values need not match the actual positions in 3d space.
        """
    )

    def _major_range_start_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMajorRangeStart,
                        self.major_range_start)

    def get_major_start(self, *args):
        """
        V.get_major_start(int) -> float
        C++: double GetMajorStart(int axis)
        Set/Get the starting position for minor and major tick points,
        and the delta values that determine their spacing.
        """
        ret = self._wrap_call(self._vtk_obj.GetMajorStart, *args)
        return ret

    def set_major_start(self, *args):
        """
        V.set_major_start(int, float)
        C++: void SetMajorStart(int axis, double value)
        Set/Get the starting position for minor and major tick points,
        and the delta values that determine their spacing.
        """
        ret = self._wrap_call(self._vtk_obj.SetMajorStart, *args)
        return ret

    major_tick_size = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the size of the major tick marks
        """
    )

    def _major_tick_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMajorTickSize,
                        self.major_tick_size)

    minor_range_start = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the starting position for minor and major tick points on
        the range and the delta values that determine their spacing. The
        range and the position need not be identical. ie the displayed
        values need not match the actual positions in 3d space.
        """
    )

    def _minor_range_start_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinorRangeStart,
                        self.minor_range_start)

    minor_start = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the starting position for minor and major tick points,
        and the delta values that determine their spacing.
        """
    )

    def _minor_start_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinorStart,
                        self.minor_start)

    minor_tick_size = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the size of the major tick marks
        """
    )

    def _minor_tick_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinorTickSize,
                        self.minor_tick_size)

    point1 = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Specify the position of the first point defining the axis.
        """
    )

    def _point1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1,
                        self.point1)

    point2 = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Specify the position of the second point defining the axis.
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

    save_title_position = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get whether title position must be saved in 2d mode
        """
    )

    def _save_title_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSaveTitlePosition,
                        self.save_title_position)

    screen_size = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the offsets used to position texts.
        """
    )

    def _screen_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScreenSize,
                        self.screen_size)

    title = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the title of the axis actor,
        """
    )

    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    title_align_location = traits.Trait(1, traits.Range(0, 3, enter_set=True, auto_set=False), help=\
        """
        Get/Set the alignement of the title related to the axis. Possible
        Alignment: VTK_ALIGN_TOP, VTK_ALIGN_BOTTOM, VTK_ALIGN_POINT1,
        VTK_ALIGN_POINT2
        """
    )

    def _title_align_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitleAlignLocation,
                        self.title_align_location)

    title_offset = traits.Float(20.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the offsets used to position texts.
        """
    )

    def _title_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitleOffset,
                        self.title_offset)

    def _get_title_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTitleTextProperty())
    def _set_title_text_property(self, arg):
        old_val = self._get_title_text_property()
        self._wrap_call(self._vtk_obj.SetTitleTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('title_text_property', old_val, arg)
    title_text_property = traits.Property(_get_title_text_property, _set_title_text_property, help=\
        """
        Set/Get the axis title text property.
        """
    )

    use2d_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the 2d mode
        """
    )

    def _use2d_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUse2DMode,
                        self.use2d_mode)

    use_text_actor3d = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Render text as polygons (vtk_vector_text) or as sprites
        (vtk_text_actor3d). In 2d mode, the value is ignored and text is
        rendered as TextActor. False(0) by default. See Also:
        get_use2d_mode(), set_use2d_mode
        """
    )

    def _use_text_actor3d_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseTextActor3D,
                        self.use_text_actor3d)

    vertical_offset_x_title2d = traits.Float(-40.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the 2d mode the vertical offset for X title in 2d mode
        """
    )

    def _vertical_offset_x_title2d_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVerticalOffsetXTitle2D,
                        self.vertical_offset_x_title2d)

    def _get_exponent_actor(self):
        return wrap_vtk(self._vtk_obj.GetExponentActor())
    exponent_actor = traits.Property(_get_exponent_actor, help=\
        """
        Get exponent follower actor
        """
    )

    def _get_exponent_prop3d(self):
        return wrap_vtk(self._vtk_obj.GetExponentProp3D())
    exponent_prop3d = traits.Property(_get_exponent_prop3d, help=\
        """
        Get title actor and it is responsible for drawing title text.
        """
    )

    def _get_number_of_labels_built(self):
        return self._vtk_obj.GetNumberOfLabelsBuilt()
    number_of_labels_built = traits.Property(_get_number_of_labels_built, help=\
        """
        Get total number of labels built. Once built this count does not
        change.
        """
    )

    def _get_point1_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPoint1Coordinate())
    point1_coordinate = traits.Property(_get_point1_coordinate, help=\
        """
        Specify the position of the first point defining the axis.
        """
    )

    def _get_point2_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPoint2Coordinate())
    point2_coordinate = traits.Property(_get_point2_coordinate, help=\
        """
        Specify the position of the second point defining the axis.
        """
    )

    def _get_title_actor(self):
        return wrap_vtk(self._vtk_obj.GetTitleActor())
    title_actor = traits.Property(_get_title_actor, help=\
        """
        Get title actor and it is responsible for drawing title text.
        """
    )

    def _get_title_prop3d(self):
        return wrap_vtk(self._vtk_obj.GetTitleProp3D())
    title_prop3d = traits.Property(_get_title_prop3d, help=\
        """
        Get title actor and it is responsible for drawing title text.
        """
    )

    def build_axis(self, *args):
        """
        V.build_axis(Viewport, bool)
        C++: void BuildAxis(Viewport *viewport, bool)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.BuildAxis, *my_args)
        return ret

    def compute_max_label_length(self, *args):
        """
        V.compute_max_label_length((float, float, float)) -> float
        C++: double ComputeMaxLabelLength(const double[3])"""
        ret = self._wrap_call(self._vtk_obj.ComputeMaxLabelLength, *args)
        return ret

    def compute_title_length(self, *args):
        """
        V.compute_title_length((float, float, float)) -> float
        C++: double ComputeTitleLength(const double[3])"""
        ret = self._wrap_call(self._vtk_obj.ComputeTitleLength, *args)
        return ret

    def render_translucent_geometry(self, *args):
        """
        V.render_translucent_geometry(Viewport) -> int
        C++: virtual int RenderTranslucentGeometry(Viewport *viewport)
        Draw the axis.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderTranslucentGeometry, *my_args)
        return ret

    def set_label_scale(self, *args):
        """
        V.set_label_scale(float)
        C++: void SetLabelScale(const double scale)
        V.set_label_scale(int, float)
        C++: void SetLabelScale(int labelIndex, const double scale)"""
        ret = self._wrap_call(self._vtk_obj.SetLabelScale, *args)
        return ret

    def set_labels(self, *args):
        """
        V.set_labels(StringArray)
        C++: void SetLabels(StringArray *labels)"""
        my_args = deref_array(args, [['vtkStringArray']])
        ret = self._wrap_call(self._vtk_obj.SetLabels, *my_args)
        return ret

    def set_title_scale(self, *args):
        """
        V.set_title_scale(float)
        C++: void SetTitleScale(const double scale)"""
        ret = self._wrap_call(self._vtk_obj.SetTitleScale, *args)
        return ret

    _updateable_traits_ = \
    (('axis_visibility', 'GetAxisVisibility'), ('calculate_label_offset',
    'GetCalculateLabelOffset'), ('calculate_title_offset',
    'GetCalculateTitleOffset'), ('draw_gridlines', 'GetDrawGridlines'),
    ('draw_gridlines_only', 'GetDrawGridlinesOnly'), ('draw_gridpolys',
    'GetDrawGridpolys'), ('draw_inner_gridlines',
    'GetDrawInnerGridlines'), ('exponent_visibility',
    'GetExponentVisibility'), ('label_visibility', 'GetLabelVisibility'),
    ('log', 'GetLog'), ('minor_ticks_visible', 'GetMinorTicksVisible'),
    ('tick_visibility', 'GetTickVisibility'), ('title_visibility',
    'GetTitleVisibility'), ('force_opaque', 'GetForceOpaque'),
    ('force_translucent', 'GetForceTranslucent'), ('dragable',
    'GetDragable'), ('pickable', 'GetPickable'), ('use_bounds',
    'GetUseBounds'), ('visibility', 'GetVisibility'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('axis_position', 'GetAxisPosition'), ('axis_type', 'GetAxisType'),
    ('tick_location', 'GetTickLocation'), ('axis_base_for_x',
    'GetAxisBaseForX'), ('axis_base_for_y', 'GetAxisBaseForY'),
    ('axis_base_for_z', 'GetAxisBaseForZ'), ('axis_on_origin',
    'GetAxisOnOrigin'), ('bounds', 'GetBounds'), ('delta_minor',
    'GetDeltaMinor'), ('delta_range_major', 'GetDeltaRangeMajor'),
    ('delta_range_minor', 'GetDeltaRangeMinor'),
    ('draw_gridlines_location', 'GetDrawGridlinesLocation'), ('exponent',
    'GetExponent'), ('exponent_location', 'GetExponentLocation'),
    ('exponent_offset', 'GetExponentOffset'), ('gridline_x_length',
    'GetGridlineXLength'), ('gridline_y_length', 'GetGridlineYLength'),
    ('gridline_z_length', 'GetGridlineZLength'),
    ('horizontal_offset_y_title2d', 'GetHorizontalOffsetYTitle2D'),
    ('label_format', 'GetLabelFormat'), ('label_offset',
    'GetLabelOffset'), ('major_range_start', 'GetMajorRangeStart'),
    ('major_tick_size', 'GetMajorTickSize'), ('minor_range_start',
    'GetMinorRangeStart'), ('minor_start', 'GetMinorStart'),
    ('minor_tick_size', 'GetMinorTickSize'), ('range', 'GetRange'),
    ('save_title_position', 'GetSaveTitlePosition'), ('screen_size',
    'GetScreenSize'), ('title', 'GetTitle'), ('title_align_location',
    'GetTitleAlignLocation'), ('title_offset', 'GetTitleOffset'),
    ('use2d_mode', 'GetUse2DMode'), ('use_text_actor3d',
    'GetUseTextActor3D'), ('vertical_offset_x_title2d',
    'GetVerticalOffsetXTitle2D'), ('orientation', 'GetOrientation'),
    ('origin', 'GetOrigin'), ('position', 'GetPosition'), ('scale',
    'GetScale'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['axis_visibility', 'calculate_label_offset',
    'calculate_title_offset', 'debug', 'dragable', 'draw_gridlines',
    'draw_gridlines_only', 'draw_gridpolys', 'draw_inner_gridlines',
    'exponent_visibility', 'force_opaque', 'force_translucent',
    'global_warning_display', 'label_visibility', 'log',
    'minor_ticks_visible', 'pickable', 'tick_visibility',
    'title_visibility', 'use_bounds', 'visibility', 'axis_position',
    'axis_type', 'tick_location', 'axis_base_for_x', 'axis_base_for_y',
    'axis_base_for_z', 'axis_on_origin', 'bounds', 'delta_minor',
    'delta_range_major', 'delta_range_minor', 'draw_gridlines_location',
    'estimated_render_time', 'exponent', 'exponent_location',
    'exponent_offset', 'gridline_x_length', 'gridline_y_length',
    'gridline_z_length', 'horizontal_offset_y_title2d', 'label_format',
    'label_offset', 'major_range_start', 'major_tick_size',
    'minor_range_start', 'minor_start', 'minor_tick_size', 'orientation',
    'origin', 'position', 'range', 'render_time_multiplier',
    'save_title_position', 'scale', 'screen_size', 'title',
    'title_align_location', 'title_offset', 'use2d_mode',
    'use_text_actor3d', 'vertical_offset_x_title2d'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AxisActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AxisActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['axis_visibility', 'calculate_label_offset',
            'calculate_title_offset', 'draw_gridlines', 'draw_gridlines_only',
            'draw_gridpolys', 'draw_inner_gridlines', 'exponent_visibility',
            'force_opaque', 'force_translucent', 'label_visibility', 'log',
            'minor_ticks_visible', 'tick_visibility', 'title_visibility',
            'use_bounds', 'visibility'], ['axis_position', 'axis_type',
            'tick_location'], ['axis_base_for_x', 'axis_base_for_y',
            'axis_base_for_z', 'axis_on_origin', 'bounds', 'delta_minor',
            'delta_range_major', 'delta_range_minor', 'draw_gridlines_location',
            'estimated_render_time', 'exponent', 'exponent_location',
            'exponent_offset', 'gridline_x_length', 'gridline_y_length',
            'gridline_z_length', 'horizontal_offset_y_title2d', 'label_format',
            'label_offset', 'major_range_start', 'major_tick_size',
            'minor_range_start', 'minor_start', 'minor_tick_size', 'orientation',
            'origin', 'position', 'range', 'render_time_multiplier',
            'save_title_position', 'scale', 'screen_size', 'title',
            'title_align_location', 'title_offset', 'use2d_mode',
            'use_text_actor3d', 'vertical_offset_x_title2d']),
            title='Edit AxisActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AxisActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


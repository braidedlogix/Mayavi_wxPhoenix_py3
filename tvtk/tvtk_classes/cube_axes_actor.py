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


class CubeAxesActor(Actor):
    """
    CubeAxesActor - create a  plot of a bounding box edges - used for
    navigation
    
    Superclass: Actor
    
    CubeAxesActor is a composite actor that draws axes of the bounding
    box of an input dataset. The axes include labels and titles for the
    x-y-z axes. The algorithm selects which axes to draw based on the
    user-defined 'fly' mode.  (STATIC is default). 'STATIC' constructs
    axes from all edges of the bounding box. 'CLOSEST_TRIAD' consists of
    the three axes x-y-z forming a triad that lies closest to the
    specified camera. 'FURTHEST_TRIAD' consists of the three axes x-y-z
    forming a triad that lies furthest from the specified camera.
    'OUTER_EDGES' is constructed from edges that are on the "exterior" of
    the bounding box, exterior as determined from examining outer edges
    of the bounding box in projection (display) space.
    
    To use this object you must define a bounding box and the camera used
    to render the CubeAxesActor. You can optionally turn on/off
    labels, ticks, gridlines, and set tick location, number of labels,
    and text to use for axis-titles.  A 'corner offset' can also be set. 
    This allows the axes to be set partially away from the actual
    bounding box to perhaps prevent overlap of labels between the various
    axes.
    
    The Bounds instance variable (an array of six doubles) is used to
    determine the bounding box.
    
    @par Thanks: This class was written by: Hank Childs, Kathleen
    Bonnell, Amy Squillacote, Brad Whitlock, Will Schroeder, Eric
    Brugger, Daniel Aguilera, Claire Guilbaud, Nicolas Dolegieviez,
    Aashish Chaudhary, Philippe Pebay, David Gobbi, David Partyka,
    Utkarsh Ayachit David Cole, Francois Bertel, and Mark Olesen Part of
    this work was supported by CEA/DIF - Commissariat a l'Energie
    Atomique, Centre DAM Ile-De-France, BP12, F-91297 Arpajon, France.
    
    @sa
    Actor AxisActor CubeAxesActor2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCubeAxesActor, obj, update, **traits)
    
    center_sticky_axes = tvtk_base.true_bool_trait(help=\
        """
        Enable/Disable centering of axes when the Sticky option is on. If
        on, the axes bounds will be centered in the viewport. Otherwise,
        the axes can move about the longer of the horizontal or verical
        directions of the viewport to follow the data. Defaults to on.
        """
    )

    def _center_sticky_axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenterStickyAxes,
                        self.center_sticky_axes_)

    draw_x_gridlines = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _draw_x_gridlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawXGridlines,
                        self.draw_x_gridlines_)

    draw_x_gridpolys = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _draw_x_gridpolys_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawXGridpolys,
                        self.draw_x_gridpolys_)

    draw_x_inner_gridlines = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _draw_x_inner_gridlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawXInnerGridlines,
                        self.draw_x_inner_gridlines_)

    draw_y_gridlines = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _draw_y_gridlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawYGridlines,
                        self.draw_y_gridlines_)

    draw_y_gridpolys = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _draw_y_gridpolys_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawYGridpolys,
                        self.draw_y_gridpolys_)

    draw_y_inner_gridlines = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _draw_y_inner_gridlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawYInnerGridlines,
                        self.draw_y_inner_gridlines_)

    draw_z_gridlines = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _draw_z_gridlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawZGridlines,
                        self.draw_z_gridlines_)

    draw_z_gridpolys = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _draw_z_gridpolys_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawZGridpolys,
                        self.draw_z_gridpolys_)

    draw_z_inner_gridlines = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _draw_z_inner_gridlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawZInnerGridlines,
                        self.draw_z_inner_gridlines_)

    sticky_axes = tvtk_base.false_bool_trait(help=\
        """
        Enable/Disable axis stickiness. When on, the axes will be
        adjusted to always be visible in the viewport unless the original
        bounds of the axes are entirely outside the viewport. Defaults to
        off.
        """
    )

    def _sticky_axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStickyAxes,
                        self.sticky_axes_)

    x_axis_label_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of labels for each axis.
        """
    )

    def _x_axis_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAxisLabelVisibility,
                        self.x_axis_label_visibility_)

    x_axis_minor_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of minor ticks for each axis.
        """
    )

    def _x_axis_minor_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAxisMinorTickVisibility,
                        self.x_axis_minor_tick_visibility_)

    x_axis_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of ticks for each axis.
        """
    )

    def _x_axis_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAxisTickVisibility,
                        self.x_axis_tick_visibility_)

    x_axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of each axis.
        """
    )

    def _x_axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAxisVisibility,
                        self.x_axis_visibility_)

    y_axis_label_visibility = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )

    def _y_axis_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAxisLabelVisibility,
                        self.y_axis_label_visibility_)

    y_axis_minor_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )

    def _y_axis_minor_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAxisMinorTickVisibility,
                        self.y_axis_minor_tick_visibility_)

    y_axis_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )

    def _y_axis_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAxisTickVisibility,
                        self.y_axis_tick_visibility_)

    y_axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of each axis.
        """
    )

    def _y_axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAxisVisibility,
                        self.y_axis_visibility_)

    z_axis_label_visibility = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )

    def _z_axis_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZAxisLabelVisibility,
                        self.z_axis_label_visibility_)

    z_axis_minor_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )

    def _z_axis_minor_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZAxisMinorTickVisibility,
                        self.z_axis_minor_tick_visibility_)

    z_axis_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )

    def _z_axis_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZAxisTickVisibility,
                        self.z_axis_tick_visibility_)

    z_axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of each axis.
        """
    )

    def _z_axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZAxisVisibility,
                        self.z_axis_visibility_)

    fly_mode = traits.Trait('closest_triad',
    tvtk_base.TraitRevPrefixMap({'closest_triad': 1, 'furthest_triad': 2, 'outer_edges': 0, 'static_edges': 4, 'static_triad': 3}), help=\
        """
        Specify a mode to control how the axes are drawn: either static,
        closest triad, furthest triad or outer edges in relation to the
        camera position.
        """
    )

    def _fly_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFlyMode,
                        self.fly_mode_)

    tick_location = traits.Trait('inside',
    tvtk_base.TraitRevPrefixMap({'inside': 0, 'both': 2, 'outside': 1}), help=\
        """
        Set/Get the location of ticks marks.
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

    def get_axis_labels(self, *args):
        """
        V.get_axis_labels(int) -> StringArray
        C++: StringArray *GetAxisLabels(int axis)
        Explicitly specify the axis labels along an axis as an array of
        strings instead of using the values.
        """
        ret = self._wrap_call(self._vtk_obj.GetAxisLabels, *args)
        return wrap_vtk(ret)

    def set_axis_labels(self, *args):
        """
        V.set_axis_labels(int, StringArray)
        C++: void SetAxisLabels(int axis, StringArray *value)
        Explicitly specify the axis labels along an axis as an array of
        strings instead of using the values.
        """
        my_args = deref_array(args, [('int', 'vtkStringArray')])
        ret = self._wrap_call(self._vtk_obj.SetAxisLabels, *my_args)
        return ret

    axis_origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _axis_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisOrigin,
                        self.axis_origin)

    bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), cols=3, help=\
        """
        
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
        Set/Get the camera to perform scaling and translation of the
        CubeAxesActor.
        """
    )

    corner_offset = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Specify an offset value to "pull back" the axes from the corner
        at which they are joined to avoid overlap of axes labels. The
        "_corner_offset" is the fraction of the axis length to pull back.
        """
    )

    def _corner_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCornerOffset,
                        self.corner_offset)

    distance_lod_threshold = traits.Trait(0.8, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set distance LOD threshold [0.0 - 1.0] for titles and labels.
        """
    )

    def _distance_lod_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistanceLODThreshold,
                        self.distance_lod_threshold)

    enable_distance_lod = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Enable and disable the use of distance based LOD for titles and
        labels.
        """
    )

    def _enable_distance_lod_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableDistanceLOD,
                        self.enable_distance_lod)

    enable_view_angle_lod = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Enable and disable the use of view angle based LOD for titles and
        labels.
        """
    )

    def _enable_view_angle_lod_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableViewAngleLOD,
                        self.enable_view_angle_lod)

    grid_line_location = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify the mode in which the cube axes should render its
        grid_lines
        """
    )

    def _grid_line_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridLineLocation,
                        self.grid_line_location)

    inertia = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the inertial factor that controls how often (i.e, how
        many renders) the axes can switch position (jump from one axes to
        another).
        """
    )

    def _inertia_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInertia,
                        self.inertia)

    label_offset = traits.Float(20.0, enter_set=True, auto_set=False, help=\
        """
        Explicitly specify the distance between labels and the axis.
        Default is 20.0.
        """
    )

    def _label_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelOffset,
                        self.label_offset)

    oriented_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _oriented_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientedBounds,
                        self.oriented_bounds)

    rebuild_axes = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Gets/Sets the rebuild_axes flag
        """
    )

    def _rebuild_axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRebuildAxes,
                        self.rebuild_axes)

    screen_size = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Explicitly specify the screen size of title and label text.
        screen_size determines the size of the text in terms of screen
        pixels. Default is 10.0.
        """
    )

    def _screen_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScreenSize,
                        self.screen_size)

    title_offset = traits.Float(20.0, enter_set=True, auto_set=False, help=\
        """
        Explicitly specify the distance between title and labels. Default
        is 20.0.
        """
    )

    def _title_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitleOffset,
                        self.title_offset)

    use2d_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set 2d mode NB: Use TextActor for titles in 2d instead of
        AxisFollower
        """
    )

    def _use2d_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUse2DMode,
                        self.use2d_mode)

    use_axis_origin = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Enable/Disable the usage of the axis_origin
        """
    )

    def _use_axis_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseAxisOrigin,
                        self.use_axis_origin)

    use_oriented_bounds = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Enable/Disable the usage of the oriented_bounds
        """
    )

    def _use_oriented_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseOrientedBounds,
                        self.use_oriented_bounds)

    use_text_actor3d = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Use or not TextActor3D for titles and labels. See Also:
        AxisActor::SetUseTextActor3D(),
        AxisActor::GetUseTextActor3D()
        """
    )

    def _use_text_actor3d_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseTextActor3D,
                        self.use_text_actor3d)

    view_angle_lod_threshold = traits.Trait(0.2, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set view angle LOD threshold [0.0 - 1.0] for titles and labels.
        """
    )

    def _view_angle_lod_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetViewAngleLODThreshold,
                        self.view_angle_lod_threshold)

    def _get_x_axes_gridlines_property(self):
        return wrap_vtk(self._vtk_obj.GetXAxesGridlinesProperty())
    def _set_x_axes_gridlines_property(self, arg):
        old_val = self._get_x_axes_gridlines_property()
        self._wrap_call(self._vtk_obj.SetXAxesGridlinesProperty,
                        deref_vtk(arg))
        self.trait_property_changed('x_axes_gridlines_property', old_val, arg)
    x_axes_gridlines_property = traits.Property(_get_x_axes_gridlines_property, _set_x_axes_gridlines_property, help=\
        """
        Get/Set axes (outer) gridlines actors properties.
        """
    )

    def _get_x_axes_gridpolys_property(self):
        return wrap_vtk(self._vtk_obj.GetXAxesGridpolysProperty())
    def _set_x_axes_gridpolys_property(self, arg):
        old_val = self._get_x_axes_gridpolys_property()
        self._wrap_call(self._vtk_obj.SetXAxesGridpolysProperty,
                        deref_vtk(arg))
        self.trait_property_changed('x_axes_gridpolys_property', old_val, arg)
    x_axes_gridpolys_property = traits.Property(_get_x_axes_gridpolys_property, _set_x_axes_gridpolys_property, help=\
        """
        Get/Set axes grid_polys actors properties.
        """
    )

    def _get_x_axes_inner_gridlines_property(self):
        return wrap_vtk(self._vtk_obj.GetXAxesInnerGridlinesProperty())
    def _set_x_axes_inner_gridlines_property(self, arg):
        old_val = self._get_x_axes_inner_gridlines_property()
        self._wrap_call(self._vtk_obj.SetXAxesInnerGridlinesProperty,
                        deref_vtk(arg))
        self.trait_property_changed('x_axes_inner_gridlines_property', old_val, arg)
    x_axes_inner_gridlines_property = traits.Property(_get_x_axes_inner_gridlines_property, _set_x_axes_inner_gridlines_property, help=\
        """
        Get/Set axes inner gridlines actors properties.
        """
    )

    def _get_x_axes_lines_property(self):
        return wrap_vtk(self._vtk_obj.GetXAxesLinesProperty())
    def _set_x_axes_lines_property(self, arg):
        old_val = self._get_x_axes_lines_property()
        self._wrap_call(self._vtk_obj.SetXAxesLinesProperty,
                        deref_vtk(arg))
        self.trait_property_changed('x_axes_lines_property', old_val, arg)
    x_axes_lines_property = traits.Property(_get_x_axes_lines_property, _set_x_axes_lines_property, help=\
        """
        Get/Set axes actors properties.
        """
    )

    x_axis_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(1e+299, 1e+299), cols=2, help=\
        """
        
        """
    )

    def _x_axis_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAxisRange,
                        self.x_axis_range)

    x_label_format = traits.String('%-#6.3g', enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels on each of the
        x-y-z axes.
        """
    )

    def _x_label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXLabelFormat,
                        self.x_label_format)

    x_title = traits.String('X-Axis', enter_set=True, auto_set=False, help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use
        "X-Axis", "Y-Axis" and "Z-Axis".
        """
    )

    def _x_title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXTitle,
                        self.x_title)

    x_units = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use
        "X-Axis", "Y-Axis" and "Z-Axis".
        """
    )

    def _x_units_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXUnits,
                        self.x_units)

    def _get_y_axes_gridlines_property(self):
        return wrap_vtk(self._vtk_obj.GetYAxesGridlinesProperty())
    def _set_y_axes_gridlines_property(self, arg):
        old_val = self._get_y_axes_gridlines_property()
        self._wrap_call(self._vtk_obj.SetYAxesGridlinesProperty,
                        deref_vtk(arg))
        self.trait_property_changed('y_axes_gridlines_property', old_val, arg)
    y_axes_gridlines_property = traits.Property(_get_y_axes_gridlines_property, _set_y_axes_gridlines_property, help=\
        """
        Get/Set axes (outer) gridlines actors properties.
        """
    )

    def _get_y_axes_gridpolys_property(self):
        return wrap_vtk(self._vtk_obj.GetYAxesGridpolysProperty())
    def _set_y_axes_gridpolys_property(self, arg):
        old_val = self._get_y_axes_gridpolys_property()
        self._wrap_call(self._vtk_obj.SetYAxesGridpolysProperty,
                        deref_vtk(arg))
        self.trait_property_changed('y_axes_gridpolys_property', old_val, arg)
    y_axes_gridpolys_property = traits.Property(_get_y_axes_gridpolys_property, _set_y_axes_gridpolys_property, help=\
        """
        Get/Set axes grid_polys actors properties.
        """
    )

    def _get_y_axes_inner_gridlines_property(self):
        return wrap_vtk(self._vtk_obj.GetYAxesInnerGridlinesProperty())
    def _set_y_axes_inner_gridlines_property(self, arg):
        old_val = self._get_y_axes_inner_gridlines_property()
        self._wrap_call(self._vtk_obj.SetYAxesInnerGridlinesProperty,
                        deref_vtk(arg))
        self.trait_property_changed('y_axes_inner_gridlines_property', old_val, arg)
    y_axes_inner_gridlines_property = traits.Property(_get_y_axes_inner_gridlines_property, _set_y_axes_inner_gridlines_property, help=\
        """
        Get/Set axes inner gridlines actors properties.
        """
    )

    def _get_y_axes_lines_property(self):
        return wrap_vtk(self._vtk_obj.GetYAxesLinesProperty())
    def _set_y_axes_lines_property(self, arg):
        old_val = self._get_y_axes_lines_property()
        self._wrap_call(self._vtk_obj.SetYAxesLinesProperty,
                        deref_vtk(arg))
        self.trait_property_changed('y_axes_lines_property', old_val, arg)
    y_axes_lines_property = traits.Property(_get_y_axes_lines_property, _set_y_axes_lines_property, help=\
        """
        Get/Set axes actors properties.
        """
    )

    y_axis_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(1e+299, 1e+299), cols=2, help=\
        """
        
        """
    )

    def _y_axis_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAxisRange,
                        self.y_axis_range)

    y_label_format = traits.String('%-#6.3g', enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels on each of the
        x-y-z axes.
        """
    )

    def _y_label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYLabelFormat,
                        self.y_label_format)

    y_title = traits.String('Y-Axis', enter_set=True, auto_set=False, help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use
        "X-Axis", "Y-Axis" and "Z-Axis".
        """
    )

    def _y_title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYTitle,
                        self.y_title)

    y_units = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use
        "X-Axis", "Y-Axis" and "Z-Axis".
        """
    )

    def _y_units_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYUnits,
                        self.y_units)

    def _get_z_axes_gridlines_property(self):
        return wrap_vtk(self._vtk_obj.GetZAxesGridlinesProperty())
    def _set_z_axes_gridlines_property(self, arg):
        old_val = self._get_z_axes_gridlines_property()
        self._wrap_call(self._vtk_obj.SetZAxesGridlinesProperty,
                        deref_vtk(arg))
        self.trait_property_changed('z_axes_gridlines_property', old_val, arg)
    z_axes_gridlines_property = traits.Property(_get_z_axes_gridlines_property, _set_z_axes_gridlines_property, help=\
        """
        Get/Set axes (outer) gridlines actors properties.
        """
    )

    def _get_z_axes_gridpolys_property(self):
        return wrap_vtk(self._vtk_obj.GetZAxesGridpolysProperty())
    def _set_z_axes_gridpolys_property(self, arg):
        old_val = self._get_z_axes_gridpolys_property()
        self._wrap_call(self._vtk_obj.SetZAxesGridpolysProperty,
                        deref_vtk(arg))
        self.trait_property_changed('z_axes_gridpolys_property', old_val, arg)
    z_axes_gridpolys_property = traits.Property(_get_z_axes_gridpolys_property, _set_z_axes_gridpolys_property, help=\
        """
        Get/Set axes grid_polys actors properties.
        """
    )

    def _get_z_axes_inner_gridlines_property(self):
        return wrap_vtk(self._vtk_obj.GetZAxesInnerGridlinesProperty())
    def _set_z_axes_inner_gridlines_property(self, arg):
        old_val = self._get_z_axes_inner_gridlines_property()
        self._wrap_call(self._vtk_obj.SetZAxesInnerGridlinesProperty,
                        deref_vtk(arg))
        self.trait_property_changed('z_axes_inner_gridlines_property', old_val, arg)
    z_axes_inner_gridlines_property = traits.Property(_get_z_axes_inner_gridlines_property, _set_z_axes_inner_gridlines_property, help=\
        """
        Get/Set axes inner gridlines actors properties.
        """
    )

    def _get_z_axes_lines_property(self):
        return wrap_vtk(self._vtk_obj.GetZAxesLinesProperty())
    def _set_z_axes_lines_property(self, arg):
        old_val = self._get_z_axes_lines_property()
        self._wrap_call(self._vtk_obj.SetZAxesLinesProperty,
                        deref_vtk(arg))
        self.trait_property_changed('z_axes_lines_property', old_val, arg)
    z_axes_lines_property = traits.Property(_get_z_axes_lines_property, _set_z_axes_lines_property, help=\
        """
        Get/Set axes actors properties.
        """
    )

    z_axis_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(1e+299, 1e+299), cols=2, help=\
        """
        
        """
    )

    def _z_axis_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZAxisRange,
                        self.z_axis_range)

    z_label_format = traits.String('%-#6.3g', enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels on each of the
        x-y-z axes.
        """
    )

    def _z_label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZLabelFormat,
                        self.z_label_format)

    z_title = traits.String('Z-Axis', enter_set=True, auto_set=False, help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use
        "X-Axis", "Y-Axis" and "Z-Axis".
        """
    )

    def _z_title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZTitle,
                        self.z_title)

    z_units = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the labels for the x, y, and z axes. By default, use
        "X-Axis", "Y-Axis" and "Z-Axis".
        """
    )

    def _z_units_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZUnits,
                        self.z_units)

    def get_label_text_property(self, *args):
        """
        V.get_label_text_property(int) -> TextProperty
        C++: TextProperty *GetLabelTextProperty(int)
        Returns the text property for the labels on an axis.
        """
        ret = self._wrap_call(self._vtk_obj.GetLabelTextProperty, *args)
        return wrap_vtk(ret)

    def _get_rendered_bounds(self):
        return self._vtk_obj.GetRenderedBounds()
    rendered_bounds = traits.Property(_get_rendered_bounds, help=\
        """
        Method used to properly return the bounds of the cube axis itself
        with all its labels.
        """
    )

    def get_title_text_property(self, *args):
        """
        V.get_title_text_property(int) -> TextProperty
        C++: TextProperty *GetTitleTextProperty(int)
        Returns the text property for the title on an axis.
        """
        ret = self._wrap_call(self._vtk_obj.GetTitleTextProperty, *args)
        return wrap_vtk(ret)

    def render_translucent_geometry(self, *args):
        """
        V.render_translucent_geometry(Viewport) -> int
        C++: virtual int RenderTranslucentGeometry(Viewport *)
        Draw the axes as per the Prop superclass' API.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderTranslucentGeometry, *my_args)
        return ret

    def set_label_scaling(self, *args):
        """
        V.set_label_scaling(bool, int, int, int)
        C++: void SetLabelScaling(bool, int, int, int)"""
        ret = self._wrap_call(self._vtk_obj.SetLabelScaling, *args)
        return ret

    def set_save_title_position(self, *args):
        """
        V.set_save_title_position(int)
        C++: void SetSaveTitlePosition(int val)
        For 2d mode only: save axis title positions for later use
        """
        ret = self._wrap_call(self._vtk_obj.SetSaveTitlePosition, *args)
        return ret

    _updateable_traits_ = \
    (('center_sticky_axes', 'GetCenterStickyAxes'), ('draw_x_gridlines',
    'GetDrawXGridlines'), ('draw_x_gridpolys', 'GetDrawXGridpolys'),
    ('draw_x_inner_gridlines', 'GetDrawXInnerGridlines'),
    ('draw_y_gridlines', 'GetDrawYGridlines'), ('draw_y_gridpolys',
    'GetDrawYGridpolys'), ('draw_y_inner_gridlines',
    'GetDrawYInnerGridlines'), ('draw_z_gridlines', 'GetDrawZGridlines'),
    ('draw_z_gridpolys', 'GetDrawZGridpolys'), ('draw_z_inner_gridlines',
    'GetDrawZInnerGridlines'), ('sticky_axes', 'GetStickyAxes'),
    ('x_axis_label_visibility', 'GetXAxisLabelVisibility'),
    ('x_axis_minor_tick_visibility', 'GetXAxisMinorTickVisibility'),
    ('x_axis_tick_visibility', 'GetXAxisTickVisibility'),
    ('x_axis_visibility', 'GetXAxisVisibility'),
    ('y_axis_label_visibility', 'GetYAxisLabelVisibility'),
    ('y_axis_minor_tick_visibility', 'GetYAxisMinorTickVisibility'),
    ('y_axis_tick_visibility', 'GetYAxisTickVisibility'),
    ('y_axis_visibility', 'GetYAxisVisibility'),
    ('z_axis_label_visibility', 'GetZAxisLabelVisibility'),
    ('z_axis_minor_tick_visibility', 'GetZAxisMinorTickVisibility'),
    ('z_axis_tick_visibility', 'GetZAxisTickVisibility'),
    ('z_axis_visibility', 'GetZAxisVisibility'), ('force_opaque',
    'GetForceOpaque'), ('force_translucent', 'GetForceTranslucent'),
    ('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('fly_mode', 'GetFlyMode'),
    ('tick_location', 'GetTickLocation'), ('axis_base_for_x',
    'GetAxisBaseForX'), ('axis_base_for_y', 'GetAxisBaseForY'),
    ('axis_base_for_z', 'GetAxisBaseForZ'), ('axis_origin',
    'GetAxisOrigin'), ('bounds', 'GetBounds'), ('corner_offset',
    'GetCornerOffset'), ('distance_lod_threshold',
    'GetDistanceLODThreshold'), ('enable_distance_lod',
    'GetEnableDistanceLOD'), ('enable_view_angle_lod',
    'GetEnableViewAngleLOD'), ('grid_line_location',
    'GetGridLineLocation'), ('inertia', 'GetInertia'), ('label_offset',
    'GetLabelOffset'), ('oriented_bounds', 'GetOrientedBounds'),
    ('rebuild_axes', 'GetRebuildAxes'), ('screen_size', 'GetScreenSize'),
    ('title_offset', 'GetTitleOffset'), ('use2d_mode', 'GetUse2DMode'),
    ('use_axis_origin', 'GetUseAxisOrigin'), ('use_oriented_bounds',
    'GetUseOrientedBounds'), ('use_text_actor3d', 'GetUseTextActor3D'),
    ('view_angle_lod_threshold', 'GetViewAngleLODThreshold'),
    ('x_axis_range', 'GetXAxisRange'), ('x_label_format',
    'GetXLabelFormat'), ('x_title', 'GetXTitle'), ('x_units',
    'GetXUnits'), ('y_axis_range', 'GetYAxisRange'), ('y_label_format',
    'GetYLabelFormat'), ('y_title', 'GetYTitle'), ('y_units',
    'GetYUnits'), ('z_axis_range', 'GetZAxisRange'), ('z_label_format',
    'GetZLabelFormat'), ('z_title', 'GetZTitle'), ('z_units',
    'GetZUnits'), ('orientation', 'GetOrientation'), ('origin',
    'GetOrigin'), ('position', 'GetPosition'), ('scale', 'GetScale'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['center_sticky_axes', 'debug', 'dragable', 'draw_x_gridlines',
    'draw_x_gridpolys', 'draw_x_inner_gridlines', 'draw_y_gridlines',
    'draw_y_gridpolys', 'draw_y_inner_gridlines', 'draw_z_gridlines',
    'draw_z_gridpolys', 'draw_z_inner_gridlines', 'force_opaque',
    'force_translucent', 'global_warning_display', 'pickable',
    'sticky_axes', 'use_bounds', 'visibility', 'x_axis_label_visibility',
    'x_axis_minor_tick_visibility', 'x_axis_tick_visibility',
    'x_axis_visibility', 'y_axis_label_visibility',
    'y_axis_minor_tick_visibility', 'y_axis_tick_visibility',
    'y_axis_visibility', 'z_axis_label_visibility',
    'z_axis_minor_tick_visibility', 'z_axis_tick_visibility',
    'z_axis_visibility', 'fly_mode', 'tick_location', 'axis_base_for_x',
    'axis_base_for_y', 'axis_base_for_z', 'axis_origin', 'bounds',
    'corner_offset', 'distance_lod_threshold', 'enable_distance_lod',
    'enable_view_angle_lod', 'estimated_render_time',
    'grid_line_location', 'inertia', 'label_offset', 'orientation',
    'oriented_bounds', 'origin', 'position', 'rebuild_axes',
    'render_time_multiplier', 'scale', 'screen_size', 'title_offset',
    'use2d_mode', 'use_axis_origin', 'use_oriented_bounds',
    'use_text_actor3d', 'view_angle_lod_threshold', 'x_axis_range',
    'x_label_format', 'x_title', 'x_units', 'y_axis_range',
    'y_label_format', 'y_title', 'y_units', 'z_axis_range',
    'z_label_format', 'z_title', 'z_units'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CubeAxesActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CubeAxesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['center_sticky_axes', 'draw_x_gridlines', 'draw_x_gridpolys',
            'draw_x_inner_gridlines', 'draw_y_gridlines', 'draw_y_gridpolys',
            'draw_y_inner_gridlines', 'draw_z_gridlines', 'draw_z_gridpolys',
            'draw_z_inner_gridlines', 'force_opaque', 'force_translucent',
            'sticky_axes', 'use_bounds', 'visibility', 'x_axis_label_visibility',
            'x_axis_minor_tick_visibility', 'x_axis_tick_visibility',
            'x_axis_visibility', 'y_axis_label_visibility',
            'y_axis_minor_tick_visibility', 'y_axis_tick_visibility',
            'y_axis_visibility', 'z_axis_label_visibility',
            'z_axis_minor_tick_visibility', 'z_axis_tick_visibility',
            'z_axis_visibility'], ['fly_mode', 'tick_location'],
            ['axis_base_for_x', 'axis_base_for_y', 'axis_base_for_z',
            'axis_origin', 'bounds', 'corner_offset', 'distance_lod_threshold',
            'enable_distance_lod', 'enable_view_angle_lod',
            'estimated_render_time', 'grid_line_location', 'inertia',
            'label_offset', 'orientation', 'oriented_bounds', 'origin',
            'position', 'rebuild_axes', 'render_time_multiplier', 'scale',
            'screen_size', 'title_offset', 'use2d_mode', 'use_axis_origin',
            'use_oriented_bounds', 'use_text_actor3d', 'view_angle_lod_threshold',
            'x_axis_range', 'x_label_format', 'x_title', 'x_units',
            'y_axis_range', 'y_label_format', 'y_title', 'y_units',
            'z_axis_range', 'z_label_format', 'z_title', 'z_units']),
            title='Edit CubeAxesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CubeAxesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


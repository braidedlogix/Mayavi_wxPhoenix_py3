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


class PolarAxesActor(Actor):
    """
    PolarAxesActor - create an actor of a polar axes -
    
    Superclass: Actor
    
    PolarAxesActor is a composite actor that draws polar axes in a
    specified plane for a give pole. Currently the plane has to be the xy
    plane.
    
    @par Thanks: This class was written by Philippe Pebay, Kitware SAS
    2011. This work was supported by CEA/DIF - Commissariat a l'Energie
    Atomique, Centre DAM Ile-De-France, BP12, F-91297 Arpajon, France.
    
    @sa
    Actor AxisActor PolarAxesActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolarAxesActor, obj, update, **traits)
    
    arc_minor_tick_visibility = tvtk_base.false_bool_trait(help=\
        """
        Turn on and off the visibility of minor ticks on the last arc.
        """
    )

    def _arc_minor_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArcMinorTickVisibility,
                        self.arc_minor_tick_visibility_)

    arc_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of major ticks on the last arc.
        """
    )

    def _arc_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArcTickVisibility,
                        self.arc_tick_visibility_)

    arc_ticks_origin_to_polar_axis = tvtk_base.true_bool_trait(help=\
        """
        If On, the ticks are drawn from the angle of the polar_axis (i.e.
        this->_minimal_radius) and continue counterclockwise with the step
        delta_angle Major/Minor. if Off, the start angle is 0.0, i.e. the
        angle on the major radius of the ellipse.
        """
    )

    def _arc_ticks_origin_to_polar_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArcTicksOriginToPolarAxis,
                        self.arc_ticks_origin_to_polar_axis_)

    auto_subdivide_polar_axis = tvtk_base.true_bool_trait(help=\
        """
        Set/Get whether the number of polar axis ticks and arcs should be
        automatically calculated Default: true
        """
    )

    def _auto_subdivide_polar_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoSubdividePolarAxis,
                        self.auto_subdivide_polar_axis_)

    axis_minor_tick_visibility = tvtk_base.false_bool_trait(help=\
        """
        Turn on and off the visibility of minor ticks on polar axis and
        last radial axis.
        """
    )

    def _axis_minor_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisMinorTickVisibility,
                        self.axis_minor_tick_visibility_)

    axis_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of major ticks on polar axis and
        last radial axis.
        """
    )

    def _axis_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisTickVisibility,
                        self.axis_tick_visibility_)

    draw_polar_arcs_gridlines = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of inner polar arcs grid lines
        """
    )

    def _draw_polar_arcs_gridlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawPolarArcsGridlines,
                        self.draw_polar_arcs_gridlines_)

    draw_radial_gridlines = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of inner radial grid lines
        """
    )

    def _draw_radial_gridlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawRadialGridlines,
                        self.draw_radial_gridlines_)

    log = tvtk_base.false_bool_trait(help=\
        """
        Enable/Disable log scale Default: true
        """
    )

    def _log_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLog,
                        self.log_)

    polar_arcs_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of arcs for polar axis.
        """
    )

    def _polar_arcs_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarArcsVisibility,
                        self.polar_arcs_visibility_)

    polar_axis_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of the polar axis.
        """
    )

    def _polar_axis_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarAxisVisibility,
                        self.polar_axis_visibility_)

    polar_label_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of labels for polar axis.
        """
    )

    def _polar_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarLabelVisibility,
                        self.polar_label_visibility_)

    polar_tick_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the overall visibility of ticks.
        """
    )

    def _polar_tick_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarTickVisibility,
                        self.polar_tick_visibility_)

    polar_title_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of titles for polar axis.
        """
    )

    def _polar_title_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarTitleVisibility,
                        self.polar_title_visibility_)

    radial_axes_origin_to_polar_axis = tvtk_base.true_bool_trait(help=\
        """
        If On, the radial axes are drawn from the angle of the polar_axis
        (i.e. this->_minimal_radius) and continue counterclockwise with the
        step delta_angle_radial_axes. if Off, the start angle is 0.0, i.e.
        the angle on the major radius of the ellipse.
        """
    )

    def _radial_axes_origin_to_polar_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadialAxesOriginToPolarAxis,
                        self.radial_axes_origin_to_polar_axis_)

    radial_axes_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of non-polar radial axes.
        """
    )

    def _radial_axes_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadialAxesVisibility,
                        self.radial_axes_visibility_)

    radial_title_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off the visibility of titles for non-polar radial
        axes.
        """
    )

    def _radial_title_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadialTitleVisibility,
                        self.radial_title_visibility_)

    arc_major_tick_size = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the size of the major ticks on the last arc.
        """
    )

    def _arc_major_tick_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArcMajorTickSize,
                        self.arc_major_tick_size)

    arc_major_tick_thickness = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the size of the thickness of the last arc ticks
        """
    )

    def _arc_major_tick_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArcMajorTickThickness,
                        self.arc_major_tick_thickness)

    arc_tick_ratio_size = traits.Float(0.3, enter_set=True, auto_set=False, help=\
        """
        Set/Get the ratio between major and minor Arc ticks size
        """
    )

    def _arc_tick_ratio_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArcTickRatioSize,
                        self.arc_tick_ratio_size)

    arc_tick_ratio_thickness = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the ratio between major and minor Arc ticks thickness
        """
    )

    def _arc_tick_ratio_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArcTickRatioThickness,
                        self.arc_tick_ratio_thickness)

    auto_scale_radius = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Turn on and off the auto-scaling of the maximum radius. Default:
        false
        """
    )

    def _auto_scale_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoScaleRadius,
                        self.auto_scale_radius)

    bounds = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(6,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
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
        PolarAxesActor.
        """
    )

    delta_angle_major = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the angle between 2 major ticks on the last arc.
        """
    )

    def _delta_angle_major_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeltaAngleMajor,
                        self.delta_angle_major)

    delta_angle_minor = traits.Float(5.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the angle between 2 minor ticks on the last arc.
        """
    )

    def _delta_angle_minor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeltaAngleMinor,
                        self.delta_angle_minor)

    delta_angle_radial_axes = traits.Float(45.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the angle between 2 radial axes.
        """
    )

    def _delta_angle_radial_axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeltaAngleRadialAxes,
                        self.delta_angle_radial_axes)

    delta_range_major = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the step between 2 major ticks, in range value (values
        displayed on the axis).
        """
    )

    def _delta_range_major_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeltaRangeMajor,
                        self.delta_range_major)

    delta_range_minor = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the step between 2 minor ticks, in range value (values
        displayed on the axis).
        """
    )

    def _delta_range_minor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeltaRangeMinor,
                        self.delta_range_minor)

    distance_lod_threshold = traits.Trait(0.7, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
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

    exponent_location = traits.Trait(2, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Get/Set the location of the exponent (if any) of the polar axis
        values. Possible location: VTK_EXPONENT_BOTTOM,
        VTK_EXPONENT_EXTERN, VTK_EXPONENT_LABELS
        """
    )

    def _exponent_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExponentLocation,
                        self.exponent_location)

    last_axis_tick_ratio_size = traits.Float(0.3, enter_set=True, auto_set=False, help=\
        """
        Set/Get the ratio between major and minor Last Radial axis ticks
        size
        """
    )

    def _last_axis_tick_ratio_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLastAxisTickRatioSize,
                        self.last_axis_tick_ratio_size)

    last_axis_tick_ratio_thickness = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the ratio between major and minor Last Radial axis ticks
        thickness
        """
    )

    def _last_axis_tick_ratio_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLastAxisTickRatioThickness,
                        self.last_axis_tick_ratio_thickness)

    last_radial_axis_major_tick_size = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the size of the major ticks on the last radial axis.
        """
    )

    def _last_radial_axis_major_tick_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLastRadialAxisMajorTickSize,
                        self.last_radial_axis_major_tick_size)

    last_radial_axis_major_tick_thickness = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the size of the thickness of last radial axis ticks
        """
    )

    def _last_radial_axis_major_tick_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLastRadialAxisMajorTickThickness,
                        self.last_radial_axis_major_tick_thickness)

    def _get_last_radial_axis_property(self):
        return wrap_vtk(self._vtk_obj.GetLastRadialAxisProperty())
    def _set_last_radial_axis_property(self, arg):
        old_val = self._get_last_radial_axis_property()
        self._wrap_call(self._vtk_obj.SetLastRadialAxisProperty,
                        deref_vtk(arg))
        self.trait_property_changed('last_radial_axis_property', old_val, arg)
    last_radial_axis_property = traits.Property(_get_last_radial_axis_property, _set_last_radial_axis_property, help=\
        """
        Get/Set last radial axis actor properties.
        """
    )

    def _get_last_radial_axis_text_property(self):
        return wrap_vtk(self._vtk_obj.GetLastRadialAxisTextProperty())
    def _set_last_radial_axis_text_property(self, arg):
        old_val = self._get_last_radial_axis_text_property()
        self._wrap_call(self._vtk_obj.SetLastRadialAxisTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('last_radial_axis_text_property', old_val, arg)
    last_radial_axis_text_property = traits.Property(_get_last_radial_axis_text_property, _set_last_radial_axis_text_property, help=\
        """
        Set/Get the last radial axis text property.
        """
    )

    maximum_angle = traits.Float(90.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum radius of the polar coordinates (in degrees).
        """
    )

    def _maximum_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumAngle,
                        self.maximum_angle)

    maximum_radius = traits.Float(5.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum radius of the polar coordinates.
        """
    )

    def _maximum_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumRadius,
                        self.maximum_radius)

    minimum_angle = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the minimum radius of the polar coordinates (in degrees).
        """
    )

    def _minimum_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumAngle,
                        self.minimum_angle)

    minimum_radius = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the minimal radius of the polar coordinates.
        """
    )

    def _minimum_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumRadius,
                        self.minimum_radius)

    number_of_polar_axis_ticks = traits.Int(11, enter_set=True, auto_set=False, help=\
        """
        Set/Get a number of ticks that one would like to display along
        polar axis NB: it modifies delta_range_major to correspond to this
        number
        """
    )

    def _number_of_polar_axis_ticks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPolarAxisTicks,
                        self.number_of_polar_axis_ticks)

    number_of_radial_axes = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Gets/Sets the number of radial axes
        """
    )

    def _number_of_radial_axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfRadialAxes,
                        self.number_of_radial_axes)

    def _get_polar_arcs_property(self):
        return wrap_vtk(self._vtk_obj.GetPolarArcsProperty())
    def _set_polar_arcs_property(self, arg):
        old_val = self._get_polar_arcs_property()
        self._wrap_call(self._vtk_obj.SetPolarArcsProperty,
                        deref_vtk(arg))
        self.trait_property_changed('polar_arcs_property', old_val, arg)
    polar_arcs_property = traits.Property(_get_polar_arcs_property, _set_polar_arcs_property, help=\
        """
        Get/Set principal polar arc actor property.
        """
    )

    def _get_polar_axis_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetPolarAxisLabelTextProperty())
    def _set_polar_axis_label_text_property(self, arg):
        old_val = self._get_polar_axis_label_text_property()
        self._wrap_call(self._vtk_obj.SetPolarAxisLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('polar_axis_label_text_property', old_val, arg)
    polar_axis_label_text_property = traits.Property(_get_polar_axis_label_text_property, _set_polar_axis_label_text_property, help=\
        """
        Set/Get the polar axis labels text property.
        """
    )

    polar_axis_major_tick_size = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the size of the major ticks on the polar axis.
        """
    )

    def _polar_axis_major_tick_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarAxisMajorTickSize,
                        self.polar_axis_major_tick_size)

    polar_axis_major_tick_thickness = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the size of the thickness of polar axis ticks
        """
    )

    def _polar_axis_major_tick_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarAxisMajorTickThickness,
                        self.polar_axis_major_tick_thickness)

    def _get_polar_axis_property(self):
        return wrap_vtk(self._vtk_obj.GetPolarAxisProperty())
    def _set_polar_axis_property(self, arg):
        old_val = self._get_polar_axis_property()
        self._wrap_call(self._vtk_obj.SetPolarAxisProperty,
                        deref_vtk(arg))
        self.trait_property_changed('polar_axis_property', old_val, arg)
    polar_axis_property = traits.Property(_get_polar_axis_property, _set_polar_axis_property, help=\
        """
        Get/Set polar axis actor properties.
        """
    )

    polar_axis_tick_ratio_size = traits.Float(0.3, enter_set=True, auto_set=False, help=\
        """
        Set/Get the ratio between major and minor Polar Axis ticks size
        """
    )

    def _polar_axis_tick_ratio_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarAxisTickRatioSize,
                        self.polar_axis_tick_ratio_size)

    polar_axis_tick_ratio_thickness = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the ratio between major and minor Polar Axis ticks
        thickness
        """
    )

    def _polar_axis_tick_ratio_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarAxisTickRatioThickness,
                        self.polar_axis_tick_ratio_thickness)

    polar_axis_title = traits.String('Radial Distance', enter_set=True, auto_set=False, help=\
        """
        Set/Get the labels for the polar axis. Default: "Radial
        Distance".
        """
    )

    def _polar_axis_title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarAxisTitle,
                        self.polar_axis_title)

    polar_axis_title_location = traits.Trait(0, traits.Range(0, 1, enter_set=True, auto_set=False), help=\
        """
        Get/Set the alignement of the polar axes title related to the
        axis. Possible Alignment: VTKTITLE_BOTTOM, VTK_TITLE_EXTERN
        """
    )

    def _polar_axis_title_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarAxisTitleLocation,
                        self.polar_axis_title_location)

    def _get_polar_axis_title_text_property(self):
        return wrap_vtk(self._vtk_obj.GetPolarAxisTitleTextProperty())
    def _set_polar_axis_title_text_property(self, arg):
        old_val = self._get_polar_axis_title_text_property()
        self._wrap_call(self._vtk_obj.SetPolarAxisTitleTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('polar_axis_title_text_property', old_val, arg)
    polar_axis_title_text_property = traits.Property(_get_polar_axis_title_text_property, _set_polar_axis_title_text_property, help=\
        """
        Set/Get the polar axis title text property.
        """
    )

    polar_label_format = traits.String('%-#6.3g', enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the polar axis labels.
        """
    )

    def _polar_label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarLabelFormat,
                        self.polar_label_format)

    pole = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Explicitly specify the coordinate of the pole.
        """
    )

    def _pole_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPole,
                        self.pole)

    radial_angle_format = traits.String('%-#3.1f', enter_set=True, auto_set=False, help=\
        """
        String to format angle values displayed on the radial axes.
        """
    )

    def _radial_angle_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadialAngleFormat,
                        self.radial_angle_format)

    radial_axis_title_location = traits.Trait(0, traits.Range(0, 1, enter_set=True, auto_set=False), help=\
        """
        Get/Set the alignement of the radial axes title related to the
        axis. Possible Alignment: VTK_TITLE_BOTTOM, VTK_TITLE_EXTERN
        """
    )

    def _radial_axis_title_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadialAxisTitleLocation,
                        self.radial_axis_title_location)

    radial_units = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Default: true
        """
    )

    def _radial_units_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadialUnits,
                        self.radial_units)

    range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 10.0), cols=2, help=\
        """
        
        """
    )

    def _range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRange,
                        self.range)

    ratio = traits.Trait(1.0, traits.Range(0.001, 100.0, enter_set=True, auto_set=False), help=\
        """
        Ratio
        """
    )

    def _ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRatio,
                        self.ratio)

    screen_size = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Explicitly specify the screen size of title and label text.
        screen_size detemines the size of the text in terms of screen
        pixels. Default: 10.0.
        """
    )

    def _screen_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScreenSize,
                        self.screen_size)

    def _get_secondary_polar_arcs_property(self):
        return wrap_vtk(self._vtk_obj.GetSecondaryPolarArcsProperty())
    def _set_secondary_polar_arcs_property(self, arg):
        old_val = self._get_secondary_polar_arcs_property()
        self._wrap_call(self._vtk_obj.SetSecondaryPolarArcsProperty,
                        deref_vtk(arg))
        self.trait_property_changed('secondary_polar_arcs_property', old_val, arg)
    secondary_polar_arcs_property = traits.Property(_get_secondary_polar_arcs_property, _set_secondary_polar_arcs_property, help=\
        """
        Get/Set secondary polar arcs actors property.
        """
    )

    def _get_secondary_radial_axes_property(self):
        return wrap_vtk(self._vtk_obj.GetSecondaryRadialAxesProperty())
    def _set_secondary_radial_axes_property(self, arg):
        old_val = self._get_secondary_radial_axes_property()
        self._wrap_call(self._vtk_obj.SetSecondaryRadialAxesProperty,
                        deref_vtk(arg))
        self.trait_property_changed('secondary_radial_axes_property', old_val, arg)
    secondary_radial_axes_property = traits.Property(_get_secondary_radial_axes_property, _set_secondary_radial_axes_property, help=\
        """
        Get/Set secondary radial axes actors properties.
        """
    )

    def _get_secondary_radial_axes_text_property(self):
        return wrap_vtk(self._vtk_obj.GetSecondaryRadialAxesTextProperty())
    def _set_secondary_radial_axes_text_property(self, arg):
        old_val = self._get_secondary_radial_axes_text_property()
        self._wrap_call(self._vtk_obj.SetSecondaryRadialAxesTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('secondary_radial_axes_text_property', old_val, arg)
    secondary_radial_axes_text_property = traits.Property(_get_secondary_radial_axes_text_property, _set_secondary_radial_axes_text_property, help=\
        """
        Set/Get the secondary radial axes text property.
        """
    )

    smallest_visible_polar_angle = traits.Trait(0.5, traits.Range(0.0, 5.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the minimum radial angle distinguishable from polar axis
        NB: This is used only when polar axis is visible Default: 0.5
        """
    )

    def _smallest_visible_polar_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSmallestVisiblePolarAngle,
                        self.smallest_visible_polar_angle)

    tick_location = traits.Trait(2, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Set/Get the location of the ticks. Inside: tick end toward
        positive direction of perpendicular axes. Outside: tick end
        toward negative direction of perpendicular axes.
        """
    )

    def _tick_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTickLocation,
                        self.tick_location)

    use2d_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Enable/Disable labels 2d mode (always facing the camera).
        """
    )

    def _use2d_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUse2DMode,
                        self.use2d_mode)

    view_angle_lod_threshold = traits.Trait(0.3, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set view angle LOD threshold [0.0 - 1.0] for titles and labels.
        """
    )

    def _view_angle_lod_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetViewAngleLODThreshold,
                        self.view_angle_lod_threshold)

    _updateable_traits_ = \
    (('arc_minor_tick_visibility', 'GetArcMinorTickVisibility'),
    ('arc_tick_visibility', 'GetArcTickVisibility'),
    ('arc_ticks_origin_to_polar_axis', 'GetArcTicksOriginToPolarAxis'),
    ('auto_subdivide_polar_axis', 'GetAutoSubdividePolarAxis'),
    ('axis_minor_tick_visibility', 'GetAxisMinorTickVisibility'),
    ('axis_tick_visibility', 'GetAxisTickVisibility'),
    ('draw_polar_arcs_gridlines', 'GetDrawPolarArcsGridlines'),
    ('draw_radial_gridlines', 'GetDrawRadialGridlines'), ('log',
    'GetLog'), ('polar_arcs_visibility', 'GetPolarArcsVisibility'),
    ('polar_axis_visibility', 'GetPolarAxisVisibility'),
    ('polar_label_visibility', 'GetPolarLabelVisibility'),
    ('polar_tick_visibility', 'GetPolarTickVisibility'),
    ('polar_title_visibility', 'GetPolarTitleVisibility'),
    ('radial_axes_origin_to_polar_axis',
    'GetRadialAxesOriginToPolarAxis'), ('radial_axes_visibility',
    'GetRadialAxesVisibility'), ('radial_title_visibility',
    'GetRadialTitleVisibility'), ('force_opaque', 'GetForceOpaque'),
    ('force_translucent', 'GetForceTranslucent'), ('dragable',
    'GetDragable'), ('pickable', 'GetPickable'), ('use_bounds',
    'GetUseBounds'), ('visibility', 'GetVisibility'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('arc_major_tick_size', 'GetArcMajorTickSize'),
    ('arc_major_tick_thickness', 'GetArcMajorTickThickness'),
    ('arc_tick_ratio_size', 'GetArcTickRatioSize'),
    ('arc_tick_ratio_thickness', 'GetArcTickRatioThickness'),
    ('auto_scale_radius', 'GetAutoScaleRadius'), ('delta_angle_major',
    'GetDeltaAngleMajor'), ('delta_angle_minor', 'GetDeltaAngleMinor'),
    ('delta_angle_radial_axes', 'GetDeltaAngleRadialAxes'),
    ('delta_range_major', 'GetDeltaRangeMajor'), ('delta_range_minor',
    'GetDeltaRangeMinor'), ('distance_lod_threshold',
    'GetDistanceLODThreshold'), ('enable_distance_lod',
    'GetEnableDistanceLOD'), ('enable_view_angle_lod',
    'GetEnableViewAngleLOD'), ('exponent_location',
    'GetExponentLocation'), ('last_axis_tick_ratio_size',
    'GetLastAxisTickRatioSize'), ('last_axis_tick_ratio_thickness',
    'GetLastAxisTickRatioThickness'), ('last_radial_axis_major_tick_size',
    'GetLastRadialAxisMajorTickSize'),
    ('last_radial_axis_major_tick_thickness',
    'GetLastRadialAxisMajorTickThickness'), ('maximum_angle',
    'GetMaximumAngle'), ('maximum_radius', 'GetMaximumRadius'),
    ('minimum_angle', 'GetMinimumAngle'), ('minimum_radius',
    'GetMinimumRadius'), ('number_of_polar_axis_ticks',
    'GetNumberOfPolarAxisTicks'), ('number_of_radial_axes',
    'GetNumberOfRadialAxes'), ('polar_axis_major_tick_size',
    'GetPolarAxisMajorTickSize'), ('polar_axis_major_tick_thickness',
    'GetPolarAxisMajorTickThickness'), ('polar_axis_tick_ratio_size',
    'GetPolarAxisTickRatioSize'), ('polar_axis_tick_ratio_thickness',
    'GetPolarAxisTickRatioThickness'), ('polar_axis_title',
    'GetPolarAxisTitle'), ('polar_axis_title_location',
    'GetPolarAxisTitleLocation'), ('polar_label_format',
    'GetPolarLabelFormat'), ('pole', 'GetPole'), ('radial_angle_format',
    'GetRadialAngleFormat'), ('radial_axis_title_location',
    'GetRadialAxisTitleLocation'), ('radial_units', 'GetRadialUnits'),
    ('range', 'GetRange'), ('ratio', 'GetRatio'), ('screen_size',
    'GetScreenSize'), ('smallest_visible_polar_angle',
    'GetSmallestVisiblePolarAngle'), ('tick_location', 'GetTickLocation'),
    ('use2d_mode', 'GetUse2DMode'), ('view_angle_lod_threshold',
    'GetViewAngleLODThreshold'), ('orientation', 'GetOrientation'),
    ('origin', 'GetOrigin'), ('position', 'GetPosition'), ('scale',
    'GetScale'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['arc_minor_tick_visibility', 'arc_tick_visibility',
    'arc_ticks_origin_to_polar_axis', 'auto_subdivide_polar_axis',
    'axis_minor_tick_visibility', 'axis_tick_visibility', 'debug',
    'dragable', 'draw_polar_arcs_gridlines', 'draw_radial_gridlines',
    'force_opaque', 'force_translucent', 'global_warning_display', 'log',
    'pickable', 'polar_arcs_visibility', 'polar_axis_visibility',
    'polar_label_visibility', 'polar_tick_visibility',
    'polar_title_visibility', 'radial_axes_origin_to_polar_axis',
    'radial_axes_visibility', 'radial_title_visibility', 'use_bounds',
    'visibility', 'arc_major_tick_size', 'arc_major_tick_thickness',
    'arc_tick_ratio_size', 'arc_tick_ratio_thickness',
    'auto_scale_radius', 'delta_angle_major', 'delta_angle_minor',
    'delta_angle_radial_axes', 'delta_range_major', 'delta_range_minor',
    'distance_lod_threshold', 'enable_distance_lod',
    'enable_view_angle_lod', 'estimated_render_time', 'exponent_location',
    'last_axis_tick_ratio_size', 'last_axis_tick_ratio_thickness',
    'last_radial_axis_major_tick_size',
    'last_radial_axis_major_tick_thickness', 'maximum_angle',
    'maximum_radius', 'minimum_angle', 'minimum_radius',
    'number_of_polar_axis_ticks', 'number_of_radial_axes', 'orientation',
    'origin', 'polar_axis_major_tick_size',
    'polar_axis_major_tick_thickness', 'polar_axis_tick_ratio_size',
    'polar_axis_tick_ratio_thickness', 'polar_axis_title',
    'polar_axis_title_location', 'polar_label_format', 'pole', 'position',
    'radial_angle_format', 'radial_axis_title_location', 'radial_units',
    'range', 'ratio', 'render_time_multiplier', 'scale', 'screen_size',
    'smallest_visible_polar_angle', 'tick_location', 'use2d_mode',
    'view_angle_lod_threshold'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolarAxesActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolarAxesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['arc_minor_tick_visibility', 'arc_tick_visibility',
            'arc_ticks_origin_to_polar_axis', 'auto_subdivide_polar_axis',
            'axis_minor_tick_visibility', 'axis_tick_visibility',
            'draw_polar_arcs_gridlines', 'draw_radial_gridlines', 'force_opaque',
            'force_translucent', 'log', 'polar_arcs_visibility',
            'polar_axis_visibility', 'polar_label_visibility',
            'polar_tick_visibility', 'polar_title_visibility',
            'radial_axes_origin_to_polar_axis', 'radial_axes_visibility',
            'radial_title_visibility', 'use_bounds', 'visibility'], [],
            ['arc_major_tick_size', 'arc_major_tick_thickness',
            'arc_tick_ratio_size', 'arc_tick_ratio_thickness',
            'auto_scale_radius', 'delta_angle_major', 'delta_angle_minor',
            'delta_angle_radial_axes', 'delta_range_major', 'delta_range_minor',
            'distance_lod_threshold', 'enable_distance_lod',
            'enable_view_angle_lod', 'estimated_render_time', 'exponent_location',
            'last_axis_tick_ratio_size', 'last_axis_tick_ratio_thickness',
            'last_radial_axis_major_tick_size',
            'last_radial_axis_major_tick_thickness', 'maximum_angle',
            'maximum_radius', 'minimum_angle', 'minimum_radius',
            'number_of_polar_axis_ticks', 'number_of_radial_axes', 'orientation',
            'origin', 'polar_axis_major_tick_size',
            'polar_axis_major_tick_thickness', 'polar_axis_tick_ratio_size',
            'polar_axis_tick_ratio_thickness', 'polar_axis_title',
            'polar_axis_title_location', 'polar_label_format', 'pole', 'position',
            'radial_angle_format', 'radial_axis_title_location', 'radial_units',
            'range', 'ratio', 'render_time_multiplier', 'scale', 'screen_size',
            'smallest_visible_polar_angle', 'tick_location', 'use2d_mode',
            'view_angle_lod_threshold']),
            title='Edit PolarAxesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolarAxesActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


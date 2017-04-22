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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class SphereSource(PolyDataAlgorithm):
    """
    SphereSource - create a polygonal sphere centered at the origin
    
    Superclass: PolyDataAlgorithm
    
    SphereSource creates a sphere (represented by polygons) of
    specified radius centered at the origin. The resolution (polygonal
    discretization) in both the latitude (phi) and longitude (theta)
    directions can be specified. It also is possible to create partial
    spheres by specifying maximum phi and theta angles. By default, the
    surface tessellation of the sphere uses triangles; however you can
    set lat_long_tessellation to produce a tessellation using
    quadrilaterals.
    @warning
    Resolution means the number of latitude or longitude lines for a
    complete sphere. If you create partial spheres the number of
    latitude/longitude lines may be off by one.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSphereSource, obj, update, **traits)
    
    lat_long_tessellation = tvtk_base.false_bool_trait(help=\
        """
        Cause the sphere to be tessellated with edges along the latitude
        and longitude lines. If off, triangles are generated at non-polar
        regions, which results in edges that are not parallel to latitude
        and longitude lines. If on, quadrilaterals are generated
        everywhere except at the poles. This can be useful for generating
        a wireframe sphere with natural latitude and longitude lines.
        """
    )

    def _lat_long_tessellation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLatLongTessellation,
                        self.lat_long_tessellation_)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    end_phi = traits.Trait(180.0, traits.Range(0.0, 360.0, enter_set=True, auto_set=False), help=\
        """
        Set the ending latitude angle. By default end_phi=_180 degrees.
        """
    )

    def _end_phi_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndPhi,
                        self.end_phi)

    end_theta = traits.Trait(360.0, traits.Range(0.0, 360.0, enter_set=True, auto_set=False), help=\
        """
        Set the ending longitude angle. By default end_theta=_360 degrees.
        """
    )

    def _end_theta_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndTheta,
                        self.end_theta)

    output_points_precision = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get the desired precision for the output points.
        Algorithm::SINGLE_PRECISION - Output single-precision floating
        point. Algorithm::DOUBLE_PRECISION - Output double-precision
        floating point.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

    phi_resolution = traits.Trait(8, traits.Range(3, 1024, enter_set=True, auto_set=False), help=\
        """
        Set the number of points in the latitude direction (ranging from
        start_phi to end_phi).
        """
    )

    def _phi_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhiResolution,
                        self.phi_resolution)

    radius = traits.Trait(0.5, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set radius of sphere. Default is .5.
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    start_phi = traits.Trait(0.0, traits.Range(0.0, 360.0, enter_set=True, auto_set=False), help=\
        """
        Set the starting latitude angle (0 is at north pole). By default
        start_phi=_0 degrees.
        """
    )

    def _start_phi_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartPhi,
                        self.start_phi)

    start_theta = traits.Trait(0.0, traits.Range(0.0, 360.0, enter_set=True, auto_set=False), help=\
        """
        Set the starting longitude angle. By default start_theta=_0
        degrees.
        """
    )

    def _start_theta_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartTheta,
                        self.start_theta)

    theta_resolution = traits.Trait(8, traits.Range(3, 1024, enter_set=True, auto_set=False), help=\
        """
        Set the number of points in the longitude direction (ranging from
        start_theta to end_theta).
        """
    )

    def _theta_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThetaResolution,
                        self.theta_resolution)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('lat_long_tessellation', 'GetLatLongTessellation'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('center',
    'GetCenter'), ('end_phi', 'GetEndPhi'), ('end_theta', 'GetEndTheta'),
    ('output_points_precision', 'GetOutputPointsPrecision'),
    ('phi_resolution', 'GetPhiResolution'), ('radius', 'GetRadius'),
    ('start_phi', 'GetStartPhi'), ('start_theta', 'GetStartTheta'),
    ('theta_resolution', 'GetThetaResolution'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'lat_long_tessellation', 'release_data_flag', 'center', 'end_phi',
    'end_theta', 'output_points_precision', 'phi_resolution',
    'progress_text', 'radius', 'start_phi', 'start_theta',
    'theta_resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SphereSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SphereSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['lat_long_tessellation'], [], ['center', 'end_phi',
            'end_theta', 'output_points_precision', 'phi_resolution', 'radius',
            'start_phi', 'start_theta', 'theta_resolution']),
            title='Edit SphereSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SphereSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


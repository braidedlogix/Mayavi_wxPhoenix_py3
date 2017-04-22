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


class GlobeSource(PolyDataAlgorithm):
    """
    GlobeSource - Sphere patch with Lat/Long scalar array.
    
    Superclass: PolyDataAlgorithm
    
    GlobeSource will generate any "rectangular" patch of the globe
    given its Longitude-Latitude extent.  It adds two point scalar arrays
    Longitude and Latitude to the output.  These arrays can be
    transformed to generate texture coordinates for any texture map. 
    This source is imperfect near the poles as implmented.  It should
    really reduce the longitude resolution as the triangles become
    slivers.
    
    \image html GlobeSourceSphericalToCartesianFigure.png\image latex
    GlobeSourceSphericalToCartesianFigure.eps
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGlobeSource, obj, update, **traits)
    
    auto_calculate_curtain_height = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )

    def _auto_calculate_curtain_height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoCalculateCurtainHeight,
                        self.auto_calculate_curtain_height_)

    quadrilateral_tessellation = tvtk_base.false_bool_trait(help=\
        """
        Cause the sphere to be tessellated with edges along the latitude
        and longitude lines. If off, triangles are generated at non-polar
        regions, which results in edges that are not parallel to latitude
        and longitude lines. If on, quadrilaterals are generated
        everywhere except at the poles. This can be useful for generating
        a wireframe sphere with natural latitude and longitude lines.
        """
    )

    def _quadrilateral_tessellation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuadrilateralTessellation,
                        self.quadrilateral_tessellation_)

    curtain_height = traits.Trait(1000.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get curtain height.
        """
    )

    def _curtain_height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCurtainHeight,
                        self.curtain_height)

    latitude_resolution = traits.Trait(10, traits.Range(3, 100, enter_set=True, auto_set=False), help=\
        """
        Set the number of points in the latitude direction (ranging from
        start_latitude to end_latitude).
        """
    )

    def _latitude_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLatitudeResolution,
                        self.latitude_resolution)

    longitude_resolution = traits.Trait(10, traits.Range(3, 100, enter_set=True, auto_set=False), help=\
        """
        Set the number of points in the longitude direction (ranging from
        start_longitude to end_longitude).
        """
    )

    def _longitude_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLongitudeResolution,
                        self.longitude_resolution)

    radius = traits.Trait(6356750.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set radius of sphere. Default is 6356750.0
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    def _get_end_latitude_max_value(self):
        return self._vtk_obj.GetEndLatitudeMaxValue()
    end_latitude_max_value = traits.Property(_get_end_latitude_max_value, help=\
        """
        Longitude Latitude clamps.
        """
    )

    def _get_end_latitude_min_value(self):
        return self._vtk_obj.GetEndLatitudeMinValue()
    end_latitude_min_value = traits.Property(_get_end_latitude_min_value, help=\
        """
        Longitude Latitude clamps.
        """
    )

    def _get_end_longitude_max_value(self):
        return self._vtk_obj.GetEndLongitudeMaxValue()
    end_longitude_max_value = traits.Property(_get_end_longitude_max_value, help=\
        """
        Longitude Latitude clamps.
        """
    )

    def _get_end_longitude_min_value(self):
        return self._vtk_obj.GetEndLongitudeMinValue()
    end_longitude_min_value = traits.Property(_get_end_longitude_min_value, help=\
        """
        Longitude Latitude clamps.
        """
    )

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

    def _get_start_latitude_max_value(self):
        return self._vtk_obj.GetStartLatitudeMaxValue()
    start_latitude_max_value = traits.Property(_get_start_latitude_max_value, help=\
        """
        Longitude Latitude clamps.
        """
    )

    def _get_start_latitude_min_value(self):
        return self._vtk_obj.GetStartLatitudeMinValue()
    start_latitude_min_value = traits.Property(_get_start_latitude_min_value, help=\
        """
        Longitude Latitude clamps.
        """
    )

    def _get_start_longitude_max_value(self):
        return self._vtk_obj.GetStartLongitudeMaxValue()
    start_longitude_max_value = traits.Property(_get_start_longitude_max_value, help=\
        """
        Longitude Latitude clamps.
        """
    )

    def _get_start_longitude_min_value(self):
        return self._vtk_obj.GetStartLongitudeMinValue()
    start_longitude_min_value = traits.Property(_get_start_longitude_min_value, help=\
        """
        Longitude Latitude clamps.
        """
    )

    def compute_globe_point(self, *args):
        """
        V.compute_globe_point(float, float, float, [float, ...], [float,
            ...])
        C++: static void ComputeGlobePoint(double theta, double phi,
            double radius, double *point, double *normal=0)
        Calculates the normal and point on a sphere with a specified
        radius at the spherical coordinates theta and phi.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeGlobePoint, *args)
        return ret

    def compute_latitude_longitude(self, *args):
        """
        V.compute_latitude_longitude([float, ...], float, float)
        C++: static void ComputeLatitudeLongitude(double *x,
            double &theta, double &phi)
        Calculates the spherical coordinates theta and phi based on the
        point on a sphere.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeLatitudeLongitude, *args)
        return ret

    def set_end_latitude(self, *args):
        """
        V.set_end_latitude(float)
        C++: void SetEndLatitude(double)
        Longitude Latitude clamps.
        """
        ret = self._wrap_call(self._vtk_obj.SetEndLatitude, *args)
        return ret

    def set_end_longitude(self, *args):
        """
        V.set_end_longitude(float)
        C++: void SetEndLongitude(double)
        Longitude Latitude clamps.
        """
        ret = self._wrap_call(self._vtk_obj.SetEndLongitude, *args)
        return ret

    def set_origin(self, *args):
        """
        V.set_origin(float, float, float)
        C++: void SetOrigin(double, double, double)
        V.set_origin((float, float, float))
        C++: void SetOrigin(double a[3])"""
        ret = self._wrap_call(self._vtk_obj.SetOrigin, *args)
        return ret

    def set_start_latitude(self, *args):
        """
        V.set_start_latitude(float)
        C++: void SetStartLatitude(double)
        Longitude Latitude clamps.
        """
        ret = self._wrap_call(self._vtk_obj.SetStartLatitude, *args)
        return ret

    def set_start_longitude(self, *args):
        """
        V.set_start_longitude(float)
        C++: void SetStartLongitude(double)
        Longitude Latitude clamps.
        """
        ret = self._wrap_call(self._vtk_obj.SetStartLongitude, *args)
        return ret

    _updateable_traits_ = \
    (('auto_calculate_curtain_height', 'GetAutoCalculateCurtainHeight'),
    ('quadrilateral_tessellation', 'GetQuadrilateralTessellation'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('curtain_height', 'GetCurtainHeight'), ('latitude_resolution',
    'GetLatitudeResolution'), ('longitude_resolution',
    'GetLongitudeResolution'), ('radius', 'GetRadius'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_calculate_curtain_height', 'debug',
    'global_warning_display', 'quadrilateral_tessellation',
    'release_data_flag', 'curtain_height', 'latitude_resolution',
    'longitude_resolution', 'progress_text', 'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GlobeSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GlobeSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_calculate_curtain_height', 'quadrilateral_tessellation'],
            [], ['curtain_height', 'latitude_resolution', 'longitude_resolution',
            'radius']),
            title='Edit GlobeSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GlobeSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


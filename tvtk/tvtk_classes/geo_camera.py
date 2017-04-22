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

from tvtk.tvtk_classes.object import Object


class GeoCamera(Object):
    """
    GeoCamera - Geo interface to a camera.
    
    Superclass: Object
    
    I wanted to hide the normal Camera API so I did not make this a
    subclass.  The camera is a helper object. You can get a pointer to
    the camera, but it should be treated like a const.
    
    View up of the camera is restricted so there is no roll relative to
    the earth.  I am going to keep view up of the camera orthogonalized
    to avoid the singularity that exists when the camera is pointing
    straight down. In this case, view up is the same as heading.
    
    The state of the view is specified by the vector:
    (Longitude,Latitude,Distance,Heading,Tilt).
      Longitude in degrees: (-180->180)
        Relative to absolute coordinates.
      Latitude in degrees: (-90->90)
        Relative to Longitude.
      Distance in Meters
        Relative to Longitude and Latitude.
        above sea level   ???? should we make this from center of earth
    ????
                          ???? what about equatorial bulge ????
      Heading in degrees:  (-180->180)
        Relative to Logitude and Latitude.
        0 is north.
        90 is east.       ???? what is the standard ????
        180 is south.
    -90 is west. Tilt in degrees: (0->90) Relative to Longitude,
        Latitude, Distance and Heading.
    
    Transformation:
      Post concatenate.
      All rotations use right hand rule and are around (0,0,0) (earth
    center).
      (0,0,0,0,0) is this rectilinear point (0, earth_radius, 0)
                  pointing (0,0,1), view up (0,1,0).
    
    
      Rotate Tilt       around x axis,
      Rotate Heading    around -y axis Center,
      Translate earth_radius in y direction.
      Rotate Latitude   around x axis by Latitude,
      Rotate Longitude  around z axis (earth axis),
    
    @sa
    GeoInteractorStyle Camera
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoCamera, obj, update, **traits)
    
    lock_heading = tvtk_base.true_bool_trait(help=\
        """
        Whether to lock the heading a particular value, or to let the
        heading "roam free" when performing latitude and longitude
        changes.
        """
    )

    def _lock_heading_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLockHeading,
                        self.lock_heading_)

    distance = traits.Float(31783750.0, enter_set=True, auto_set=False, help=\
        """
        Distance is in Meters Relative to Longitude and Latitude. above
        sea level   ???? should we make this from center of earth ????
        ???? what about equatorial bulge ????
        """
    )

    def _distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistance,
                        self.distance)

    heading = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Heading is in degrees:  (-180->180) Relative to Logitude and
        Latitude. 0 is north. 90 is east.       ???? what is the standard
        ???? 180 is south.
        -90 is west. Rotate Heading    around -y axis Center,
        """
    )

    def _heading_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeading,
                        self.heading)

    latitude = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Latitude is in degrees: (-90->90) Relative to Longitude. Rotate
        Latitude   around x axis by Latitude,
        """
    )

    def _latitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLatitude,
                        self.latitude)

    longitude = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Longitude is in degrees: (-180->180) Relative to absolute
        coordinates. Rotate Longitude  around z axis (earth axis),
        """
    )

    def _longitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLongitude,
                        self.longitude)

    origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Get the rectilinear cooridinate location of the origin. This is
        used to shift the terrain points.
        """
    )

    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    origin_latitude = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        This point is shifted to 0,0,0 to avoid open_gl issues.
        """
    )

    def _origin_latitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginLatitude,
                        self.origin_latitude)

    origin_longitude = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        This point is shifted to 0,0,0 to avoid open_gl issues.
        """
    )

    def _origin_longitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginLongitude,
                        self.origin_longitude)

    tilt = traits.Float(90.0, enter_set=True, auto_set=False, help=\
        """
        Tilt is also know as pitch. Tilt is in degrees: (0->90) Relative
        to Longitude, Latitude, and Heading. Rotate Tilt       around x
        axis,
        """
    )

    def _tilt_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTilt,
                        self.tilt)

    def get_node_coverage(self, *args):
        """
        V.get_node_coverage(GeoTerrainNode) -> float
        C++: double GetNodeCoverage(GeoTerrainNode *node)
        This method estimates how much of the view is covered by the
        sphere. Returns a value from 0 to 1.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetNodeCoverage, *my_args)
        return ret

    def _get_position(self):
        return self._vtk_obj.GetPosition()
    position = traits.Property(_get_position, help=\
        """
        
        """
    )

    def _get_vtk_camera(self):
        return wrap_vtk(self._vtk_obj.GetVTKCamera())
    vtk_camera = traits.Property(_get_vtk_camera, help=\
        """
        This vtk camera is updated to match this geo cameras state. It
        should be treated as a const and should not be modified.
        """
    )

    def initialize_node_analysis(self, *args):
        """
        V.initialize_node_analysis([int, int])
        C++: void InitializeNodeAnalysis(int rendererSize[2])
        We precompute some values to speed up update of the terrain.
        Unfortunately, they have to be manually/explicitly updated when
        the camera or renderer size changes.
        """
        ret = self._wrap_call(self._vtk_obj.InitializeNodeAnalysis, *args)
        return ret

    _updateable_traits_ = \
    (('lock_heading', 'GetLockHeading'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('distance',
    'GetDistance'), ('heading', 'GetHeading'), ('latitude',
    'GetLatitude'), ('longitude', 'GetLongitude'), ('origin',
    'GetOrigin'), ('origin_latitude', 'GetOriginLatitude'),
    ('origin_longitude', 'GetOriginLongitude'), ('tilt', 'GetTilt'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'lock_heading', 'distance',
    'heading', 'latitude', 'longitude', 'origin', 'origin_latitude',
    'origin_longitude', 'tilt'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoCamera, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoCamera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['lock_heading'], [], ['distance', 'heading', 'latitude',
            'longitude', 'origin', 'origin_latitude', 'origin_longitude',
            'tilt']),
            title='Edit GeoCamera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoCamera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.pass_input_type_algorithm import PassInputTypeAlgorithm


class GeoAssignCoordinates(PassInputTypeAlgorithm):
    """
    GeoAssignCoordinates - Given latitude and longitude arrays, take
    the values in those arrays and convert them to x,y,z world
    coordinates.
    
    Superclass: PassInputTypeAlgorithm
    
    Givem latitude and longitude arrays, take the values in those arrays
    and convert them to x,y,z world coordinates. Uses a spherical model
    of the earth to do the conversion. The position is in meters relative
    to the center of the earth.
    
    If a transform is given, use the transform to convert latitude and
    longitude to the world coordinate.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoAssignCoordinates, obj, update, **traits)
    
    coordinates_in_arrays = tvtk_base.true_bool_trait(help=\
        """
        If on, uses latitude_array_name and longitude_array_name to move
        values in data arrays into the points of the data set. Turn off
        if the latitude and longitude are already in the points.
        """
    )

    def _coordinates_in_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCoordinatesInArrays,
                        self.coordinates_in_arrays_)

    globe_radius = traits.Float(6356750.0, enter_set=True, auto_set=False, help=\
        """
        The base radius to use in GLOBAL mode. Default is the earth's
        radius.
        """
    )

    def _globe_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobeRadius,
                        self.globe_radius)

    latitude_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the latitude coordinate array name.
        """
    )

    def _latitude_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLatitudeArrayName,
                        self.latitude_array_name)

    longitude_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the longitude coordinate array name.
        """
    )

    def _longitude_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLongitudeArrayName,
                        self.longitude_array_name)

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        The transform to use to convert coordinates of the form (lat,
        long, 0) to (x, y z). If this is NULL (the default), use
        globe_radius to perform a spherical embedding.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    _updateable_traits_ = \
    (('coordinates_in_arrays', 'GetCoordinatesInArrays'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('globe_radius', 'GetGlobeRadius'), ('latitude_array_name',
    'GetLatitudeArrayName'), ('longitude_array_name',
    'GetLongitudeArrayName'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'coordinates_in_arrays', 'debug',
    'global_warning_display', 'release_data_flag', 'globe_radius',
    'latitude_array_name', 'longitude_array_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoAssignCoordinates, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoAssignCoordinates properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['coordinates_in_arrays'], [], ['globe_radius',
            'latitude_array_name', 'longitude_array_name']),
            title='Edit GeoAssignCoordinates properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoAssignCoordinates properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


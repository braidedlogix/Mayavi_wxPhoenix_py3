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


class GeoGraticule(PolyDataAlgorithm):
    """
    GeoGraticule - Create a polygonal lat-long grid
    
    Superclass: PolyDataAlgorithm
    
    This filter generates polydata to illustrate the distortions
    introduced by a map projection. The level parameter specifies the
    number of lines to be drawn. Poles are treated differently than other
    regions; hence the use of a Level parameter instead of a
    number_of_lines parameter. The latitude and longitude are specified as
    half-open intervals with units of degrees. By default the latitude
    bounds are [-90,90[ and the longitude bounds are [0,180[.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoGraticule, obj, update, **traits)
    
    geometry_type = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set//get the type(s) of cells that will be output by the filter.
        By default, polylines are output. You may also request
        quadrilaterals. This is a bit vector of geometry_type enums.
        """
    )

    def _geometry_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeometryType,
                        self.geometry_type)

    latitude_bounds = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(-90.0, 90.0), cols=2, help=\
        """
        
        """
    )

    def _latitude_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLatitudeBounds,
                        self.latitude_bounds)

    latitude_level = traits.Trait(2, traits.Range(0, 11, enter_set=True, auto_set=False), help=\
        """
        The frequency level of latitude lines.
        """
    )

    def _latitude_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLatitudeLevel,
                        self.latitude_level)

    longitude_bounds = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 180.0), cols=2, help=\
        """
        
        """
    )

    def _longitude_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLongitudeBounds,
                        self.longitude_bounds)

    longitude_level = traits.Trait(1, traits.Range(0, 11, enter_set=True, auto_set=False), help=\
        """
        The frequency level of longitude lines.
        """
    )

    def _longitude_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLongitudeLevel,
                        self.longitude_level)

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

    def get_latitude_delta(self, *args):
        """
        V.get_latitude_delta(int) -> float
        C++: static double GetLatitudeDelta(int level)
        The latitude delta at a certain frequency level.
        """
        ret = self._wrap_call(self._vtk_obj.GetLatitudeDelta, *args)
        return ret

    def get_longitude_delta(self, *args):
        """
        V.get_longitude_delta(int) -> float
        C++: static double GetLongitudeDelta(int level)
        The longitude delta at a certain frequency level.
        """
        ret = self._wrap_call(self._vtk_obj.GetLongitudeDelta, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('geometry_type', 'GetGeometryType'), ('latitude_bounds',
    'GetLatitudeBounds'), ('latitude_level', 'GetLatitudeLevel'),
    ('longitude_bounds', 'GetLongitudeBounds'), ('longitude_level',
    'GetLongitudeLevel'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'geometry_type', 'latitude_bounds',
    'latitude_level', 'longitude_bounds', 'longitude_level',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoGraticule, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoGraticule properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['geometry_type', 'latitude_bounds', 'latitude_level',
            'longitude_bounds', 'longitude_level']),
            title='Edit GeoGraticule properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoGraticule properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


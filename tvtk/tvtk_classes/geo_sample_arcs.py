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


class GeoSampleArcs(PolyDataAlgorithm):
    """
    GeoSampleArcs - Samples geospatial lines at regular intervals.
    
    Superclass: PolyDataAlgorithm
    
    GeoSampleArcs refines lines in the input polygonal data so that
    the distance between adjacent points is no more than a threshold
    distance. Points are interpolated along the surface of the globe.
    This is useful in order to keep lines such as political boundaries
    from intersecting the globe and becoming invisible.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoSampleArcs, obj, update, **traits)
    
    input_coordinate_system = traits.Trait('rectangular',
    tvtk_base.TraitRevPrefixMap({'rectangular': 0, 'spherical': 1}), help=\
        """
        The input coordinate system. RECTANGULAR is x,y,z meters relative
        the the earth center. SPHERICAL is longitude,latitude,altitude.
        """
    )

    def _input_coordinate_system_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputCoordinateSystem,
                        self.input_coordinate_system_)

    output_coordinate_system = traits.Trait('rectangular',
    tvtk_base.TraitRevPrefixMap({'rectangular': 0, 'spherical': 1}), help=\
        """
        The desired output coordinate system. RECTANGULAR is x,y,z meters
        relative the the earth center. SPHERICAL is
        longitude,latitude,altitude.
        """
    )

    def _output_coordinate_system_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputCoordinateSystem,
                        self.output_coordinate_system_)

    globe_radius = traits.Float(6356750.0, enter_set=True, auto_set=False, help=\
        """
        The base radius used to determine the earth's surface. Default is
        the earth's radius in meters. TODO: Change this to take in a
        GeoTerrain to get altitude.
        """
    )

    def _globe_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobeRadius,
                        self.globe_radius)

    maximum_distance_meters = traits.Float(100000.0, enter_set=True, auto_set=False, help=\
        """
        The maximum distance, in meters, between adjacent points.
        """
    )

    def _maximum_distance_meters_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumDistanceMeters,
                        self.maximum_distance_meters)

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
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('input_coordinate_system', 'GetInputCoordinateSystem'),
    ('output_coordinate_system', 'GetOutputCoordinateSystem'),
    ('globe_radius', 'GetGlobeRadius'), ('maximum_distance_meters',
    'GetMaximumDistanceMeters'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'input_coordinate_system',
    'output_coordinate_system', 'globe_radius', 'maximum_distance_meters',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoSampleArcs, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoSampleArcs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['input_coordinate_system', 'output_coordinate_system'],
            ['globe_radius', 'maximum_distance_meters']),
            title='Edit GeoSampleArcs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoSampleArcs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


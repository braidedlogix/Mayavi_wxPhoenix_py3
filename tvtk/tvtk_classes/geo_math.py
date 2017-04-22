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


class GeoMath(Object):
    """
    GeoMath - Useful geographic calculations
    
    Superclass: Object
    
    GeoMath provides some useful geographic calculations.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoMath, obj, update, **traits)
    
    def distance_squared(self, *args):
        """
        V.distance_squared([float, float, float], [float, float, float])
            -> float
        C++: static double DistanceSquared(double pt0[3], double pt1[3])
        Returns the squared distance between two points.
        """
        ret = self._wrap_call(self._vtk_obj.DistanceSquared, *args)
        return ret

    def earth_radius_meters(self):
        """
        V.earth_radius_meters() -> float
        C++: static double EarthRadiusMeters()
        Returns the average radius of the earth in meters.
        """
        ret = self._vtk_obj.EarthRadiusMeters()
        return ret
        

    def long_lat_alt_to_rect(self, *args):
        """
        V.long_lat_alt_to_rect([float, float, float], [float, float, float])
        C++: static void LongLatAltToRect(double lla[3], double rect[3])
        Converts a (longitude, latitude, altitude) triple to world
        coordinates where the center of the earth is at the origin. Units
        are in meters. Note that having altitude realtive to sea level
        causes issues.
        """
        ret = self._wrap_call(self._vtk_obj.LongLatAltToRect, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoMath, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoMath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit GeoMath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoMath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


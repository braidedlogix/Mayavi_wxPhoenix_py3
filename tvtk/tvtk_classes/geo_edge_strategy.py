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

from tvtk.tvtk_classes.edge_layout_strategy import EdgeLayoutStrategy


class GeoEdgeStrategy(EdgeLayoutStrategy):
    """
    GeoEdgeStrategy - Layout graph edges on a globe as arcs.
    
    Superclass: EdgeLayoutStrategy
    
    GeoEdgeStrategy produces arcs for each edge in the input graph.
    This is useful for viewing lines on a sphere (e.g. the earth). The
    arcs may "jump" above the sphere's surface using explode_factor.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoEdgeStrategy, obj, update, **traits)
    
    explode_factor = traits.Float(0.2, enter_set=True, auto_set=False, help=\
        """
        Factor on which to "explode" the arcs away from the surface. A
        value of 0.0 keeps the values on the surface. Values larger than
        0.0 push the arcs away from the surface by a distance
        proportional to the distance between the points. The default is
        0.2.
        """
    )

    def _explode_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExplodeFactor,
                        self.explode_factor)

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

    number_of_subdivisions = traits.Int(20, enter_set=True, auto_set=False, help=\
        """
        The number of subdivisions in the arc. The default is 20.
        """
    )

    def _number_of_subdivisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSubdivisions,
                        self.number_of_subdivisions)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('explode_factor', 'GetExplodeFactor'),
    ('globe_radius', 'GetGlobeRadius'), ('number_of_subdivisions',
    'GetNumberOfSubdivisions'), ('edge_weight_array_name',
    'GetEdgeWeightArrayName'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'edge_weight_array_name',
    'explode_factor', 'globe_radius', 'number_of_subdivisions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoEdgeStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoEdgeStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['edge_weight_array_name', 'explode_factor',
            'globe_radius', 'number_of_subdivisions']),
            title='Edit GeoEdgeStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoEdgeStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


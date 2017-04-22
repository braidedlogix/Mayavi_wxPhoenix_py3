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

from tvtk.tvtk_classes.geo_tree_node import GeoTreeNode


class GeoTerrainNode(GeoTreeNode):
    """
    GeoTerrainNode - 
    
    Superclass: GeoTreeNode
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoTerrainNode, obj, update, **traits)
    
    def get_child(self, *args):
        """
        V.get_child(int) -> GeoTerrainNode
        C++: GeoTerrainNode *GetChild(int idx)
        Every subclass implements these methods returning the specific
        type. This is easier than templating.
        """
        ret = self._wrap_call(self._vtk_obj.GetChild, *args)
        return wrap_vtk(ret)

    def set_child(self, *args):
        """
        V.set_child(GeoTreeNode, int)
        C++: void SetChild(GeoTreeNode *node, int idx)
        Get a child of this node. If one is set, then they all should
        set.  No not mix subclasses.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetChild, *my_args)
        return ret

    coverage = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        For 2d projections, store the maximum deviation of line segment
        centers from the actual projection value.
        """
    )

    def _coverage_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCoverage,
                        self.coverage)

    error = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        For 2d projections, store the maximum deviation of line segment
        centers from the actual projection value.
        """
    )

    def _error_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetError,
                        self.error)

    graticule_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        For 2d projections, store the granularity of the graticule in
        this node.
        """
    )

    def _graticule_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraticuleLevel,
                        self.graticule_level)

    def _get_model(self):
        return wrap_vtk(self._vtk_obj.GetModel())
    def _set_model(self, arg):
        old_val = self._get_model()
        self._wrap_call(self._vtk_obj.SetModel,
                        deref_vtk(arg))
        self.trait_property_changed('model', old_val, arg)
    model = traits.Property(_get_model, _set_model, help=\
        """
        Get the terrrain model.  The user has to copy the terrain into
        this object.
        """
    )

    def _get_parent(self):
        return wrap_vtk(self._vtk_obj.GetParent())
    def _set_parent(self, arg):
        old_val = self._get_parent()
        self._wrap_call(self._vtk_obj.SetParent,
                        deref_vtk(arg))
        self.trait_property_changed('parent', old_val, arg)
    parent = traits.Property(_get_parent, _set_parent, help=\
        """
        Every subclass implements these methods returning the specific
        type. This is easier than templating.
        """
    )

    projection_bounds = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _projection_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectionBounds,
                        self.projection_bounds)

    def get_altitude(self, *args):
        """
        V.get_altitude(float, float) -> float
        C++: double GetAltitude(double longitude, double latitude)
        Given, a long, lat position, return altitude in meters relative
        to  sea level.
        """
        ret = self._wrap_call(self._vtk_obj.GetAltitude, *args)
        return ret

    def _get_bounding_sphere_center(self):
        return self._vtk_obj.GetBoundingSphereCenter()
    bounding_sphere_center = traits.Property(_get_bounding_sphere_center, help=\
        """
        
        """
    )

    def _get_bounding_sphere_radius(self):
        return self._vtk_obj.GetBoundingSphereRadius()
    bounding_sphere_radius = traits.Property(_get_bounding_sphere_radius, help=\
        """
        Bounding sphere is precomputed for faster updates of terrain.
        """
    )

    def _get_corner_normal00(self):
        return self._vtk_obj.GetCornerNormal00()
    corner_normal00 = traits.Property(_get_corner_normal00, help=\
        """
        
        """
    )

    def _get_corner_normal01(self):
        return self._vtk_obj.GetCornerNormal01()
    corner_normal01 = traits.Property(_get_corner_normal01, help=\
        """
        
        """
    )

    def _get_corner_normal10(self):
        return self._vtk_obj.GetCornerNormal10()
    corner_normal10 = traits.Property(_get_corner_normal10, help=\
        """
        
        """
    )

    def _get_corner_normal11(self):
        return self._vtk_obj.GetCornerNormal11()
    corner_normal11 = traits.Property(_get_corner_normal11, help=\
        """
        
        """
    )

    def update_bounding_sphere(self):
        """
        V.update_bounding_sphere()
        C++: void UpdateBoundingSphere()
        Bounding sphere is precomputed for faster updates of terrain.
        """
        ret = self._vtk_obj.UpdateBoundingSphere()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('coverage', 'GetCoverage'), ('error',
    'GetError'), ('graticule_level', 'GetGraticuleLevel'),
    ('projection_bounds', 'GetProjectionBounds'), ('id', 'GetId'),
    ('latitude_range', 'GetLatitudeRange'), ('level', 'GetLevel'),
    ('longitude_range', 'GetLongitudeRange'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'coverage', 'error',
    'graticule_level', 'id', 'latitude_range', 'level', 'longitude_range',
    'projection_bounds'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoTerrainNode, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoTerrainNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['coverage', 'error', 'graticule_level', 'id',
            'latitude_range', 'level', 'longitude_range', 'projection_bounds']),
            title='Edit GeoTerrainNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoTerrainNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


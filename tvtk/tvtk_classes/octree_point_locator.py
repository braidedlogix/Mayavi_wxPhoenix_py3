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

from tvtk.tvtk_classes.abstract_point_locator import AbstractPointLocator


class OctreePointLocator(AbstractPointLocator):
    """
    OctreePointLocator - an octree spatial decomposition of a set of
    points
    
    Superclass: AbstractPointLocator
    
    Given a DataSet, create an octree that is locally refined such
    that all leaf octants contain less than a certain amount of points. 
    Note that there is no size constraint that a leaf octant in relation
    to any of its neighbors.
    
    This class can also generate a poly_data representation of the
    boundaries of the spatial regions in the decomposition.
    
    @sa
    Locator PointLocator OctreePointLocatorNode
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOctreePointLocator, obj, update, **traits)
    
    create_cubic_octants = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Get/Set macro for create_cubic_octants.
        """
    )

    def _create_cubic_octants_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCreateCubicOctants,
                        self.create_cubic_octants)

    fudge_factor = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Some algorithms on octrees require a value that is a very small
        distance relative to the diameter of the entire space divided by
        the octree.  This factor is the maximum axis-aligned width of the
        space multiplied by 10e-6.
        """
    )

    def _fudge_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFudgeFactor,
                        self.fudge_factor)

    maximum_points_per_region = traits.Int(100, enter_set=True, auto_set=False, help=\
        """
        Maximum number of points per spatial region.  Default is 100.
        """
    )

    def _maximum_points_per_region_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumPointsPerRegion,
                        self.maximum_points_per_region)

    def _get_number_of_leaf_nodes(self):
        return self._vtk_obj.GetNumberOfLeafNodes()
    number_of_leaf_nodes = traits.Property(_get_number_of_leaf_nodes, help=\
        """
        The number of leaf nodes of the tree, the spatial regions
        """
    )

    def get_points_in_region(self, *args):
        """
        V.get_points_in_region(int) -> IdTypeArray
        C++: IdTypeArray *GetPointsInRegion(int leafNodeId)
        Get a list of the original IDs of all points in a leaf node.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointsInRegion, *args)
        return wrap_vtk(ret)

    def get_region_bounds(self, *args):
        """
        V.get_region_bounds(int, [float, float, float, float, float, float])
        C++: void GetRegionBounds(int regionID, double bounds[6])
        Get the spatial bounds of octree region
        """
        ret = self._wrap_call(self._vtk_obj.GetRegionBounds, *args)
        return ret

    def get_region_containing_point(self, *args):
        """
        V.get_region_containing_point(float, float, float) -> int
        C++: int GetRegionContainingPoint(double x, double y, double z)
        Get the id of the leaf region containing the specified location.
        """
        ret = self._wrap_call(self._vtk_obj.GetRegionContainingPoint, *args)
        return ret

    def get_region_data_bounds(self, *args):
        """
        V.get_region_data_bounds(int, [float, float, float, float, float,
            float])
        C++: void GetRegionDataBounds(int leafNodeID, double bounds[6])
        Get the bounds of the data within the leaf node
        """
        ret = self._wrap_call(self._vtk_obj.GetRegionDataBounds, *args)
        return ret

    def find_closest_point_in_region(self, *args):
        """
        V.find_closest_point_in_region(int, [float, ...], float) -> int
        C++: IdType FindClosestPointInRegion(int regionId, double *x,
            double &dist2)
        V.find_closest_point_in_region(int, float, float, float, float) -> int
        C++: IdType FindClosestPointInRegion(int regionId, double x,
            double y, double z, double &dist2)
        Find the Id of the point in the given leaf region which is
        closest to the given point.  Return the ID of the point, and set
        the square of the distance of between the points.
        """
        ret = self._wrap_call(self._vtk_obj.FindClosestPointInRegion, *args)
        return ret

    def find_points_in_area(self, *args):
        """
        V.find_points_in_area([float, ...], IdTypeArray, bool)
        C++: void FindPointsInArea(double *area, IdTypeArray *ids,
            bool clearArray=true)
        Fill ids with points found in area.  The area is a 6-tuple
        containing (xmin, xmax, ymin, ymax, zmin, zmax). This method will
        clear the array by default.  To append ids to an array, set
        clear_array to false.
        """
        my_args = deref_array(args, [('tuple', 'vtkIdTypeArray', 'bool')])
        ret = self._wrap_call(self._vtk_obj.FindPointsInArea, *my_args)
        return ret

    _updateable_traits_ = \
    (('automatic', 'GetAutomatic'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('create_cubic_octants', 'GetCreateCubicOctants'), ('fudge_factor',
    'GetFudgeFactor'), ('maximum_points_per_region',
    'GetMaximumPointsPerRegion'), ('max_level', 'GetMaxLevel'),
    ('tolerance', 'GetTolerance'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['automatic', 'debug', 'global_warning_display',
    'create_cubic_octants', 'fudge_factor', 'max_level',
    'maximum_points_per_region', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OctreePointLocator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OctreePointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic'], [], ['create_cubic_octants', 'fudge_factor',
            'max_level', 'maximum_points_per_region', 'tolerance']),
            title='Edit OctreePointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OctreePointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


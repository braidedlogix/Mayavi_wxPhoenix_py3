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


class OctreePointLocatorNode(Object):
    """
    OctreePointLocatorNode - Octree node that has 8 children each of
    equal size
    
    Superclass: Object
    
    This class represents a single spatial region in a 3d axis octant
    partitioning.  It is intended to work efficiently with the
    OctreePointLocator and is not meant for general use.  It is
    assumed the region bounds some set of points.  The ordering of the
    children is
    (-x,-y,-z),(+x,-y,-z),(-x,+y,-z),(+x,+y,-z),(-x,-y,+z),(+x,-y,+z),
    (-x,+y,+z),(+x,+y,+z).  The portion of the domain assigned to an
    octant is Min < x <= Max.
    
    @sa
    OctreePointLocator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOctreePointLocatorNode, obj, update, **traits)
    
    def get_bounds(self, *args):
        """
        V.get_bounds([float, ...])
        C++: void GetBounds(double *b)
        Set/Get the bounds of the spatial region represented by this
        node. Caller allocates storage for 6-vector in get_bounds.
        """
        ret = self._wrap_call(self._vtk_obj.GetBounds, *args)
        return ret

    def set_bounds(self, *args):
        """
        V.set_bounds(float, float, float, float, float, float)
        C++: void SetBounds(double xMin, double xMax, double yMin,
            double yMax, double zMin, double zMax)
        V.set_bounds((float, float, float, float, float, float))
        C++: void SetBounds(const double b[6])
        Set/Get the bounds of the spatial region represented by this
        node. Caller allocates storage for 6-vector in get_bounds.
        """
        ret = self._wrap_call(self._vtk_obj.SetBounds, *args)
        return ret

    def get_data_bounds(self, *args):
        """
        V.get_data_bounds([float, ...])
        C++: void GetDataBounds(double *b)
        Set/Get the bounds of the points contained in this spatial
        region. This may be smaller than the bounds of the region itself.
        Caller allocates storage for 6-vector in get_data_bounds.
        """
        ret = self._wrap_call(self._vtk_obj.GetDataBounds, *args)
        return ret

    def set_data_bounds(self, *args):
        """
        V.set_data_bounds(float, float, float, float, float, float)
        C++: void SetDataBounds(double xMin, double xMax, double yMin,
            double yMax, double zMin, double zMax)
        Set/Get the bounds of the points contained in this spatial
        region. This may be smaller than the bounds of the region itself.
        Caller allocates storage for 6-vector in get_data_bounds.
        """
        ret = self._wrap_call(self._vtk_obj.SetDataBounds, *args)
        return ret

    max_bounds = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Set the xmax, ymax and zmax value of the bounds of this region
        """
    )

    def _max_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxBounds,
                        self.max_bounds)

    max_data_bounds = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Set the xmax, ymax and zmax value of the bounds of this data
        within this region.
        """
    )

    def _max_data_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxDataBounds,
                        self.max_data_bounds)

    min_bounds = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Set the xmin, ymin and zmin value of the bounds of this region
        """
    )

    def _min_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinBounds,
                        self.min_bounds)

    min_data_bounds = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Set the xmin, ymin and zmin value of the bounds of this data
        within this region.
        """
    )

    def _min_data_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinDataBounds,
                        self.min_data_bounds)

    number_of_points = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of points contained in this region.
        """
    )

    def _number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPoints,
                        self.number_of_points)

    def get_child(self, *args):
        """
        V.get_child(int) -> OctreePointLocatorNode
        C++: OctreePointLocatorNode *GetChild(int i)
        Get a pointer to the ith child of this node.
        """
        ret = self._wrap_call(self._vtk_obj.GetChild, *args)
        return wrap_vtk(ret)

    def get_distance2_to_boundary(self, *args):
        """
        V.get_distance2_to_boundary(float, float, float,
            OctreePointLocatorNode, int) -> float
        C++: double GetDistance2ToBoundary(double x, double y, double z,
            OctreePointLocatorNode *top, int useDataBounds)
        V.get_distance2_to_boundary(float, float, float, [float, ...],
            OctreePointLocatorNode, int) -> float
        C++: double GetDistance2ToBoundary(double x, double y, double z,
            double *boundaryPt, OctreePointLocatorNode *top,
            int useDataBounds)
        Calculate the distance squared from any point to the boundary of
        this region.  Use the boundary of the points within the region if
        use_data_bounds is non-zero.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetDistance2ToBoundary, *my_args)
        return ret

    def get_distance2_to_inner_boundary(self, *args):
        """
        V.get_distance2_to_inner_boundary(float, float, float,
            OctreePointLocatorNode) -> float
        C++: double GetDistance2ToInnerBoundary(double x, double y,
            double z, OctreePointLocatorNode *top)
        Calculate the distance from the specified point (which is
        required to be inside this spatial region) to an interior
        boundary.  An interior boundary is one that is not also an
        boundary of the entire space partitioned by the tree of
        OctreePointLocatorNode's.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetDistance2ToInnerBoundary, *my_args)
        return ret

    def _get_id(self):
        return self._vtk_obj.GetID()
    id = traits.Property(_get_id, help=\
        """
        Get the ID associated with the region described by this node.  If
        this is not a leaf node, this value should be -1.
        """
    )

    def _get_min_id(self):
        return self._vtk_obj.GetMinID()
    min_id = traits.Property(_get_min_id, help=\
        """
        If this node is not a leaf node, there are leaf nodes below it
        whose regions represent a partitioning of this region.  The IDs
        of these leaf nodes form a contigous set.  Get the first of the
        first point's ID that is contained in this node.
        """
    )

    def get_sub_octant_index(self, *args):
        """
        V.get_sub_octant_index([float, ...], int) -> int
        C++: int GetSubOctantIndex(double *point, int CheckContainment)
        Return the id of the suboctant that a given point is in. If
        check_containment is non-zero then it checks whether the point is
        in the actual bounding box of the suboctant, otherwise it only
        checks which octant the point is in that is created from the
        axis-aligned partitioning of the domain at this octant's center.
        """
        ret = self._wrap_call(self._vtk_obj.GetSubOctantIndex, *args)
        return ret

    def compute_octree_node_information(self, *args):
        """
        V.compute_octree_node_information(OctreePointLocatorNode, int,
            int, [float, ...])
        C++: void ComputeOctreeNodeInformation(
            OctreePointLocatorNode *Parent, int &NextLeafId,
            int &NextMinId, float *coordinates)
        Recursive function to compute ID, min_val, max_val, and min_id.
        Parent is used for min_val and max_val in the case that no points
        are in the leaf node.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeOctreeNodeInformation, *my_args)
        return ret

    def contains_point(self, *args):
        """
        V.contains_point(float, float, float, int) -> int
        C++: int ContainsPoint(double x, double y, double z,
            int useDataBounds)
        Return 1 if this spatial region entirely contains the given
        point. Use the possibly smaller bounds of the points within the
        region if use_data_bounds is non-zero.
        """
        ret = self._wrap_call(self._vtk_obj.ContainsPoint, *args)
        return ret

    def create_child_nodes(self):
        """
        V.create_child_nodes()
        C++: void CreateChildNodes()
        Add the 8 children.
        """
        ret = self._vtk_obj.CreateChildNodes()
        return ret
        

    def delete_child_nodes(self):
        """
        V.delete_child_nodes()
        C++: void DeleteChildNodes()
        Delete the 8 children.
        """
        ret = self._vtk_obj.DeleteChildNodes()
        return ret
        

    def intersects_region(self, *args):
        """
        V.intersects_region(PlanesIntersection, int) -> int
        C++: int IntersectsRegion(PlanesIntersection *pi,
            int useDataBounds)
        A PlanesIntersection object represents a convex 3d region
        bounded by planes, and it is capable of computing intersections
        of boxes with itself.  Return 1 if this spatial region intersects
        the spatial region described by the PlanesIntersection object.
        Use the possibly smaller bounds of the points within the region
        if use_data_bounds is non-zero.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IntersectsRegion, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_points', 'GetNumberOfPoints'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'number_of_points'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OctreePointLocatorNode, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OctreePointLocatorNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['number_of_points']),
            title='Edit OctreePointLocatorNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OctreePointLocatorNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


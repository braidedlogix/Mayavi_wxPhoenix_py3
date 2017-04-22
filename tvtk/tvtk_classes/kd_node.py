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


class KdNode(Object):
    """
    KdNode - This class represents a single spatial region
        in an 3d axis aligned binary spatial partitioning.
    
    Superclass: Object
    
    It is assumed
        the region bounds some set of points.  Regions are represented
        as nodes in a binary tree.
    
    @sa
         KdTree OBSPCuts
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkKdNode, obj, update, **traits)
    
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
        C++: void SetBounds(double x1, double x2, double y1, double y2,
            double z1, double z2)
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
        C++: void SetDataBounds(double x1, double x2, double y1,
            double y2, double z1, double z2)
        V.set_data_bounds([float, ...])
        C++: void SetDataBounds(float *v)
        Set/Get the bounds of the points contained in this spatial
        region. This may be smaller than the bounds of the region itself.
        Caller allocates storage for 6-vector in get_data_bounds.
        """
        ret = self._wrap_call(self._vtk_obj.SetDataBounds, *args)
        return ret

    dim = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Set/Get the dimension along which this region is divided. (0 - x,
        1 - y, 2 - z, 3 - leaf node (default)).
        """
    )

    def _dim_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDim,
                        self.dim)

    id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the ID associated with the region described by this node.
         If this is not a leaf node, this value should be -1.
        """
    )

    def _id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetID,
                        self.id)

    def _get_left(self):
        return wrap_vtk(self._vtk_obj.GetLeft())
    def _set_left(self, arg):
        old_val = self._get_left()
        self._wrap_call(self._vtk_obj.SetLeft,
                        deref_vtk(arg))
        self.trait_property_changed('left', old_val, arg)
    left = traits.Property(_get_left, _set_left, help=\
        """
        Set/Get a pointer to the left child of this node.
        """
    )

    max_bounds = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set the xmax, ymax and zmax value of the bounds of this region
        """
    )

    def _max_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxBounds,
                        self.max_bounds)

    max_data_bounds = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set the xmax, ymax and zmax value of the bounds of this data
        within this region
        """
    )

    def _max_data_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxDataBounds,
                        self.max_data_bounds)

    max_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        If this node is not a leaf node, there are leaf nodes below it
        whose regions represent a partitioning of this region.  The IDs
        of these leaf nodes form a contigous set.  Set/Get the range of
        the IDs of the leaf nodes below this node.  If this is already a
        leaf node, these values should be the same as the ID.
        """
    )

    def _max_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxID,
                        self.max_id)

    min_bounds = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set the xmin, ymin and zmin value of the bounds of this region
        """
    )

    def _min_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinBounds,
                        self.min_bounds)

    min_data_bounds = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set the xmin, ymin and zmin value of the bounds of this data
        within this region
        """
    )

    def _min_data_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinDataBounds,
                        self.min_data_bounds)

    min_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        If this node is not a leaf node, there are leaf nodes below it
        whose regions represent a partitioning of this region.  The IDs
        of these leaf nodes form a contigous set.  Set/Get the range of
        the IDs of the leaf nodes below this node.  If this is already a
        leaf node, these values should be the same as the ID.
        """
    )

    def _min_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinID,
                        self.min_id)

    number_of_points = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of points contained in this region.
        """
    )

    def _number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPoints,
                        self.number_of_points)

    def _get_right(self):
        return wrap_vtk(self._vtk_obj.GetRight())
    def _set_right(self, arg):
        old_val = self._get_right()
        self._wrap_call(self._vtk_obj.SetRight,
                        deref_vtk(arg))
        self.trait_property_changed('right', old_val, arg)
    right = traits.Property(_get_right, _set_right, help=\
        """
        Set/Get a pointer to the right child of this node.
        """
    )

    def _get_up(self):
        return wrap_vtk(self._vtk_obj.GetUp())
    def _set_up(self, arg):
        old_val = self._get_up()
        self._wrap_call(self._vtk_obj.SetUp,
                        deref_vtk(arg))
        self.trait_property_changed('up', old_val, arg)
    up = traits.Property(_get_up, _set_up, help=\
        """
        Set/Get a pointer to the parent of this node.
        """
    )

    def get_distance2_to_boundary(self, *args):
        """
        V.get_distance2_to_boundary(float, float, float, int) -> float
        C++: double GetDistance2ToBoundary(double x, double y, double z,
            int useDataBounds)
        V.get_distance2_to_boundary(float, float, float, [float, ...], int)
            -> float
        C++: double GetDistance2ToBoundary(double x, double y, double z,
            double *boundaryPt, int useDataBounds)
        Calculate the distance squared from any point to the boundary of
        this region.  Use the boundary of the points within the region if
        use_data_bounds is non-zero.
        """
        ret = self._wrap_call(self._vtk_obj.GetDistance2ToBoundary, *args)
        return ret

    def get_distance2_to_inner_boundary(self, *args):
        """
        V.get_distance2_to_inner_boundary(float, float, float) -> float
        C++: double GetDistance2ToInnerBoundary(double x, double y,
            double z)
        Calculate the distance from the specified point (which is
        required to be inside this spatial region) to an interior
        boundary.  An interior boundary is one that is not also an
        boundary of the entire space partitioned by the tree of
        KdNode's.
        """
        ret = self._wrap_call(self._vtk_obj.GetDistance2ToInnerBoundary, *args)
        return ret

    def _get_division_position(self):
        return self._vtk_obj.GetDivisionPosition()
    division_position = traits.Property(_get_division_position, help=\
        """
        Get the location of the division plane along the axis the region
        is divided.  See also get_dim().  The result is undertermined if
        this node is not divided (a leaf node).
        """
    )

    def add_child_nodes(self, *args):
        """
        V.add_child_nodes(KdNode, KdNode)
        C++: void AddChildNodes(KdNode *left, KdNode *right)
        Add the left and right children.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddChildNodes, *my_args)
        return ret

    def contains_box(self, *args):
        """
        V.contains_box(float, float, float, float, float, float, int)
            -> int
        C++: int ContainsBox(double x1, double x2, double y1, double y2,
            double z1, double z2, int useDataBounds)
        Return 1 if this spatial region entirely contains a box specified
        by it's bounds. Use the possibly smaller bounds of the points
        within the region if use_data_bounds is non-zero.
        """
        ret = self._wrap_call(self._vtk_obj.ContainsBox, *args)
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

    def delete_child_nodes(self):
        """
        V.delete_child_nodes()
        C++: void DeleteChildNodes()
        Delete the left and right children.
        """
        ret = self._vtk_obj.DeleteChildNodes()
        return ret
        

    def intersects_box(self, *args):
        """
        V.intersects_box(float, float, float, float, float, float, int)
            -> int
        C++: int IntersectsBox(double x1, double x2, double y1, double y2,
             double z1, double z2, int useDataBounds)
        Return 1 if this spatial region intersects the axis-aligned box
        given by the bounds passed in.  Use the possibly smaller bounds
        of the points within the region if use_data_bounds is non-zero.
        """
        ret = self._wrap_call(self._vtk_obj.IntersectsBox, *args)
        return ret

    def intersects_cell(self, *args):
        """
        V.intersects_cell(Cell, int, int, [float, ...]) -> int
        C++: int IntersectsCell(Cell *cell, int useDataBounds,
            int cellRegion=-1, double *cellBounds=NULL)
        Return 1 if the cell specified intersects this region.  If you
        already know the ID of the region containing the cell's centroid,
        provide that as an argument.  If you already know the bounds of
        the cell, provide that as well, in the form of
        xmin,xmax,ymin,ymax,zmin, zmax.  Either of these may speed the
        calculation. Use the possibly smaller bounds of the points within
        the region if use_data_bounds is non-zero.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IntersectsCell, *my_args)
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

    def intersects_sphere2(self, *args):
        """
        V.intersects_sphere2(float, float, float, float, int) -> int
        C++: int IntersectsSphere2(double x, double y, double z,
            double rSquared, int useDataBounds)
        Return 1 if this spatial region intersects a sphere described by
        it's center and the square of it's radius. Use the possibly
        smaller bounds of the points within the region if use_data_bounds
        is non-zero.
        """
        ret = self._wrap_call(self._vtk_obj.IntersectsSphere2, *args)
        return ret

    def print_node(self, *args):
        """
        V.print_node(int)
        C++: void PrintNode(int depth)
        For debugging purposes, print out this node.
        """
        ret = self._wrap_call(self._vtk_obj.PrintNode, *args)
        return ret

    def print_verbose_node(self, *args):
        """
        V.print_verbose_node(int)
        C++: void PrintVerboseNode(int depth)
        For debugging purposes, print out this node.
        """
        ret = self._wrap_call(self._vtk_obj.PrintVerboseNode, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('dim', 'GetDim'), ('id', 'GetID'),
    ('max_bounds', 'GetMaxBounds'), ('max_data_bounds',
    'GetMaxDataBounds'), ('max_id', 'GetMaxID'), ('min_bounds',
    'GetMinBounds'), ('min_data_bounds', 'GetMinDataBounds'), ('min_id',
    'GetMinID'), ('number_of_points', 'GetNumberOfPoints'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'dim', 'id', 'max_bounds',
    'max_data_bounds', 'max_id', 'min_bounds', 'min_data_bounds',
    'min_id', 'number_of_points'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(KdNode, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit KdNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['dim', 'id', 'max_bounds', 'max_data_bounds', 'max_id',
            'min_bounds', 'min_data_bounds', 'min_id', 'number_of_points']),
            title='Edit KdNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit KdNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


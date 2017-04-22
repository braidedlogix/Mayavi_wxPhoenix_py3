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

from tvtk.tvtk_classes.data_object import DataObject


class BSPCuts(DataObject):
    """
    BSPCuts - This class represents an axis-aligned Binary Spatial
       Partitioning of a 3d space.
    
    Superclass: DataObject
    
    This class converts between the KdTree
       representation of a tree of KdNodes (used by
    DistributedDataFilter)
       and a compact array representation that might be provided by a
       graph partitioning library like Zoltan.  Such a representation
       could be used in message passing.
    
    @sa
         KdTree KdNode DistributedDataFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBSPCuts, obj, update, **traits)
    
    def get_arrays(self, *args):
        """
        V.get_arrays(int, [int, ...], [float, ...], [int, ...], [int, ...],
             [float, ...], [float, ...], [int, ...]) -> int
        C++: int GetArrays(int len, int *dim, double *coord, int *lower,
            int *upper, double *lowerDataCoord, double *upperDataCoord,
            int *npoints)
        Get the arrays representing the cuts in the partitioning.
        """
        ret = self._wrap_call(self._vtk_obj.GetArrays, *args)
        return ret

    def _get_kd_node_tree(self):
        return wrap_vtk(self._vtk_obj.GetKdNodeTree())
    kd_node_tree = traits.Property(_get_kd_node_tree, help=\
        """
        Return a tree of KdNode's representing the cuts specified in
        this object.  This is our copy, don't delete it.
        """
    )

    def _get_number_of_cuts(self):
        return self._vtk_obj.GetNumberOfCuts()
    number_of_cuts = traits.Property(_get_number_of_cuts, help=\
        """
        Get the number of cuts in the partitioning, which also the size
        of the arrays in the array representation of the partitioning.
        """
    )

    def create_cuts(self, *args):
        """
        V.create_cuts([float, ...], int, [int, ...], [float, ...], [int,
            ...], [int, ...], [float, ...], [float, ...], [int, ...])
        C++: void CreateCuts(double *bounds, int ncuts, int *dim,
            double *coord, int *lower, int *upper, double *lowerDataCoord,
             double *upperDataCoord, int *npoints)
        V.create_cuts(KdNode)
        C++: void CreateCuts(KdNode *kd)
        Initialize the cuts with arrays of information.  This type of
        information would be obtained from a graph partitioning software
        package like Zoltan.
        
        * bounds - the bounds (xmin, xmax, ymin, ymax, zmin, zmax) of the
        * space being partitioned
        * ncuts - the number cuts, also the size of the following arrays
        * dim   - the dimension along which the cut is made (x/y/z -
          0/1/2)
        * coord - the location of the cut along the axis
        * lower - array index for the lower region bounded by the cut
        * upper - array index for the upper region bounded by the cut
        * lower_data_coord - optional upper bound of the data in the lower
          region
        * upper_data_coord - optional lower bound of the data in the upper
          region
        * npoints - optional number of points in the spatial region
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CreateCuts, *my_args)
        return ret

    def equals(self, *args):
        """
        V.equals(BSPCuts, float) -> int
        C++: int Equals(BSPCuts *other, double tolerance=0.0)
        Compare these cuts with those of the other tree.  Returns true if
        the two trees are the same.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Equals, *my_args)
        return ret

    def print_arrays(self):
        """
        V.print_arrays()
        C++: void PrintArrays()"""
        ret = self._vtk_obj.PrintArrays()
        return ret
        

    def print_tree(self):
        """
        V.print_tree()
        C++: void PrintTree()"""
        ret = self._vtk_obj.PrintTree()
        return ret
        

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BSPCuts, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BSPCuts properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit BSPCuts properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BSPCuts properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class HyperTree(Object):
    """
    HyperTree - An object structured as a tree where each node has
    exactly either 2^n or 3^n children.
    
    Superclass: Object
    
    An hypertree is a dataset where each node has either exactly 2^n or
    3^n children or no child at all if the node is a leaf. `n' is the
    dimension of the dataset (1 (binary tree), 2 (quadtree) or 3 (octree)
    ). The class name comes from the following paper:
    
    
     @ARTICLE{yau-srihari-1983,
      author={Mann-May Yau and Sargur N. Srihari},
      title={A Hierarchical Data Structure for Multidimensional Digital Images},
      journal={Communications of the ACM},
      month={July},
      year={1983},
      volume={26},
      number={7},
      pages={504--515}
      }
     
    
    Each node is a cell. Attributes are associated with cells, not with
    points. The geometry is implicitly given by the size of the root node
    on each axis and position of the center and the orientation. (TODO:
    review center position and orientation). The geometry is then not
    limited to an hybercube but can have a rectangular shape. Attributes
    are associated with leaves. For LOD (Level-Of-Detail) purpose,
    attributes can be computed on none-leaf nodes by computing the
    average values from its children (which can be leaves or not).
    
    By construction, an hypertree is efficient in memory usage when the
    geometry is sparse. The LOD feature allows to cull quickly part of
    the dataset.
    
    This is an abstract class used as a superclass by a templated compact
    class. All methods are pure virtual. This is done to hide templates.
    
    @par Case with 2^n children:
    * 3d case (octree) for each node, each child index (from 0 to 7) is
      encoded in the following orientation. It is easy to access each
      child as a cell of a grid. Note also that the binary representation
    is relevant, each bit code a side: bit 0 encodes -x side (0) or +x
      side (1) bit 1 encodes -y side (0) or +y side (1) bit 2 encodes -z
      side (0) or +z side (2)
    - the -z side first
    - 0: -y -x sides
    - 1: -y +x sides
    - 2: +y -x sides
    - 3: +y +x sides
                  +y
     +-+-+        ^
     |2|3|        |
     +-+-+  O +z  +-> +x
     |0|1|
     +-+-+
     
    
    @par Case with 2^n children:
    - then the +z side, in counter-clockwise
    - 4: -y -x sides
    - 5: -y +x sides
    - 6: +y -x sides
    - 7: +y +x sides
                  +y
     +-+-+        ^
     |6|7|        |
     +-+-+  O +z  +-> +x
     |4|5|
     +-+-+
     
    
    @par Case with 2^n children: The cases with fewer dimensions are
    consistent with the octree case:
    
    @par Case with 2^n children:
    * Quadtree: in counter-clockwise
    - 0: -y -x edges
    - 1: -y +x edges
    - 2: +y -x edges
    - 3: +y +x edges
             +y
     +-+-+   ^
     |2|3|   |
     +-+-+  O+-> +x
     |0|1|
     +-+-+
     
    
    @par Case with 2^n children:
    * Binary tree:
     +0+1+  O+-> +x
     
    
    @warning
    It is not a spatial search object. If you are looking for this kind
    of octree see CellLocator instead.
    
    @par Thanks: This class was written by Philippe Pebay, Joachim
    Pouderoux and Charles Law, Kitware 2013 This work was supported in
    part by Commissariat a l'Energie Atomique (CEA/DIF)
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHyperTree, obj, update, **traits)
    
    def get_global_index_from_local(self, *args):
        """
        V.get_global_index_from_local(int) -> int
        C++: virtual IdType GetGlobalIndexFromLocal(IdType local)
        Get the global id of a local node. Use the mapping function if
        available or the start global index.
        """
        ret = self._wrap_call(self._vtk_obj.GetGlobalIndexFromLocal, *args)
        return ret

    def set_global_index_from_local(self, *args):
        """
        V.set_global_index_from_local(int, int)
        C++: virtual void SetGlobalIndexFromLocal(IdType local,
            IdType global)
        Set the mapping between local & global ids used by
        hyper_tree_grids.
        """
        ret = self._wrap_call(self._vtk_obj.SetGlobalIndexFromLocal, *args)
        return ret

    def get_scale(self, *args):
        """
        V.get_scale([float, float, float])
        C++: virtual void GetScale(double[3])
        V.get_scale(int) -> float
        C++: virtual double GetScale(unsigned int)"""
        ret = self._wrap_call(self._vtk_obj.GetScale, *args)
        return ret

    def set_scale(self, *args):
        """
        V.set_scale([float, float, float])
        C++: virtual void SetScale(double[3])"""
        ret = self._wrap_call(self._vtk_obj.SetScale, *args)
        return ret

    def _get_actual_memory_size(self):
        return self._vtk_obj.GetActualMemorySize()
    actual_memory_size = traits.Property(_get_actual_memory_size, help=\
        """
        Return the actual memory size in kibibytes (1024 bytes). NB:
        Ignores the attribute array.
        """
    )

    def _get_branch_factor(self):
        return self._vtk_obj.GetBranchFactor()
    branch_factor = traits.Property(_get_branch_factor, help=\
        """
        
        """
    )

    def _get_dimension(self):
        return self._vtk_obj.GetDimension()
    dimension = traits.Property(_get_dimension, help=\
        """
        
        """
    )

    def _get_number_of_index(self):
        return self._vtk_obj.GetNumberOfIndex()
    number_of_index = traits.Property(_get_number_of_index, help=\
        """
        
        """
    )

    def _get_number_of_leaves(self):
        return self._vtk_obj.GetNumberOfLeaves()
    number_of_leaves = traits.Property(_get_number_of_leaves, help=\
        """
        
        """
    )

    def _get_number_of_levels(self):
        return self._vtk_obj.GetNumberOfLevels()
    number_of_levels = traits.Property(_get_number_of_levels, help=\
        """
        Return the number of levels.
        \post result_greater_or_equal_to_one: result>=1
        """
    )

    def _get_number_of_nodes(self):
        return self._vtk_obj.GetNumberOfNodes()
    number_of_nodes = traits.Property(_get_number_of_nodes, help=\
        """
        
        """
    )

    def create_instance(self, *args):
        """
        V.create_instance(int, int) -> HyperTree
        C++: static HyperTree *CreateInstance(
            unsigned int branchFactor, unsigned int dimension)
        Return an instance of a templated hypertree for given branch
        factor and dimension This is done to hide templates.
        """
        ret = self._wrap_call(self._vtk_obj.CreateInstance, *args)
        return wrap_vtk(ret)

    def find_child_parameters(self, *args):
        """
        V.find_child_parameters(int, int, bool)
        C++: virtual void FindChildParameters(int, IdType &, bool &)
        Find the Index, Parent Index and is_leaf() parameters of a child
        for hypertree. This is done to hide templates.
        """
        ret = self._wrap_call(self._vtk_obj.FindChildParameters, *args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()"""
        ret = self._vtk_obj.Initialize()
        return ret
        

    def new_cursor(self):
        """
        V.new_cursor() -> HyperTreeCursor
        C++: virtual HyperTreeCursor *NewCursor()"""
        ret = wrap_vtk(self._vtk_obj.NewCursor())
        return ret
        

    def set_global_index_start(self, *args):
        """
        V.set_global_index_start(int)
        C++: virtual void SetGlobalIndexStart(IdType)
        Set the start global index for the current tree. The global index
        of a node will be this index + the node index.
        """
        ret = self._wrap_call(self._vtk_obj.SetGlobalIndexStart, *args)
        return ret

    def subdivide_leaf(self, *args):
        """
        V.subdivide_leaf(HyperTreeCursor)
        C++: virtual void SubdivideLeaf(HyperTreeCursor *leaf)
        Subdivide node pointed by cursor, only if its a leaf. At the end,
        cursor points on the node that used to be leaf.
        \pre leaf_exists: leaf!=0
        \pre is_a_leaf: leaf->_current_is_leaf()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SubdivideLeaf, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('global_index_from_local',
    'GetGlobalIndexFromLocal'), ('scale', 'GetScale'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'global_index_from_local',
    'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HyperTree, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HyperTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['global_index_from_local', 'scale']),
            title='Edit HyperTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HyperTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


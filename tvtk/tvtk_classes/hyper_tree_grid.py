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

from tvtk.tvtk_classes.data_set import DataSet


class HyperTreeGrid(DataSet):
    """
    HyperTreeGrid - A dataset containing a grid of HyperTree
    instances arranged as a rectilinear grid.
    
    Superclass: DataSet
    
    An hypertree grid is a dataset containing a rectilinear grid of root
    nodes, each of which can be refined as a HyperTree grid. This
    organization of the root nodes allows for the definition of
    tree-based AMR grids that do not have uniform geometry. Some filters
    can be applied on this dataset: contour, outline, geometry.
    
    @warning
    It is not a spatial search object. If you are looking for this kind
    of octree see CellLocator instead. Extent support is not finished
    yet.
    
    @sa
    HyperTree RectilinearGrid
    
    @par Thanks: This class was written by Philippe Pebay, Joachim
    Pouderoux and Charles Law, Kitware 2013 This work was supported in
    part by Commissariat a l'Energie Atomique (CEA/DIF)
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHyperTreeGrid, obj, update, **traits)
    
    branch_factor = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set/Get the subdivision factor in the grid refinement scheme NB:
        Can only be 2 or 3
        """
    )

    def _branch_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBranchFactor,
                        self.branch_factor)

    dimension = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the dimensionality of the grid NB: Can only be 1, 2 or 3
        """
    )

    def _dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimension,
                        self.dimension)

    grid_size = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(0, 0, 0), cols=3, help=\
        """
        Set/Get sizes of this rectilinear grid dataset
        """
    )

    def _grid_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridSize,
                        self.grid_size)

    def _get_material_mask(self):
        return wrap_vtk(self._vtk_obj.GetMaterialMask())
    def _set_material_mask(self, arg):
        old_val = self._get_material_mask()
        my_arg = deref_array([arg], [['vtkBitArray']])
        self._wrap_call(self._vtk_obj.SetMaterialMask,
                        my_arg[0])
        self.trait_property_changed('material_mask', old_val, arg)
    material_mask = traits.Property(_get_material_mask, _set_material_mask, help=\
        """
        Specify the blanking mask of primal leaf cells
        """
    )

    def _get_material_mask_index(self):
        return wrap_vtk(self._vtk_obj.GetMaterialMaskIndex())
    def _set_material_mask_index(self, arg):
        old_val = self._get_material_mask_index()
        my_arg = deref_array([arg], [['vtkIdTypeArray']])
        self._wrap_call(self._vtk_obj.SetMaterialMaskIndex,
                        my_arg[0])
        self.trait_property_changed('material_mask_index', old_val, arg)
    material_mask_index = traits.Property(_get_material_mask_index, _set_material_mask_index, help=\
        """
        Specify the visibility mask of primal leaf cells
        """
    )

    transposed_root_indexing = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Specify whether indexing mode of grid root cells must be
        transposed to x-axis first, z-axis last, instead of the default
        z-axis first, k-axis last
        """
    )

    def _transposed_root_indexing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTransposedRootIndexing,
                        self.transposed_root_indexing)

    def _get_x_coordinates(self):
        return wrap_vtk(self._vtk_obj.GetXCoordinates())
    def _set_x_coordinates(self, arg):
        old_val = self._get_x_coordinates()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetXCoordinates,
                        my_arg[0])
        self.trait_property_changed('x_coordinates', old_val, arg)
    x_coordinates = traits.Property(_get_x_coordinates, _set_x_coordinates, help=\
        """
        Specify the grid coordinates in the x-direction.
        """
    )

    def _get_y_coordinates(self):
        return wrap_vtk(self._vtk_obj.GetYCoordinates())
    def _set_y_coordinates(self, arg):
        old_val = self._get_y_coordinates()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetYCoordinates,
                        my_arg[0])
        self.trait_property_changed('y_coordinates', old_val, arg)
    y_coordinates = traits.Property(_get_y_coordinates, _set_y_coordinates, help=\
        """
        Specify the grid coordinates in the y-direction.
        """
    )

    def _get_z_coordinates(self):
        return wrap_vtk(self._vtk_obj.GetZCoordinates())
    def _set_z_coordinates(self, arg):
        old_val = self._get_z_coordinates()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetZCoordinates,
                        my_arg[0])
        self.trait_property_changed('z_coordinates', old_val, arg)
    z_coordinates = traits.Property(_get_z_coordinates, _set_z_coordinates, help=\
        """
        Specify the grid coordinates in the z-direction.
        """
    )

    def get_level_zero_coords_from_index(self, *args):
        """
        V.get_level_zero_coords_from_index(int, int, int, int)
        C++: void GetLevelZeroCoordsFromIndex(IdType index,
            unsigned int &i, unsigned int &j, unsigned int &k)
        Convert a level 0 index to its ijk coordinates according the grid
        size.
        """
        ret = self._wrap_call(self._vtk_obj.GetLevelZeroCoordsFromIndex, *args)
        return ret

    def _get_number_of_children(self):
        return self._vtk_obj.GetNumberOfChildren()
    number_of_children = traits.Property(_get_number_of_children, help=\
        """
        The number of children each node can have.
        """
    )

    def _get_number_of_leaves(self):
        return self._vtk_obj.GetNumberOfLeaves()
    number_of_leaves = traits.Property(_get_number_of_leaves, help=\
        """
        Get the number of leaves in the primal tree grid.
        """
    )

    def get_number_of_levels(self, *args):
        """
        V.get_number_of_levels(int) -> int
        C++: IdType GetNumberOfLevels(IdType)
        Return the number of levels in an individual (primal) tree
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfLevels, *args)
        return ret

    def _get_number_of_trees(self):
        return self._vtk_obj.GetNumberOfTrees()
    number_of_trees = traits.Property(_get_number_of_trees, help=\
        """
        Return the number of trees in the level 0 grid.
        """
    )

    def DIMENSION(self):
        """
        V.dimension() -> InformationIntegerKey
        C++: static InformationIntegerKey *DIMENSION()"""
        ret = wrap_vtk(self._vtk_obj.DIMENSION())
        return ret
        

    def generate_super_cursor_traversal_table(self):
        """
        V.generate_super_cursor_traversal_table()
        C++: void GenerateSuperCursorTraversalTable()
        Generate the table before calling initialize_super_cursor_child.
        """
        ret = self._vtk_obj.GenerateSuperCursorTraversalTable()
        return ret
        

    def generate_trees(self):
        """
        V.generate_trees()
        C++: virtual void GenerateTrees()
        This method must be called once the tree settings change
        """
        ret = self._vtk_obj.GenerateTrees()
        return ret
        

    def LEVELS(self):
        """
        V.levels() -> InformationIntegerKey
        C++: static InformationIntegerKey *LEVELS()"""
        ret = wrap_vtk(self._vtk_obj.LEVELS())
        return ret
        

    def new_cursor(self, *args):
        """
        V.new_cursor(int) -> HyperTreeCursor
        C++: HyperTreeCursor *NewCursor(IdType)
        Create a new cursor: an object that can traverse the cells of an
        individual hyper tree.
        \post result_exists: result!=0
        """
        ret = self._wrap_call(self._vtk_obj.NewCursor, *args)
        return wrap_vtk(ret)

    def SIZES(self):
        """
        V.sizes() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *SIZES()"""
        ret = wrap_vtk(self._vtk_obj.SIZES())
        return ret
        

    def set_grid_extent(self, *args):
        """
        V.set_grid_extent([int, int, int, int, int, int])
        C++: void SetGridExtent(int extent[6])
        V.set_grid_extent(int, int, int, int, int, int)
        C++: void SetGridExtent(int iMin, int iMax, int jMin, int jMax,
            int kMin, int kMax)
        Set/Get extent of this rectilinear grid dataset
        """
        ret = self._wrap_call(self._vtk_obj.SetGridExtent, *args)
        return ret

    def set_indexing_mode_to_ijk(self):
        """
        V.set_indexing_mode_to_ijk()
        C++: void SetIndexingModeToIJK()
        Specify whether indexing mode of grid root cells must be
        transposed to x-axis first, z-axis last, instead of the default
        z-axis first, k-axis last
        """
        ret = self._vtk_obj.SetIndexingModeToIJK()
        return ret
        

    def set_indexing_mode_to_kji(self):
        """
        V.set_indexing_mode_to_kji()
        C++: void SetIndexingModeToKJI()
        Specify whether indexing mode of grid root cells must be
        transposed to x-axis first, z-axis last, instead of the default
        z-axis first, k-axis last
        """
        ret = self._vtk_obj.SetIndexingModeToKJI()
        return ret
        

    def subdivide_leaf(self, *args):
        """
        V.subdivide_leaf(HyperTreeCursor, int)
        C++: void SubdivideLeaf(HyperTreeCursor *, IdType)
        Subdivide node pointed by cursor, only if its a leaf. At the end,
        cursor points on the node that used to be leaf.
        \pre leaf_exists: leaf!=0
        \pre is_a_leaf: leaf->_current_is_leaf()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SubdivideLeaf, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('branch_factor', 'GetBranchFactor'), ('dimension', 'GetDimension'),
    ('grid_size', 'GetGridSize'), ('transposed_root_indexing',
    'GetTransposedRootIndexing'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'branch_factor', 'dimension', 'grid_size',
    'transposed_root_indexing'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HyperTreeGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HyperTreeGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], ['branch_factor', 'dimension',
            'grid_size', 'transposed_root_indexing']),
            title='Edit HyperTreeGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HyperTreeGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


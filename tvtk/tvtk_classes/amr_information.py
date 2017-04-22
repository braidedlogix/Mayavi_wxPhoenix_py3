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


class AMRInformation(Object):
    """
    AMRInformation - Meta data that describes the structure of an AMR
    data set
    
    Superclass: Object
    
    AMRInformation encaspulates the following meta information for an
    AMR data set
    - a list of AMRBox objects
    - Refinement ratio between AMR levels
    - Grid spacing for each level
    - The file block index for each block
    - parent child information, if requested
    
    @sa
    OverlappingAMR, AMRBox
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAMRInformation, obj, update, **traits)
    
    def get_amr_block_source_index(self, *args):
        """
        V.get_amr_block_source_index(int) -> int
        C++: int GetAMRBlockSourceIndex(int index)
        Get/Set the source_index of a block. Typically, this is a
        file-type specific index that can be used by a reader to load a
        particular file block
        """
        ret = self._wrap_call(self._vtk_obj.GetAMRBlockSourceIndex, *args)
        return ret

    def set_amr_block_source_index(self, *args):
        """
        V.set_amr_block_source_index(int, int)
        C++: void SetAMRBlockSourceIndex(int index, int sourceId)
        Get/Set the source_index of a block. Typically, this is a
        file-type specific index that can be used by a reader to load a
        particular file block
        """
        ret = self._wrap_call(self._vtk_obj.SetAMRBlockSourceIndex, *args)
        return ret

    def get_amr_box(self, *args):
        """
        V.get_amr_box(int, int) -> AMRBox
        C++: const AMRBox &GetAMRBox(unsigned int level,
            unsigned int id)
        Methods to set and get the AMR box at a given position
        """
        ret = self._wrap_call(self._vtk_obj.GetAMRBox, *args)
        return wrap_vtk(ret)

    def set_amr_box(self, *args):
        """
        V.set_amr_box(int, int, AMRBox)
        C++: void SetAMRBox(unsigned int level, unsigned int id,
            const AMRBox &box)
        Methods to set and get the AMR box at a given position
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetAMRBox, *my_args)
        return ret

    grid_description = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        returns the value of UniformGrid::GridDescription() of any
        block
        """
    )

    def _grid_description_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridDescription,
                        self.grid_description)

    origin = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Get the AMR dataset origin The origin is essentially the minimum
        of all the grids.
        """
    )

    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    def get_refinement_ratio(self, *args):
        """
        V.get_refinement_ratio(int) -> int
        C++: int GetRefinementRatio(unsigned int level)
        Returns the refinement of a given level.
        """
        ret = self._wrap_call(self._vtk_obj.GetRefinementRatio, *args)
        return ret

    def set_refinement_ratio(self, *args):
        """
        V.set_refinement_ratio(int, int)
        C++: void SetRefinementRatio(unsigned int level, int ratio)
        Set the refinement ratio at a level. This method should be called
        for all levels, if called at all.
        """
        ret = self._wrap_call(self._vtk_obj.SetRefinementRatio, *args)
        return ret

    def get_spacing(self, *args):
        """
        V.get_spacing(int, [float, float, float])
        C++: void GetSpacing(unsigned int level, double spacing[3])
        Return the spacing at the given fiven
        """
        ret = self._wrap_call(self._vtk_obj.GetSpacing, *args)
        return ret

    def set_spacing(self, *args):
        """
        V.set_spacing(int, (float, ...))
        C++: void SetSpacing(unsigned int level, const double *h)
        Set the spacing at a given level
        """
        ret = self._wrap_call(self._vtk_obj.SetSpacing, *args)
        return ret

    def _get_bounds(self):
        return self._vtk_obj.GetBounds()
    bounds = traits.Property(_get_bounds, help=\
        """
        Returns the bounds of the entire domain
        """
    )

    def get_children(self, *args):
        """
        V.get_children(int, int, int) -> (int, ...)
        C++: unsigned int *GetChildren(unsigned int level,
            unsigned int index, unsigned int &numChildren)
        Return a pointer to Children of a block.  The first entry is the
        number of children the block has followed by its childern ids in
        level+1. If none exits it returns NULL.
        """
        ret = self._wrap_call(self._vtk_obj.GetChildren, *args)
        return ret

    def get_coarsened_amr_box(self, *args):
        """
        V.get_coarsened_amr_box(int, int, AMRBox) -> bool
        C++: bool GetCoarsenedAMRBox(unsigned int level, unsigned int id,
            AMRBox &box)
        return the amr box coarsened to the previous level
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetCoarsenedAMRBox, *my_args)
        return ret

    def get_index(self, *args):
        """
        V.get_index(int, int) -> int
        C++: int GetIndex(unsigned int level, unsigned int id)
        Returns the single index from a pair of indices
        """
        ret = self._wrap_call(self._vtk_obj.GetIndex, *args)
        return ret

    def get_number_of_data_sets(self, *args):
        """
        V.get_number_of_data_sets(int) -> int
        C++: unsigned int GetNumberOfDataSets(unsigned int level)
        Returns the number of datasets at the given levelx
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfDataSets, *args)
        return ret

    def _get_number_of_levels(self):
        return self._vtk_obj.GetNumberOfLevels()
    number_of_levels = traits.Property(_get_number_of_levels, help=\
        """
        Return the number of levels
        """
    )

    def get_parents(self, *args):
        """
        V.get_parents(int, int, int) -> (int, ...)
        C++: unsigned int *GetParents(unsigned int level,
            unsigned int index, unsigned int &numParents)
        Return a pointer to Parents of a block.  The first entry is the
        number of parents the block has followed by its parent ids in
        level-1. If none exits it returns NULL.
        """
        ret = self._wrap_call(self._vtk_obj.GetParents, *args)
        return ret

    def _get_total_number_of_blocks(self):
        return self._vtk_obj.GetTotalNumberOfBlocks()
    total_number_of_blocks = traits.Property(_get_total_number_of_blocks, help=\
        """
        Returns total number of datasets
        """
    )

    def audit(self):
        """
        V.audit() -> bool
        C++: bool Audit()
        Checks whether the meta data is internally consistent.
        """
        ret = self._vtk_obj.Audit()
        return ret
        

    def compute_index_pair(self, *args):
        """
        V.compute_index_pair(int, int, int)
        C++: void ComputeIndexPair(unsigned int index,
            unsigned int &level, unsigned int &id)
        Returns the an index pair given a single index
        """
        ret = self._wrap_call(self._vtk_obj.ComputeIndexPair, *args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(AMRInformation)
        C++: void DeepCopy(AMRInformation *other)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def find_cell(self, *args):
        """
        V.find_cell([float, float, float], int, int, int) -> bool
        C++: bool FindCell(double q[3], unsigned int level,
            unsigned int index, int &cellIdx)
        Given a point q, find whether q is bounded by the data set at
        (level,index).  If it is, set cell_idx to the cell index and
        return true; otherwise return false
        """
        ret = self._wrap_call(self._vtk_obj.FindCell, *args)
        return ret

    def find_grid(self, *args):
        """
        V.find_grid([float, float, float], int, int) -> bool
        C++: bool FindGrid(double q[3], int level, unsigned int &gridId)
        V.find_grid([float, float, float], int, int) -> bool
        C++: bool FindGrid(double q[3], unsigned int &level,
            unsigned int &gridId)
        find the grid that contains the point q at the specified level
        """
        ret = self._wrap_call(self._vtk_obj.FindGrid, *args)
        return ret

    def generate_parent_child_information(self):
        """
        V.generate_parent_child_information()
        C++: void GenerateParentChildInformation()
        Generate the parent/child relationships - needed to be called
        before get_parents or get_children can be used!
        """
        ret = self._vtk_obj.GenerateParentChildInformation()
        return ret
        

    def generate_refinement_ratio(self):
        """
        V.generate_refinement_ratio()
        C++: void GenerateRefinementRatio()
        This method computes the refinement ratio at each level. At each
        level, l, the refinement ratio r_l is computed by r_l = D_{l} /
        D_{l+1}, where D_{l+1} and D_{l} are the grid spacings at the
        next and current level respectively.
        
        * .SECTION Assumptions
        * 1) Within each level, the refinement ratios are the same for
          all blocks.
        * 2) The refinement ratio is uniform along each dimension of the
          block.
        """
        ret = self._vtk_obj.GenerateRefinementRatio()
        return ret
        

    def has_children_information(self):
        """
        V.has_children_information() -> bool
        C++: bool HasChildrenInformation()
        Return whether parent child information has been generated
        """
        ret = self._vtk_obj.HasChildrenInformation()
        return ret
        

    def has_refinement_ratio(self):
        """
        V.has_refinement_ratio() -> bool
        C++: bool HasRefinementRatio()
        Returns Wether refinement ratio has been set (either by calling
        generate_refinement_ratio() or by calling set_refinement_ratio()
        """
        ret = self._vtk_obj.HasRefinementRatio()
        return ret
        

    def has_spacing(self, *args):
        """
        V.has_spacing(int) -> bool
        C++: bool HasSpacing(unsigned int level)"""
        ret = self._wrap_call(self._vtk_obj.HasSpacing, *args)
        return ret

    def initialize(self, *args):
        """
        V.initialize(int, (int, ...))
        C++: void Initialize(int numLevels, const int *blocksPerLevel)
        Initialize the meta information num_levels is the number of levels
        blocks_per_level[i] is the number of blocks at level i
        """
        ret = self._wrap_call(self._vtk_obj.Initialize, *args)
        return ret

    def print_parent_child_info(self, *args):
        """
        V.print_parent_child_info(int, int)
        C++: void PrintParentChildInfo(unsigned int level,
            unsigned int index)
        Prints the parents and children of a requested block (Debug
        Routine)
        """
        ret = self._wrap_call(self._vtk_obj.PrintParentChildInfo, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('grid_description',
    'GetGridDescription'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'grid_description'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AMRInformation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AMRInformation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['grid_description']),
            title='Edit AMRInformation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AMRInformation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


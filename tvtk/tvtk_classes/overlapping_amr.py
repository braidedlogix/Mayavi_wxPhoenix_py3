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

from tvtk.tvtk_classes.uniform_grid_amr import UniformGridAMR


class OverlappingAMR(UniformGridAMR):
    """
    OverlappingAMR - hierarchical dataset of UniformGrids
    
    Superclass: UniformGridAMR
    
    OverlappingAMR extends UniformGridAMR by exposing access to the
    amr meta data, which stores all structural information represented by
    an AMRInformation object
    
    @sa
    AMRInformation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOverlappingAMR, obj, update, **traits)
    
    def get_amr_block_source_index(self, *args):
        """
        V.get_amr_block_source_index(int, int) -> int
        C++: int GetAMRBlockSourceIndex(unsigned int level,
            unsigned int id)
        Set/Get the source id of a block. The source id is produced by an
        AMR source, e.g. a file reader might set this to be a file block
        id
        """
        ret = self._wrap_call(self._vtk_obj.GetAMRBlockSourceIndex, *args)
        return ret

    def set_amr_block_source_index(self, *args):
        """
        V.set_amr_block_source_index(int, int, int)
        C++: void SetAMRBlockSourceIndex(unsigned int level,
            unsigned int id, int sourceId)
        Set/Get the source id of a block. The source id is produced by an
        AMR source, e.g. a file reader might set this to be a file block
        id
        """
        ret = self._wrap_call(self._vtk_obj.SetAMRBlockSourceIndex, *args)
        return ret

    def get_amr_box(self, *args):
        """
        V.get_amr_box(int, int) -> AMRBox
        C++: const AMRBox &GetAMRBox(unsigned int level,
            unsigned int id)
        Set/Get the AMRBox for a given block
        """
        ret = self._wrap_call(self._vtk_obj.GetAMRBox, *args)
        return wrap_vtk(ret)

    def set_amr_box(self, *args):
        """
        V.set_amr_box(int, int, AMRBox)
        C++: void SetAMRBox(unsigned int level, unsigned int id,
            const AMRBox &box)
        Set/Get the AMRBox for a given block
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetAMRBox, *my_args)
        return ret

    def _get_amr_info(self):
        return wrap_vtk(self._vtk_obj.GetAMRInfo())
    def _set_amr_info(self, arg):
        old_val = self._get_amr_info()
        self._wrap_call(self._vtk_obj.SetAMRInfo,
                        deref_vtk(arg))
        self.trait_property_changed('amr_info', old_val, arg)
    amr_info = traits.Property(_get_amr_info, _set_amr_info, help=\
        """
        Get/Set the interal representation of amr meta meta data
        """
    )

    def get_refinement_ratio(self, *args):
        """
        V.get_refinement_ratio(int) -> int
        C++: int GetRefinementRatio(unsigned int level)
        V.get_refinement_ratio(CompositeDataIterator) -> int
        C++: int GetRefinementRatio(CompositeDataIterator *iter)
        Returns the refinement of a given level.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetRefinementRatio, *my_args)
        return ret

    def set_refinement_ratio(self, *args):
        """
        V.set_refinement_ratio(int, int)
        C++: void SetRefinementRatio(unsigned int level, int refRatio)
        Sets the refinement of a given level. The spacing at level
        level+1 is defined as spacing(level+1) =
        spacing(level)/ref_ratio(level). Note that currently, this is not
        enforced by this class however some algorithms might not function
        properly if the spacing in the blocks (vtk_uniform_grid) does not
        match the one described by the refinement ratio.
        """
        ret = self._wrap_call(self._vtk_obj.SetRefinementRatio, *args)
        return ret

    def get_spacing(self, *args):
        """
        V.get_spacing(int, [float, float, float])
        C++: void GetSpacing(unsigned int level, double spacing[3])
        Get/Set the grid spacing at a given level
        """
        ret = self._wrap_call(self._vtk_obj.GetSpacing, *args)
        return ret

    def set_spacing(self, *args):
        """
        V.set_spacing(int, (float, float, float))
        C++: void SetSpacing(unsigned int level, const double spacing[3])
        Get/Set the grid spacing at a given level
        """
        ret = self._wrap_call(self._vtk_obj.SetSpacing, *args)
        return ret

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

    def _get_origin(self):
        return self._vtk_obj.GetOrigin()
    origin = traits.Property(_get_origin, help=\
        """
        Get/Set the global origin of the amr data set
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

    def audit(self):
        """
        V.audit()
        C++: void Audit()
        Check whether the data set is internally consistent, e.g. whether
        the meta data and acutal data blocks match. Incorrectness will be
        reported as error messages
        """
        ret = self._vtk_obj.Audit()
        return ret
        

    def find_grid(self, *args):
        """
        V.find_grid([float, float, float], int, int) -> bool
        C++: bool FindGrid(double q[3], unsigned int &level,
            unsigned int &gridId)
        Given a point q, find the highest level grid that contains it.
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
        

    def has_children_information(self):
        """
        V.has_children_information() -> bool
        C++: bool HasChildrenInformation()
        Return whether parent child information has been generated
        """
        ret = self._vtk_obj.HasChildrenInformation()
        return ret
        

    def NUMBER_OF_BLANKED_POINTS(self):
        """
        V.number__of__blanked__points() -> InformationIdTypeKey
        C++: static InformationIdTypeKey *NUMBER_OF_BLANKED_POINTS()"""
        ret = wrap_vtk(self._vtk_obj.NUMBER_OF_BLANKED_POINTS())
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

    def set_origin(self, *args):
        """
        V.set_origin((float, ...))
        C++: void SetOrigin(const double *)
        Get/Set the global origin of the amr data set
        """
        ret = self._wrap_call(self._vtk_obj.SetOrigin, *args)
        return ret

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('grid_description', 'GetGridDescription'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'grid_description'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OverlappingAMR, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OverlappingAMR properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], ['grid_description']),
            title='Edit OverlappingAMR properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OverlappingAMR properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


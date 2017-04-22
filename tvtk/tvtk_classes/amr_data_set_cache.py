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


class AMRDataSetCache(Object):
    """
    AMRDataSetCache -  A concrete implementation of Object that
    provides functionality for
     caching AMR blocks.
    
    Superclass: Object
    
    The primary intent of this class is to be used by the
     AMR reader infrastructure for caching blocks/data in memory to
    minimize
     out-of-core operations.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAMRDataSetCache, obj, update, **traits)
    
    def get_amr_block(self, *args):
        """
        V.get_amr_block(int) -> UniformGrid
        C++: UniformGrid *GetAMRBlock(int compositeIdx)
        Given the composite index, this method returns the AMR block.
        NOTE: Null is returned if the AMR block does not exist in the
        cache.
        """
        ret = self._wrap_call(self._vtk_obj.GetAMRBlock, *args)
        return wrap_vtk(ret)

    def get_amr_block_cell_data(self, *args):
        """
        V.get_amr_block_cell_data(int, string) -> DataArray
        C++: DataArray *GetAMRBlockCellData(int compositeIdx,
            const char *dataName)
        Given the name of the cell array and AMR block composite index,
        this method returns a pointer to the cell data array. NOTE: Null
        is returned if the cell array and/or block is not cached.
        """
        ret = self._wrap_call(self._vtk_obj.GetAMRBlockCellData, *args)
        return wrap_vtk(ret)

    def get_amr_block_point_data(self, *args):
        """
        V.get_amr_block_point_data(int, string) -> DataArray
        C++: DataArray *GetAMRBlockPointData(int compositeIdx,
            const char *dataName)
        Given the name of the point array and AMR block composite index,
        this method returns a pointer to the point data array. NOTE: Null
        is returend if the point array and /or block is not cached.
        """
        ret = self._wrap_call(self._vtk_obj.GetAMRBlockPointData, *args)
        return wrap_vtk(ret)

    def has_amr_block(self, *args):
        """
        V.has_amr_block(int) -> bool
        C++: bool HasAMRBlock(const int compositeIdx)
        Checks if the AMR block associated with the given composite is
        cached.
        """
        ret = self._wrap_call(self._vtk_obj.HasAMRBlock, *args)
        return ret

    def has_amr_block_cell_data(self, *args):
        """
        V.has_amr_block_cell_data(int, string) -> bool
        C++: bool HasAMRBlockCellData(int compositeIdx, const char *name)
        Checks if the cell data array, associated with the provided name,
        has been cached for the AMR block with the given composite index.
        """
        ret = self._wrap_call(self._vtk_obj.HasAMRBlockCellData, *args)
        return ret

    def has_amr_block_point_data(self, *args):
        """
        V.has_amr_block_point_data(int, string) -> bool
        C++: bool HasAMRBlockPointData(int compositeIdx, const char *name)
        Checks if the point data array, associated with the provided
        name, has been cached for the AMR block with the given composite
        index.
        """
        ret = self._wrap_call(self._vtk_obj.HasAMRBlockPointData, *args)
        return ret

    def insert_amr_block(self, *args):
        """
        V.insert_amr_block(int, UniformGrid)
        C++: void InsertAMRBlock(int compositeIdx,
            UniformGrid *amrGrid)
        Inserts an AMR block to the cache
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InsertAMRBlock, *my_args)
        return ret

    def insert_amr_block_cell_data(self, *args):
        """
        V.insert_amr_block_cell_data(int, DataArray)
        C++: void InsertAMRBlockCellData(int compositeIdx,
            DataArray *dataArray)
        Inserts a cell data array to an already cached block NOTE:
        this->_has_amr_block( composite_idx ) == true
        """
        my_args = deref_array(args, [('int', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.InsertAMRBlockCellData, *my_args)
        return ret

    def insert_amr_block_point_data(self, *args):
        """
        V.insert_amr_block_point_data(int, DataArray)
        C++: void InsertAMRBlockPointData(int compositeIdx,
            DataArray *dataArray)
        Inserts a point data array to an already cached block NOTE:
        this->_has_amr_block( composite_idx ) == true
        """
        my_args = deref_array(args, [('int', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.InsertAMRBlockPointData, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AMRDataSetCache, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AMRDataSetCache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit AMRDataSetCache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AMRDataSetCache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


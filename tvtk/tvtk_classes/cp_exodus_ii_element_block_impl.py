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


class CPExodusIIElementBlockImpl(Object):
    """
    CPExodusIIElementBlockImpl - no description provided.
    
    Superclass: Object
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCPExodusIIElementBlockImpl, obj, update, **traits)
    
    def get_cell_points(self, *args):
        """
        V.get_cell_points(int, IdList)
        C++: void GetCellPoints(IdType cellId, IdList *ptIds)"""
        my_args = deref_array(args, [('int', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetCellPoints, *my_args)
        return ret

    def get_cell_type(self, *args):
        """
        V.get_cell_type(int) -> int
        C++: int GetCellType(IdType cellId)"""
        ret = self._wrap_call(self._vtk_obj.GetCellType, *args)
        return ret

    def get_ids_of_cells_of_type(self, *args):
        """
        V.get_ids_of_cells_of_type(int, IdTypeArray)
        C++: void GetIdsOfCellsOfType(int type, IdTypeArray *array)"""
        my_args = deref_array(args, [('int', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.GetIdsOfCellsOfType, *my_args)
        return ret

    def _get_max_cell_size(self):
        return self._vtk_obj.GetMaxCellSize()
    max_cell_size = traits.Property(_get_max_cell_size, help=\
        """
        
        """
    )

    def _get_number_of_cells(self):
        return self._vtk_obj.GetNumberOfCells()
    number_of_cells = traits.Property(_get_number_of_cells, help=\
        """
        
        """
    )

    def get_point_cells(self, *args):
        """
        V.get_point_cells(int, IdList)
        C++: void GetPointCells(IdType ptId, IdList *cellIds)"""
        my_args = deref_array(args, [('int', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetPointCells, *my_args)
        return ret

    def allocate(self, *args):
        """
        V.allocate(int, int)
        C++: void Allocate(IdType numCells, int extSize=1000)"""
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def insert_next_cell(self, *args):
        """
        V.insert_next_cell(int, IdList) -> int
        C++: IdType InsertNextCell(int type, IdList *ptIds)
        V.insert_next_cell(int, int, [int, ...]) -> int
        C++: IdType InsertNextCell(int type, IdType npts,
            IdType *ptIds)
        V.insert_next_cell(int, int, [int, ...], int, [int, ...]) -> int
        C++: IdType InsertNextCell(int type, IdType npts,
            IdType *ptIds, IdType nfaces, IdType *faces)"""
        my_args = deref_array(args, [('int', 'vtkIdList'), ('int', 'int', ['int', Ellipsis]), ('int', 'int', ['int', Ellipsis], 'int', ['int', Ellipsis])])
        ret = self._wrap_call(self._vtk_obj.InsertNextCell, *my_args)
        return ret

    def is_homogeneous(self):
        """
        V.is_homogeneous() -> int
        C++: int IsHomogeneous()"""
        ret = self._vtk_obj.IsHomogeneous()
        return ret
        

    def replace_cell(self, *args):
        """
        V.replace_cell(int, int, [int, ...])
        C++: void ReplaceCell(IdType cellId, int npts, IdType *pts)"""
        ret = self._wrap_call(self._vtk_obj.ReplaceCell, *args)
        return ret

    def set_exodus_connectivity_array(self, *args):
        """
        V.set_exodus_connectivity_array([int, ...], string, int, int) -> bool
        C++: bool SetExodusConnectivityArray(int *elements,
            const std::string &type, int numElements, int nodesPerElement)
        Set the Exodus element block data. 'elements' is the array
        returned from ex_get_elem_conn. 'type', 'num_elements', and
        'nodes_per_element' are obtained from ex_get_elem_block. Returns
        true or false depending on whether or not the element type can be
        translated into a VTK cell type. This object takes ownership of
        the elements array unless this function returns false.
        """
        ret = self._wrap_call(self._vtk_obj.SetExodusConnectivityArray, *args)
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
            return super(CPExodusIIElementBlockImpl, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CPExodusIIElementBlockImpl properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit CPExodusIIElementBlockImpl properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CPExodusIIElementBlockImpl properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.point_set import PointSet


class UnstructuredGridBase(PointSet):
    """
    UnstructuredGridBase - dataset represents arbitrary combinations
    of all possible cell types.
    
    Superclass: PointSet
    
    May be mapped onto a non-standard memory layout.
    
    UnstructuredGridBase defines the core UnstructuredGrid API,
    omitting functions that are implementation dependent.
    
    @sa
    MappedDataArray UnstructuredGrid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGridBase, obj, update, **traits)
    
    def get_ids_of_cells_of_type(self, *args):
        """
        V.get_ids_of_cells_of_type(int, IdTypeArray)
        C++: virtual void GetIdsOfCellsOfType(int type,
            IdTypeArray *array)
        Fill IdTypeArray container with list of cell Ids.  This method
        traverses all cells and, for a particular cell type, inserts the
        cell Id into the container.
        """
        my_args = deref_array(args, [('int', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.GetIdsOfCellsOfType, *my_args)
        return ret

    def allocate(self, *args):
        """
        V.allocate(int, int)
        C++: virtual void Allocate(IdType numCells=1000,
            int extSize=1000)
        Allocate memory for the number of cells indicated. ext_size is not
        used.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def insert_next_cell(self, *args):
        """
        V.insert_next_cell(int, int, [int, ...]) -> int
        C++: virtual IdType InsertNextCell(int type, IdType npts,
            IdType *ptIds)
        V.insert_next_cell(int, IdList) -> int
        C++: virtual IdType InsertNextCell(int type, IdList *ptIds)
        V.insert_next_cell(int, int, [int, ...], int, [int, ...]) -> int
        C++: virtual IdType InsertNextCell(int type, IdType npts,
            IdType *ptIds, IdType nfaces, IdType *faces)
        Insert/create cell in object by type and list of point ids
        defining cell topology. Most cells require just a type which
        implicitly defines a set of points and their ordering. For
        non-polyhedron cell type, npts is the number of unique points in
        the cell. pts are the list of global point Ids. For polyhedron
        cell, a special input format is required. npts is the number of
        faces in the cell. pt_ids is the list of face stream:
        (num_face0_pts, id1, id2, id3, num_face1_pts,id_1, id2, id3, ...)
        """
        my_args = deref_array(args, [('int', 'int', ['int', Ellipsis]), ('int', 'vtkIdList'), ('int', 'int', ['int', Ellipsis], 'int', ['int', Ellipsis])])
        ret = self._wrap_call(self._vtk_obj.InsertNextCell, *my_args)
        return ret

    def is_homogeneous(self):
        """
        V.is_homogeneous() -> int
        C++: virtual int IsHomogeneous()
        Traverse cells and determine if cells are all of the same type.
        """
        ret = self._vtk_obj.IsHomogeneous()
        return ret
        

    def replace_cell(self, *args):
        """
        V.replace_cell(int, int, [int, ...])
        C++: virtual void ReplaceCell(IdType cellId, int npts,
            IdType *pts)
        Replace the points defining cell "cell_id" with a new set of
        points. This operator is (typically) used when links from points
        to cells have not been built (i.e., build_links() has not been
        executed). Use the operator replace_linked_cell() to replace a cell
        when cell structure has been built.
        """
        ret = self._wrap_call(self._vtk_obj.ReplaceCell, *args)
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
            return super(UnstructuredGridBase, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGridBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit UnstructuredGridBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGridBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


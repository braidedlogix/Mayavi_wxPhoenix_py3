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

from tvtk.tvtk_classes.abstract_grid_connectivity import AbstractGridConnectivity


class StructuredGridConnectivity(AbstractGridConnectivity):
    """
    StructuredGridConnectivity -  StructuredGridConnectivity is a
    concrete instance of Object that
     implements functionality for computing the neighboring topology
    within a
     single partitioned structured grid dataset.
    
    Superclass: AbstractGridConnectivity
    
    This class implementation does
     not have any support for distributed data. For the parallel
    implementation
     see PStructuredGridConnectivity.
    
    @sa
     GhostArray PStructuredGridConnectivity
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStructuredGridConnectivity, obj, update, **traits)
    
    def get_ghosted_grid_extent(self, *args):
        """
        V.get_ghosted_grid_extent(int, [int, int, int, int, int, int])
        C++: void GetGhostedGridExtent(const int gridID, int ext[6])
        Returns the ghosted grid extent for the block corresponding the
        """
        ret = self._wrap_call(self._vtk_obj.GetGhostedGridExtent, *args)
        return ret

    def set_ghosted_grid_extent(self, *args):
        """
        V.set_ghosted_grid_extent(int, [int, int, int, int, int, int])
        C++: void SetGhostedGridExtent(const int gridID, int ext[6])
        Sets the ghosted grid extent for the grid corresponding to the
        given grid ID to the given extent.
        """
        ret = self._wrap_call(self._vtk_obj.SetGhostedGridExtent, *args)
        return ret

    number_of_grids = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the total number of domains distributed among processors
        """
    )

    def _number_of_grids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfGrids,
                        self.number_of_grids)

    whole_extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(-1, -1, -1, -1, -1, -1), cols=3, help=\
        """
        
        """
    )

    def _whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWholeExtent,
                        self.whole_extent)

    def _get_data_dimension(self):
        return self._vtk_obj.GetDataDimension()
    data_dimension = traits.Property(_get_data_dimension, help=\
        """
        Returns the data dimension based on the whole extent
        """
    )

    def get_grid_extent(self, *args):
        """
        V.get_grid_extent(int, [int, int, int, int, int, int])
        C++: void GetGridExtent(const int gridID, int extent[6])
        Returns the grid extent of the grid corresponding to the given
        grid ID.
        """
        ret = self._wrap_call(self._vtk_obj.GetGridExtent, *args)
        return ret

    def get_grid_neighbor(self, *args):
        """
        V.get_grid_neighbor(int, int) -> StructuredNeighbor
        C++: StructuredNeighbor GetGridNeighbor(const int gridID,
            const int nei)
        Returns the neighbor corresponding to the index nei for the grid
        with the given (global) grid ID.
        """
        ret = self._wrap_call(self._vtk_obj.GetGridNeighbor, *args)
        return wrap_vtk(ret)

    def get_neighbors(self, *args):
        """
        V.get_neighbors(int, [int, ...]) -> IdList
        C++: IdList *GetNeighbors(const int gridID, int *extents)
        Returns the list of neighboring blocks for the given grid and the
        corresponding overlapping extents are filled in the 1-D flat
        array strided by 6.
        
        * NOTE: the flat array extents must be pre-allocated.
        """
        ret = self._wrap_call(self._vtk_obj.GetNeighbors, *args)
        return wrap_vtk(ret)

    def get_number_of_neighbors(self, *args):
        """
        V.get_number_of_neighbors(int) -> int
        C++: int GetNumberOfNeighbors(const int gridID)
        Returns the number of neighbors for the grid corresponding to the
        given grid ID.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfNeighbors, *args)
        return ret

    def fill_ghost_arrays(self, *args):
        """
        V.fill_ghost_arrays(int, UnsignedCharArray, UnsignedCharArray)
        C++: void FillGhostArrays(const int gridID,
            UnsignedCharArray *nodesArray,
            UnsignedCharArray *cellsArray) override;
        Filles the mesh property arrays, nodes and cells, for the grid
        corresponding to the given grid ID. NOTE: this method assumes
        that compute_neighbors() has been called.
        """
        my_args = deref_array(args, [('int', 'vtkUnsignedCharArray', 'vtkUnsignedCharArray')])
        ret = self._wrap_call(self._vtk_obj.FillGhostArrays, *my_args)
        return ret

    def register_grid(self, *args):
        """
        V.register_grid(int, [int, int, int, int, int, int],
            UnsignedCharArray, UnsignedCharArray, PointData,
            CellData, Points)
        C++: virtual void RegisterGrid(const int gridID, int extents[6],
            UnsignedCharArray *nodesGhostArray,
            UnsignedCharArray *cellGhostArray, PointData *pointData,
             CellData *cellData, Points *gridNodes)
        Registers the current grid corresponding to the grid ID by its
        global extent w.r.t. the whole extent.
        """
        my_args = deref_array(args, [('int', ['int', 'int', 'int', 'int', 'int', 'int'], 'vtkUnsignedCharArray', 'vtkUnsignedCharArray', 'vtkPointData', 'vtkCellData', 'vtkPoints')])
        ret = self._wrap_call(self._vtk_obj.RegisterGrid, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_grids', 'GetNumberOfGrids'),
    ('whole_extent', 'GetWholeExtent'), ('number_of_ghost_layers',
    'GetNumberOfGhostLayers'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'number_of_ghost_layers',
    'number_of_grids', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StructuredGridConnectivity, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StructuredGridConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['number_of_ghost_layers', 'number_of_grids',
            'whole_extent']),
            title='Edit StructuredGridConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StructuredGridConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


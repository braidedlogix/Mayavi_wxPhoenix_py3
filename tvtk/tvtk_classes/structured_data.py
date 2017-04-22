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


class StructuredData(Object):
    """
    StructuredData - Singleton class for topologically regular data
    
    Superclass: Object
    
    StructuredData is a singleton class that provides an interface for
    topologically regular data. Regular data is data that can be accessed
    in rectangular fashion using an i-j-k index. A finite difference
    grid, a volume, or a pixmap are all considered regular.
    
    @sa
    StructuredGrid UniformGrid RectilinearGrid
    RectilinearGrid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStructuredData, obj, update, **traits)
    
    def get_cell_dimensions_from_extent(self, *args):
        """
        V.get_cell_dimensions_from_extent([int, int, int, int, int, int],
            [int, int, int], int)
        C++: static void GetCellDimensionsFromExtent(int ext[6],
            int celldims[3], int dataDescription=VTK_EMPTY)
        Returns the cell dimensions, i.e., the number of cells along the
        i,j,k for the grid with the given grid extent. Note, the grid
        extent is the number of points. The data_description field is not
        used.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellDimensionsFromExtent, *args)
        return ret

    def get_cell_dimensions_from_point_dimensions(self, *args):
        """
        V.get_cell_dimensions_from_point_dimensions([int, int, int], [int, int,
             int])
        C++: static void GetCellDimensionsFromPointDimensions(
            int pntdims[3], int cellDims[3])
        Given the dimensions of the grid, in pntdims, this method returns
        the corresponding cell dimensions for the given grid. The
        data_description field is not used.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellDimensionsFromPointDimensions, *args)
        return ret

    def get_cell_extent_from_point_extent(self, *args):
        """
        V.get_cell_extent_from_point_extent([int, int, int, int, int, int],
            [int, int, int, int, int, int], int)
        C++: static void GetCellExtentFromPointExtent(int pntExtent[6],
            int cellExtent[6], int dataDescription=VTK_EMPTY)
        Given the point extent of a grid, this method computes the
        corresponding cell extent for the grid. The data_description field
        is not used.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellExtentFromPointExtent, *args)
        return ret

    def get_cell_neighbors(self, *args):
        """
        V.get_cell_neighbors(int, IdList, IdList, [int, int, int])
        C++: static void GetCellNeighbors(IdType cellId,
            IdList *ptIds, IdList *cellIds, int dim[3])
        Get the cells using the points pt_ids, exclusive of the cell
        cell_id. (See DataSet for more info.)
        """
        my_args = deref_array(args, [('int', 'vtkIdList', 'vtkIdList', ['int', 'int', 'int'])])
        ret = self._wrap_call(self._vtk_obj.GetCellNeighbors, *my_args)
        return ret

    def get_cell_points(self, *args):
        """
        V.get_cell_points(int, IdList, int, [int, int, int])
        C++: static void GetCellPoints(IdType cellId, IdList *ptIds,
             int dataDescription, int dim[3])
        Get the points defining a cell. (See DataSet for more info.)
        """
        my_args = deref_array(args, [('int', 'vtkIdList', 'int', ['int', 'int', 'int'])])
        ret = self._wrap_call(self._vtk_obj.GetCellPoints, *my_args)
        return ret

    def get_data_description(self, *args):
        """
        V.get_data_description([int, int, int]) -> int
        C++: static int GetDataDescription(int dims[3])
        Returns the data description given the dimensions (eg.
        VTK_SINGLE_POINT, VTK_X_LINE, VTK_XY_PLANE etc.)
        """
        ret = self._wrap_call(self._vtk_obj.GetDataDescription, *args)
        return ret

    def get_data_description_from_extent(self, *args):
        """
        V.get_data_description_from_extent([int, int, int, int, int, int])
            -> int
        C++: static int GetDataDescriptionFromExtent(int ext[6])
        Returns the data description given the dimensions (eg.
        VTK_SINGLE_POINT, VTK_X_LINE, VTK_XY_PLANE etc.)
        """
        ret = self._wrap_call(self._vtk_obj.GetDataDescriptionFromExtent, *args)
        return ret

    def get_data_dimension(self, *args):
        """
        V.get_data_dimension(int) -> int
        C++: static int GetDataDimension(int dataDescription)
        V.get_data_dimension([int, int, int, int, int, int]) -> int
        C++: static int GetDataDimension(int ext[6])
        Return the topological dimension of the data (e.g., 0, 1, 2, or
        3d).
        """
        ret = self._wrap_call(self._vtk_obj.GetDataDimension, *args)
        return ret

    def get_dimensions_from_extent(self, *args):
        """
        V.get_dimensions_from_extent([int, int, int, int, int, int], [int,
            int, int], int)
        C++: static void GetDimensionsFromExtent(int ext[6], int dims[3],
            int dataDescription=VTK_EMPTY)
        Computes the structured grid dimensions based on the given
        extent. The data_description field is not used.
        """
        ret = self._wrap_call(self._vtk_obj.GetDimensionsFromExtent, *args)
        return ret

    def get_global_structured_coordinates(self, *args):
        """
        V.get_global_structured_coordinates([int, int, int], [int, int, int,
            int, int, int], [int, int, int], int)
        C++: static void GetGlobalStructuredCoordinates(int lijk[3],
            int ext[6], int ijk[3], int dataDescription=VTK_EMPTY)
        Given local structured coordinates, and the corresponding global
        sub-grid extent, this method computes the global ijk coordinates.
        The data_description parameter is not used.
        """
        ret = self._wrap_call(self._vtk_obj.GetGlobalStructuredCoordinates, *args)
        return ret

    def get_local_structured_coordinates(self, *args):
        """
        V.get_local_structured_coordinates([int, int, int], [int, int, int,
            int, int, int], [int, int, int], int)
        C++: static void GetLocalStructuredCoordinates(int ijk[3],
            int ext[6], int lijk[3], int dataDescription=VTK_EMPTY)
        Given the global structured coordinates for a point or cell, ijk,
        w.r.t. as well as, the global sub-grid cell or point extent, this
        method computes the corresponding local structured coordinates,
        lijk, starting from 0. The data_description argument is not used.
        """
        ret = self._wrap_call(self._vtk_obj.GetLocalStructuredCoordinates, *args)
        return ret

    def get_number_of_cells(self, *args):
        """
        V.get_number_of_cells([int, int, int, int, int, int], int) -> int
        C++: static IdType GetNumberOfCells(int ext[6],
            int dataDescription=VTK_EMPTY)
        Given the grid extent, this method returns the total number of
        cells within the extent. The data_description field is not used.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfCells, *args)
        return ret

    def get_number_of_points(self, *args):
        """
        V.get_number_of_points([int, int, int, int, int, int], int) -> int
        C++: static IdType GetNumberOfPoints(int ext[6],
            int dataDescription=VTK_EMPTY)
        Given the grid extent, this method returns the total number of
        points within the extent. The data_description field is not used.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfPoints, *args)
        return ret

    def get_point_cells(self, *args):
        """
        V.get_point_cells(int, IdList, [int, int, int])
        C++: static void GetPointCells(IdType ptId, IdList *cellIds,
             int dim[3])
        Get the cells using a point. (See DataSet for more info.)
        """
        my_args = deref_array(args, [('int', 'vtkIdList', ['int', 'int', 'int'])])
        ret = self._wrap_call(self._vtk_obj.GetPointCells, *my_args)
        return ret

    def compute_cell_id(self, *args):
        """
        V.compute_cell_id([int, int, int], [int, int, int], int) -> int
        C++: static IdType ComputeCellId(int dim[3], int ijk[3],
            int dataDescription=VTK_EMPTY)
        Given a location in structured coordinates (i-j-k), and the
        dimensions of the structured dataset, return the cell id.  This
        method does not adjust for the beginning of the extent. The
        data_description argument is not used.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeCellId, *args)
        return ret

    def compute_cell_id_for_extent(self, *args):
        """
        V.compute_cell_id_for_extent([int, int, int, int, int, int], [int,
            int, int], int) -> int
        C++: static IdType ComputeCellIdForExtent(int extent[6],
            int ijk[3], int dataDescription=VTK_EMPTY)
        Given a location in structured coordinates (i-j-k), and the
        extent of the structured dataset, return the point id. The
        data_description argument is not used.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeCellIdForExtent, *args)
        return ret

    def compute_cell_structured_coords(self, *args):
        """
        V.compute_cell_structured_coords(int, [int, int, int], [int, int,
            int], int)
        C++: static void ComputeCellStructuredCoords(
            const IdType cellId, int dim[3], int ijk[3],
            int dataDescription=VTK_EMPTY)
        Given a cell_id and grid dimensions 'dim', get the structured
        coordinates (i-j-k). This method does not adjust for the
        beginning of the extent. The data_description argument is not
        used.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeCellStructuredCoords, *args)
        return ret

    def compute_cell_structured_coords_for_extent(self, *args):
        """
        V.compute_cell_structured_coords_for_extent(int, [int, int, int, int,
            int, int], [int, int, int], int)
        C++: static void ComputeCellStructuredCoordsForExtent(
            const IdType cellIdx, int ext[6], int ijk[3],
            int dataDescription=VTK_EMPTY)
        Given the global grid extent and the linear index of a cell
        within the grid extent, this method computes the corresponding
        structured coordinates of the given cell. This method adjusts for
        the beginning of the extent. The data_description argument is not
        used.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeCellStructuredCoordsForExtent, *args)
        return ret

    def compute_point_id(self, *args):
        """
        V.compute_point_id([int, int, int], [int, int, int], int) -> int
        C++: static IdType ComputePointId(int dim[3], int ijk[3],
            int dataDescription=VTK_EMPTY)
        Given a location in structured coordinates (i-j-k), and the
        dimensions of the structured dataset, return the point id.  This
        method does not adjust for the beginning of the extent. The
        data_description argument is not used.
        """
        ret = self._wrap_call(self._vtk_obj.ComputePointId, *args)
        return ret

    def compute_point_id_for_extent(self, *args):
        """
        V.compute_point_id_for_extent([int, int, int, int, int, int], [int,
            int, int], int) -> int
        C++: static IdType ComputePointIdForExtent(int extent[6],
            int ijk[3], int dataDescription=VTK_EMPTY)
        Given a location in structured coordinates (i-j-k), and the
        extent of the structured dataset, return the point id. The
        data_description argument is not used.
        """
        ret = self._wrap_call(self._vtk_obj.ComputePointIdForExtent, *args)
        return ret

    def compute_point_structured_coords(self, *args):
        """
        V.compute_point_structured_coords(int, [int, int, int], [int, int,
            int], int)
        C++: static void ComputePointStructuredCoords(
            const IdType ptId, int dim[3], int ijk[3],
            int dataDescription=VTK_EMPTY)
        Given a point_id and grid dimensions 'dim', get the structured
        coordinates (i-j-k). This method does not adjust for the
        beginning of the extent. The data_description argument is not
        used.
        """
        ret = self._wrap_call(self._vtk_obj.ComputePointStructuredCoords, *args)
        return ret

    def compute_point_structured_coords_for_extent(self, *args):
        """
        V.compute_point_structured_coords_for_extent(int, [int, int, int, int,
            int, int], [int, int, int], int)
        C++: static void ComputePointStructuredCoordsForExtent(
            const IdType ptId, int ext[6], int ijk[3],
            int dataDescription=VTK_EMPTY)
        Given a point_id and the grid extent ext, get the structured
        coordinates (i-j-k). This method adjusts for the beginning of the
        extent. The data_description argument is not used.
        """
        ret = self._wrap_call(self._vtk_obj.ComputePointStructuredCoordsForExtent, *args)
        return ret

    def set_dimensions(self, *args):
        """
        V.set_dimensions([int, int, int], [int, int, int]) -> int
        C++: static int SetDimensions(int inDim[3], int dim[3])
        Specify the dimensions of a regular, rectangular dataset. The
        input is the new dimensions (in_dim) and the current dimensions
        (dim). The function returns the dimension of the dataset (_0-_3d).
        If the dimensions are improperly specified a -1 is returned. If
        the dimensions are unchanged, a value of 100 is returned.
        """
        ret = self._wrap_call(self._vtk_obj.SetDimensions, *args)
        return ret

    def set_extent(self, *args):
        """
        V.set_extent([int, int, int, int, int, int], [int, int, int, int,
            int, int]) -> int
        C++: static int SetExtent(int inExt[6], int ext[6])
        Specify the dimensions of a regular, rectangular dataset. The
        input is the new dimensions (in_dim) and the current dimensions
        (dim). The function returns the dimension of the dataset (_0-_3d).
        If the dimensions are improperly specified a -1 is returned. If
        the dimensions are unchanged, a value of 100 is returned.
        """
        ret = self._wrap_call(self._vtk_obj.SetExtent, *args)
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
            return super(StructuredData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StructuredData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit StructuredData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StructuredData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


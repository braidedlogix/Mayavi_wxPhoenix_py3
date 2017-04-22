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


class DataSet(DataObject):
    """
    DataSet - abstract class to specify dataset behavior
    
    Superclass: DataObject
    
    DataSet is an abstract class that specifies an interface for
    dataset objects. DataSet also provides methods to provide
    informations about the data, such as center, bounding box, and
    representative length.
    
    In vtk a dataset consists of a structure (geometry and topology) and
    attribute data. The structure is defined implicitly or explicitly as
    a collection of cells. The geometry of the structure is contained in
    point coordinates plus the cell interpolation functions. The topology
    of the dataset structure is defined by cell types and how the cells
    share their defining points.
    
    Attribute data in vtk is either point data (data at points) or cell
    data (data at cells). Typically filters operate on point data, but
    some may operate on cell data, both cell and point data, either one,
    or none.
    
    @sa
    PointSet StructuredPoints StructuredGrid UnstructuredGrid
    RectilinearGrid PolyData PointData CellData DataObject
    FieldData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataSet, obj, update, **traits)
    
    def _get_bounds(self):
        return self._vtk_obj.GetBounds()
    bounds = traits.Property(_get_bounds, help=\
        """
        Return a pointer to the geometry bounding box in the form
        (xmin,xmax, ymin,ymax, zmin,zmax). THIS METHOD IS NOT THREAD
        SAFE.
        """
    )

    def get_cell(self, *args):
        """
        V.get_cell(int) -> Cell
        C++: virtual Cell *GetCell(IdType cellId)
        V.get_cell(int, GenericCell)
        C++: virtual void GetCell(IdType cellId, GenericCell *cell)
        Get cell with cell_id such that: 0 <= cell_id < number_of_cells. THIS
        METHOD IS NOT THREAD SAFE.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetCell, *my_args)
        return wrap_vtk(ret)

    def get_cell_bounds(self, *args):
        """
        V.get_cell_bounds(int, [float, float, float, float, float, float])
        C++: virtual void GetCellBounds(IdType cellId,
            double bounds[6])
        Get the bounds of the cell with cell_id such that: 0 <= cell_id <
        number_of_cells. A subclass may be able to determine the bounds of
        cell without using an expensive get_cell() method. A default
        implementation is provided that actually uses a get_cell() call. 
        This is to ensure the method is available to all datasets. 
        Subclasses should override this method to provide an efficient
        implementation. THIS METHOD IS THREAD SAFE IF FIRST CALLED FROM A
        SINGLE THREAD AND THE DATASET IS NOT MODIFIED
        """
        ret = self._wrap_call(self._vtk_obj.GetCellBounds, *args)
        return ret

    def _get_cell_data(self):
        return wrap_vtk(self._vtk_obj.GetCellData())
    cell_data = traits.Property(_get_cell_data, help=\
        """
        Return a pointer to this dataset's cell data. THIS METHOD IS
        THREAD SAFE
        """
    )

    def _get_cell_ghost_array(self):
        return wrap_vtk(self._vtk_obj.GetCellGhostArray())
    cell_ghost_array = traits.Property(_get_cell_ghost_array, help=\
        """
        Get the array that defines the ghost type of each cell. We cache
        the pointer to the array to save a lookup involving string
        comparisons
        """
    )

    def get_cell_neighbors(self, *args):
        """
        V.get_cell_neighbors(int, IdList, IdList)
        C++: virtual void GetCellNeighbors(IdType cellId,
            IdList *ptIds, IdList *cellIds)
        Topological inquiry to get all cells using list of points
        exclusive of cell specified (e.g., cell_id). Note that the list
        consists of only cells that use ALL the points provided. THIS
        METHOD IS THREAD SAFE IF FIRST CALLED FROM A SINGLE THREAD AND
        THE DATASET IS NOT MODIFIED
        """
        my_args = deref_array(args, [('int', 'vtkIdList', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetCellNeighbors, *my_args)
        return ret

    def get_cell_points(self, *args):
        """
        V.get_cell_points(int, IdList)
        C++: virtual void GetCellPoints(IdType cellId,
            IdList *ptIds)
        Topological inquiry to get points defining cell. THIS METHOD IS
        THREAD SAFE IF FIRST CALLED FROM A SINGLE THREAD AND THE DATASET
        IS NOT MODIFIED
        """
        my_args = deref_array(args, [('int', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetCellPoints, *my_args)
        return ret

    def get_cell_type(self, *args):
        """
        V.get_cell_type(int) -> int
        C++: virtual int GetCellType(IdType cellId)
        Get type of cell with cell_id such that: 0 <= cell_id <
        number_of_cells. THIS METHOD IS THREAD SAFE IF FIRST CALLED FROM A
        SINGLE THREAD AND THE DATASET IS NOT MODIFIED
        """
        ret = self._wrap_call(self._vtk_obj.GetCellType, *args)
        return ret

    def get_cell_types(self, *args):
        """
        V.get_cell_types(CellTypes)
        C++: virtual void GetCellTypes(CellTypes *types)
        Get a list of types of cells in a dataset. The list consists of
        an array of types (not necessarily in any order), with a single
        entry per type. For example a dataset 5 triangles, 3 lines, and
        100 hexahedra would result a list of three entries, corresponding
        to the types VTK_TRIANGLE, VTK_LINE, and VTK_HEXAHEDRON. THIS
        METHOD IS THREAD SAFE IF FIRST CALLED FROM A SINGLE THREAD AND
        THE DATASET IS NOT MODIFIED
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetCellTypes, *my_args)
        return ret

    def _get_center(self):
        return self._vtk_obj.GetCenter()
    center = traits.Property(_get_center, help=\
        """
        Get the center of the bounding box. THIS METHOD IS NOT THREAD
        SAFE.
        """
    )

    def _get_length(self):
        return self._vtk_obj.GetLength()
    length = traits.Property(_get_length, help=\
        """
        Return the length of the diagonal of the bounding box. THIS
        METHOD IS THREAD SAFE IF FIRST CALLED FROM A SINGLE THREAD AND
        THE DATASET IS NOT MODIFIED
        """
    )

    def _get_max_cell_size(self):
        return self._vtk_obj.GetMaxCellSize()
    max_cell_size = traits.Property(_get_max_cell_size, help=\
        """
        Convenience method returns largest cell size in dataset. This is
        generally used to allocate memory for supporting data structures.
        THIS METHOD IS THREAD SAFE
        """
    )

    def _get_number_of_cells(self):
        return self._vtk_obj.GetNumberOfCells()
    number_of_cells = traits.Property(_get_number_of_cells, help=\
        """
        Determine the number of cells composing the dataset. THIS METHOD
        IS THREAD SAFE
        """
    )

    def _get_number_of_points(self):
        return self._vtk_obj.GetNumberOfPoints()
    number_of_points = traits.Property(_get_number_of_points, help=\
        """
        Determine the number of points composing the dataset. THIS METHOD
        IS THREAD SAFE
        """
    )

    def get_point(self, *args):
        """
        V.get_point(int) -> (float, float, float)
        C++: virtual double *GetPoint(IdType ptId)
        V.get_point(int, [float, float, float])
        C++: virtual void GetPoint(IdType id, double x[3])
        Get point coordinates with pt_id such that: 0 <= pt_id <
        number_of_points. THIS METHOD IS NOT THREAD SAFE.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint, *args)
        return ret

    def get_point_cells(self, *args):
        """
        V.get_point_cells(int, IdList)
        C++: virtual void GetPointCells(IdType ptId,
            IdList *cellIds)
        Topological inquiry to get cells using point. THIS METHOD IS
        THREAD SAFE IF FIRST CALLED FROM A SINGLE THREAD AND THE DATASET
        IS NOT MODIFIED
        """
        my_args = deref_array(args, [('int', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetPointCells, *my_args)
        return ret

    def _get_point_data(self):
        return wrap_vtk(self._vtk_obj.GetPointData())
    point_data = traits.Property(_get_point_data, help=\
        """
        Return a pointer to this dataset's point data. THIS METHOD IS
        THREAD SAFE
        """
    )

    def _get_point_ghost_array(self):
        return wrap_vtk(self._vtk_obj.GetPointGhostArray())
    point_ghost_array = traits.Property(_get_point_ghost_array, help=\
        """
        Gets the array that defines the ghost type of each point. We
        cache the pointer to the array to save a lookup involving string
        comparisons
        """
    )

    def _get_scalar_range(self):
        return self._vtk_obj.GetScalarRange()
    scalar_range = traits.Property(_get_scalar_range, help=\
        """
        Convenience method to get the range of the first component (and
        only the first component) of any scalars in the data set.  If the
        data has both point data and cell data, it returns the (min/max)
        range of combined point and cell data.  If there are no point or
        cell scalars the method will return (0,1).  Note: It might be
        necessary to call Update to create or refresh the scalars before
        calling this method. THIS METHOD IS THREAD SAFE IF FIRST CALLED
        FROM A SINGLE THREAD AND THE DATASET IS NOT MODIFIED
        """
    )

    def allocate_cell_ghost_array(self):
        """
        V.allocate_cell_ghost_array() -> UnsignedCharArray
        C++: UnsignedCharArray *AllocateCellGhostArray()
        Allocate ghost array for cells.
        """
        ret = wrap_vtk(self._vtk_obj.AllocateCellGhostArray())
        return ret
        

    def allocate_point_ghost_array(self):
        """
        V.allocate_point_ghost_array() -> UnsignedCharArray
        C++: UnsignedCharArray *AllocatePointGhostArray()
        Allocate ghost array for points.
        """
        ret = wrap_vtk(self._vtk_obj.AllocatePointGhostArray())
        return ret
        

    def check_attributes(self):
        """
        V.check_attributes() -> int
        C++: int CheckAttributes()
        This method checks to see if the cell and point attributes match
        the geometry.  Many filters will crash if the number of tupples
        in an array is less than the number of points/cells. This method
        returns 1 if there is a mismatch, and 0 if everything is ok.  It
        prints an error if an array is too short, and a warning if an
        array is too long.
        """
        ret = self._vtk_obj.CheckAttributes()
        return ret
        

    def compute_bounds(self):
        """
        V.compute_bounds()
        C++: virtual void ComputeBounds()
        Compute the data bounding box from data points. THIS METHOD IS
        NOT THREAD SAFE.
        """
        ret = self._vtk_obj.ComputeBounds()
        return ret
        

    def copy_attributes(self, *args):
        """
        V.copy_attributes(DataSet)
        C++: virtual void CopyAttributes(DataSet *ds)
        Copy the attributes associated with the specified dataset to this
        instance of DataSet. THIS METHOD IS NOT THREAD SAFE.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyAttributes, *my_args)
        return ret

    def copy_structure(self, *args):
        """
        V.copy_structure(DataSet)
        C++: virtual void CopyStructure(DataSet *ds)
        Copy the geometric and topological structure of an object. Note
        that the invoking object and the object pointed to by the
        parameter ds must be of the same type. THIS METHOD IS NOT THREAD
        SAFE.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyStructure, *my_args)
        return ret

    def find_and_get_cell(self, *args):
        """
        V.find_and_get_cell([float, float, float], Cell, int, float, int,
            [float, float, float], [float, ...]) -> Cell
        C++: virtual Cell *FindAndGetCell(double x[3], Cell *cell,
            IdType cellId, double tol2, int &subId, double pcoords[3],
            double *weights)
        Locate the cell that contains a point and return the cell. Also
        returns the subcell id, parametric coordinates and weights for
        subsequent interpolation. This method combines the derived class
        methods int find_cell and Cell *_get_cell. Derived classes may
        provide a more efficient implementation. See for example
        StructuredPoints. THIS METHOD IS NOT THREAD SAFE.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FindAndGetCell, *my_args)
        return wrap_vtk(ret)

    def find_cell(self, *args):
        """
        V.find_cell([float, float, float], Cell, int, float, int,
            [float, float, float], [float, ...]) -> int
        C++: virtual IdType FindCell(double x[3], Cell *cell,
            IdType cellId, double tol2, int &subId, double pcoords[3],
            double *weights)
        V.find_cell([float, float, float], Cell, GenericCell, int,
            float, int, [float, float, float], [float, ...]) -> int
        C++: virtual IdType FindCell(double x[3], Cell *cell,
            GenericCell *gencell, IdType cellId, double tol2,
            int &subId, double pcoords[3], double *weights)
        Locate cell based on global coordinate x and tolerance squared.
        If cell and cell_id is non-NULL, then search starts from this cell
        and looks at immediate neighbors.  Returns cell_id >= 0 if inside,
        < 0 otherwise.  The parametric coordinates are provided in
        pcoords[3]. The interpolation weights are returned in weights[].
        (The number of weights is equal to the number of points in the
        found cell). Tolerance is used to control how close the point is
        to be considered "in" the cell. THIS METHOD IS NOT THREAD SAFE.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FindCell, *my_args)
        return ret

    def find_point(self, *args):
        """
        V.find_point(float, float, float) -> int
        C++: IdType FindPoint(double x, double y, double z)
        V.find_point([float, float, float]) -> int
        C++: virtual IdType FindPoint(double x[3])
        Locate the closest point to the global coordinate x. Return the
        point id. If point id < 0; then no point found. (This may arise
        when point is outside of dataset.) THIS METHOD IS THREAD SAFE IF
        FIRST CALLED FROM A SINGLE THREAD AND THE DATASET IS NOT MODIFIED
        """
        ret = self._wrap_call(self._vtk_obj.FindPoint, *args)
        return ret

    def generate_ghost_array(self, *args):
        """
        V.generate_ghost_array([int, int, int, int, int, int])
        C++: virtual void GenerateGhostArray(int zeroExt[6])
        V.generate_ghost_array([int, int, int, int, int, int], bool)
        C++: virtual void GenerateGhostArray(int zeroExt[6],
            bool cellOnly)
        Normally called by pipeline executives or algoritms only. This
        method computes the ghost arrays for a given dataset. The zero_ext
        argument specifies the extent of the region which ghost type = 0.
        """
        ret = self._wrap_call(self._vtk_obj.GenerateGhostArray, *args)
        return ret

    def has_any_blank_cells(self):
        """
        V.has_any_blank_cells() -> bool
        C++: virtual bool HasAnyBlankCells()
        Returns 1 if there are any blanking cells 0 otherwise. Blanking
        is supported only for StructuredGrid and UniformGrid
        """
        ret = self._vtk_obj.HasAnyBlankCells()
        return ret
        

    def has_any_blank_points(self):
        """
        V.has_any_blank_points() -> bool
        C++: virtual bool HasAnyBlankPoints()
        Returns 1 if there are any blanking points 0 otherwise. Blanking
        is supported only for StructuredGrid and UniformGrid
        """
        ret = self._vtk_obj.HasAnyBlankPoints()
        return ret
        

    def has_any_ghost_cells(self):
        """
        V.has_any_ghost_cells() -> bool
        C++: bool HasAnyGhostCells()
        Returns 1 if there are any ghost cells 0 otherwise.
        """
        ret = self._vtk_obj.HasAnyGhostCells()
        return ret
        

    def has_any_ghost_points(self):
        """
        V.has_any_ghost_points() -> bool
        C++: bool HasAnyGhostPoints()
        Returns 1 if there are any ghost points 0 otherwise.
        """
        ret = self._vtk_obj.HasAnyGhostPoints()
        return ret
        

    def new_cell_iterator(self):
        """
        V.new_cell_iterator() -> CellIterator
        C++: virtual CellIterator *NewCellIterator()
        Return an iterator that traverses the cells in this data set.
        """
        ret = wrap_vtk(self._vtk_obj.NewCellIterator())
        return ret
        

    def squeeze(self):
        """
        V.squeeze()
        C++: virtual void Squeeze()
        Reclaim any extra memory used to store data. THIS METHOD IS NOT
        THREAD SAFE.
        """
        ret = self._vtk_obj.Squeeze()
        return ret
        

    def update_cell_ghost_array_cache(self):
        """
        V.update_cell_ghost_array_cache()
        C++: void UpdateCellGhostArrayCache()
        Updates the pointer to the cell ghost array.
        """
        ret = self._vtk_obj.UpdateCellGhostArrayCache()
        return ret
        

    def update_point_ghost_array_cache(self):
        """
        V.update_point_ghost_array_cache()
        C++: void UpdatePointGhostArrayCache()
        Updates the pointer to the point ghost array.
        """
        ret = self._vtk_obj.UpdatePointGhostArrayCache()
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
            return super(DataSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit DataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


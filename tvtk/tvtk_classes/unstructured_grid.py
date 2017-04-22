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

from tvtk.tvtk_classes.unstructured_grid_base import UnstructuredGridBase


class UnstructuredGrid(UnstructuredGridBase):
    """
    UnstructuredGrid - dataset represents arbitrary combinations of
    all possible cell types
    
    Superclass: UnstructuredGridBase
    
    UnstructuredGrid is a data object that is a concrete
    implementation of DataSet. UnstructuredGrid represents any
    combinations of any cell types. This includes 0d (e.g., points), 1d
    (e.g., lines, polylines), 2d (e.g., triangles, polygons), and 3d
    (e.g., hexahedron, tetrahedron, polyhedron, etc.).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGrid, obj, update, **traits)
    
    def get_cells(self):
        """
        V.get_cells() -> CellArray
        C++: CellArray *GetCells()"""
        ret = wrap_vtk(self._vtk_obj.GetCells())
        return ret
        

    def set_cells(self, *args):
        """
        V.set_cells(int, CellArray)
        C++: void SetCells(int type, CellArray *cells)
        V.set_cells([int, ...], CellArray)
        C++: void SetCells(int *types, CellArray *cells)
        V.set_cells(UnsignedCharArray, IdTypeArray, CellArray)
        C++: void SetCells(UnsignedCharArray *cellTypes,
            IdTypeArray *cellLocations, CellArray *cells)
        V.set_cells(UnsignedCharArray, IdTypeArray, CellArray,
            IdTypeArray, IdTypeArray)
        C++: void SetCells(UnsignedCharArray *cellTypes,
            IdTypeArray *cellLocations, CellArray *cells,
            IdTypeArray *faceLocations, IdTypeArray *faces)
        Special methods specific to UnstructuredGrid for defining the
        cells composing the dataset. Most cells require just arrays of
        cell_types, cell_locations and cell_connectivities which implicitly
        define the set of points in each cell and their ordering. In
        those cases the cell_connectivities are of the format
        (num_face0_pts, id1, id2, id3, num_face1_pts, id1, id2, id3...).
        However, some cells like Polyhedron require points plus a list
        of faces. To handle Polyhedron, set_cells() support a special
        input cell_connectivities format (num_cell_faces, num_face0_pts, id1,
        id2, id3, num_face1_pts,id_1, id2, id3, ...) The functions use
        Polyhedron::DecomposeAPolyhedronCell() to convert polyhedron
        cells into standard format.
        """
        my_args = deref_array(args, [('int', 'vtkCellArray'), (['int', Ellipsis], 'vtkCellArray'), ('vtkUnsignedCharArray', 'vtkIdTypeArray', 'vtkCellArray'), ('vtkUnsignedCharArray', 'vtkIdTypeArray', 'vtkCellArray', 'vtkIdTypeArray', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.SetCells, *my_args)
        return ret

    def _get_cell_links(self):
        return wrap_vtk(self._vtk_obj.GetCellLinks())
    cell_links = traits.Property(_get_cell_links, help=\
        """
        
        """
    )

    def _get_cell_locations_array(self):
        return wrap_vtk(self._vtk_obj.GetCellLocationsArray())
    cell_locations_array = traits.Property(_get_cell_locations_array, help=\
        """
        
        """
    )

    def _get_cell_types_array(self):
        return wrap_vtk(self._vtk_obj.GetCellTypesArray())
    cell_types_array = traits.Property(_get_cell_types_array, help=\
        """
        
        """
    )

    def _get_face_locations(self):
        return wrap_vtk(self._vtk_obj.GetFaceLocations())
    face_locations = traits.Property(_get_face_locations, help=\
        """
        Get pointer to faces and facelocations. Support for polyhedron
        cells.
        """
    )

    def get_face_stream(self, *args):
        """
        V.get_face_stream(int, IdList)
        C++: void GetFaceStream(IdType cellId, IdList *ptIds)
        Get the face stream of a polyhedron cell in the following format:
        (num_cell_faces, num_face0_pts, id1, id2, id3, num_face1_pts,id_1, id2,
        id3, ...). If the requested cell is not a polyhedron, then the
        standard get_cell_points is called to return a list of unique point
        ids (id1, id2, id3, ...).
        """
        my_args = deref_array(args, [('int', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetFaceStream, *my_args)
        return ret

    def _get_faces(self):
        return wrap_vtk(self._vtk_obj.GetFaces())
    faces = traits.Property(_get_faces, help=\
        """
        Special support for polyhedron. Return NULL for all other cell
        types.
        """
    )

    def _get_ghost_level(self):
        return self._vtk_obj.GetGhostLevel()
    ghost_level = traits.Property(_get_ghost_level, help=\
        """
        Get the ghost level.
        """
    )

    def _get_number_of_pieces(self):
        return self._vtk_obj.GetNumberOfPieces()
    number_of_pieces = traits.Property(_get_number_of_pieces, help=\
        """
        Set / Get the piece and the number of pieces. Similar to extent
        in 3d.
        """
    )

    def _get_piece(self):
        return self._vtk_obj.GetPiece()
    piece = traits.Property(_get_piece, help=\
        """
        Set / Get the piece and the number of pieces. Similar to extent
        in 3d.
        """
    )

    def add_reference_to_cell(self, *args):
        """
        V.add_reference_to_cell(int, int)
        C++: void AddReferenceToCell(IdType ptId, IdType cellId)"""
        ret = self._wrap_call(self._vtk_obj.AddReferenceToCell, *args)
        return ret

    def build_links(self):
        """
        V.build_links()
        C++: void BuildLinks()"""
        ret = self._vtk_obj.BuildLinks()
        return ret
        

    def convert_face_stream_point_ids(self, *args):
        """
        V.convert_face_stream_point_ids(IdList, [int, ...])
        C++: static void ConvertFaceStreamPointIds(IdList *faceStream,
            IdType *idMap)
        V.convert_face_stream_point_ids(int, [int, ...], [int, ...])
        C++: static void ConvertFaceStreamPointIds(IdType nfaces,
            IdType *faceStream, IdType *idMap)
        Convert pid in a face stream into id_map[pid]. The face stream is
        of format [n_cell_faces, n_face0_pts, i, j, k, n_face1_pts, i, j, k,
        ...]. The user is responsible to make sure all the Ids in
        face_stream do not exceed the range of id_map.
        """
        my_args = deref_array(args, [('vtkIdList', ['int', Ellipsis]), ('int', ['int', Ellipsis], ['int', Ellipsis])])
        ret = self._wrap_call(self._vtk_obj.ConvertFaceStreamPointIds, *my_args)
        return ret

    def decompose_a_polyhedron_cell(self, *args):
        """
        V.decompose_a_polyhedron_cell(CellArray, int, int, CellArray,
            IdTypeArray)
        C++: static void DecomposeAPolyhedronCell(
            CellArray *polyhedronCellArray, IdType &nCellpts,
            IdType &nCellfaces, CellArray *cellArray,
            IdTypeArray *faces)
        V.decompose_a_polyhedron_cell([int, ...], int, int, CellArray,
            IdTypeArray)
        C++: static void DecomposeAPolyhedronCell(
            IdType *polyhedronCellStream, IdType &nCellpts,
            IdType &nCellfaces, CellArray *cellArray,
            IdTypeArray *faces)
        V.decompose_a_polyhedron_cell(int, [int, ...], int, CellArray,
            IdTypeArray)
        C++: static void DecomposeAPolyhedronCell(IdType nCellFaces,
            IdType *inFaceStream, IdType &nCellpts,
            CellArray *cellArray, IdTypeArray *faces)
        A static method for converting a polyhedron CellArray of
        format [n_cell_faces, n_face0_pts, i, j, k, n_face1_pts, i, j, k, ...]
        into three components: (1) an integer indicating the number of
        faces (2) a standard CellArray storing point ids [n_cell0_pts,
        i, j, k] and (3) an IdTypeArray storing face connectivity in
        format [n_face0_pts, i, j, k, n_face1_pts, i, j, k, ...] Note: input
        is assumed to contain only one polyhedron cell. Outputs (2) and
        (3) will be stacked at the end of the input cell_array and faces.
        The original data in the input will not be touched.
        """
        my_args = deref_array(args, [('vtkCellArray', 'int', 'int', 'vtkCellArray', 'vtkIdTypeArray'), (['int', Ellipsis], 'int', 'int', 'vtkCellArray', 'vtkIdTypeArray'), ('int', ['int', Ellipsis], 'int', 'vtkCellArray', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.DecomposeAPolyhedronCell, *my_args)
        return ret

    def initialize_faces_representation(self, *args):
        """
        V.initialize_faces_representation(int) -> int
        C++: int InitializeFacesRepresentation(IdType numPrevCells)
        Special function used by UnstructuredGridReader. By default
        UnstructuredGrid does not contain face information, which is
        only used by polyhedron cells. If so far no polyhedron cells have
        been added, Faces and face_locations pointers will be NULL. In
        this case, need to initialize the arrays and assign values to the
        previous non-polyhedron cells.
        """
        ret = self._wrap_call(self._vtk_obj.InitializeFacesRepresentation, *args)
        return ret

    def insert_next_linked_cell(self, *args):
        """
        V.insert_next_linked_cell(int, int, [int, ...]) -> int
        C++: IdType InsertNextLinkedCell(int type, int npts,
            IdType *pts)"""
        ret = self._wrap_call(self._vtk_obj.InsertNextLinkedCell, *args)
        return ret

    def remove_ghost_cells(self):
        """
        V.remove_ghost_cells()
        C++: void RemoveGhostCells()
        This method will remove any cell that is marked as ghost (has the
        DataSetAttributes::DUPLICATECELL bit set).
        """
        ret = self._vtk_obj.RemoveGhostCells()
        return ret
        

    def remove_reference_to_cell(self, *args):
        """
        V.remove_reference_to_cell(int, int)
        C++: void RemoveReferenceToCell(IdType ptId, IdType cellId)"""
        ret = self._wrap_call(self._vtk_obj.RemoveReferenceToCell, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Standard DataSet methods; see DataSet.h for documentation.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def resize_cell_list(self, *args):
        """
        V.resize_cell_list(int, int)
        C++: void ResizeCellList(IdType ptId, int size)"""
        ret = self._wrap_call(self._vtk_obj.ResizeCellList, *args)
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
            return super(UnstructuredGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit UnstructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


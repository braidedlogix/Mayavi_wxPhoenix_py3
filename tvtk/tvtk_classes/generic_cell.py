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

from tvtk.tvtk_classes.cell import Cell


class GenericCell(Cell):
    """
    GenericCell - provides thread-safe access to cells
    
    Superclass: Cell
    
    GenericCell is a class that provides access to concrete types of
    cells. It's main purpose is to allow thread-safe access to cells,
    supporting the DataSet::GetCell(vtkGenericCell *) method.
    GenericCell acts like any type of cell, it just dereferences an
    internal representation. The set_cell_type() methods use #define
    constants; these are defined in the file CellType.h.
    
    @sa
    Cell DataSet
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericCell, obj, update, **traits)
    
    def _get_faces(self):
        return self._vtk_obj.GetFaces()
    def _set_faces(self, arg):
        old_val = self._get_faces()
        self._wrap_call(self._vtk_obj.SetFaces,
                        arg)
        self.trait_property_changed('faces', old_val, arg)
    faces = traits.Property(_get_faces, _set_faces, help=\
        """
        See the Cell API for descriptions of these methods.
        """
    )

    def _get_point_ids(self):
        return wrap_vtk(self._vtk_obj.GetPointIds())
    def _set_point_ids(self, arg):
        old_val = self._get_point_ids()
        my_arg = deref_array([arg], [['vtkIdList']])
        self._wrap_call(self._vtk_obj.SetPointIds,
                        my_arg[0])
        self.trait_property_changed('point_ids', old_val, arg)
    point_ids = traits.Property(_get_point_ids, _set_point_ids, help=\
        """
        Return the list of point ids defining the cell.
        """
    )

    def _get_points(self):
        return wrap_vtk(self._vtk_obj.GetPoints())
    def _set_points(self, arg):
        old_val = self._get_points()
        my_arg = deref_array([arg], [['vtkPoints']])
        self._wrap_call(self._vtk_obj.SetPoints,
                        my_arg[0])
        self.trait_property_changed('points', old_val, arg)
    points = traits.Property(_get_points, _set_points, help=\
        """
        Get the point coordinates for the cell.
        """
    )

    def _get_representative_cell(self):
        return wrap_vtk(self._vtk_obj.GetRepresentativeCell())
    representative_cell = traits.Property(_get_representative_cell, help=\
        """
        
        """
    )

    def instantiate_cell(self, *args):
        """
        V.instantiate_cell(int) -> Cell
        C++: static Cell *InstantiateCell(int cellType)
        Instantiate a new Cell based on it's cell type value
        """
        ret = self._wrap_call(self._vtk_obj.InstantiateCell, *args)
        return wrap_vtk(ret)

    def set_cell_type(self, *args):
        """
        V.set_cell_type(int)
        C++: void SetCellType(int cellType)
        This method is used to support the
        DataSet::GetCell(vtkGenericCell *) method. It allows
        GenericCell to act like any cell type by dereferencing an
        internal instance of a concrete cell type. When you set the cell
        type, you are resetting a pointer to an internal cell which is
        then used for computation.
        """
        ret = self._wrap_call(self._vtk_obj.SetCellType, *args)
        return ret

    def set_cell_type_to_bi_quadratic_quad(self):
        """
        V.set_cell_type_to_bi_quadratic_quad()
        C++: void SetCellTypeToBiQuadraticQuad()"""
        ret = self._vtk_obj.SetCellTypeToBiQuadraticQuad()
        return ret
        

    def set_cell_type_to_bi_quadratic_quadratic_hexahedron(self):
        """
        V.set_cell_type_to_bi_quadratic_quadratic_hexahedron()
        C++: void SetCellTypeToBiQuadraticQuadraticHexahedron()"""
        ret = self._vtk_obj.SetCellTypeToBiQuadraticQuadraticHexahedron()
        return ret
        

    def set_cell_type_to_bi_quadratic_quadratic_wedge(self):
        """
        V.set_cell_type_to_bi_quadratic_quadratic_wedge()
        C++: void SetCellTypeToBiQuadraticQuadraticWedge()"""
        ret = self._vtk_obj.SetCellTypeToBiQuadraticQuadraticWedge()
        return ret
        

    def set_cell_type_to_bi_quadratic_triangle(self):
        """
        V.set_cell_type_to_bi_quadratic_triangle()
        C++: void SetCellTypeToBiQuadraticTriangle()"""
        ret = self._vtk_obj.SetCellTypeToBiQuadraticTriangle()
        return ret
        

    def set_cell_type_to_convex_point_set(self):
        """
        V.set_cell_type_to_convex_point_set()
        C++: void SetCellTypeToConvexPointSet()"""
        ret = self._vtk_obj.SetCellTypeToConvexPointSet()
        return ret
        

    def set_cell_type_to_cubic_line(self):
        """
        V.set_cell_type_to_cubic_line()
        C++: void SetCellTypeToCubicLine()"""
        ret = self._vtk_obj.SetCellTypeToCubicLine()
        return ret
        

    def set_cell_type_to_empty_cell(self):
        """
        V.set_cell_type_to_empty_cell()
        C++: void SetCellTypeToEmptyCell()"""
        ret = self._vtk_obj.SetCellTypeToEmptyCell()
        return ret
        

    def set_cell_type_to_hexagonal_prism(self):
        """
        V.set_cell_type_to_hexagonal_prism()
        C++: void SetCellTypeToHexagonalPrism()"""
        ret = self._vtk_obj.SetCellTypeToHexagonalPrism()
        return ret
        

    def set_cell_type_to_hexahedron(self):
        """
        V.set_cell_type_to_hexahedron()
        C++: void SetCellTypeToHexahedron()"""
        ret = self._vtk_obj.SetCellTypeToHexahedron()
        return ret
        

    def set_cell_type_to_line(self):
        """
        V.set_cell_type_to_line()
        C++: void SetCellTypeToLine()"""
        ret = self._vtk_obj.SetCellTypeToLine()
        return ret
        

    def set_cell_type_to_pentagonal_prism(self):
        """
        V.set_cell_type_to_pentagonal_prism()
        C++: void SetCellTypeToPentagonalPrism()"""
        ret = self._vtk_obj.SetCellTypeToPentagonalPrism()
        return ret
        

    def set_cell_type_to_pixel(self):
        """
        V.set_cell_type_to_pixel()
        C++: void SetCellTypeToPixel()"""
        ret = self._vtk_obj.SetCellTypeToPixel()
        return ret
        

    def set_cell_type_to_poly_line(self):
        """
        V.set_cell_type_to_poly_line()
        C++: void SetCellTypeToPolyLine()"""
        ret = self._vtk_obj.SetCellTypeToPolyLine()
        return ret
        

    def set_cell_type_to_poly_vertex(self):
        """
        V.set_cell_type_to_poly_vertex()
        C++: void SetCellTypeToPolyVertex()"""
        ret = self._vtk_obj.SetCellTypeToPolyVertex()
        return ret
        

    def set_cell_type_to_polygon(self):
        """
        V.set_cell_type_to_polygon()
        C++: void SetCellTypeToPolygon()"""
        ret = self._vtk_obj.SetCellTypeToPolygon()
        return ret
        

    def set_cell_type_to_polyhedron(self):
        """
        V.set_cell_type_to_polyhedron()
        C++: void SetCellTypeToPolyhedron()"""
        ret = self._vtk_obj.SetCellTypeToPolyhedron()
        return ret
        

    def set_cell_type_to_pyramid(self):
        """
        V.set_cell_type_to_pyramid()
        C++: void SetCellTypeToPyramid()"""
        ret = self._vtk_obj.SetCellTypeToPyramid()
        return ret
        

    def set_cell_type_to_quad(self):
        """
        V.set_cell_type_to_quad()
        C++: void SetCellTypeToQuad()"""
        ret = self._vtk_obj.SetCellTypeToQuad()
        return ret
        

    def set_cell_type_to_quadratic_edge(self):
        """
        V.set_cell_type_to_quadratic_edge()
        C++: void SetCellTypeToQuadraticEdge()"""
        ret = self._vtk_obj.SetCellTypeToQuadraticEdge()
        return ret
        

    def set_cell_type_to_quadratic_hexahedron(self):
        """
        V.set_cell_type_to_quadratic_hexahedron()
        C++: void SetCellTypeToQuadraticHexahedron()"""
        ret = self._vtk_obj.SetCellTypeToQuadraticHexahedron()
        return ret
        

    def set_cell_type_to_quadratic_linear_quad(self):
        """
        V.set_cell_type_to_quadratic_linear_quad()
        C++: void SetCellTypeToQuadraticLinearQuad()"""
        ret = self._vtk_obj.SetCellTypeToQuadraticLinearQuad()
        return ret
        

    def set_cell_type_to_quadratic_linear_wedge(self):
        """
        V.set_cell_type_to_quadratic_linear_wedge()
        C++: void SetCellTypeToQuadraticLinearWedge()"""
        ret = self._vtk_obj.SetCellTypeToQuadraticLinearWedge()
        return ret
        

    def set_cell_type_to_quadratic_polygon(self):
        """
        V.set_cell_type_to_quadratic_polygon()
        C++: void SetCellTypeToQuadraticPolygon()"""
        ret = self._vtk_obj.SetCellTypeToQuadraticPolygon()
        return ret
        

    def set_cell_type_to_quadratic_pyramid(self):
        """
        V.set_cell_type_to_quadratic_pyramid()
        C++: void SetCellTypeToQuadraticPyramid()"""
        ret = self._vtk_obj.SetCellTypeToQuadraticPyramid()
        return ret
        

    def set_cell_type_to_quadratic_quad(self):
        """
        V.set_cell_type_to_quadratic_quad()
        C++: void SetCellTypeToQuadraticQuad()"""
        ret = self._vtk_obj.SetCellTypeToQuadraticQuad()
        return ret
        

    def set_cell_type_to_quadratic_tetra(self):
        """
        V.set_cell_type_to_quadratic_tetra()
        C++: void SetCellTypeToQuadraticTetra()"""
        ret = self._vtk_obj.SetCellTypeToQuadraticTetra()
        return ret
        

    def set_cell_type_to_quadratic_triangle(self):
        """
        V.set_cell_type_to_quadratic_triangle()
        C++: void SetCellTypeToQuadraticTriangle()"""
        ret = self._vtk_obj.SetCellTypeToQuadraticTriangle()
        return ret
        

    def set_cell_type_to_quadratic_wedge(self):
        """
        V.set_cell_type_to_quadratic_wedge()
        C++: void SetCellTypeToQuadraticWedge()"""
        ret = self._vtk_obj.SetCellTypeToQuadraticWedge()
        return ret
        

    def set_cell_type_to_tetra(self):
        """
        V.set_cell_type_to_tetra()
        C++: void SetCellTypeToTetra()"""
        ret = self._vtk_obj.SetCellTypeToTetra()
        return ret
        

    def set_cell_type_to_tri_quadratic_hexahedron(self):
        """
        V.set_cell_type_to_tri_quadratic_hexahedron()
        C++: void SetCellTypeToTriQuadraticHexahedron()"""
        ret = self._vtk_obj.SetCellTypeToTriQuadraticHexahedron()
        return ret
        

    def set_cell_type_to_triangle(self):
        """
        V.set_cell_type_to_triangle()
        C++: void SetCellTypeToTriangle()"""
        ret = self._vtk_obj.SetCellTypeToTriangle()
        return ret
        

    def set_cell_type_to_triangle_strip(self):
        """
        V.set_cell_type_to_triangle_strip()
        C++: void SetCellTypeToTriangleStrip()"""
        ret = self._vtk_obj.SetCellTypeToTriangleStrip()
        return ret
        

    def set_cell_type_to_vertex(self):
        """
        V.set_cell_type_to_vertex()
        C++: void SetCellTypeToVertex()"""
        ret = self._vtk_obj.SetCellTypeToVertex()
        return ret
        

    def set_cell_type_to_voxel(self):
        """
        V.set_cell_type_to_voxel()
        C++: void SetCellTypeToVoxel()"""
        ret = self._vtk_obj.SetCellTypeToVoxel()
        return ret
        

    def set_cell_type_to_wedge(self):
        """
        V.set_cell_type_to_wedge()
        C++: void SetCellTypeToWedge()"""
        ret = self._vtk_obj.SetCellTypeToWedge()
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
            return super(GenericCell, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericCell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit GenericCell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericCell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


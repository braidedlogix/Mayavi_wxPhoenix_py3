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


class Cell(Object):
    """
    Cell - abstract class to specify cell behavior
    
    Superclass: Object
    
    Cell is an abstract class that specifies the interfaces for data
    cells. Data cells are simple topological elements like points, lines,
    polygons, and tetrahedra of which visualization datasets are
    composed. In some cases visualization datasets may explicitly
    represent cells (e.g., PolyData, UnstructuredGrid), and in some
    cases, the datasets are implicitly composed of cells (e.g.,
    StructuredPoints).
    
    @warning
    The #define VTK_CELL_SIZE is a parameter used to construct cells and
    provide a general guideline for controlling object execution. This
    parameter is not a hard boundary: you can create cells with more
    points.
    
    @sa
    Hexahedron Line Pixel PolyLine PolyVertex Polygon
    Quad Tetra Triangle TriangleStrip Vertex Voxel
    Wedge Pyramid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCell, obj, update, **traits)
    
    def _get_faces(self):
        return self._vtk_obj.GetFaces()
    def _set_faces(self, arg):
        old_val = self._get_faces()
        self._wrap_call(self._vtk_obj.SetFaces,
                        arg)
        self.trait_property_changed('faces', old_val, arg)
    faces = traits.Property(_get_faces, _set_faces, help=\
        """
        
        """
    )

    def _get_bounds(self):
        return self._vtk_obj.GetBounds()
    bounds = traits.Property(_get_bounds, help=\
        """
        Compute cell bounding box (xmin,xmax,ymin,ymax,zmin,zmax). Copy
        result into user provided array.
        """
    )

    def _get_cell_dimension(self):
        return self._vtk_obj.GetCellDimension()
    cell_dimension = traits.Property(_get_cell_dimension, help=\
        """
        Return the topological dimensional of the cell (0,1,2, or 3).
        """
    )

    def _get_cell_type(self):
        return self._vtk_obj.GetCellType()
    cell_type = traits.Property(_get_cell_type, help=\
        """
        Return the type of cell.
        """
    )

    def get_edge(self, *args):
        """
        V.get_edge(int) -> Cell
        C++: virtual Cell *GetEdge(int edgeId)
        Return the edge cell from the edge_id of the cell.
        """
        ret = self._wrap_call(self._vtk_obj.GetEdge, *args)
        return wrap_vtk(ret)

    def get_face(self, *args):
        """
        V.get_face(int) -> Cell
        C++: virtual Cell *GetFace(int faceId)
        Return the face cell from the face_id of the cell.
        """
        ret = self._wrap_call(self._vtk_obj.GetFace, *args)
        return wrap_vtk(ret)

    def _get_length2(self):
        return self._vtk_obj.GetLength2()
    length2 = traits.Property(_get_length2, help=\
        """
        Compute Length squared of cell (i.e., bounding box diagonal
        squared).
        """
    )

    def _get_number_of_edges(self):
        return self._vtk_obj.GetNumberOfEdges()
    number_of_edges = traits.Property(_get_number_of_edges, help=\
        """
        Return the number of edges in the cell.
        """
    )

    def _get_number_of_faces(self):
        return self._vtk_obj.GetNumberOfFaces()
    number_of_faces = traits.Property(_get_number_of_faces, help=\
        """
        Return the number of faces in the cell.
        """
    )

    def _get_number_of_points(self):
        return self._vtk_obj.GetNumberOfPoints()
    number_of_points = traits.Property(_get_number_of_points, help=\
        """
        Return the number of points in the cell.
        """
    )

    def get_parametric_center(self, *args):
        """
        V.get_parametric_center([float, float, float]) -> int
        C++: virtual int GetParametricCenter(double pcoords[3])
        Return center of the cell in parametric coordinates.  Note that
        the parametric center is not always located at (0.5,0.5,0.5). The
        return value is the sub_id that the center is in (if a composite
        cell). If you want the center in x-y-z space, invoke the
        evaluate_location() method.
        """
        ret = self._wrap_call(self._vtk_obj.GetParametricCenter, *args)
        return ret

    def _get_parametric_coords(self):
        return self._vtk_obj.GetParametricCoords()
    parametric_coords = traits.Property(_get_parametric_coords, help=\
        """
        Return a contiguous array of parametric coordinates of the points
        defining this cell. In other words, (px,py,pz, px,py,pz, etc..) 
        The coordinates are ordered consistent with the definition of the
        point ordering for the cell. This method returns a non-NULL
        pointer when the cell is a primary type (i.e., is_primary_cell() is
        true). Note that 3d parametric coordinates are returned no matter
        what the topological dimension of the cell.
        """
    )

    def get_parametric_distance(self, *args):
        """
        V.get_parametric_distance([float, float, float]) -> float
        C++: virtual double GetParametricDistance(double pcoords[3])
        Return the distance of the parametric coordinate provided to the
        cell. If inside the cell, a distance of zero is returned. This is
        used during picking to get the correct cell picked. (The
        tolerance will occasionally allow cells to be picked who are not
        really intersected "inside" the cell.)
        """
        ret = self._wrap_call(self._vtk_obj.GetParametricDistance, *args)
        return ret

    def get_point_id(self, *args):
        """
        V.get_point_id(int) -> int
        C++: IdType GetPointId(int ptId)
        For cell point i, return the actual point id.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointId, *args)
        return ret

    def _get_point_ids(self):
        return wrap_vtk(self._vtk_obj.GetPointIds())
    point_ids = traits.Property(_get_point_ids, help=\
        """
        Return the list of point ids defining the cell.
        """
    )

    def _get_points(self):
        return wrap_vtk(self._vtk_obj.GetPoints())
    points = traits.Property(_get_points, help=\
        """
        Get the point coordinates for the cell.
        """
    )

    def cell_boundary(self, *args):
        """
        V.cell_boundary(int, [float, float, float], IdList) -> int
        C++: virtual int CellBoundary(int subId, double pcoords[3],
            IdList *pts)
        Given parametric coordinates of a point, return the closest cell
        boundary, and whether the point is inside or outside of the cell.
        The cell boundary is defined by a list of points (pts) that
        specify a face (_3d cell), edge (_2d cell), or vertex (_1d cell). If
        the return value of the method is != 0, then the point is inside
        the cell.
        """
        my_args = deref_array(args, [('int', ['float', 'float', 'float'], 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.CellBoundary, *my_args)
        return ret

    def clip(self, *args):
        """
        V.clip(float, DataArray, IncrementalPointLocator,
            CellArray, PointData, PointData, CellData, int,
            CellData, int)
        C++: virtual void Clip(double value, DataArray *cellScalars,
            IncrementalPointLocator *locator,
            CellArray *connectivity, PointData *inPd,
            PointData *outPd, CellData *inCd, IdType cellId,
            CellData *outCd, int insideOut)
        Cut (or clip) the cell based on the input cell_scalars and the
        specified value. The output of the clip operation will be one or
        more cells of the same topological dimension as the original
        cell. The flag inside_out controls what part of the cell is
        considered inside - normally cell points whose scalar value is
        greater than "value" are considered inside. If inside_out is on,
        this is reversed. Also, if the output cell data is non-NULL, the
        cell data from the clipped cell is passed to the generated
        contouring primitives. (Note: the copy_allocate() method must be
        invoked on both the output cell and point data. The cell_id refers
        to the cell from which the cell data is copied.)
        """
        my_args = deref_array(args, [('float', 'vtkDataArray', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkPointData', 'vtkPointData', 'vtkCellData', 'int', 'vtkCellData', 'int')])
        ret = self._wrap_call(self._vtk_obj.Clip, *my_args)
        return ret

    def contour(self, *args):
        """
        V.contour(float, DataArray, IncrementalPointLocator,
            CellArray, CellArray, CellArray, PointData,
            PointData, CellData, int, CellData)
        C++: virtual void Contour(double value, DataArray *cellScalars,
             IncrementalPointLocator *locator, CellArray *verts,
            CellArray *lines, CellArray *polys, PointData *inPd,
            PointData *outPd, CellData *inCd, IdType cellId,
            CellData *outCd)
        Generate contouring primitives. The scalar list cell_scalars are
        scalar values at each cell point. The point locator is
        essentially a points list that merges points as they are inserted
        (i.e., prevents duplicates). Contouring primitives can be
        vertices, lines, or polygons. It is possible to interpolate point
        data along the edge by providing input and output point data - if
        out_pd is NULL, then no interpolation is performed. Also, if the
        output cell data is non-NULL, the cell data from the contoured
        cell is passed to the generated contouring primitives. (Note: the
        copy_allocate() method must be invoked on both the output cell and
        point data. The cell_id refers to the cell from which the cell
        data is copied.)
        """
        my_args = deref_array(args, [('float', 'vtkDataArray', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkCellArray', 'vtkCellArray', 'vtkPointData', 'vtkPointData', 'vtkCellData', 'int', 'vtkCellData')])
        ret = self._wrap_call(self._vtk_obj.Contour, *my_args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(Cell)
        C++: virtual void DeepCopy(Cell *c)
        Copy this cell by completely copying internal data structures.
        This is slower but safer than shallow_copy().
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def derivatives(self, *args):
        """
        V.derivatives(int, [float, float, float], [float, ...], int,
            [float, ...])
        C++: virtual void Derivatives(int subId, double pcoords[3],
            double *values, int dim, double *derivs)
        Compute derivatives given cell sub_id and parametric coordinates.
        The values array is a series of data value(s) at the cell points.
        There is a one-to-one correspondence between cell point and data
        value(s). Dim is the number of data values per cell point. Derivs
        are derivatives in the x-y-z coordinate directions for each data
        value. Thus, if computing derivatives for a scalar function in a
        hexahedron, dim=1, 8 values are supplied, and 3 deriv values are
        returned (i.e., derivatives in x-y-z directions). On the other
        hand, if computing derivatives of velocity (vx,vy,vz) dim=3, 24
        values are supplied ((vx,vy,vz)1, (vx,vy,vz)2, ....()8), and 9
        deriv values are returned ((d(vx)/dx),(d(vx)/dy),(d(vx)/dz),
        (d(vy)/dx),(d(vy)/dy), (d(vy)/dz),
        (d(vz)/dx),(d(vz)/dy),(d(vz)/dz)).
        """
        ret = self._wrap_call(self._vtk_obj.Derivatives, *args)
        return ret

    def evaluate_location(self, *args):
        """
        V.evaluate_location(int, [float, float, float], [float, float,
            float], [float, ...])
        C++: virtual void EvaluateLocation(int &subId, double pcoords[3],
            double x[3], double *weights)
        Determine global coordinate (x[3]) from sub_id and parametric
        coordinates. Also returns interpolation weights. (The number of
        weights is equal to the number of points in the cell.)
        """
        ret = self._wrap_call(self._vtk_obj.EvaluateLocation, *args)
        return ret

    def evaluate_position(self, *args):
        """
        V.evaluate_position([float, float, float], [float, ...], int,
            [float, float, float], float, [float, ...]) -> int
        C++: virtual int EvaluatePosition(double x[3],
            double *closestPoint, int &subId, double pcoords[3],
            double &dist2, double *weights)
        Given a point x[3] return inside(=1), outside(=0) cell, or (-1)
        computational problem encountered; evaluate parametric
        coordinates, sub-cell id (!=0 only if cell is composite),
        distance squared of point x[3] to cell (in particular, the
        sub-cell indicated), closest point on cell to x[3] (unless
        closest_point is null, in which case, the closest point and dist2
        are not found), and interpolation weights in cell. (The number of
        weights is equal to the number of points defining the cell).
        Note: on rare occasions a -1 is returned from the method. This
        means that numerical error has occurred and all data returned
        from this method should be ignored. Also, inside/outside is
        determine parametrically. That is, a point is inside if it
        satisfies parametric limits. This can cause problems for cells of
        topological dimension 2 or less, since a point in 3d can project
        onto the cell within parametric limits but be "far" from the
        cell.  Thus the value dist2 may be checked to determine true
        in/out.
        """
        ret = self._wrap_call(self._vtk_obj.EvaluatePosition, *args)
        return ret

    def initialize(self, *args):
        """
        V.initialize(int, [int, ...], Points)
        C++: void Initialize(int npts, IdType *pts, Points *p)
        V.initialize()
        C++: virtual void Initialize()
        Initialize cell from outside with point ids and point coordinates
        specified.
        """
        my_args = deref_array(args, [('int', ['int', Ellipsis], 'vtkPoints'), None])
        ret = self._wrap_call(self._vtk_obj.Initialize, *my_args)
        return ret

    def interpolate_derivs(self, *args):
        """
        V.interpolate_derivs([float, float, float], [float, ...])
        C++: virtual void InterpolateDerivs(double pcoords[3],
            double *derivs)"""
        ret = self._wrap_call(self._vtk_obj.InterpolateDerivs, *args)
        return ret

    def interpolate_functions(self, *args):
        """
        V.interpolate_functions([float, float, float], [float, ...])
        C++: virtual void InterpolateFunctions(double pcoords[3],
            double *weight)
        Compute the interpolation functions/derivatives (aka shape
        functions/derivatives) No-ops at this level. Typically overridden
        in subclasses.
        """
        ret = self._wrap_call(self._vtk_obj.InterpolateFunctions, *args)
        return ret

    def intersect_with_line(self, *args):
        """
        V.intersect_with_line([float, float, float], [float, float, float],
            float, float, [float, float, float], [float, float, float],
            int) -> int
        C++: virtual int IntersectWithLine(double p1[3], double p2[3],
            double tol, double &t, double x[3], double pcoords[3],
            int &subId)
        Intersect with a ray. Return parametric coordinates (both line
        and cell) and global intersection coordinates, given ray
        definition p1[3], p2[3] and tolerance tol. The method returns
        non-zero value if intersection occurs. A parametric distance t
        between 0 and 1 along the ray representing the intersection
        point, the point coordinates x[3] in data coordinates and also
        pcoords[3] in parametric coordinates. sub_id is the index within
        the cell if a composed cell like a triangle strip.
        """
        ret = self._wrap_call(self._vtk_obj.IntersectWithLine, *args)
        return ret

    def is_explicit_cell(self):
        """
        V.is_explicit_cell() -> int
        C++: virtual int IsExplicitCell()
        Explicit cells require additional representational information
        beyond the usual cell type and connectivity list information.
        Most cells in VTK are implicit cells.
        """
        ret = self._vtk_obj.IsExplicitCell()
        return ret
        

    def is_linear(self):
        """
        V.is_linear() -> int
        C++: virtual int IsLinear()
        Non-linear cells require special treatment beyond the usual cell
        type and connectivity list information.  Most cells in VTK are
        implicit cells.
        """
        ret = self._vtk_obj.IsLinear()
        return ret
        

    def is_primary_cell(self):
        """
        V.is_primary_cell() -> int
        C++: virtual int IsPrimaryCell()
        Return whether this cell type has a fixed topology or whether the
        topology varies depending on the data (e.g., ConvexPointSet).
        This compares to composite cells that are typically composed of
        primary cells (e.g., a triangle strip composite cell is made up
        of triangle primary cells).
        """
        ret = self._vtk_obj.IsPrimaryCell()
        return ret
        

    def requires_explicit_face_representation(self):
        """
        V.requires_explicit_face_representation() -> int
        C++: virtual int RequiresExplicitFaceRepresentation()
        Determine whether the cell requires explicit face representation,
        and methods for setting and getting the faces (see Polyhedron
        for example usage of these methods).
        """
        ret = self._vtk_obj.RequiresExplicitFaceRepresentation()
        return ret
        

    def requires_initialization(self):
        """
        V.requires_initialization() -> int
        C++: virtual int RequiresInitialization()
        Some cells require initialization prior to access. For example,
        they may have to triangulate themselves or set up internal data
        structures.
        """
        ret = self._vtk_obj.RequiresInitialization()
        return ret
        

    def shallow_copy(self, *args):
        """
        V.shallow_copy(Cell)
        C++: virtual void ShallowCopy(Cell *c)
        Copy this cell by reference counting the internal data
        structures. This is safe if you want a "read-only" copy. If you
        modify the cell you might wish to use deep_copy().
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    def triangulate(self, *args):
        """
        V.triangulate(int, IdList, Points) -> int
        C++: virtual int Triangulate(int index, IdList *ptIds,
            Points *pts)
        Generate simplices of proper dimension. If cell is 3d,
        tetrahedron are generated; if 2d triangles; if 1d lines; if 0d
        points. The form of the output is a sequence of points, each n+1
        points (where n is topological cell dimension) defining a
        simplex. The index is a parameter that controls which
        triangulation to use (if more than one is possible). If numerical
        degeneracy encountered, 0 is returned, otherwise 1 is returned.
        This method does not insert new points: all the points that
        define the simplices are the points that define the cell.
        """
        my_args = deref_array(args, [('int', 'vtkIdList', 'vtkPoints')])
        ret = self._wrap_call(self._vtk_obj.Triangulate, *my_args)
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
            return super(Cell, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Cell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit Cell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Cell properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class Triangle(Cell):
    """
    Triangle - a cell that represents a triangle
    
    Superclass: Cell
    
    Triangle is a concrete implementation of Cell to represent a
    triangle located in 3-space.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTriangle, obj, update, **traits)
    
    def get_edge_array(self, *args):
        """
        V.get_edge_array(int) -> (int, ...)
        C++: int *GetEdgeArray(int edgeId)
        Return the ids of the vertices defining edge (`edge_id`). Ids are
        related to the cell, not to the dataset.
        """
        ret = self._wrap_call(self._vtk_obj.GetEdgeArray, *args)
        return ret

    def barycentric_coords(self, *args):
        """
        V.barycentric_coords([float, float], [float, float], [float,
            float], [float, float], [float, float, float]) -> int
        C++: static int BarycentricCoords(double x[2], double x1[2],
            double x2[2], double x3[2], double bcoords[3])
        Given a 2d point x[2], determine the barycentric coordinates of
        the point. Barycentric coordinates are a natural coordinate
        system for simplices that express a position as a linear
        combination of the vertices. For a triangle, there are three
        barycentric coordinates (because there are three vertices), and
        the sum of the coordinates must equal 1. If a point x is inside a
        simplex, then all three coordinates will be strictly positive. 
        If two coordinates are zero (so the third =1), then the point x
        is on a vertex. If one coordinates are zero, the point x is on an
        edge. In this method, you must specify the vertex coordinates
        x1->x3. Returns 0 if triangle is degenerate.
        """
        ret = self._wrap_call(self._vtk_obj.BarycentricCoords, *args)
        return ret

    def circumcircle(self, *args):
        """
        V.circumcircle([float, float], [float, float], [float, float],
            [float, float]) -> float
        C++: static double Circumcircle(double p1[2], double p2[2],
            double p3[2], double center[2])
        Compute the circumcenter (center[3]) and radius squared (method
        return value) of a triangle defined by the three points x1, x2,
        and x3. (Note that the coordinates are 2d. 3d points can be used
        but the z-component will be ignored.)
        """
        ret = self._wrap_call(self._vtk_obj.Circumcircle, *args)
        return ret

    def compute_area(self):
        """
        V.compute_area() -> float
        C++: double ComputeArea()
        A convenience function to compute the area of a Triangle.
        """
        ret = self._vtk_obj.ComputeArea()
        return ret
        

    def compute_normal(self, *args):
        """
        V.compute_normal(Points, int, [int, ...], [float, float, float])
        C++: static void ComputeNormal(Points *p, int numPts,
            IdType *pts, double n[3])
        V.compute_normal([float, float, float], [float, float, float],
            [float, float, float], [float, float, float])
        C++: static void ComputeNormal(double v1[3], double v2[3],
            double v3[3], double n[3])
        Compute the triangle normal from a points list, and a list of
        point ids that index into the points list.
        """
        my_args = deref_array(args, [('vtkPoints', 'int', ['int', Ellipsis], ['float', 'float', 'float']), (['float', 'float', 'float'], ['float', 'float', 'float'], ['float', 'float', 'float'], ['float', 'float', 'float'])])
        ret = self._wrap_call(self._vtk_obj.ComputeNormal, *my_args)
        return ret

    def compute_normal_direction(self, *args):
        """
        V.compute_normal_direction([float, float, float], [float, float,
            float], [float, float, float], [float, float, float])
        C++: static void ComputeNormalDirection(double v1[3],
            double v2[3], double v3[3], double n[3])
        Compute the (unnormalized) triangle normal direction from three
        points.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeNormalDirection, *args)
        return ret

    def compute_quadric(self, *args):
        """
        V.compute_quadric([float, float, float], [float, float, float],
            [float, float, float], [[float, float, float, float], [float,
            float, float, float], [float, float, float, float], [float,
            float, float, float]])
        C++: static void ComputeQuadric(double x1[3], double x2[3],
            double x3[3], double quadric[4][4])
        V.compute_quadric([float, float, float], [float, float, float],
            [float, float, float], Quadric)
        C++: static void ComputeQuadric(double x1[3], double x2[3],
            double x3[3], Quadric *quadric)
        Calculate the error quadric for this triangle.  Return the
        quadric as a 4x4 matrix or a Quadric.  (from Peter Lindstrom's
        Siggraph 2000 paper, "Out-of-Core Simplification of Large
        Polygonal Models")
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeQuadric, *my_args)
        return ret

    def interpolation_derivs(self, *args):
        """
        V.interpolation_derivs([float, float, float], [float, float, float,
             float, float, float])
        C++: static void InterpolationDerivs(double pcoords[3],
            double derivs[6])
        @deprecated Replaced by Triangle::InterpolateDerivs as of VTK
        5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationDerivs, *args)
        return ret

    def interpolation_functions(self, *args):
        """
        V.interpolation_functions([float, float, float], [float, float,
            float])
        C++: static void InterpolationFunctions(double pcoords[3],
            double sf[3])
        @deprecated Replaced by Triangle::InterpolateFunctions as of
        VTK 5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationFunctions, *args)
        return ret

    def point_in_triangle(self, *args):
        """
        V.point_in_triangle([float, float, float], [float, float, float],
            [float, float, float], [float, float, float], float) -> int
        C++: static int PointInTriangle(double x[3], double x1[3],
            double x2[3], double x3[3], double tol2)
        Given a point x, determine whether it is inside (within the
        tolerance squared, tol2) the triangle defined by the three
        coordinate values p1, p2, p3. Method is via comparing dot
        products. (Note: in current implementation the tolerance only
        works in the neighborhood of the three vertices of the triangle.
        """
        ret = self._wrap_call(self._vtk_obj.PointInTriangle, *args)
        return ret

    def project_to2d(self, *args):
        """
        V.project_to2d([float, float, float], [float, float, float],
            [float, float, float], [float, float], [float, float], [float,
             float]) -> int
        C++: static int ProjectTo2D(double x1[3], double x2[3],
            double x3[3], double v1[2], double v2[2], double v3[2])
        Project triangle defined in 3d to 2d coordinates. Returns 0 if
        degenerate triangle; non-zero value otherwise. Input points are
        x1->x3; output 2d points are v1->v3.
        """
        ret = self._wrap_call(self._vtk_obj.ProjectTo2D, *args)
        return ret

    def triangle_area(self, *args):
        """
        V.triangle_area([float, float, float], [float, float, float],
            [float, float, float]) -> float
        C++: static double TriangleArea(double p1[3], double p2[3],
            double p3[3])
        Compute the area of a triangle in 3d. See also
        Triangle::ComputeArea()
        """
        ret = self._wrap_call(self._vtk_obj.TriangleArea, *args)
        return ret

    def triangle_center(self, *args):
        """
        V.triangle_center([float, float, float], [float, float, float],
            [float, float, float], [float, float, float])
        C++: static void TriangleCenter(double p1[3], double p2[3],
            double p3[3], double center[3])
        Compute the center of the triangle.
        """
        ret = self._wrap_call(self._vtk_obj.TriangleCenter, *args)
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
            return super(Triangle, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Triangle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit Triangle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Triangle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


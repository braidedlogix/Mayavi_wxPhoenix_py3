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

from tvtk.tvtk_classes.non_linear_cell import NonLinearCell


class QuadraticPolygon(NonLinearCell):
    """
    QuadraticPolygon - a cell that represents a parabolic n-sided
    polygon
    
    Superclass: NonLinearCell
    
    QuadraticPolygon is a concrete implementation of NonLinearCell
    to represent a 2d n-sided (2*n nodes) parabolic polygon. The polygon
    cannot have any internal holes, and cannot self-intersect. The cell
    includes a mid-edge node for each of the n edges of the cell. The
    ordering of the 2*n points defining the cell are point ids (0..n-1
    and n..2*n-1) where ids 0..n-1 define the corner vertices of the
    polygon; ids n..2*n-1 define the midedge nodes. Define the polygon
    with points ordered in the counter- clockwise direction; do not
    repeat the last point.
    
    @sa
    QuadraticEdge QuadraticTriangle QuadraticTetra
    QuadraticHexahedron QuadraticWedge QuadraticPyramid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkQuadraticPolygon, obj, update, **traits)
    
    use_mvc_interpolation = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Set/Get the flag indicating whether to use Mean Value Coordinate
        for the interpolation. If true, interpolate_functions() uses the
        Mean Value Coordinate to compute weights. Otherwise, the
        conventional 1/r^2 method is used. The use_mvc_interpolation
        parameter is set to true by default.
        """
    )

    def _use_mvc_interpolation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseMVCInterpolation,
                        self.use_mvc_interpolation)

    def compute_centroid(self, *args):
        """
        V.compute_centroid(IdTypeArray, Points, [float, float,
            float])
        C++: static void ComputeCentroid(IdTypeArray *ids,
            Points *pts, double centroid[3])
        These methods are based on the Polygon ones : the
        QuadraticPolygon (with n edges and 2*n points) is transform
        into a Polygon (with 2*n edges and 2*n points) and the
        Polygon methods are called.
        """
        my_args = deref_array(args, [('vtkIdTypeArray', 'vtkPoints', ['float', 'float', 'float'])])
        ret = self._wrap_call(self._vtk_obj.ComputeCentroid, *my_args)
        return ret

    def distance_to_polygon(self, *args):
        """
        V.distance_to_polygon([float, float, float], int, [float, ...],
            [float, float, float, float, float, float], [float, float,
            float]) -> float
        C++: static double DistanceToPolygon(double x[3], int numPts,
            double *pts, double bounds[6], double closest[3])
        These methods are based on the Polygon ones : the
        QuadraticPolygon (with n edges and 2*n points) is transform
        into a Polygon (with 2*n edges and 2*n points) and the
        Polygon methods are called.
        """
        ret = self._wrap_call(self._vtk_obj.DistanceToPolygon, *args)
        return ret

    def intersect_convex2d_cells(self, *args):
        """
        V.intersect_convex2d_cells(Cell, Cell, float, [float, float,
            float], [float, float, float]) -> int
        C++: static int IntersectConvex2DCells(Cell *cell1,
            Cell *cell2, double tol, double p0[3], double p1[3])
        These methods are based on the Polygon ones : the
        QuadraticPolygon (with n edges and 2*n points) is transform
        into a Polygon (with 2*n edges and 2*n points) and the
        Polygon methods are called.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IntersectConvex2DCells, *my_args)
        return ret

    def intersect_polygon_with_polygon(self, *args):
        """
        V.intersect_polygon_with_polygon(int, [float, ...], [float, float,
            float, float, float, float], int, [float, ...], [float, float,
             float], float, [float, float, float]) -> int
        C++: static int IntersectPolygonWithPolygon(int npts, double *pts,
             double bounds[6], int npts2, double *pts2, double bounds2[3],
             double tol, double x[3])
        These methods are based on the Polygon ones : the
        QuadraticPolygon (with n edges and 2*n points) is transform
        into a Polygon (with 2*n edges and 2*n points) and the
        Polygon methods are called.
        """
        ret = self._wrap_call(self._vtk_obj.IntersectPolygonWithPolygon, *args)
        return ret

    def non_degenerate_triangulate(self, *args):
        """
        V.non_degenerate_triangulate(IdList) -> int
        C++: int NonDegenerateTriangulate(IdList *outTris)
        These methods are based on the Polygon ones : the
        QuadraticPolygon (with n edges and 2*n points) is transform
        into a Polygon (with 2*n edges and 2*n points) and the
        Polygon methods are called.
        """
        my_args = deref_array(args, [['vtkIdList']])
        ret = self._wrap_call(self._vtk_obj.NonDegenerateTriangulate, *my_args)
        return ret

    def parameterize_polygon(self, *args):
        """
        V.parameterize_polygon([float, float, float], [float, float,
            float], float, [float, float, float], float, [float, float,
            float]) -> int
        C++: int ParameterizePolygon(double p0[3], double p10[3],
            double &l10, double p20[3], double &l20, double n[3])
        These methods are based on the Polygon ones : the
        QuadraticPolygon (with n edges and 2*n points) is transform
        into a Polygon (with 2*n edges and 2*n points) and the
        Polygon methods are called.
        """
        ret = self._wrap_call(self._vtk_obj.ParameterizePolygon, *args)
        return ret

    def point_in_polygon(self, *args):
        """
        V.point_in_polygon([float, float, float], int, [float, ...], [float,
             float, float, float, float, float], [float, float, float])
            -> int
        C++: static int PointInPolygon(double x[3], int numPts,
            double *pts, double bounds[6], double n[3])
        These methods are based on the Polygon ones : the
        QuadraticPolygon (with n edges and 2*n points) is transform
        into a Polygon (with 2*n edges and 2*n points) and the
        Polygon methods are called.
        """
        ret = self._wrap_call(self._vtk_obj.PointInPolygon, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('use_mvc_interpolation',
    'GetUseMVCInterpolation'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'use_mvc_interpolation'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(QuadraticPolygon, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit QuadraticPolygon properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['use_mvc_interpolation']),
            title='Edit QuadraticPolygon properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit QuadraticPolygon properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


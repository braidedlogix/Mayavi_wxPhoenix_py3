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


class Line(Cell):
    """
    Line - cell represents a 1d line
    
    Superclass: Cell
    
    Line is a concrete implementation of Cell to represent a 1d
    line.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLine, obj, update, **traits)
    
    def distance_between_line_segments(self, *args):
        """
        V.distance_between_line_segments([float, float, float], [float,
            float, float], [float, float, float], [float, float, float],
            [float, float, float], [float, float, float], float, float)
            -> float
        C++: static double DistanceBetweenLineSegments(double l0[3],
            double l1[3], double m0[3], double m1[3],
            double closestPt1[3], double closestPt2[3], double &t1,
            double &t2)
        Computes the shortest distance squared between two finite line
        segments defined by their end points (l0,l1) and (m0,m1). Upon
        return, the closest points on the two line segments will be
        stored in closest_pt1 and closest_pt2. Their parametric coords (0
        <= t0, t1 <= 1) will be stored in t0 and t1. The return value is
        the shortest distance squared between the two line-segments.
        """
        ret = self._wrap_call(self._vtk_obj.DistanceBetweenLineSegments, *args)
        return ret

    def distance_between_lines(self, *args):
        """
        V.distance_between_lines([float, float, float], [float, float,
            float], [float, float, float], [float, float, float], [float,
            float, float], [float, float, float], float, float) -> float
        C++: static double DistanceBetweenLines(double l0[3],
            double l1[3], double m0[3], double m1[3],
            double closestPt1[3], double closestPt2[3], double &t1,
            double &t2)
        Computes the shortest distance squared between two infinite
        lines, each defined by a pair of points (l0,l1) and (m0,m1). Upon
        return, the closest points on the two line segments will be
        stored in closest_pt1 and closest_pt2. Their parametric coords
        (-inf <= t0, t1 <= inf) will be stored in t0 and t1. The return
        value is the shortest distance squared between the two
        line-segments.
        """
        ret = self._wrap_call(self._vtk_obj.DistanceBetweenLines, *args)
        return ret

    def distance_to_line(self, *args):
        """
        V.distance_to_line([float, float, float], [float, float, float],
            [float, float, float], float, [float, ...]) -> float
        C++: static double DistanceToLine(double x[3], double p1[3],
            double p2[3], double &t, double *closestPoint=NULL)
        V.distance_to_line([float, float, float], [float, float, float],
            [float, float, float]) -> float
        C++: static double DistanceToLine(double x[3], double p1[3],
            double p2[3])
        Compute the distance of a point x to a finite line (p1,p2). The
        method computes the parametric coordinate t and the point
        location on the line. Note that t is unconstrained (i.e., it may
        lie outside the range [0,1]) but the closest point will lie
        within the finite line [p1,p2], if it is defined. Also, the
        method returns the distance squared between x and the line
        (p1,p2).
        """
        ret = self._wrap_call(self._vtk_obj.DistanceToLine, *args)
        return ret

    def interpolation_derivs(self, *args):
        """
        V.interpolation_derivs([float, float, float], [float, float])
        C++: static void InterpolationDerivs(double pcoords[3],
            double derivs[2])
        @deprecated Replaced by Line::InterpolateDerivs as of VTK 5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationDerivs, *args)
        return ret

    def interpolation_functions(self, *args):
        """
        V.interpolation_functions([float, float, float], [float, float])
        C++: static void InterpolationFunctions(double pcoords[3],
            double weights[2])
        @deprecated Replaced by Line::InterpolateFunctions as of VTK
        5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationFunctions, *args)
        return ret

    def intersection(self, *args):
        """
        V.intersection([float, float, float], [float, float, float],
            [float, float, float], [float, float, float], float, float)
            -> int
        C++: static int Intersection(double p1[3], double p2[3],
            double x1[3], double x2[3], double &u, double &v)
        Performs intersection of the projection of two finite 3d lines
        onto a 2d plane. An intersection is found if the projection of
        the two lines onto the plane perpendicular to the cross product
        of the two lines intersect. The parameters (u,v) are the
        parametric coordinates of the lines at the position of closest
        approach.
        """
        ret = self._wrap_call(self._vtk_obj.Intersection, *args)
        return ret

    def intersection3d(self, *args):
        """
        V.intersection3d([float, float, float], [float, float, float],
            [float, float, float], [float, float, float], float, float)
            -> int
        C++: static int Intersection3D(double p1[3], double p2[3],
            double x1[3], double x2[3], double &u, double &v)
        Performs intersection of two finite 3d lines. An intersection is
        found if the projection of the two lines onto the plane
        perpendicular to the cross product of the two lines intersect,
        and if the distance between the closest points of approach are
        within a relative tolerance. The parameters (u,v) are the
        parametric coordinates of the lines at the position of closest
        approach.
        
        * NOTE: "Unlike Intersection(), which determines whether the
          projections of
        * two lines onto a plane intersect, intersection3d() determines
          whether the
        * lines themselves in 3d space intersect, within a tolerance.
        """
        ret = self._wrap_call(self._vtk_obj.Intersection3D, *args)
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
            return super(Line, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Line properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit Line properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Line properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class BiQuadraticQuadraticWedge(NonLinearCell):
    """
    BiQuadraticQuadraticWedge - cell represents a parabolic, 18-node
    isoparametric wedge
    
    Superclass: NonLinearCell
    
    BiQuadraticQuadraticWedge is a concrete implementation of
    NonLinearCell to represent a three-dimensional, 18-node
    isoparametric biquadratic wedge. The interpolation is the standard
    finite element, biquadratic-quadratic isoparametric shape function
    plus the linear functions. The cell includes a mid-edge node. The
    ordering of the 18 points defining the cell is point ids (0-5,6-15,
    16-18) where point ids 0-5 are the six corner vertices of the wedge;
    followed by nine midedge nodes (6-15) and 3 center-face nodes. Note
    that these midedge nodes correspond lie on the edges defined by
    (0,1), (1,2), (2,0), (3,4), (4,5), (5,3), (0,3), (1,4), (2,5), and
    the center-face nodes are laying in quads 16-(0,1,4,3), 17-(1,2,5,4)
    and (2,0,3,5).
    
    @sa
    QuadraticEdge QuadraticTriangle QuadraticTetra
    QuadraticHexahedron QuadraticQuad QuadraticPyramid
    
    @par Thanks: Thanks to Soeren Gebbert  who developed this class and
    integrated it into VTK 5.0.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBiQuadraticQuadraticWedge, obj, update, **traits)
    
    def get_edge_array(self, *args):
        """
        V.get_edge_array(int) -> (int, ...)
        C++: static int *GetEdgeArray(int edgeId)
        Return the ids of the vertices defining edge/face
        (`edge_id`/`face_id'). Ids are related to the cell, not to the
        dataset.
        """
        ret = self._wrap_call(self._vtk_obj.GetEdgeArray, *args)
        return ret

    def get_face_array(self, *args):
        """
        V.get_face_array(int) -> (int, ...)
        C++: static int *GetFaceArray(int faceId)
        Return the ids of the vertices defining edge/face
        (`edge_id`/`face_id'). Ids are related to the cell, not to the
        dataset.
        """
        ret = self._wrap_call(self._vtk_obj.GetFaceArray, *args)
        return ret

    def interpolation_derivs(self, *args):
        """
        V.interpolation_derivs([float, float, float], [float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float])
        C++: static void InterpolationDerivs(double pcoords[3],
            double derivs[45])
        @deprecated Replaced by
        BiQuadraticQuadraticWedge::InterpolateDerivs as of VTK 5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationDerivs, *args)
        return ret

    def interpolation_functions(self, *args):
        """
        V.interpolation_functions([float, float, float], [float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float])
        C++: static void InterpolationFunctions(double pcoords[3],
            double weights[15])
        @deprecated Replaced by
        BiQuadraticQuadraticWedge::InterpolateFunctions as of VTK 5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationFunctions, *args)
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
            return super(BiQuadraticQuadraticWedge, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BiQuadraticQuadraticWedge properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit BiQuadraticQuadraticWedge properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BiQuadraticQuadraticWedge properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


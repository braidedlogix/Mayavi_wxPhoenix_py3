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


class TriQuadraticHexahedron(NonLinearCell):
    """
    TriQuadraticHexahedron - cell represents a parabolic, 27-node
    isoparametric hexahedron
    
    Superclass: NonLinearCell
    
    TriQuadraticHexahedron is a concrete implementation of
    NonLinearCell to represent a three-dimensional, 27-node
    isoparametric triquadratic hexahedron. The interpolation is the
    standard finite element, triquadratic isoparametric shape function.
    The cell includes 8 edge nodes, 12 mid-edge nodes, 6 mid-face nodes
    and one mid-volume node. The ordering of the 27 points defining the
    cell is point ids (0-7,8-19, 20-25, 26) where point ids 0-7 are the
    eight corner vertices of the cube; followed by twelve midedge nodes
    (8-19); followed by 6 mid-face nodes (20-25) and the last node (26)
    is the mid-volume node. Note that these midedge nodes correspond lie
    on the edges defined by (0,1), (1,2), (2,3), (3,0), (4,5), (5,6),
    (6,7), (7,4), (0,4), (1,5), (2,6), (3,7). The mid-surface nodes lies
    on the faces defined by (first edge nodes id's, than mid-edge nodes
    id's): (0,1,5,4;8,17,12,16), (1,2,6,5;9,18,13,17),
    (2,3,7,6,10,19,14,18), (3,0,4,7;11,16,15,19), (0,1,2,3;8,9,10,11),
    (4,5,6,7;12,13,14,15). The last point lies in the center of the cell
    (0,1,2,3,4,5,6,7).
    
    
    
     top
      7--14--6
      |      |
     15  25  13
      |      |
      4--12--5
    
      middle
     19--23--18
      |      |
     20  26  21
      |      |
     16--22--17
    
     bottom
      3--10--2
      |      |
     11  24  9
      |      |
      0-- 8--1
    
     
    
    @sa
    QuadraticEdge QuadraticTriangle QuadraticTetra
    QuadraticQuad QuadraticPyramid QuadraticWedge
    BiQuadraticQuad
    
    @par Thanks: Thanks to Soeren Gebbert  who developed this class and
    integrated it into VTK 5.0.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTriQuadraticHexahedron, obj, update, **traits)
    
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
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float])
        C++: static void InterpolationDerivs(double pcoords[3],
            double derivs[81])
        @deprecated Replaced by
        TriQuadraticHexahedron::InterpolateDerivs as of VTK 5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationDerivs, *args)
        return ret

    def interpolation_functions(self, *args):
        """
        V.interpolation_functions([float, float, float], [float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float, float, float, float, float, float])
        C++: static void InterpolationFunctions(double pcoords[3],
            double weights[27])
        @deprecated Replaced by
        TriQuadraticHexahedron::InterpolateFunctions as of VTK 5.2
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
            return super(TriQuadraticHexahedron, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TriQuadraticHexahedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit TriQuadraticHexahedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TriQuadraticHexahedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


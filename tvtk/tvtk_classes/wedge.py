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

from tvtk.tvtk_classes.cell3d import Cell3D


class Wedge(Cell3D):
    """
    Wedge - a 3d cell that represents a linear wedge
    
    Superclass: Cell3D
    
    Wedge is a concrete implementation of Cell to represent a
    linear 3d wedge. A wedge consists of two triangular and three
    quadrilateral faces and is defined by the six points (0-5). Wedge
    uses the standard isoparametric shape functions for a linear wedge.
    The wedge is defined by the six points (0-5) where (0,1,2) is the
    base of the wedge which, using the right hand rule, forms a triangle
    whose normal points outward (away from the triangular face (3,4,5)).
    
    @sa
    ConvexPointSet Hexahedron Pyramid Tetra Voxel
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWedge, obj, update, **traits)
    
    def get_edge_array(self, *args):
        """
        V.get_edge_array(int) -> (int, int)
        C++: static int *GetEdgeArray(int edgeId)
        Return the ids of the vertices defining edge/face
        (`edge_id`/`face_id'). Ids are related to the cell, not to the
        dataset.
        """
        ret = self._wrap_call(self._vtk_obj.GetEdgeArray, *args)
        return ret

    def get_face_array(self, *args):
        """
        V.get_face_array(int) -> (int, int, int, int)
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
            float, float, float, float, float, float, float])
        C++: static void InterpolationDerivs(double pcoords[3],
            double derivs[18])
        @deprecated Replaced by Wedge::InterpolateDerivs as of VTK 5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationDerivs, *args)
        return ret

    def interpolation_functions(self, *args):
        """
        V.interpolation_functions([float, float, float], [float, float,
            float, float, float, float])
        C++: static void InterpolationFunctions(double pcoords[3],
            double weights[6])
        @deprecated Replaced by Wedge::InterpolateFunctions as of VTK
        5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationFunctions, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('merge_tolerance', 'GetMergeTolerance'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'merge_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Wedge, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Wedge properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['merge_tolerance']),
            title='Edit Wedge properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Wedge properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


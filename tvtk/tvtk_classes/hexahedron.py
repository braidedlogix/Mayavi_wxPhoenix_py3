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


class Hexahedron(Cell3D):
    """
    Hexahedron - a cell that represents a linear 3d hexahedron
    
    Superclass: Cell3D
    
    Hexahedron is a concrete implementation of Cell to represent a
    linear, 3d rectangular hexahedron (e.g., "brick" topology).
    Hexahedron uses the standard isoparametric shape functions for a
    linear hexahedron. The hexahedron is defined by the eight points
    (0-7) where (0,1,2,3) is the base of the hexahedron which, using the
    right hand rule, forms a quadrilaterial whose normal points in the
    direction of the opposite face (4,5,6,7).
    
    @sa
    ConvexPointSet Pyramid Tetra Voxel Wedge
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHexahedron, obj, update, **traits)
    
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
            float, float, float, float, float, float, float, float, float,
             float, float, float, float])
        C++: static void InterpolationDerivs(double pcoords[3],
            double derivs[24])
        @deprecated Replaced by Hexahedron::InterpolateDerivs as of
        VTK 5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationDerivs, *args)
        return ret

    def interpolation_functions(self, *args):
        """
        V.interpolation_functions([float, float, float], [float, float,
            float, float, float, float, float, float])
        C++: static void InterpolationFunctions(double pcoords[3],
            double weights[8])
        @deprecated Replaced by Hexahedron::InterpolateFunctions as of
        VTK 5.2
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
            return super(Hexahedron, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Hexahedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['merge_tolerance']),
            title='Edit Hexahedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Hexahedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


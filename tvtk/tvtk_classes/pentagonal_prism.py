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


class PentagonalPrism(Cell3D):
    """
    PentagonalPrism - a 3d cell that represents a convex prism with
    pentagonal base
    
    Superclass: Cell3D
    
    PentagonalPrism is a concrete implementation of Cell to
    represent a linear convex 3d prism with pentagonal base. Such prism
    is defined by the ten points (0-9), where (0,1,2,3,4) is the base of
    the prism which, using the right hand rule, forms a pentagon whose
    normal points is in the direction of the opposite face (5,6,7,8,9).
    
    @par Thanks: Thanks to Philippe Guerville who developed this class.
    Thanks to Charles Pignerol (CEA-DAM, France) who ported this class
    under VTK 4.
    
    Thanks to Jean Favre (CSCS, Switzerland) who contributed to integrate
    this class in VTK.
    
    Please address all comments to Jean Favre (jfavre at cscs.ch).
    
    @par Thanks: The Interpolation functions and derivatives were changed
    in June 2015 by Bill Lorensen. These changes follow the formulation
    in: http://dilbert.engr.ucdavis.edu/~suku/nem/papers/polyelas.pdf
    NOTE: An additional copy of this paper is located at:
    http://www.vtk.org/_wiki/_file:_application_of_polygonal_finite_elements_in_lin
    ear_elasticity.pdf
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPentagonalPrism, obj, update, **traits)
    
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
            float, float])
        C++: static void InterpolationDerivs(double pcoords[3],
            double derivs[30])
        @deprecated Replaced by PentagonalPrism::InterpolateDerivs as
        of VTK 5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationDerivs, *args)
        return ret

    def interpolation_functions(self, *args):
        """
        V.interpolation_functions([float, float, float], [float, float,
            float, float, float, float, float, float, float, float])
        C++: static void InterpolationFunctions(double pcoords[3],
            double weights[10])
        @deprecated Replaced by PentagonalPrism::InterpolateFunctions
        as of VTK 5.2
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
            return super(PentagonalPrism, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PentagonalPrism properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['merge_tolerance']),
            title='Edit PentagonalPrism properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PentagonalPrism properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


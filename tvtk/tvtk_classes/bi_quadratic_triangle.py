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


class BiQuadraticTriangle(NonLinearCell):
    """
    BiQuadraticTriangle - cell represents a parabolic, isoparametric
    triangle
    
    Superclass: NonLinearCell
    
    BiQuadraticTriangle is a concrete implementation of
    NonLinearCell to represent a two-dimensional, 7-node,
    isoparametric parabolic triangle. The interpolation is the standard
    finite element, bi-quadratic isoparametric shape function. The cell
    includes three mid-edge nodes besides the three triangle vertices and
    a center node. The ordering of the three points defining the cell is
    point ids (0-2,3-6) where id #3 is the midedge node between points
    (0,1); id #4 is the midedge node between points (1,2); and id #5 is
    the midedge node between points (2,0). id #6 is the center node of
    the cell.
    
    @sa
    Triangle QuadraticTriangle BiQuadraticQuad
    BiQuadraticQuadraticWedge BiQuadraticQuadraticHexahedron@par
    Thanks:  This file has been developed by Oxalya - www.oxalya.com
    Copyright (c) EDF - www.edf.fr 
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBiQuadraticTriangle, obj, update, **traits)
    
    def interpolation_derivs(self, *args):
        """
        V.interpolation_derivs([float, float, float], [float, float, float,
             float, float, float, float, float, float, float, float,
            float, float, float])
        C++: static void InterpolationDerivs(double pcoords[3],
            double derivs[14])
        @deprecated Replaced by BiQuadraticTriangle::InterpolateDerivs
        as of VTK 5.2
        """
        ret = self._wrap_call(self._vtk_obj.InterpolationDerivs, *args)
        return ret

    def interpolation_functions(self, *args):
        """
        V.interpolation_functions([float, float, float], [float, float,
            float, float, float, float, float])
        C++: static void InterpolationFunctions(double pcoords[3],
            double weights[7])
        @deprecated Replaced by
        BiQuadraticTriangle::InterpolateFunctions as of VTK 5.2
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
            return super(BiQuadraticTriangle, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BiQuadraticTriangle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit BiQuadraticTriangle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BiQuadraticTriangle properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


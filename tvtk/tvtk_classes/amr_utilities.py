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


class AMRUtilities(Object):
    """
    AMRUtilities -  A concrete instance of Object that employs a
    singleton design
     pattern and implements functionality for AMR specific operations.
    
    Superclass: Object
    
    @sa
     OverlappingAMR, AMRBox
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAMRUtilities, obj, update, **traits)
    
    def blank_cells(self, *args):
        """
        V.blank_cells(OverlappingAMR)
        C++: static void BlankCells(OverlappingAMR *amr)
        Blank cells in overlapping AMR
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.BlankCells, *my_args)
        return ret

    def has_partially_overlapping_ghost_cells(self, *args):
        """
        V.has_partially_overlapping_ghost_cells(OverlappingAMR) -> bool
        C++: static bool HasPartiallyOverlappingGhostCells(
            OverlappingAMR *amr)
        A quick test of whether partially overlapping ghost cells exist.
        This test starts from the highest-res boxes and checks if they
        have partially overlapping cells. The code returns with true once
        partially overlapping cells are detected. Otherwise, false is
        returned.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HasPartiallyOverlappingGhostCells, *my_args)
        return ret

    def strip_ghost_layers(self, *args):
        """
        V.strip_ghost_layers(OverlappingAMR, OverlappingAMR)
        C++: static void StripGhostLayers(
            OverlappingAMR *ghostedAMRData,
            OverlappingAMR *strippedAMRData)
        This method detects and strips partially overlapping cells from a
        given AMR dataset. If ghost layers are detected, they are removed
        and new grid instances are created to represent the stripped
        data-set otherwise, each block is shallow-copied.
        
        * .SECTION Assumptions
        * 1) The ghosted AMR data must have complete metadata
          information.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.StripGhostLayers, *my_args)
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
            return super(AMRUtilities, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AMRUtilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit AMRUtilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AMRUtilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


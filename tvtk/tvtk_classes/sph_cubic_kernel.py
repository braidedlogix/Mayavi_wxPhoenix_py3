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

from tvtk.tvtk_classes.sph_kernel import SPHKernel


class SPHCubicKernel(SPHKernel):
    """
    SPHCubicKernel - a cubic SPH interpolation kernel
    
    Superclass: SPHKernel
    
    SPHCubicKernel is an smooth particle hydrodynamics interpolation
    kernel as described by D.J. Price. This is a cubic formulation.
    
    @warning
    For more information see D.J. Price, Smoothed particle hydrodynamics
    and magnetohydrodynamics, J. Comput. Phys. 231:759-794, 2012.
    Especially equation 49.
    
    @par Acknowledgments: The following work has been generously
    supported by Altair Engineering and flui_dyna gmb_h. Please contact
    Steve Cosgrove or Milos Stanic for more information.
    
    @sa
    SPHKernel SPHInterpolator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSPHCubicKernel, obj, update, **traits)
    
    _updateable_traits_ = \
    (('requires_initialization', 'GetRequiresInitialization'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('dimension', 'GetDimension'), ('spatial_step', 'GetSpatialStep'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'requires_initialization',
    'dimension', 'spatial_step'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SPHCubicKernel, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SPHCubicKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['requires_initialization'], [], ['dimension', 'spatial_step']),
            title='Edit SPHCubicKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SPHCubicKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


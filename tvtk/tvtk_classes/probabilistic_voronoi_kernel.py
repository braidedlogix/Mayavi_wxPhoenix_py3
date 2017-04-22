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

from tvtk.tvtk_classes.generalized_kernel import GeneralizedKernel


class ProbabilisticVoronoiKernel(GeneralizedKernel):
    """
    ProbabilisticVoronoiKernel - interpolate from the weighted closest
    point
    
    Superclass: GeneralizedKernel
    
    ProbabilisticVoronoiKernel is an interpolation kernel that
    interpolates from the closest weighted point from a neighborhood of
    points. The weights refer to the probabilistic weighting that can be
    provided to the compute_weights() method.
    
    Note that the local neighborhood is taken from the kernel footprint
    specified in the superclass GeneralizedKernel.
    
    @warning
    If probability weightings are not defined, then the kernel provides
    the same results as VoronoiKernel, except a less efficiently.
    
    @sa
    InterpolationKernel GeneralizedKernel VoronoiKernel
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProbabilisticVoronoiKernel, obj, update, **traits)
    
    _updateable_traits_ = \
    (('normalize_weights', 'GetNormalizeWeights'),
    ('requires_initialization', 'GetRequiresInitialization'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('kernel_footprint', 'GetKernelFootprint'), ('number_of_points',
    'GetNumberOfPoints'), ('radius', 'GetRadius'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'normalize_weights',
    'requires_initialization', 'kernel_footprint', 'number_of_points',
    'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProbabilisticVoronoiKernel, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ProbabilisticVoronoiKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['normalize_weights', 'requires_initialization'],
            ['kernel_footprint'], ['number_of_points', 'radius']),
            title='Edit ProbabilisticVoronoiKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProbabilisticVoronoiKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class ShepardKernel(GeneralizedKernel):
    """
    ShepardKernel - a Shepard method interpolation kernel
    
    Superclass: GeneralizedKernel
    
    ShepardKernel is an interpolation kernel that uses the method of
    Shepard to perform interpolation. The weights are computed as 1/r^p,
    where r is the distance to a neighbor point within the kernal radius
    R; and p (the power parameter) is a positive exponent (typically
    p=2).
    
    @warning
    The weights are normalized sp that SUM(Wi) = 1. If a neighbor point p
    precisely lies on the point to be interpolated, then the interpolated
    point takes on the values associated with p.
    
    @sa
    PointInterpolator PointInterpolator2D InterpolationKernel
    GaussianKernel SPHKernel ShepardKernel
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkShepardKernel, obj, update, **traits)
    
    power_parameter = traits.Trait(2.0, traits.Range(0.001, 100.0, enter_set=True, auto_set=False), help=\
        """
        Set / Get the power parameter p. By default p=2. Values (which
        must be a positive, real value) != 2 may affect performance
        significantly.
        """
    )

    def _power_parameter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPowerParameter,
                        self.power_parameter)

    _updateable_traits_ = \
    (('normalize_weights', 'GetNormalizeWeights'),
    ('requires_initialization', 'GetRequiresInitialization'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('kernel_footprint', 'GetKernelFootprint'), ('power_parameter',
    'GetPowerParameter'), ('number_of_points', 'GetNumberOfPoints'),
    ('radius', 'GetRadius'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'normalize_weights',
    'requires_initialization', 'kernel_footprint', 'number_of_points',
    'power_parameter', 'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ShepardKernel, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ShepardKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['normalize_weights', 'requires_initialization'],
            ['kernel_footprint'], ['number_of_points', 'power_parameter',
            'radius']),
            title='Edit ShepardKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ShepardKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


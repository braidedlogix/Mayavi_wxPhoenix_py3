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

from tvtk.tvtk_classes.interpolation_kernel import InterpolationKernel


class SPHKernel(InterpolationKernel):
    """
    SPHKernel - a family of SPH interpolation kernels
    
    Superclass: InterpolationKernel
    
    SPHKernel is an abstract superclass for smoothed-particle
    hydrodynamics interpolation kernels as described by D.J. Price (see
    full reference below).
    
    Note that the kernel operates over a volume in space defined by a
    radius at a sampling point. The kernel implicitly assumes that the
    particles making up the input data satisfies physical properties such
    as conservation of mass. Therefore subclasses of this kernel are not
    generally applicable for interpolation processes, and therefore
    operate in conjunction with the vth_sph_interpolator class.
    
    By default the kernel computes local particle volume from the spatial
    step^3. However, if both an optional mass and density arrays are
    provided then they are used to compute local volume.
    
    Also be default, the local neighborhood around a point to be
    interpolated is computed as the cutoff_factor * spatial_step. (Note the
    cutoff_factor varies for each type of SPH kernel.) However, the user
    may specify a cutoff_array which enables variable cutoff distances per
    each point.
    
    @warning
    For more information see D.J. Price, Smoothed particle hydrodynamics
    and magnetohydrodynamics, J. Comput. Phys. 231:759-794, 2012.
    Especially equation 49.
    
    @par Acknowledgments: The following work has been generously
    supported by Altair Engineering and flui_dyna gmb_h. Please contact
    Steve Cosgrove or Milos Stanic for more information.
    
    @sa
    SPHKernel SPHQuinticKernel InterpolationKernel
    GaussianKernel ShepardKernel LinearKernel
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSPHKernel, obj, update, **traits)
    
    def _get_cutoff_array(self):
        return wrap_vtk(self._vtk_obj.GetCutoffArray())
    def _set_cutoff_array(self, arg):
        old_val = self._get_cutoff_array()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetCutoffArray,
                        my_arg[0])
        self.trait_property_changed('cutoff_array', old_val, arg)
    cutoff_array = traits.Property(_get_cutoff_array, _set_cutoff_array, help=\
        """
        Specify the (optional) array defining a cutoff distance. If
        provided this distance is used to find the interpolating points
        within the local neighborbood. Otherwise the cutoff distance is
        defined as the cutoff factor times the spatial step size.
        """
    )

    def _get_density_array(self):
        return wrap_vtk(self._vtk_obj.GetDensityArray())
    def _set_density_array(self, arg):
        old_val = self._get_density_array()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetDensityArray,
                        my_arg[0])
        self.trait_property_changed('density_array', old_val, arg)
    density_array = traits.Property(_get_density_array, _set_density_array, help=\
        """
        Specify the (optional) density array. Used with the mass array to
        compute local particle volumes.
        """
    )

    dimension = traits.Trait(3, traits.Range(1, 3, enter_set=True, auto_set=False), help=\
        """
        The domain dimension, default to 3.
        """
    )

    def _dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimension,
                        self.dimension)

    def _get_mass_array(self):
        return wrap_vtk(self._vtk_obj.GetMassArray())
    def _set_mass_array(self, arg):
        old_val = self._get_mass_array()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetMassArray,
                        my_arg[0])
        self.trait_property_changed('mass_array', old_val, arg)
    mass_array = traits.Property(_get_mass_array, _set_mass_array, help=\
        """
        Specify the (optional) mass array. Used with the density array to
        compute local particle volumes.
        """
    )

    spatial_step = traits.Trait(0.001, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        The user defined intial particle spatial step. This is also
        referred to as the smoothing length.
        """
    )

    def _spatial_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpatialStep,
                        self.spatial_step)

    def _get_cutoff_factor(self):
        return self._vtk_obj.GetCutoffFactor()
    cutoff_factor = traits.Property(_get_cutoff_factor, help=\
        """
        Return the cutoff factor. This is hard wired into the kernel
        (e.g., the SPHQuinticKernel has a cutoff factor = 3.0).
        """
    )

    def _get_norm_factor(self):
        return self._vtk_obj.GetNormFactor()
    norm_factor = traits.Property(_get_norm_factor, help=\
        """
        Return the SPH normalization factor. This also includes the
        contribution of 1/h^d, where h is the smoothing length (i.e.,
        spatial step) and d is the dimension of the kernel. The returned
        value is only valid after the kernel is initialized.
        """
    )

    def compute_deriv_weight(self, *args):
        """
        V.compute_deriv_weight(float) -> float
        C++: virtual double ComputeDerivWeight(const double d)
        Compute weighting factor for derivative quantities given a
        normalized distance from a sample point.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeDerivWeight, *args)
        return ret

    def compute_deriv_weights(self, *args):
        """
        V.compute_deriv_weights([float, float, float], IdList,
            DoubleArray, DoubleArray) -> int
        C++: virtual IdType ComputeDerivWeights(double x[3],
            IdList *pIds, DoubleArray *weights,
            DoubleArray *gradWeights)
        Given a point x, and a list of basis points p_ids, compute
        interpolation weights, plus derivative weights, associated with
        these basis points.
        """
        my_args = deref_array(args, [(['float', 'float', 'float'], 'vtkIdList', 'vtkDoubleArray', 'vtkDoubleArray')])
        ret = self._wrap_call(self._vtk_obj.ComputeDerivWeights, *my_args)
        return ret

    def compute_function_weight(self, *args):
        """
        V.compute_function_weight(float) -> float
        C++: virtual double ComputeFunctionWeight(const double d)
        Compute weighting factor given a normalized distance from a
        sample point.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeFunctionWeight, *args)
        return ret

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
            return super(SPHKernel, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SPHKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['requires_initialization'], [], ['dimension', 'spatial_step']),
            title='Edit SPHKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SPHKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class EllipsoidalGaussianKernel(GeneralizedKernel):
    """
    EllipsoidalGaussianKernel - an ellipsoidal Gaussian interpolation
    kernel
    
    Superclass: GeneralizedKernel
    
    EllipsoidalGaussianKernel is an interpolation kernel that returns
    the weights for all points found in the ellipsoid defined by radius R
    in combination with local data (normals and/or scalars). For example,
    "pancake" weightings (the local normal parallel to the minimum
    ellisoidal axis); or "needle" weightings (the local normal parallel
    to the maximum ellipsoidal axis) are possible. (Note that spherical
    Gaussian weightings are more efficiently computed using
    GaussianKernel.)
    
    The ellipsoidal Gaussian can be described by:
    
    
        W(x) = S * exp( -( Sharpness^2 * ((rxy/E)**2 + z**2)/R**2) )
    
    where S is the local scalar value; E is a user-defined eccentricity
    factor that controls the elliptical shape of the splat; z is the
    distance of the current voxel sample point along the local normal N;
    and rxy is the distance to neigbor point x in the direction
    prependicular to N.
    
    @warning
    The weights are normalized so that SUM(Wi) = 1. If a neighbor point p
    precisely lies on the point to be interpolated, then the interpolated
    point takes on the values associated with p.
    
    @sa
    PointInterpolator InterpolationKernel GeneralizedKernel
    GaussianKernel VoronoiKernel SPHKernel ShepardKernel
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEllipsoidalGaussianKernel, obj, update, **traits)
    
    use_normals = tvtk_base.true_bool_trait(help=\
        """
        Specify whether vector values should be used to affect the shape
        of the Gaussian distribution. By default this is on.
        """
    )

    def _use_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseNormals,
                        self.use_normals_)

    use_scalars = tvtk_base.false_bool_trait(help=\
        """
        Specify whether scalar values should be used to scale the
        weights. By default this is off.
        """
    )

    def _use_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseScalars,
                        self.use_scalars_)

    eccentricity = traits.Trait(2.0, traits.Range(1e-06, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Set / Get the eccentricity of the ellipsoidal Gaussian. A
        value=1.0 produces a spherical distribution. Values < 1 produce a
        needle like distribution (in the direction of the normal); values
        > 1 produce a pancake like distribution (orthogonal to the
        normal).
        """
    )

    def _eccentricity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEccentricity,
                        self.eccentricity)

    normals_array_name = traits.String('Normals', enter_set=True, auto_set=False, help=\
        """
        Specify the normals array name. Used to orient the ellipsoid.
        Note that by default the input normals are used (i.e. the input
        to PointInterpolator). If no input normals are available, then
        the named normals_array_name is used.
        """
    )

    def _normals_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalsArrayName,
                        self.normals_array_name)

    scalars_array_name = traits.String('Scalars', enter_set=True, auto_set=False, help=\
        """
        Specify the scalars array name. Used to scale the ellipsoid. Note
        that by default the input scalars are used (i.e. the input to
        PointInterpolator). If no input scalars are available, then
        the named scalars_array_name is used.
        """
    )

    def _scalars_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarsArrayName,
                        self.scalars_array_name)

    scale_factor = traits.Trait(1.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Multiply the Gaussian splat distribution by this value. If
        use_scalars is on and a scalar aray is provided, then the scalar
        value will be multiplied by the scale_factor times the Gaussian
        function.
        """
    )

    def _scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleFactor,
                        self.scale_factor)

    sharpness = traits.Trait(2.0, traits.Range(1.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Set / Get the sharpness (i.e., falloff) of the Gaussian. By
        default Sharpness=2. As the sharpness increases the effects of
        distant points are reduced.
        """
    )

    def _sharpness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSharpness,
                        self.sharpness)

    _updateable_traits_ = \
    (('use_normals', 'GetUseNormals'), ('use_scalars', 'GetUseScalars'),
    ('normalize_weights', 'GetNormalizeWeights'),
    ('requires_initialization', 'GetRequiresInitialization'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('kernel_footprint', 'GetKernelFootprint'), ('eccentricity',
    'GetEccentricity'), ('normals_array_name', 'GetNormalsArrayName'),
    ('scalars_array_name', 'GetScalarsArrayName'), ('scale_factor',
    'GetScaleFactor'), ('sharpness', 'GetSharpness'), ('number_of_points',
    'GetNumberOfPoints'), ('radius', 'GetRadius'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'normalize_weights',
    'requires_initialization', 'use_normals', 'use_scalars',
    'kernel_footprint', 'eccentricity', 'normals_array_name',
    'number_of_points', 'radius', 'scalars_array_name', 'scale_factor',
    'sharpness'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EllipsoidalGaussianKernel, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit EllipsoidalGaussianKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['normalize_weights', 'requires_initialization', 'use_normals',
            'use_scalars'], ['kernel_footprint'], ['eccentricity',
            'normals_array_name', 'number_of_points', 'radius',
            'scalars_array_name', 'scale_factor', 'sharpness']),
            title='Edit EllipsoidalGaussianKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EllipsoidalGaussianKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


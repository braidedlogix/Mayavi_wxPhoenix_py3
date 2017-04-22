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


class GeneralizedKernel(InterpolationKernel):
    """
    GeneralizedKernel - flexible, general interpolation kernels
    
    Superclass: InterpolationKernel
    
    GeneralizedKernel is an abstract class that defines an API for
    concrete general-purpose, kernel subclasses. GeneralizedKernels
    has important properties that make them useful in a variety of
    interpolation applications:
    
    1. The weights are normalized.
    2. The footprint of the basis is configurable.
    3. Probablistic weighting functions can be used to favor certain
       weights.  The following paragraphs describe each of these
       properties in more detail.
    
    Normalized weightings simple mean Sum(w_i) = 1. This ensures that the
    interpolation process is well behaved.
    
    The interpolation footprint is the set of points that are used to
    perform the interpolation process. For example, it is possible to
    choose between a radius-based kernel selection, and one based on the
    N nearest neighbors. Note that the performance and mathematical
    properties of kernels may vary greatly depending on which kernel
    style is selected. For example, if a radius-based kernel footprint is
    used, and the radius is too big, the algorithm can perform in n^3
    fashion.
    
    Finally, in advanced usage, probability functions can be applied to
    the interpolation weights (prior to normalization). These probability
    functions are confidence estimates that the data at a particular
    point is accurate. A typical application is when laser scans are used
    to acquire point measurements, which return normals that indicate
    glancing returns versus direct, near orthogonal hits. Another use is
    when point clouds are combined, where some clouds are acquired with
    more accurate, detailed devices versus a broad, potentially coarser
    acquisition process.
    
    @warning
    Some kernels, like the Voronoi kernel, cannot be subclasses of this
    class because their definition inherently defines the basis style.
    For example, the Voronoi kernel is simply the single closest point.
    SPH kernals are similar, because they implicitly depend on a particle
    distribution consistent with simulation constraints such as
    conservation of mass, etc.
    
    @sa
    PointInterpolator PointInterpolator2D GaussianKernel
    SPHKernel ShepardKernel LinearKernel VoronoiKernel
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeneralizedKernel, obj, update, **traits)
    
    normalize_weights = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether the interpolation weights should be normalized
        after they are computed. Generally this is left on as it results
        in more reasonable behavior.
        """
    )

    def _normalize_weights_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalizeWeights,
                        self.normalize_weights_)

    kernel_footprint = traits.Trait('radius',
    tvtk_base.TraitRevPrefixMap({'radius': 0, 'n_closest': 1}), help=\
        """
        Specify the interpolation basis style. By default, a Radius style
        is used (i.e., the basis is defined from all points within a
        specified radius). However, it is also possible to select the N
        closest points (NClosest). Note that in most formulations the
        Radius style is assumed as it provides better mathematical
        properties. However, for convenience some bases are easier to use
        when the N closest points are taken.
        """
    )

    def _kernel_footprint_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKernelFootprint,
                        self.kernel_footprint_)

    number_of_points = traits.Trait(8, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        If the interpolation basis style is NClosest, then this method
        specifies the number of the closest points used to form the
        interpolation basis.
        """
    )

    def _number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPoints,
                        self.number_of_points)

    radius = traits.Trait(1.0, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        If the interpolation basis style is Radius, then this method
        specifies the radius within which the basis points must lie.
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

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
            return super(GeneralizedKernel, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeneralizedKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['normalize_weights', 'requires_initialization'],
            ['kernel_footprint'], ['number_of_points', 'radius']),
            title='Edit GeneralizedKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeneralizedKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


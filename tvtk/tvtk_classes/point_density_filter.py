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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class PointDensityFilter(ImageAlgorithm):
    """
    PointDensityFilter - produce density field from input point cloud
    
    Superclass: ImageAlgorithm
    
    PointDensityFilter is a filter that generates a density field on a
    volume from a point cloud. Basically the density is computed as
    number of points in a local neighborhood per unit volume; or
    optionally, the number of points in a local neighborhood surrounding
    each voxel. The local neighborhood is specified as a radius around
    each sample position (i.e., each voxel) which can be of fixed value;
    or the radius can be relative to the voxel size. The density
    computation may be further weighted by a scalar value which is simply
    multiplied by each point's presumed density of 1.0.
    
    To use this filter, specify an input of type PointSet (i.e., has
    an explicit representation of points). Optionally a scalar weighting
    function can be provided (part of the input to the filter). Then
    specify how the local spherical neigborhood is to be defined, either
    by a fixed radius or a radius relative to the voxel size. Finally,
    specify how the density is specified, either as a points/volume, or
    as number of points. (The weighting scalar array will affect both of
    these results if provided and enabled.)
    
    @warning
    A point locator is used to speed up searches. By default a fast
    StaticPointLocator is used; however the user may specify an
    alternative locator. In some situations adaptive locators may run
    faster depending on the relative variation in point cloud density.
    
    @warning
    Note that the volume calculation can be affected by the boundary. The
    local spherical neighborhood around a "near volume boundary" voxel
    may extend beyond the volume extent, meaning that density computation
    may be reduced. To counter this effect, the volume may be increased
    in size and/or resolution so that the point cloud fits well within
    the volume.
    
    @warning
    While this class is very similar to many other of VTK's the point
    splatting and interpolation classes, the algorithm density
    computation is specialized to generate the density computation over a
    volume, does not require (scalar weighting) data attributes to run,
    and does not require multiple inputs. As an interesting side note:
    using the PointInterpolation class with a LinearKernel, a
    (scalar) weighting point attribute, a point cloud source, and an
    input volume produces the same result as this filter does (assuming
    that the input volume is the same).
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    CheckerboardSplatter ShepardMethod GaussianSplatter
    PointInterpolator SPHInterpolator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointDensityFilter, obj, update, **traits)
    
    scalar_weighting = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the weighting of point density by a scalar array. By
        default scalar weighting is off.
        """
    )

    def _scalar_weighting_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarWeighting,
                        self.scalar_weighting_)

    density_estimate = traits.Trait('relative_radius',
    tvtk_base.TraitRevPrefixMap({'relative_radius': 1, 'fixed_radius': 0}), help=\
        """
        Specify the method to estimate point density. The density can be
        calculated using a fixed sphere radius; or a sphere radius that
        is relative to voxel size.
        """
    )

    def _density_estimate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDensityEstimate,
                        self.density_estimate_)

    density_form = traits.Trait('number_of_points',
    tvtk_base.TraitRevPrefixMap({'number_of_points': 1, 'volume_normalized': 0}), help=\
        """
        Specify the form by which the density is expressed. Either the
        density is expressed as (number of points/local sphere volume),
        or as simply the (number of points) within the local sphere.
        """
    )

    def _density_form_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDensityForm,
                        self.density_form_)

    adjust_distance = traits.Trait(0.1, traits.Range(-1.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set / get the relative amount to pad the model bounds if
        automatic computation is performed. The padding is the fraction
        to scale the model bounds in each of the x-y-z directions. By
        default the padding is 0.10 (i.e., 10% larger in each direction).
        """
    )

    def _adjust_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAdjustDistance,
                        self.adjust_distance)

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Specify a point locator. By default a StaticPointLocator is
        used. The locator performs efficient searches to locate near a
        specified interpolation position.
        """
    )

    model_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _model_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModelBounds,
                        self.model_bounds)

    radius = traits.Trait(1.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set / get the radius variable defining the local sphere used to
        estimate the density function. The Radius is used when the
        density estimate is ^ set to a fixed radius (i.e., the radius
        doesn't change).
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    relative_radius = traits.Trait(1.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set / get the relative radius factor defining the local sphere
        used to estimate the density function. The relative sphere radius
        is equal to the diagonal length of a voxel times the radius
        factor. The relative_radius is used when the density estimate is
        set to relative radius (i.e., relative to voxel size).
        """
    )

    def _relative_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRelativeRadius,
                        self.relative_radius)

    sample_dimensions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(100, 100, 100), cols=3, help=\
        """
        Set / get the dimensions of the sampling volume. Higher values
        generally produce better results but may be much slower. Note
        however that too high a resolution can generate excessive noise;
        too low and data can be excessively smoothed.
        """
    )

    def _sample_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleDimensions,
                        self.sample_dimensions)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get a data object for one of the input port connections.  The use
        of this method is strongly discouraged, but some filters that
        were written a long time ago still use this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('scalar_weighting', 'GetScalarWeighting'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('density_estimate',
    'GetDensityEstimate'), ('density_form', 'GetDensityForm'),
    ('adjust_distance', 'GetAdjustDistance'), ('model_bounds',
    'GetModelBounds'), ('radius', 'GetRadius'), ('relative_radius',
    'GetRelativeRadius'), ('sample_dimensions', 'GetSampleDimensions'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'scalar_weighting', 'density_estimate',
    'density_form', 'adjust_distance', 'model_bounds', 'progress_text',
    'radius', 'relative_radius', 'sample_dimensions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointDensityFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PointDensityFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['scalar_weighting'], ['density_estimate', 'density_form'],
            ['adjust_distance', 'model_bounds', 'radius', 'relative_radius',
            'sample_dimensions']),
            title='Edit PointDensityFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointDensityFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


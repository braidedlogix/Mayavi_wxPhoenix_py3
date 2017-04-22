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


class GaussianSplatter(ImageAlgorithm):
    """
    GaussianSplatter - splat points into a volume with an elliptical,
    Gaussian distribution
    
    Superclass: ImageAlgorithm
    
    GaussianSplatter is a filter that injects input points into a
    structured points (volume) dataset. As each point is injected, it
    "splats" or distributes values to nearby voxels. Data is distributed
    using an elliptical, Gaussian distribution function. The distribution
    function is modified using scalar values (expands distribution) or
    normals (creates ellipsoidal distribution rather than spherical).
    
    In general, the Gaussian distribution function f(x) around a given
    splat point p is given by
    
    
        f(x) = scale_factor * exp( exponent_factor*((r/_radius)**_2) )
    
    where x is the current voxel sample point; r is the distance |x-p|
    exponent_factor <= 0.0, and scale_factor can be multiplied by the
    scalar value of the point p that is currently being splatted.
    
    If points normals are present (and normal_warping is on), then the
    splat function becomes elliptical (as compared to the spherical one
    described by the previous equation). The Gaussian distribution
    function then becomes:
    
    
        f(x) = scale_factor *
                  exp( exponent_factor*( ((rxy/E)**2 + z**2)/R**2) )
    
    where E is a user-defined eccentricity factor that controls the
    elliptical shape of the splat; z is the distance of the current voxel
    sample point along normal N; and rxy is the distance of x in the
    direction prependicular to N.
    
    This class is typically used to convert point-valued distributions
    into a volume representation. The volume is then usually iso-surfaced
    or volume rendered to generate a visualization. It can be used to
    create surfaces from point distributions, or to create structure
    (i.e., topology) when none exists.
    
    @warning
    The input to this filter is any dataset type. This filter can be used
    to resample any form of data, i.e., the input data need not be
    unstructured.
    
    @warning
    Some voxels may never receive a contribution during the splatting
    process. The final value of these points can be specified with the
    "_null_value" instance variable.
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    ShepardMethod CheckerboardSplatter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGaussianSplatter, obj, update, **traits)
    
    capping = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the capping of the outer boundary of the volume to a
        specified cap value. This can be used to close surfaces (after
        iso-surfacing) and create other effects.
        """
    )

    def _capping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCapping,
                        self.capping_)

    normal_warping = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the generation of elliptical splats. If normal
        warping is on, then the input normals affect the distribution of
        the splat. This boolean is used in combination with the
        Eccentricity ivar.
        """
    )

    def _normal_warping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalWarping,
                        self.normal_warping_)

    scalar_warping = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the scaling of splats by scalar value.
        """
    )

    def _scalar_warping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarWarping,
                        self.scalar_warping_)

    accumulation_mode = traits.Trait('max',
    tvtk_base.TraitRevPrefixMap({'max': 1, 'min': 0, 'sum': 2}), help=\
        """
        Specify the scalar accumulation mode. This mode expresses how
        scalar values are combined when splats are overlapped. The Max
        mode acts like a set union operation and is the most commonly
        used; the Min mode acts like a set intersection, and the sum is
        just weird.
        """
    )

    def _accumulation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAccumulationMode,
                        self.accumulation_mode_)

    cap_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Specify the cap value to use. (This instance variable only has
        effect if the ivar Capping is on.)
        """
    )

    def _cap_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCapValue,
                        self.cap_value)

    eccentricity = traits.Trait(2.5, traits.Range(0.001, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Control the shape of elliptical splatting. Eccentricity is the
        ratio of the major axis (aligned along normal) to the minor
        (axes) aligned along other two axes. So Eccentricity > 1 creates
        needles with the long axis in the direction of the normal;
        Eccentricity<1 creates pancakes perpendicular to the normal
        vector.
        """
    )

    def _eccentricity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEccentricity,
                        self.eccentricity)

    exponent_factor = traits.Float(-5.0, enter_set=True, auto_set=False, help=\
        """
        Set / get the sharpness of decay of the splats. This is the
        exponent constant in the Gaussian equation. Normally this is a
        negative value.
        """
    )

    def _exponent_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExponentFactor,
                        self.exponent_factor)

    model_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _model_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModelBounds,
                        self.model_bounds)

    null_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the Null value for output points not receiving a contribution
        from the input points. (This is the initial value of the voxel
        samples.)
        """
    )

    def _null_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNullValue,
                        self.null_value)

    radius = traits.Trait(0.1, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set / get the radius of propagation of the splat. This value is
        expressed as a percentage of the length of the longest side of
        the sampling volume. Smaller numbers greatly reduce execution
        time.
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    sample_dimensions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(50, 50, 50), cols=3, help=\
        """
        Set / get the dimensions of the sampling structured point set.
        Higher values produce better results but are much slower.
        """
    )

    def _sample_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleDimensions,
                        self.sample_dimensions)

    scale_factor = traits.Trait(1.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Multiply Gaussian splat distribution by this value. If
        scalar_warping is on, then the Scalar value will be multiplied by
        the scale_factor times the Gaussian function.
        """
    )

    def _scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleFactor,
                        self.scale_factor)

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

    def compute_model_bounds(self, *args):
        """
        V.compute_model_bounds(DataSet, ImageData, Information)
        C++: void ComputeModelBounds(DataSet *input,
            ImageData *output, Information *outInfo)
        V.compute_model_bounds(CompositeDataSet, ImageData,
            Information)
        C++: void ComputeModelBounds(CompositeDataSet *input,
            ImageData *output, Information *outInfo)
        Compute the size of the sample bounding box automatically from
        the input data. This is an internal helper function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeModelBounds, *my_args)
        return ret

    def sample_point(self, *args):
        """
        V.sample_point([float, float, float]) -> float
        C++: double SamplePoint(double x[3])
        Provide access to templated helper class. Note that sample_point()
        method is public here because some compilers don't handle friend
        functions properly.
        """
        ret = self._wrap_call(self._vtk_obj.SamplePoint, *args)
        return ret

    def set_scalar(self, *args):
        """
        V.set_scalar(int, float, [float, ...])
        C++: void SetScalar(int idx, double dist2, double *sPtr)
        Provide access to templated helper class. Note that sample_point()
        method is public here because some compilers don't handle friend
        functions properly.
        """
        ret = self._wrap_call(self._vtk_obj.SetScalar, *args)
        return ret

    _updateable_traits_ = \
    (('capping', 'GetCapping'), ('normal_warping', 'GetNormalWarping'),
    ('scalar_warping', 'GetScalarWarping'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('accumulation_mode',
    'GetAccumulationMode'), ('cap_value', 'GetCapValue'), ('eccentricity',
    'GetEccentricity'), ('exponent_factor', 'GetExponentFactor'),
    ('model_bounds', 'GetModelBounds'), ('null_value', 'GetNullValue'),
    ('radius', 'GetRadius'), ('sample_dimensions', 'GetSampleDimensions'),
    ('scale_factor', 'GetScaleFactor'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'capping', 'debug', 'global_warning_display',
    'normal_warping', 'release_data_flag', 'scalar_warping',
    'accumulation_mode', 'cap_value', 'eccentricity', 'exponent_factor',
    'model_bounds', 'null_value', 'progress_text', 'radius',
    'sample_dimensions', 'scale_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GaussianSplatter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GaussianSplatter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['capping', 'normal_warping', 'scalar_warping'],
            ['accumulation_mode'], ['cap_value', 'eccentricity',
            'exponent_factor', 'model_bounds', 'null_value', 'radius',
            'sample_dimensions', 'scale_factor']),
            title='Edit GaussianSplatter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GaussianSplatter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


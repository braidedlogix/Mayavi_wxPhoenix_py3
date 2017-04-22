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

from tvtk.tvtk_classes.volume_mapper import VolumeMapper


class SmartVolumeMapper(VolumeMapper):
    """
    SmartVolumeMapper - Adaptive volume mapper
    
    Superclass: VolumeMapper
    
    SmartVolumeMapper is a volume mapper that will delegate to a
    specific volume mapper based on rendering parameters and available
    hardware. Use the set_requested_render_mode() method to control the
    behavior of the selection. The following options are available:
    
    @par SmartVolumeMapper::DefaultRenderMode:
             Allow the SmartVolumeMapper to select the best mapper
    based on
             rendering parameters and hardware support. If GPU ray
    casting is
             supported, this mapper will be used for all rendering. If
    not,
             then the FixedPointRayCastMapper will be used
    exclusively.
             This is the default requested render mode, and is generally
    the
             best option. When you use this option, your volume will
    always
             be rendered, but the method used to render it may vary based
             on parameters and platform.
    
    @par SmartVolumeMapper::RayCastRenderMode:
             Use the FixedPointVolumeRayCastMapper for both
    interactive and
             still rendering. When you use this option your volume will
    always
             be rendered with the FixedPointVolumeRayCastMapper.
    
    @par SmartVolumeMapper::GPURenderMode:
             Use the GPUVolumeRayCastMapper, if supported, for both
             interactive and still rendering. If the GPU ray caster is
    not
             supported (due to hardware limitations or rendering
    parameters)
             then no image will be rendered. Use this option only if you
    have
             already checked for supported based on the current hardware,
             number of scalar components, and rendering parameters in the
             VolumeProperty.
    
    @par SmartVolumeMapper::GPURenderMode:
     You can adjust the contrast and brightness in the rendered image
    using the
     final_color_window and final_color_level ivars. By default the
     final_color_window is set to 1.0, and the final_color_level is set to
    0.5,
     which applies no correction to the computed image. To apply the
    window /
     level operation to the computer image color, first a Scale and Bias
     value are computed:
    
    
     scale = 1.0 / this->_final_color_window
     bias  = 0.5 - this->_final_color_level / this->_final_color_window
     
     To compute a new color (R', G', B', A') from an existing color
    (R,G,B,A)
     for a pixel, the following equation is used:
    
    
     R' = R*scale + bias*A
     G' = G*scale + bias*A
     B' = B*scale + bias*A
     A' = A
      Note that bias is multiplied by the alpha component before adding
    because the red, green, and blue component of the color are already
    pre-multiplied by alpha. Also note that the window / level operation
    leaves the alpha component unchanged - it only adjusts the RGB
    values.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSmartVolumeMapper, obj, update, **traits)
    
    auto_adjust_sample_distances = tvtk_base.true_bool_trait(help=\
        """
        If auto_adjust_sample_distances is on, the image_sample_distance will
        be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        Note that, this flag is ignored when
        interactive_adjust_sample_distances is enabled. To explicitly set
        and use this flag, one must disable
        interactive_adjust_sample_distances.
        """
    )

    def _auto_adjust_sample_distances_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoAdjustSampleDistances,
                        self.auto_adjust_sample_distances_)

    interactive_adjust_sample_distances = tvtk_base.true_bool_trait(help=\
        """
        If the interactive_adjust_sample_distances flag is enabled,
        SmartVolumeMapper interactively sets and resets the
        auto_adjust_sample_distances flag on the internal volume mapper.
        This flag along with interactive_update_rate is useful to adjust
        volume mapper sample distance based on whether the render is
        interactive or still. By default,
        interactive_adjust_sample_distances is enabled.
        """
    )

    def _interactive_adjust_sample_distances_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteractiveAdjustSampleDistances,
                        self.interactive_adjust_sample_distances_)

    interpolation_mode = traits.Trait('cubic',
    tvtk_base.TraitRevPrefixMap({'cubic': 2, 'linear': 1, 'nearest_neighbor': 0}), help=\
        """
        Set interpolation mode for downsampling (lowres GPU) (initial
        value: cubic).
        """
    )

    def _interpolation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolationMode,
                        self.interpolation_mode_)

    requested_render_mode = traits.Trait('default',
    tvtk_base.TraitRevPrefixMap({'default': 0, 'gpu': 4, 'osp_ray': 6, 'ray_cast': 2}), help=\
        """
        Set the requested render mode. The default is
        SmartVolumeMapper::DefaultRenderMode.
        """
    )

    def _requested_render_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRequestedRenderMode,
                        self.requested_render_mode_)

    final_color_level = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set the final color level. The level controls the brightness of
        the image. The final color window will be centered at the final
        color level, and together represent a linear remapping of color
        values. The default value for the level is 0.5.
        """
    )

    def _final_color_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFinalColorLevel,
                        self.final_color_level)

    final_color_window = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the final color window. This controls the contrast of the
        image. The default value is 1.0. The Window can be negative (this
        causes a "negative" effect on the image) Although Window can be
        set to 0.0, any value less than 0.00001 and greater than or equal
        to 0.0 will be set to 0.00001, and any value greater than
        -0.00001 but less than or equal to 0.0 will be set to -0.00001.
        Initial value is 1.0.
        """
    )

    def _final_color_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFinalColorWindow,
                        self.final_color_window)

    interactive_update_rate = traits.Trait(1.0, traits.Range(1e-10, 10000000000.0, enter_set=True, auto_set=False), help=\
        """
        If the desired_update_rate of the RenderWindow that caused the
        Render falls at or above this rate, the render is considered
        interactive and the mapper may be adjusted (depending on the
        render mode). Initial value is 1.0.
        """
    )

    def _interactive_update_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteractiveUpdateRate,
                        self.interactive_update_rate)

    max_memory_fraction = traits.Trait(0.75, traits.Range(0.10000000149011612, 1.0, enter_set=True, auto_set=False), help=\
        """
        Value passed to the GPU mapper. Ignored by other mappers. Maximum
        fraction of the max_memory_in_bytes that should be used to hold the
        texture. Valid values are 0.1 to 1.0.
        """
    )

    def _max_memory_fraction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxMemoryFraction,
                        self.max_memory_fraction)

    max_memory_in_bytes = traits.Int(134217728, enter_set=True, auto_set=False, help=\
        """
        Value passed to the GPU mapper. Ignored by other mappers. Maximum
        size of the 3d texture in GPU memory. Will default to the size
        computed from the graphics card. Can be adjusted by the user.
        Useful if the automatic detection is defective or missing.
        """
    )

    def _max_memory_in_bytes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxMemoryInBytes,
                        self.max_memory_in_bytes)

    sample_distance = traits.Float(-1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the distance between samples used for rendering when
        auto_adjust_sample_distances is off, or when this mapper has more
        than 1 second allocated to it for rendering. If sample_distance is
        negative, it will be computed based on the dataset spacing.
        Initial value is -1.0.
        """
    )

    def _sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleDistance,
                        self.sample_distance)

    vector_component = traits.Trait(2037150581, 2037150581, traits.Range(0, 3, enter_set=True, auto_set=False), help=\
        """
        vector_mode is a special rendering mode for 3-component vectors
        which makes use of gpu_ray_cast_mapper's independent-component
        capabilities. In this mode, a single component in the vector can
        be selected for rendering. In addition, the mapper can compute a
        scalar field representing the magnitude of this vector using a
        ImageMagnitude object (MAGNITUDE mode).
        """
    )

    def _vector_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorComponent,
                        self.vector_component)

    vector_mode = traits.Trait(-1, traits.Range(-1, 1, enter_set=True, auto_set=False), help=\
        """
        vector_mode is a special rendering mode for 3-component vectors
        which makes use of gpu_ray_cast_mapper's independent-component
        capabilities. In this mode, a single component in the vector can
        be selected for rendering. In addition, the mapper can compute a
        scalar field representing the magnitude of this vector using a
        ImageMagnitude object (MAGNITUDE mode).
        """
    )

    def _vector_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorMode,
                        self.vector_mode)

    def _get_auto_adjust_sample_distances_max_value(self):
        return self._vtk_obj.GetAutoAdjustSampleDistancesMaxValue()
    auto_adjust_sample_distances_max_value = traits.Property(_get_auto_adjust_sample_distances_max_value, help=\
        """
        If auto_adjust_sample_distances is on, the image_sample_distance will
        be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        Note that, this flag is ignored when
        interactive_adjust_sample_distances is enabled. To explicitly set
        and use this flag, one must disable
        interactive_adjust_sample_distances.
        """
    )

    def _get_auto_adjust_sample_distances_min_value(self):
        return self._vtk_obj.GetAutoAdjustSampleDistancesMinValue()
    auto_adjust_sample_distances_min_value = traits.Property(_get_auto_adjust_sample_distances_min_value, help=\
        """
        If auto_adjust_sample_distances is on, the image_sample_distance will
        be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        Note that, this flag is ignored when
        interactive_adjust_sample_distances is enabled. To explicitly set
        and use this flag, one must disable
        interactive_adjust_sample_distances.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input data
        """
    )

    def _get_interactive_adjust_sample_distances_max_value(self):
        return self._vtk_obj.GetInteractiveAdjustSampleDistancesMaxValue()
    interactive_adjust_sample_distances_max_value = traits.Property(_get_interactive_adjust_sample_distances_max_value, help=\
        """
        If the interactive_adjust_sample_distances flag is enabled,
        SmartVolumeMapper interactively sets and resets the
        auto_adjust_sample_distances flag on the internal volume mapper.
        This flag along with interactive_update_rate is useful to adjust
        volume mapper sample distance based on whether the render is
        interactive or still. By default,
        interactive_adjust_sample_distances is enabled.
        """
    )

    def _get_interactive_adjust_sample_distances_min_value(self):
        return self._vtk_obj.GetInteractiveAdjustSampleDistancesMinValue()
    interactive_adjust_sample_distances_min_value = traits.Property(_get_interactive_adjust_sample_distances_min_value, help=\
        """
        If the interactive_adjust_sample_distances flag is enabled,
        SmartVolumeMapper interactively sets and resets the
        auto_adjust_sample_distances flag on the internal volume mapper.
        This flag along with interactive_update_rate is useful to adjust
        volume mapper sample distance based on whether the render is
        interactive or still. By default,
        interactive_adjust_sample_distances is enabled.
        """
    )

    def _get_last_used_render_mode(self):
        return self._vtk_obj.GetLastUsedRenderMode()
    last_used_render_mode = traits.Property(_get_last_used_render_mode, help=\
        """
        This will return the render mode used during the previous call to
        Render().
        """
    )

    def create_canonical_view(self, *args):
        """
        V.create_canonical_view(Renderer, Volume, Volume,
            ImageData, int, [float, float, float], [float, float,
            float])
        C++: void CreateCanonicalView(Renderer *ren, Volume *volume,
             Volume *volume2, ImageData *image, int blend_mode,
            double viewDirection[3], double viewUp[3])
        This method can be used to render a representative view of the
        input data into the supplied image given the supplied blending
        mode, view direction, and view up vector.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CreateCanonicalView, *my_args)
        return ret

    _updateable_traits_ = \
    (('auto_adjust_sample_distances', 'GetAutoAdjustSampleDistances'),
    ('interactive_adjust_sample_distances',
    'GetInteractiveAdjustSampleDistances'), ('cropping', 'GetCropping'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('interpolation_mode', 'GetInterpolationMode'),
    ('requested_render_mode', 'GetRequestedRenderMode'), ('blend_mode',
    'GetBlendMode'), ('cropping_region_flags', 'GetCroppingRegionFlags'),
    ('scalar_mode', 'GetScalarMode'), ('final_color_level',
    'GetFinalColorLevel'), ('final_color_window', 'GetFinalColorWindow'),
    ('interactive_update_rate', 'GetInteractiveUpdateRate'),
    ('max_memory_fraction', 'GetMaxMemoryFraction'),
    ('max_memory_in_bytes', 'GetMaxMemoryInBytes'), ('sample_distance',
    'GetSampleDistance'), ('vector_component', 'GetVectorComponent'),
    ('vector_mode', 'GetVectorMode'), ('average_ip_scalar_range',
    'GetAverageIPScalarRange'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_adjust_sample_distances', 'cropping',
    'debug', 'global_warning_display',
    'interactive_adjust_sample_distances', 'release_data_flag',
    'blend_mode', 'cropping_region_flags', 'interpolation_mode',
    'requested_render_mode', 'scalar_mode', 'average_ip_scalar_range',
    'final_color_level', 'final_color_window', 'interactive_update_rate',
    'max_memory_fraction', 'max_memory_in_bytes', 'progress_text',
    'sample_distance', 'vector_component', 'vector_mode'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SmartVolumeMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SmartVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_adjust_sample_distances', 'cropping',
            'interactive_adjust_sample_distances'], ['blend_mode',
            'cropping_region_flags', 'interpolation_mode',
            'requested_render_mode', 'scalar_mode'], ['average_ip_scalar_range',
            'final_color_level', 'final_color_window', 'interactive_update_rate',
            'max_memory_fraction', 'max_memory_in_bytes', 'sample_distance',
            'vector_component', 'vector_mode']),
            title='Edit SmartVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SmartVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


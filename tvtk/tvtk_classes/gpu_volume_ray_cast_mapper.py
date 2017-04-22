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


class GPUVolumeRayCastMapper(VolumeMapper):
    """
    GPUVolumeRayCastMapper - Ray casting performed on the GPU.
    
    Superclass: VolumeMapper
    
    GPUVolumeRayCastMapper is a volume mapper that performs ray
    casting on the GPU using fragment programs.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGPUVolumeRayCastMapper, obj, update, **traits)
    
    auto_adjust_sample_distances = tvtk_base.true_bool_trait(help=\
        """
        If auto_adjust_sample_distances is on, the the image_sample_distance
        will be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
    )

    def _auto_adjust_sample_distances_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoAdjustSampleDistances,
                        self.auto_adjust_sample_distances_)

    clamp_depth_to_backface = tvtk_base.false_bool_trait(help=\
        """
        Enable or disable clamping the depth value of the fully
        transparent voxel to the depth of the back-face of the volume.
        This parameter is used when render_to_image mode is enabled. When
        clamp_depth_to_back_face is false, the fully transparent voxels will
        have a value of 1.0 in the depth image. When this is true, the
        fully transparent voxels will have the depth value of the face at
        which the ray exits the volume. By default, this is set to 0
        (off).
        \sa set_render_to_image(), get_depth_image()
        """
    )

    def _clamp_depth_to_backface_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClampDepthToBackface,
                        self.clamp_depth_to_backface_)

    lock_sample_distance_to_input_spacing = tvtk_base.false_bool_trait(help=\
        """
        Compute the sample distance from the data spacing.  When the
        number of voxels is 8, the sample distance will be roughly 1/200
        the average voxel size. The distance will grow proportionally to
        num_voxels^(_1/_3). Off by default.
        """
    )

    def _lock_sample_distance_to_input_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLockSampleDistanceToInputSpacing,
                        self.lock_sample_distance_to_input_spacing_)

    render_to_image = tvtk_base.false_bool_trait(help=\
        """
        Enable or disable setting output of volume rendering to be color
        and depth textures. By default this is set to 0 (off). It should
        be noted that it is possible that underlying API specific mapper
        may not supoport render_to_image mode.
        \warning
        \li This method ignores any other volumes / props in the scene.
        \li This method does not respect the general attributes of the
        scene i.e. background color, etc. It always produces a color
        image that has a transparent white background outside the bounds
        of the volume.
        
        * \sa get_depth_image(), get_color_image()
        """
    )

    def _render_to_image_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRenderToImage,
                        self.render_to_image_)

    use_depth_pass = tvtk_base.false_bool_trait(help=\
        """
        If use_depth_pass is on, the mapper will use two passes. In the
        first pass, an isocontour depth buffer will be utilized as
        starting point for ray-casting hence eliminating traversal on
        voxels that are not going to participate in final rendering.
        use_depth_pass requires reasonable contour values to be set which
        can be set by calling get_depth_pass_contour_values() method and
        using ControurValues API.
        """
    )

    def _use_depth_pass_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseDepthPass,
                        self.use_depth_pass_)

    use_jittering = tvtk_base.false_bool_trait(help=\
        """
        If use_jittering is on, each ray traversal direction will be
        perturbed slightly using a noise-texture to get rid of wood-grain
        effect.
        """
    )

    def _use_jittering_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseJittering,
                        self.use_jittering_)

    depth_image_scalar_type = traits.Trait('float',
    tvtk_base.TraitRevPrefixMap({'float': 10, 'unsigned_char': 3, 'unsigned_short': 5}), help=\
        """
        Set/Get the scalar type of the depth texture in render_to_image
        mode. By default, the type if VTK_FLOAT.
        \sa set_render_to_image()
        """
    )

    def _depth_image_scalar_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepthImageScalarType,
                        self.depth_image_scalar_type_)

    mask_type = traits.Trait('label_map',
    tvtk_base.TraitRevPrefixMap({'label_map': 1, 'binary': 0}), help=\
        """
        Set the mask type, if mask is to be used. See documentation for
        set_mask_input(). The default is a label_map_mask_type.
        """
    )

    def _mask_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaskType,
                        self.mask_type_)

    final_color_level = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the window / level applied to the final color. This
        allows brightness / contrast adjustments on the final image.
        window is the width of the window. level is the center of the
        window. Initial window value is 1.0 Initial level value is 0.5
        window cannot be null but can be negative, this way values will
        be reversed. |window| can be larger than 1.0 level can be any
        real value.
        """
    )

    def _final_color_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFinalColorLevel,
                        self.final_color_level)

    final_color_window = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the window / level applied to the final color. This
        allows brightness / contrast adjustments on the final image.
        window is the width of the window. level is the center of the
        window. Initial window value is 1.0 Initial level value is 0.5
        window cannot be null but can be negative, this way values will
        be reversed. |window| can be larger than 1.0 level can be any
        real value.
        """
    )

    def _final_color_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFinalColorWindow,
                        self.final_color_window)

    image_sample_distance = traits.Trait(1.0, traits.Range(0.10000000149011612, 100.0, enter_set=True, auto_set=False), help=\
        """
        Sampling distance in the XY image dimensions. Default value of 1
        meaning 1 ray cast per pixel. If set to 0.5, 4 rays will be cast
        per pixel. If set to 2.0, 1 ray will be cast for every 4 (2 by 2)
        pixels. This value will be adjusted to meet a desired frame rate
        when auto_adjust_sample_distances is on.
        """
    )

    def _image_sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageSampleDistance,
                        self.image_sample_distance)

    mask_blend_factor = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Tells how much mask color transfer function is used compared to
        the standard color transfer function when the mask is true. This
        is relevant only for the label map mask. 0.0 means only standard
        color transfer function. 1.0 means only mask color transfer
        function. The default value is 1.0.
        """
    )

    def _mask_blend_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaskBlendFactor,
                        self.mask_blend_factor)

    def _get_mask_input(self):
        return wrap_vtk(self._vtk_obj.GetMaskInput())
    def _set_mask_input(self, arg):
        old_val = self._get_mask_input()
        self._wrap_call(self._vtk_obj.SetMaskInput,
                        deref_vtk(arg))
        self.trait_property_changed('mask_input', old_val, arg)
    mask_input = traits.Property(_get_mask_input, _set_mask_input, help=\
        """
        Optionally, set a mask input. This mask may be a binary mask or a
        label map. This must be specified via set_mask_type.
        
        * If the mask is a binary mask, the volume rendering is confined
          to regions
        * within the binary mask. The binary mask is assumed to have a
          datatype of
        * UCHAR and values of 255 (inside) and 0 (outside).
        
        * The mask may also be a label map. The label map is allowed to
          contain only
        * 3 labels (values of 0, 1 and 2) and must have a datatype of
          UCHAR. In voxels
        * with label value of 0, the color transfer function supplied by
          component
        * 0 is used.
        * In voxels with label value of 1, the color transfer function
          supplied by
        * component 1 is used and blended with the transfer function
          supplied by
        * component 0, with the blending weight being determined by
        * mask_blend_factor.
        * In voxels with a label value of 2, the color transfer function
          supplied
        * by component 2 is used and blended with the transfer function
          supplied by
        * component 0, with the blending weight being determined by
        * mask_blend_factor.
        """
    )

    max_memory_fraction = traits.Trait(0.75, traits.Range(0.10000000149011612, 1.0, enter_set=True, auto_set=False), help=\
        """
        Maximum fraction of the max_memory_in_bytes that should be used to
        hold the texture. Valid values are 0.1 to 1.0.
        """
    )

    def _max_memory_fraction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxMemoryFraction,
                        self.max_memory_fraction)

    max_memory_in_bytes = traits.Int(134217728, enter_set=True, auto_set=False, help=\
        """
        Maximum size of the 3d texture in GPU memory. Will default to the
        size computed from the graphics card. Can be adjusted by the
        user.
        """
    )

    def _max_memory_in_bytes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxMemoryInBytes,
                        self.max_memory_in_bytes)

    maximum_image_sample_distance = traits.Trait(10.0, traits.Range(0.10000000149011612, 100.0, enter_set=True, auto_set=False), help=\
        """
        This is the maximum image sample distance allow when the image
        sample distance is being automatically adjusted.
        """
    )

    def _maximum_image_sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumImageSampleDistance,
                        self.maximum_image_sample_distance)

    minimum_image_sample_distance = traits.Trait(1.0, traits.Range(0.10000000149011612, 100.0, enter_set=True, auto_set=False), help=\
        """
        This is the minimum image sample distance allow when the image
        sample distance is being automatically adjusted.
        """
    )

    def _minimum_image_sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumImageSampleDistance,
                        self.minimum_image_sample_distance)

    report_progress = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Tells if the mapper will report intermediate progress. Initial
        value is true. As the progress works with a GL blocking call
        (gl_finish()), this can be useful for huge dataset but can slow
        down rendering of small dataset. It should be set to true for big
        dataset or complex shading and streaming but to false for small
        datasets.
        """
    )

    def _report_progress_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReportProgress,
                        self.report_progress)

    sample_distance = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the distance between samples used for rendering when
        auto_adjust_sample_distances is off, or when this mapper has more
        than 1 second allocated to it for rendering. Initial value is
        1.0.
        """
    )

    def _sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleDistance,
                        self.sample_distance)

    def _get_auto_adjust_sample_distances_max_value(self):
        return self._vtk_obj.GetAutoAdjustSampleDistancesMaxValue()
    auto_adjust_sample_distances_max_value = traits.Property(_get_auto_adjust_sample_distances_max_value, help=\
        """
        If auto_adjust_sample_distances is on, the the image_sample_distance
        will be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
    )

    def _get_auto_adjust_sample_distances_min_value(self):
        return self._vtk_obj.GetAutoAdjustSampleDistancesMinValue()
    auto_adjust_sample_distances_min_value = traits.Property(_get_auto_adjust_sample_distances_min_value, help=\
        """
        If auto_adjust_sample_distances is on, the the image_sample_distance
        will be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
    )

    def get_color_image(self, *args):
        """
        V.get_color_image(ImageData)
        C++: virtual void GetColorImage(ImageData *)
        Low level API to export the color texture as ImageData in
        render_to_image mode. Should be implemented by the graphics API
        specific mapper (GL or other).
        \sa set_render_to_image()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetColorImage, *my_args)
        return ret

    def get_depth_image(self, *args):
        """
        V.get_depth_image(ImageData)
        C++: virtual void GetDepthImage(ImageData *)
        Low level API to export the depth texture as ImageData in
        render_to_image mode. Should be implemented by the graphics API
        specific mapper (GL or other).
        \sa set_render_to_image()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetDepthImage, *my_args)
        return ret

    def _get_depth_pass_contour_values(self):
        return wrap_vtk(self._vtk_obj.GetDepthPassContourValues())
    depth_pass_contour_values = traits.Property(_get_depth_pass_contour_values, help=\
        """
        Return handle to contour values container so that values can be
        set by the application. Contour values will be used only when
        use_depth_pass is on.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input data
        """
    )

    def _get_lock_sample_distance_to_input_spacing_max_value(self):
        return self._vtk_obj.GetLockSampleDistanceToInputSpacingMaxValue()
    lock_sample_distance_to_input_spacing_max_value = traits.Property(_get_lock_sample_distance_to_input_spacing_max_value, help=\
        """
        Compute the sample distance from the data spacing.  When the
        number of voxels is 8, the sample distance will be roughly 1/200
        the average voxel size. The distance will grow proportionally to
        num_voxels^(_1/_3). Off by default.
        """
    )

    def _get_lock_sample_distance_to_input_spacing_min_value(self):
        return self._vtk_obj.GetLockSampleDistanceToInputSpacingMinValue()
    lock_sample_distance_to_input_spacing_min_value = traits.Property(_get_lock_sample_distance_to_input_spacing_min_value, help=\
        """
        Compute the sample distance from the data spacing.  When the
        number of voxels is 8, the sample distance will be roughly 1/200
        the average voxel size. The distance will grow proportionally to
        num_voxels^(_1/_3). Off by default.
        """
    )

    def get_reduction_ratio(self, *args):
        """
        V.get_reduction_ratio([float, float, float])
        C++: virtual void GetReductionRatio(double ratio[3])
        Return how much the dataset has to be reduced in each dimension
        to fit on the GPU. If the value is 1.0, there is no need to
        reduce the dataset.
        \pre the calling thread has a current open_gl context.
        \pre mapper_supported:
            is_render_supported(renderer->_get_render_window(),_0)
        The computation is based on hardware limits (_3d texture indexable
        size) and max_memory_in_bytes.
        \post valid_i_ratio: ratio[0]>0 && ratio[0]<=1.0
        \post valid_j_ratio: ratio[1]>0 && ratio[1]<=1.0
        \post valid_k_ratio: ratio[2]>0 && ratio[2]<=1.0
        """
        ret = self._wrap_call(self._vtk_obj.GetReductionRatio, *args)
        return ret

    def _get_use_depth_pass_max_value(self):
        return self._vtk_obj.GetUseDepthPassMaxValue()
    use_depth_pass_max_value = traits.Property(_get_use_depth_pass_max_value, help=\
        """
        If use_depth_pass is on, the mapper will use two passes. In the
        first pass, an isocontour depth buffer will be utilized as
        starting point for ray-casting hence eliminating traversal on
        voxels that are not going to participate in final rendering.
        use_depth_pass requires reasonable contour values to be set which
        can be set by calling get_depth_pass_contour_values() method and
        using ControurValues API.
        """
    )

    def _get_use_depth_pass_min_value(self):
        return self._vtk_obj.GetUseDepthPassMinValue()
    use_depth_pass_min_value = traits.Property(_get_use_depth_pass_min_value, help=\
        """
        If use_depth_pass is on, the mapper will use two passes. In the
        first pass, an isocontour depth buffer will be utilized as
        starting point for ray-casting hence eliminating traversal on
        voxels that are not going to participate in final rendering.
        use_depth_pass requires reasonable contour values to be set which
        can be set by calling get_depth_pass_contour_values() method and
        using ControurValues API.
        """
    )

    def _get_use_jittering_max_value(self):
        return self._vtk_obj.GetUseJitteringMaxValue()
    use_jittering_max_value = traits.Property(_get_use_jittering_max_value, help=\
        """
        If use_jittering is on, each ray traversal direction will be
        perturbed slightly using a noise-texture to get rid of wood-grain
        effect.
        """
    )

    def _get_use_jittering_min_value(self):
        return self._vtk_obj.GetUseJitteringMinValue()
    use_jittering_min_value = traits.Property(_get_use_jittering_min_value, help=\
        """
        If use_jittering is on, each ray traversal direction will be
        perturbed slightly using a noise-texture to get rid of wood-grain
        effect.
        """
    )

    def create_canonical_view(self, *args):
        """
        V.create_canonical_view(Renderer, Volume, ImageData, int,
            [float, float, float], [float, float, float])
        C++: void CreateCanonicalView(Renderer *ren, Volume *volume,
             ImageData *image, int blend_mode, double viewDirection[3],
             double viewUp[3])"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CreateCanonicalView, *my_args)
        return ret

    def gpu_render(self, *args):
        """
        V.gpu_render(Renderer, Volume)
        C++: virtual void GPURender(Renderer *, Volume *)
        Handled in the subclass - the actual render method
        \pre input is up-to-date.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GPURender, *my_args)
        return ret

    def is_render_supported(self, *args):
        """
        V.is_render_supported(RenderWindow, VolumeProperty) -> int
        C++: virtual int IsRenderSupported(RenderWindow *window,
            VolumeProperty *property)
        Based on hardware and properties, we may or may not be able to
        render using 3d texture mapping. This indicates if 3d texture
        mapping is supported by the hardware, and if the other extensions
        necessary to support the specific properties are available.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsRenderSupported, *my_args)
        return ret

    _updateable_traits_ = \
    (('auto_adjust_sample_distances', 'GetAutoAdjustSampleDistances'),
    ('clamp_depth_to_backface', 'GetClampDepthToBackface'),
    ('lock_sample_distance_to_input_spacing',
    'GetLockSampleDistanceToInputSpacing'), ('render_to_image',
    'GetRenderToImage'), ('use_depth_pass', 'GetUseDepthPass'),
    ('use_jittering', 'GetUseJittering'), ('cropping', 'GetCropping'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('depth_image_scalar_type', 'GetDepthImageScalarType'), ('mask_type',
    'GetMaskType'), ('blend_mode', 'GetBlendMode'),
    ('cropping_region_flags', 'GetCroppingRegionFlags'), ('scalar_mode',
    'GetScalarMode'), ('final_color_level', 'GetFinalColorLevel'),
    ('final_color_window', 'GetFinalColorWindow'),
    ('image_sample_distance', 'GetImageSampleDistance'),
    ('mask_blend_factor', 'GetMaskBlendFactor'), ('max_memory_fraction',
    'GetMaxMemoryFraction'), ('max_memory_in_bytes',
    'GetMaxMemoryInBytes'), ('maximum_image_sample_distance',
    'GetMaximumImageSampleDistance'), ('minimum_image_sample_distance',
    'GetMinimumImageSampleDistance'), ('report_progress',
    'GetReportProgress'), ('sample_distance', 'GetSampleDistance'),
    ('average_ip_scalar_range', 'GetAverageIPScalarRange'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_adjust_sample_distances',
    'clamp_depth_to_backface', 'cropping', 'debug',
    'global_warning_display', 'lock_sample_distance_to_input_spacing',
    'release_data_flag', 'render_to_image', 'use_depth_pass',
    'use_jittering', 'blend_mode', 'cropping_region_flags',
    'depth_image_scalar_type', 'mask_type', 'scalar_mode',
    'average_ip_scalar_range', 'final_color_level', 'final_color_window',
    'image_sample_distance', 'mask_blend_factor', 'max_memory_fraction',
    'max_memory_in_bytes', 'maximum_image_sample_distance',
    'minimum_image_sample_distance', 'progress_text', 'report_progress',
    'sample_distance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GPUVolumeRayCastMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GPUVolumeRayCastMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_adjust_sample_distances', 'clamp_depth_to_backface',
            'cropping', 'lock_sample_distance_to_input_spacing',
            'render_to_image', 'use_depth_pass', 'use_jittering'], ['blend_mode',
            'cropping_region_flags', 'depth_image_scalar_type', 'mask_type',
            'scalar_mode'], ['average_ip_scalar_range', 'final_color_level',
            'final_color_window', 'image_sample_distance', 'mask_blend_factor',
            'max_memory_fraction', 'max_memory_in_bytes',
            'maximum_image_sample_distance', 'minimum_image_sample_distance',
            'report_progress', 'sample_distance']),
            title='Edit GPUVolumeRayCastMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GPUVolumeRayCastMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


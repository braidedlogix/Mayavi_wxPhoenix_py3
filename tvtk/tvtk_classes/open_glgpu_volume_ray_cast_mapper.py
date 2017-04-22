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

from tvtk.tvtk_classes.gpu_volume_ray_cast_mapper import GPUVolumeRayCastMapper


class OpenGLGPUVolumeRayCastMapper(GPUVolumeRayCastMapper):
    """
    OpenGLGPUVolumeRayCastMapper - no description provided.
    
    Superclass: GPUVolumeRayCastMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLGPUVolumeRayCastMapper, obj, update, **traits)
    
    def _get_color_texture(self):
        return wrap_vtk(self._vtk_obj.GetColorTexture())
    color_texture = traits.Property(_get_color_texture, help=\
        """
        Low level API to enable access to color texture in
        render_to_texture mode. It will return either NULL if render_to_image
        was never turned on or texture captured the last time
        render_to_image was on.
        """
    )

    def _get_current_pass(self):
        return self._vtk_obj.GetCurrentPass()
    current_pass = traits.Property(_get_current_pass, help=\
        """
        Mapper can have multiple passes and internally it will set the
        state. The state can not be set externally explicitly but can be
        set indirectly depending on the options set by the user.
        """
    )

    def _get_depth_texture(self):
        return wrap_vtk(self._vtk_obj.GetDepthTexture())
    depth_texture = traits.Property(_get_depth_texture, help=\
        """
        Low level API to enable access to depth texture in
        render_to_texture mode. It will return either NULL if render_to_image
        was never turned on or texture captured the last time
        render_to_image was on.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input data
        """
    )

    def set_noise_generator(self, *args):
        """
        V.set_noise_generator(ImplicitFunction)
        C++: void SetNoiseGenerator(ImplicitFunction *generator)
        Sets a user defined function to generate the ray jittering noise.
        PerlinNoise is used by default with a texture size equivlent
        to the window size. These settings will have no effect when
        use_jittering is Off.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetNoiseGenerator, *my_args)
        return ret

    def set_noise_texture_size(self, *args):
        """
        V.set_noise_texture_size(int, int)
        C++: void SetNoiseTextureSize(int, int)
        V.set_noise_texture_size((int, int))
        C++: void SetNoiseTextureSize(int a[2])"""
        ret = self._wrap_call(self._vtk_obj.SetNoiseTextureSize, *args)
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
            return super(OpenGLGPUVolumeRayCastMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLGPUVolumeRayCastMapper properties', scrollable=True, resizable=True,
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
            title='Edit OpenGLGPUVolumeRayCastMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLGPUVolumeRayCastMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.render_window import RenderWindow


class OpenGLRenderWindow(RenderWindow):
    """
    OpenGLRenderWindow - open_gl rendering window
    
    Superclass: RenderWindow
    
    OpenGLRenderWindow is a concrete implementation of the abstract
    class RenderWindow. OpenGLRenderer interfaces to the open_gl
    graphics library. Application programmers should normally use
    RenderWindow instead of the open_gl specific version.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLRenderWindow, obj, update, **traits)
    
    context_supports_open_gl32 = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Get if the context includes opengl core profile 3.2 support
        """
    )

    def _context_supports_open_gl32_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetContextSupportsOpenGL32,
                        self.context_supports_open_gl32)

    global_maximum_number_of_multi_samples = traits.Int(8, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum number of multisamples
        """
    )

    def _global_maximum_number_of_multi_samples_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobalMaximumNumberOfMultiSamples,
                        self.global_maximum_number_of_multi_samples)

    def get_pixel_data(self, *args):
        """
        V.get_pixel_data(int, int, int, int, int) -> (int, ...)
        C++: virtual unsigned char *GetPixelData(int x, int y, int x2,
            int y2, int front)
        V.get_pixel_data(int, int, int, int, int, UnsignedCharArray)
            -> int
        C++: virtual int GetPixelData(int x, int y, int x2, int y2,
            int front, UnsignedCharArray *data)
        Set/Get the pixel data of an image, transmitted as RGBRGB...
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'int'), ('int', 'int', 'int', 'int', 'int', 'vtkUnsignedCharArray')])
        ret = self._wrap_call(self._vtk_obj.GetPixelData, *my_args)
        return ret

    def set_pixel_data(self, *args):
        """
        V.set_pixel_data(int, int, int, int, [int, ...], int) -> int
        C++: virtual int SetPixelData(int x, int y, int x2, int y2,
            unsigned char *data, int front)
        V.set_pixel_data(int, int, int, int, UnsignedCharArray, int)
            -> int
        C++: virtual int SetPixelData(int x, int y, int x2, int y2,
            UnsignedCharArray *data, int front)
        Set/Get the pixel data of an image, transmitted as RGBRGB...
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', ['int', Ellipsis], 'int'), ('int', 'int', 'int', 'int', 'vtkUnsignedCharArray', 'int')])
        ret = self._wrap_call(self._vtk_obj.SetPixelData, *my_args)
        return ret

    def get_rgba_char_pixel_data(self, *args):
        """
        V.get_rgba_char_pixel_data(int, int, int, int, int) -> (int, ...)
        C++: virtual unsigned char *GetRGBACharPixelData(int x, int y,
            int x2, int y2, int front)
        V.get_rgba_char_pixel_data(int, int, int, int, int,
            UnsignedCharArray) -> int
        C++: virtual int GetRGBACharPixelData(int x, int y, int x2,
            int y2, int front, UnsignedCharArray *data)
        Set/Get the pixel data of an image, transmitted as RGBARGBA...
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'int'), ('int', 'int', 'int', 'int', 'int', 'vtkUnsignedCharArray')])
        ret = self._wrap_call(self._vtk_obj.GetRGBACharPixelData, *my_args)
        return ret

    def set_rgba_char_pixel_data(self, *args):
        """
        V.set_rgba_char_pixel_data(int, int, int, int, [int, ...], int, int)
            -> int
        C++: virtual int SetRGBACharPixelData(int x, int y, int x2,
            int y2, unsigned char *data, int front, int blend=0)
        V.set_rgba_char_pixel_data(int, int, int, int, UnsignedCharArray,
            int, int) -> int
        C++: virtual int SetRGBACharPixelData(int x, int y, int x2,
            int y2, UnsignedCharArray *data, int front, int blend=0)
        Set/Get the pixel data of an image, transmitted as RGBARGBA...
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', ['int', Ellipsis], 'int', 'int'), ('int', 'int', 'int', 'int', 'vtkUnsignedCharArray', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.SetRGBACharPixelData, *my_args)
        return ret

    def get_rgba_pixel_data(self, *args):
        """
        V.get_rgba_pixel_data(int, int, int, int, int) -> (float, ...)
        C++: virtual float *GetRGBAPixelData(int x, int y, int x2, int y2,
             int front)
        V.get_rgba_pixel_data(int, int, int, int, int, FloatArray) -> int
        C++: virtual int GetRGBAPixelData(int x, int y, int x2, int y2,
            int front, FloatArray *data)
        Set/Get the pixel data of an image, transmitted as RGBARGBA...
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'int'), ('int', 'int', 'int', 'int', 'int', 'vtkFloatArray')])
        ret = self._wrap_call(self._vtk_obj.GetRGBAPixelData, *my_args)
        return ret

    def set_rgba_pixel_data(self, *args):
        """
        V.set_rgba_pixel_data(int, int, int, int, [float, ...], int, int)
            -> int
        C++: virtual int SetRGBAPixelData(int x, int y, int x2, int y2,
            float *data, int front, int blend=0)
        V.set_rgba_pixel_data(int, int, int, int, FloatArray, int, int)
            -> int
        C++: virtual int SetRGBAPixelData(int x, int y, int x2, int y2,
            FloatArray *data, int front, int blend=0)
        Set/Get the pixel data of an image, transmitted as RGBARGBA...
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'tuple', 'int', 'int'), ('int', 'int', 'int', 'int', 'vtkFloatArray', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.SetRGBAPixelData, *my_args)
        return ret

    size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        Set the size of the window in screen coordinates in pixels.
        """
    )

    def _size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSize,
                        self.size)

    use_off_screen_buffers = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _use_off_screen_buffers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseOffScreenBuffers,
                        self.use_off_screen_buffers)

    def get_zbuffer_data(self, *args):
        """
        V.get_zbuffer_data(int, int, int, int) -> (float, ...)
        C++: virtual float *GetZbufferData(int x1, int y1, int x2, int y2)
        V.get_zbuffer_data(int, int, int, int, [float, ...]) -> int
        C++: virtual int GetZbufferData(int x1, int y1, int x2, int y2,
            float *z)
        V.get_zbuffer_data(int, int, int, int, FloatArray) -> int
        C++: virtual int GetZbufferData(int x1, int y1, int x2, int y2,
            FloatArray *z)
        Set/Get the zbuffer data from an image
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int'), ('int', 'int', 'int', 'int', 'tuple'), ('int', 'int', 'int', 'int', 'vtkFloatArray')])
        ret = self._wrap_call(self._vtk_obj.GetZbufferData, *my_args)
        return ret

    def set_zbuffer_data(self, *args):
        """
        V.set_zbuffer_data(int, int, int, int, [float, ...]) -> int
        C++: virtual int SetZbufferData(int x1, int y1, int x2, int y2,
            float *buffer)
        V.set_zbuffer_data(int, int, int, int, FloatArray) -> int
        C++: virtual int SetZbufferData(int x1, int y1, int x2, int y2,
            FloatArray *buffer)
        Set/Get the zbuffer data from an image
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'tuple'), ('int', 'int', 'int', 'int', 'vtkFloatArray')])
        ret = self._wrap_call(self._vtk_obj.SetZbufferData, *my_args)
        return ret

    def _get_back_buffer(self):
        return self._vtk_obj.GetBackBuffer()
    back_buffer = traits.Property(_get_back_buffer, help=\
        """
        Return the open_gl name of the back left buffer. It is GL_BACK if
        GL is bound to the window-system-provided framebuffer. It is
        vtkgl::COLOR_ATTACHMENT0_EXT if GL is bound to an
        application-created framebuffer object (GPU-based offscreen
        rendering) It is used by OpenGLCamera.
        """
    )

    def _get_back_left_buffer(self):
        return self._vtk_obj.GetBackLeftBuffer()
    back_left_buffer = traits.Property(_get_back_left_buffer, help=\
        """
        Return the open_gl name of the back left buffer. It is
        GL_BACK_LEFT if GL is bound to the window-system-provided
        framebuffer. It is vtkgl::COLOR_ATTACHMENT0_EXT if GL is bound to
        an application-created framebuffer object (GPU-based offscreen
        rendering) It is used by OpenGLCamera.
        """
    )

    def _get_back_right_buffer(self):
        return self._vtk_obj.GetBackRightBuffer()
    back_right_buffer = traits.Property(_get_back_right_buffer, help=\
        """
        Return the open_gl name of the back right buffer. It is
        GL_BACK_RIGHT if GL is bound to the window-system-provided
        framebuffer. It is vtkgl::COLOR_ATTACHMENT0_EXT+1 if GL is bound
        to an application-created framebuffer object (GPU-based offscreen
        rendering) It is used by OpenGLCamera.
        """
    )

    def _get_context_creation_time(self):
        return self._vtk_obj.GetContextCreationTime()
    context_creation_time = traits.Property(_get_context_creation_time, help=\
        """
        Get the time when the open_gl context was created.
        """
    )

    def get_default_texture_internal_format(self, *args):
        """
        V.get_default_texture_internal_format(int, int, bool, bool) -> int
        C++: int GetDefaultTextureInternalFormat(int vtktype,
            int numComponents, bool needInteger, bool needFloat)
        Get a mapping of vtk data types to native texture formats for
        this window we put this on the render_window so that every texture
        does not have to build these structures themselves
        """
        ret = self._wrap_call(self._vtk_obj.GetDefaultTextureInternalFormat, *args)
        return ret

    def _get_frame_buffer_object(self):
        return self._vtk_obj.GetFrameBufferObject()
    frame_buffer_object = traits.Property(_get_frame_buffer_object, help=\
        """
        Returns the current default FBO (0 when off_screen_rendering is
        inactive).
        """
    )

    def _get_front_buffer(self):
        return self._vtk_obj.GetFrontBuffer()
    front_buffer = traits.Property(_get_front_buffer, help=\
        """
        Return the open_gl name of the front left buffer. It is GL_FRONT
        if GL is bound to the window-system-provided framebuffer. It is
        vtkgl::COLOR_ATTACHMENT0_EXT if GL is bound to an
        application-created framebuffer object (GPU-based offscreen
        rendering) It is used by OpenGLCamera.
        """
    )

    def _get_front_left_buffer(self):
        return self._vtk_obj.GetFrontLeftBuffer()
    front_left_buffer = traits.Property(_get_front_left_buffer, help=\
        """
        Return the open_gl name of the front left buffer. It is
        GL_FRONT_LEFT if GL is bound to the window-system-provided
        framebuffer. It is vtkgl::COLOR_ATTACHMENT0_EXT if GL is bound to
        an application-created framebuffer object (GPU-based offscreen
        rendering) It is used by OpenGLCamera.
        """
    )

    def _get_front_right_buffer(self):
        return self._vtk_obj.GetFrontRightBuffer()
    front_right_buffer = traits.Property(_get_front_right_buffer, help=\
        """
        Return the open_gl name of the front right buffer. It is
        GL_FRONT_RIGHT if GL is bound to the window-system-provided
        framebuffer. It is vtkgl::COLOR_ATTACHMENT0_EXT+1 if GL is bound
        to an application-created framebuffer object (GPU-based offscreen
        rendering) It is used by OpenGLCamera.
        """
    )

    def _get_maximum_hardware_line_width(self):
        return self._vtk_obj.GetMaximumHardwareLineWidth()
    maximum_hardware_line_width = traits.Property(_get_maximum_hardware_line_width, help=\
        """
        Return the largest line width supported by the hardware
        """
    )

    def _get_open_gl_support_message(self):
        return self._vtk_obj.GetOpenGLSupportMessage()
    open_gl_support_message = traits.Property(_get_open_gl_support_message, help=\
        """
        Return a message profiding additional details about the results
        of calling supports_open_gl()  This can be used to retrieve more
        specifics about what failed
        """
    )

    def get_open_gl_version(self, *args):
        """
        V.get_open_gl_version(int, int)
        C++: void GetOpenGLVersion(int &major, int &minor)
        Get the major and minor version numbers of the open_gl context we
        are using ala 3.2, 3.3, 4.0, etc... returns 0,0 if opengl has not
        been initialized yet
        """
        ret = self._wrap_call(self._vtk_obj.GetOpenGLVersion, *args)
        return ret

    def _get_shader_cache(self):
        return wrap_vtk(self._vtk_obj.GetShaderCache())
    shader_cache = traits.Property(_get_shader_cache, help=\
        """
        Returns an Shader Cache object
        """
    )

    def get_texture_unit_for_texture(self, *args):
        """
        V.get_texture_unit_for_texture(TextureObject) -> int
        C++: int GetTextureUnitForTexture(TextureObject *)
        Get the texture unit for a given texture object
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetTextureUnitForTexture, *my_args)
        return ret

    def _get_texture_unit_manager(self):
        return wrap_vtk(self._vtk_obj.GetTextureUnitManager())
    texture_unit_manager = traits.Property(_get_texture_unit_manager, help=\
        """
        Returns its texture unit manager object. A new one will be
        created if one hasn't already been set up.
        """
    )

    def activate_texture(self, *args):
        """
        V.activate_texture(TextureObject)
        C++: void ActivateTexture(TextureObject *)
        Activate a texture unit for this texture
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ActivateTexture, *my_args)
        return ret

    def deactivate_texture(self, *args):
        """
        V.deactivate_texture(TextureObject)
        C++: void DeactivateTexture(TextureObject *)
        Deactive a previously activated texture
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeactivateTexture, *my_args)
        return ret

    def draw_pixels(self, *args):
        """
        V.draw_pixels(int, int, int, int, int, int, void)
        C++: virtual void DrawPixels(int x1, int y1, int x2, int y2,
            int numComponents, int dataType, void *data)
        V.draw_pixels(int, int, int, int, int, int, int, int, int, int,
            int, int, void)
        C++: virtual void DrawPixels(int dstXmin, int dstYmin,
            int dstXmax, int dstYmax, int srcXmin, int srcYmin,
            int srcXmax, int srcYmax, int srcWidth, int srcHeight,
            int numComponents, int dataType, void *data)
        V.draw_pixels(int, int, int, int, void)
        C++: virtual void DrawPixels(int srcWidth, int srcHeight,
            int numComponents, int dataType, void *data)
        Replacement for the old gl_draw_pixels function
        """
        ret = self._wrap_call(self._vtk_obj.DrawPixels, *args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize(void)
        Initialize the rendering window.  This will setup all
        system-specific resources.  This method and Finalize() must be
        symmetric and it should be possible to call them multiple times,
        even changing window_id in-between.  This is what window_remap
        does.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def is_point_sprite_bug_present(self):
        """
        V.is_point_sprite_bug_present() -> bool
        C++: virtual bool IsPointSpriteBugPresent()
        Returns true if driver has an egl/_open_gl bug that makes
        ChartsCoreCxx-TestChartDoubleColors and other tests to fail
        because point sprites don't work correctly (gl__point_coord is
        undefined) unless gl_enable(_gl__point__sprite)
        """
        ret = self._vtk_obj.IsPointSpriteBugPresent()
        return ret
        

    def open_gl_init(self):
        """
        V.open_gl_init()
        C++: virtual void OpenGLInit()
        Initialize open_gl for this window.
        """
        ret = self._vtk_obj.OpenGLInit()
        return ret
        

    def open_gl_init_context(self):
        """
        V.open_gl_init_context()
        C++: virtual void OpenGLInitContext()"""
        ret = self._vtk_obj.OpenGLInitContext()
        return ret
        

    def open_gl_init_state(self):
        """
        V.open_gl_init_state()
        C++: virtual void OpenGLInitState()"""
        ret = self._vtk_obj.OpenGLInitState()
        return ret
        

    def pop_context(self):
        """
        V.pop_context()
        C++: virtual void PopContext()"""
        ret = self._vtk_obj.PopContext()
        return ret
        

    def push_context(self):
        """
        V.push_context()
        C++: virtual void PushContext()
        Ability to push and pop this window's context as the current
        context. The idea being to if needed make this window's context
        current and when done releasing resources restore the prior
        context.  The default implementation here is only meant as a
        backup for subclasses that lack a proper implementation.
        """
        ret = self._vtk_obj.PushContext()
        return ret
        

    def register_graphics_resources(self, *args):
        """
        V.register_graphics_resources(GenericOpenGLResourceFreeCallback)
        C++: void RegisterGraphicsResources(
            GenericOpenGLResourceFreeCallback *cb)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RegisterGraphicsResources, *my_args)
        return ret

    def unregister_graphics_resources(self, *args):
        """
        V.unregister_graphics_resources(
            GenericOpenGLResourceFreeCallback)
        C++: void UnregisterGraphicsResources(
            GenericOpenGLResourceFreeCallback *cb)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UnregisterGraphicsResources, *my_args)
        return ret

    _updateable_traits_ = \
    (('borders', 'GetBorders'), ('full_screen', 'GetFullScreen'),
    ('is_picking', 'GetIsPicking'), ('line_smoothing',
    'GetLineSmoothing'), ('point_smoothing', 'GetPointSmoothing'),
    ('polygon_smoothing', 'GetPolygonSmoothing'), ('stencil_capable',
    'GetStencilCapable'), ('stereo_capable_window',
    'GetStereoCapableWindow'), ('stereo_render', 'GetStereoRender'),
    ('swap_buffers', 'GetSwapBuffers'), ('double_buffer',
    'GetDoubleBuffer'), ('erase', 'GetErase'), ('mapped', 'GetMapped'),
    ('off_screen_rendering', 'GetOffScreenRendering'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('stereo_type', 'GetStereoType'), ('context_supports_open_gl32',
    'GetContextSupportsOpenGL32'),
    ('global_maximum_number_of_multi_samples',
    'GetGlobalMaximumNumberOfMultiSamples'), ('size', 'GetSize'),
    ('use_off_screen_buffers', 'GetUseOffScreenBuffers'), ('aa_frames',
    'GetAAFrames'), ('abort_render', 'GetAbortRender'),
    ('alpha_bit_planes', 'GetAlphaBitPlanes'), ('anaglyph_color_mask',
    'GetAnaglyphColorMask'), ('anaglyph_color_saturation',
    'GetAnaglyphColorSaturation'), ('current_cursor', 'GetCurrentCursor'),
    ('desired_update_rate', 'GetDesiredUpdateRate'), ('device_index',
    'GetDeviceIndex'), ('fd_frames', 'GetFDFrames'), ('in_abort_check',
    'GetInAbortCheck'), ('multi_samples', 'GetMultiSamples'),
    ('number_of_layers', 'GetNumberOfLayers'), ('sub_frames',
    'GetSubFrames'), ('use_constant_fd_offsets',
    'GetUseConstantFDOffsets'), ('dpi', 'GetDPI'), ('position',
    'GetPosition'), ('tile_scale', 'GetTileScale'), ('tile_viewport',
    'GetTileViewport'), ('window_name', 'GetWindowName'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['borders', 'debug', 'double_buffer', 'erase', 'full_screen',
    'global_warning_display', 'is_picking', 'line_smoothing', 'mapped',
    'off_screen_rendering', 'point_smoothing', 'polygon_smoothing',
    'stencil_capable', 'stereo_capable_window', 'stereo_render',
    'swap_buffers', 'stereo_type', 'aa_frames', 'abort_render',
    'alpha_bit_planes', 'anaglyph_color_mask',
    'anaglyph_color_saturation', 'context_supports_open_gl32',
    'current_cursor', 'desired_update_rate', 'device_index', 'dpi',
    'fd_frames', 'global_maximum_number_of_multi_samples',
    'in_abort_check', 'multi_samples', 'number_of_layers', 'position',
    'size', 'sub_frames', 'tile_scale', 'tile_viewport',
    'use_constant_fd_offsets', 'use_off_screen_buffers', 'window_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLRenderWindow, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLRenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['borders', 'double_buffer', 'erase', 'full_screen',
            'is_picking', 'line_smoothing', 'mapped', 'off_screen_rendering',
            'point_smoothing', 'polygon_smoothing', 'stencil_capable',
            'stereo_capable_window', 'stereo_render', 'swap_buffers'],
            ['stereo_type'], ['aa_frames', 'abort_render', 'alpha_bit_planes',
            'anaglyph_color_mask', 'anaglyph_color_saturation',
            'context_supports_open_gl32', 'current_cursor', 'desired_update_rate',
            'device_index', 'dpi', 'fd_frames',
            'global_maximum_number_of_multi_samples', 'in_abort_check',
            'multi_samples', 'number_of_layers', 'position', 'size', 'sub_frames',
            'tile_scale', 'tile_viewport', 'use_constant_fd_offsets',
            'use_off_screen_buffers', 'window_name']),
            title='Edit OpenGLRenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLRenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


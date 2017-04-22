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

from tvtk.tvtk_classes.window import Window


class RenderWindow(Window):
    """
    RenderWindow - create a window for renderers to draw into
    
    Superclass: Window
    
    RenderWindow is an abstract object to specify the behavior of a
    rendering window. A rendering window is a window in a graphical user
    interface where renderers draw their images. Methods are provided to
    synchronize the rendering process, set window size, and control
    double buffering.  The window also allows rendering in stereo.  The
    interlaced render stereo type is for output to a VRex stereo
    projector.  All of the odd horizontal lines are from the left eye,
    and the even lines are from the right eye.  The user has to make the
    render window aligned with the VRex projector, or the eye will be
    swapped.
    
    @warning
    In VTK versions 4 and later, the WindowToImageFilter class is part
    of the canonical way to output an image of a window to a file
    (replacing the obsolete save_image_as_ppm method for RenderWindows
    that existed in 3.2 and earlier).  Connect one of these filters to
    the output of the window, and filter's output to a writer such as
    PNGWriter.
    
    @sa
    Renderer RenderWindowInteractor WindowToImageFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderWindow, obj, update, **traits)
    
    borders = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off window manager borders. Typically, you shouldn't turn
        the borders off, because that bypasses the window manager and can
        cause undesirable behavior.
        """
    )

    def _borders_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorders,
                        self.borders_)

    full_screen = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off rendering full screen window size.
        """
    )

    def _full_screen_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFullScreen,
                        self.full_screen_)

    is_picking = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _is_picking_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIsPicking,
                        self.is_picking_)

    line_smoothing = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off line smoothing. Default is off. This must be applied
        before the first Render.
        """
    )

    def _line_smoothing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineSmoothing,
                        self.line_smoothing_)

    point_smoothing = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off point smoothing. Default is off. This must be applied
        before the first Render.
        """
    )

    def _point_smoothing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointSmoothing,
                        self.point_smoothing_)

    polygon_smoothing = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off polygon smoothing. Default is off. This must be
        applied before the first Render.
        """
    )

    def _polygon_smoothing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolygonSmoothing,
                        self.polygon_smoothing_)

    stencil_capable = tvtk_base.false_bool_trait(help=\
        """
        Set / Get the availability of the stencil buffer.
        """
    )

    def _stencil_capable_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStencilCapable,
                        self.stencil_capable_)

    stereo_capable_window = tvtk_base.false_bool_trait(help=\
        """
        Prescribe that the window be created in a stereo-capable mode.
        This method must be called before the window is realized. Default
        is off.
        """
    )

    def _stereo_capable_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStereoCapableWindow,
                        self.stereo_capable_window_)

    stereo_render = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off stereo rendering.
        """
    )

    def _stereo_render_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStereoRender,
                        self.stereo_render_)

    swap_buffers = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off buffer swapping between images.
        """
    )

    def _swap_buffers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSwapBuffers,
                        self.swap_buffers_)

    stereo_type = traits.Trait('crystal_eyes',
    tvtk_base.TraitRevPrefixMap({'crystal_eyes': 1, 'anaglyph': 7, 'checkerboard': 8, 'dresden': 6, 'fake': 10, 'interlaced': 3, 'left': 4, 'red_blue': 2, 'right': 5, 'split_viewport_horizontal': 9}), help=\
        """
        Set/Get what type of stereo rendering to use.  crystal_eyes mode
        uses frame-sequential capabilities available in open_gl to drive
        LCD shutter glasses and stereo projectors.  red_blue mode is a
        simple type of stereo for use with red-blue glasses. Anaglyph
        mode is a superset of red_blue mode, but the color output channels
        can be configured using the anaglyph_color_mask and the color of
        the original image can be (somewhat) maintained using
        anaglyph_color_saturation;  the default colors for Anaglyph mode is
        red-cyan.  Interlaced stereo mode produces a composite image
        where horizontal lines alternate between left and right views. 
        stereo_left and stereo_right modes choose one or the other stereo
        view.  Dresden mode is yet another stereoscopic interleaving.
        Fake simply causes the window to render twice without actually
        swapping the camera from left eye to right eye. This is useful in
        certain applications that want to emulate the rendering passes
        without actually rendering in stereo mode.
        """
    )

    def _stereo_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStereoType,
                        self.stereo_type_)

    aa_frames = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of frames for doing antialiasing. The default is
        zero. Typically five or six will yield reasonable results without
        taking too long.
        """
    )

    def _aa_frames_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAAFrames,
                        self.aa_frames)

    abort_render = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This is a flag that can be set to interrupt a rendering that is
        in progress.
        """
    )

    def _abort_render_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAbortRender,
                        self.abort_render)

    alpha_bit_planes = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Turn on/off the use of alpha bitplanes.
        """
    )

    def _alpha_bit_planes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlphaBitPlanes,
                        self.alpha_bit_planes)

    anaglyph_color_mask = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(4, 3), cols=2, help=\
        """
        
        """
    )

    def _anaglyph_color_mask_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAnaglyphColorMask,
                        self.anaglyph_color_mask)

    anaglyph_color_saturation = traits.Trait(0.6499999761581421, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/get the anaglyph color saturation factor.  This number ranges
        from 0.0 to 1.0:  0.0 means that no color from the original
        object is maintained, 1.0 means all of the color is maintained. 
        The default value is 0.65.  Too much saturation can produce
        uncomfortable 3d viewing because anaglyphs also use color to
        encode 3d.
        """
    )

    def _anaglyph_color_saturation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAnaglyphColorSaturation,
                        self.anaglyph_color_saturation)

    current_cursor = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Change the shape of the cursor.
        """
    )

    def _current_cursor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCurrentCursor,
                        self.current_cursor)

    desired_update_rate = traits.Float(0.0001, enter_set=True, auto_set=False, help=\
        """
        Set/Get the desired update rate. This is used with the
        LODActor class. When using level of detail actors you need to
        specify what update rate you require. The LODActors then will
        pick the correct resolution to meet your desired update rate in
        frames per second. A value of zero indicates that they can use
        all the time they want to.
        """
    )

    def _desired_update_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDesiredUpdateRate,
                        self.desired_update_rate)

    device_index = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        If there are several graphics card installed on a system, this
        index can be used to specify which card you want to render to.
        the default is 0. This may not work on all derived render window
        and it may need to be set before the first render.
        """
    )

    def _device_index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeviceIndex,
                        self.device_index)

    fd_frames = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of frames for doing focal depth. The default is
        zero. Depending on how your scene is organized you can get away
        with as few as four frames for focal depth or you might need
        thirty. One thing to note is that if you are using focal depth
        frames, then you will not need many (if any) frames for
        antialiasing.
        """
    )

    def _fd_frames_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFDFrames,
                        self.fd_frames)

    in_abort_check = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This is a flag that can be set to interrupt a rendering that is
        in progress.
        """
    )

    def _in_abort_check_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInAbortCheck,
                        self.in_abort_check)

    def _get_interactor(self):
        return wrap_vtk(self._vtk_obj.GetInteractor())
    def _set_interactor(self, arg):
        old_val = self._get_interactor()
        self._wrap_call(self._vtk_obj.SetInteractor,
                        deref_vtk(arg))
        self.trait_property_changed('interactor', old_val, arg)
    interactor = traits.Property(_get_interactor, _set_interactor, help=\
        """
        Get the interactor associated with this render window
        """
    )

    multi_samples = traits.Int(8, enter_set=True, auto_set=False, help=\
        """
        Set / Get the number of multisamples to use for hardware
        antialiasing.
        """
    )

    def _multi_samples_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMultiSamples,
                        self.multi_samples)

    number_of_layers = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Get the number of layers for renderers.  Each renderer should
        have its layer set individually.  Some algorithms iterate through
        all layers, so it is not wise to set the number of layers to be
        exorbitantly large (say bigger than 100).
        """
    )

    def _number_of_layers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfLayers,
                        self.number_of_layers)

    def get_pixel_data(self, *args):
        """
        V.get_pixel_data(int, int, int, int, int) -> (int, ...)
        C++: virtual unsigned char *GetPixelData(int x, int y, int x2,
            int y2, int front)
        V.get_pixel_data(int, int, int, int, int, UnsignedCharArray)
            -> int
        C++: virtual int GetPixelData(int x, int y, int x2, int y2,
            int front, UnsignedCharArray *data)
        Get the pixel data of an image, transmitted as RGBRGBRGB. The
        front argument indicates if the front buffer should be used or
        the back buffer. It is the caller's responsibility to delete the
        resulting array. It is very important to realize that the memory
        in this array is organized from the bottom of the window to the
        top. The origin of the screen is in the lower left corner. The y
        axis increases as you go up the screen. So the storage of pixels
        is from left to right and from bottom to top. (x,y) is any corner
        of the rectangle. (x2,y2) is its opposite corner on the diagonal.
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
        Set/Get the pixel data of an image, transmitted as RGBRGBRGB. The
        front argument indicates if the front buffer should be used or
        the back buffer. It is the caller's responsibility to delete the
        resulting array. It is very important to realize that the memory
        in this array is organized from the bottom of the window to the
        top. The origin of the screen is in the lower left corner. The y
        axis increases as you go up the screen. So the storage of pixels
        is from left to right and from bottom to top. (x,y) is any corner
        of the rectangle. (x2,y2) is its opposite corner on the diagonal.
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
        Same as get/_set_pixel_data except that the image also contains an
        alpha component. The image is transmitted as RGBARGBARGBA... each
        of which is a float value. The "blend" parameter controls whether
        the set_rgba_pixel_data method blends the data with the previous
        contents of the frame buffer or completely replaces the frame
        buffer data.
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
        Same as get/_set_pixel_data except that the image also contains an
        alpha component. The image is transmitted as RGBARGBARGBA... each
        of which is a float value. The "blend" parameter controls whether
        the set_rgba_pixel_data method blends the data with the previous
        contents of the frame buffer or completely replaces the frame
        buffer data.
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
        Same as get/_set_pixel_data except that the image also contains an
        alpha component. The image is transmitted as RGBARGBARGBA... each
        of which is a float value. The "blend" parameter controls whether
        the set_rgba_pixel_data method blends the data with the previous
        contents of the frame buffer or completely replaces the frame
        buffer data.
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'int'), ('int', 'int', 'int', 'int', 'int', 'vtkFloatArray')])
        ret = self._wrap_call(self._vtk_obj.GetRGBAPixelData, *my_args)
        return ret

    def set_rgba_pixel_data(self, *args):
        """
        V.set_rgba_pixel_data(int, int, int, int, [float, ...], int, int)
            -> int
        C++: virtual int SetRGBAPixelData(int x, int y, int x2, int y2,
            float *, int front, int blend=0)
        V.set_rgba_pixel_data(int, int, int, int, FloatArray, int, int)
            -> int
        C++: virtual int SetRGBAPixelData(int, int, int, int,
            FloatArray *, int, int blend=0)
        Same as get/_set_pixel_data except that the image also contains an
        alpha component. The image is transmitted as RGBARGBARGBA... each
        of which is a float value. The "blend" parameter controls whether
        the set_rgba_pixel_data method blends the data with the previous
        contents of the frame buffer or completely replaces the frame
        buffer data.
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'tuple', 'int', 'int'), ('int', 'int', 'int', 'int', 'vtkFloatArray', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.SetRGBAPixelData, *my_args)
        return ret

    sub_frames = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of sub frames for doing motion blur. The default
        is zero. Once this is set greater than one, you will no longer
        see a new frame for every Render().  If you set this to five, you
        will need to do five Render() invocations before seeing the
        result. This isn't very impressive unless something is changing
        between the Renders. Changing this value may reset the current
        subframe count.
        """
    )

    def _sub_frames_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubFrames,
                        self.sub_frames)

    use_constant_fd_offsets = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Turn on/off using constant offsets for focal depth rendering. The
        default is off. When constants offsets are used, re-rendering the
        same scene using the same camera yields the same image; otherwise
        offsets are random numbers at each rendering that yields slightly
        different images.
        """
    )

    def _use_constant_fd_offsets_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseConstantFDOffsets,
                        self.use_constant_fd_offsets)

    use_off_screen_buffers = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Create and bind offscreen rendering buffers without destroying
        the current open_gl context. This allows to temporary switch to
        offscreen rendering (ie. to make a screenshot even if the window
        is hidden). Return if the creation was successful (1) or not (0).
        Note: This function requires that the device supports open_gl
        framebuffer extension. The function has no effect if
        off_screen_rendering is ON.
        """
    )

    def _use_off_screen_buffers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseOffScreenBuffers,
                        self.use_off_screen_buffers)

    def get_zbuffer_data(self, *args):
        """
        V.get_zbuffer_data(int, int, int, int) -> (float, ...)
        C++: virtual float *GetZbufferData(int x, int y, int x2, int y2)
        V.get_zbuffer_data(int, int, int, int, [float, ...]) -> int
        C++: virtual int GetZbufferData(int x, int y, int x2, int y2,
            float *z)
        V.get_zbuffer_data(int, int, int, int, FloatArray) -> int
        C++: virtual int GetZbufferData(int x, int y, int x2, int y2,
            FloatArray *z)
        Set/Get the zbuffer data from the frame buffer. (x,y) is any
        corner of the rectangle. (x2,y2) is its opposite corner on the
        diagonal.
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int'), ('int', 'int', 'int', 'int', 'tuple'), ('int', 'int', 'int', 'int', 'vtkFloatArray')])
        ret = self._wrap_call(self._vtk_obj.GetZbufferData, *my_args)
        return ret

    def set_zbuffer_data(self, *args):
        """
        V.set_zbuffer_data(int, int, int, int, [float, ...]) -> int
        C++: virtual int SetZbufferData(int x, int y, int x2, int y2,
            float *z)
        V.set_zbuffer_data(int, int, int, int, FloatArray) -> int
        C++: virtual int SetZbufferData(int x, int y, int x2, int y2,
            FloatArray *z)
        Set/Get the zbuffer data from the frame buffer. (x,y) is any
        corner of the rectangle. (x2,y2) is its opposite corner on the
        diagonal.
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'tuple'), ('int', 'int', 'int', 'int', 'vtkFloatArray')])
        ret = self._wrap_call(self._vtk_obj.SetZbufferData, *my_args)
        return ret

    def _get_capturing_gl2ps_special_props(self):
        return self._vtk_obj.GetCapturingGL2PSSpecialProps()
    capturing_gl2ps_special_props = traits.Property(_get_capturing_gl2ps_special_props, help=\
        """
        Returns true if the render process is capturing text actors.
        """
    )

    def get_color_buffer_sizes(self, *args):
        """
        V.get_color_buffer_sizes([int, ...]) -> int
        C++: virtual int GetColorBufferSizes(int *rgba)
        Get the size of the color buffer. Returns 0 if not able to
        determine otherwise sets R G B and A into buffer.
        """
        ret = self._wrap_call(self._vtk_obj.GetColorBufferSizes, *args)
        return ret

    def _get_depth_buffer_size(self):
        return self._vtk_obj.GetDepthBufferSize()
    depth_buffer_size = traits.Property(_get_depth_buffer_size, help=\
        """
        This method should be defined by the subclass. How many bits of
        precision are there in the zbuffer?
        """
    )

    def _get_event_pending(self):
        return self._vtk_obj.GetEventPending()
    event_pending = traits.Property(_get_event_pending, help=\
        """
        Check to see if a mouse button has been pressed.  All other
        events are ignored by this method.  Ideally, you want to abort
        the render on any event which causes the desired_update_rate to
        switch from a high-quality rate to a more interactive rate.
        """
    )

    def _get_never_rendered(self):
        return self._vtk_obj.GetNeverRendered()
    never_rendered = traits.Property(_get_never_rendered, help=\
        """
        This flag is set if the window hasn't rendered since it was
        created
        """
    )

    def _get_number_of_devices(self):
        return self._vtk_obj.GetNumberOfDevices()
    number_of_devices = traits.Property(_get_number_of_devices, help=\
        """
        Returns the number of devices (graphics cards) on a system. This
        may not work on all derived render windows.
        """
    )

    def _get_painter_device_adapter(self):
        return wrap_vtk(self._vtk_obj.GetPainterDeviceAdapter())
    painter_device_adapter = traits.Property(_get_painter_device_adapter, help=\
        """
        Get the PainterDeviceAdapter which can be used to paint on
        this render window.  Note the old open_gl backend requires this
        method.
        """
    )

    def _get_render_library(self):
        return self._vtk_obj.GetRenderLibrary()
    render_library = traits.Property(_get_render_library, help=\
        """
        What rendering library has the user requested
        """
    )

    def _get_renderers(self):
        return wrap_vtk(self._vtk_obj.GetRenderers())
    renderers = traits.Property(_get_renderers, help=\
        """
        Return the collection of renderers in the render window.
        """
    )

    def _get_rendering_backend(self):
        return self._vtk_obj.GetRenderingBackend()
    rendering_backend = traits.Property(_get_rendering_backend, help=\
        """
        What rendering backend has the user requested
        """
    )

    def get_zbuffer_data_at_point(self, *args):
        """
        V.get_zbuffer_data_at_point(int, int) -> float
        C++: float GetZbufferDataAtPoint(int x, int y)
        Set/Get the zbuffer data from the frame buffer. (x,y) is any
        corner of the rectangle. (x2,y2) is its opposite corner on the
        diagonal.
        """
        ret = self._wrap_call(self._vtk_obj.GetZbufferDataAtPoint, *args)
        return ret

    def add_renderer(self, *args):
        """
        V.add_renderer(Renderer)
        C++: virtual void AddRenderer(Renderer *)
        Add a renderer to the list of renderers.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddRenderer, *my_args)
        return ret

    def alpha_bit_planes_off(self):
        """
        V.alpha_bit_planes_off()
        C++: void AlphaBitPlanesOff()
        Turn on/off the use of alpha bitplanes.
        """
        ret = self._vtk_obj.AlphaBitPlanesOff()
        return ret
        

    def alpha_bit_planes_on(self):
        """
        V.alpha_bit_planes_on()
        C++: void AlphaBitPlanesOn()
        Turn on/off the use of alpha bitplanes.
        """
        ret = self._vtk_obj.AlphaBitPlanesOn()
        return ret
        

    def capture_gl2ps_special_props(self, *args):
        """
        V.capture_gl2ps_special_props(Collection)
        C++: void CaptureGL2PSSpecialProps(Collection *specialProps)
        The gl2ps exporter must handle certain props in a special way
        (e.g. text). This method performs a render and captures all
        "_gl2ps-special" props in the specified collection. The collection
        will contain a PropCollection for each Renderer in
        this->_get_renderers(), each containing the special props rendered
        by the corresponding renderer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CaptureGL2PSSpecialProps, *my_args)
        return ret

    def check_abort_status(self):
        """
        V.check_abort_status() -> int
        C++: virtual int CheckAbortStatus()
        This is a flag that can be set to interrupt a rendering that is
        in progress.
        """
        ret = self._vtk_obj.CheckAbortStatus()
        return ret
        

    def check_in_render_status(self):
        """
        V.check_in_render_status() -> int
        C++: virtual int CheckInRenderStatus()
        Are we rendering at the moment
        """
        ret = self._vtk_obj.CheckInRenderStatus()
        return ret
        

    def clear_in_render_status(self):
        """
        V.clear_in_render_status()
        C++: virtual void ClearInRenderStatus()
        Clear status (after an exception was thrown for example)
        """
        ret = self._vtk_obj.ClearInRenderStatus()
        return ret
        

    def copy_result_frame(self):
        """
        V.copy_result_frame()
        C++: virtual void CopyResultFrame()
        Performed at the end of the rendering process to generate image.
        This is typically done right before swapping buffers.
        """
        ret = self._vtk_obj.CopyResultFrame()
        return ret
        

    def finalize(self):
        """
        V.finalize()
        C++: virtual void Finalize()
        Finalize the rendering process.
        """
        ret = self._vtk_obj.Finalize()
        return ret
        

    def frame(self):
        """
        V.frame()
        C++: virtual void Frame()
        A termination method performed at the end of the rendering
        process to do things like swapping buffers (if necessary) or
        similar actions.
        """
        ret = self._vtk_obj.Frame()
        return ret
        

    def has_renderer(self, *args):
        """
        V.has_renderer(Renderer) -> int
        C++: int HasRenderer(Renderer *)
        Query if a renderer is in the list of renderers.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HasRenderer, *my_args)
        return ret

    def hide_cursor(self):
        """
        V.hide_cursor()
        C++: virtual void HideCursor()
        Hide or Show the mouse cursor, it is nice to be able to hide the
        default cursor if you want VTK to display a 3d cursor instead.
        Set cursor position in window (note that (0,0) is the lower left
        corner).
        """
        ret = self._vtk_obj.HideCursor()
        return ret
        

    def initialize_from_current_context(self):
        """
        V.initialize_from_current_context() -> bool
        C++: virtual bool InitializeFromCurrentContext()
        Initialize the render window from the information associated with
        the currently activated open_gl context.
        """
        ret = self._vtk_obj.InitializeFromCurrentContext()
        return ret
        

    def is_current(self):
        """
        V.is_current() -> bool
        C++: virtual bool IsCurrent()
        Tells if this window is the current graphics context for the
        calling thread.
        """
        ret = self._vtk_obj.IsCurrent()
        return ret
        

    def is_direct(self):
        """
        V.is_direct() -> int
        C++: virtual int IsDirect()
        Is this render window using hardware acceleration? 0-false,
        1-true
        """
        ret = self._vtk_obj.IsDirect()
        return ret
        

    def is_drawable(self):
        """
        V.is_drawable() -> bool
        C++: virtual bool IsDrawable()
        Test if the window has a valid drawable. This is currently only
        an issue on Mac OS X Cocoa where rendering to an invalid drawable
        results in all open_gl calls to fail with "invalid framebuffer
        operation".
        """
        ret = self._vtk_obj.IsDrawable()
        return ret
        

    def make_render_window_interactor(self):
        """
        V.make_render_window_interactor() -> RenderWindowInteractor
        C++: virtual RenderWindowInteractor *MakeRenderWindowInteractor(
            )
        Create an interactor to control renderers in this window. We need
        to know what type of interactor to create, because we might be in
        X Windows or MS Windows.
        """
        ret = wrap_vtk(self._vtk_obj.MakeRenderWindowInteractor())
        return ret
        

    def release_rgba_pixel_data(self, *args):
        """
        V.release_rgba_pixel_data([float, ...])
        C++: virtual void ReleaseRGBAPixelData(float *data)
        Same as get/_set_pixel_data except that the image also contains an
        alpha component. The image is transmitted as RGBARGBARGBA... each
        of which is a float value. The "blend" parameter controls whether
        the set_rgba_pixel_data method blends the data with the previous
        contents of the frame buffer or completely replaces the frame
        buffer data.
        """
        ret = self._wrap_call(self._vtk_obj.ReleaseRGBAPixelData, *args)
        return ret

    def remove_renderer(self, *args):
        """
        V.remove_renderer(Renderer)
        C++: void RemoveRenderer(Renderer *)
        Remove a renderer from the list of renderers.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveRenderer, *my_args)
        return ret

    def report_capabilities(self):
        """
        V.report_capabilities() -> string
        C++: virtual const char *ReportCapabilities()
        Get report of capabilities for the render window
        """
        ret = self._vtk_obj.ReportCapabilities()
        return ret
        

    def set_cursor_position(self, *args):
        """
        V.set_cursor_position(int, int)
        C++: virtual void SetCursorPosition(int, int)
        Hide or Show the mouse cursor, it is nice to be able to hide the
        default cursor if you want VTK to display a 3d cursor instead.
        Set cursor position in window (note that (0,0) is the lower left
        corner).
        """
        ret = self._wrap_call(self._vtk_obj.SetCursorPosition, *args)
        return ret

    def set_force_make_current(self):
        """
        V.set_force_make_current()
        C++: virtual void SetForceMakeCurrent()
        If called, allow make_current() to skip cache-check when called.
        make_current() reverts to original behavior of cache-checking on
        the next render.
        """
        ret = self._vtk_obj.SetForceMakeCurrent()
        return ret
        

    def set_next_window_id(self, *args):
        """
        V.set_next_window_id(void)
        C++: virtual void SetNextWindowId(void *)
        Dummy stubs for Window API.
        """
        ret = self._wrap_call(self._vtk_obj.SetNextWindowId, *args)
        return ret

    def set_next_window_info(self, *args):
        """
        V.set_next_window_info(string)
        C++: virtual void SetNextWindowInfo(char *)
        Dummy stubs for Window API.
        """
        ret = self._wrap_call(self._vtk_obj.SetNextWindowInfo, *args)
        return ret

    def show_cursor(self):
        """
        V.show_cursor()
        C++: virtual void ShowCursor()
        Hide or Show the mouse cursor, it is nice to be able to hide the
        default cursor if you want VTK to display a 3d cursor instead.
        Set cursor position in window (note that (0,0) is the lower left
        corner).
        """
        ret = self._vtk_obj.ShowCursor()
        return ret
        

    def start(self):
        """
        V.start()
        C++: virtual void Start()
        Initialize the rendering process.
        """
        ret = self._vtk_obj.Start()
        return ret
        

    def stereo_midpoint(self):
        """
        V.stereo_midpoint()
        C++: virtual void StereoMidpoint()
        Intermediate method performs operations required between the
        rendering of the left and right eye.
        """
        ret = self._vtk_obj.StereoMidpoint()
        return ret
        

    def stereo_render_complete(self):
        """
        V.stereo_render_complete()
        C++: virtual void StereoRenderComplete()
        Handles work required once both views have been rendered when
        using stereo rendering.
        """
        ret = self._vtk_obj.StereoRenderComplete()
        return ret
        

    def stereo_update(self):
        """
        V.stereo_update()
        C++: virtual void StereoUpdate()
        Update the system, if needed, due to stereo rendering. For some
        stereo methods, subclasses might need to switch some hardware
        settings here.
        """
        ret = self._vtk_obj.StereoUpdate()
        return ret
        

    def supports_open_gl(self):
        """
        V.supports_open_gl() -> int
        C++: virtual int SupportsOpenGL()
        Does this render window support open_gl? 0-false, 1-true
        """
        ret = self._vtk_obj.SupportsOpenGL()
        return ret
        

    def wait_for_completion(self):
        """
        V.wait_for_completion()
        C++: virtual void WaitForCompletion()
        Block the thread until the actual rendering is finished(). Useful
        for measurement only.
        """
        ret = self._vtk_obj.WaitForCompletion()
        return ret
        

    def window_remap(self):
        """
        V.window_remap()
        C++: virtual void WindowRemap()
        Remap the rendering window. This probably only works on UNIX
        right now. It is useful for changing properties that can't
        normally be changed once the window is up.
        """
        ret = self._vtk_obj.WindowRemap()
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
    ('stereo_type', 'GetStereoType'), ('aa_frames', 'GetAAFrames'),
    ('abort_render', 'GetAbortRender'), ('alpha_bit_planes',
    'GetAlphaBitPlanes'), ('anaglyph_color_mask', 'GetAnaglyphColorMask'),
    ('anaglyph_color_saturation', 'GetAnaglyphColorSaturation'),
    ('current_cursor', 'GetCurrentCursor'), ('desired_update_rate',
    'GetDesiredUpdateRate'), ('device_index', 'GetDeviceIndex'),
    ('fd_frames', 'GetFDFrames'), ('in_abort_check', 'GetInAbortCheck'),
    ('multi_samples', 'GetMultiSamples'), ('number_of_layers',
    'GetNumberOfLayers'), ('sub_frames', 'GetSubFrames'),
    ('use_constant_fd_offsets', 'GetUseConstantFDOffsets'),
    ('use_off_screen_buffers', 'GetUseOffScreenBuffers'), ('dpi',
    'GetDPI'), ('position', 'GetPosition'), ('size', 'GetSize'),
    ('tile_scale', 'GetTileScale'), ('tile_viewport', 'GetTileViewport'),
    ('window_name', 'GetWindowName'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['borders', 'debug', 'double_buffer', 'erase', 'full_screen',
    'global_warning_display', 'is_picking', 'line_smoothing', 'mapped',
    'off_screen_rendering', 'point_smoothing', 'polygon_smoothing',
    'stencil_capable', 'stereo_capable_window', 'stereo_render',
    'swap_buffers', 'stereo_type', 'aa_frames', 'abort_render',
    'alpha_bit_planes', 'anaglyph_color_mask',
    'anaglyph_color_saturation', 'current_cursor', 'desired_update_rate',
    'device_index', 'dpi', 'fd_frames', 'in_abort_check', 'multi_samples',
    'number_of_layers', 'position', 'size', 'sub_frames', 'tile_scale',
    'tile_viewport', 'use_constant_fd_offsets', 'use_off_screen_buffers',
    'window_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderWindow, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderWindow properties', scrollable=True, resizable=True,
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
            'anaglyph_color_mask', 'anaglyph_color_saturation', 'current_cursor',
            'desired_update_rate', 'device_index', 'dpi', 'fd_frames',
            'in_abort_check', 'multi_samples', 'number_of_layers', 'position',
            'size', 'sub_frames', 'tile_scale', 'tile_viewport',
            'use_constant_fd_offsets', 'use_off_screen_buffers', 'window_name']),
            title='Edit RenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


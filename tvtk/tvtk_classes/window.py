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

from tvtk.tvtk_classes.object import Object


class Window(Object):
    """
    Window - window superclass for RenderWindow
    
    Superclass: Object
    
    Window is an abstract object to specify the behavior of a
    rendering window.  It contains Viewports.
    
    @sa
    RenderWindow Viewport
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWindow, obj, update, **traits)
    
    double_buffer = tvtk_base.true_bool_trait(help=\
        """
        Keep track of whether double buffering is on or off
        """
    )

    def _double_buffer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDoubleBuffer,
                        self.double_buffer_)

    erase = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off erasing the screen between images. This allows
        multiple exposure sequences if turned on. You will need to turn
        double buffering off or make use of the swap_buffers methods to
        prevent you from swapping buffers between exposures.
        """
    )

    def _erase_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetErase,
                        self.erase_)

    mapped = tvtk_base.false_bool_trait(help=\
        """
        Keep track of whether the rendering window has been mapped to
        screen.
        """
    )

    def _mapped_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMapped,
                        self.mapped_)

    off_screen_rendering = tvtk_base.false_bool_trait(help=\
        """
        Create a window in memory instead of on the screen. This may not
        be supported for every type of window and on some windows you may
        need to invoke this prior to the first render.
        """
    )

    def _off_screen_rendering_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffScreenRendering,
                        self.off_screen_rendering_)

    dpi = traits.Trait(72, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Return a best estimate to the dots per inch of the display device
        being rendered (or printed).
        """
    )

    def _dpi_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDPI,
                        self.dpi)

    position = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        Set/Get the position in screen coordinates of the rendering
        window.
        """
    )

    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        Set/Get the size of the window in screen coordinates in pixels.
        """
    )

    def _size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSize,
                        self.size)

    tile_scale = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(1, 1), cols=2, help=\
        """
        
        """
    )

    def _tile_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTileScale,
                        self.tile_scale)

    tile_viewport = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, 0.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _tile_viewport_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTileViewport,
                        self.tile_viewport)

    window_name = traits.String('Visualization Toolkit - OpenGL', enter_set=True, auto_set=False, help=\
        """
        Get name of rendering window
        """
    )

    def _window_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWindowName,
                        self.window_name)

    def _get_actual_size(self):
        return self._vtk_obj.GetActualSize()
    actual_size = traits.Property(_get_actual_size, help=\
        """
        get_size() returns the size * this->_tile_scale, whereas this method
        returns the size without multiplying with the tile scale.
        """
    )

    def _get_generic_context(self):
        return self._vtk_obj.GetGenericContext()
    generic_context = traits.Property(_get_generic_context, help=\
        """
        These are window system independent methods that are used to help
        interface Window to native windowing systems.
        """
    )

    def _get_generic_display_id(self):
        return self._vtk_obj.GetGenericDisplayId()
    generic_display_id = traits.Property(_get_generic_display_id, help=\
        """
        These are window system independent methods that are used to help
        interface Window to native windowing systems.
        """
    )

    def _get_generic_drawable(self):
        return self._vtk_obj.GetGenericDrawable()
    generic_drawable = traits.Property(_get_generic_drawable, help=\
        """
        These are window system independent methods that are used to help
        interface Window to native windowing systems.
        """
    )

    def _get_generic_parent_id(self):
        return self._vtk_obj.GetGenericParentId()
    generic_parent_id = traits.Property(_get_generic_parent_id, help=\
        """
        These are window system independent methods that are used to help
        interface Window to native windowing systems.
        """
    )

    def _get_generic_window_id(self):
        return self._vtk_obj.GetGenericWindowId()
    generic_window_id = traits.Property(_get_generic_window_id, help=\
        """
        These are window system independent methods that are used to help
        interface Window to native windowing systems.
        """
    )

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

    def _get_screen_size(self):
        return self._vtk_obj.GetScreenSize()
    screen_size = traits.Property(_get_screen_size, help=\
        """
        Get the current size of the screen in pixels.
        """
    )

    def detect_dpi(self):
        """
        V.detect_dpi() -> bool
        C++: virtual bool DetectDPI()
        Attempt to detect and set the DPI of the display device by
        querying the system. Note that this is not supported on all
        backends, and this method will return false if the DPI could not
        be detected. Use get_dpi() to inspect the detected value.
        """
        ret = self._vtk_obj.DetectDPI()
        return ret
        

    def make_current(self):
        """
        V.make_current()
        C++: virtual void MakeCurrent()
        Make the window current. May be overridden in subclasses to do
        for example a gl_x_make_current or a wgl_make_current.
        """
        ret = self._vtk_obj.MakeCurrent()
        return ret
        

    def render(self):
        """
        V.render()
        C++: virtual void Render()
        Ask each viewport owned by this Window to render its image and
        synchronize this process.
        """
        ret = self._vtk_obj.Render()
        return ret
        

    def set_display_id(self, *args):
        """
        V.set_display_id(void)
        C++: virtual void SetDisplayId(void *)
        These are window system independent methods that are used to help
        interface Window to native windowing systems.
        """
        ret = self._wrap_call(self._vtk_obj.SetDisplayId, *args)
        return ret

    def set_parent_id(self, *args):
        """
        V.set_parent_id(void)
        C++: virtual void SetParentId(void *)
        These are window system independent methods that are used to help
        interface Window to native windowing systems.
        """
        ret = self._wrap_call(self._vtk_obj.SetParentId, *args)
        return ret

    def set_parent_info(self, *args):
        """
        V.set_parent_info(string)
        C++: virtual void SetParentInfo(char *)
        These are window system independent methods that are used to help
        interface Window to native windowing systems.
        """
        ret = self._wrap_call(self._vtk_obj.SetParentInfo, *args)
        return ret

    def set_window_id(self, *args):
        """
        V.set_window_id(void)
        C++: virtual void SetWindowId(void *)
        These are window system independent methods that are used to help
        interface Window to native windowing systems.
        """
        ret = self._wrap_call(self._vtk_obj.SetWindowId, *args)
        return ret

    def set_window_info(self, *args):
        """
        V.set_window_info(string)
        C++: virtual void SetWindowInfo(char *)
        These are window system independent methods that are used to help
        interface Window to native windowing systems.
        """
        ret = self._wrap_call(self._vtk_obj.SetWindowInfo, *args)
        return ret

    _updateable_traits_ = \
    (('double_buffer', 'GetDoubleBuffer'), ('erase', 'GetErase'),
    ('mapped', 'GetMapped'), ('off_screen_rendering',
    'GetOffScreenRendering'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('dpi',
    'GetDPI'), ('position', 'GetPosition'), ('size', 'GetSize'),
    ('tile_scale', 'GetTileScale'), ('tile_viewport', 'GetTileViewport'),
    ('window_name', 'GetWindowName'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'double_buffer', 'erase', 'global_warning_display',
    'mapped', 'off_screen_rendering', 'dpi', 'position', 'size',
    'tile_scale', 'tile_viewport', 'window_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Window, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Window properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['double_buffer', 'erase', 'mapped', 'off_screen_rendering'],
            [], ['dpi', 'position', 'size', 'tile_scale', 'tile_viewport',
            'window_name']),
            title='Edit Window properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Window properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


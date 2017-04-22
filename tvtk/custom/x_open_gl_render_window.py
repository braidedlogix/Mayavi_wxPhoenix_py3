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

from tvtk.tvtk_classes.open_gl_render_window import OpenGLRenderWindow


class XOpenGLRenderWindow(OpenGLRenderWindow):
    """
    XOpenGLRenderWindow - open_gl rendering window
    
    Superclass: OpenGLRenderWindow
    
    XOpenGLRenderWindow is a concrete implementation of the abstract
    class RenderWindow. OpenGLRenderer interfaces to the open_gl
    graphics library. Application programmers should normally use
    RenderWindow instead of the open_gl specific version.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXOpenGLRenderWindow, obj, update, **traits)
    
    current_cursor = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Change the shape of the cursor
        """
    )

    def _current_cursor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCurrentCursor,
                        self.current_cursor)

    position = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        Move the window to a new position on the display.
        """
    )

    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        Specify the size of the rendering window in pixels.
        """
    )

    def _size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSize,
                        self.size)

    window_name = traits.String('Visualization Toolkit - OpenGL', enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _window_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWindowName,
                        self.window_name)

    def _get_desired_depth(self):
        return self._vtk_obj.GetDesiredDepth()
    desired_depth = traits.Property(_get_desired_depth, help=\
        """
        Get the X properties of an ideal rendering window.
        """
    )

    def pref_full_screen(self):
        """
        V.pref_full_screen()
        C++: virtual void PrefFullScreen(void)
        Set the preferred window size to full screen.
        """
        ret = self._vtk_obj.PrefFullScreen()
        return ret
        

    def window_initialize(self):
        """
        V.window_initialize()
        C++: virtual void WindowInitialize(void)
        Initialize the window for rendering.
        """
        ret = self._vtk_obj.WindowInitialize()
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
    ('stereo_type', 'GetStereoType'), ('current_cursor',
    'GetCurrentCursor'), ('position', 'GetPosition'), ('size', 'GetSize'),
    ('window_name', 'GetWindowName'), ('context_supports_open_gl32',
    'GetContextSupportsOpenGL32'),
    ('global_maximum_number_of_multi_samples',
    'GetGlobalMaximumNumberOfMultiSamples'), ('use_off_screen_buffers',
    'GetUseOffScreenBuffers'), ('aa_frames', 'GetAAFrames'),
    ('abort_render', 'GetAbortRender'), ('alpha_bit_planes',
    'GetAlphaBitPlanes'), ('anaglyph_color_mask', 'GetAnaglyphColorMask'),
    ('anaglyph_color_saturation', 'GetAnaglyphColorSaturation'),
    ('desired_update_rate', 'GetDesiredUpdateRate'), ('device_index',
    'GetDeviceIndex'), ('fd_frames', 'GetFDFrames'), ('in_abort_check',
    'GetInAbortCheck'), ('multi_samples', 'GetMultiSamples'),
    ('number_of_layers', 'GetNumberOfLayers'), ('sub_frames',
    'GetSubFrames'), ('use_constant_fd_offsets',
    'GetUseConstantFDOffsets'), ('dpi', 'GetDPI'), ('tile_scale',
    'GetTileScale'), ('tile_viewport', 'GetTileViewport'),
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
            return super(XOpenGLRenderWindow, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit XOpenGLRenderWindow properties', scrollable=True, resizable=True,
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
            title='Edit XOpenGLRenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XOpenGLRenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


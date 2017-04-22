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


class GenericOpenGLRenderWindow(OpenGLRenderWindow):
    """
    GenericOpenGLRenderWindow - platform independent render window
    
    Superclass: OpenGLRenderWindow
    
    GenericOpenGLRenderWindow provides a skeleton for implementing a
    render window using one's own open_gl context and drawable. To be
    effective, one must register an observer for window_make_current_event,
    window_is_current_event and window_frame_event.  When this class sends a
    window_is_current_event, the call data is an bool* which one can use to
    return whether the context is current.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericOpenGLRenderWindow, obj, update, **traits)
    
    back_buffer = traits.Int(1029, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _back_buffer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackBuffer,
                        self.back_buffer)

    back_left_buffer = traits.Int(1026, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _back_left_buffer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackLeftBuffer,
                        self.back_left_buffer)

    back_right_buffer = traits.Int(1027, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _back_right_buffer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackRightBuffer,
                        self.back_right_buffer)

    front_buffer = traits.Int(1028, enter_set=True, auto_set=False, help=\
        """
        set the drawing buffers to use
        """
    )

    def _front_buffer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrontBuffer,
                        self.front_buffer)

    front_left_buffer = traits.Int(1024, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _front_left_buffer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrontLeftBuffer,
                        self.front_left_buffer)

    front_right_buffer = traits.Int(1025, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _front_right_buffer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrontRightBuffer,
                        self.front_right_buffer)

    def create_a_window(self):
        """
        V.create_a_window()
        C++: void CreateAWindow()"""
        ret = self._vtk_obj.CreateAWindow()
        return ret
        

    def destroy_window(self):
        """
        V.destroy_window()
        C++: void DestroyWindow()"""
        ret = self._vtk_obj.DestroyWindow()
        return ret
        

    def pop_state(self):
        """
        V.pop_state()
        C++: void PopState()
        no-op (for API compat with open_gl1).
        """
        ret = self._vtk_obj.PopState()
        return ret
        

    def push_state(self):
        """
        V.push_state()
        C++: void PushState()
        no-op (for API compat with open_gl1).
        """
        ret = self._vtk_obj.PushState()
        return ret
        

    def set_is_current(self, *args):
        """
        V.set_is_current(bool)
        C++: void SetIsCurrent(bool newValue)
        Allow to update state within observer callback without changing
        data argument and MTime.
        """
        ret = self._wrap_call(self._vtk_obj.SetIsCurrent, *args)
        return ret

    def set_is_direct(self, *args):
        """
        V.set_is_direct(int)
        C++: void SetIsDirect(int newValue)
        Allow to update state within observer callback without changing
        data argument and MTime.
        """
        ret = self._wrap_call(self._vtk_obj.SetIsDirect, *args)
        return ret

    def set_supports_open_gl(self, *args):
        """
        V.set_supports_open_gl(int)
        C++: void SetSupportsOpenGL(int newValue)
        Allow to update state within observer callback without changing
        data argument and MTime.
        """
        ret = self._wrap_call(self._vtk_obj.SetSupportsOpenGL, *args)
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
    ('stereo_type', 'GetStereoType'), ('back_buffer', 'GetBackBuffer'),
    ('back_left_buffer', 'GetBackLeftBuffer'), ('back_right_buffer',
    'GetBackRightBuffer'), ('front_buffer', 'GetFrontBuffer'),
    ('front_left_buffer', 'GetFrontLeftBuffer'), ('front_right_buffer',
    'GetFrontRightBuffer'), ('context_supports_open_gl32',
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
    'anaglyph_color_saturation', 'back_buffer', 'back_left_buffer',
    'back_right_buffer', 'context_supports_open_gl32', 'current_cursor',
    'desired_update_rate', 'device_index', 'dpi', 'fd_frames',
    'front_buffer', 'front_left_buffer', 'front_right_buffer',
    'global_maximum_number_of_multi_samples', 'in_abort_check',
    'multi_samples', 'number_of_layers', 'position', 'size', 'sub_frames',
    'tile_scale', 'tile_viewport', 'use_constant_fd_offsets',
    'use_off_screen_buffers', 'window_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericOpenGLRenderWindow, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericOpenGLRenderWindow properties', scrollable=True, resizable=True,
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
            'anaglyph_color_mask', 'anaglyph_color_saturation', 'back_buffer',
            'back_left_buffer', 'back_right_buffer', 'context_supports_open_gl32',
            'current_cursor', 'desired_update_rate', 'device_index', 'dpi',
            'fd_frames', 'front_buffer', 'front_left_buffer',
            'front_right_buffer', 'global_maximum_number_of_multi_samples',
            'in_abort_check', 'multi_samples', 'number_of_layers', 'position',
            'size', 'sub_frames', 'tile_scale', 'tile_viewport',
            'use_constant_fd_offsets', 'use_off_screen_buffers', 'window_name']),
            title='Edit GenericOpenGLRenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericOpenGLRenderWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.context_device2d import ContextDevice2D


class OpenGLContextDevice2D(ContextDevice2D):
    """
    OpenGLContextDevice2D - Class for drawing 2d primitives using
    open_gl 1.1+.
    
    Superclass: ContextDevice2D
    
    This class takes care of drawing the 2d primitives for the
    Context2D class. In general this class should not be used
    directly, but called by Context2D which takes care of many of the
    higher level details.
    
    @sa
    OpenGL2ContextDevice2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLContextDevice2D, obj, update, **traits)
    
    def get_matrix(self, *args):
        """
        V.get_matrix(Matrix3x3)
        C++: virtual void GetMatrix(Matrix3x3 *m)
        Set the model view matrix for the display
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetMatrix, *my_args)
        return ret

    def set_matrix(self, *args):
        """
        V.set_matrix(Matrix3x3)
        C++: virtual void SetMatrix(Matrix3x3 *m)
        Set the model view matrix for the display
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetMatrix, *my_args)
        return ret

    maximum_marker_cache_size = traits.Int(20, enter_set=True, auto_set=False, help=\
        """
        Adjust the size of the marker_cache. This implementation generates
        point sprites for each mark size/shape and uses draw_point_sprites
        to render them. The number of cached markers can be accessed with
        this function.
        """
    )

    def _maximum_marker_cache_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumMarkerCacheSize,
                        self.maximum_marker_cache_size)

    def _get_model_matrix(self):
        return wrap_vtk(self._vtk_obj.GetModelMatrix())
    model_matrix = traits.Property(_get_model_matrix, help=\
        """
        Get the projection matrix this is needed
        """
    )

    def _get_projection_matrix(self):
        return wrap_vtk(self._vtk_obj.GetProjectionMatrix())
    projection_matrix = traits.Property(_get_projection_matrix, help=\
        """
        Get the projection matrix this is needed
        """
    )

    def _get_render_window(self):
        return wrap_vtk(self._vtk_obj.GetRenderWindow())
    render_window = traits.Property(_get_render_window, help=\
        """
        Get the active render_window of the device. Will return null if
        not active.
        """
    )

    def has_glsl(self):
        """
        V.has_glsl() -> bool
        C++: bool HasGLSL()
        Check whether the current context device has support for GLSL.
        """
        ret = self._vtk_obj.HasGLSL()
        return ret
        

    def release_graphics_resources(self, *args):
        """
        V.release_graphics_resources(Window)
        C++: virtual void ReleaseGraphicsResources(Window *window)
        Release any graphics resources that are being consumed by this
        device. The parameter window could be used to determine which
        graphic resources to release.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReleaseGraphicsResources, *my_args)
        return ret

    def set_color(self, *args):
        """
        V.set_color([int, int, int])
        C++: virtual void SetColor(unsigned char color[3])
        Set the color for the device using unsigned char of length 3,
        RGB.
        """
        ret = self._wrap_call(self._vtk_obj.SetColor, *args)
        return ret

    def set_string_renderer_to_free_type(self):
        """
        V.set_string_renderer_to_free_type() -> bool
        C++: bool SetStringRendererToFreeType()
        Force the use of the freetype based render strategy. If Qt is
        available then freetype will be used preferentially, otherwise
        this has no effect. Returns true on success.
        """
        ret = self._vtk_obj.SetStringRendererToFreeType()
        return ret
        

    def set_string_renderer_to_qt(self):
        """
        V.set_string_renderer_to_qt() -> bool
        C++: bool SetStringRendererToQt()
        Force the use of the Qt based string render strategy. If Qt is
        not available then freetype will be used and this will return
        false.
        """
        ret = self._vtk_obj.SetStringRendererToQt()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('maximum_marker_cache_size',
    'GetMaximumMarkerCacheSize'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'maximum_marker_cache_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLContextDevice2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLContextDevice2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['maximum_marker_cache_size']),
            title='Edit OpenGLContextDevice2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLContextDevice2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


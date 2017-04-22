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


class OpenGLShaderCache(Object):
    """
    OpenGLShaderCache - manage Shader Programs within a context
    
    Superclass: Object
    
    OpenGLShaderCache manages shader program compilation and binding
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLShaderCache, obj, update, **traits)
    
    def _get_last_shader_bound(self):
        return wrap_vtk(self._vtk_obj.GetLastShaderBound())
    last_shader_bound = traits.Property(_get_last_shader_bound, help=\
        """
        
        """
    )

    def clear_last_shader_bound(self):
        """
        V.clear_last_shader_bound()
        C++: virtual void ClearLastShaderBound()
        Get/Clear the last Shader bound, called by shaders as they
        release their graphics resources
        """
        ret = self._vtk_obj.ClearLastShaderBound()
        return ret
        

    def ready_shader_program(self, *args):
        """
        V.ready_shader_program(string, string, string, TransformFeedback)
             -> ShaderProgram
        C++: virtual ShaderProgram *ReadyShaderProgram(
            const char *vertexCode, const char *fragmentCode,
            const char *geometryCode, TransformFeedback *cap=NULL)
        V.ready_shader_program(ShaderProgram, TransformFeedback)
            -> ShaderProgram
        C++: virtual ShaderProgram *ReadyShaderProgram(
            ShaderProgram *shader, TransformFeedback *cap=NULL)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReadyShaderProgram, *my_args)
        return wrap_vtk(ret)

    def release_current_shader(self):
        """
        V.release_current_shader()
        C++: void ReleaseCurrentShader()
        Release the current shader.  Basically go back to having no
        shaders loaded.  This is useful for old legacy code that relies
        on no shaders being loaded.
        """
        ret = self._vtk_obj.ReleaseCurrentShader()
        return ret
        

    def release_graphics_resources(self, *args):
        """
        V.release_graphics_resources(Window)
        C++: virtual void ReleaseGraphicsResources(Window *win)
        Free up any resources being used by the provided shader
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReleaseGraphicsResources, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLShaderCache, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLShaderCache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit OpenGLShaderCache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLShaderCache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


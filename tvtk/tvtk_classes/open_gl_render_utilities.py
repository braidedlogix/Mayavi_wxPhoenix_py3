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


class OpenGLRenderUtilities(Object):
    """
    OpenGLRenderUtilities - open_gl rendering utility functions
    
    Superclass: Object
    
    OpenGLRenderUtilities provides functions to help render
    primitives.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLRenderUtilities, obj, update, **traits)
    
    def _get_full_screen_quad_fragment_shader_template(self):
        return self._vtk_obj.GetFullScreenQuadFragmentShaderTemplate()
    full_screen_quad_fragment_shader_template = traits.Property(_get_full_screen_quad_fragment_shader_template, help=\
        """
        Draw a full-screen quad:
        * vertex_shader and geometry_shader should be used as-is when
          building the shader_program.
        * fragment_shader_template supports the replacements
          //VTK::FSQ::Decl and //VTK::FSQ::Impl for declaring variables
          and the shader body, respectively.
        * The varying tex_coord is available to the fragment shader for
          texture lookups into full-screen textures, ie.
          texture_2d(texture_name, tex_coord).
        * prep_full_screen_vao initializes a new VAO for drawing a quad.
        * draw_full_screen_quad actually draws the quad.
        
        * Example usage:
        * * typedef OpenGLRenderUtilities GLUtil;
        
        * // Prep fragment shader source:
        * std::string frag_shader =
          gl_util::_get_full_screen_quad_fragment_shader_template();
        * ShaderProgram::Substitute(fragShader, "//VTK::FSQ::Decl",
        * "uniform sampler_2d a_texture;");
        * ShaderProgram::Substitute(fragShader, "//VTK::FSQ::Impl",
        * "gl__frag_data[_0] = texture_2d(a_texture, tex_coord);");
        
        * // Create shader program:
        * ShaderProgram *prog = shader_cache->_ready_shader_program(
        * gl_util::_get_full_screen_quad_vertex_shader().c_str(),
        * frag_shader.c_str(),
        * gl_util::_get_full_screen_quad_geometry_shader().c_str());
        
        * // Initialize new VAO/vertex buffer. This is only done once:
        * Newverts;
        * Newvao;
        * gl_util::_prep_full_screen_vao(verts._get(), vao.Get(), prog);
        
        * // Setup shader program to sample TextureObject a_texture:
        * a_texture->_activate();
        * prog->_set_uniformi("a_texture", a_texture->_get_texture_unit());
        
        * // Render the full-screen quad:
        * vao->Bind();
        * gl_util::_draw_full_screen_quad();
        * vao->Release();
        * a_texture->_deactivate();
        * 
        """
    )

    def _get_full_screen_quad_geometry_shader(self):
        return self._vtk_obj.GetFullScreenQuadGeometryShader()
    full_screen_quad_geometry_shader = traits.Property(_get_full_screen_quad_geometry_shader, help=\
        """
        Draw a full-screen quad:
        * vertex_shader and geometry_shader should be used as-is when
          building the shader_program.
        * fragment_shader_template supports the replacements
          //VTK::FSQ::Decl and //VTK::FSQ::Impl for declaring variables
          and the shader body, respectively.
        * The varying tex_coord is available to the fragment shader for
          texture lookups into full-screen textures, ie.
          texture_2d(texture_name, tex_coord).
        * prep_full_screen_vao initializes a new VAO for drawing a quad.
        * draw_full_screen_quad actually draws the quad.
        
        * Example usage:
        * * typedef OpenGLRenderUtilities GLUtil;
        
        * // Prep fragment shader source:
        * std::string frag_shader =
          gl_util::_get_full_screen_quad_fragment_shader_template();
        * ShaderProgram::Substitute(fragShader, "//VTK::FSQ::Decl",
        * "uniform sampler_2d a_texture;");
        * ShaderProgram::Substitute(fragShader, "//VTK::FSQ::Impl",
        * "gl__frag_data[_0] = texture_2d(a_texture, tex_coord);");
        
        * // Create shader program:
        * ShaderProgram *prog = shader_cache->_ready_shader_program(
        * gl_util::_get_full_screen_quad_vertex_shader().c_str(),
        * frag_shader.c_str(),
        * gl_util::_get_full_screen_quad_geometry_shader().c_str());
        
        * // Initialize new VAO/vertex buffer. This is only done once:
        * Newverts;
        * Newvao;
        * gl_util::_prep_full_screen_vao(verts._get(), vao.Get(), prog);
        
        * // Setup shader program to sample TextureObject a_texture:
        * a_texture->_activate();
        * prog->_set_uniformi("a_texture", a_texture->_get_texture_unit());
        
        * // Render the full-screen quad:
        * vao->Bind();
        * gl_util::_draw_full_screen_quad();
        * vao->Release();
        * a_texture->_deactivate();
        * 
        """
    )

    def _get_full_screen_quad_vertex_shader(self):
        return self._vtk_obj.GetFullScreenQuadVertexShader()
    full_screen_quad_vertex_shader = traits.Property(_get_full_screen_quad_vertex_shader, help=\
        """
        Draw a full-screen quad:
        * vertex_shader and geometry_shader should be used as-is when
          building the shader_program.
        * fragment_shader_template supports the replacements
          //VTK::FSQ::Decl and //VTK::FSQ::Impl for declaring variables
          and the shader body, respectively.
        * The varying tex_coord is available to the fragment shader for
          texture lookups into full-screen textures, ie.
          texture_2d(texture_name, tex_coord).
        * prep_full_screen_vao initializes a new VAO for drawing a quad.
        * draw_full_screen_quad actually draws the quad.
        
        * Example usage:
        * * typedef OpenGLRenderUtilities GLUtil;
        
        * // Prep fragment shader source:
        * std::string frag_shader =
          gl_util::_get_full_screen_quad_fragment_shader_template();
        * ShaderProgram::Substitute(fragShader, "//VTK::FSQ::Decl",
        * "uniform sampler_2d a_texture;");
        * ShaderProgram::Substitute(fragShader, "//VTK::FSQ::Impl",
        * "gl__frag_data[_0] = texture_2d(a_texture, tex_coord);");
        
        * // Create shader program:
        * ShaderProgram *prog = shader_cache->_ready_shader_program(
        * gl_util::_get_full_screen_quad_vertex_shader().c_str(),
        * frag_shader.c_str(),
        * gl_util::_get_full_screen_quad_geometry_shader().c_str());
        
        * // Initialize new VAO/vertex buffer. This is only done once:
        * Newverts;
        * Newvao;
        * gl_util::_prep_full_screen_vao(verts._get(), vao.Get(), prog);
        
        * // Setup shader program to sample TextureObject a_texture:
        * a_texture->_activate();
        * prog->_set_uniformi("a_texture", a_texture->_get_texture_unit());
        
        * // Render the full-screen quad:
        * vao->Bind();
        * gl_util::_draw_full_screen_quad();
        * vao->Release();
        * a_texture->_deactivate();
        * 
        """
    )

    def draw_full_screen_quad(self):
        """
        V.draw_full_screen_quad()
        C++: static void DrawFullScreenQuad()
        Draw a full-screen quad:
        * vertex_shader and geometry_shader should be used as-is when
          building the shader_program.
        * fragment_shader_template supports the replacements
          //VTK::FSQ::Decl and //VTK::FSQ::Impl for declaring variables
          and the shader body, respectively.
        * The varying tex_coord is available to the fragment shader for
          texture lookups into full-screen textures, ie.
          texture_2d(texture_name, tex_coord).
        * prep_full_screen_vao initializes a new VAO for drawing a quad.
        * draw_full_screen_quad actually draws the quad.
        
        * Example usage:
        * * typedef OpenGLRenderUtilities GLUtil;
        
        * // Prep fragment shader source:
        * std::string frag_shader =
          gl_util::_get_full_screen_quad_fragment_shader_template();
        * ShaderProgram::Substitute(fragShader, "//VTK::FSQ::Decl",
        * "uniform sampler_2d a_texture;");
        * ShaderProgram::Substitute(fragShader, "//VTK::FSQ::Impl",
        * "gl__frag_data[_0] = texture_2d(a_texture, tex_coord);");
        
        * // Create shader program:
        * ShaderProgram *prog = shader_cache->_ready_shader_program(
        * gl_util::_get_full_screen_quad_vertex_shader().c_str(),
        * frag_shader.c_str(),
        * gl_util::_get_full_screen_quad_geometry_shader().c_str());
        
        * // Initialize new VAO/vertex buffer. This is only done once:
        * Newverts;
        * Newvao;
        * gl_util::_prep_full_screen_vao(verts._get(), vao.Get(), prog);
        
        * // Setup shader program to sample TextureObject a_texture:
        * a_texture->_activate();
        * prog->_set_uniformi("a_texture", a_texture->_get_texture_unit());
        
        * // Render the full-screen quad:
        * vao->Bind();
        * gl_util::_draw_full_screen_quad();
        * vao->Release();
        * a_texture->_deactivate();
        * 
        """
        ret = self._vtk_obj.DrawFullScreenQuad()
        return ret
        

    def prep_full_screen_vao(self, *args):
        """
        V.prep_full_screen_vao(OpenGLBufferObject,
            OpenGLVertexArrayObject, ShaderProgram) -> bool
        C++: static bool PrepFullScreenVAO(OpenGLBufferObject *verts,
            OpenGLVertexArrayObject *vao, ShaderProgram *prog)
        Draw a full-screen quad:
        * vertex_shader and geometry_shader should be used as-is when
          building the shader_program.
        * fragment_shader_template supports the replacements
          //VTK::FSQ::Decl and //VTK::FSQ::Impl for declaring variables
          and the shader body, respectively.
        * The varying tex_coord is available to the fragment shader for
          texture lookups into full-screen textures, ie.
          texture_2d(texture_name, tex_coord).
        * prep_full_screen_vao initializes a new VAO for drawing a quad.
        * draw_full_screen_quad actually draws the quad.
        
        * Example usage:
        * * typedef OpenGLRenderUtilities GLUtil;
        
        * // Prep fragment shader source:
        * std::string frag_shader =
          gl_util::_get_full_screen_quad_fragment_shader_template();
        * ShaderProgram::Substitute(fragShader, "//VTK::FSQ::Decl",
        * "uniform sampler_2d a_texture;");
        * ShaderProgram::Substitute(fragShader, "//VTK::FSQ::Impl",
        * "gl__frag_data[_0] = texture_2d(a_texture, tex_coord);");
        
        * // Create shader program:
        * ShaderProgram *prog = shader_cache->_ready_shader_program(
        * gl_util::_get_full_screen_quad_vertex_shader().c_str(),
        * frag_shader.c_str(),
        * gl_util::_get_full_screen_quad_geometry_shader().c_str());
        
        * // Initialize new VAO/vertex buffer. This is only done once:
        * Newverts;
        * Newvao;
        * gl_util::_prep_full_screen_vao(verts._get(), vao.Get(), prog);
        
        * // Setup shader program to sample TextureObject a_texture:
        * a_texture->_activate();
        * prog->_set_uniformi("a_texture", a_texture->_get_texture_unit());
        
        * // Render the full-screen quad:
        * vao->Bind();
        * gl_util::_draw_full_screen_quad();
        * vao->Release();
        * a_texture->_deactivate();
        * 
        """
        my_args = deref_array(args, [('vtkOpenGLBufferObject', 'vtkOpenGLVertexArrayObject', 'vtkShaderProgram')])
        ret = self._wrap_call(self._vtk_obj.PrepFullScreenVAO, *my_args)
        return ret

    def render_quad(self, *args):
        """
        V.render_quad([float, ...], [float, ...], ShaderProgram,
            OpenGLVertexArrayObject)
        C++: static void RenderQuad(float *verts, float *tcoords,
            ShaderProgram *program, OpenGLVertexArrayObject *vao)
        Helper function that draws a quad on the screen at the specified
        vertex coordinates and if tcoords are not NULL with the specified
        texture coordinates.
        """
        my_args = deref_array(args, [('tuple', 'tuple', 'vtkShaderProgram', 'vtkOpenGLVertexArrayObject')])
        ret = self._wrap_call(self._vtk_obj.RenderQuad, *my_args)
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
            return super(OpenGLRenderUtilities, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLRenderUtilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit OpenGLRenderUtilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLRenderUtilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


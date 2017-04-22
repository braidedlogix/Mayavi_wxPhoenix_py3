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

from tvtk.tvtk_classes.render_pass import RenderPass


class OpenGLRenderPass(RenderPass):
    """
    OpenGLRenderPass - Abstract render pass with shader modifications.
    
    Superclass: RenderPass
    
    Allows a render pass to update shader code using a new virtual API.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLRenderPass, obj, update, **traits)
    
    def _get_shader_stage_m_time(self):
        return self._vtk_obj.GetShaderStageMTime()
    shader_stage_m_time = traits.Property(_get_shader_stage_m_time, help=\
        """
        For multi-stage render passes that need to change shader code
        during a single pass, use this method to notify a mapper that the
        shader needs to be rebuilt (rather than reuse the last cached
        shader. This method should return the last time that the shader
        stage changed, or 0 if the shader is single-stage.
        """
    )

    def render_passes(self):
        """
        V.render_passes() -> InformationObjectBaseVectorKey
        C++: static InformationObjectBaseVectorKey *RenderPasses()
        Key containing information about the current pass.
        """
        ret = wrap_vtk(self._vtk_obj.RenderPasses())
        return ret
        

    def replace_shader_values(self, *args):
        """
        V.replace_shader_values(string, string, string, AbstractMapper,
            Prop) -> bool
        C++: virtual bool ReplaceShaderValues(std::string &vertexShader,
            std::string &geometryShader, std::string &fragmentShader,
            AbstractMapper *mapper, Prop *prop)
        Use ShaderProgram::Substitute to replace //VTK::XXX:YYY
        declarations in the shader sources. Return false on error.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReplaceShaderValues, *my_args)
        return ret

    def set_shader_parameters(self, *args):
        """
        V.set_shader_parameters(ShaderProgram, AbstractMapper,
            Prop) -> bool
        C++: virtual bool SetShaderParameters(ShaderProgram *program,
            AbstractMapper *mapper, Prop *prop)
        Update the uniforms of the shader program. Return false on error.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetShaderParameters, *my_args)
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
            return super(OpenGLRenderPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLRenderPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit OpenGLRenderPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLRenderPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


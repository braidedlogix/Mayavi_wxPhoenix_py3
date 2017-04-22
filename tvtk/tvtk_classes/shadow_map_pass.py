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


class ShadowMapPass(RenderPass):
    """
    ShadowMapPass - Implement a shadow mapping render pass.
    
    Superclass: RenderPass
    
    Render the opaque polygonal geometry of a scene with shadow maps (a
    technique to render hard shadows in hardware).
    
    This pass expects an initialized depth buffer and color buffer.
    Initialized buffers means they have been cleared with farest z-value
    and background color/gradient/transparent color. An opaque pass may
    have been performed right after the initialization.
    
    Its delegate is usually set to a OpaquePass.
    
    @par Implementation: The first pass of the algorithm is to generate a
    shadow map per light (depth map from the light point of view) by
    rendering the opaque objects with the OCCLUDER property keys. The
    second pass is to render the opaque objects with the RECEIVER keys.
    
    @sa
    RenderPass, OpaquePass
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkShadowMapPass, obj, update, **traits)
    
    def _get_opaque_sequence(self):
        return wrap_vtk(self._vtk_obj.GetOpaqueSequence())
    def _set_opaque_sequence(self, arg):
        old_val = self._get_opaque_sequence()
        self._wrap_call(self._vtk_obj.SetOpaqueSequence,
                        deref_vtk(arg))
        self.trait_property_changed('opaque_sequence', old_val, arg)
    opaque_sequence = traits.Property(_get_opaque_sequence, _set_opaque_sequence, help=\
        """
        Pass that render the lights and opaque geometry Typically a
        sequence pass with a light pass and opaque pass.
        """
    )

    def _get_shadow_map_baker_pass(self):
        return wrap_vtk(self._vtk_obj.GetShadowMapBakerPass())
    def _set_shadow_map_baker_pass(self, arg):
        old_val = self._get_shadow_map_baker_pass()
        self._wrap_call(self._vtk_obj.SetShadowMapBakerPass,
                        deref_vtk(arg))
        self.trait_property_changed('shadow_map_baker_pass', old_val, arg)
    shadow_map_baker_pass = traits.Property(_get_shadow_map_baker_pass, _set_shadow_map_baker_pass, help=\
        """
        Pass that generates the shadow maps. the ShadowMapPass will
        use the Resolution ivar of this pass. Initial value is a NULL
        pointer.
        """
    )

    def _get_fragment_declaration(self):
        return self._vtk_obj.GetFragmentDeclaration()
    fragment_declaration = traits.Property(_get_fragment_declaration, help=\
        """
        Get the shader code to compute light factors based on a mappers
        vertex_vc variable
        """
    )

    def _get_fragment_implementation(self):
        return self._vtk_obj.GetFragmentImplementation()
    fragment_implementation = traits.Property(_get_fragment_implementation, help=\
        """
        
        """
    )

    def set_uniforms(self, *args):
        """
        V.set_uniforms(ShaderProgram)
        C++: void SetUniforms(ShaderProgram *program)
        A mapper can call this to set the uniforms that this pass uses
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUniforms, *my_args)
        return ret

    def shadow_map_pass(self):
        """
        V.shadow_map_pass() -> InformationObjectBaseKey
        C++: static InformationObjectBaseKey *ShadowMapPass()
        this key will contain the shadow map pass
        """
        ret = wrap_vtk(self._vtk_obj.ShadowMapPass())
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
            return super(ShadowMapPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ShadowMapPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ShadowMapPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ShadowMapPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


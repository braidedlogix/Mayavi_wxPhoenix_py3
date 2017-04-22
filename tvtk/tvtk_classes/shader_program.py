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


class ShaderProgram(Object):
    """
    ShaderProgram - a glsl shader program
    
    Superclass: Object
    
    This class contains the vertex, fragment, geometry shaders that
    combine to make a shader program
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkShaderProgram, obj, update, **traits)
    
    compiled = tvtk_base.false_bool_trait(help=\
        """
        Set/Get flag for if this program is compiled
        """
    )

    def _compiled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCompiled,
                        self.compiled_)

    def _get_fragment_shader(self):
        return wrap_vtk(self._vtk_obj.GetFragmentShader())
    def _set_fragment_shader(self, arg):
        old_val = self._get_fragment_shader()
        self._wrap_call(self._vtk_obj.SetFragmentShader,
                        deref_vtk(arg))
        self.trait_property_changed('fragment_shader', old_val, arg)
    fragment_shader = traits.Property(_get_fragment_shader, _set_fragment_shader, help=\
        """
        Get the fragment shader for this program
        """
    )

    def _get_geometry_shader(self):
        return wrap_vtk(self._vtk_obj.GetGeometryShader())
    def _set_geometry_shader(self, arg):
        old_val = self._get_geometry_shader()
        self._wrap_call(self._vtk_obj.SetGeometryShader,
                        deref_vtk(arg))
        self.trait_property_changed('geometry_shader', old_val, arg)
    geometry_shader = traits.Property(_get_geometry_shader, _set_geometry_shader, help=\
        """
        Get the geometry shader for this program
        """
    )

    md5_hash = traits.String('', enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _md5_hash_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMD5Hash,
                        self.md5_hash)

    def _get_transform_feedback(self):
        return wrap_vtk(self._vtk_obj.GetTransformFeedback())
    def _set_transform_feedback(self, arg):
        old_val = self._get_transform_feedback()
        self._wrap_call(self._vtk_obj.SetTransformFeedback,
                        deref_vtk(arg))
        self.trait_property_changed('transform_feedback', old_val, arg)
    transform_feedback = traits.Property(_get_transform_feedback, _set_transform_feedback, help=\
        """
        Get/Set a transform_feedback_capture object on this shader program.
        """
    )

    def _get_vertex_shader(self):
        return wrap_vtk(self._vtk_obj.GetVertexShader())
    def _set_vertex_shader(self, arg):
        old_val = self._get_vertex_shader()
        self._wrap_call(self._vtk_obj.SetVertexShader,
                        deref_vtk(arg))
        self.trait_property_changed('vertex_shader', old_val, arg)
    vertex_shader = traits.Property(_get_vertex_shader, _set_vertex_shader, help=\
        """
        Get the vertex shader for this program
        """
    )

    def _get_error(self):
        return self._vtk_obj.GetError()
    error = traits.Property(_get_error, help=\
        """
        Get the error message (empty if none) for the shader program.
        """
    )

    def _get_handle(self):
        return self._vtk_obj.GetHandle()
    handle = traits.Property(_get_handle, help=\
        """
        Get the handle of the shader program.
        """
    )

    def disable_attribute_array(self, *args):
        """
        V.disable_attribute_array(string) -> bool
        C++: bool DisableAttributeArray(const char *name)
        Disable the named attribute array. Return false if the attribute
        array is not contained in the linked shader program.
        """
        ret = self._wrap_call(self._vtk_obj.DisableAttributeArray, *args)
        return ret

    def enable_attribute_array(self, *args):
        """
        V.enable_attribute_array(string) -> bool
        C++: bool EnableAttributeArray(const char *name)
        Enable the named attribute array. Return false if the attribute
        array is not contained in the linked shader program.
        """
        ret = self._wrap_call(self._vtk_obj.EnableAttributeArray, *args)
        return ret

    def is_attribute_used(self, *args):
        """
        V.is_attribute_used(string) -> bool
        C++: bool IsAttributeUsed(const char *name)
        Return true if the compiled and linked shader has an attribute
        matching @a name.
        """
        ret = self._wrap_call(self._vtk_obj.IsAttributeUsed, *args)
        return ret

    def is_uniform_used(self, *args):
        """
        V.is_uniform_used(string) -> bool
        C++: bool IsUniformUsed(const char *)
        methods to inquire as to what uniforms/attributes are used by
        this shader.  This can save some compute time if the uniforms or
        attributes are expensive to compute
        """
        ret = self._wrap_call(self._vtk_obj.IsUniformUsed, *args)
        return ret

    def release_graphics_resources(self, *args):
        """
        V.release_graphics_resources(Window)
        C++: void ReleaseGraphicsResources(Window *win)
        release any graphics resources this class is using.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReleaseGraphicsResources, *my_args)
        return ret

    def set_number_of_outputs(self, *args):
        """
        V.set_number_of_outputs(int)
        C++: void SetNumberOfOutputs(unsigned int a)"""
        ret = self._wrap_call(self._vtk_obj.SetNumberOfOutputs, *args)
        return ret

    def set_uniform1fv(self, *args):
        """
        V.set_uniform1fv(string, int, (float, ...)) -> bool
        C++: bool SetUniform1fv(const char *name, const int count,
            const float *f)"""
        ret = self._wrap_call(self._vtk_obj.SetUniform1fv, *args)
        return ret

    def set_uniform1iv(self, *args):
        """
        V.set_uniform1iv(string, int, (int, ...)) -> bool
        C++: bool SetUniform1iv(const char *name, const int count,
            const int *f)
        Set the name uniform array to f with count elements
        """
        ret = self._wrap_call(self._vtk_obj.SetUniform1iv, *args)
        return ret

    def set_uniform2f(self, *args):
        """
        V.set_uniform2f(string, (float, float)) -> bool
        C++: bool SetUniform2f(const char *name, const float v[2])"""
        ret = self._wrap_call(self._vtk_obj.SetUniform2f, *args)
        return ret

    def set_uniform2i(self, *args):
        """
        V.set_uniform2i(string, (int, int)) -> bool
        C++: bool SetUniform2i(const char *name, const int v[2])"""
        ret = self._wrap_call(self._vtk_obj.SetUniform2i, *args)
        return ret

    def set_uniform3f(self, *args):
        """
        V.set_uniform3f(string, (float, float, float)) -> bool
        C++: bool SetUniform3f(const char *name, const float v[3])"""
        ret = self._wrap_call(self._vtk_obj.SetUniform3f, *args)
        return ret

    def set_uniform3uc(self, *args):
        """
        V.set_uniform3uc(string, (int, int, int)) -> bool
        C++: bool SetUniform3uc(const char *name,
            const unsigned char v[3])"""
        ret = self._wrap_call(self._vtk_obj.SetUniform3uc, *args)
        return ret

    def set_uniform4f(self, *args):
        """
        V.set_uniform4f(string, (float, float, float, float)) -> bool
        C++: bool SetUniform4f(const char *name, const float v[4])"""
        ret = self._wrap_call(self._vtk_obj.SetUniform4f, *args)
        return ret

    def set_uniform4uc(self, *args):
        """
        V.set_uniform4uc(string, (int, int, int, int)) -> bool
        C++: bool SetUniform4uc(const char *name,
            const unsigned char v[4])"""
        ret = self._wrap_call(self._vtk_obj.SetUniform4uc, *args)
        return ret

    def set_uniform_matrix(self, *args):
        """
        V.set_uniform_matrix(string, Matrix3x3) -> bool
        C++: bool SetUniformMatrix(const char *name, Matrix3x3 *v)
        V.set_uniform_matrix(string, Matrix4x4) -> bool
        C++: bool SetUniformMatrix(const char *name, Matrix4x4 *v)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUniformMatrix, *my_args)
        return ret

    def set_uniform_matrix3x3(self, *args):
        """
        V.set_uniform_matrix3x3(string, [float, ...]) -> bool
        C++: bool SetUniformMatrix3x3(const char *name, float *v)"""
        ret = self._wrap_call(self._vtk_obj.SetUniformMatrix3x3, *args)
        return ret

    def set_uniform_matrix4x4(self, *args):
        """
        V.set_uniform_matrix4x4(string, [float, ...]) -> bool
        C++: bool SetUniformMatrix4x4(const char *name, float *v)"""
        ret = self._wrap_call(self._vtk_obj.SetUniformMatrix4x4, *args)
        return ret

    def set_uniform_matrix4x4v(self, *args):
        """
        V.set_uniform_matrix4x4v(string, int, [float, ...]) -> bool
        C++: bool SetUniformMatrix4x4v(const char *name, const int count,
            float *v)"""
        ret = self._wrap_call(self._vtk_obj.SetUniformMatrix4x4v, *args)
        return ret

    def set_uniformf(self, *args):
        """
        V.set_uniformf(string, float) -> bool
        C++: bool SetUniformf(const char *name, float v)"""
        ret = self._wrap_call(self._vtk_obj.SetUniformf, *args)
        return ret

    def set_uniformi(self, *args):
        """
        V.set_uniformi(string, int) -> bool
        C++: bool SetUniformi(const char *name, int v)
        Set the name uniform value to int v.
        """
        ret = self._wrap_call(self._vtk_obj.SetUniformi, *args)
        return ret

    def substitute(self, *args):
        """
        V.substitute(string, string, string, bool) -> bool
        C++: static bool Substitute(std::string &source,
            const std::string &search, const std::string &replace,
            bool all=true)
        perform in place string substitutions, indicate if a substitution
        was done this is useful for building up shader strings which
        typically involve lots of string substitutions. Return true if a
        substitution was done.
        """
        ret = self._wrap_call(self._vtk_obj.Substitute, *args)
        return ret

    def use_attribute_array(self, *args):
        """
        V.use_attribute_array(string, int, int, int, int, NormalizeOption)
            -> bool
        C++: bool UseAttributeArray(const char *name, int offset,
            size_t stride, int elementType, int elementTupleSize,
            NormalizeOption normalize)
        Use the named attribute array with the bound buffer_object.
        @param name of the attribute (as seen in the shader program).
        @param offset into the bound buffer_object.
        @param stride The stride of the element access (i.e. the size of
            each
        element in the currently bound buffer_object). 0 may be used to
        indicate tightly packed data.
        @param element_type Tag identifying the memory representation of
            the
        element.
        @param element_tuple_size The number of elements per vertex (e.g. a
        3d
        position attribute would be 3).
        @param normalize Indicates the range used by the attribute data.
        See normalize_option for more information.
        @return false if the attribute array does not exist.
        """
        ret = self._wrap_call(self._vtk_obj.UseAttributeArray, *args)
        return ret

    def is_bound(self):
        """
        V.is_bound() -> bool
        C++: bool isBound()
        Check if the program is currently bound, or not.
        @return True if the program is bound, false otherwise.
        """
        ret = self._vtk_obj.isBound()
        return ret
        

    _updateable_traits_ = \
    (('compiled', 'GetCompiled'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('md5_hash',
    'GetMD5Hash'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['compiled', 'debug', 'global_warning_display', 'md5_hash'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ShaderProgram, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ShaderProgram properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compiled'], [], ['md5_hash']),
            title='Edit ShaderProgram properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ShaderProgram properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


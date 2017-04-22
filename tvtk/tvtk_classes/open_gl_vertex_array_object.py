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


class OpenGLVertexArrayObject(Object):
    """
    OpenGLVertexArrayObject - The vertex_array_object class uses, or
    emulates, vertex array objects.
    
    Superclass: Object
    
    These are extremely useful for setup/tear down of vertex attributes,
    and can offer significant performance benefits when the hardware
    supports them.
    
    It should be noted that this object is very lightweight, and it
    assumes the objects being used are correctly set up. Even without
    support for VAOs this class caches the array locations, types, etc
    and avoids repeated look ups. It it bound to a single shader_program
    object.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLVertexArrayObject, obj, update, **traits)
    
    def add_attribute_array(self, *args):
        """
        V.add_attribute_array(ShaderProgram, OpenGLBufferObject,
            string, int, int, int, int, bool) -> bool
        C++: bool AddAttributeArray(ShaderProgram *program,
            OpenGLBufferObject *buffer, const std::string &name,
            int offset, size_t stride, int elementType,
            int elementTupleSize, bool normalize)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddAttributeArray, *my_args)
        return ret

    def add_attribute_array_with_divisor(self, *args):
        """
        V.add_attribute_array_with_divisor(ShaderProgram,
            OpenGLBufferObject, string, int, int, int, int, bool, int,
            bool) -> bool
        C++: bool AddAttributeArrayWithDivisor(ShaderProgram *program,
            OpenGLBufferObject *buffer, const std::string &name,
            int offset, size_t stride, int elementType,
            int elementTupleSize, bool normalize, int divisor,
            bool isMatrix)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddAttributeArrayWithDivisor, *my_args)
        return ret

    def add_attribute_matrix_with_divisor(self, *args):
        """
        V.add_attribute_matrix_with_divisor(ShaderProgram,
            OpenGLBufferObject, string, int, int, int, int, bool, int)
            -> bool
        C++: bool AddAttributeMatrixWithDivisor(ShaderProgram *program,
             OpenGLBufferObject *buffer, const std::string &name,
            int offset, size_t stride, int elementType,
            int elementTupleSize, bool normalize, int divisor)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddAttributeMatrixWithDivisor, *my_args)
        return ret

    def bind(self):
        """
        V.bind()
        C++: void Bind()"""
        ret = self._vtk_obj.Bind()
        return ret
        

    def release(self):
        """
        V.release()
        C++: void Release()"""
        ret = self._vtk_obj.Release()
        return ret
        

    def release_graphics_resources(self):
        """
        V.release_graphics_resources()
        C++: void ReleaseGraphicsResources()"""
        ret = self._vtk_obj.ReleaseGraphicsResources()
        return ret
        

    def remove_attribute_array(self, *args):
        """
        V.remove_attribute_array(string) -> bool
        C++: bool RemoveAttributeArray(const std::string &name)"""
        ret = self._wrap_call(self._vtk_obj.RemoveAttributeArray, *args)
        return ret

    def set_force_emulation(self, *args):
        """
        V.set_force_emulation(bool)
        C++: void SetForceEmulation(bool val)"""
        ret = self._wrap_call(self._vtk_obj.SetForceEmulation, *args)
        return ret

    def shader_program_changed(self):
        """
        V.shader_program_changed()
        C++: void ShaderProgramChanged()"""
        ret = self._vtk_obj.ShaderProgramChanged()
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
            return super(OpenGLVertexArrayObject, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLVertexArrayObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit OpenGLVertexArrayObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLVertexArrayObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


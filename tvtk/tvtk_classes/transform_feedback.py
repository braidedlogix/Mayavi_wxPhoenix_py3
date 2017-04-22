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


class TransformFeedback(Object):
    """
    TransformFeedback - Manages a transform_feedback buffer.
    
    Superclass: Object
    
    open_gl's transform_feedback allows varying attributes from a
    vertex/geometry shader to be captured into a buffer for later
    processing. This is used in VTK to capture vertex information during
    gl2ps export when using the open_gl2 backend as a replacement for the
    deprecated open_gl feedback buffer.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTransformFeedback, obj, update, **traits)
    
    number_of_vertices = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The number of vertices expected to be captured. If the draw_mode
        setter is used, primitive_mode will also be set appropriately. For
        the single argument version set function, set the exact number of
        vertices expected to be emitted, accounting for primitive
        expansion (e.g. triangle strips -> triangle strips). The two
        argument setter is for convenience. Given the number of vertices
        used as input to a draw command and the draw mode, it will
        calculate the total number of vertices.
        """
    )

    def _number_of_vertices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfVertices,
                        self.number_of_vertices)

    primitive_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The type of primitive to capture. Must be one of GL_POINTS,
        GL_LINES, or GL_TRIANGLES. Default is GL_POINTS. Must be set
        prior to calling bind_buffer.
        """
    )

    def _primitive_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPrimitiveMode,
                        self.primitive_mode)

    def _get_buffer_data(self):
        return self._vtk_obj.GetBufferData()
    buffer_data = traits.Property(_get_buffer_data, help=\
        """
        Get the transform buffer data as a void pointer. Only valid after
        calling read_buffer.
        """
    )

    def _get_buffer_handle(self):
        return self._vtk_obj.GetBufferHandle()
    buffer_handle = traits.Property(_get_buffer_handle, help=\
        """
        Get the handle to the transform buffer object. Only valid after
        calling bind_buffer and before read_buffer.
        """
    )

    def _get_buffer_size(self):
        return self._vtk_obj.GetBufferSize()
    buffer_size = traits.Property(_get_buffer_size, help=\
        """
        The size (in bytes) of the capture buffer. Available after adding
        all Varyings and setting number_of_vertices.
        """
    )

    def _get_bytes_per_vertex(self):
        return self._vtk_obj.GetBytesPerVertex()
    bytes_per_vertex = traits.Property(_get_bytes_per_vertex, help=\
        """
        Returns the number of data elements each vertex requires for a
        given role.
        """
    )

    def add_varying(self, *args):
        """
        V.add_varying(VaryingRole, string)
        C++: void AddVarying(VaryingRole role, const std::string &var)
        Capture the varying 'var' with the indicated role.
        """
        ret = self._wrap_call(self._vtk_obj.AddVarying, *args)
        return ret

    def bind_buffer(self):
        """
        V.bind_buffer()
        C++: void BindBuffer()
        Generates, binds, and allocates the feedback buffer, then call
        gl_begin_transform_feedback with the specified primitive_mode. Must
        be called after bind_varyings and before any relevant gl_draw
        commands.
        """
        ret = self._vtk_obj.BindBuffer()
        return ret
        

    def bind_varyings(self, *args):
        """
        V.bind_varyings(ShaderProgram)
        C++: void BindVaryings(ShaderProgram *prog)
        GL_SEPARATE_ATTRIBS is not supported yet. The buffer_mode argument
        to gl_transform_feedback_varyings. Must be GL_INTERLEAVED_ATTRIBS or
        GL_SEPARATE_ATTRIBS. Default is interleaved. Must be set prior to
        calling bind_varyings. SetMacro(BufferMode, int)
        GetMacro(BufferMode, int)
        
        Call gl_transform_feedback_varyings(). Must be called after the
        shaders are attached to prog, but before the program is linked.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.BindVaryings, *my_args)
        return ret

    def clear_varyings(self):
        """
        V.clear_varyings()
        C++: void ClearVaryings()
        Clear the list of varying attributes to capture.
        """
        ret = self._vtk_obj.ClearVaryings()
        return ret
        

    def read_buffer(self):
        """
        V.read_buffer()
        C++: void ReadBuffer()
        Calls gl_end_transform_feedback(), flushes the open_gl command
        stream, and reads the transform feedback buffer into buffer_data.
        Must be called after any relevant gl_draw commands.
        """
        ret = self._vtk_obj.ReadBuffer()
        return ret
        

    def release_buffer_data(self, *args):
        """
        V.release_buffer_data(bool)
        C++: void ReleaseBufferData(bool freeBuffer=true)
        Release the memory used by the buffer data. If free_buffer == true
        (default), the data is deleted. If false, the caller is
        responsible for deleting the buffer_data with delete[].
        """
        ret = self._wrap_call(self._vtk_obj.ReleaseBufferData, *args)
        return ret

    def release_graphics_resources(self):
        """
        V.release_graphics_resources()
        C++: void ReleaseGraphicsResources()
        Release any graphics resources used by this object.
        """
        ret = self._vtk_obj.ReleaseGraphicsResources()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_vertices',
    'GetNumberOfVertices'), ('primitive_mode', 'GetPrimitiveMode'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'number_of_vertices',
    'primitive_mode'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TransformFeedback, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TransformFeedback properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['number_of_vertices', 'primitive_mode']),
            title='Edit TransformFeedback properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TransformFeedback properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


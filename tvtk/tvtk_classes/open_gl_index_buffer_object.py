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

from tvtk.tvtk_classes.open_gl_buffer_object import OpenGLBufferObject


class OpenGLIndexBufferObject(OpenGLBufferObject):
    """
    OpenGLIndexBufferObject - open_gl vertex buffer object
    
    Superclass: OpenGLBufferObject
    
    open_gl buffer object to store geometry and/or attribute data on the
    GPU.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLIndexBufferObject, obj, update, **traits)
    
    def create_edge_flag_index_buffer(self, *args):
        """
        V.create_edge_flag_index_buffer(CellArray, DataArray) -> int
        C++: size_t CreateEdgeFlagIndexBuffer(CellArray *cells,
            DataArray *edgeflags)"""
        my_args = deref_array(args, [('vtkCellArray', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.CreateEdgeFlagIndexBuffer, *my_args)
        return ret

    def create_line_index_buffer(self, *args):
        """
        V.create_line_index_buffer(CellArray) -> int
        C++: size_t CreateLineIndexBuffer(CellArray *cells)
        create a IBO for wireframe polys/tris
        """
        my_args = deref_array(args, [['vtkCellArray']])
        ret = self._wrap_call(self._vtk_obj.CreateLineIndexBuffer, *my_args)
        return ret

    def create_point_index_buffer(self, *args):
        """
        V.create_point_index_buffer(CellArray) -> int
        C++: size_t CreatePointIndexBuffer(CellArray *cells)
        used to create an IBO for primatives as points
        """
        my_args = deref_array(args, [['vtkCellArray']])
        ret = self._wrap_call(self._vtk_obj.CreatePointIndexBuffer, *my_args)
        return ret

    def create_strip_index_buffer(self, *args):
        """
        V.create_strip_index_buffer(CellArray, bool) -> int
        C++: size_t CreateStripIndexBuffer(CellArray *cells,
            bool wireframeTriStrips)
        used to create an IBO for line strips and triangle strips
        """
        my_args = deref_array(args, [('vtkCellArray', 'bool')])
        ret = self._wrap_call(self._vtk_obj.CreateStripIndexBuffer, *my_args)
        return ret

    def create_triangle_index_buffer(self, *args):
        """
        V.create_triangle_index_buffer(CellArray, Points) -> int
        C++: size_t CreateTriangleIndexBuffer(CellArray *cells,
            Points *points)
        used to create an IBO for triangle primatives
        """
        my_args = deref_array(args, [('vtkCellArray', 'vtkPoints')])
        ret = self._wrap_call(self._vtk_obj.CreateTriangleIndexBuffer, *my_args)
        return ret

    def create_triangle_line_index_buffer(self, *args):
        """
        V.create_triangle_line_index_buffer(CellArray) -> int
        C++: size_t CreateTriangleLineIndexBuffer(CellArray *cells)
        create a IBO for wireframe polys/tris
        """
        my_args = deref_array(args, [['vtkCellArray']])
        ret = self._wrap_call(self._vtk_obj.CreateTriangleLineIndexBuffer, *my_args)
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
            return super(OpenGLIndexBufferObject, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLIndexBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit OpenGLIndexBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLIndexBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


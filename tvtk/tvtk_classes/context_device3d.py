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


class ContextDevice3D(Object):
    """
    ContextDevice3D - Abstract class for drawing 3d primitives.
    
    Superclass: Object
    
    This defines the interface for a ContextDevice3D. In this sense a
    context_device is a class used to paint 3d primitives onto a device,
    such as an open_gl context.
    
    This is private API, and should not be used outside of the
    Context3D.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContextDevice3D, obj, update, **traits)
    
    def get_matrix(self, *args):
        """
        V.get_matrix(Matrix4x4)
        C++: virtual void GetMatrix(Matrix4x4 *m)
        Set the model view matrix for the display
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetMatrix, *my_args)
        return ret

    def set_matrix(self, *args):
        """
        V.set_matrix(Matrix4x4)
        C++: virtual void SetMatrix(Matrix4x4 *m)
        Set the model view matrix for the display
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetMatrix, *my_args)
        return ret

    def apply_brush(self, *args):
        """
        V.apply_brush(Brush)
        C++: virtual void ApplyBrush(Brush *brush)
        Apply the supplied brush which controls the outlines of shapes,
        as well as lines, points and related primitives. This makes a
        deep copy of the Brush object in the Context2D, it does not
        hold a pointer to the supplied object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ApplyBrush, *my_args)
        return ret

    def apply_pen(self, *args):
        """
        V.apply_pen(Pen)
        C++: virtual void ApplyPen(Pen *pen)
        Apply the supplied pen which controls the outlines of shapes, as
        well as lines, points and related primitives. This makes a deep
        copy of the Pen object in the Context2D, it does not hold a
        pointer to the supplied object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ApplyPen, *my_args)
        return ret

    def disable_clipping(self):
        """
        V.disable_clipping()
        C++: virtual void DisableClipping()
        Disable clipping of the display. Remove in a future release -
        retained for API compatibility.
        """
        ret = self._vtk_obj.DisableClipping()
        return ret
        

    def disable_clipping_plane(self, *args):
        """
        V.disable_clipping_plane(int)
        C++: virtual void DisableClippingPlane(int i)
        Enable/Disable the specified clipping plane.
        """
        ret = self._wrap_call(self._vtk_obj.DisableClippingPlane, *args)
        return ret

    def draw_lines(self, *args):
        """
        V.draw_lines((float, ...), int, (int, ...), int)
        C++: virtual void DrawLines(const float *verts, int n,
            const unsigned char *colors=0, int nc=0)
        Draw lines defined by specified pair of points.
        \sa draw_poly()
        """
        ret = self._wrap_call(self._vtk_obj.DrawLines, *args)
        return ret

    def draw_points(self, *args):
        """
        V.draw_points((float, ...), int, (int, ...), int)
        C++: virtual void DrawPoints(const float *verts, int n,
            const unsigned char *colors=0, int nc=0)
        Draw points at the vertex positions specified.
        """
        ret = self._wrap_call(self._vtk_obj.DrawPoints, *args)
        return ret

    def draw_poly(self, *args):
        """
        V.draw_poly((float, ...), int, (int, ...), int)
        C++: virtual void DrawPoly(const float *verts, int n,
            const unsigned char *colors=0, int nc=0)
        Draw a polyline between the specified points.
        \sa draw_lines()
        """
        ret = self._wrap_call(self._vtk_obj.DrawPoly, *args)
        return ret

    def draw_triangle_mesh(self, *args):
        """
        V.draw_triangle_mesh((float, ...), int, (int, ...), int)
        C++: virtual void DrawTriangleMesh(const float *mesh, int n,
            const unsigned char *colors, int nc)
        Draw triangles to generate the specified mesh.
        """
        ret = self._wrap_call(self._vtk_obj.DrawTriangleMesh, *args)
        return ret

    def enable_clipping(self, *args):
        """
        V.enable_clipping(bool)
        C++: virtual void EnableClipping(bool enable)
        Enable or disable the clipping of the scene.
        """
        ret = self._wrap_call(self._vtk_obj.EnableClipping, *args)
        return ret

    def enable_clipping_plane(self, *args):
        """
        V.enable_clipping_plane(int, [float, ...])
        C++: virtual void EnableClippingPlane(int i,
            double *planeEquation)
        Enable/Disable the specified clipping plane.
        """
        ret = self._wrap_call(self._vtk_obj.EnableClippingPlane, *args)
        return ret

    def multiply_matrix(self, *args):
        """
        V.multiply_matrix(Matrix4x4)
        C++: virtual void MultiplyMatrix(Matrix4x4 *m)
        Multiply the current model view matrix by the supplied one
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MultiplyMatrix, *my_args)
        return ret

    def pop_matrix(self):
        """
        V.pop_matrix()
        C++: virtual void PopMatrix()
        Pop the current matrix off of the stack.
        """
        ret = self._vtk_obj.PopMatrix()
        return ret
        

    def push_matrix(self):
        """
        V.push_matrix()
        C++: virtual void PushMatrix()
        Push the current matrix onto the stack.
        """
        ret = self._vtk_obj.PushMatrix()
        return ret
        

    def set_clipping(self, *args):
        """
        V.set_clipping(Recti)
        C++: virtual void SetClipping(const Recti &rect)
        Supply a float array of length 4 with x1, y1, width, height
        specifying clipping region for the device in pixels.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetClipping, *my_args)
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
            return super(ContextDevice3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ContextDevice3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ContextDevice3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContextDevice3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


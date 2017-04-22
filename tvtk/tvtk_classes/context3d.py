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


class Context3D(Object):
    """
    Context3D - Class for drawing 3d primitives to a graphical context.
    
    Superclass: Object
    
    This defines the interface for drawing onto a 3d context. The context
    must be set up with a ContextDevice3D derived class that provides
    the functions to facilitate the low level calls to the context.
    Currently only an open_gl based device is provided.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContext3D, obj, update, **traits)
    
    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        Compute the current transform applied to the context.
        """
    )

    def _get_device(self):
        return wrap_vtk(self._vtk_obj.GetDevice())
    device = traits.Property(_get_device, help=\
        """
        Get access to the underlying 3d context.
        """
    )

    def append_transform(self, *args):
        """
        V.append_transform(Transform)
        C++: void AppendTransform(Transform *transform)
        Append the transform for the context, the underlying device will
        use the matrix of the transform. Note, this is set immediately,
        later changes to the matrix will have no effect until it is set
        again. The matrix of the transform will multiply the current
        context transform.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AppendTransform, *my_args)
        return ret

    def apply_brush(self, *args):
        """
        V.apply_brush(Brush)
        C++: void ApplyBrush(Brush *brush)
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
        C++: void ApplyPen(Pen *pen)
        Apply the supplied pen which controls the outlines of shapes, as
        well as lines, points and related primitives. This makes a deep
        copy of the Pen object in the Context2D, it does not hold a
        pointer to the supplied object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ApplyPen, *my_args)
        return ret

    def begin(self, *args):
        """
        V.begin(ContextDevice3D) -> bool
        C++: bool Begin(ContextDevice3D *device)
        Begin painting on a ContextDevice3D, no painting can occur
        before this call has been made. Only one painter is allowed at a
        time on any given paint device. Returns true if successful,
        otherwise false.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Begin, *my_args)
        return ret

    def disable_clipping_plane(self, *args):
        """
        V.disable_clipping_plane(int)
        C++: void DisableClippingPlane(int i)
        Enable/Disable the specified clipping plane. i is the index of
        the clipping plane being enabled or disabled (0 - 5).
        plane_equation points to the four coefficients of the equation for
        the clipping plane: Ax + By + Cz + D = 0.  This is the equation
        format expected by gl_clip_plane.
        """
        ret = self._wrap_call(self._vtk_obj.DisableClippingPlane, *args)
        return ret

    def draw_line(self, *args):
        """
        V.draw_line(Vector3f, Vector3f)
        C++: void DrawLine(const Vector3f &start,
            const Vector3f &end)
        Draw a line between the specified points.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DrawLine, *my_args)
        return ret

    def draw_point(self, *args):
        """
        V.draw_point(Vector3f)
        C++: void DrawPoint(const Vector3f &point)
        Draw a point at the point in 3d space.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DrawPoint, *my_args)
        return ret

    def draw_points(self, *args):
        """
        V.draw_points((float, ...), int)
        C++: void DrawPoints(const float *points, int n)
        V.draw_points((float, ...), int, [int, ...], int)
        C++: void DrawPoints(const float *points, int n,
            unsigned char *colors, int nc_comps)
        Draw a sequence of points at the specified locations.
        """
        ret = self._wrap_call(self._vtk_obj.DrawPoints, *args)
        return ret

    def draw_poly(self, *args):
        """
        V.draw_poly((float, ...), int)
        C++: void DrawPoly(const float *points, int n)
        Draw a poly line between the specified points.
        """
        ret = self._wrap_call(self._vtk_obj.DrawPoly, *args)
        return ret

    def draw_triangle_mesh(self, *args):
        """
        V.draw_triangle_mesh((float, ...), int, (int, ...), int)
        C++: void DrawTriangleMesh(const float *mesh, int n,
            const unsigned char *colors, int nc)
        Draw triangles to generate the specified mesh.
        """
        ret = self._wrap_call(self._vtk_obj.DrawTriangleMesh, *args)
        return ret

    def enable_clipping_plane(self, *args):
        """
        V.enable_clipping_plane(int, [float, ...])
        C++: void EnableClippingPlane(int i, double *planeEquation)
        Enable/Disable the specified clipping plane. i is the index of
        the clipping plane being enabled or disabled (0 - 5).
        plane_equation points to the four coefficients of the equation for
        the clipping plane: Ax + By + Cz + D = 0.  This is the equation
        format expected by gl_clip_plane.
        """
        ret = self._wrap_call(self._vtk_obj.EnableClippingPlane, *args)
        return ret

    def end(self):
        """
        V.end() -> bool
        C++: bool End()
        Ends painting on the device, you would not usually need to call
        this as it should be called by the destructor. Returns true if
        the painter is no longer active, otherwise false.
        """
        ret = self._vtk_obj.End()
        return ret
        

    def pop_matrix(self):
        """
        V.pop_matrix()
        C++: void PopMatrix()
        Push/pop the transformation matrix for the painter (sets the
        underlying matrix for the device when available).
        """
        ret = self._vtk_obj.PopMatrix()
        return ret
        

    def push_matrix(self):
        """
        V.push_matrix()
        C++: void PushMatrix()
        Push/pop the transformation matrix for the painter (sets the
        underlying matrix for the device when available).
        """
        ret = self._vtk_obj.PushMatrix()
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
            return super(Context3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Context3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit Context3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Context3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


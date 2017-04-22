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


class ContextDevice2D(Object):
    """
    ContextDevice2D - Abstract class for drawing 2d primitives.
    
    Superclass: Object
    
    This defines the interface for a ContextDevice2D. In this sense a
    context_device is a class used to paint 2d primitives onto a device,
    such as an open_gl context or a q_graphics_view.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContextDevice2D, obj, update, **traits)
    
    def get_matrix(self, *args):
        """
        V.get_matrix(Matrix3x3)
        C++: virtual void GetMatrix(Matrix3x3 *m)
        Set the model view matrix for the display
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetMatrix, *my_args)
        return ret

    def set_matrix(self, *args):
        """
        V.set_matrix(Matrix3x3)
        C++: virtual void SetMatrix(Matrix3x3 *m)
        Set the model view matrix for the display
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetMatrix, *my_args)
        return ret

    def _get_brush(self):
        return wrap_vtk(self._vtk_obj.GetBrush())
    brush = traits.Property(_get_brush, help=\
        """
        Get the pen which controls the outlines of shapes as well as
        lines, points and related primitives.
        """
    )

    def _get_buffer_id_mode(self):
        return self._vtk_obj.GetBufferIdMode()
    buffer_id_mode = traits.Property(_get_buffer_id_mode, help=\
        """
        Tell if the device context is in buffer_id creation mode. Initial
        value is false.
        """
    )

    def _get_height(self):
        return self._vtk_obj.GetHeight()
    height = traits.Property(_get_height, help=\
        """
        Get the width of the device in pixels.
        """
    )

    def _get_pen(self):
        return wrap_vtk(self._vtk_obj.GetPen())
    pen = traits.Property(_get_pen, help=\
        """
        Get the pen which controls the outlines of shapes, as well as
        lines, points and related primitives. This object can be modified
        and the changes will be reflected in subsequent drawing
        operations.
        """
    )

    def _get_text_prop(self):
        return wrap_vtk(self._vtk_obj.GetTextProp())
    text_prop = traits.Property(_get_text_prop, help=\
        """
        Get the text properties object for the Context2D.
        """
    )

    def _get_width(self):
        return self._vtk_obj.GetWidth()
    width = traits.Property(_get_width, help=\
        """
        Get the width of the device in pixels.
        """
    )

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

    def apply_text_prop(self, *args):
        """
        V.apply_text_prop(TextProperty)
        C++: virtual void ApplyTextProp(TextProperty *prop)
        Apply the supplied text property which controls how text is
        rendered. This makes a deep copy of the TextProperty object in
        the Context2D, it does not hold a pointer to the supplied
        object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ApplyTextProp, *my_args)
        return ret

    def begin(self, *args):
        """
        V.begin(Viewport)
        C++: virtual void Begin(Viewport *)
        Begin drawing, pass in the viewport to set up the view.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Begin, *my_args)
        return ret

    def buffer_id_mode_begin(self, *args):
        """
        V.buffer_id_mode_begin(AbstractContextBufferId)
        C++: virtual void BufferIdModeBegin(
            AbstractContextBufferId *bufferId)
        Start buffer_id creation Mode. The default implementation is
        empty.
        \pre not_yet: !_get_buffer_id_mode()
        \pre buffer_id_exists: buffer_id!=_0
        \post started: get_buffer_id_mode()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.BufferIdModeBegin, *my_args)
        return ret

    def buffer_id_mode_end(self):
        """
        V.buffer_id_mode_end()
        C++: virtual void BufferIdModeEnd()
        Finalize buffer_id creation Mode. It makes sure that the content
        of the buffer_id passed in argument of buffer_id_mode_begin() is
        correctly set. The default implementation is empty.
        \pre started: get_buffer_id_mode()
        \post done: !_get_buffer_id_mode()
        """
        ret = self._vtk_obj.BufferIdModeEnd()
        return ret
        

    def compute_justified_string_bounds(self, *args):
        """
        V.compute_justified_string_bounds(string, [float, float, float,
            float])
        C++: virtual void ComputeJustifiedStringBounds(const char *string,
             float bounds[4])
        Compute the bounds of the supplied string while taking into
        account the justification of the currently applied text property.
        Simple rotations (0, 90, 180, 270) are also correctly taken into
        account.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeJustifiedStringBounds, *args)
        return ret

    def compute_string_bounds(self, *args):
        """
        V.compute_string_bounds(string, [float, float, float, float])
        C++: virtual void ComputeStringBounds(const StdString &string,
            float bounds[4])
        V.compute_string_bounds(unicode, [float, float, float, float])
        C++: virtual void ComputeStringBounds(
            const UnicodeString &string, float bounds[4])
        Compute the bounds of the supplied string. The bounds will be
        copied to the supplied bounds variable, the first two elements
        are the bottom corner of the string, and the second two elements
        are the width and height of the bounding box. NOTE: This function
        does not take account of the text rotation or justification.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeStringBounds, *args)
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
        

    def draw_ellipse_wedge(self, *args):
        """
        V.draw_ellipse_wedge(float, float, float, float, float, float,
            float, float)
        C++: virtual void DrawEllipseWedge(float x, float y, float outRx,
            float outRy, float inRx, float inRy, float startAngle,
            float stopAngle)
        Draw an elliptic wedge with center at x, y, outer radii out_rx,
        out_ry, inner radii in_rx, in_ry between angles start_angle and
        stop_angle (expressed in degrees).
        \pre positive_out_rx: out_rx>=_0
        \pre positive_out_ry: out_ry>=_0
        \pre positive_in_rx: in_rx>=_0
        \pre positive_in_ry: in_ry>=_0
        \pre ordered_rx: in_rx<=out_rx
        \pre ordered_ry: in_ry<=out_ry
        """
        ret = self._wrap_call(self._vtk_obj.DrawEllipseWedge, *args)
        return ret

    def draw_elliptic_arc(self, *args):
        """
        V.draw_elliptic_arc(float, float, float, float, float, float)
        C++: virtual void DrawEllipticArc(float x, float y, float rX,
            float rY, float startAngle, float stopAngle)
        Draw an elliptic arc with center at x,y with radii r_x and r_y
        between angles start_angle and stop_angle (expressed in degrees).
        \pre positive_r_x: r_x>=_0
        \pre positive_r_y: r_y>=_0
        """
        ret = self._wrap_call(self._vtk_obj.DrawEllipticArc, *args)
        return ret

    def draw_image(self, *args):
        """
        V.draw_image([float, float], float, ImageData)
        C++: virtual void DrawImage(float p[2], float scale,
            ImageData *image)
        V.draw_image(Rectf, ImageData)
        C++: virtual void DrawImage(const Rectf &pos,
            ImageData *image)
        Draw the supplied image at the given x, y (p[0], p[1]) (bottom
        corner), scaled by scale (1.0 would match the image).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DrawImage, *my_args)
        return ret

    def draw_lines(self, *args):
        """
        V.draw_lines([float, ...], int, [int, ...], int)
        C++: virtual void DrawLines(float *f, int n,
            unsigned char *colors=0, int nc_comps=0)
        Draw lines using the points - memory layout is as follows:
        l1p1,l1p2,l2p1,l2p2... The lines will be colored by colors array
        which has nc_comps components (defining a single color).
        \sa draw_poly()
        """
        ret = self._wrap_call(self._vtk_obj.DrawLines, *args)
        return ret

    def draw_markers(self, *args):
        """
        V.draw_markers(int, bool, [float, ...], int, [int, ...], int)
        C++: virtual void DrawMarkers(int shape, bool highlight,
            float *points, int n, unsigned char *colors=0, int nc_comps=0)
        Draw a series of markers centered at the points supplied. The
        shape argument controls the marker shape, and can be one of
        - VTK_MARKER_CROSS
        - VTK_MARKER_PLUS
        - VTK_MARKER_SQUARE
        - VTK_MARKER_CIRCLE
        - VTK_MARKER_DIAMOND
        \param colors is an optional array of colors.
        \param nc_comps is the number of components for the color.
        """
        ret = self._wrap_call(self._vtk_obj.DrawMarkers, *args)
        return ret

    def draw_math_text_string(self, *args):
        """
        V.draw_math_text_string([float, ...], string)
        C++: virtual void DrawMathTextString(float *point,
            const StdString &string)
        Draw text using math_text markup for mathematical equations. See
        http://matplotlib.sourceforge.net/users/mathtext.html for more
        information.
        """
        ret = self._wrap_call(self._vtk_obj.DrawMathTextString, *args)
        return ret

    def draw_point_sprites(self, *args):
        """
        V.draw_point_sprites(ImageData, [float, ...], int, [int, ...],
            int)
        C++: virtual void DrawPointSprites(ImageData *sprite,
            float *points, int n, unsigned char *colors=0, int nc_comps=0)
        Draw a series of point sprites, images centred at the points
        supplied. The supplied ImageData is the sprite to be drawn,
        only squares will be drawn and the size is set using
        set_point_size.
        \param colors is an optional array of colors.
        \param nc_comps is the number of components for the color.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DrawPointSprites, *my_args)
        return ret

    def draw_points(self, *args):
        """
        V.draw_points([float, ...], int, [int, ...], int)
        C++: virtual void DrawPoints(float *points, int n,
            unsigned char *colors=0, int nc_comps=0)
        Draw a series of points - fastest code path due to memory layout
        of the coordinates. The colors and nc_comps are optional - color
        array.
        """
        ret = self._wrap_call(self._vtk_obj.DrawPoints, *args)
        return ret

    def draw_poly(self, *args):
        """
        V.draw_poly([float, ...], int, [int, ...], int)
        C++: virtual void DrawPoly(float *points, int n,
            unsigned char *colors=0, int nc_comps=0)
        Draw a poly line using the points - fastest code path due to
        memory layout of the coordinates. The line will be colored by the
        colors array, which must be have nc_comps components (defining a
        single color).
        \sa draw_lines()
        """
        ret = self._wrap_call(self._vtk_obj.DrawPoly, *args)
        return ret

    def draw_polygon(self, *args):
        """
        V.draw_polygon([float, ...], int)
        C++: virtual void DrawPolygon(float *, int)
        Draw a polygon using the specified number of points.
        """
        ret = self._wrap_call(self._vtk_obj.DrawPolygon, *args)
        return ret

    def draw_quad(self, *args):
        """
        V.draw_quad([float, ...], int)
        C++: virtual void DrawQuad(float *, int)
        Draw a quad using the specified number of points.
        """
        ret = self._wrap_call(self._vtk_obj.DrawQuad, *args)
        return ret

    def draw_quad_strip(self, *args):
        """
        V.draw_quad_strip([float, ...], int)
        C++: virtual void DrawQuadStrip(float *, int)
        Draw a quad using the specified number of points.
        """
        ret = self._wrap_call(self._vtk_obj.DrawQuadStrip, *args)
        return ret

    def draw_string(self, *args):
        """
        V.draw_string([float, ...], string)
        C++: virtual void DrawString(float *point,
            const StdString &string)
        V.draw_string([float, ...], unicode)
        C++: virtual void DrawString(float *point,
            const UnicodeString &string)
        Draw some text to the screen.
        """
        ret = self._wrap_call(self._vtk_obj.DrawString, *args)
        return ret

    def enable_clipping(self, *args):
        """
        V.enable_clipping(bool)
        C++: virtual void EnableClipping(bool enable)
        Enable or disable the clipping of the scene.
        """
        ret = self._wrap_call(self._vtk_obj.EnableClipping, *args)
        return ret

    def end(self):
        """
        V.end()
        C++: virtual void End()
        End drawing, clean up the view.
        """
        ret = self._vtk_obj.End()
        return ret
        

    def math_text_is_supported(self):
        """
        V.math_text_is_supported() -> bool
        C++: virtual bool MathTextIsSupported()
        Return true if math_text rendering available on this device.
        """
        ret = self._vtk_obj.MathTextIsSupported()
        return ret
        

    def multiply_matrix(self, *args):
        """
        V.multiply_matrix(Matrix3x3)
        C++: virtual void MultiplyMatrix(Matrix3x3 *m)
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
        V.set_clipping([int, ...])
        C++: virtual void SetClipping(int *x)
        Supply a float array of length 4 with x1, y1, width, height
        specifying clipping region for the device in pixels.
        """
        ret = self._wrap_call(self._vtk_obj.SetClipping, *args)
        return ret

    def set_color4(self, *args):
        """
        V.set_color4([int, int, int, int])
        C++: virtual void SetColor4(unsigned char color[4])
        Set the color for the device using unsigned char of length 4,
        RGBA.
        """
        ret = self._wrap_call(self._vtk_obj.SetColor4, *args)
        return ret

    def set_line_type(self, *args):
        """
        V.set_line_type(int)
        C++: virtual void SetLineType(int type)
        Set the line type type (using anonymous enum in Pen).
        """
        ret = self._wrap_call(self._vtk_obj.SetLineType, *args)
        return ret

    def set_line_width(self, *args):
        """
        V.set_line_width(float)
        C++: virtual void SetLineWidth(float width)
        Set the line width.
        """
        ret = self._wrap_call(self._vtk_obj.SetLineWidth, *args)
        return ret

    def set_point_size(self, *args):
        """
        V.set_point_size(float)
        C++: virtual void SetPointSize(float size)
        Set the point size for glyphs/sprites.
        """
        ret = self._wrap_call(self._vtk_obj.SetPointSize, *args)
        return ret

    def set_texture(self, *args):
        """
        V.set_texture(ImageData, int)
        C++: virtual void SetTexture(ImageData *image, int properties)
        Set the texture for the device, it is used to fill the polygons
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTexture, *my_args)
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
            return super(ContextDevice2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ContextDevice2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ContextDevice2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContextDevice2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


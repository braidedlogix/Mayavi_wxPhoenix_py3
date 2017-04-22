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


class TextRenderer(Object):
    """
    TextRenderer - Interface for generating images and path data from
    string data, using multiple backends.
    
    Superclass: Object
    
    TextRenderer produces images, bounding boxes, and Path objects
    that represent text. The advantage of using this class is to easily
    integrate mathematical expressions into renderings by automatically
    switching between free_type and math_text backends. If the input string
    contains at least two "$" symbols separated by text, the math_text
    backend will be used. If the string does not meet this criteria, or
    if no math_text implementation is available, the faster free_type
    rendering facilities are used. Literal $ symbols can be used by
    escaping them with backslashes, "\$" (or "\\$" if the string is set
    programatically).
    
    For example, "Acceleration ($\\frac{m}{s^2}$)" will use math_text, but "\\$500,
    \\$100" will use free_type.
    
    By default, the backend is set to Detect, which determines the
    backend based on the contents of the string. This can be changed by
    setting the default_backend ivar.
    
    Note that this class is abstract -- link to the RenderingFreetype
    module to get the default implementation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextRenderer, obj, update, **traits)
    
    default_backend = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The backend to use when none is specified. Default: Detect
        """
    )

    def _default_backend_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultBackend,
                        self.default_backend)

    def get_bounding_box(self, *args):
        """
        V.get_bounding_box(TextProperty, string, [int, int, int, int],
            int, int) -> bool
        C++: bool GetBoundingBox(TextProperty *tprop,
            const StdString &str, int bbox[4], int dpi,
            int backend=TextRenderer::Default)
        V.get_bounding_box(TextProperty, unicode, [int, int, int, int],
            int, int) -> bool
        C++: bool GetBoundingBox(TextProperty *tprop,
            const UnicodeString &str, int bbox[4], int dpi,
            int backend=TextRenderer::Default)
        Given a text property and a string, get the bounding box {xmin,
        xmax, ymin, ymax} of the rendered string in pixels. The origin of
        the bounding box is the anchor point described by the horizontal
        and vertical justification text property variables. Return true
        on success, false otherwise.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetBoundingBox, *my_args)
        return ret

    def get_constrained_font_size(self, *args):
        """
        V.get_constrained_font_size(string, TextProperty, int, int, int,
            int) -> int
        C++: int GetConstrainedFontSize(const StdString &str,
            TextProperty *tprop, int targetWidth, int targetHeight,
            int dpi, int backend=TextRenderer::Default)
        V.get_constrained_font_size(unicode, TextProperty, int, int, int,
            int) -> int
        C++: int GetConstrainedFontSize(const UnicodeString &str,
            TextProperty *tprop, int targetWidth, int targetHeight,
            int dpi, int backend=TextRenderer::Default)
        This function returns the font size (in points) and sets the size
        in @a tprop that is required to fit the string in the target
        rectangle. The computed font size will be set in tprop as well.
        If an error occurs, this function will return -1.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetConstrainedFontSize, *my_args)
        return ret

    def _get_instance(self):
        return wrap_vtk(self._vtk_obj.GetInstance())
    instance = traits.Property(_get_instance, help=\
        """
        Return the singleton instance with no reference counting. May
        return NULL if the object factory cannot find an override.
        """
    )

    def detect_backend(self, *args):
        """
        V.detect_backend(string) -> int
        C++: virtual int DetectBackend(const StdString &str)
        V.detect_backend(unicode) -> int
        C++: virtual int DetectBackend(const UnicodeString &str)
        Determine the appropriate back end needed to render the given
        string.
        """
        ret = self._wrap_call(self._vtk_obj.DetectBackend, *args)
        return ret

    def free_type_is_supported(self):
        """
        V.free_type_is_supported() -> bool
        C++: virtual bool FreeTypeIsSupported()
        Test for availability of various backends
        """
        ret = self._vtk_obj.FreeTypeIsSupported()
        return ret
        

    def math_text_is_supported(self):
        """
        V.math_text_is_supported() -> bool
        C++: virtual bool MathTextIsSupported()"""
        ret = self._vtk_obj.MathTextIsSupported()
        return ret
        

    def render_string(self, *args):
        """
        V.render_string(TextProperty, string, ImageData, [int, int],
            int, int) -> bool
        C++: bool RenderString(TextProperty *tprop,
            const StdString &str, ImageData *data, int textDims[2],
            int dpi, int backend=TextRenderer::Default)
        V.render_string(TextProperty, unicode, ImageData, [int, int],
             int, int) -> bool
        C++: bool RenderString(TextProperty *tprop,
            const UnicodeString &str, ImageData *data,
            int textDims[2], int dpi,
            int backend=TextRenderer::Default)
        Given a text property and a string, this function initializes the
        ImageData *data and renders it in a ImageData. Return true
        on success, false otherwise. If using the overload that specifies
        "text_dims", the array will be overwritten with the pixel width
        and height defining a tight bounding box around the text in the
        image, starting from the upper-right corner. This is used when
        rendering for a texture on graphics hardware that requires
        texture image dimensions to be a power of two; text_dims can be
        used to determine the texture coordinates needed to cleanly fit
        the text on the target. The origin of the image's extents is
        aligned with the anchor point described by the text property's
        vertical and horizontal justification options.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderString, *my_args)
        return ret

    def set_scale_to_power_of_two(self, *args):
        """
        V.set_scale_to_power_of_two(bool)
        C++: void SetScaleToPowerOfTwo(bool scale)
        Set to true if the graphics implmentation requires texture image
        dimensions to be a power of two. Default is true, but this member
        will be set appropriately by
        OpenGLRenderWindow::OpenGLInitContext when GL is inited.
        """
        ret = self._wrap_call(self._vtk_obj.SetScaleToPowerOfTwo, *args)
        return ret

    def string_to_path(self, *args):
        """
        V.string_to_path(TextProperty, string, Path, int, int) -> bool
        C++: bool StringToPath(TextProperty *tprop,
            const StdString &str, Path *path, int dpi,
            int backend=TextRenderer::Default)
        V.string_to_path(TextProperty, unicode, Path, int, int)
            -> bool
        C++: bool StringToPath(TextProperty *tprop,
            const UnicodeString &str, Path *path, int dpi,
            int backend=TextRenderer::Default)
        Given a text property and a string, this function populates the
        Path path with the outline of the rendered string. The origin
        of the path coordinates is aligned with the anchor point
        described by the text property's horizontal and vertical
        justification options. Return true on success, false otherwise.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.StringToPath, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('default_backend', 'GetDefaultBackend'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'default_backend'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextRenderer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TextRenderer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['default_backend']),
            title='Edit TextRenderer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextRenderer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


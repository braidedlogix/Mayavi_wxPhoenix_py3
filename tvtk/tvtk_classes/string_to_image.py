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


class StringToImage(Object):
    """
    StringToImage - base class for classes that render supplied text
    to an image.
    
    Superclass: Object
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStringToImage, obj, update, **traits)
    
    scale_to_power_of_two = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Should we produce images at powers of 2, makes rendering on old
        open_gl hardware easier. Default is false.
        """
    )

    def _scale_to_power_of_two_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleToPowerOfTwo,
                        self.scale_to_power_of_two)

    def get_bounds(self, *args):
        """
        V.get_bounds(TextProperty, unicode, int) -> Vector2i
        C++: virtual Vector2i GetBounds(TextProperty *property,
            const UnicodeString &string, int dpi)
        V.get_bounds(TextProperty, string, int) -> Vector2i
        C++: virtual Vector2i GetBounds(TextProperty *property,
            const StdString &string, int dpi)
        Given a text property and a string, get the bounding box [xmin,
        xmax] x [ymin, ymax]. Note that this is the bounding box of the
        area where actual pixels will be written, given a
        text/pen/baseline location of (0,0). For example, if the string
        starts with a 'space', or depending on the orientation, you can
        end up with a [-20, -10] x [5, 10] bbox (the math to get the real
        bbox is straightforward). Return 1 on success, 0 otherwise. You
        can use is_bounding_box_valid() to test if the computed bbox is
        valid (it may not if get_bounding_box() failed or if the string was
        empty).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetBounds, *my_args)
        return wrap_vtk(ret)

    def render_string(self, *args):
        """
        V.render_string(TextProperty, unicode, int, ImageData, [int,
            int]) -> int
        C++: virtual int RenderString(TextProperty *property,
            const UnicodeString &string, int dpi, ImageData *data,
            int textDims[2]=NULL)
        V.render_string(TextProperty, string, int, ImageData, [int,
            int]) -> int
        C++: virtual int RenderString(TextProperty *property,
            const StdString &string, int dpi, ImageData *data,
            int text_dims[2]=NULL)
        Given a text property and a string, this function initializes the
        ImageData *data and renders it in a ImageData. text_dims, if
        provided, will be overwritten by the pixel width and height of
        the rendered string. This is useful when scale_to_power_of_two is
        true, and the image dimensions may not match the dimensions of
        the rendered text.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderString, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('scale_to_power_of_two',
    'GetScaleToPowerOfTwo'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'scale_to_power_of_two'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StringToImage, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StringToImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['scale_to_power_of_two']),
            title='Edit StringToImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StringToImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


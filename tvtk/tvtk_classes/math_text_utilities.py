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


class MathTextUtilities(Object):
    """
    MathTextUtilities - Abstract interface to equation rendering.
    
    Superclass: Object
    
    MathTextUtilities defines an interface for equation rendering.
    Intended for use with the python matplotlib.mathtext module
    (implemented in the Matplotlib module).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMathTextUtilities, obj, update, **traits)
    
    def _get_instance(self):
        return wrap_vtk(self._vtk_obj.GetInstance())
    def _set_instance(self, arg):
        old_val = self._get_instance()
        self._wrap_call(self._vtk_obj.SetInstance,
                        deref_vtk(arg))
        self.trait_property_changed('instance', old_val, arg)
    instance = traits.Property(_get_instance, _set_instance, help=\
        """
        Return the singleton instance with no reference counting.
        """
    )

    def _get_scale_to_power_of_two(self):
        return self._vtk_obj.GetScaleToPowerOfTwo()
    def _set_scale_to_power_of_two(self, arg):
        old_val = self._get_scale_to_power_of_two()
        self._wrap_call(self._vtk_obj.SetScaleToPowerOfTwo,
                        arg)
        self.trait_property_changed('scale_to_power_of_two', old_val, arg)
    scale_to_power_of_two = traits.Property(_get_scale_to_power_of_two, _set_scale_to_power_of_two, help=\
        """
        Set to true if the graphics implmentation requires texture image
        dimensions to be a power of two. Default is true, but this member
        will be set appropriately when GL is inited.
        """
    )

    def get_bounding_box(self, *args):
        """
        V.get_bounding_box(TextProperty, string, int, [int, int, int,
            int]) -> bool
        C++: virtual bool GetBoundingBox(TextProperty *tprop,
            const char *str, int dpi, int bbox[4])
        Determine the dimensions of the image that render_string will
        produce for a given str, tprop, and dpi
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetBoundingBox, *my_args)
        return ret

    def get_constrained_font_size(self, *args):
        """
        V.get_constrained_font_size(string, TextProperty, int, int, int)
            -> int
        C++: virtual int GetConstrainedFontSize(const char *str,
            TextProperty *tprop, int targetWidth, int targetHeight,
            int dpi)
        This function returns the font size (in points) required to fit
        the string in the target rectangle. The font size of tprop is
        updated to the computed value as well. If an error occurs (e.g.
        an improperly formatted math_text string), -1 is returned.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetConstrainedFontSize, *my_args)
        return ret

    def is_available(self):
        """
        V.is_available() -> bool
        C++: virtual bool IsAvailable()
        Returns true if mathtext rendering is available.
        """
        ret = self._vtk_obj.IsAvailable()
        return ret
        

    def render_string(self, *args):
        """
        V.render_string(string, ImageData, TextProperty, int, [int,
            int]) -> bool
        C++: virtual bool RenderString(const char *str,
            ImageData *data, TextProperty *tprop, int dpi,
            int textDims[2]=NULL)
        Render the given string str into the ImageData data with a
        resolution of dpi. text_dims, will be overwritten by the pixel
        width and height of the rendered string. This is useful when
        scale_to_power_of_two is set to true, and the image dimensions may
        not match the dimensions of the rendered text.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderString, *my_args)
        return ret

    def string_to_path(self, *args):
        """
        V.string_to_path(string, Path, TextProperty, int) -> bool
        C++: virtual bool StringToPath(const char *str, Path *path,
            TextProperty *tprop, int dpi)
        Parse the math_text expression in str and fill path with a contour
        of the glyphs.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.StringToPath, *my_args)
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
            return super(MathTextUtilities, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MathTextUtilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit MathTextUtilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MathTextUtilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


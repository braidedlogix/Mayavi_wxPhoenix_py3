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


class NamedColors(Object):
    """
    NamedColors - A class holding colors and their names.
    
    Superclass: Object
    
    NamedColors is class that holds colors and their associated names.
    
    Color names are case insensitive and are stored as lower-case names
    along with a 4-element array whose elements are red, green, blue and
    alpha, in that order, corresponding to the RGBA value of the color.
    
    It is assumed that if the RGBA values are unsigned char then each
    element lies in the range 0...255 and if the RGBA values are double
    then each element lies in the range 0...1.
    
    The colors and names are those in
    http://en.wikipedia.org/wiki/Web_colors that are derived from the
    CSS3 specification: http://www.w3.org/TR/css3-color/#svg-color In
    this table common synonyms such as cyan/aqua and magenta/fuchsia are
    also included.
    
    Also included in this class are names and colors taken from
    Wrapping/Tcl/vtktesting/colors.tcl and
    Wrapping/Python/vtk/util/colors.py.
    
    Web colors and names in http://en.wikipedia.org/wiki/Web_colors take
    precedence over those in colors.tcl and colors.py. One consequence of
    this is that while colors.py and colors.tcl specify green as
    equivalent to (0,255,0), the web color standard defines it as
    (0,128,0).
    
    For a web page of VTK Named Colors and their RGB values, see:
    http://www.vtk.org/_wiki/_vtk/_examples/_python/_visualization/_vtk_named_colo
    r_patches_html .
    
    The code used to generate this table is available from:
    http://www.vtk.org/_wiki/_vtk/_examples/_python/_visualization/_named_color_pa
    tches , this is useful if you wish to generate your own table.
    
    The set_color methods will overwrite existing colors if the name of
    the color being set matches an existing color. Note that
    color_exists() can be used to test for existence of the color being
    set.
    
    In the case of the get_color methods returning doubles, alternative
    versions, identified by the letters RGB in the names, are provided.
    These get functions return just the red, green and blue components of
    a color.
    
    The class also provides methods for defining a color through an HTML
    color string. The following formats are supported:
    
    - #RGB                  (3-digit hexadecimal number, where #_4f2 is a
      shortcut for #_44ff22)
    - #RRGGBB               (6-digit hexadecimal number)
    - rgb(r, g, b)          (where r, g, b are in 0..255 or percentage
      values)
    - rgba(r, g, b, a)      (where r, g, b, are in 0..255 or percentage
      values, a is in 0.0..1.0)
    - a CSS3 color name     (e.g. "steelblue")
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkNamedColors, obj, update, **traits)
    
    def get_color(self, *args):
        """
        V.get_color(string, int, int, int, int)
        C++: void GetColor(const StdString &name, unsigned char &r,
            unsigned char &g, unsigned char &b, unsigned char &a)
        V.get_color(string, [int, int, int, int])
        C++: void GetColor(const StdString &name,
            unsigned char rgba[4])
        V.get_color(string, Color4ub)
        C++: void GetColor(const StdString &name, Color4ub &rgba)
        V.get_color(string, float, float, float, float)
        C++: void GetColor(const StdString &name, double &r, double &g,
             double &b, double &a)
        V.get_color(string, [float, float, float, float])
        C++: void GetColor(const StdString &name, double rgba[4])
        V.get_color(string, Color4d)
        C++: void GetColor(const StdString &name, Color4d &rgba)
        V.get_color(string, float, float, float)
        C++: void GetColor(const StdString &name, double &r, double &g,
             double &b)
        V.get_color(string, Color3ub)
        C++: void GetColor(const StdString &name, Color3ub &rgb)
        V.get_color(string, Color3d)
        C++: void GetColor(const StdString &name, Color3d &rgb)
        Get the color by name. The name is treated as being
        case-insensitive. The color is returned as four unsigned char
        variables: red, green, blue, alpha. The range of each element is
        0...255. The color black is returned if the color is not found.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetColor, *my_args)
        return ret

    def set_color(self, *args):
        """
        V.set_color(string, int, int, int, int)
        C++: virtual void SetColor(const StdString &name,
            const unsigned char &r, const unsigned char &g,
            const unsigned char &b, const unsigned char &a=255)
        V.set_color(string, float, float, float, float)
        C++: virtual void SetColor(const StdString &name,
            const double &r, const double &g, const double &b,
            const double &a=1)
        V.set_color(string, (int, int, int, int))
        C++: virtual void SetColor(const StdString &name,
            const unsigned char rgba[4])
        V.set_color(string, Color4ub)
        C++: virtual void SetColor(const StdString &name,
            const Color4ub &rgba)
        V.set_color(string, Color3ub)
        C++: virtual void SetColor(const StdString &name,
            const Color3ub &rgb)
        V.set_color(string, (float, float, float, float))
        C++: virtual void SetColor(const StdString &name,
            const double rgba[4])
        V.set_color(string, Color4d)
        C++: virtual void SetColor(const StdString &name,
            const Color4d &rgba)
        V.set_color(string, Color3d)
        C++: virtual void SetColor(const StdString &name,
            const Color3d &rgb)
        V.set_color(string, string)
        C++: void SetColor(const StdString &name,
            const StdString &htmlString)
        Set the color by name. The name is treated as being
        case-insensitive. The range of each color is 0...255. No color is
        set if the name is empty.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetColor, *my_args)
        return ret

    def get_color3d(self, *args):
        """
        V.get_color3d(string) -> Color3d
        C++: Color3d GetColor3d(const StdString &name)
        Get the color by name. The name is treated as being
        case-insensitive. The color is returned as a Color3d class.
        The color black is returned if the color is not found.
        """
        ret = self._wrap_call(self._vtk_obj.GetColor3d, *args)
        return wrap_vtk(ret)

    def get_color3ub(self, *args):
        """
        V.get_color3ub(string) -> Color3ub
        C++: Color3ub GetColor3ub(const StdString &name)
        Get the color by name. The name is treated as being
        case-insensitive. The color is returned as a Color3ub class.
        The color black is returned if the color is not found.
        """
        ret = self._wrap_call(self._vtk_obj.GetColor3ub, *args)
        return wrap_vtk(ret)

    def get_color4d(self, *args):
        """
        V.get_color4d(string) -> Color4d
        C++: Color4d GetColor4d(const StdString &name)
        Get the color by name. The name is treated as being
        case-insensitive. The color is returned as a Color4d class.
        The color black is returned if the color is not found.
        """
        ret = self._wrap_call(self._vtk_obj.GetColor4d, *args)
        return wrap_vtk(ret)

    def get_color4ub(self, *args):
        """
        V.get_color4ub(string) -> Color4ub
        C++: Color4ub GetColor4ub(const StdString &name)
        Get the color by name. The name is treated as being
        case-insensitive. The color is returned as a Color4ub class.
        The color black is returned if the color is not found.
        """
        ret = self._wrap_call(self._vtk_obj.GetColor4ub, *args)
        return wrap_vtk(ret)

    def _get_color_names(self):
        return self._vtk_obj.GetColorNames()
    color_names = traits.Property(_get_color_names, help=\
        """
        Return a string of color names with each name delimited by a line
        feed. This is easily parsed by the user into whatever data
        structure they require. Examples for parsing are provided in:
        test_named_colors.cxx and test_named_colors_integration.py
        """
    )

    def get_color_rgb(self, *args):
        """
        V.get_color_rgb(string, [float, float, float])
        C++: void GetColorRGB(const StdString &name, double rgb[3])
        Get the color by name. The name is treated as being
        case-insensitive. The color is returned as a double array: [red,
        green, blue]. The range of each element is 0...1. The color black
        is returned if the color is not found.
        """
        ret = self._wrap_call(self._vtk_obj.GetColorRGB, *args)
        return ret

    def _get_number_of_colors(self):
        return self._vtk_obj.GetNumberOfColors()
    number_of_colors = traits.Property(_get_number_of_colors, help=\
        """
        Get the number of colors.
        """
    )

    def _get_synonyms(self):
        return self._vtk_obj.GetSynonyms()
    synonyms = traits.Property(_get_synonyms, help=\
        """
        Return a string of synonyms such as cyan/aqua and
        magenta/fuchsia. The string is formatted such that a single line
        feed delimits each color in the synonym and a double line feed
        delimits each synonym. Warning this could take a long time for
        very large color maps. This is easily parsed by the user into
        whatever data structure they require.
        """
    )

    def color_exists(self, *args):
        """
        V.color_exists(string) -> bool
        C++: bool ColorExists(const StdString &name)
        Return true if the color exists.
        """
        ret = self._wrap_call(self._vtk_obj.ColorExists, *args)
        return ret

    def html_color_to_rgb(self, *args):
        """
        V.html_color_to_rgb(string) -> Color3ub
        C++: Color3ub HTMLColorToRGB(const StdString &colorString)
        Return a Color3ub instance from an HTML color string in any of
        the following formats:
        - #RGB
        - #RRGGBB
        - rgb(r, g, b)
        - rgba(r, g, b, a)
        - a CSS3 color name, e.g. "steelblue" If the string argument
          defines a color using one of the above formats the method
          returns the successfully parsed color else returns the color
          black.
        """
        ret = self._wrap_call(self._vtk_obj.HTMLColorToRGB, *args)
        return wrap_vtk(ret)

    def html_color_to_rgba(self, *args):
        """
        V.html_color_to_rgba(string) -> Color4ub
        C++: Color4ub HTMLColorToRGBA(const StdString &colorString)
        Return a Color4ub instance from an HTML color string in any of
        the following formats:
        - #RGB
        - #RRGGBB
        - rgb(r, g, b)
        - rgba(r, g, b, a)
        - a CSS3 color name, e.g. "steelblue" If the string argument
          defines a color using one of the above formats the method
          returns the successfully parsed color else returns a color
          equal to `rgba(0, 0, 0, 0)`.
        """
        ret = self._wrap_call(self._vtk_obj.HTMLColorToRGBA, *args)
        return wrap_vtk(ret)

    def rgba_to_html_color(self, *args):
        """
        V.rgba_to_html_color(Color4ub) -> string
        C++: StdString RGBAToHTMLColor(const Color4ub &rgba)
        Given a Color4ub instance as input color return a valid HTML
        color string in the `rgba(r, g, b, a)` format.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RGBAToHTMLColor, *my_args)
        return ret

    def rgb_to_html_color(self, *args):
        """
        V.rgb_to_html_color(Color3ub) -> string
        C++: StdString RGBToHTMLColor(const Color3ub &rgb)
        Given a Color3ub instance as input color return a valid HTML
        color string in the `#RRGGBB` format.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RGBToHTMLColor, *my_args)
        return ret

    def remove_color(self, *args):
        """
        V.remove_color(string)
        C++: void RemoveColor(const StdString &name)
        Remove the color by name. The name is treated as being
        case-insensitive. Examples for parsing are provided in:
        test_named_colors.cxx and test_named_colors_integration.py
        """
        ret = self._wrap_call(self._vtk_obj.RemoveColor, *args)
        return ret

    def reset_colors(self):
        """
        V.reset_colors()
        C++: void ResetColors()
        Reset the colors in the color map to the original colors. Any
        colors inserted by the user will be lost.
        """
        ret = self._vtk_obj.ResetColors()
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
            return super(NamedColors, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit NamedColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit NamedColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit NamedColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


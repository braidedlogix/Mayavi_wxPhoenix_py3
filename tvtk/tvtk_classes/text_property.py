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


class TextProperty(Object):
    """
    TextProperty - represent text properties.
    
    Superclass: Object
    
    TextProperty is an object that represents text properties. The
    primary properties that can be set are color, opacity, font size,
    font family horizontal and vertical justification, bold/italic/shadow
    styles.
    @sa
    TextMapper TextActor LegendBoxActor CaptionActor2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextProperty, obj, update, **traits)
    
    bold = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable text bolding.
        """
    )

    def _bold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBold,
                        self.bold_)

    frame = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable text frame.
        """
    )

    def _frame_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrame,
                        self.frame_)

    italic = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable text italic.
        """
    )

    def _italic_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetItalic,
                        self.italic_)

    shadow = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable text shadow.
        """
    )

    def _shadow_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShadow,
                        self.shadow_)

    use_tight_bounding_box = tvtk_base.false_bool_trait(help=\
        """
        If this property is on, text is alligned to drawn pixels not to
        font metrix. If the text does not include descents, the bounding
        box will not extend below the baseline. This option can be used
        to get centered labels. It does not work well if the string
        changes as the string position will move around.
        """
    )

    def _use_tight_bounding_box_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseTightBoundingBox,
                        self.use_tight_bounding_box_)

    font_family = traits.Trait('arial',
    tvtk_base.TraitRevPrefixMap({'arial': 0, 'courier': 1, 'times': 2}), help=\
        """
        Set/Get the font family. Supports legacy three font family
        system. If the symbolic constant VTK_FONT_FILE is returned by
        get_font_family(), the string returned by get_font_file() must be an
        absolute filepath to a local free_type compatible font.
        """
    )

    def _font_family_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFontFamily,
                        self.font_family_)

    justification = traits.Trait('left',
    tvtk_base.TraitRevPrefixMap({'left': 0, 'centered': 1, 'right': 2}), help=\
        """
        Set/Get the horizontal justification to left (default), centered,
        or right.
        """
    )

    def _justification_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetJustification,
                        self.justification_)

    vertical_justification = traits.Trait('bottom',
    tvtk_base.TraitRevPrefixMap({'bottom': 0, 'centered': 1, 'top': 2}), help=\
        """
        Set/Get the vertical justification to bottom (default), middle,
        or top.
        """
    )

    def _vertical_justification_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVerticalJustification,
                        self.vertical_justification_)

    background_color = tvtk_base.vtk_color_trait((0.0, 0.0, 0.0), help=\
        """
        
        """
    )

    def _background_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundColor,
                        self.background_color, False)

    background_opacity = traits.Trait(0.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        The background opacity. 1.0 is totally opaque and 0.0 is
        completely transparent.
        """
    )

    def _background_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundOpacity,
                        self.background_opacity)

    color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )

    def _color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColor,
                        self.color, False)

    font_file = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The absolute filepath to a local file containing a
        freetype-readable font if get_font_family() return VTK_FONT_FILE.
        The result is undefined for other values of get_font_family().
        """
    )

    def _font_file_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFontFile,
                        self.font_file)

    font_size = traits.Trait(12, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the font size (in points).
        """
    )

    def _font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFontSize,
                        self.font_size)

    frame_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )

    def _frame_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrameColor,
                        self.frame_color, False)

    frame_width = traits.Trait(1, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the width of the frame. The width is expressed in pixels.
        The default is 1 pixel.
        """
    )

    def _frame_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrameWidth,
                        self.frame_width)

    line_offset = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the vertical offset (measured in pixels).
        """
    )

    def _line_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineOffset,
                        self.line_offset)

    line_spacing = traits.Float(1.1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the (extra) spacing between lines, expressed as a text
        height multiplication factor.
        """
    )

    def _line_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineSpacing,
                        self.line_spacing)

    opacity = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the text's opacity. 1.0 is totally opaque and 0.0 is
        completely transparent.
        """
    )

    def _opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOpacity,
                        self.opacity)

    orientation = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the text's orientation (in degrees).
        """
    )

    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation)

    shadow_offset = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(1, -1), cols=2, help=\
        """
        
        """
    )

    def _shadow_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShadowOffset,
                        self.shadow_offset)

    def get_font_family_from_string(self, *args):
        """
        V.get_font_family_from_string(string) -> int
        C++: static int GetFontFamilyFromString(const char *f)
        Set/Get the font family. Supports legacy three font family
        system. If the symbolic constant VTK_FONT_FILE is returned by
        get_font_family(), the string returned by get_font_file() must be an
        absolute filepath to a local free_type compatible font.
        """
        ret = self._wrap_call(self._vtk_obj.GetFontFamilyFromString, *args)
        return ret

    def _get_font_family_min_value(self):
        return self._vtk_obj.GetFontFamilyMinValue()
    font_family_min_value = traits.Property(_get_font_family_min_value, help=\
        """
        Set/Get the font family. Supports legacy three font family
        system. If the symbolic constant VTK_FONT_FILE is returned by
        get_font_family(), the string returned by get_font_file() must be an
        absolute filepath to a local free_type compatible font.
        """
    )

    def get_shadow_color(self, *args):
        """
        V.get_shadow_color([float, float, float])
        C++: void GetShadowColor(double color[3])
        Get the shadow color. It is computed from the Color ivar
        """
        ret = self._wrap_call(self._vtk_obj.GetShadowColor, *args)
        return ret

    def set_font_family_as_string(self, *args):
        """
        V.set_font_family_as_string(string)
        C++: void SetFontFamilyAsString(char *)
        Set/Get the font family. Supports legacy three font family
        system. If the symbolic constant VTK_FONT_FILE is returned by
        get_font_family(), the string returned by get_font_file() must be an
        absolute filepath to a local free_type compatible font.
        """
        ret = self._wrap_call(self._vtk_obj.SetFontFamilyAsString, *args)
        return ret

    def shallow_copy(self, *args):
        """
        V.shallow_copy(TextProperty)
        C++: void ShallowCopy(TextProperty *tprop)
        Shallow copy of a text property.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    _updateable_traits_ = \
    (('bold', 'GetBold'), ('frame', 'GetFrame'), ('italic', 'GetItalic'),
    ('shadow', 'GetShadow'), ('use_tight_bounding_box',
    'GetUseTightBoundingBox'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('font_family',
    'GetFontFamily'), ('justification', 'GetJustification'),
    ('vertical_justification', 'GetVerticalJustification'),
    ('background_color', 'GetBackgroundColor'), ('background_opacity',
    'GetBackgroundOpacity'), ('color', 'GetColor'), ('font_file',
    'GetFontFile'), ('font_size', 'GetFontSize'), ('frame_color',
    'GetFrameColor'), ('frame_width', 'GetFrameWidth'), ('line_offset',
    'GetLineOffset'), ('line_spacing', 'GetLineSpacing'), ('opacity',
    'GetOpacity'), ('orientation', 'GetOrientation'), ('shadow_offset',
    'GetShadowOffset'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['bold', 'debug', 'frame', 'global_warning_display', 'italic',
    'shadow', 'use_tight_bounding_box', 'font_family', 'justification',
    'vertical_justification', 'background_color', 'background_opacity',
    'color', 'font_file', 'font_size', 'frame_color', 'frame_width',
    'line_offset', 'line_spacing', 'opacity', 'orientation',
    'shadow_offset'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextProperty, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TextProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['bold', 'frame', 'italic', 'shadow', 'use_tight_bounding_box'],
            ['font_family', 'justification', 'vertical_justification'],
            ['background_color', 'background_opacity', 'color', 'font_file',
            'font_size', 'frame_color', 'frame_width', 'line_offset',
            'line_spacing', 'opacity', 'orientation', 'shadow_offset']),
            title='Edit TextProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class FreeTypeTools(Object):
    """
    FreeTypeTools - free_type library support
    
    Superclass: Object
    
    FreeTypeTools provides a low-level interface to the free_type2
    library, including font-cache and rasterization.
    
    @warning
    Internal use only.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFreeTypeTools, obj, update, **traits)
    
    debug_textures = tvtk_base.false_bool_trait(help=\
        """
        If true, images produced by render_string will have a transparent
        grey background and set the justification anchor texel to bright
        yellow.
        """
    )

    def _debug_textures_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDebugTextures,
                        self.debug_textures_)

    force_compiled_fonts = tvtk_base.false_bool_trait(help=\
        """
        Force use of the fonts compiled into VTK, ignoring any font_config
        or embedded fonts. Useful for generating test images consistently
        across platforms. This flag is on by default.
        """
    )

    def _force_compiled_fonts_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForceCompiledFonts,
                        self.force_compiled_fonts_)

    scale_to_power_two = tvtk_base.false_bool_trait(help=\
        """
        Set whether the image produced should be scaled up to the nearest
        power of
        2. This is normally required for older graphics cards where all
           textures must be a power of 2. This defaults to false, and
           should be fine on modern hardware.
        """
    )

    def _scale_to_power_two_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleToPowerTwo,
                        self.scale_to_power_two_)

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

    maximum_number_of_bytes = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum number of faces (FT_Face), sizes (FT_Size)
        and bytes used by the cache. These settings can be changed as
        long as it is done prior to accessing any of the caches or the
        cache manager.
        """
    )

    def _maximum_number_of_bytes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfBytes,
                        self.maximum_number_of_bytes)

    maximum_number_of_faces = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum number of faces (FT_Face), sizes (FT_Size)
        and bytes used by the cache. These settings can be changed as
        long as it is done prior to accessing any of the caches or the
        cache manager.
        """
    )

    def _maximum_number_of_faces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfFaces,
                        self.maximum_number_of_faces)

    maximum_number_of_sizes = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum number of faces (FT_Face), sizes (FT_Size)
        and bytes used by the cache. These settings can be changed as
        long as it is done prior to accessing any of the caches or the
        cache manager.
        """
    )

    def _maximum_number_of_sizes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfSizes,
                        self.maximum_number_of_sizes)

    def get_bounding_box(self, *args):
        """
        V.get_bounding_box(TextProperty, string, int, [int, int, int,
            int]) -> bool
        C++: bool GetBoundingBox(TextProperty *tprop,
            const StdString &str, int dpi, int bbox[4])
        V.get_bounding_box(TextProperty, unicode, int, [int, int, int,
            int]) -> bool
        C++: bool GetBoundingBox(TextProperty *tprop,
            const UnicodeString &str, int dpi, int bbox[4])
        Given a text property and a string, get the bounding box {xmin,
        xmax, ymin, ymax} of the rendered string in pixels. The origin of
        the bounding box is the anchor point described by the horizontal
        and vertical justification text property variables. Returns true
        on success, false otherwise.
        @sa get_metrics
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetBoundingBox, *my_args)
        return ret

    def get_constrained_font_size(self, *args):
        """
        V.get_constrained_font_size(string, TextProperty, int, int, int)
            -> int
        C++: int GetConstrainedFontSize(const StdString &str,
            TextProperty *tprop, int dpi, int targetWidth,
            int targetHeight)
        V.get_constrained_font_size(unicode, TextProperty, int, int, int)
            -> int
        C++: int GetConstrainedFontSize(const UnicodeString &str,
            TextProperty *tprop, int dpi, int targetWidth,
            int targetHeight)
        This function returns the font size (in points) required to fit
        the string in the target rectangle. The font size of tprop is
        updated to the computed value as well. If an error occurs, -1 is
        returned.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetConstrainedFontSize, *my_args)
        return ret

    def hash_buffer(self, *args):
        """
        V.hash_buffer(void, int, int) -> int
        C++: static TypeUInt32 HashBuffer(const void *str, size_t n,
            TypeUInt32 hash=0)
        Hash a string of a given length. This function hashes n chars and
        does not depend on a terminating null character.
        """
        ret = self._wrap_call(self._vtk_obj.HashBuffer, *args)
        return ret

    def hash_string(self, *args):
        """
        V.hash_string(string) -> int
        C++: static TypeUInt16 HashString(const char *str)
        Turn a string into a hash. This is not a general purpose hash
        function, and is only used to generate identifiers for cached
        fonts.
        """
        ret = self._wrap_call(self._vtk_obj.HashString, *args)
        return ret

    def map_id_to_text_property(self, *args):
        """
        V.map_id_to_text_property(int, TextProperty)
        C++: void MapIdToTextProperty(size_t tprop_cache_id,
            TextProperty *tprop)
        Given a text property 'tprop', get its unique ID in our cache
        framework. In the same way, given a unique ID in our cache,
        retrieve the corresponding text property and assign its
        parameters to 'tprop'. Warning: there is no one to one mapping
        between a single text property the corresponding ID, and
        vice-versa. The ID is just a fast hash, a binary mask
        concatenating the attributes of the text property that are
        relevant to our cache (Color, Opacity, Justification setting are
        not stored).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MapIdToTextProperty, *my_args)
        return ret

    def map_text_property_to_id(self, *args):
        """
        V.map_text_property_to_id(TextProperty, [int, ...])
        C++: void MapTextPropertyToId(TextProperty *tprop,
            size_t *tprop_cache_id)
        Given a text property 'tprop', get its unique ID in our cache
        framework. In the same way, given a unique ID in our cache,
        retrieve the corresponding text property and assign its
        parameters to 'tprop'. Warning: there is no one to one mapping
        between a single text property the corresponding ID, and
        vice-versa. The ID is just a fast hash, a binary mask
        concatenating the attributes of the text property that are
        relevant to our cache (Color, Opacity, Justification setting are
        not stored).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MapTextPropertyToId, *my_args)
        return ret

    def render_string(self, *args):
        """
        V.render_string(TextProperty, string, int, ImageData, [int,
            int]) -> bool
        C++: bool RenderString(TextProperty *tprop,
            const StdString &str, int dpi, ImageData *data,
            int textDims[2]=NULL)
        V.render_string(TextProperty, unicode, int, ImageData, [int,
            int]) -> bool
        C++: bool RenderString(TextProperty *tprop,
            const UnicodeString &str, int dpi, ImageData *data,
            int textDims[2]=NULL)
        Given a text property and a string, this function initializes the
        ImageData *data and renders it in a ImageData. text_dims, if
        provided, will be overwritten by the pixel width and height of
        the rendered string. This is useful when scale_to_power_of_two is
        true, and the image dimensions may not match the dimensions of
        the rendered text. The origin of the image's extents is aligned
        with the anchor point described by the text property's vertical
        and horizontal justification options.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderString, *my_args)
        return ret

    def string_to_path(self, *args):
        """
        V.string_to_path(TextProperty, string, int, Path) -> bool
        C++: bool StringToPath(TextProperty *tprop,
            const StdString &str, int dpi, Path *path)
        V.string_to_path(TextProperty, unicode, int, Path) -> bool
        C++: bool StringToPath(TextProperty *tprop,
            const UnicodeString &str, int dpi, Path *path)
        Given a text property and a string, this function populates the
        Path path with the outline of the rendered string. The origin
        of the path coordinates is aligned with the anchor point
        described by the text property's horizontal and vertical
        justification options.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.StringToPath, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug_textures', 'GetDebugTextures'), ('force_compiled_fonts',
    'GetForceCompiledFonts'), ('scale_to_power_two',
    'GetScaleToPowerTwo'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_number_of_bytes', 'GetMaximumNumberOfBytes'),
    ('maximum_number_of_faces', 'GetMaximumNumberOfFaces'),
    ('maximum_number_of_sizes', 'GetMaximumNumberOfSizes'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'debug_textures', 'force_compiled_fonts',
    'global_warning_display', 'scale_to_power_two',
    'maximum_number_of_bytes', 'maximum_number_of_faces',
    'maximum_number_of_sizes'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FreeTypeTools, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FreeTypeTools properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['debug_textures', 'force_compiled_fonts',
            'scale_to_power_two'], [], ['maximum_number_of_bytes',
            'maximum_number_of_faces', 'maximum_number_of_sizes']),
            title='Edit FreeTypeTools properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FreeTypeTools properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


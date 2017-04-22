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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class Texture(ImageAlgorithm):
    """
    Texture - handles properties associated with a texture map
    
    Superclass: ImageAlgorithm
    
    Texture is an object that handles loading and binding of texture
    maps. It obtains its data from an input image data dataset type. Thus
    you can create visualization pipelines to read, process, and
    construct textures. Note that textures will only work if texture
    coordinates are also defined, and if the rendering system supports
    texture.
    
    Instances of Texture are associated with actors via the actor's
    set_texture() method. Actors can share texture maps (this is
    encouraged to save memory resources.)
    
    @warning
    Currently only 2d texture maps are supported, even though the data
    pipeline supports 1,2, and 3d texture coordinates.
    
    @warning
    Some renderers such as old open_gl require that the texture map
    dimensions are a power of two in each direction. If a non-power of
    two texture map is used, it is automatically resampled to a power of
    two in one or more directions, at the cost of an expensive
    computation. If the open_gl implementation is recent enough
    (_open_gl>=_2._0 or extension GL_ARB_texture_non_power_of_two exists)
    there is no such restriction and no extra computational cost.
    @sa
    Actor Renderer OpenGLTexture
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTexture, obj, update, **traits)
    
    edge_clamp = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the clamping of the texture map when the texture
        coords extend beyond the [0,1] range. Only used when Repeat is
        off, and edge clamping is supported by the graphics card.
        """
    )

    def _edge_clamp_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeClamp,
                        self.edge_clamp_)

    interpolate = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off linear interpolation of the texture map when
        rendering.
        """
    )

    def _interpolate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolate,
                        self.interpolate_)

    map_color_scalars_through_lookup_table = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the mapping of color scalars through the lookup
        table. The default is Off. If Off, unsigned char scalars will be
        used directly as texture. If On, scalars will be mapped through
        the lookup table to generate 4-component unsigned char scalars.
        This ivar does not affect other scalars like unsigned short,
        float, etc. These scalars are always mapped through lookup
        tables.
        """
    )

    def _map_color_scalars_through_lookup_table_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMapColorScalarsThroughLookupTable,
                        self.map_color_scalars_through_lookup_table_)

    premultiplied_alpha = tvtk_base.false_bool_trait(help=\
        """
        Whether the texture colors are premultiplied by alpha. Initial
        value is false.
        """
    )

    def _premultiplied_alpha_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPremultipliedAlpha,
                        self.premultiplied_alpha_)

    repeat = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the repetition of the texture map when the texture
        coords extend beyond the [0,1] range.
        """
    )

    def _repeat_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRepeat,
                        self.repeat_)

    restrict_power_of2_image_smaller = tvtk_base.false_bool_trait(help=\
        """
        When the texture is forced to be a power of 2, the default
        behavior is for the "new" image's dimensions  to be greater than
        or equal to with respects to the original.  Setting
        restrict_power_of2_image_smaller to be 1 (or ON) with force the new
        image's dimensions to be less than or equal to with respects to
        the original.
        """
    )

    def _restrict_power_of2_image_smaller_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRestrictPowerOf2ImageSmaller,
                        self.restrict_power_of2_image_smaller_)

    quality = traits.Trait('default',
    tvtk_base.TraitRevPrefixMap({'default': 0, '16_bit': 16, '32_bit': 32}), help=\
        """
        Force texture quality to 16-bit or 32-bit. This might not be
        supported on all machines.
        """
    )

    def _quality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuality,
                        self.quality_)

    blending_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Used to specify how the texture will blend its RGB and Alpha
        values with other textures and the fragment the texture is
        rendered upon.
        """
    )

    def _blending_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBlendingMode,
                        self.blending_mode)

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Specify the lookup table to convert scalars if necessary
        """
    )

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        Set a transform on the texture which allows one to scale, rotate
        and translate the texture.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input as a ImageData object.  This method is for
        backwards compatibility.
        """
    )

    def _get_mapped_scalars(self):
        return wrap_vtk(self._vtk_obj.GetMappedScalars())
    mapped_scalars = traits.Property(_get_mapped_scalars, help=\
        """
        Get Mapped Scalars
        """
    )

    def _get_texture_unit(self):
        return self._vtk_obj.GetTextureUnit()
    texture_unit = traits.Property(_get_texture_unit, help=\
        """
        Return the texture unit used for this texture
        """
    )

    def is_translucent(self):
        """
        V.is_translucent() -> int
        C++: virtual int IsTranslucent()
        Is this Texture Translucent? returns false (0) if the texture is
        either fully opaque or has only fully transparent pixels and
        fully opaque pixels and the Interpolate flag is turn off.
        """
        ret = self._vtk_obj.IsTranslucent()
        return ret
        

    def load(self, *args):
        """
        V.load(Renderer)
        C++: virtual void Load(Renderer *)
        Abstract interface to renderer. Each concrete subclass of
        Texture will load its data into graphics system in response to
        this method invocation.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Load, *my_args)
        return ret

    def map_scalars_to_colors(self, *args):
        """
        V.map_scalars_to_colors(DataArray) -> (int, ...)
        C++: unsigned char *MapScalarsToColors(DataArray *scalars)
        Map scalar values into color scalars.
        """
        my_args = deref_array(args, [['vtkDataArray']])
        ret = self._wrap_call(self._vtk_obj.MapScalarsToColors, *my_args)
        return ret

    def post_render(self, *args):
        """
        V.post_render(Renderer)
        C++: virtual void PostRender(Renderer *)
        Cleans up after the texture rendering to restore the state of the
        graphics context.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PostRender, *my_args)
        return ret

    def release_graphics_resources(self, *args):
        """
        V.release_graphics_resources(Window)
        C++: virtual void ReleaseGraphicsResources(Window *)
        Release any graphics resources that are being consumed by this
        texture. The parameter window could be used to determine which
        graphic resources to release.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReleaseGraphicsResources, *my_args)
        return ret

    def render(self, *args):
        """
        V.render(Renderer)
        C++: virtual void Render(Renderer *ren)
        Renders a texture map. It first checks the object's modified time
        to make sure the texture maps Input is valid, then it invokes the
        Load() method.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Render, *my_args)
        return ret

    _updateable_traits_ = \
    (('edge_clamp', 'GetEdgeClamp'), ('interpolate', 'GetInterpolate'),
    ('map_color_scalars_through_lookup_table',
    'GetMapColorScalarsThroughLookupTable'), ('premultiplied_alpha',
    'GetPremultipliedAlpha'), ('repeat', 'GetRepeat'),
    ('restrict_power_of2_image_smaller',
    'GetRestrictPowerOf2ImageSmaller'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('quality', 'GetQuality'),
    ('blending_mode', 'GetBlendingMode'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'edge_clamp', 'global_warning_display',
    'interpolate', 'map_color_scalars_through_lookup_table',
    'premultiplied_alpha', 'release_data_flag', 'repeat',
    'restrict_power_of2_image_smaller', 'quality', 'blending_mode',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Texture, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Texture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['edge_clamp', 'interpolate',
            'map_color_scalars_through_lookup_table', 'premultiplied_alpha',
            'repeat', 'restrict_power_of2_image_smaller'], ['quality'],
            ['blending_mode']),
            title='Edit Texture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Texture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


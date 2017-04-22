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

from tvtk.tvtk_classes.texture import Texture


class OpenGLTexture(Texture):
    """
    OpenGLTexture - open_gl texture map
    
    Superclass: Texture
    
    OpenGLTexture is a concrete implementation of the abstract class
    Texture. OpenGLTexture interfaces to the open_gl rendering
    library.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLTexture, obj, update, **traits)
    
    is_depth_texture = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Provide for specifying a format for the texture
        """
    )

    def _is_depth_texture_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIsDepthTexture,
                        self.is_depth_texture)

    def _get_texture_object(self):
        return wrap_vtk(self._vtk_obj.GetTextureObject())
    def _set_texture_object(self, arg):
        old_val = self._get_texture_object()
        self._wrap_call(self._vtk_obj.SetTextureObject,
                        deref_vtk(arg))
        self.trait_property_changed('texture_object', old_val, arg)
    texture_object = traits.Property(_get_texture_object, _set_texture_object, help=\
        """
        
        """
    )

    texture_type = traits.Int(3553, enter_set=True, auto_set=False, help=\
        """
        What type of texture map gl__texture__2d versus
        GL_TEXTURE_RECTANGLE
        """
    )

    def _texture_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureType,
                        self.texture_type)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input as a ImageData object.  This method is for
        backwards compatibility.
        """
    )

    def copy_tex_image(self, *args):
        """
        V.copy_tex_image(int, int, int, int)
        C++: void CopyTexImage(int x, int y, int width, int height)
        copy the renderers read buffer into this texture
        """
        ret = self._wrap_call(self._vtk_obj.CopyTexImage, *args)
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
    ('is_depth_texture', 'GetIsDepthTexture'), ('texture_type',
    'GetTextureType'), ('blending_mode', 'GetBlendingMode'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'edge_clamp', 'global_warning_display',
    'interpolate', 'map_color_scalars_through_lookup_table',
    'premultiplied_alpha', 'release_data_flag', 'repeat',
    'restrict_power_of2_image_smaller', 'quality', 'blending_mode',
    'is_depth_texture', 'progress_text', 'texture_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLTexture, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['edge_clamp', 'interpolate',
            'map_color_scalars_through_lookup_table', 'premultiplied_alpha',
            'repeat', 'restrict_power_of2_image_smaller'], ['quality'],
            ['blending_mode', 'is_depth_texture', 'texture_type']),
            title='Edit OpenGLTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


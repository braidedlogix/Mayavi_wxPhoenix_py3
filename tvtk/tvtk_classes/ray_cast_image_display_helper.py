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


class RayCastImageDisplayHelper(Object):
    """
    RayCastImageDisplayHelper - helper class that draws the image to
    the screen
    
    Superclass: Object
    
    This is a helper class for drawing images created from ray casting on
    the screen. This is the abstract device-independent superclass.
    
    @sa
    VolumeRayCastMapper UnstructuredGridVolumeRayCastMapper
    OpenGLRayCastImageDisplayHelper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRayCastImageDisplayHelper, obj, update, **traits)
    
    pre_multiplied_colors = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )

    def _pre_multiplied_colors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreMultipliedColors,
                        self.pre_multiplied_colors_)

    pixel_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set / Get the pixel scale to be applied to the image before
        display. Can be set to scale the incoming pixel values - for
        example the fixed point mapper uses the unsigned short API but
        with 15 bit values so needs a scale of 2.0.
        """
    )

    def _pixel_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPixelScale,
                        self.pixel_scale)

    def _get_pre_multiplied_colors_max_value(self):
        return self._vtk_obj.GetPreMultipliedColorsMaxValue()
    pre_multiplied_colors_max_value = traits.Property(_get_pre_multiplied_colors_max_value, help=\
        """
        
        """
    )

    def _get_pre_multiplied_colors_min_value(self):
        return self._vtk_obj.GetPreMultipliedColorsMinValue()
    pre_multiplied_colors_min_value = traits.Property(_get_pre_multiplied_colors_min_value, help=\
        """
        
        """
    )

    def release_graphics_resources(self, *args):
        """
        V.release_graphics_resources(Window)
        C++: virtual void ReleaseGraphicsResources(Window *)
        Derived class should implemen this if needed
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReleaseGraphicsResources, *my_args)
        return ret

    def render_texture(self, *args):
        """
        V.render_texture(Volume, Renderer, [int, int], [int, int],
            [int, int], [int, int], float, [int, ...])
        C++: virtual void RenderTexture(Volume *vol, Renderer *ren,
            int imageMemorySize[2], int imageViewportSize[2],
            int imageInUseSize[2], int imageOrigin[2],
            float requestedDepth, unsigned char *image)
        V.render_texture(Volume, Renderer, [int, int], [int, int],
            [int, int], [int, int], float, [int, ...])
        C++: virtual void RenderTexture(Volume *vol, Renderer *ren,
            int imageMemorySize[2], int imageViewportSize[2],
            int imageInUseSize[2], int imageOrigin[2],
            float requestedDepth, unsigned short *image)
        V.render_texture(Volume, Renderer, FixedPointRayCastImage,
             float)
        C++: virtual void RenderTexture(Volume *vol, Renderer *ren,
            FixedPointRayCastImage *image, float requestedDepth)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderTexture, *my_args)
        return ret

    _updateable_traits_ = \
    (('pre_multiplied_colors', 'GetPreMultipliedColors'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pixel_scale', 'GetPixelScale'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pre_multiplied_colors',
    'pixel_scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RayCastImageDisplayHelper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RayCastImageDisplayHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['pre_multiplied_colors'], [], ['pixel_scale']),
            title='Edit RayCastImageDisplayHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RayCastImageDisplayHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


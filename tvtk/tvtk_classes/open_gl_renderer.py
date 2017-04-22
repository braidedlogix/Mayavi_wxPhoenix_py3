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

from tvtk.tvtk_classes.renderer import Renderer


class OpenGLRenderer(Renderer):
    """
    OpenGLRenderer - open_gl renderer
    
    Superclass: Renderer
    
    OpenGLRenderer is a concrete implementation of the abstract class
    Renderer. OpenGLRenderer interfaces to the open_gl graphics
    library.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLRenderer, obj, update, **traits)
    
    def _get_depth_peeling_higher_layer(self):
        return self._vtk_obj.GetDepthPeelingHigherLayer()
    depth_peeling_higher_layer = traits.Property(_get_depth_peeling_higher_layer, help=\
        """
        Is rendering at translucent geometry stage using depth peeling
        and rendering a layer other than the first one? (Boolean value)
        If so, the uniform variables use_texture and Texture can be set.
        (Used by OpenGLProperty or OpenGLTexture)
        """
    )

    def have_apple_primitive_id_bug(self):
        """
        V.have_apple_primitive_id_bug() -> bool
        C++: bool HaveApplePrimitiveIdBug()
        Indicate if this system is subject to the apple/amd bug of not
        having a working gl_primitive_id
        """
        ret = self._vtk_obj.HaveApplePrimitiveIdBug()
        return ret
        

    def update_lights(self):
        """
        V.update_lights() -> int
        C++: int UpdateLights(void)
        Ask lights to load themselves into graphics pipeline.
        """
        ret = self._vtk_obj.UpdateLights()
        return ret
        

    _updateable_traits_ = \
    (('automatic_light_creation', 'GetAutomaticLightCreation'),
    ('backing_store', 'GetBackingStore'), ('draw', 'GetDraw'), ('erase',
    'GetErase'), ('interactive', 'GetInteractive'),
    ('light_follow_camera', 'GetLightFollowCamera'),
    ('preserve_color_buffer', 'GetPreserveColorBuffer'),
    ('preserve_depth_buffer', 'GetPreserveDepthBuffer'),
    ('textured_background', 'GetTexturedBackground'),
    ('two_sided_lighting', 'GetTwoSidedLighting'), ('use_depth_peeling',
    'GetUseDepthPeeling'), ('use_fxaa', 'GetUseFXAA'),
    ('use_hidden_line_removal', 'GetUseHiddenLineRemoval'),
    ('use_shadows', 'GetUseShadows'), ('gradient_background',
    'GetGradientBackground'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('allocated_render_time', 'GetAllocatedRenderTime'), ('ambient',
    'GetAmbient'), ('clipping_range_expansion',
    'GetClippingRangeExpansion'), ('layer', 'GetLayer'),
    ('maximum_number_of_peels', 'GetMaximumNumberOfPeels'),
    ('near_clipping_plane_tolerance', 'GetNearClippingPlaneTolerance'),
    ('occlusion_ratio', 'GetOcclusionRatio'), ('aspect', 'GetAspect'),
    ('background', 'GetBackground'), ('background2', 'GetBackground2'),
    ('current_pick_id', 'GetCurrentPickId'), ('display_point',
    'GetDisplayPoint'), ('pixel_aspect', 'GetPixelAspect'), ('view_point',
    'GetViewPoint'), ('viewport', 'GetViewport'), ('world_point',
    'GetWorldPoint'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['automatic_light_creation', 'backing_store', 'debug', 'draw',
    'erase', 'global_warning_display', 'gradient_background',
    'interactive', 'light_follow_camera', 'preserve_color_buffer',
    'preserve_depth_buffer', 'textured_background', 'two_sided_lighting',
    'use_depth_peeling', 'use_fxaa', 'use_hidden_line_removal',
    'use_shadows', 'allocated_render_time', 'ambient', 'aspect',
    'background', 'background2', 'clipping_range_expansion',
    'current_pick_id', 'display_point', 'layer',
    'maximum_number_of_peels', 'near_clipping_plane_tolerance',
    'occlusion_ratio', 'pixel_aspect', 'view_point', 'viewport',
    'world_point'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLRenderer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLRenderer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic_light_creation', 'backing_store', 'draw', 'erase',
            'gradient_background', 'interactive', 'light_follow_camera',
            'preserve_color_buffer', 'preserve_depth_buffer',
            'textured_background', 'two_sided_lighting', 'use_depth_peeling',
            'use_fxaa', 'use_hidden_line_removal', 'use_shadows'], [],
            ['allocated_render_time', 'ambient', 'aspect', 'background',
            'background2', 'clipping_range_expansion', 'current_pick_id',
            'display_point', 'layer', 'maximum_number_of_peels',
            'near_clipping_plane_tolerance', 'occlusion_ratio', 'pixel_aspect',
            'view_point', 'viewport', 'world_point']),
            title='Edit OpenGLRenderer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLRenderer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


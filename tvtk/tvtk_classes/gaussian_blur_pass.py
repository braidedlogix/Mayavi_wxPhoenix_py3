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

from tvtk.tvtk_classes.image_processing_pass import ImageProcessingPass


class GaussianBlurPass(ImageProcessingPass):
    """
    GaussianBlurPass - Implement a post-processing Gaussian blur
    render pass.
    
    Superclass: ImageProcessingPass
    
    Blur the image renderered by its delegate. Blurring uses a Gaussian
    low-pass filter with a 5x5 kernel.
    
    This pass expects an initialized depth buffer and color buffer.
    Initialized buffers means they have been cleared with farest z-value
    and background color/gradient/transparent color. An opaque pass may
    have been performed right after the initialization.
    
    The delegate is used once.
    
    Its delegate is usually set to a CameraPass or to a
    post-processing pass.
    
    This pass requires a open_gl context that supports texture objects
    (TO), framebuffer objects (FBO) and GLSL. If not, it will emit an
    error message and will render its delegate and return.
    
    @par Implementation: As the filter is separable, it first blurs the
    image horizontally and then vertically. This reduces the number of
    texture sampling to 5 per pass. In addition, as texture sampling can
    already blend texel values in linear mode, by adjusting the texture
    coordinate accordingly, only 3 texture sampling are actually
    necessary. Reference: open_gl Bloom Toturial by Philip Rideout,
    section Exploit Hardware Filtering 
    http://prideout.net/bloom/index.php#Sneaky
    
    @sa
    RenderPass
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGaussianBlurPass, obj, update, **traits)
    
    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GaussianBlurPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GaussianBlurPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit GaussianBlurPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GaussianBlurPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


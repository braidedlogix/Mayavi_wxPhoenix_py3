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


class FXAAOptions(Object):
    """
    FXAAOptions - Configuration for FXAA implementations.
    
    Superclass: Object
    
    This class encapsulates the settings for OpenGLFXAAFilter.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFXAAOptions, obj, update, **traits)
    
    use_high_quality_endpoints = tvtk_base.true_bool_trait(help=\
        """
        Use an improved edge endpoint detection algorithm.
        
        * If true, a modified edge endpoint detection algorithm is used
          that requires
        * more texture lookups, but will properly detect aliased
          single-pixel lines.
        
        * If false, the edge endpoint algorithm proposed by NVIDIA will
          by used. This
        * algorithm is faster (fewer lookups), but will fail to detect
          endpoints of
        * single pixel edge steps.
        
        * Default setting is true.
        """
    )

    def _use_high_quality_endpoints_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseHighQualityEndpoints,
                        self.use_high_quality_endpoints_)

    endpoint_search_iterations = traits.Trait(12, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the number of iterations for the endpoint search algorithm.
        Increasing this value will increase runtime, but also properly
        detect longer edges. The current implementation steps one pixel
        in both the positive and negative directions per iteration. The
        default value is 12, which will resolve endpoints of edges < 25
        pixels long (2 * 12 + 1).
        """
    )

    def _endpoint_search_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndpointSearchIterations,
                        self.endpoint_search_iterations)

    hard_contrast_threshold = traits.Trait(0.0625, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Similar to relative_contrast_threshold, but not scaled by the
        maximum luminosity.
        
        * If the contrast of the current pixel and it's 4 immediate NSWE
          neighbors is
        * less than hard_contrast_threshold, the pixel is not considered
          aliased and
        * will not be affected by FXAA.
        
        * Suggested settings:
        * - 1/32: Visible limit
        * - 1/16: High quality (default)
        * - 1/12: Upper limit (start of visible unfiltered edges)
        """
    )

    def _hard_contrast_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHardContrastThreshold,
                        self.hard_contrast_threshold)

    relative_contrast_threshold = traits.Trait(0.125, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Threshold for applying FXAA to a pixel, relative to the maximum
        luminosity of its 4 immediate neighbors.
        
        * The luminosity of the current pixel and it's NSWE neighbors is
          computed.
        * The maximum luminosity and luminosity range (contrast) of all 5
        pixels is
        * found. If the contrast is less than relative_contrast_threshold *
        max_lum,
        * the pixel is not considered aliased and will not be affected by
        FXAA.
        
        * Suggested settings:
        * - 1/3: Too little
        * - 1/4: Low quality
        * - 1/8: High quality (default)
        * - 1/16: Overkill
        """
    )

    def _relative_contrast_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRelativeContrastThreshold,
                        self.relative_contrast_threshold)

    subpixel_blend_limit = traits.Trait(0.75, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Subpixel aliasing is corrected by applying a lowpass filter to
        the current pixel. This is implemented by blending an average of
        the 3x3 neighborhood around the pixel into the final result. The
        amount of blending is determined by comparing the detected amount
        of subpixel aliasing to the total contrasting of the CNSWE
        pixels:
        
        * subpixel_blending = abs(lum_c - lum_ave_nswe) / (lum_max_cnswe -
          lum_min_cnswe)
        
        * This parameter sets an upper limit to the amount of subpixel
          blending to
        * prevent the image from simply getting blurred.
        
        * Suggested settings:
        * - 1/2: Low amount of blending.
        * - 3/4: Medium amount of blending (default)
        * - 7/8: High amount of blending.
        * - 1: Maximum amount of blending.
        """
    )

    def _subpixel_blend_limit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubpixelBlendLimit,
                        self.subpixel_blend_limit)

    subpixel_contrast_threshold = traits.Trait(0.25, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Minimum amount of subpixel aliasing required for subpixel
        antialiasing to be applied.
        
        * Subpixel aliasing is corrected by applying a lowpass filter to
          the current
        * pixel. This is implemented by blending an average of the 3x3
          neighborhood
        * around the pixel into the final result. The amount of blending
          is
        * determined by comparing the detected amount of subpixel
          aliasing to the
        * total contrasting of the CNSWE pixels:
        
        * subpixel_blending = abs(lum_c - lum_ave_nswe) / (lum_max_cnswe -
          lum_min_cnswe)
        
        * If subpixel_blending is less than this threshold, no lowpass
          blending will
        * occur.
        
        * Suggested settings:
        * - 1/2: Low subpixel aliasing removal
        * - 1/3: Medium subpixel aliasing removal
        * - 1/4: Default subpixel aliasing removal
        * - 1/8: High subpixel aliasing removal
        * - 0: Complete subpixel aliasing removal
        """
    )

    def _subpixel_contrast_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubpixelContrastThreshold,
                        self.subpixel_contrast_threshold)

    _updateable_traits_ = \
    (('use_high_quality_endpoints', 'GetUseHighQualityEndpoints'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('endpoint_search_iterations',
    'GetEndpointSearchIterations'), ('hard_contrast_threshold',
    'GetHardContrastThreshold'), ('relative_contrast_threshold',
    'GetRelativeContrastThreshold'), ('subpixel_blend_limit',
    'GetSubpixelBlendLimit'), ('subpixel_contrast_threshold',
    'GetSubpixelContrastThreshold'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'use_high_quality_endpoints',
    'endpoint_search_iterations', 'hard_contrast_threshold',
    'relative_contrast_threshold', 'subpixel_blend_limit',
    'subpixel_contrast_threshold'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FXAAOptions, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FXAAOptions properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_high_quality_endpoints'], [],
            ['endpoint_search_iterations', 'hard_contrast_threshold',
            'relative_contrast_threshold', 'subpixel_blend_limit',
            'subpixel_contrast_threshold']),
            title='Edit FXAAOptions properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FXAAOptions properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


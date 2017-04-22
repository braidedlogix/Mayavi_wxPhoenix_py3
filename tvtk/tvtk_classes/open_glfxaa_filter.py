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


class OpenGLFXAAFilter(Object):
    """
    OpenGLFXAAFilter - Perform FXAA antialiasing on the current
    framebuffer.
    
    Superclass: Object
    
    Call Execute() to run a FXAA antialiasing pass on the current open_gl
    framebuffer. See method documentation for tunable parameters.
    
    Based on the following implementation and description:
    
    Whitepaper:
    http://developer.download.nvidia.com/assets/gamedev/files/sdk/11/FXAA_
    white_paper.pdf
    
    Sample implementation:
    https://github.com/_nvidia_game_works/_graphics_samples/blob/master/samples
    /es3-kepler/FXAA/FXAA3_11.h
    
    TODO there are currently some "banding" artifacts on some edges,
    particularly single pixel lines. These seem to be caused by using a
    linear RGB input, rather than a gamma-correct s_rgb input. Future work
    should combine this pass with a gamma correction pass to correct
    this. Bonus points for precomputing luminosity into the s_rgb's alpha
    channel to save cycles in the FXAA shader!
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLFXAAFilter, obj, update, **traits)
    
    use_high_quality_endpoints = tvtk_base.true_bool_trait(help=\
        """
        Parameter for tuning the FXAA implementation. See FXAAOptions
        for details and suggested values.
        """
    )

    def _use_high_quality_endpoints_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseHighQualityEndpoints,
                        self.use_high_quality_endpoints_)

    debug_option_value = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Parameter for tuning the FXAA implementation. See FXAAOptions
        for details and suggested values.
        """
    )

    def _debug_option_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDebugOptionValue,
                        self.debug_option_value)

    endpoint_search_iterations = traits.Trait(12, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Parameter for tuning the FXAA implementation. See FXAAOptions
        for details and suggested values.
        """
    )

    def _endpoint_search_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndpointSearchIterations,
                        self.endpoint_search_iterations)

    hard_contrast_threshold = traits.Trait(0.0625, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Parameter for tuning the FXAA implementation. See FXAAOptions
        for details and suggested values.
        """
    )

    def _hard_contrast_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHardContrastThreshold,
                        self.hard_contrast_threshold)

    relative_contrast_threshold = traits.Trait(0.125, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Parameter for tuning the FXAA implementation. See FXAAOptions
        for details and suggested values.
        """
    )

    def _relative_contrast_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRelativeContrastThreshold,
                        self.relative_contrast_threshold)

    subpixel_blend_limit = traits.Trait(0.75, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Parameter for tuning the FXAA implementation. See FXAAOptions
        for details and suggested values.
        """
    )

    def _subpixel_blend_limit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubpixelBlendLimit,
                        self.subpixel_blend_limit)

    subpixel_contrast_threshold = traits.Trait(0.25, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Parameter for tuning the FXAA implementation. See FXAAOptions
        for details and suggested values.
        """
    )

    def _subpixel_contrast_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubpixelContrastThreshold,
                        self.subpixel_contrast_threshold)

    def execute(self, *args):
        """
        V.execute(OpenGLRenderer)
        C++: void Execute(OpenGLRenderer *ren)
        Perform FXAA on the current render buffer in ren.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Execute, *my_args)
        return ret

    def release_graphics_resources(self):
        """
        V.release_graphics_resources()
        C++: void ReleaseGraphicsResources()
        Release all open_gl state.
        """
        ret = self._vtk_obj.ReleaseGraphicsResources()
        return ret
        

    def update_configuration(self, *args):
        """
        V.update_configuration(FXAAOptions)
        C++: void UpdateConfiguration(FXAAOptions *opts)
        Copy the configuration values from opts into this filter. Note
        that this copies the configuration values from opts -- it does
        not save theopts pointer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UpdateConfiguration, *my_args)
        return ret

    _updateable_traits_ = \
    (('use_high_quality_endpoints', 'GetUseHighQualityEndpoints'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('debug_option_value',
    'GetDebugOptionValue'), ('endpoint_search_iterations',
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
    'debug_option_value', 'endpoint_search_iterations',
    'hard_contrast_threshold', 'relative_contrast_threshold',
    'subpixel_blend_limit', 'subpixel_contrast_threshold'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLFXAAFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLFXAAFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_high_quality_endpoints'], [], ['debug_option_value',
            'endpoint_search_iterations', 'hard_contrast_threshold',
            'relative_contrast_threshold', 'subpixel_blend_limit',
            'subpixel_contrast_threshold']),
            title='Edit OpenGLFXAAFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLFXAAFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


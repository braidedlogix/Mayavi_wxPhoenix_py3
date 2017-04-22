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

from tvtk.tvtk_classes.depth_image_processing_pass import DepthImageProcessingPass


class DepthOfFieldPass(DepthImageProcessingPass):
    """
    DepthOfFieldPass - Implement a post-processing DOF blur pass.
    
    Superclass: DepthImageProcessingPass
    
    Currently only does behind the focal plane
    
    This pass expects an initialized depth buffer and color buffer.
    Initialized buffers means they have been cleared with farest z-value
    and background color/gradient/transparent color.
    
    The delegate is used once.
    
    Its delegate is usually set to a CameraPass or to a
    post-processing pass.
    
    @par Implementation: As the filter is separable, it first blurs the
    image horizontally and then vertically. This reduces the number of
    texture samples
    
    @sa
    RenderPass
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDepthOfFieldPass, obj, update, **traits)
    
    automatic_focal_distance = tvtk_base.true_bool_trait(help=\
        """
        Use automatic focal distance calculation, this is on by default
        When on the center of the viewport will always be in focus
        regardless of where the focal point is.
        """
    )

    def _automatic_focal_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutomaticFocalDistance,
                        self.automatic_focal_distance_)

    _updateable_traits_ = \
    (('automatic_focal_distance', 'GetAutomaticFocalDistance'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['automatic_focal_distance', 'debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DepthOfFieldPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DepthOfFieldPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic_focal_distance'], [], []),
            title='Edit DepthOfFieldPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DepthOfFieldPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


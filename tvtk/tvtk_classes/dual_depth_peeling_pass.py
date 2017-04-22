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

from tvtk.tvtk_classes.depth_peeling_pass import DepthPeelingPass


class DualDepthPeelingPass(DepthPeelingPass):
    """
    DualDepthPeelingPass - Implements the dual depth peeling algorithm.
    
    Superclass: DepthPeelingPass
    
    Dual depth peeling is an augmentatation of the standard depth peeling
    algorithm that peels two layers (front and back) for each render
    pass. The technique is described in "Order independent transparency
    with dual depth peeling" (February 2008) by L. Bavoil, K. Myers.
    
    The pass occurs in several stages:
    
    1. Copy the current (opaque geometry) depth buffer into a texture.
    2. Initialize the min-max depth buffer from the opaque depth texture
       and the translucent geometry.
    3. Peel the nearest and farthest fragments: 3a. Blend fragments that
       match the nearest depth of the min-max depth buffer into the front
    buffer. 3b. Write the far depth fragments into a temporary buffer.
       3c. Extract the next set of min/max depth values for the next
       peel. 3d. Blend the temporary far fragment texture (3b) into an
       accumulation texture. 3e. Go back to 3a and repeat until the
       maximum number of peels is met, or the desired occlusion ratio is
       satisfied.
    4. If the occlusion ratio != 0 (i.e. we hit the maximum number of
       peels before finishing), alpha blend the remaining fragments
       in-between the near and far accumulation textures.
    5. Blend all accumulation buffers over the opaque color buffer to
       produce the final image.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDualDepthPeelingPass, obj, update, **traits)
    
    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('maximum_number_of_peels',
    'GetMaximumNumberOfPeels'), ('occlusion_ratio', 'GetOcclusionRatio'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'maximum_number_of_peels',
    'occlusion_ratio'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DualDepthPeelingPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DualDepthPeelingPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['maximum_number_of_peels', 'occlusion_ratio']),
            title='Edit DualDepthPeelingPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DualDepthPeelingPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


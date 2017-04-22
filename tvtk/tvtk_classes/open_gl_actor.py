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

from tvtk.tvtk_classes.actor import Actor


class OpenGLActor(Actor):
    """
    OpenGLActor - open_gl actor
    
    Superclass: Actor
    
    OpenGLActor is a concrete implementation of the abstract class
    Actor. OpenGLActor interfaces to the open_gl rendering library.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLActor, obj, update, **traits)
    
    def gl_depth_mask_override(self):
        """
        V.gl_depth_mask_override() -> InformationIntegerKey
        C++: static InformationIntegerKey *GLDepthMaskOverride()
        If this key is set in get_property_keys(), the gl_depth_mask will be
        adjusted prior to rendering translucent objects. This is useful
        for e.g. depth peeling.
        
        * If get_is_opaque() == true, the depth mask is always enabled,
          regardless of
        * this key. Otherwise, the depth mask is disabled for default
          alpha blending
        * unless this key is set.
        
        * If this key is set, the integer value has the following
          meanings:
        * 0: gl_depth_mask(_gl__false)
        * 1: gl_depth_mask(_gl__true)
        * Anything else: No change to depth mask.
        """
        ret = wrap_vtk(self._vtk_obj.GLDepthMaskOverride())
        return ret
        

    _updateable_traits_ = \
    (('force_opaque', 'GetForceOpaque'), ('force_translucent',
    'GetForceTranslucent'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('orientation', 'GetOrientation'),
    ('origin', 'GetOrigin'), ('position', 'GetPosition'), ('scale',
    'GetScale'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'force_opaque', 'force_translucent',
    'global_warning_display', 'pickable', 'use_bounds', 'visibility',
    'estimated_render_time', 'orientation', 'origin', 'position',
    'render_time_multiplier', 'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['force_opaque', 'force_translucent', 'use_bounds',
            'visibility'], [], ['estimated_render_time', 'orientation', 'origin',
            'position', 'render_time_multiplier', 'scale']),
            title='Edit OpenGLActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.prop import Prop


class ContextActor(Prop):
    """
    ContextActor - provides a Prop derived object.
    
    Superclass: Prop
    
    This object provides the entry point for the ContextScene to be
    rendered in a Renderer. Uses the render_overlay pass to render the
    2d ContextScene.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContextActor, obj, update, **traits)
    
    def _get_scene(self):
        return wrap_vtk(self._vtk_obj.GetScene())
    def _set_scene(self, arg):
        old_val = self._get_scene()
        self._wrap_call(self._vtk_obj.SetScene,
                        deref_vtk(arg))
        self.trait_property_changed('scene', old_val, arg)
    scene = traits.Property(_get_scene, _set_scene, help=\
        """
        Get the chart object for the actor.
        """
    )

    def _get_context(self):
        return wrap_vtk(self._vtk_obj.GetContext())
    context = traits.Property(_get_context, help=\
        """
        Get the Context2D for the actor.
        """
    )

    _updateable_traits_ = \
    (('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'estimated_render_time',
    'render_time_multiplier'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContextActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ContextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_bounds', 'visibility'], [], ['estimated_render_time',
            'render_time_multiplier']),
            title='Edit ContextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


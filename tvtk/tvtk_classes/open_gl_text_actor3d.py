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

from tvtk.tvtk_classes.text_actor3d import TextActor3D


class OpenGLTextActor3D(TextActor3D):
    """
    OpenGLTextActor3D - open_gl2 override for TextActor3D.
    
    Superclass: TextActor3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLTextActor3D, obj, update, **traits)
    
    def _get_input(self):
        return self._vtk_obj.GetInput()
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        arg)
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set the text string to be displayed.
        """
    )

    _updateable_traits_ = \
    (('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('orientation', 'GetOrientation'),
    ('origin', 'GetOrigin'), ('position', 'GetPosition'), ('scale',
    'GetScale'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'estimated_render_time', 'orientation',
    'origin', 'position', 'render_time_multiplier', 'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLTextActor3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLTextActor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_bounds', 'visibility'], [], ['estimated_render_time',
            'orientation', 'origin', 'position', 'render_time_multiplier',
            'scale']),
            title='Edit OpenGLTextActor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLTextActor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


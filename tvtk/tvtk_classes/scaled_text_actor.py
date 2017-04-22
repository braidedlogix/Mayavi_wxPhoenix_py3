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

from tvtk.tvtk_classes.text_actor import TextActor


class ScaledTextActor(TextActor):
    """
    ScaledTextActor - create text that will scale as needed
    
    Superclass: TextActor
    
    ScaledTextActor is deprecated. New code should use TextActor
    with the Scaled = true option.
    
    @sa
    TextActor Actor2D TextMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScaledTextActor, obj, update, **traits)
    
    def _get_input(self):
        return self._vtk_obj.GetInput()
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        arg)
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set the text string to be displayed. "\n" is recognized as a
        carriage return/linefeed (line separator). The characters must be
        in the UTF-8 encoding. Convenience method to the underlying
        mapper
        """
    )

    _updateable_traits_ = \
    (('use_border_align', 'GetUseBorderAlign'), ('dragable',
    'GetDragable'), ('pickable', 'GetPickable'), ('use_bounds',
    'GetUseBounds'), ('visibility', 'GetVisibility'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('text_scale_mode', 'GetTextScaleMode'), ('alignment_point',
    'GetAlignmentPoint'), ('maximum_line_height', 'GetMaximumLineHeight'),
    ('minimum_size', 'GetMinimumSize'), ('orientation', 'GetOrientation'),
    ('height', 'GetHeight'), ('layer_number', 'GetLayerNumber'),
    ('position', 'GetPosition'), ('position2', 'GetPosition2'), ('width',
    'GetWidth'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_border_align', 'use_bounds', 'visibility', 'text_scale_mode',
    'alignment_point', 'estimated_render_time', 'height', 'layer_number',
    'maximum_line_height', 'minimum_size', 'orientation', 'position',
    'position2', 'render_time_multiplier', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScaledTextActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ScaledTextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_border_align', 'use_bounds', 'visibility'],
            ['text_scale_mode'], ['alignment_point', 'estimated_render_time',
            'height', 'layer_number', 'maximum_line_height', 'minimum_size',
            'orientation', 'position', 'position2', 'render_time_multiplier',
            'width']),
            title='Edit ScaledTextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScaledTextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


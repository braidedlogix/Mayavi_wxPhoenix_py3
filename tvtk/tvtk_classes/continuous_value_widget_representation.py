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

from tvtk.tvtk_classes.widget_representation import WidgetRepresentation


class ContinuousValueWidgetRepresentation(WidgetRepresentation):
    """
    ContinuousValueWidgetRepresentation - provide the representation
    for a continuous value
    
    Superclass: WidgetRepresentation
    
    This class is used mainly as a superclass for continuous value
    widgets
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContinuousValueWidgetRepresentation, obj, update, **traits)
    
    value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValue,
                        self.value)

    _updateable_traits_ = \
    (('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('value', 'GetValue'), ('handle_size',
    'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'picking_managed', 'use_bounds', 'visibility',
    'estimated_render_time', 'handle_size', 'place_factor',
    'render_time_multiplier', 'value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContinuousValueWidgetRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ContinuousValueWidgetRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['need_to_render', 'picking_managed', 'use_bounds',
            'visibility'], [], ['estimated_render_time', 'handle_size',
            'place_factor', 'render_time_multiplier', 'value']),
            title='Edit ContinuousValueWidgetRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContinuousValueWidgetRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


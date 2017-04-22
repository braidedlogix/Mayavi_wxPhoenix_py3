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

from tvtk.tvtk_classes.border_representation import BorderRepresentation


class ProgressBarRepresentation(BorderRepresentation):
    """
    ProgressBarRepresentation - represent a ProgressBarWidget
    
    Superclass: BorderRepresentation
    
    This class is used to represent a ProgressBarWidget.
    
    @sa
    ProgressBarWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProgressBarRepresentation, obj, update, **traits)
    
    draw_background = tvtk_base.true_bool_trait(help=\
        """
        Set/Get background visibility Default is off
        """
    )

    def _draw_background_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawBackground,
                        self.draw_background_)

    background_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )

    def _background_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundColor,
                        self.background_color, False)

    progress_bar_color = tvtk_base.vtk_color_trait((0.0, 1.0, 0.0), help=\
        """
        
        """
    )

    def _progress_bar_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProgressBarColor,
                        self.progress_bar_color, False)

    progress_rate = traits.Trait(0.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the progress rate of the progress bar, between 0 and 1
        default is 0
        """
    )

    def _progress_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProgressRate,
                        self.progress_rate)

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    property = traits.Property(_get_property, help=\
        """
        By obtaining this property you can specify the properties of the
        representation.
        """
    )

    _updateable_traits_ = \
    (('draw_background', 'GetDrawBackground'), ('moving', 'GetMoving'),
    ('proportional_resize', 'GetProportionalResize'), ('need_to_render',
    'GetNeedToRender'), ('picking_managed', 'GetPickingManaged'),
    ('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('show_border', 'GetShowBorder'),
    ('background_color', 'GetBackgroundColor'), ('progress_bar_color',
    'GetProgressBarColor'), ('progress_rate', 'GetProgressRate'),
    ('maximum_size', 'GetMaximumSize'), ('minimum_size',
    'GetMinimumSize'), ('position', 'GetPosition'), ('position2',
    'GetPosition2'), ('show_horizontal_border',
    'GetShowHorizontalBorder'), ('show_vertical_border',
    'GetShowVerticalBorder'), ('tolerance', 'GetTolerance'),
    ('handle_size', 'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'draw_background', 'global_warning_display',
    'moving', 'need_to_render', 'pickable', 'picking_managed',
    'proportional_resize', 'use_bounds', 'visibility', 'show_border',
    'background_color', 'estimated_render_time', 'handle_size',
    'maximum_size', 'minimum_size', 'place_factor', 'position',
    'position2', 'progress_bar_color', 'progress_rate',
    'render_time_multiplier', 'show_horizontal_border',
    'show_vertical_border', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProgressBarRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ProgressBarRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['draw_background', 'moving', 'need_to_render',
            'picking_managed', 'proportional_resize', 'use_bounds', 'visibility'],
            ['show_border'], ['background_color', 'estimated_render_time',
            'handle_size', 'maximum_size', 'minimum_size', 'place_factor',
            'position', 'position2', 'progress_bar_color', 'progress_rate',
            'render_time_multiplier', 'show_horizontal_border',
            'show_vertical_border', 'tolerance']),
            title='Edit ProgressBarRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProgressBarRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


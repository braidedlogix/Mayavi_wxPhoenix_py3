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

from tvtk.tvtk_classes.tree_area_view import TreeAreaView


class TreeMapView(TreeAreaView):
    """
    TreeMapView - Displays a tree as a tree map.
    
    Superclass: TreeAreaView
    
    TreeMapView shows a Tree in a tree map, where each vertex in
    the tree is represented by a box.  Child boxes are contained within
    the parent box, and may be colored and sized by various parameters.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeMapView, obj, update, **traits)
    
    def get_font_size_range(self, *args):
        """
        V.get_font_size_range([int, int, int])
        C++: virtual void GetFontSizeRange(int range[3])
        The sizes of the fonts used for labeling.
        """
        ret = self._wrap_call(self._vtk_obj.GetFontSizeRange, *args)
        return ret

    def set_font_size_range(self, *args):
        """
        V.set_font_size_range(int, int, int)
        C++: virtual void SetFontSizeRange(const int maxSize,
            const int minSize, const int delta=4)
        The sizes of the fonts used for labeling.
        """
        ret = self._wrap_call(self._vtk_obj.SetFontSizeRange, *args)
        return ret

    def set_layout_strategy_to_box(self):
        """
        V.set_layout_strategy_to_box()
        C++: virtual void SetLayoutStrategyToBox()
        Sets the treemap layout strategy
        """
        ret = self._vtk_obj.SetLayoutStrategyToBox()
        return ret
        

    def set_layout_strategy_to_slice_and_dice(self):
        """
        V.set_layout_strategy_to_slice_and_dice()
        C++: virtual void SetLayoutStrategyToSliceAndDice()
        Sets the treemap layout strategy
        """
        ret = self._vtk_obj.SetLayoutStrategyToSliceAndDice()
        return ret
        

    def set_layout_strategy_to_squarify(self):
        """
        V.set_layout_strategy_to_squarify()
        C++: virtual void SetLayoutStrategyToSquarify()
        Sets the treemap layout strategy
        """
        ret = self._vtk_obj.SetLayoutStrategyToSquarify()
        return ret
        

    _updateable_traits_ = \
    (('area_label_visibility', 'GetAreaLabelVisibility'), ('color_areas',
    'GetColorAreas'), ('color_edges', 'GetColorEdges'),
    ('edge_label_visibility', 'GetEdgeLabelVisibility'),
    ('use_rectangular_coordinates', 'GetUseRectangularCoordinates'),
    ('display_hover_text', 'GetDisplayHoverText'),
    ('render_on_mouse_move', 'GetRenderOnMouseMove'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('label_placement_mode', 'GetLabelPlacementMode'),
    ('label_render_mode', 'GetLabelRenderMode'), ('selection_mode',
    'GetSelectionMode'), ('area_color_array_name',
    'GetAreaColorArrayName'), ('area_hover_array_name',
    'GetAreaHoverArrayName'), ('area_label_array_name',
    'GetAreaLabelArrayName'), ('area_label_font_size',
    'GetAreaLabelFontSize'), ('area_size_array_name',
    'GetAreaSizeArrayName'), ('bundling_strength', 'GetBundlingStrength'),
    ('edge_color_array_name', 'GetEdgeColorArrayName'),
    ('edge_label_array_name', 'GetEdgeLabelArrayName'),
    ('edge_label_font_size', 'GetEdgeLabelFontSize'),
    ('edge_scalar_bar_visibility', 'GetEdgeScalarBarVisibility'),
    ('label_priority_array_name', 'GetLabelPriorityArrayName'),
    ('shrink_percentage', 'GetShrinkPercentage'), ('icon_size',
    'GetIconSize'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['area_label_visibility', 'color_areas', 'color_edges', 'debug',
    'display_hover_text', 'edge_label_visibility',
    'global_warning_display', 'render_on_mouse_move',
    'use_rectangular_coordinates', 'label_placement_mode',
    'label_render_mode', 'selection_mode', 'area_color_array_name',
    'area_hover_array_name', 'area_label_array_name',
    'area_label_font_size', 'area_size_array_name', 'bundling_strength',
    'edge_color_array_name', 'edge_label_array_name',
    'edge_label_font_size', 'edge_scalar_bar_visibility', 'icon_size',
    'label_priority_array_name', 'shrink_percentage'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeMapView, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeMapView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['area_label_visibility', 'color_areas', 'color_edges',
            'display_hover_text', 'edge_label_visibility', 'render_on_mouse_move',
            'use_rectangular_coordinates'], ['label_placement_mode',
            'label_render_mode', 'selection_mode'], ['area_color_array_name',
            'area_hover_array_name', 'area_label_array_name',
            'area_label_font_size', 'area_size_array_name', 'bundling_strength',
            'edge_color_array_name', 'edge_label_array_name',
            'edge_label_font_size', 'edge_scalar_bar_visibility', 'icon_size',
            'label_priority_array_name', 'shrink_percentage']),
            title='Edit TreeMapView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeMapView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


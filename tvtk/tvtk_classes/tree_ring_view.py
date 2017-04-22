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


class TreeRingView(TreeAreaView):
    """
    TreeRingView - Displays a tree in concentric rings.
    
    Superclass: TreeAreaView
    
    Accepts a graph and a hierarchy - currently a tree - and provides a
    hierarchy-aware display.  Currently, this means displaying the
    hierarchy using a tree ring layout, then rendering the graph vertices
    as leaves of the tree with curved graph edges between leaves.
    
    .SEE ALSO GraphLayoutView
    
    @par Thanks: Thanks to Jason Shepherd for implementing this class
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeRingView, obj, update, **traits)
    
    root_at_center = tvtk_base.false_bool_trait(help=\
        """
        Sets whether the root is at the center or around the outside.
        """
    )

    def _root_at_center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRootAtCenter,
                        self.root_at_center_)

    interior_log_spacing_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the log spacing factor for the invisible interior tree used
        for routing edges of the overlaid graph.
        """
    )

    def _interior_log_spacing_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteriorLogSpacingValue,
                        self.interior_log_spacing_value)

    interior_radius = traits.Float(6.0, enter_set=True, auto_set=False, help=\
        """
        Set the interior radius of the tree (i.e. the size of the "hole"
        in the center).
        """
    )

    def _interior_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteriorRadius,
                        self.interior_radius)

    layer_thickness = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the thickness of each layer.
        """
    )

    def _layer_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLayerThickness,
                        self.layer_thickness)

    def set_root_angles(self, *args):
        """
        V.set_root_angles(float, float)
        C++: void SetRootAngles(double start, double end)
        Set the root angles for laying out the hierarchy.
        """
        ret = self._wrap_call(self._vtk_obj.SetRootAngles, *args)
        return ret

    _updateable_traits_ = \
    (('root_at_center', 'GetRootAtCenter'), ('area_label_visibility',
    'GetAreaLabelVisibility'), ('color_areas', 'GetColorAreas'),
    ('color_edges', 'GetColorEdges'), ('edge_label_visibility',
    'GetEdgeLabelVisibility'), ('use_rectangular_coordinates',
    'GetUseRectangularCoordinates'), ('display_hover_text',
    'GetDisplayHoverText'), ('render_on_mouse_move',
    'GetRenderOnMouseMove'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('label_placement_mode', 'GetLabelPlacementMode'),
    ('label_render_mode', 'GetLabelRenderMode'), ('selection_mode',
    'GetSelectionMode'), ('interior_log_spacing_value',
    'GetInteriorLogSpacingValue'), ('interior_radius',
    'GetInteriorRadius'), ('layer_thickness', 'GetLayerThickness'),
    ('area_color_array_name', 'GetAreaColorArrayName'),
    ('area_hover_array_name', 'GetAreaHoverArrayName'),
    ('area_label_array_name', 'GetAreaLabelArrayName'),
    ('area_label_font_size', 'GetAreaLabelFontSize'),
    ('area_size_array_name', 'GetAreaSizeArrayName'),
    ('bundling_strength', 'GetBundlingStrength'),
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
    'global_warning_display', 'render_on_mouse_move', 'root_at_center',
    'use_rectangular_coordinates', 'label_placement_mode',
    'label_render_mode', 'selection_mode', 'area_color_array_name',
    'area_hover_array_name', 'area_label_array_name',
    'area_label_font_size', 'area_size_array_name', 'bundling_strength',
    'edge_color_array_name', 'edge_label_array_name',
    'edge_label_font_size', 'edge_scalar_bar_visibility', 'icon_size',
    'interior_log_spacing_value', 'interior_radius',
    'label_priority_array_name', 'layer_thickness', 'shrink_percentage'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeRingView, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeRingView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['area_label_visibility', 'color_areas', 'color_edges',
            'display_hover_text', 'edge_label_visibility', 'render_on_mouse_move',
            'root_at_center', 'use_rectangular_coordinates'],
            ['label_placement_mode', 'label_render_mode', 'selection_mode'],
            ['area_color_array_name', 'area_hover_array_name',
            'area_label_array_name', 'area_label_font_size',
            'area_size_array_name', 'bundling_strength', 'edge_color_array_name',
            'edge_label_array_name', 'edge_label_font_size',
            'edge_scalar_bar_visibility', 'icon_size',
            'interior_log_spacing_value', 'interior_radius',
            'label_priority_array_name', 'layer_thickness', 'shrink_percentage']),
            title='Edit TreeRingView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeRingView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


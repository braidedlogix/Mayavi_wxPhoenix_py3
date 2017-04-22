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

from tvtk.tvtk_classes.rendered_representation import RenderedRepresentation


class RenderedGraphRepresentation(RenderedRepresentation):
    """
    RenderedGraphRepresentation - 
    
    Superclass: RenderedRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderedGraphRepresentation, obj, update, **traits)
    
    color_edges_by_array = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _color_edges_by_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorEdgesByArray,
                        self.color_edges_by_array_)

    color_vertices_by_array = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _color_vertices_by_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorVerticesByArray,
                        self.color_vertices_by_array_)

    edge_icon_visibility = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _edge_icon_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeIconVisibility,
                        self.edge_icon_visibility_)

    edge_label_visibility = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _edge_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeLabelVisibility,
                        self.edge_label_visibility_)

    edge_visibility = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )

    def _edge_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeVisibility,
                        self.edge_visibility_)

    enable_edges_by_array = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _enable_edges_by_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableEdgesByArray,
                        self.enable_edges_by_array_)

    enable_vertices_by_array = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _enable_vertices_by_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableVerticesByArray,
                        self.enable_vertices_by_array_)

    hide_edge_labels_on_interaction = tvtk_base.false_bool_trait(help=\
        """
        Whether to hide the display of edge labels during mouse
        interaction.  Default is off.
        """
    )

    def _hide_edge_labels_on_interaction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHideEdgeLabelsOnInteraction,
                        self.hide_edge_labels_on_interaction_)

    hide_vertex_labels_on_interaction = tvtk_base.false_bool_trait(help=\
        """
        Whether to hide the display of vertex labels during mouse
        interaction.  Default is off.
        """
    )

    def _hide_vertex_labels_on_interaction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHideVertexLabelsOnInteraction,
                        self.hide_vertex_labels_on_interaction_)

    scaling = tvtk_base.false_bool_trait(help=\
        """
        Set whether to scale vertex glyphs.
        """
    )

    def _scaling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaling,
                        self.scaling_)

    use_edge_icon_type_map = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _use_edge_icon_type_map_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseEdgeIconTypeMap,
                        self.use_edge_icon_type_map_)

    use_vertex_icon_type_map = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _use_vertex_icon_type_map_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseVertexIconTypeMap,
                        self.use_vertex_icon_type_map_)

    vertex_icon_visibility = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _vertex_icon_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexIconVisibility,
                        self.vertex_icon_visibility_)

    vertex_label_visibility = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _vertex_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexLabelVisibility,
                        self.vertex_label_visibility_)

    def get_edge_layout_strategy(self):
        """
        V.get_edge_layout_strategy() -> EdgeLayoutStrategy
        C++: virtual EdgeLayoutStrategy *GetEdgeLayoutStrategy()
        Set/get the graph layout strategy.
        """
        ret = wrap_vtk(self._vtk_obj.GetEdgeLayoutStrategy())
        return ret
        

    def set_edge_layout_strategy_to_arc_parallel(self):
        """
        V.set_edge_layout_strategy_to_arc_parallel()
        C++: void SetEdgeLayoutStrategyToArcParallel()
        Set/get the graph layout strategy.
        """
        self._vtk_obj.SetEdgeLayoutStrategyToArcParallel()

    def set_edge_layout_strategy_to_geo(self):
        """
        V.set_edge_layout_strategy_to_geo(float)
        C++: virtual void SetEdgeLayoutStrategyToGeo(
            double explodeFactor=0.2)
        Set the edge layout strategy to a geospatial arced strategy
        appropriate for GeoView.
        """
        self._vtk_obj.SetEdgeLayoutStrategyToGeo()

    def set_edge_layout_strategy_to_pass_through(self):
        """
        V.set_edge_layout_strategy_to_pass_through()
        C++: void SetEdgeLayoutStrategyToPassThrough()
        Set/get the graph layout strategy.
        """
        self._vtk_obj.SetEdgeLayoutStrategyToPassThrough()

    def get_layout_strategy(self):
        """
        V.get_layout_strategy() -> GraphLayoutStrategy
        C++: virtual GraphLayoutStrategy *GetLayoutStrategy()
        Set/get the graph layout strategy.
        """
        ret = wrap_vtk(self._vtk_obj.GetLayoutStrategy())
        return ret
        

    def set_layout_strategy_to_circular(self):
        """
        V.set_layout_strategy_to_circular()
        C++: void SetLayoutStrategyToCircular()"""
        self._vtk_obj.SetLayoutStrategyToCircular()

    def set_layout_strategy_to_clustering2d(self):
        """
        V.set_layout_strategy_to_clustering2d()
        C++: void SetLayoutStrategyToClustering2D()"""
        self._vtk_obj.SetLayoutStrategyToClustering2D()

    def set_layout_strategy_to_community2d(self):
        """
        V.set_layout_strategy_to_community2d()
        C++: void SetLayoutStrategyToCommunity2D()"""
        self._vtk_obj.SetLayoutStrategyToCommunity2D()

    def set_layout_strategy_to_cone(self):
        """
        V.set_layout_strategy_to_cone()
        C++: void SetLayoutStrategyToCone()"""
        self._vtk_obj.SetLayoutStrategyToCone()

    def set_layout_strategy_to_cosmic_tree(self):
        """
        V.set_layout_strategy_to_cosmic_tree()
        C++: void SetLayoutStrategyToCosmicTree()
        V.set_layout_strategy_to_cosmic_tree(string, bool, int, int)
        C++: virtual void SetLayoutStrategyToCosmicTree(
            const char *nodeSizeArrayName, bool sizeLeafNodesOnly=true,
            int layoutDepth=0, IdType layoutRoot=-1)"""
        self._vtk_obj.SetLayoutStrategyToCosmicTree()

    def set_layout_strategy_to_fast2d(self):
        """
        V.set_layout_strategy_to_fast2d()
        C++: void SetLayoutStrategyToFast2D()"""
        self._vtk_obj.SetLayoutStrategyToFast2D()

    def set_layout_strategy_to_force_directed(self):
        """
        V.set_layout_strategy_to_force_directed()
        C++: void SetLayoutStrategyToForceDirected()"""
        self._vtk_obj.SetLayoutStrategyToForceDirected()

    def set_layout_strategy_to_pass_through(self):
        """
        V.set_layout_strategy_to_pass_through()
        C++: void SetLayoutStrategyToPassThrough()"""
        self._vtk_obj.SetLayoutStrategyToPassThrough()

    def set_layout_strategy_to_random(self):
        """
        V.set_layout_strategy_to_random()
        C++: void SetLayoutStrategyToRandom()
        Set predefined layout strategies.
        """
        self._vtk_obj.SetLayoutStrategyToRandom()

    def set_layout_strategy_to_simple2d(self):
        """
        V.set_layout_strategy_to_simple2d()
        C++: void SetLayoutStrategyToSimple2D()"""
        self._vtk_obj.SetLayoutStrategyToSimple2D()

    def set_layout_strategy_to_span_tree(self):
        """
        V.set_layout_strategy_to_span_tree()
        C++: void SetLayoutStrategyToSpanTree()"""
        self._vtk_obj.SetLayoutStrategyToSpanTree()

    def set_layout_strategy_to_tree(self):
        """
        V.set_layout_strategy_to_tree()
        C++: void SetLayoutStrategyToTree()
        V.set_layout_strategy_to_tree(bool, float, float, float)
        C++: virtual void SetLayoutStrategyToTree(bool radial,
            double angle=90, double leafSpacing=0.9,
            double logSpacing=1.0)"""
        self._vtk_obj.SetLayoutStrategyToTree()

    vertex_icon_selection_mode = traits.Trait('ignore_selection',
    tvtk_base.TraitRevPrefixMap({'ignore_selection': 3, 'annotation_icon': 2, 'selected_icon': 0, 'selected_offset': 1}), help=\
        """
        Set the mode to one of  ApplyIcons::SELECTED_ICON - use
        vertex_selected_icon ApplyIcons::SELECTED_OFFSET - use
        vertex_selected_icon as offset ApplyIcons::ANNOTATION_ICON - use
        current annotation icon ApplyIcons::IGNORE_SELECTION - ignore
        selected elements  The default is IGNORE_SELECTION.
        """
    )

    def _vertex_icon_selection_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexIconSelectionMode,
                        self.vertex_icon_selection_mode_)

    edge_color_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )

    def _edge_color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeColorArrayName,
                        self.edge_color_array_name)

    edge_hover_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )

    def _edge_hover_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeHoverArrayName,
                        self.edge_hover_array_name)

    edge_icon_alignment = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _edge_icon_alignment_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeIconAlignment,
                        self.edge_icon_alignment)

    edge_icon_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )

    def _edge_icon_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeIconArrayName,
                        self.edge_icon_array_name)

    edge_icon_priority_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )

    def _edge_icon_priority_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeIconPriorityArrayName,
                        self.edge_icon_priority_array_name)

    edge_label_array_name = traits.String('LabelText', enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _edge_label_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeLabelArrayName,
                        self.edge_label_array_name)

    edge_label_priority_array_name = traits.String('Priority', enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _edge_label_priority_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeLabelPriorityArrayName,
                        self.edge_label_priority_array_name)

    def _get_edge_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetEdgeLabelTextProperty())
    def _set_edge_label_text_property(self, arg):
        old_val = self._get_edge_label_text_property()
        self._wrap_call(self._vtk_obj.SetEdgeLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('edge_label_text_property', old_val, arg)
    edge_label_text_property = traits.Property(_get_edge_label_text_property, _set_edge_label_text_property, help=\
        """
        
        """
    )

    edge_scalar_bar_visibility = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Vertex/edge scalar bar visibility.
        """
    )

    def _edge_scalar_bar_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeScalarBarVisibility,
                        self.edge_scalar_bar_visibility)

    edge_selection = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _edge_selection_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeSelection,
                        self.edge_selection)

    enabled_edges_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )

    def _enabled_edges_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnabledEdgesArrayName,
                        self.enabled_edges_array_name)

    enabled_vertices_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )

    def _enabled_vertices_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnabledVerticesArrayName,
                        self.enabled_vertices_array_name)

    glyph_type = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the graph vertex glyph type.
        """
    )

    def _glyph_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlyphType,
                        self.glyph_type)

    scaling_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the glyph scaling array name.
        """
    )

    def _scaling_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalingArrayName,
                        self.scaling_array_name)

    vertex_color_array_name = traits.String('VertexDegree', enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _vertex_color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexColorArrayName,
                        self.vertex_color_array_name)

    vertex_default_icon = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _vertex_default_icon_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexDefaultIcon,
                        self.vertex_default_icon)

    vertex_hover_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )

    def _vertex_hover_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexHoverArrayName,
                        self.vertex_hover_array_name)

    vertex_icon_alignment = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _vertex_icon_alignment_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexIconAlignment,
                        self.vertex_icon_alignment)

    vertex_icon_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )

    def _vertex_icon_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexIconArrayName,
                        self.vertex_icon_array_name)

    vertex_icon_priority_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )

    def _vertex_icon_priority_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexIconPriorityArrayName,
                        self.vertex_icon_priority_array_name)

    vertex_label_array_name = traits.String('VertexDegree', enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _vertex_label_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexLabelArrayName,
                        self.vertex_label_array_name)

    vertex_label_priority_array_name = traits.String('VertexDegree', enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _vertex_label_priority_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexLabelPriorityArrayName,
                        self.vertex_label_priority_array_name)

    def _get_vertex_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetVertexLabelTextProperty())
    def _set_vertex_label_text_property(self, arg):
        old_val = self._get_vertex_label_text_property()
        self._wrap_call(self._vtk_obj.SetVertexLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('vertex_label_text_property', old_val, arg)
    vertex_label_text_property = traits.Property(_get_vertex_label_text_property, _set_vertex_label_text_property, help=\
        """
        
        """
    )

    vertex_scalar_bar_visibility = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Vertex/edge scalar bar visibility.
        """
    )

    def _vertex_scalar_bar_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexScalarBarVisibility,
                        self.vertex_scalar_bar_visibility)

    vertex_selected_icon = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _vertex_selected_icon_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexSelectedIcon,
                        self.vertex_selected_icon)

    def _get_edge_layout_strategy_name(self):
        return self._vtk_obj.GetEdgeLayoutStrategyName()
    edge_layout_strategy_name = traits.Property(_get_edge_layout_strategy_name, help=\
        """
        Set the edge layout strategy by name.
        """
    )

    def _get_edge_scalar_bar(self):
        return wrap_vtk(self._vtk_obj.GetEdgeScalarBar())
    edge_scalar_bar = traits.Property(_get_edge_scalar_bar, help=\
        """
        Obtain the scalar bar widget used to draw a legend for the
        vertices/edges.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def _get_layout_strategy_name(self):
        return self._vtk_obj.GetLayoutStrategyName()
    layout_strategy_name = traits.Property(_get_layout_strategy_name, help=\
        """
        Get/set the layout strategy by name.
        """
    )

    def _get_vertex_scalar_bar(self):
        return wrap_vtk(self._vtk_obj.GetVertexScalarBar())
    vertex_scalar_bar = traits.Property(_get_vertex_scalar_bar, help=\
        """
        Obtain the scalar bar widget used to draw a legend for the
        vertices/edges.
        """
    )

    def add_edge_icon_type(self, *args):
        """
        V.add_edge_icon_type(string, int)
        C++: virtual void AddEdgeIconType(const char *name, int type)"""
        ret = self._wrap_call(self._vtk_obj.AddEdgeIconType, *args)
        return ret

    def add_vertex_icon_type(self, *args):
        """
        V.add_vertex_icon_type(string, int)
        C++: virtual void AddVertexIconType(const char *name, int type)"""
        ret = self._wrap_call(self._vtk_obj.AddVertexIconType, *args)
        return ret

    def clear_edge_icon_types(self):
        """
        V.clear_edge_icon_types()
        C++: virtual void ClearEdgeIconTypes()"""
        ret = self._vtk_obj.ClearEdgeIconTypes()
        return ret
        

    def clear_vertex_icon_types(self):
        """
        V.clear_vertex_icon_types()
        C++: virtual void ClearVertexIconTypes()"""
        ret = self._vtk_obj.ClearVertexIconTypes()
        return ret
        

    def compute_selected_graph_bounds(self, *args):
        """
        V.compute_selected_graph_bounds([float, float, float, float, float,
            float])
        C++: void ComputeSelectedGraphBounds(double bounds[6])
        Compute the bounding box of the selected subgraph.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeSelectedGraphBounds, *args)
        return ret

    def is_layout_complete(self):
        """
        V.is_layout_complete() -> bool
        C++: virtual bool IsLayoutComplete()
        Whether the current graph layout is complete.
        """
        ret = self._vtk_obj.IsLayoutComplete()
        return ret
        

    def update_layout(self):
        """
        V.update_layout()
        C++: virtual void UpdateLayout()
        Performs another iteration on the graph layout.
        """
        ret = self._vtk_obj.UpdateLayout()
        return ret
        

    _updateable_traits_ = \
    (('color_edges_by_array', 'GetColorEdgesByArray'),
    ('color_vertices_by_array', 'GetColorVerticesByArray'),
    ('edge_icon_visibility', 'GetEdgeIconVisibility'),
    ('edge_label_visibility', 'GetEdgeLabelVisibility'),
    ('edge_visibility', 'GetEdgeVisibility'), ('enable_edges_by_array',
    'GetEnableEdgesByArray'), ('enable_vertices_by_array',
    'GetEnableVerticesByArray'), ('hide_edge_labels_on_interaction',
    'GetHideEdgeLabelsOnInteraction'),
    ('hide_vertex_labels_on_interaction',
    'GetHideVertexLabelsOnInteraction'), ('scaling', 'GetScaling'),
    ('use_edge_icon_type_map', 'GetUseEdgeIconTypeMap'),
    ('use_vertex_icon_type_map', 'GetUseVertexIconTypeMap'),
    ('vertex_icon_visibility', 'GetVertexIconVisibility'),
    ('vertex_label_visibility', 'GetVertexLabelVisibility'),
    ('selectable', 'GetSelectable'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('vertex_icon_selection_mode', 'GetVertexIconSelectionMode'),
    ('edge_color_array_name', 'GetEdgeColorArrayName'),
    ('edge_hover_array_name', 'GetEdgeHoverArrayName'),
    ('edge_icon_alignment', 'GetEdgeIconAlignment'),
    ('edge_icon_array_name', 'GetEdgeIconArrayName'),
    ('edge_icon_priority_array_name', 'GetEdgeIconPriorityArrayName'),
    ('edge_label_array_name', 'GetEdgeLabelArrayName'),
    ('edge_label_priority_array_name', 'GetEdgeLabelPriorityArrayName'),
    ('edge_scalar_bar_visibility', 'GetEdgeScalarBarVisibility'),
    ('edge_selection', 'GetEdgeSelection'), ('enabled_edges_array_name',
    'GetEnabledEdgesArrayName'), ('enabled_vertices_array_name',
    'GetEnabledVerticesArrayName'), ('glyph_type', 'GetGlyphType'),
    ('scaling_array_name', 'GetScalingArrayName'),
    ('vertex_color_array_name', 'GetVertexColorArrayName'),
    ('vertex_default_icon', 'GetVertexDefaultIcon'),
    ('vertex_hover_array_name', 'GetVertexHoverArrayName'),
    ('vertex_icon_alignment', 'GetVertexIconAlignment'),
    ('vertex_icon_array_name', 'GetVertexIconArrayName'),
    ('vertex_icon_priority_array_name', 'GetVertexIconPriorityArrayName'),
    ('vertex_label_array_name', 'GetVertexLabelArrayName'),
    ('vertex_label_priority_array_name',
    'GetVertexLabelPriorityArrayName'), ('vertex_scalar_bar_visibility',
    'GetVertexScalarBarVisibility'), ('vertex_selected_icon',
    'GetVertexSelectedIcon'), ('label_render_mode', 'GetLabelRenderMode'),
    ('selection_array_name', 'GetSelectionArrayName'), ('selection_type',
    'GetSelectionType'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'color_edges_by_array', 'color_vertices_by_array',
    'debug', 'edge_icon_visibility', 'edge_label_visibility',
    'edge_visibility', 'enable_edges_by_array',
    'enable_vertices_by_array', 'global_warning_display',
    'hide_edge_labels_on_interaction',
    'hide_vertex_labels_on_interaction', 'release_data_flag', 'scaling',
    'selectable', 'use_edge_icon_type_map', 'use_vertex_icon_type_map',
    'vertex_icon_visibility', 'vertex_label_visibility',
    'vertex_icon_selection_mode', 'edge_color_array_name',
    'edge_hover_array_name', 'edge_icon_alignment',
    'edge_icon_array_name', 'edge_icon_priority_array_name',
    'edge_label_array_name', 'edge_label_priority_array_name',
    'edge_scalar_bar_visibility', 'edge_selection',
    'enabled_edges_array_name', 'enabled_vertices_array_name',
    'glyph_type', 'label_render_mode', 'progress_text',
    'scaling_array_name', 'selection_array_name', 'selection_type',
    'vertex_color_array_name', 'vertex_default_icon',
    'vertex_hover_array_name', 'vertex_icon_alignment',
    'vertex_icon_array_name', 'vertex_icon_priority_array_name',
    'vertex_label_array_name', 'vertex_label_priority_array_name',
    'vertex_scalar_bar_visibility', 'vertex_selected_icon'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderedGraphRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderedGraphRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['color_edges_by_array', 'color_vertices_by_array',
            'edge_icon_visibility', 'edge_label_visibility', 'edge_visibility',
            'enable_edges_by_array', 'enable_vertices_by_array',
            'hide_edge_labels_on_interaction',
            'hide_vertex_labels_on_interaction', 'scaling', 'selectable',
            'use_edge_icon_type_map', 'use_vertex_icon_type_map',
            'vertex_icon_visibility', 'vertex_label_visibility'],
            ['vertex_icon_selection_mode'], ['edge_color_array_name',
            'edge_hover_array_name', 'edge_icon_alignment',
            'edge_icon_array_name', 'edge_icon_priority_array_name',
            'edge_label_array_name', 'edge_label_priority_array_name',
            'edge_scalar_bar_visibility', 'edge_selection',
            'enabled_edges_array_name', 'enabled_vertices_array_name',
            'glyph_type', 'label_render_mode', 'scaling_array_name',
            'selection_array_name', 'selection_type', 'vertex_color_array_name',
            'vertex_default_icon', 'vertex_hover_array_name',
            'vertex_icon_alignment', 'vertex_icon_array_name',
            'vertex_icon_priority_array_name', 'vertex_label_array_name',
            'vertex_label_priority_array_name', 'vertex_scalar_bar_visibility',
            'vertex_selected_icon']),
            title='Edit RenderedGraphRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderedGraphRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


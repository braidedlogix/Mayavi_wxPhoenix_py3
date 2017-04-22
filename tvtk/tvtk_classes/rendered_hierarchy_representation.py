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

from tvtk.tvtk_classes.rendered_graph_representation import RenderedGraphRepresentation


class RenderedHierarchyRepresentation(RenderedGraphRepresentation):
    """
    RenderedHierarchyRepresentation - 
    
    Superclass: RenderedGraphRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderedHierarchyRepresentation, obj, update, **traits)
    
    color_graph_edges_by_array = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _color_graph_edges_by_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorGraphEdgesByArray,
                        self.color_graph_edges_by_array_)

    graph_edge_label_visibility = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _graph_edge_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeLabelVisibility,
                        self.graph_edge_label_visibility_)

    graph_visibility = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _graph_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphVisibility,
                        self.graph_visibility_)

    bundling_strength = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _bundling_strength_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBundlingStrength,
                        self.bundling_strength)

    graph_edge_color_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )

    def _graph_edge_color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeColorArrayName,
                        self.graph_edge_color_array_name)

    graph_edge_label_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )

    def _graph_edge_label_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeLabelArrayName,
                        self.graph_edge_label_array_name)

    graph_edge_label_font_size = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _graph_edge_label_font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeLabelFontSize,
                        self.graph_edge_label_font_size)

    def get_graph_spline_type(self, *args):
        """
        V.get_graph_spline_type(int) -> int
        C++: virtual int GetGraphSplineType(int idx)
        Sets the spline type for the graph edges.
        SplineGraphEdges::CUSTOM uses a CardinalSpline.
        SplineGraphEdges::BSPLINE uses a b-spline. The default is
        BSPLINE.
        """
        ret = self._wrap_call(self._vtk_obj.GetGraphSplineType, *args)
        return ret

    def set_graph_spline_type(self, *args):
        """
        V.set_graph_spline_type(int, int)
        C++: virtual void SetGraphSplineType(int type, int idx)
        Sets the spline type for the graph edges.
        SplineGraphEdges::CUSTOM uses a CardinalSpline.
        SplineGraphEdges::BSPLINE uses a b-spline. The default is
        BSPLINE.
        """
        ret = self._wrap_call(self._vtk_obj.SetGraphSplineType, *args)
        return ret

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def set_graph_edge_color_to_spline_fraction(self, *args):
        """
        V.set_graph_edge_color_to_spline_fraction()
        C++: virtual void SetGraphEdgeColorToSplineFraction()
        V.set_graph_edge_color_to_spline_fraction(int)
        C++: virtual void SetGraphEdgeColorToSplineFraction(int idx)"""
        ret = self._wrap_call(self._vtk_obj.SetGraphEdgeColorToSplineFraction, *args)
        return ret

    _updateable_traits_ = \
    (('color_graph_edges_by_array', 'GetColorGraphEdgesByArray'),
    ('graph_edge_label_visibility', 'GetGraphEdgeLabelVisibility'),
    ('graph_visibility', 'GetGraphVisibility'), ('color_edges_by_array',
    'GetColorEdgesByArray'), ('color_vertices_by_array',
    'GetColorVerticesByArray'), ('edge_icon_visibility',
    'GetEdgeIconVisibility'), ('edge_label_visibility',
    'GetEdgeLabelVisibility'), ('edge_visibility', 'GetEdgeVisibility'),
    ('enable_edges_by_array', 'GetEnableEdgesByArray'),
    ('enable_vertices_by_array', 'GetEnableVerticesByArray'),
    ('hide_edge_labels_on_interaction', 'GetHideEdgeLabelsOnInteraction'),
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
    ('bundling_strength', 'GetBundlingStrength'),
    ('graph_edge_color_array_name', 'GetGraphEdgeColorArrayName'),
    ('graph_edge_label_array_name', 'GetGraphEdgeLabelArrayName'),
    ('graph_edge_label_font_size', 'GetGraphEdgeLabelFontSize'),
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
    (['abort_execute', 'color_edges_by_array',
    'color_graph_edges_by_array', 'color_vertices_by_array', 'debug',
    'edge_icon_visibility', 'edge_label_visibility', 'edge_visibility',
    'enable_edges_by_array', 'enable_vertices_by_array',
    'global_warning_display', 'graph_edge_label_visibility',
    'graph_visibility', 'hide_edge_labels_on_interaction',
    'hide_vertex_labels_on_interaction', 'release_data_flag', 'scaling',
    'selectable', 'use_edge_icon_type_map', 'use_vertex_icon_type_map',
    'vertex_icon_visibility', 'vertex_label_visibility',
    'vertex_icon_selection_mode', 'bundling_strength',
    'edge_color_array_name', 'edge_hover_array_name',
    'edge_icon_alignment', 'edge_icon_array_name',
    'edge_icon_priority_array_name', 'edge_label_array_name',
    'edge_label_priority_array_name', 'edge_scalar_bar_visibility',
    'edge_selection', 'enabled_edges_array_name',
    'enabled_vertices_array_name', 'glyph_type',
    'graph_edge_color_array_name', 'graph_edge_label_array_name',
    'graph_edge_label_font_size', 'label_render_mode', 'progress_text',
    'scaling_array_name', 'selection_array_name', 'selection_type',
    'vertex_color_array_name', 'vertex_default_icon',
    'vertex_hover_array_name', 'vertex_icon_alignment',
    'vertex_icon_array_name', 'vertex_icon_priority_array_name',
    'vertex_label_array_name', 'vertex_label_priority_array_name',
    'vertex_scalar_bar_visibility', 'vertex_selected_icon'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderedHierarchyRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderedHierarchyRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['color_edges_by_array', 'color_graph_edges_by_array',
            'color_vertices_by_array', 'edge_icon_visibility',
            'edge_label_visibility', 'edge_visibility', 'enable_edges_by_array',
            'enable_vertices_by_array', 'graph_edge_label_visibility',
            'graph_visibility', 'hide_edge_labels_on_interaction',
            'hide_vertex_labels_on_interaction', 'scaling', 'selectable',
            'use_edge_icon_type_map', 'use_vertex_icon_type_map',
            'vertex_icon_visibility', 'vertex_label_visibility'],
            ['vertex_icon_selection_mode'], ['bundling_strength',
            'edge_color_array_name', 'edge_hover_array_name',
            'edge_icon_alignment', 'edge_icon_array_name',
            'edge_icon_priority_array_name', 'edge_label_array_name',
            'edge_label_priority_array_name', 'edge_scalar_bar_visibility',
            'edge_selection', 'enabled_edges_array_name',
            'enabled_vertices_array_name', 'glyph_type',
            'graph_edge_color_array_name', 'graph_edge_label_array_name',
            'graph_edge_label_font_size', 'label_render_mode',
            'scaling_array_name', 'selection_array_name', 'selection_type',
            'vertex_color_array_name', 'vertex_default_icon',
            'vertex_hover_array_name', 'vertex_icon_alignment',
            'vertex_icon_array_name', 'vertex_icon_priority_array_name',
            'vertex_label_array_name', 'vertex_label_priority_array_name',
            'vertex_scalar_bar_visibility', 'vertex_selected_icon']),
            title='Edit RenderedHierarchyRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderedHierarchyRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


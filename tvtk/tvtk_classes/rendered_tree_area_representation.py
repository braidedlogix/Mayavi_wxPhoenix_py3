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


class RenderedTreeAreaRepresentation(RenderedRepresentation):
    """
    RenderedTreeAreaRepresentation - 
    
    Superclass: RenderedRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderedTreeAreaRepresentation, obj, update, **traits)
    
    area_label_visibility = tvtk_base.false_bool_trait(help=\
        """
        Whether to show area labels.  Default is off.
        """
    )

    def _area_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAreaLabelVisibility,
                        self.area_label_visibility_)

    color_areas_by_array = tvtk_base.true_bool_trait(help=\
        """
        Whether to color vertices.  Default is off.
        """
    )

    def _color_areas_by_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorAreasByArray,
                        self.color_areas_by_array_)

    color_graph_edges_by_array = tvtk_base.false_bool_trait(help=\
        """
        Whether to color edges.  Default is off.
        """
    )

    def _color_graph_edges_by_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorGraphEdgesByArray,
                        self.color_graph_edges_by_array_)

    graph_edge_label_visibility = tvtk_base.false_bool_trait(help=\
        """
        Whether to show edge labels.  Default is off.
        """
    )

    def _graph_edge_label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeLabelVisibility,
                        self.graph_edge_label_visibility_)

    use_rectangular_coordinates = tvtk_base.false_bool_trait(help=\
        """
        Whether the area represents radial or rectangular coordinates.
        """
    )

    def _use_rectangular_coordinates_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseRectangularCoordinates,
                        self.use_rectangular_coordinates_)

    area_color_array_name = traits.String('level', enter_set=True, auto_set=False, help=\
        """
        The array to use for coloring vertices.  Default is "color".
        """
    )

    def _area_color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAreaColorArrayName,
                        self.area_color_array_name)

    area_hover_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The name of the array whose value appears when the mouse hovers
        over a rectangle in the treemap.
        """
    )

    def _area_hover_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAreaHoverArrayName,
                        self.area_hover_array_name)

    area_label_array_name = traits.String('id', enter_set=True, auto_set=False, help=\
        """
        The array to use for area labeling.  Default is "label".
        """
    )

    def _area_label_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAreaLabelArrayName,
                        self.area_label_array_name)

    def _get_area_label_mapper(self):
        return wrap_vtk(self._vtk_obj.GetAreaLabelMapper())
    def _set_area_label_mapper(self, arg):
        old_val = self._get_area_label_mapper()
        self._wrap_call(self._vtk_obj.SetAreaLabelMapper,
                        deref_vtk(arg))
        self.trait_property_changed('area_label_mapper', old_val, arg)
    area_label_mapper = traits.Property(_get_area_label_mapper, _set_area_label_mapper, help=\
        """
        The mapper for rendering labels on areas. This may e.g. be
        Dynamic2DLabelMapper or TreeMapLabelMapper.
        """
    )

    area_label_priority_array_name = traits.String('Priority', enter_set=True, auto_set=False, help=\
        """
        The array to use for area labeling priority. Default is
        "_graph_vertex_degree".
        """
    )

    def _area_label_priority_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAreaLabelPriorityArrayName,
                        self.area_label_priority_array_name)

    def _get_area_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetAreaLabelTextProperty())
    def _set_area_label_text_property(self, arg):
        old_val = self._get_area_label_text_property()
        self._wrap_call(self._vtk_obj.SetAreaLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('area_label_text_property', old_val, arg)
    area_label_text_property = traits.Property(_get_area_label_text_property, _set_area_label_text_property, help=\
        """
        The text property for the area labels.
        """
    )

    def _get_area_layout_strategy(self):
        return wrap_vtk(self._vtk_obj.GetAreaLayoutStrategy())
    def _set_area_layout_strategy(self, arg):
        old_val = self._get_area_layout_strategy()
        self._wrap_call(self._vtk_obj.SetAreaLayoutStrategy,
                        deref_vtk(arg))
        self.trait_property_changed('area_layout_strategy', old_val, arg)
    area_layout_strategy = traits.Property(_get_area_layout_strategy, _set_area_layout_strategy, help=\
        """
        The layout strategy for producing spatial regions for the tree.
        """
    )

    area_size_array_name = traits.String('size', enter_set=True, auto_set=False, help=\
        """
        The array to use for area sizes. Default is "size".
        """
    )

    def _area_size_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAreaSizeArrayName,
                        self.area_size_array_name)

    def _get_area_to_poly_data(self):
        return wrap_vtk(self._vtk_obj.GetAreaToPolyData())
    def _set_area_to_poly_data(self, arg):
        old_val = self._get_area_to_poly_data()
        self._wrap_call(self._vtk_obj.SetAreaToPolyData,
                        deref_vtk(arg))
        self.trait_property_changed('area_to_poly_data', old_val, arg)
    area_to_poly_data = traits.Property(_get_area_to_poly_data, _set_area_to_poly_data, help=\
        """
        The filter for converting areas to polydata. This may e.g. be
        TreeMapToPolyData or TreeRingToPolyData. The filter must
        take a Tree as input and produce PolyData.
        """
    )

    edge_scalar_bar_visibility = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Visibility of scalar bar actor for edges.
        """
    )

    def _edge_scalar_bar_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeScalarBarVisibility,
                        self.edge_scalar_bar_visibility)

    graph_bundling_strength = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the bundling strength.
        """
    )

    def _graph_bundling_strength_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphBundlingStrength,
                        self.graph_bundling_strength)

    graph_edge_color_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array to use for coloring edges.  Default is "color".
        """
    )

    def _graph_edge_color_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeColorArrayName,
                        self.graph_edge_color_array_name)

    graph_edge_label_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The array to use for edge labeling.  Default is "label".
        """
    )

    def _graph_edge_label_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphEdgeLabelArrayName,
                        self.graph_edge_label_array_name)

    def _get_graph_edge_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetGraphEdgeLabelTextProperty())
    def _set_graph_edge_label_text_property(self, arg):
        old_val = self._get_graph_edge_label_text_property()
        self._wrap_call(self._vtk_obj.SetGraphEdgeLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('graph_edge_label_text_property', old_val, arg)
    graph_edge_label_text_property = traits.Property(_get_graph_edge_label_text_property, _set_graph_edge_label_text_property, help=\
        """
        The text property for the graph edge labels.
        """
    )

    graph_hover_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The name of the array whose value appears when the mouse hovers
        over a graph edge.
        """
    )

    def _graph_hover_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphHoverArrayName,
                        self.graph_hover_array_name)

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

    label_render_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the label render mode. QT - Use QtTreeRingLabeler with
        fitted labeling and unicode support. Requires VTK_USE_QT to be
        on. FREETYPE - Use standard freetype text rendering.
        """
    )

    def _label_render_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelRenderMode,
                        self.label_render_mode)

    shrink_percentage = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set the region shrink percentage between 0.0 and 1.0.
        """
    )

    def _shrink_percentage_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShrinkPercentage,
                        self.shrink_percentage)

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
        C++: virtual void SetGraphEdgeColorToSplineFraction(int idx)
        Set the color to be the spline fraction
        """
        ret = self._wrap_call(self._vtk_obj.SetGraphEdgeColorToSplineFraction, *args)
        return ret

    _updateable_traits_ = \
    (('area_label_visibility', 'GetAreaLabelVisibility'),
    ('color_areas_by_array', 'GetColorAreasByArray'),
    ('color_graph_edges_by_array', 'GetColorGraphEdgesByArray'),
    ('graph_edge_label_visibility', 'GetGraphEdgeLabelVisibility'),
    ('use_rectangular_coordinates', 'GetUseRectangularCoordinates'),
    ('selectable', 'GetSelectable'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('area_color_array_name', 'GetAreaColorArrayName'),
    ('area_hover_array_name', 'GetAreaHoverArrayName'),
    ('area_label_array_name', 'GetAreaLabelArrayName'),
    ('area_label_priority_array_name', 'GetAreaLabelPriorityArrayName'),
    ('area_size_array_name', 'GetAreaSizeArrayName'),
    ('edge_scalar_bar_visibility', 'GetEdgeScalarBarVisibility'),
    ('graph_bundling_strength', 'GetGraphBundlingStrength'),
    ('graph_edge_color_array_name', 'GetGraphEdgeColorArrayName'),
    ('graph_edge_label_array_name', 'GetGraphEdgeLabelArrayName'),
    ('graph_hover_array_name', 'GetGraphHoverArrayName'),
    ('label_render_mode', 'GetLabelRenderMode'), ('shrink_percentage',
    'GetShrinkPercentage'), ('selection_array_name',
    'GetSelectionArrayName'), ('selection_type', 'GetSelectionType'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'area_label_visibility', 'color_areas_by_array',
    'color_graph_edges_by_array', 'debug', 'global_warning_display',
    'graph_edge_label_visibility', 'release_data_flag', 'selectable',
    'use_rectangular_coordinates', 'area_color_array_name',
    'area_hover_array_name', 'area_label_array_name',
    'area_label_priority_array_name', 'area_size_array_name',
    'edge_scalar_bar_visibility', 'graph_bundling_strength',
    'graph_edge_color_array_name', 'graph_edge_label_array_name',
    'graph_hover_array_name', 'label_render_mode', 'progress_text',
    'selection_array_name', 'selection_type', 'shrink_percentage'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderedTreeAreaRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderedTreeAreaRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['area_label_visibility', 'color_areas_by_array',
            'color_graph_edges_by_array', 'graph_edge_label_visibility',
            'selectable', 'use_rectangular_coordinates'], [],
            ['area_color_array_name', 'area_hover_array_name',
            'area_label_array_name', 'area_label_priority_array_name',
            'area_size_array_name', 'edge_scalar_bar_visibility',
            'graph_bundling_strength', 'graph_edge_color_array_name',
            'graph_edge_label_array_name', 'graph_hover_array_name',
            'label_render_mode', 'selection_array_name', 'selection_type',
            'shrink_percentage']),
            title='Edit RenderedTreeAreaRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderedTreeAreaRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


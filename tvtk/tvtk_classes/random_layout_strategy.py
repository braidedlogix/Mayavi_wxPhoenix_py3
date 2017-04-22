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

from tvtk.tvtk_classes.graph_layout_strategy import GraphLayoutStrategy


class RandomLayoutStrategy(GraphLayoutStrategy):
    """
    RandomLayoutStrategy - randomly places vertices in 2 or 3
    dimensions
    
    Superclass: GraphLayoutStrategy
    
    Assigns points to the vertices of a graph randomly within a bounded
    range.
    
    .SECION Thanks Thanks to Brian Wylie from Sandia National
    Laboratories for adding incremental layout capabilities.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRandomLayoutStrategy, obj, update, **traits)
    
    automatic_bounds_computation = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off automatic graph bounds calculation. If this boolean
        is off, then the manually specified graph_bounds is used. If on,
        then the input's bounds us used as the graph bounds.
        """
    )

    def _automatic_bounds_computation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutomaticBoundsComputation,
                        self.automatic_bounds_computation_)

    three_dimensional_layout = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off layout of graph in three dimensions. If off, graph
        layout occurs in two dimensions. By default, three dimensional
        layout is on.
        """
    )

    def _three_dimensional_layout_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThreeDimensionalLayout,
                        self.three_dimensional_layout_)

    graph_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(-0.5, 0.5, -0.5, 0.5, -0.5, 0.5), cols=3, help=\
        """
        
        """
    )

    def _graph_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGraphBounds,
                        self.graph_bounds)

    random_seed = traits.Trait(123, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Seed the random number generator used to compute point positions.
        This has a significant effect on their final positions when the
        layout is complete.
        """
    )

    def _random_seed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRandomSeed,
                        self.random_seed)

    _updateable_traits_ = \
    (('automatic_bounds_computation', 'GetAutomaticBoundsComputation'),
    ('three_dimensional_layout', 'GetThreeDimensionalLayout'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('graph_bounds', 'GetGraphBounds'), ('random_seed', 'GetRandomSeed'),
    ('edge_weight_field', 'GetEdgeWeightField'), ('weight_edges',
    'GetWeightEdges'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['automatic_bounds_computation', 'debug', 'global_warning_display',
    'three_dimensional_layout', 'edge_weight_field', 'graph_bounds',
    'random_seed', 'weight_edges'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RandomLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RandomLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic_bounds_computation', 'three_dimensional_layout'],
            [], ['edge_weight_field', 'graph_bounds', 'random_seed',
            'weight_edges']),
            title='Edit RandomLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RandomLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


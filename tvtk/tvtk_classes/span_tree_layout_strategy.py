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


class SpanTreeLayoutStrategy(GraphLayoutStrategy):
    """
    SpanTreeLayoutStrategy - SpanTreeLayout is a strategy for
    drawing directed graphs that works by first extracting a spanning
    tree (more accurately, a spanning forest), and using this both to
    position graph vertices and to plan the placement of non
    
    Superclass: GraphLayoutStrategy
    
    -tree edges.  The latter are drawn with the aid of edge points to
        produce a tidy drawing.
    
    The approach is best suited to "quasi-trees", graphs where the number
    of edges is of the same order as the number of nodes; it is less well
    suited to denser graphs.  The boolean flag depth_first_spanning_tree
    determines whether a depth-first or breadth-first strategy is used to
    construct the underlying forest, and the choice of strategy affects
    the output layout significantly.  Informal experiments suggest that
    the breadth-first strategy is better for denser graphs.
    
    Different layouts could also be produced by plugging in alternative
    tree layout strategies.  To work with the method of routing non-tree
    edges, any strategy should draw a tree so that levels are equally
    spaced along the z-axis, precluding for example the use of a radial
    or balloon layout.
    
    SpanTreeLayout is based on an approach to 3d graph layout first
    developed as part of the "tulip" tool by Dr. David Auber at la_bri,
    U.Bordeaux: see www.tulip-software.org
    
    This implementation departs from the original version in that: (a) it
    is reconstructed to use Titan/VTK data structures; (b) it uses a
    faster method for dealing with non-tree edges,
        requiring at most two edge points per edge (c) allows for
    plugging in different tree layout methods (d) allows selection of two
    different strategies for building
        the underlying layout tree, which can yield significantly
        different results depending on the data.
    
    @par Thanks: Thanks to David Duke from the University of Leeds for
    providing this implementation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSpanTreeLayoutStrategy, obj, update, **traits)
    
    depth_first_spanning_tree = tvtk_base.false_bool_trait(help=\
        """
        If set, base the layout on a depth-first spanning tree, rather
        than the default breadth-first spanning tree. Switching between
        DFT and BFT may significantly change the layout, and choice must
        be made on a per-graph basis. Default value is off.
        """
    )

    def _depth_first_spanning_tree_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepthFirstSpanningTree,
                        self.depth_first_spanning_tree_)

    _updateable_traits_ = \
    (('depth_first_spanning_tree', 'GetDepthFirstSpanningTree'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('edge_weight_field', 'GetEdgeWeightField'), ('weight_edges',
    'GetWeightEdges'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'depth_first_spanning_tree', 'global_warning_display',
    'edge_weight_field', 'weight_edges'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SpanTreeLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SpanTreeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['depth_first_spanning_tree'], [], ['edge_weight_field',
            'weight_edges']),
            title='Edit SpanTreeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SpanTreeLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


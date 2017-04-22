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

from tvtk.tvtk_classes.graph_algorithm import GraphAlgorithm


class GraphHierarchicalBundleEdges(GraphAlgorithm):
    """
    GraphHierarchicalBundleEdges - layout graph arcs in bundles
    
    Superclass: GraphAlgorithm
    
    This algorithm creates a PolyData from a Graph.  As opposed to
    GraphToPolyData, which converts each arc into a straight line,
    each arc is converted to a polyline, following a tree structure.  The
    filter requires both a Graph and Tree as input.  The tree
    vertices must be a superset of the graph vertices.  A common example
    is when the graph vertices correspond to the leaves of the tree, but
    the internal vertices of the tree represent groupings of graph
    vertices.  The algorithm matches the vertices using the array
    "_pedigree_id".  The user may alternately set the direct_mapping flag to
    indicate that the two structures must have directly corresponding
    offsets (i.e. node i in the graph must correspond to node i in the
    tree).
    
    The Graph defines the topology of the output PolyData (i.e. the
    connections between nodes) while the Tree defines the geometry
    (i.e. the location of nodes and arc routes).  Thus, the tree must
    have been assigned vertex locations, but the graph does not need
    locations, in fact they will be ignored.  The edges approximately
    follow the path from the source to target nodes in the tree.  A
    bundling parameter controls how closely the edges are bundled
    together along the tree structure.
    
    You may follow this algorithm with SplineFilter in order to make
    nicely curved edges.
    
    @par Thanks: This algorithm was developed in the paper Danny Holten.
    Hierarchical Edge Bundles: Visualization of Adjacency Relations
    Relations in Hierarchical Data. IEEE Transactions on Visualization
    and Computer Graphics, Vol. 12, No. 5, 2006. pp. 741-748.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGraphHierarchicalBundleEdges, obj, update, **traits)
    
    direct_mapping = tvtk_base.false_bool_trait(help=\
        """
        If on, uses direct mapping from tree to graph vertices. If off,
        both the graph and tree must contain pedigree_id arrays which are
        used to match graph and tree vertices. Default is off.
        """
    )

    def _direct_mapping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirectMapping,
                        self.direct_mapping_)

    bundling_strength = traits.Trait(0.8, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        The level of arc bundling in the graph. A strength of 0 creates
        straight lines, while a strength of 1 forces arcs to pass
        directly through hierarchy node points. The default value is 0.8.
        """
    )

    def _bundling_strength_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBundlingStrength,
                        self.bundling_strength)

    def fill_input_port_information(self, *args):
        """
        V.fill_input_port_information(int, Information) -> int
        C++: int FillInputPortInformation(int port, Information *info)
        Set the input type of the algorithm to Graph.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillInputPortInformation, *my_args)
        return ret

    _updateable_traits_ = \
    (('direct_mapping', 'GetDirectMapping'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('bundling_strength',
    'GetBundlingStrength'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'direct_mapping',
    'global_warning_display', 'release_data_flag', 'bundling_strength',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GraphHierarchicalBundleEdges, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GraphHierarchicalBundleEdges properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['direct_mapping'], [], ['bundling_strength']),
            title='Edit GraphHierarchicalBundleEdges properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GraphHierarchicalBundleEdges properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


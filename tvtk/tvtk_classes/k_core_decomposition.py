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


class KCoreDecomposition(GraphAlgorithm):
    """
    KCoreDecomposition - Compute the k-core decomposition of the input
    graph.
    
    Superclass: GraphAlgorithm
    
    The k-core decomposition is a graph partitioning strategy that is
    useful for analyzing the structure of large networks. A k-core of a
    graph G is a maximal connected subgraph of G in which all vertices
    have degree at least k.  The k-core membership for each vertex of the
    input graph is found on the vertex data of the output graph as an
    array named '_k_core_decomposition_numbers' by default.  The algorithm
    used to find the k-cores has O(number of graph edges) running time,
    and is described in the following reference paper.
    
    An O(m) Algorithm for Cores Decomposition of Networks
      V. Batagelj, M. Zaversnik, 2001
    
    @par Thanks: Thanks to Thomas Otahal from Sandia National
    Laboratories for providing this implementation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkKCoreDecomposition, obj, update, **traits)
    
    check_input_graph = tvtk_base.true_bool_trait(help=\
        """
        Check the input graph for self loops and parallel edges.  The
        k-core is not defined for graphs that contain either of these. 
        Default is on.
        """
    )

    def _check_input_graph_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCheckInputGraph,
                        self.check_input_graph_)

    use_in_degree_neighbors = tvtk_base.true_bool_trait(help=\
        """
        Directed graphs only.  Use only the in edges to compute the
        vertex degree of a vertex.  The default is to use both in and out
        edges to compute vertex degree.
        """
    )

    def _use_in_degree_neighbors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseInDegreeNeighbors,
                        self.use_in_degree_neighbors_)

    use_out_degree_neighbors = tvtk_base.true_bool_trait(help=\
        """
        Directed graphs only.  Use only the out edges to compute the
        vertex degree of a vertex.  The default is to use both in and out
        edges to compute vertex degree.
        """
    )

    def _use_out_degree_neighbors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseOutDegreeNeighbors,
                        self.use_out_degree_neighbors_)

    def set_output_array_name(self, *args):
        """
        V.set_output_array_name(string)
        C++: void SetOutputArrayName(char *)
        Set the output array name. If no output array name is set then
        the name '_k_core_decomposition_numbers' is used.
        """
        ret = self._wrap_call(self._vtk_obj.SetOutputArrayName, *args)
        return ret

    _updateable_traits_ = \
    (('check_input_graph', 'GetCheckInputGraph'),
    ('use_in_degree_neighbors', 'GetUseInDegreeNeighbors'),
    ('use_out_degree_neighbors', 'GetUseOutDegreeNeighbors'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'check_input_graph', 'debug',
    'global_warning_display', 'release_data_flag',
    'use_in_degree_neighbors', 'use_out_degree_neighbors',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(KCoreDecomposition, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit KCoreDecomposition properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['check_input_graph', 'use_in_degree_neighbors',
            'use_out_degree_neighbors'], [], []),
            title='Edit KCoreDecomposition properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit KCoreDecomposition properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


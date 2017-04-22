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

from tvtk.tvtk_classes.object import Object


class OutEdgeIterator(Object):
    """
    OutEdgeIterator - Iterates through all outgoing edges from a
    vertex.
    
    Superclass: Object
    
    OutEdgeIterator iterates through all edges whose source is a
    particular vertex. Instantiate this class directly and call
    Initialize() to traverse the vertex of a graph. Alternately, use
    get_in_edges() on the graph to initialize the iterator. it->Next()
    returns a OutEdgeType structure, which contains Id, the edge's id, and Target, the
    edge's target vertex.
    
    @sa
    Graph InEdgeIterator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOutEdgeIterator, obj, update, **traits)
    
    def _get_graph(self):
        return wrap_vtk(self._vtk_obj.GetGraph())
    graph = traits.Property(_get_graph, help=\
        """
        Get the graph and vertex associated with this iterator.
        """
    )

    def _get_vertex(self):
        return self._vtk_obj.GetVertex()
    vertex = traits.Property(_get_vertex, help=\
        """
        Get the graph and vertex associated with this iterator.
        """
    )

    def has_next(self):
        """
        V.has_next() -> bool
        C++: bool HasNext()
        Whether this iterator has more edges.
        """
        ret = self._vtk_obj.HasNext()
        return ret
        

    def initialize(self, *args):
        """
        V.initialize(Graph, int)
        C++: void Initialize(Graph *g, IdType v)
        Initialize the iterator with a graph and vertex.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Initialize, *my_args)
        return ret

    def next(self):
        """
        V.next() -> OutEdgeType
        C++: OutEdgeType Next()
        Returns the next edge in the graph.
        """
        ret = wrap_vtk(self._vtk_obj.Next())
        return ret
        

    def next_graph_edge(self):
        """
        V.next_graph_edge() -> GraphEdge
        C++: GraphEdge *NextGraphEdge()
        Just like Next(), but returns heavy-weight GraphEdge object
        instead of the EdgeType struct, for use with wrappers. The
        graph edge is owned by this iterator, and changes after each call
        to next_graph_edge().
        """
        ret = wrap_vtk(self._vtk_obj.NextGraphEdge())
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OutEdgeIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OutEdgeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit OutEdgeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OutEdgeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


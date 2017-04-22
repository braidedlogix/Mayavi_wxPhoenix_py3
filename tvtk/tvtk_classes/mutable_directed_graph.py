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

from tvtk.tvtk_classes.directed_graph import DirectedGraph


class MutableDirectedGraph(DirectedGraph):
    """
    MutableDirectedGraph - An editable directed graph.
    
    Superclass: DirectedGraph
    
    MutableDirectedGraph is a directed graph which has additional
    methods for adding edges and vertices. add_child() is a convenience
    method for constructing trees. shallow_copy(), deep_copy(),
    checked_shallow_copy() and checked_deep_copy() will succeed for instances
    of DirectedGraph, MutableDirectedGraph and Tree.
    
    @sa
    DirectedGraph Graph Tree
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMutableDirectedGraph, obj, update, **traits)
    
    number_of_vertices = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Allocates space for the specified number of vertices in the
        graph's internal data structures.
        
        * This has no effect on the number of vertex coordinate tuples or
        * vertex attribute tuples allocated; you are responsible for
        * guaranteeing these match.
        * Also, this call is not implemented for distributed-memory
          graphs since
        * the semantics are unclear; calling this function on a graph
          with a
        * non-NULL distributed_graph_helper will generate an error message
          and
        * no allocation will be performed.
        """
    )

    def _number_of_vertices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfVertices,
                        self.number_of_vertices)

    def add_child(self, *args):
        """
        V.add_child(int, VariantArray) -> int
        C++: IdType AddChild(IdType parent,
            VariantArray *propertyArr)
        V.add_child(int) -> int
        C++: IdType AddChild(IdType parent)
        Convenience method for creating trees. Returns the newly created
        vertex id. Shortcut forvtk_id_type v = g->_add_vertex();
        g->_add_edge(parent, v);
        If non-null, property_arr provides edge properties for the
        newly-created edge. The values in property_arr must match up with
        the arrays in the edge data returned by get_edge_data().
        """
        my_args = deref_array(args, [('int', 'vtkVariantArray'), ['int']])
        ret = self._wrap_call(self._vtk_obj.AddChild, *my_args)
        return ret

    def add_edge(self, *args):
        """
        V.add_edge(int, int) -> EdgeType
        C++: EdgeType AddEdge(IdType u, IdType v)
        V.add_edge(int, int, VariantArray) -> EdgeType
        C++: EdgeType AddEdge(IdType u, IdType v,
            VariantArray *propertyArr)
        V.add_edge(Variant, int, VariantArray) -> EdgeType
        C++: EdgeType AddEdge(const Variant &u, IdType v,
            VariantArray *propertyArr=0)
        V.add_edge(int, Variant, VariantArray) -> EdgeType
        C++: EdgeType AddEdge(IdType u, const Variant &v,
            VariantArray *propertyArr=0)
        V.add_edge(Variant, Variant, VariantArray) -> EdgeType
        C++: EdgeType AddEdge(const Variant &u, const Variant &v,
             VariantArray *propertyArr=0)
        Adds a directed edge from u to v, where u and v are vertex
        indices, and returns a EdgeType structure describing that
        edge.
        
        * EdgeType contains fields for Source vertex index,
        * Target vertex index, and edge index Id.
        """
        my_args = deref_array(args, [('int', 'int'), ('int', 'int', 'vtkVariantArray'), ('vtkVariant', 'int', 'vtkVariantArray'), ('int', 'vtkVariant', 'vtkVariantArray'), ('vtkVariant', 'vtkVariant', 'vtkVariantArray')])
        ret = self._wrap_call(self._vtk_obj.AddEdge, *my_args)
        return wrap_vtk(ret)

    def add_graph_edge(self, *args):
        """
        V.add_graph_edge(int, int) -> GraphEdge
        C++: GraphEdge *AddGraphEdge(IdType u, IdType v)
        Variant of add_edge() that returns a heavyweight GraphEdge
        object. The graph owns the reference of the edge and will replace
        its contents on the next call to add_graph_edge().
        
        *
        
        ote This is a less efficient method for use with wrappers.
        * In C++ you should use the faster add_edge().
        """
        ret = self._wrap_call(self._vtk_obj.AddGraphEdge, *args)
        return wrap_vtk(ret)

    def add_vertex(self, *args):
        """
        V.add_vertex() -> int
        C++: IdType AddVertex()
        V.add_vertex(VariantArray) -> int
        C++: IdType AddVertex(VariantArray *propertyArr)
        V.add_vertex(Variant) -> int
        C++: IdType AddVertex(const Variant &pedigreeId)
        Adds a vertex to the graph and returns the index of the new
        vertex.
        
        *
        
        ote In a distributed graph (i.e. a graph whose distributed_helper
        * is non-null), this routine cannot be used to add a vertex
        * if the vertices in the graph have pedigree IDs, because this
          routine
        * will always add the vertex locally, which may conflict with the
        * proper location of the vertex based on the distribution of the
        * pedigree IDs.
        """
        my_args = deref_array(args, [None, ['vtkVariantArray'], ['vtkVariant']])
        ret = self._wrap_call(self._vtk_obj.AddVertex, *my_args)
        return ret

    def lazy_add_edge(self, *args):
        """
        V.lazy_add_edge(int, int, VariantArray)
        C++: void LazyAddEdge(IdType u, IdType v,
            VariantArray *propertyArr=0)
        V.lazy_add_edge(Variant, int, VariantArray)
        C++: void LazyAddEdge(const Variant &u, IdType v,
            VariantArray *propertyArr=0)
        V.lazy_add_edge(int, Variant, VariantArray)
        C++: void LazyAddEdge(IdType u, const Variant &v,
            VariantArray *propertyArr=0)
        V.lazy_add_edge(Variant, Variant, VariantArray)
        C++: void LazyAddEdge(const Variant &u, const Variant &v,
            VariantArray *propertyArr=0)
        Adds a directed edge from u to v, where u and v are vertex
        indices.
        
        * The number and order of values in the optional parameter
        * property_arr must match up with the arrays in the edge data
        * retrieved by get_edge_data().
        
        * This method is lazily evaluated for distributed graphs (i.e.
          graphs
        * whose distributed_helper is non-null) the next time Synchronize
          is
        * called on the helper.
        """
        my_args = deref_array(args, [('int', 'int', 'vtkVariantArray'), ('vtkVariant', 'int', 'vtkVariantArray'), ('int', 'vtkVariant', 'vtkVariantArray'), ('vtkVariant', 'vtkVariant', 'vtkVariantArray')])
        ret = self._wrap_call(self._vtk_obj.LazyAddEdge, *my_args)
        return ret

    def lazy_add_vertex(self, *args):
        """
        V.lazy_add_vertex()
        C++: void LazyAddVertex()
        V.lazy_add_vertex(VariantArray)
        C++: void LazyAddVertex(VariantArray *propertyArr)
        V.lazy_add_vertex(Variant)
        C++: void LazyAddVertex(const Variant &pedigreeId)
        Adds a vertex to the graph.
        
        * This method is lazily evaluated for distributed graphs (i.e.
          graphs
        * whose distributed_helper is non-null) the next time Synchronize
          is
        * called on the helper.
        """
        my_args = deref_array(args, [None, ['vtkVariantArray'], ['vtkVariant']])
        ret = self._wrap_call(self._vtk_obj.LazyAddVertex, *my_args)
        return ret

    def remove_edge(self, *args):
        """
        V.remove_edge(int)
        C++: void RemoveEdge(IdType e)
        Removes the edge from the graph. Note: This invalidates the last
        edge index, which is reassigned to e.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveEdge, *args)
        return ret

    def remove_edges(self, *args):
        """
        V.remove_edges(IdTypeArray)
        C++: void RemoveEdges(IdTypeArray *arr)
        Removes a collection of edges from the graph.
        """
        my_args = deref_array(args, [['vtkIdTypeArray']])
        ret = self._wrap_call(self._vtk_obj.RemoveEdges, *my_args)
        return ret

    def remove_vertex(self, *args):
        """
        V.remove_vertex(int)
        C++: void RemoveVertex(IdType v)
        Removes the vertex from the graph along with any connected edges.
        Note: This invalidates the last vertex index, which is reassigned
        to v.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveVertex, *args)
        return ret

    def remove_vertices(self, *args):
        """
        V.remove_vertices(IdTypeArray)
        C++: void RemoveVertices(IdTypeArray *arr)
        Removes a collection of vertices from the graph along with any
        connected edges.
        """
        my_args = deref_array(args, [['vtkIdTypeArray']])
        ret = self._wrap_call(self._vtk_obj.RemoveVertices, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_vertices', 'GetNumberOfVertices'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'number_of_vertices'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MutableDirectedGraph, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MutableDirectedGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], ['number_of_vertices']),
            title='Edit MutableDirectedGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MutableDirectedGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


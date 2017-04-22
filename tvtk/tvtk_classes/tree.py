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

from tvtk.tvtk_classes.directed_acyclic_graph import DirectedAcyclicGraph


class Tree(DirectedAcyclicGraph):
    """
    Tree - A rooted tree data structure.
    
    Superclass: DirectedAcyclicGraph
    
    Tree is a connected directed graph with no cycles. A tree is a
    type of directed graph, so works with all graph algorithms.
    
    Tree is a read-only data structure. To construct a tree, create an
    instance of MutableDirectedGraph. Add vertices and edges with
    add_vertex() and add_edge(). You may alternately start by adding a
    single vertex as the root then call graph->_add_child(parent) which
    adds a new vertex and connects the parent to the child. The tree MUST
    have all edges in the proper direction, from parent to child. After
    building the tree, call tree->_checked_shallow_copy(graph) to copy the
    structure into a Tree. This method will return false if the graph
    is an invalid tree.
    
    Tree provides some convenience methods for obtaining the parent
    and children of a vertex, for finding the root, and determining if a
    vertex is a leaf (a vertex with no children).
    
    @sa
    DirectedGraph MutableDirectedGraph Graph
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTree, obj, update, **traits)
    
    def get_child(self, *args):
        """
        V.get_child(int, int) -> int
        C++: IdType GetChild(IdType v, IdType i)
        Get the i-th child of a parent vertex.
        """
        ret = self._wrap_call(self._vtk_obj.GetChild, *args)
        return ret

    def get_children(self, *args):
        """
        V.get_children(int, AdjacentVertexIterator)
        C++: void GetChildren(IdType v, AdjacentVertexIterator *it)
        Get the child vertices of a vertex. This is a convenience method
        that functions exactly like get_adjacent_vertices.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetChildren, *my_args)
        return ret

    def get_level(self, *args):
        """
        V.get_level(int) -> int
        C++: IdType GetLevel(IdType v)
        Get the level of the vertex in the tree.  The root vertex has
        level 0. Returns -1 if the vertex id is < 0 or greater than the
        number of vertices in the tree.
        """
        ret = self._wrap_call(self._vtk_obj.GetLevel, *args)
        return ret

    def get_number_of_children(self, *args):
        """
        V.get_number_of_children(int) -> int
        C++: IdType GetNumberOfChildren(IdType v)
        Get the number of children of a vertex.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfChildren, *args)
        return ret

    def get_parent(self, *args):
        """
        V.get_parent(int) -> int
        C++: IdType GetParent(IdType v)
        Get the parent of a vertex.
        """
        ret = self._wrap_call(self._vtk_obj.GetParent, *args)
        return ret

    def get_parent_edge(self, *args):
        """
        V.get_parent_edge(int) -> EdgeType
        C++: EdgeType GetParentEdge(IdType v)
        Get the edge connecting the vertex to its parent.
        """
        ret = self._wrap_call(self._vtk_obj.GetParentEdge, *args)
        return wrap_vtk(ret)

    def _get_root(self):
        return self._vtk_obj.GetRoot()
    root = traits.Property(_get_root, help=\
        """
        Get the root vertex of the tree.
        """
    )

    def is_leaf(self, *args):
        """
        V.is_leaf(int) -> bool
        C++: bool IsLeaf(IdType vertex)
        Return whether the vertex is a leaf (i.e. it has no children).
        """
        ret = self._wrap_call(self._vtk_obj.IsLeaf, *args)
        return ret

    def reorder_children(self, *args):
        """
        V.reorder_children(int, IdTypeArray)
        C++: virtual void ReorderChildren(IdType parent,
            IdTypeArray *children)
        Reorder the children of a parent vertex. The children array must
        contain all the children of parent, just in a different order.
        This does not change the topology of the tree.
        """
        my_args = deref_array(args, [('int', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.ReorderChildren, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Tree, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Tree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit Tree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Tree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


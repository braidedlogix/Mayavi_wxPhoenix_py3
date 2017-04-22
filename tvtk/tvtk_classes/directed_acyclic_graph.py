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


class DirectedAcyclicGraph(DirectedGraph):
    """
    DirectedAcyclicGraph - A rooted tree data structure.
    
    Superclass: DirectedGraph
    
    DirectedAcyclicGraph is a connected directed graph with no cycles.
    A tree is a type of directed graph, so works with all graph
    algorithms.
    
    DirectedAcyclicGraph is a read-only data structure. To construct a
    tree, create an instance of MutableDirectedGraph. Add vertices and
    edges with add_vertex() and add_edge(). You may alternately start by
    adding a single vertex as the root then call graph->_add_child(parent)
    which adds a new vertex and connects the parent to the child. The
    tree MUST have all edges in the proper direction, from parent to
    child. After building the tree, call tree->_checked_shallow_copy(graph)
    to copy the structure into a DirectedAcyclicGraph. This method
    will return false if the graph is an invalid tree.
    
    DirectedAcyclicGraph provides some convenience methods for
    obtaining the parent and children of a vertex, for finding the root,
    and determining if a vertex is a leaf (a vertex with no children).
    
    @sa
    DirectedGraph MutableDirectedGraph Graph
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDirectedAcyclicGraph, obj, update, **traits)
    
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
            return super(DirectedAcyclicGraph, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DirectedAcyclicGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit DirectedAcyclicGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DirectedAcyclicGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


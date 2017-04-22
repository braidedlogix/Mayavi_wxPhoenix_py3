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


class CollapseGraph(GraphAlgorithm):
    """
    CollapseGraph - "Collapses" vertices onto their neighbors.
    
    Superclass: GraphAlgorithm
    
    CollapseGraph "collapses" vertices onto their neighbors, while
    maintaining connectivity.  Two inputs are required - a graph
    (directed or undirected), and a vertex selection that can be
    converted to indices.
    
    Conceptually, each of the vertices specified in the input selection
    expands, "swallowing" adacent vertices.  Edges to-or-from the
    "swallowed" vertices become edges to-or-from the expanding vertices,
    maintaining the overall graph connectivity.
    
    In the case of directed graphs, expanding vertices only swallow
    vertices that are connected via out edges.  This rule provides
    intuitive behavior when working with trees, so that "child" vertices
    collapse into their parents when the parents are part of the input
    selection.
    
    Input port 0: graph Input port 1: selection
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCollapseGraph, obj, update, **traits)
    
    def set_graph_connection(self, *args):
        """
        V.set_graph_connection(AlgorithmOutput)
        C++: void SetGraphConnection(AlgorithmOutput *)
        Convenience function provided for setting the graph input.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGraphConnection, *my_args)
        return ret

    def set_selection_connection(self, *args):
        """
        V.set_selection_connection(AlgorithmOutput)
        C++: void SetSelectionConnection(AlgorithmOutput *)
        Convenience function provided for setting the selection input.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSelectionConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CollapseGraph, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CollapseGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit CollapseGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CollapseGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


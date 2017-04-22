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


class StreamGraph(GraphAlgorithm):
    """
    StreamGraph - combines two graphs
    
    Superclass: GraphAlgorithm
    
    StreamGraph iteratively collects information from the input graph
    and combines it in the output graph. It internally maintains a graph
    instance that is incrementally updated every time the filter is
    called.
    
    Each update, MergeGraphs is used to combine this filter's input
    with the internal graph.
    
    If you can use an edge window array to filter out old edges based on
    a moving threshold.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStreamGraph, obj, update, **traits)
    
    use_edge_window = tvtk_base.false_bool_trait(help=\
        """
        Whether to use an edge window array. The default is to not use a
        window array.
        """
    )

    def _use_edge_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseEdgeWindow,
                        self.use_edge_window_)

    edge_window = traits.Float(10000.0, enter_set=True, auto_set=False, help=\
        """
        The time window amount. Edges with values lower than the maximum
        value minus this window will be removed from the graph. The
        default edge window is 10000.
        """
    )

    def _edge_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeWindow,
                        self.edge_window)

    edge_window_array_name = traits.String('time', enter_set=True, auto_set=False, help=\
        """
        The edge window array. The default array name is "time".
        """
    )

    def _edge_window_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeWindowArrayName,
                        self.edge_window_array_name)

    _updateable_traits_ = \
    (('use_edge_window', 'GetUseEdgeWindow'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('edge_window', 'GetEdgeWindow'),
    ('edge_window_array_name', 'GetEdgeWindowArrayName'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'use_edge_window', 'edge_window',
    'edge_window_array_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StreamGraph, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StreamGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_edge_window'], [], ['edge_window',
            'edge_window_array_name']),
            title='Edit StreamGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StreamGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


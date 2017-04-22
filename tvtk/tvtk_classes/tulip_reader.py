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

from tvtk.tvtk_classes.undirected_graph_algorithm import UndirectedGraphAlgorithm


class TulipReader(UndirectedGraphAlgorithm):
    """
    TulipReader - Reads tulip graph files.
    
    Superclass: UndirectedGraphAlgorithm
    
    TulipReader reads in files in the Tulip format. Definition of the
    Tulip file format can be found online at:
    http://tulip.labri.fr/tlpformat.php An example is the following 
    (nodes 0 1 2 3 4 5 6 7 8 9) (edge 0 0 1) (edge 1 1 2) (edge 2 2 3)
    (edge 3 3 4) (edge 4 4 5) (edge 5 5 6) (edge 6 6 7) (edge 7 7 8)
    (edge 8 8 9) (edge 9 9 0) (edge 10 0 5) (edge 11 2 7) (edge 12 4 9) 
    where "nodes" defines all the nodes ids in the graph, and "edge" is a
    triple of edge id, source vertex id, and target vertex id. The graph
    is read in as undirected graph. Pedigree ids are set on the output
    graph's vertices and edges that match the node and edge ids defined
    in the Tulip file.
    
    Clusters are output as a AnnotationLayers on output port 1. Each
    cluster name is used to create an annotation layer, and each cluster
    with that name is added to the layer as a SelectionNode. Nesting
    hierarchies are treated as if they were flat. See
    GraphAnnotationLayersFilter for an example of how the clusters can
    be represented visually.
    
    @attention Only string, int, and double properties are supported.
    Display information is discarded.
    
    @par Thanks: Thanks to Colin Myers, University of Leeds for extending
    this implementation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTulipReader, obj, update, **traits)
    
    file_name = tvtk_base.vtk_file_name("", help=\
        """
        The Tulip file name.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TulipReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TulipReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['file_name']),
            title='Edit TulipReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TulipReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


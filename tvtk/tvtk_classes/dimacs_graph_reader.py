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


class DIMACSGraphReader(GraphAlgorithm):
    """
    DIMACSGraphReader - reads Graph data from a DIMACS formatted
    file
    
    Superclass: GraphAlgorithm
    
    DIMACSGraphReader is a source object that reads Graph data
    files from a DIMACS format.
    
    The reader has special handlers for max-flow and graph coloring
    problems, which are specified in the problem line as 'max' and 'edge'
    respectively. Other graphs are treated as generic DIMACS files.
    
    DIMACS formatted files consist of lines in which the first character
    in in column 0 specifies the type of the line.
    
    Generic DIMACS files have the following line types:
    - problem statement line : p graph num_verts num_edges
    - node line (optional)   : n node_id node_weight
    - edge line              : a src_id trg_id edge_weight
    - alternate edge format  : e src_id trg_id edge_weight
    - comment lines          : c I am a comment line
    ** note, there should be one and only one problem statement line per
       file.
    
    DIMACS graphs are undirected and nodes are numbered 1..n
    
    See webpage for additional formatting details.
    -  http://dimacs.rutgers.edu/Challenges/
    -  http://www.dis.uniroma1.it/~challenge9/format.shtml
    
    @sa
    DIMACSGraphWriter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDIMACSGraphReader, obj, update, **traits)
    
    edge_attribute_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Edge attribute array name
        """
    )

    def _edge_attribute_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeAttributeArrayName,
                        self.edge_attribute_array_name)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        The DIMACS file name.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    vertex_attribute_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Vertex attribute array name
        """
    )

    def _vertex_attribute_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexAttributeArrayName,
                        self.vertex_attribute_array_name)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('edge_attribute_array_name', 'GetEdgeAttributeArrayName'),
    ('file_name', 'GetFileName'), ('vertex_attribute_array_name',
    'GetVertexAttributeArrayName'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'edge_attribute_array_name', 'file_name',
    'progress_text', 'vertex_attribute_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DIMACSGraphReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DIMACSGraphReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['edge_attribute_array_name', 'file_name',
            'vertex_attribute_array_name']),
            title='Edit DIMACSGraphReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DIMACSGraphReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


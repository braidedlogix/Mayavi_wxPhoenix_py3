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

from tvtk.tvtk_classes.xml_writer import XMLWriter


class PhyloXMLTreeWriter(XMLWriter):
    """
    PhyloXMLTreeWriter - write Tree data to phylo_xml format.
    
    Superclass: XMLWriter
    
    PhyloXMLTreeWriter is writes a Tree to a phylo_xml formatted
    file or string.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPhyloXMLTreeWriter, obj, update, **traits)
    
    edge_weight_array_name = traits.String('weight', enter_set=True, auto_set=False, help=\
        """
        Get/Set the name of the input's tree edge weight array. This
        array must be part of the input tree's edge_data. The default name
        is "weight".  If this array cannot be found, then no edge weights
        will be included in the output of this writer.
        """
    )

    def _edge_weight_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeWeightArrayName,
                        self.edge_weight_array_name)

    node_name_array_name = traits.String('node name', enter_set=True, auto_set=False, help=\
        """
        Get/Set the name of the input's tree node name array. This array
        must be part of the input tree's vertex_data. The default name is "node
        name".  If this array cannot be found, then no node names will be
        included in the output of this writer.
        """
    )

    def _node_name_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNodeNameArrayName,
                        self.node_name_array_name)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> Tree
        C++: Tree *GetInput()
        V.get_input(int) -> Tree
        C++: Tree *GetInput(int port)
        Get the input to this writer.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def ignore_array(self, *args):
        """
        V.ignore_array(string)
        C++: void IgnoreArray(const char *arrayName)
        Do not include name the vertex_data array in the phylo_xml output
        of this writer.  Call this function once for each array that you
        wish to ignore.
        """
        ret = self._wrap_call(self._vtk_obj.IgnoreArray, *args)
        return ret

    _updateable_traits_ = \
    (('encode_appended_data', 'GetEncodeAppendedData'),
    ('write_to_output_string', 'GetWriteToOutputString'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('byte_order',
    'GetByteOrder'), ('data_mode', 'GetDataMode'), ('header_type',
    'GetHeaderType'), ('id_type', 'GetIdType'), ('edge_weight_array_name',
    'GetEdgeWeightArrayName'), ('node_name_array_name',
    'GetNodeNameArrayName'), ('block_size', 'GetBlockSize'), ('file_name',
    'GetFileName'), ('number_of_time_steps', 'GetNumberOfTimeSteps'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'encode_appended_data',
    'global_warning_display', 'release_data_flag',
    'write_to_output_string', 'byte_order', 'data_mode', 'header_type',
    'id_type', 'block_size', 'edge_weight_array_name', 'file_name',
    'node_name_array_name', 'number_of_time_steps', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PhyloXMLTreeWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PhyloXMLTreeWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['encode_appended_data', 'write_to_output_string'],
            ['byte_order', 'data_mode', 'header_type', 'id_type'], ['block_size',
            'edge_weight_array_name', 'file_name', 'node_name_array_name',
            'number_of_time_steps']),
            title='Edit PhyloXMLTreeWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PhyloXMLTreeWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


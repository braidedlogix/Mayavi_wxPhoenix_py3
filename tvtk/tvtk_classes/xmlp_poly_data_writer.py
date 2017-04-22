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

from tvtk.tvtk_classes.xmlp_unstructured_data_writer import XMLPUnstructuredDataWriter


class XMLPPolyDataWriter(XMLPUnstructuredDataWriter):
    """
    XMLPPolyDataWriter - Write PVTK XML poly_data files.
    
    Superclass: XMLPUnstructuredDataWriter
    
    XMLPPolyDataWriter writes the PVTK XML poly_data file format. One
    poly data input can be written into a parallel file format with any
    number of pieces spread across files.  The standard extension for
    this writer's file format is "pvtp".  This writer uses
    XMLPolyDataWriter to write the individual piece files.
    
    @sa
    XMLPolyDataWriter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLPPolyDataWriter, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get/Set the writer's input.
        """
    )

    _updateable_traits_ = \
    (('write_summary_file', 'GetWriteSummaryFile'),
    ('encode_appended_data', 'GetEncodeAppendedData'),
    ('write_to_output_string', 'GetWriteToOutputString'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('byte_order',
    'GetByteOrder'), ('data_mode', 'GetDataMode'), ('header_type',
    'GetHeaderType'), ('id_type', 'GetIdType'), ('end_piece',
    'GetEndPiece'), ('ghost_level', 'GetGhostLevel'), ('number_of_pieces',
    'GetNumberOfPieces'), ('start_piece', 'GetStartPiece'), ('block_size',
    'GetBlockSize'), ('file_name', 'GetFileName'),
    ('number_of_time_steps', 'GetNumberOfTimeSteps'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'encode_appended_data',
    'global_warning_display', 'release_data_flag', 'write_summary_file',
    'write_to_output_string', 'byte_order', 'data_mode', 'header_type',
    'id_type', 'block_size', 'end_piece', 'file_name', 'ghost_level',
    'number_of_pieces', 'number_of_time_steps', 'progress_text',
    'start_piece'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLPPolyDataWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLPPolyDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['encode_appended_data', 'write_summary_file',
            'write_to_output_string'], ['byte_order', 'data_mode', 'header_type',
            'id_type'], ['block_size', 'end_piece', 'file_name', 'ghost_level',
            'number_of_pieces', 'number_of_time_steps', 'start_piece']),
            title='Edit XMLPPolyDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLPPolyDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


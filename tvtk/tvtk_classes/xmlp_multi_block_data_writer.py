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

from tvtk.tvtk_classes.xml_multi_block_data_writer import XMLMultiBlockDataWriter


class XMLPMultiBlockDataWriter(XMLMultiBlockDataWriter):
    """
    XMLPMultiBlockDataWriter - parallel writer for
    HierarchicalBoxDataSet.
    
    Superclass: XMLMultiBlockDataWriter
    
    XMLPCompositeDataWriter writes (in parallel or serially) the VTK
    XML multi-group, multi-block hierarchical and hierarchical box files.
    XML multi-group data files are meta-files that point to a list of
    serial VTK XML files.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLPMultiBlockDataWriter, obj, update, **traits)
    
    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        Controller used to communicate data type of blocks. By default,
        the global controller is used. If you want another controller to
        be used, set it with this. If no controller is set, only the
        local blocks will be written to the meta-file.
        """
    )

    number_of_pieces = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Get/Set the number of pieces that are being written in parallel.
        """
    )

    def _number_of_pieces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPieces,
                        self.number_of_pieces)

    start_piece = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the range of pieces assigned to this writer.
        """
    )

    def _start_piece_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartPiece,
                        self.start_piece)

    write_meta_file = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set whether this instance will write the meta-file. write_meta_file
        is set to flag only on process 0 and all other processes have
        write_meta_file set to 0 by default.
        """
    )

    def _write_meta_file_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteMetaFile,
                        self.write_meta_file)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Assign a data object as input. Note that this method does not
        establish a pipeline connection. Use set_input_connection() to
        setup a pipeline connection.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('encode_appended_data', 'GetEncodeAppendedData'),
    ('write_to_output_string', 'GetWriteToOutputString'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('byte_order',
    'GetByteOrder'), ('data_mode', 'GetDataMode'), ('header_type',
    'GetHeaderType'), ('id_type', 'GetIdType'), ('number_of_pieces',
    'GetNumberOfPieces'), ('start_piece', 'GetStartPiece'),
    ('write_meta_file', 'GetWriteMetaFile'), ('ghost_level',
    'GetGhostLevel'), ('block_size', 'GetBlockSize'), ('file_name',
    'GetFileName'), ('number_of_time_steps', 'GetNumberOfTimeSteps'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'encode_appended_data',
    'global_warning_display', 'release_data_flag',
    'write_to_output_string', 'byte_order', 'data_mode', 'header_type',
    'id_type', 'block_size', 'file_name', 'ghost_level',
    'number_of_pieces', 'number_of_time_steps', 'progress_text',
    'start_piece', 'write_meta_file'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLPMultiBlockDataWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLPMultiBlockDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['encode_appended_data', 'write_to_output_string'],
            ['byte_order', 'data_mode', 'header_type', 'id_type'], ['block_size',
            'file_name', 'ghost_level', 'number_of_pieces',
            'number_of_time_steps', 'start_piece', 'write_meta_file']),
            title='Edit XMLPMultiBlockDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLPMultiBlockDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


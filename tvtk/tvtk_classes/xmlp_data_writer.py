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


class XMLPDataWriter(XMLWriter):
    """
    XMLPDataWriter - Write data in a parallel XML format.
    
    Superclass: XMLWriter
    
    XMLPDataWriter is the superclass for all XML parallel data set
    writers.  It provides functionality needed for writing parallel
    formats, such as the selection of which writer writes the summary
    file and what range of pieces are assigned to each serial writer.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLPDataWriter, obj, update, **traits)
    
    write_summary_file = tvtk_base.true_bool_trait(help=\
        """
        Get/Set whether the writer should write the summary file that
        refers to all of the pieces' individual files. This is on by
        default. Note that only the first process writes the summary
        file.
        """
    )

    def _write_summary_file_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteSummaryFile,
                        self.write_summary_file_)

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
        be used, set it with this.
        """
    )

    end_piece = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the range of pieces assigned to this writer.
        """
    )

    def _end_piece_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndPiece,
                        self.end_piece)

    ghost_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the ghost level used for this writer's piece.
        """
    )

    def _ghost_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGhostLevel,
                        self.ghost_level)

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
            return super(XMLPDataWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLPDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['encode_appended_data', 'write_summary_file',
            'write_to_output_string'], ['byte_order', 'data_mode', 'header_type',
            'id_type'], ['block_size', 'end_piece', 'file_name', 'ghost_level',
            'number_of_pieces', 'number_of_time_steps', 'start_piece']),
            title='Edit XMLPDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLPDataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


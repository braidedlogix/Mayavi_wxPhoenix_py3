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

from tvtk.tvtk_classes.algorithm import Algorithm


class XMLWriter(Algorithm):
    """
    XMLWriter - Superclass for VTK's XML file writers.
    
    Superclass: Algorithm
    
    XMLWriter provides methods implementing most of the functionality
    needed to write VTK XML file formats.  Concrete subclasses provide
    actual writer implementations calling upon this functionality.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLWriter, obj, update, **traits)
    
    encode_appended_data = tvtk_base.true_bool_trait(help=\
        """
        Get/Set whether the appended data section is base64 encoded.  If
        encoded, reading and writing will be slower, but the file will be
        fully valid XML and text-only.  If not encoded, the XML
        specification will be violated, but reading and writing will be
        fast.  The default is to do the encoding.
        """
    )

    def _encode_appended_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEncodeAppendedData,
                        self.encode_appended_data_)

    write_to_output_string = tvtk_base.false_bool_trait(help=\
        """
        Enable writing to an output_string instead of the default, a file.
        """
    )

    def _write_to_output_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteToOutputString,
                        self.write_to_output_string_)

    byte_order = traits.Trait('little_endian',
    tvtk_base.TraitRevPrefixMap({'little_endian': 1, 'big_endian': 0}), help=\
        """
        Get/Set the byte order of data written to the file.  The default
        is the machine's hardware byte order.
        """
    )

    def _byte_order_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetByteOrder,
                        self.byte_order_)

    data_mode = traits.Trait('appended',
    tvtk_base.TraitRevPrefixMap({'appended': 2, 'ascii': 0, 'binary': 1}), help=\
        """
        Get/Set the data mode used for the file's data.  The options are
        XMLWriter::Ascii, XMLWriter::Binary, and
        XMLWriter::Appended.
        """
    )

    def _data_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataMode,
                        self.data_mode_)

    header_type = traits.Trait('u_int32',
    tvtk_base.TraitRevPrefixMap({'u_int32': 32, 'u_int64': 64}), help=\
        """
        Get/Set the binary data header word type.  The default is UInt32.
        Set to UInt64 when storing arrays requiring 64-bit indexing.
        """
    )

    def _header_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeaderType,
                        self.header_type_)

    id_type = traits.Trait('int64',
    tvtk_base.TraitRevPrefixMap({'int64': 64, 'int32': 32}), help=\
        """
        Get/Set the size of the IdType values stored in the file.  The
        default is the real size of IdType.
        """
    )

    def _id_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIdType,
                        self.id_type_)

    block_size = traits.Int(32768, enter_set=True, auto_set=False, help=\
        """
        Get/Set the block size used in compression.  When reading, this
        controls the granularity of how much extra information must be
        read when only part of the data are requested.  The value should
        be a multiple of the largest scalar data type.
        """
    )

    def _block_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBlockSize,
                        self.block_size)

    def _get_compressor(self):
        return wrap_vtk(self._vtk_obj.GetCompressor())
    def _set_compressor(self, arg):
        old_val = self._get_compressor()
        self._wrap_call(self._vtk_obj.SetCompressor,
                        deref_vtk(arg))
        self.trait_property_changed('compressor', old_val, arg)
    compressor = traits.Property(_get_compressor, _set_compressor, help=\
        """
        Get/Set the compressor used to compress binary and appended data
        before writing to the file.  Default is a ZLibDataCompressor.
        """
    )

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Get/Set the name of the output file.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    number_of_time_steps = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the number of time steps
        """
    )

    def _number_of_time_steps_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTimeSteps,
                        self.number_of_time_steps)

    def _get_default_file_extension(self):
        return self._vtk_obj.GetDefaultFileExtension()
    default_file_extension = traits.Property(_get_default_file_extension, help=\
        """
        Get the default file extension for files written by this writer.
        """
    )

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

    def _get_output_string(self):
        return self._vtk_obj.GetOutputString()
    output_string = traits.Property(_get_output_string, help=\
        """
        Enable writing to an output_string instead of the default, a file.
        """
    )

    def set_compressor_type(self, *args):
        """
        V.set_compressor_type(int)
        C++: void SetCompressorType(int compressorType)
        Convenience functions to set the compressor to certain known
        types.
        """
        ret = self._wrap_call(self._vtk_obj.SetCompressorType, *args)
        return ret

    def set_compressor_type_to_none(self):
        """
        V.set_compressor_type_to_none()
        C++: void SetCompressorTypeToNone()
        Convenience functions to set the compressor to certain known
        types.
        """
        ret = self._vtk_obj.SetCompressorTypeToNone()
        return ret
        

    def set_compressor_type_to_z_lib(self):
        """
        V.set_compressor_type_to_z_lib()
        C++: void SetCompressorTypeToZLib()
        Convenience functions to set the compressor to certain known
        types.
        """
        ret = self._vtk_obj.SetCompressorTypeToZLib()
        return ret
        

    def set_input_data(self, *args):
        """
        V.set_input_data(DataObject)
        C++: void SetInputData(DataObject *)
        V.set_input_data(int, DataObject)
        C++: void SetInputData(int, DataObject *)
        Assign a data object as input. Note that this method does not
        establish a pipeline connection. Use set_input_connection() to
        setup a pipeline connection.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    def start(self):
        """
        V.start()
        C++: void Start()
        API to interface an outside the VTK pipeline control
        """
        ret = self._vtk_obj.Start()
        return ret
        

    def stop(self):
        """
        V.stop()
        C++: void Stop()
        API to interface an outside the VTK pipeline control
        """
        ret = self._vtk_obj.Stop()
        return ret
        

    def write(self):
        """
        V.write() -> int
        C++: int Write()
        Invoke the writer.  Returns 1 for success, 0 for failure.
        """
        ret = self._vtk_obj.Write()
        return ret
        

    def write_next_time(self, *args):
        """
        V.write_next_time(float)
        C++: void WriteNextTime(double time)
        API to interface an outside the VTK pipeline control
        """
        ret = self._wrap_call(self._vtk_obj.WriteNextTime, *args)
        return ret

    _updateable_traits_ = \
    (('encode_appended_data', 'GetEncodeAppendedData'),
    ('write_to_output_string', 'GetWriteToOutputString'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('byte_order',
    'GetByteOrder'), ('data_mode', 'GetDataMode'), ('header_type',
    'GetHeaderType'), ('id_type', 'GetIdType'), ('block_size',
    'GetBlockSize'), ('file_name', 'GetFileName'),
    ('number_of_time_steps', 'GetNumberOfTimeSteps'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'encode_appended_data',
    'global_warning_display', 'release_data_flag',
    'write_to_output_string', 'byte_order', 'data_mode', 'header_type',
    'id_type', 'block_size', 'file_name', 'number_of_time_steps',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['encode_appended_data', 'write_to_output_string'],
            ['byte_order', 'data_mode', 'header_type', 'id_type'], ['block_size',
            'file_name', 'number_of_time_steps']),
            title='Edit XMLWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


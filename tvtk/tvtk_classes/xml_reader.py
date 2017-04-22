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


class XMLReader(Algorithm):
    """
    XMLReader - Superclass for VTK's XML format readers.
    
    Superclass: Algorithm
    
    XMLReader uses XMLDataParser to parse a <a
    href="http://www.vtk.org/Wiki/VTK_XML_Formats">VTK XMLinput file.
    Concrete subclasses then traverse the parsed file structure and
    extract data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLReader, obj, update, **traits)
    
    read_from_input_string = tvtk_base.false_bool_trait(help=\
        """
        Enable reading from an input_string instead of the default, a
        file.
        """
    )

    def _read_from_input_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadFromInputString,
                        self.read_from_input_string_)

    def get_cell_array_status(self, *args):
        """
        V.get_cell_array_status(string) -> int
        C++: int GetCellArrayStatus(const char *name)
        Get/Set whether the point or cell array with the given name is to
        be read.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellArrayStatus, *args)
        return ret

    def set_cell_array_status(self, *args):
        """
        V.set_cell_array_status(string, int)
        C++: void SetCellArrayStatus(const char *name, int status)
        Get/Set whether the point or cell array with the given name is to
        be read.
        """
        ret = self._wrap_call(self._vtk_obj.SetCellArrayStatus, *args)
        return ret

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Get/Set the name of the input file.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_parser_error_observer(self):
        return wrap_vtk(self._vtk_obj.GetParserErrorObserver())
    def _set_parser_error_observer(self, arg):
        old_val = self._get_parser_error_observer()
        self._wrap_call(self._vtk_obj.SetParserErrorObserver,
                        deref_vtk(arg))
        self.trait_property_changed('parser_error_observer', old_val, arg)
    parser_error_observer = traits.Property(_get_parser_error_observer, _set_parser_error_observer, help=\
        """
        Set/get the error_observer for the internal xml parser This is
        useful for applications that want to catch error messages.
        """
    )

    def get_point_array_status(self, *args):
        """
        V.get_point_array_status(string) -> int
        C++: int GetPointArrayStatus(const char *name)
        Get/Set whether the point or cell array with the given name is to
        be read.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayStatus, *args)
        return ret

    def set_point_array_status(self, *args):
        """
        V.set_point_array_status(string, int)
        C++: void SetPointArrayStatus(const char *name, int status)
        Get/Set whether the point or cell array with the given name is to
        be read.
        """
        ret = self._wrap_call(self._vtk_obj.SetPointArrayStatus, *args)
        return ret

    def _get_reader_error_observer(self):
        return wrap_vtk(self._vtk_obj.GetReaderErrorObserver())
    def _set_reader_error_observer(self, arg):
        old_val = self._get_reader_error_observer()
        self._wrap_call(self._vtk_obj.SetReaderErrorObserver,
                        deref_vtk(arg))
        self.trait_property_changed('reader_error_observer', old_val, arg)
    reader_error_observer = traits.Property(_get_reader_error_observer, _set_reader_error_observer, help=\
        """
        Set/get the error_observer for the internal reader This is useful
        for applications that want to catch error messages.
        """
    )

    time_step = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Which time_step to read.
        """
    )

    def _time_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStep,
                        self.time_step)

    time_step_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _time_step_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStepRange,
                        self.time_step_range)

    def get_cell_array_name(self, *args):
        """
        V.get_cell_array_name(int) -> string
        C++: const char *GetCellArrayName(int index)
        Get the name of the point or cell array with the given index in
        the input.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellArrayName, *args)
        return ret

    def _get_cell_data_array_selection(self):
        return wrap_vtk(self._vtk_obj.GetCellDataArraySelection())
    cell_data_array_selection = traits.Property(_get_cell_data_array_selection, help=\
        """
        Get the data array selection tables used to configure which data
        arrays are loaded by the reader.
        """
    )

    def _get_number_of_cell_arrays(self):
        return self._vtk_obj.GetNumberOfCellArrays()
    number_of_cell_arrays = traits.Property(_get_number_of_cell_arrays, help=\
        """
        Get the number of point or cell arrays available in the input.
        """
    )

    def _get_number_of_point_arrays(self):
        return self._vtk_obj.GetNumberOfPointArrays()
    number_of_point_arrays = traits.Property(_get_number_of_point_arrays, help=\
        """
        Get the number of point or cell arrays available in the input.
        """
    )

    def _get_number_of_time_steps(self):
        return self._vtk_obj.GetNumberOfTimeSteps()
    number_of_time_steps = traits.Property(_get_number_of_time_steps, help=\
        """
        
        """
    )

    def _get_output_as_data_set(self):
        return wrap_vtk(self._vtk_obj.GetOutputAsDataSet())
    output_as_data_set = traits.Property(_get_output_as_data_set, help=\
        """
        Get the output as a DataSet pointer.
        """
    )

    def get_point_array_name(self, *args):
        """
        V.get_point_array_name(int) -> string
        C++: const char *GetPointArrayName(int index)
        Get the name of the point or cell array with the given index in
        the input.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayName, *args)
        return ret

    def _get_point_data_array_selection(self):
        return wrap_vtk(self._vtk_obj.GetPointDataArraySelection())
    point_data_array_selection = traits.Property(_get_point_data_array_selection, help=\
        """
        Get the data array selection tables used to configure which data
        arrays are loaded by the reader.
        """
    )

    def _get_xml_parser(self):
        return wrap_vtk(self._vtk_obj.GetXMLParser())
    xml_parser = traits.Property(_get_xml_parser, help=\
        """
        Returns the internal XML parser. This can be used to access the
        XML DOM after request_information() was called.
        """
    )

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: virtual int CanReadFile(const char *name)
        Test whether the file (type) with the given name can be read by
        this reader. If the file has a newer version than the reader, we
        still say we can read the file type and we fail later, when we
        try to read the file. This enables clients (_para_view) to
        distinguish between failures when we need to look for another
        reader and failures when we don't.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    def copy_output_information(self, *args):
        """
        V.copy_output_information(Information, int)
        C++: virtual void CopyOutputInformation(Information *outInfo,
            int port)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyOutputInformation, *my_args)
        return ret

    def set_input_string(self, *args):
        """
        V.set_input_string(string)
        C++: void SetInputString(std::string s)
        Enable reading from an input_string instead of the default, a
        file.
        """
        ret = self._wrap_call(self._vtk_obj.SetInputString, *args)
        return ret

    _updateable_traits_ = \
    (('read_from_input_string', 'GetReadFromInputString'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('time_step', 'GetTimeStep'), ('time_step_range',
    'GetTimeStepRange'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'read_from_input_string', 'release_data_flag', 'file_name',
    'progress_text', 'time_step', 'time_step_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['read_from_input_string'], [], ['file_name', 'time_step',
            'time_step_range']),
            title='Edit XMLReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


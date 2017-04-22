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

from tvtk.tvtk_classes.writer import Writer


class DelimitedTextWriter(Writer):
    """
    DelimitedTextWriter - Delimited text writer for Table
    
    Superclass: Writer
    
    Writes a Table as a delimited text file (such as CSV).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDelimitedTextWriter, obj, update, **traits)
    
    write_to_output_string = tvtk_base.false_bool_trait(help=\
        """
        Enable writing to an output_string instead of the default, a file.
        """
    )

    def _write_to_output_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteToOutputString,
                        self.write_to_output_string_)

    field_delimiter = traits.String(',', enter_set=True, auto_set=False, help=\
        """
        Get/Set the delimiter use to separate fields ("," by default.)
        """
    )

    def _field_delimiter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldDelimiter,
                        self.field_delimiter)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Get/Set the filename for the file.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    string_delimiter = traits.String('"', enter_set=True, auto_set=False, help=\
        """
        Get/Set the delimiter used for string data, if any eg. double
        quotes(").
        """
    )

    def _string_delimiter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStringDelimiter,
                        self.string_delimiter)

    use_string_delimiter = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Get/Set if string_delimiter must be used for string data. True by
        default.
        """
    )

    def _use_string_delimiter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseStringDelimiter,
                        self.use_string_delimiter)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def get_string(self, *args):
        """
        V.get_string(string) -> string
        C++: StdString GetString(StdString string)
        Internal method: Returns the "string" with the "_string_delimiter"
        if use_string_delimiter is true.
        """
        ret = self._wrap_call(self._vtk_obj.GetString, *args)
        return ret

    def register_and_get_output_string(self):
        """
        V.register_and_get_output_string() -> string
        C++: char *RegisterAndGetOutputString()
        This convenience method returns the string, sets the IVAR to
        NULL, so that the user is responsible for deleting the string.
        """
        ret = self._vtk_obj.RegisterAndGetOutputString()
        return ret
        

    _updateable_traits_ = \
    (('write_to_output_string', 'GetWriteToOutputString'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('field_delimiter', 'GetFieldDelimiter'), ('file_name',
    'GetFileName'), ('string_delimiter', 'GetStringDelimiter'),
    ('use_string_delimiter', 'GetUseStringDelimiter'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'write_to_output_string', 'field_delimiter',
    'file_name', 'progress_text', 'string_delimiter',
    'use_string_delimiter'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DelimitedTextWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DelimitedTextWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['write_to_output_string'], [], ['field_delimiter', 'file_name',
            'string_delimiter', 'use_string_delimiter']),
            title='Edit DelimitedTextWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DelimitedTextWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


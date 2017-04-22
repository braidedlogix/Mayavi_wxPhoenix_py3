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


class DataObjectWriter(Writer):
    """
    DataObjectWriter - write vtk field data
    
    Superclass: Writer
    
    DataObjectWriter is a source object that writes ASCII or binary
    field data files in vtk format. Field data is a general form of data
    in matrix form.
    
    @warning
    Binary files written on one system may not be readable on other
    systems.
    
    @sa
    FieldData FieldDataReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataObjectWriter, obj, update, **traits)
    
    write_to_output_string = tvtk_base.false_bool_trait(help=\
        """
        Methods delegated to DataWriter, see DataWriter.
        """
    )

    def _write_to_output_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteToOutputString,
                        self.write_to_output_string_)

    file_type = traits.Trait('ascii',
    tvtk_base.TraitRevPrefixMap({'ascii': 1, 'binary': 2}), help=\
        """
        Methods delegated to DataWriter, see DataWriter.
        """
    )

    def _file_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileType,
                        self.file_type_)

    field_data_name = traits.String('FieldData', enter_set=True, auto_set=False, help=\
        """
        Methods delegated to DataWriter, see DataWriter.
        """
    )

    def _field_data_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldDataName,
                        self.field_data_name)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Methods delegated to DataWriter, see DataWriter.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    header = traits.String('vtk output', enter_set=True, auto_set=False, help=\
        """
        Methods delegated to DataWriter, see DataWriter.
        """
    )

    def _header_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeader,
                        self.header)

    def _get_binary_output_string(self):
        return self._vtk_obj.GetBinaryOutputString()
    binary_output_string = traits.Property(_get_binary_output_string, help=\
        """
        Methods delegated to DataWriter, see DataWriter.
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
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_output_std_string(self):
        return self._vtk_obj.GetOutputStdString()
    output_std_string = traits.Property(_get_output_std_string, help=\
        """
        Methods delegated to DataWriter, see DataWriter.
        """
    )

    def _get_output_string(self):
        return self._vtk_obj.GetOutputString()
    output_string = traits.Property(_get_output_string, help=\
        """
        Methods delegated to DataWriter, see DataWriter.
        """
    )

    def _get_output_string_length(self):
        return self._vtk_obj.GetOutputStringLength()
    output_string_length = traits.Property(_get_output_string_length, help=\
        """
        Methods delegated to DataWriter, see DataWriter.
        """
    )

    _updateable_traits_ = \
    (('write_to_output_string', 'GetWriteToOutputString'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_type',
    'GetFileType'), ('field_data_name', 'GetFieldDataName'), ('file_name',
    'GetFileName'), ('header', 'GetHeader'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'write_to_output_string', 'file_type',
    'field_data_name', 'file_name', 'header', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataObjectWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DataObjectWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['write_to_output_string'], ['file_type'], ['field_data_name',
            'file_name', 'header']),
            title='Edit DataObjectWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataObjectWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


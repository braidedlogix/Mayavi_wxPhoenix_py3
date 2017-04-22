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

from tvtk.tvtk_classes.table_algorithm import TableAlgorithm


class TecplotTableReader(TableAlgorithm):
    """
    TecplotTableReader - reads in Tecplot tabular data and outputs a
    Table data structure.
    
    Superclass: TableAlgorithm
    
    TecplotTableReader is an interface for reading tabulat data in
    Tecplot ascii format.
    
    @par Thanks: Thanks to DelimitedTextReader authors.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTecplotTableReader, obj, update, **traits)
    
    generate_pedigree_ids = tvtk_base.false_bool_trait(help=\
        """
        If on (default), generates pedigree ids automatically. If off,
        assign one of the arrays to be the pedigree id.
        """
    )

    def _generate_pedigree_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePedigreeIds,
                        self.generate_pedigree_ids_)

    output_pedigree_ids = tvtk_base.false_bool_trait(help=\
        """
        If on, assigns pedigree ids to output. Defaults to off.
        """
    )

    def _output_pedigree_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPedigreeIds,
                        self.output_pedigree_ids_)

    column_names_on_line = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Specifies the line number that holds the column names. Default is
        1.
        """
    )

    def _column_names_on_line_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColumnNamesOnLine,
                        self.column_names_on_line)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specifies the delimited text file to be loaded.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    header_lines = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Specifies the number of lines that form the header of the file.
        Default is 2.
        """
    )

    def _header_lines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeaderLines,
                        self.header_lines)

    max_records = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specifies the maximum number of records to read from the file. 
        Limiting the number of records to read is useful for previewing
        the contents of a file.
        """
    )

    def _max_records_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxRecords,
                        self.max_records)

    pedigree_id_array_name = traits.String('id', enter_set=True, auto_set=False, help=\
        """
        The name of the array for generating or assigning pedigree ids
        (default "id").
        """
    )

    def _pedigree_id_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPedigreeIdArrayName,
                        self.pedigree_id_array_name)

    skip_column_names = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Specifies the number of fields to skip while reading the column
        names. Default is 1.
        """
    )

    def _skip_column_names_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSkipColumnNames,
                        self.skip_column_names)

    def _get_last_error(self):
        return self._vtk_obj.GetLastError()
    last_error = traits.Property(_get_last_error, help=\
        """
        Returns a human-readable description of the most recent error, if
        any. Otherwise, returns an empty string.  Note that the result is
        only valid after calling Update().
        """
    )

    _updateable_traits_ = \
    (('generate_pedigree_ids', 'GetGeneratePedigreeIds'),
    ('output_pedigree_ids', 'GetOutputPedigreeIds'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('column_names_on_line',
    'GetColumnNamesOnLine'), ('file_name', 'GetFileName'),
    ('header_lines', 'GetHeaderLines'), ('max_records', 'GetMaxRecords'),
    ('pedigree_id_array_name', 'GetPedigreeIdArrayName'),
    ('skip_column_names', 'GetSkipColumnNames'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_pedigree_ids',
    'global_warning_display', 'output_pedigree_ids', 'release_data_flag',
    'column_names_on_line', 'file_name', 'header_lines', 'max_records',
    'pedigree_id_array_name', 'progress_text', 'skip_column_names'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TecplotTableReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TecplotTableReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_pedigree_ids', 'output_pedigree_ids'], [],
            ['column_names_on_line', 'file_name', 'header_lines', 'max_records',
            'pedigree_id_array_name', 'skip_column_names']),
            title='Edit TecplotTableReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TecplotTableReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


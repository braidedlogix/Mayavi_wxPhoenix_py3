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


class RISReader(TableAlgorithm):
    """
    RISReader - reader for RIS files
    
    Superclass: TableAlgorithm
    
    RIS is a tagged format for expressing bibliographic citations.  Data
    is structured as a collection of records with each record composed of
    one-to-many fields.  See
    
    http://en.wikipedia.org/wiki/RIS_(file_format)
    http://www.refman.com/support/risformat_intro.asp
    http://www.adeptscience.co.uk/kb/article/A626
    
    for details.  RISReader will convert an RIS file into a Table,
    with the set of table columns determined dynamically from the
    contents of the file.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRISReader, obj, update, **traits)
    
    delimiter = traits.String(';', enter_set=True, auto_set=False, help=\
        """
        Set/get the delimiter to be used for concatenating field data
        (default: ";")
        """
    )

    def _delimiter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDelimiter,
                        self.delimiter)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/get the file to load
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    max_records = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get the maximum number of records to read from the file (zero
        = unlimited)
        """
    )

    def _max_records_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxRecords,
                        self.max_records)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('delimiter',
    'GetDelimiter'), ('file_name', 'GetFileName'), ('max_records',
    'GetMaxRecords'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'delimiter', 'file_name', 'max_records',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RISReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RISReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['delimiter', 'file_name', 'max_records']),
            title='Edit RISReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RISReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


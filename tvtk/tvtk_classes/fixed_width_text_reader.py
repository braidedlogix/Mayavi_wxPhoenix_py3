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


class FixedWidthTextReader(TableAlgorithm):
    """
    FixedWidthTextReader - reader for pulling in text files with
    fixed-width fields
    
    Superclass: TableAlgorithm
    
    FixedWidthTextReader reads in a table from a text file where each
    column occupies a certain number of characters.
    
    This class emits progress_event for every 100 lines it reads.
    
    @warning
    This first version of the reader will assume that all fields have the
    same width.  It also assumes that the first line in the file has at
    least as many fields (i.e. at least as many characters) as any other
    line in the file.
    
    @par Thanks: Thanks to Andy Wilson from Sandia National Laboratories
    for implementing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFixedWidthTextReader, obj, update, **traits)
    
    have_headers = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether to treat the first line of the file as headers.
        """
    )

    def _have_headers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHaveHeaders,
                        self.have_headers_)

    strip_white_space = tvtk_base.false_bool_trait(help=\
        """
        If set, this flag will cause the reader to strip whitespace from
        the beginning and ending of each field.  Defaults to off.
        """
    )

    def _strip_white_space_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStripWhiteSpace,
                        self.strip_white_space_)

    field_width = traits.Int(10, enter_set=True, auto_set=False, help=\
        """
        Set/get the field width
        """
    )

    def _field_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldWidth,
                        self.field_width)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_table_error_observer(self):
        return wrap_vtk(self._vtk_obj.GetTableErrorObserver())
    def _set_table_error_observer(self, arg):
        old_val = self._get_table_error_observer()
        self._wrap_call(self._vtk_obj.SetTableErrorObserver,
                        deref_vtk(arg))
        self.trait_property_changed('table_error_observer', old_val, arg)
    table_error_observer = traits.Property(_get_table_error_observer, _set_table_error_observer, help=\
        """
        Set/get the error_observer for the internal Table This is
        useful for applications that want to catch error messages.
        """
    )

    _updateable_traits_ = \
    (('have_headers', 'GetHaveHeaders'), ('strip_white_space',
    'GetStripWhiteSpace'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('field_width',
    'GetFieldWidth'), ('file_name', 'GetFileName'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'have_headers',
    'release_data_flag', 'strip_white_space', 'field_width', 'file_name',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FixedWidthTextReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FixedWidthTextReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['have_headers', 'strip_white_space'], [], ['field_width',
            'file_name']),
            title='Edit FixedWidthTextReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FixedWidthTextReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


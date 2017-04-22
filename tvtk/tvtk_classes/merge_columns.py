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


class MergeColumns(TableAlgorithm):
    """
    MergeColumns - merge two columns into a single column
    
    Superclass: TableAlgorithm
    
    MergeColumns replaces two columns in a table with a single column
    containing data in both columns.  The columns are set using
    
    
      set_input_array_to_process(_0, 0, 0,
    DataObject::FIELD_ASSOCIATION_ROWS, "col1")
    
    and
    
    
      set_input_array_to_process(_1, 0, 0,
    DataObject::FIELD_ASSOCIATION_ROWS, "col2")
    
    where "col1" and "col2" are the names of the columns to merge. The
    user may also specify the name of the merged column. The arrays must
    be of the same type. If the arrays are numeric, the values are summed
    in the merged column. If the arrays are strings, the values are
    concatenated.  The strings are separated by a space if they are both
    nonempty.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMergeColumns, obj, update, **traits)
    
    merged_column_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The name to give the merged column created by this filter.
        """
    )

    def _merged_column_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMergedColumnName,
                        self.merged_column_name)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('merged_column_name', 'GetMergedColumnName'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'merged_column_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MergeColumns, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MergeColumns properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['merged_column_name']),
            title='Edit MergeColumns properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MergeColumns properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


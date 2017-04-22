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


class MergeTables(TableAlgorithm):
    """
    MergeTables - combine two tables
    
    Superclass: TableAlgorithm
    
    Combines the columns of two tables into one larger table. The number
    of rows in the resulting table is the sum of the number of rows in
    each of the input tables. The number of columns in the output is
    generally the sum of the number of columns in each input table,
    except in the case where column names are duplicated in both tables.
    In this case, if merge_columns_by_name is on (the default), the two
    columns will be merged into a single column of the same name. If
    merge_columns_by_name is off, both columns will exist in the output. You
    may set the first_table_prefix and second_table_prefix to define how the
    columns named are modified.  One of these prefixes may be the empty
    string, but they must be different.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMergeTables, obj, update, **traits)
    
    merge_columns_by_name = tvtk_base.true_bool_trait(help=\
        """
        If on, merges columns with the same name. If off, keeps both
        columns, but calls one first_table_prefix + name, and the other
        second_table_prefix + name. Default is on.
        """
    )

    def _merge_columns_by_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMergeColumnsByName,
                        self.merge_columns_by_name_)

    prefix_all_but_merged = tvtk_base.false_bool_trait(help=\
        """
        If on, all columns will have prefixes except merged columns. If
        off, only unmerged columns with the same name will have prefixes.
        Default is off.
        """
    )

    def _prefix_all_but_merged_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPrefixAllButMerged,
                        self.prefix_all_but_merged_)

    first_table_prefix = traits.String('Table1.', enter_set=True, auto_set=False, help=\
        """
        The prefix to give to same-named fields from the first table.
        Default is "Table1.".
        """
    )

    def _first_table_prefix_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFirstTablePrefix,
                        self.first_table_prefix)

    second_table_prefix = traits.String('Table2.', enter_set=True, auto_set=False, help=\
        """
        The prefix to give to same-named fields from the second table.
        Default is "Table2.".
        """
    )

    def _second_table_prefix_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSecondTablePrefix,
                        self.second_table_prefix)

    _updateable_traits_ = \
    (('merge_columns_by_name', 'GetMergeColumnsByName'),
    ('prefix_all_but_merged', 'GetPrefixAllButMerged'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('first_table_prefix',
    'GetFirstTablePrefix'), ('second_table_prefix',
    'GetSecondTablePrefix'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'merge_columns_by_name', 'prefix_all_but_merged', 'release_data_flag',
    'first_table_prefix', 'progress_text', 'second_table_prefix'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MergeTables, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MergeTables properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['merge_columns_by_name', 'prefix_all_but_merged'], [],
            ['first_table_prefix', 'second_table_prefix']),
            title='Edit MergeTables properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MergeTables properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


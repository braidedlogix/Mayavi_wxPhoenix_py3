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


class TransposeTable(TableAlgorithm):
    """
    TransposeTable - Transpose an input table.
    
    Superclass: TableAlgorithm
    
    This algorithm allows to transpose a Table as a matrix. Columns
    become rows and vice versa. A new column can be added to the result
    table at index 0 to collect the name of the initial columns (when
    add_id_column is true). Such a column can be used to name the columns
    of the result. Note that columns of the output table will have a
    variant type is the columns of the initial table are not consistant.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTransposeTable, obj, update, **traits)
    
    add_id_column = tvtk_base.true_bool_trait(help=\
        """
        This flag indicates if a column must be inserted at index 0 with
        the names (ids) of the input columns. Default: true
        """
    )

    def _add_id_column_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAddIdColumn,
                        self.add_id_column_)

    use_id_column = tvtk_base.false_bool_trait(help=\
        """
        This flag indicates if the output column must be named using the
        names listed in the index 0 column. Default: false
        """
    )

    def _use_id_column_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseIdColumn,
                        self.use_id_column_)

    id_column_name = traits.String('ColName', enter_set=True, auto_set=False, help=\
        """
        Get/Set the name of the id column added by option add_id_column.
        Default: col_name
        """
    )

    def _id_column_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIdColumnName,
                        self.id_column_name)

    _updateable_traits_ = \
    (('add_id_column', 'GetAddIdColumn'), ('use_id_column',
    'GetUseIdColumn'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('id_column_name', 'GetIdColumnName'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'add_id_column', 'debug', 'global_warning_display',
    'release_data_flag', 'use_id_column', 'id_column_name',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TransposeTable, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TransposeTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['add_id_column', 'use_id_column'], [], ['id_column_name']),
            title='Edit TransposeTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TransposeTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


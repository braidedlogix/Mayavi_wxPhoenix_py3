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


class ReduceTable(TableAlgorithm):
    """
    ReduceTable - combine some of the rows of a table
    
    Superclass: TableAlgorithm
    
    Collapses the rows of the input table so that one particular column
    (the index_column) does not contain any duplicate values. Thus the
    output table will have the same columns as the input table, but
    potentially fewer rows.  One example use of this class would be to
    generate a summary table from a table of observations. When two or
    more rows of the input table share a value in the index_column, the
    values from these rows will be combined on a column-by-column basis. 
    By default, such numerical values will be reduced to their mean, and
    non-numerical values will be reduced to their mode.  This default
    behavior can be changed by calling set_numerical_reduction_method() or
    set_non_numerical_reduction_method(). You can also specify the reduction
    method to use for a particular column by calling
    set_reduction_method_for_column().
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkReduceTable, obj, update, **traits)
    
    index_column = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Get/Set the column that will be used to reduce the input table.
        Any rows sharing a value in this column will be collapsed into a
        single row in the output table.
        """
    )

    def _index_column_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIndexColumn,
                        self.index_column)

    non_numerical_reduction_method = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Get/Set the method that should be used to combine non-numerical
        values.
        """
    )

    def _non_numerical_reduction_method_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNonNumericalReductionMethod,
                        self.non_numerical_reduction_method)

    numerical_reduction_method = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the method that should be used to combine numerical
        values.
        """
    )

    def _numerical_reduction_method_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumericalReductionMethod,
                        self.numerical_reduction_method)

    def get_reduction_method_for_column(self, *args):
        """
        V.get_reduction_method_for_column(int) -> int
        C++: int GetReductionMethodForColumn(IdType col)
        Get the method that should be used to combine the values within
        the specified column.  Returns -1 if no method has been set for
        this particular column.
        """
        ret = self._wrap_call(self._vtk_obj.GetReductionMethodForColumn, *args)
        return ret

    def set_reduction_method_for_column(self, *args):
        """
        V.set_reduction_method_for_column(int, int)
        C++: void SetReductionMethodForColumn(IdType col, int method)
        Set the method that should be used to combine the values within
        the specified column.
        """
        ret = self._wrap_call(self._vtk_obj.SetReductionMethodForColumn, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('index_column', 'GetIndexColumn'), ('non_numerical_reduction_method',
    'GetNonNumericalReductionMethod'), ('numerical_reduction_method',
    'GetNumericalReductionMethod'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'index_column', 'non_numerical_reduction_method',
    'numerical_reduction_method', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ReduceTable, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ReduceTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['index_column', 'non_numerical_reduction_method',
            'numerical_reduction_method']),
            title='Edit ReduceTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ReduceTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


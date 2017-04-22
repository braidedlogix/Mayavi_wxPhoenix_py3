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

from tvtk.tvtk_classes.array_data_algorithm import ArrayDataAlgorithm


class TableToSparseArray(ArrayDataAlgorithm):
    """
    TableToSparseArray - converts a Table into a sparse array.
    
    Superclass: ArrayDataAlgorithm
    
    Converts a Table into a sparse array.  Use add_coordinate_column()
    to designate one-to-many table columns that contain coordinates for
    each array value, and set_value_column() to designate the table column
    that contains array values.
    
    Thus, the number of dimensions in the output array will equal the
    number of calls to add_coordinate_column().
    
    The coordinate columns will also be used to populate dimension labels
    in the output array.
    
    By default, the extent of the output array will be set to the range
    [0, largest coordinate + 1) along each dimension.  In some situations
    you may prefer to set the extents explicitly, using the
    set_output_extents() method.  This is useful when the output array
    should be larger than its largest coordinates, or when working with
    partitioned data.
    
    @par Thanks: Developed by Timothy M. Shead (tshead@sandia.gov) at
    Sandia National Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTableToSparseArray, obj, update, **traits)
    
    value_column = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Specify the input table column that will be mapped to values in
        the output array.
        """
    )

    def _value_column_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValueColumn,
                        self.value_column)

    def add_coordinate_column(self, *args):
        """
        V.add_coordinate_column(string)
        C++: void AddCoordinateColumn(const char *name)
        Specify the set of input table columns that will be mapped to
        coordinates in the output sparse array.
        """
        ret = self._wrap_call(self._vtk_obj.AddCoordinateColumn, *args)
        return ret

    def clear_coordinate_columns(self):
        """
        V.clear_coordinate_columns()
        C++: void ClearCoordinateColumns()
        Specify the set of input table columns that will be mapped to
        coordinates in the output sparse array.
        """
        ret = self._vtk_obj.ClearCoordinateColumns()
        return ret
        

    def clear_output_extents(self):
        """
        V.clear_output_extents()
        C++: void ClearOutputExtents()
        Explicitly specify the extents of the output array.
        """
        ret = self._vtk_obj.ClearOutputExtents()
        return ret
        

    def set_output_extents(self, *args):
        """
        V.set_output_extents(ArrayExtents)
        C++: void SetOutputExtents(const ArrayExtents &extents)
        Explicitly specify the extents of the output array.
        """
        my_args = deref_array(args, [['vtkArrayExtents']])
        ret = self._wrap_call(self._vtk_obj.SetOutputExtents, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('value_column', 'GetValueColumn'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'value_column'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TableToSparseArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TableToSparseArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['value_column']),
            title='Edit TableToSparseArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TableToSparseArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


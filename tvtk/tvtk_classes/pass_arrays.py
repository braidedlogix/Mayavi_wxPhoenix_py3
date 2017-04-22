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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class PassArrays(DataObjectAlgorithm):
    """
    PassArrays - Passes a subset of arrays to the output
    
    Superclass: DataObjectAlgorithm
    
    This filter preserves all the topology of the input, but only a
    subset of arrays are passed to the output. Add an array to be passed
    to the output data object with add_array(). If remove_arrays is on, the
    specified arrays will be the ones that are removed instead of the
    ones that are kept.
    
    Arrays with special attributes (scalars, pedigree ids, etc.) will
    retain those attributes in the output.
    
    By default, only those field types with at least one array specified
    through add_array will be processed. If instead use_field_types is
    turned on, you explicitly set which field types to process with
    add_field_type.
    
    Example 1:
    
    pass_array->_add_array(vtk_data_object::_point, "velocity"); 
    
    The output will have only that one array "velocity" in the point
    data, but cell and field data will be untouched.
    
    Example 2:
    
    pass_array->_add_array(vtk_data_object::_point, "velocity");
    pass_array->_use_field_types_on();
    pass_array->_add_field_type(vtk_data_object::_point);
    pass_array->_add_field_type(vtk_data_object::_cell); 
    
    The point data would still contain the single array, but the cell
    data would be cleared since you did not specify any arrays to pass.
    Field data would still be untouched.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPassArrays, obj, update, **traits)
    
    remove_arrays = tvtk_base.false_bool_trait(help=\
        """
        Instead of passing only the specified arrays, remove the
        specified arrays and keep all other arrays. Default is off.
        """
    )

    def _remove_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRemoveArrays,
                        self.remove_arrays_)

    use_field_types = tvtk_base.false_bool_trait(help=\
        """
        Process only those field types explicitly specified with
        add_field_type. Otherwise, processes field types associated with at
        least one specified array. Default is off.
        """
    )

    def _use_field_types_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseFieldTypes,
                        self.use_field_types_)

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

    def add_array(self, *args):
        """
        V.add_array(int, string)
        C++: virtual void AddArray(int fieldType, const char *name)
        Adds an array to pass through. field_type where the array that
        should be passed (point data, cell data, etc.). It should be one
        of the constants defined in the DataObject::AttributeTypes
        enumeration.
        """
        ret = self._wrap_call(self._vtk_obj.AddArray, *args)
        return ret

    def add_cell_data_array(self, *args):
        """
        V.add_cell_data_array(string)
        C++: virtual void AddCellDataArray(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.AddCellDataArray, *args)
        return ret

    def add_field_data_array(self, *args):
        """
        V.add_field_data_array(string)
        C++: virtual void AddFieldDataArray(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.AddFieldDataArray, *args)
        return ret

    def add_field_type(self, *args):
        """
        V.add_field_type(int)
        C++: virtual void AddFieldType(int fieldType)
        Add a field type to process. field_type where the array that
        should be passed (point data, cell data, etc.). It should be one
        of the constants defined in the DataObject::AttributeTypes
        enumeration. NOTE: These are only used if use_field_type is turned
        on.
        """
        ret = self._wrap_call(self._vtk_obj.AddFieldType, *args)
        return ret

    def add_point_data_array(self, *args):
        """
        V.add_point_data_array(string)
        C++: virtual void AddPointDataArray(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.AddPointDataArray, *args)
        return ret

    def clear_arrays(self):
        """
        V.clear_arrays()
        C++: virtual void ClearArrays()
        Clear all arrays to pass through.
        """
        ret = self._vtk_obj.ClearArrays()
        return ret
        

    def clear_cell_data_arrays(self):
        """
        V.clear_cell_data_arrays()
        C++: virtual void ClearCellDataArrays()
        Clear all arrays to pass through.
        """
        ret = self._vtk_obj.ClearCellDataArrays()
        return ret
        

    def clear_field_data_arrays(self):
        """
        V.clear_field_data_arrays()
        C++: virtual void ClearFieldDataArrays()
        Clear all arrays to pass through.
        """
        ret = self._vtk_obj.ClearFieldDataArrays()
        return ret
        

    def clear_field_types(self):
        """
        V.clear_field_types()
        C++: virtual void ClearFieldTypes()
        Clear all field types to process.
        """
        ret = self._vtk_obj.ClearFieldTypes()
        return ret
        

    def clear_point_data_arrays(self):
        """
        V.clear_point_data_arrays()
        C++: virtual void ClearPointDataArrays()
        Clear all arrays to pass through.
        """
        ret = self._vtk_obj.ClearPointDataArrays()
        return ret
        

    def remove_array(self, *args):
        """
        V.remove_array(int, string)
        C++: virtual void RemoveArray(int fieldType, const char *name)"""
        ret = self._wrap_call(self._vtk_obj.RemoveArray, *args)
        return ret

    def remove_cell_data_array(self, *args):
        """
        V.remove_cell_data_array(string)
        C++: virtual void RemoveCellDataArray(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.RemoveCellDataArray, *args)
        return ret

    def remove_field_data_array(self, *args):
        """
        V.remove_field_data_array(string)
        C++: virtual void RemoveFieldDataArray(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.RemoveFieldDataArray, *args)
        return ret

    def remove_point_data_array(self, *args):
        """
        V.remove_point_data_array(string)
        C++: virtual void RemovePointDataArray(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.RemovePointDataArray, *args)
        return ret

    _updateable_traits_ = \
    (('remove_arrays', 'GetRemoveArrays'), ('use_field_types',
    'GetUseFieldTypes'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'remove_arrays', 'use_field_types',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PassArrays, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PassArrays properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['remove_arrays', 'use_field_types'], [], []),
            title='Edit PassArrays properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PassArrays properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


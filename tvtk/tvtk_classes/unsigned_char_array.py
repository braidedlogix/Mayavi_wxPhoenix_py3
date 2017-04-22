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

from tvtk.tvtk_classes.data_array import DataArray


class UnsignedCharArray(DataArray):
    """
    UnsignedCharArray - dynamic, self-adjusting array of unsigned char
    
    Superclass: DataArray
    
    UnsignedCharArray is an array of values of type unsigned char. It
    provides methods for insertion and retrieval of values and will
    automatically resize itself to hold new data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnsignedCharArray, obj, update, **traits)
    
    number_of_values = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _number_of_values_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfValues,
                        self.number_of_values)

    def get_typed_tuple(self, *args):
        """
        V.get_typed_tuple(int, [int, ...])
        C++: void GetTypedTuple(IdType i, unsigned char *tuple)"""
        ret = self._wrap_call(self._vtk_obj.GetTypedTuple, *args)
        return ret

    def set_typed_tuple(self, *args):
        """
        V.set_typed_tuple(int, (int, ...))
        C++: void SetTypedTuple(IdType i, const unsigned char *tuple)"""
        ret = self._wrap_call(self._vtk_obj.SetTypedTuple, *args)
        return ret

    def get_value(self, *args):
        """
        V.get_value(int) -> int
        C++: unsigned char GetValue(IdType id)"""
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, int)
        C++: void SetValue(IdType id, unsigned char value)"""
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

    def _get_data_type_value_max(self):
        return self._vtk_obj.GetDataTypeValueMax()
    data_type_value_max = traits.Property(_get_data_type_value_max, help=\
        """
        Get the maximum data value in its native type.
        """
    )

    def _get_data_type_value_min(self):
        return self._vtk_obj.GetDataTypeValueMin()
    data_type_value_min = traits.Property(_get_data_type_value_min, help=\
        """
        Get the minimum data value in its native type.
        """
    )

    def get_pointer(self, *args):
        """
        V.get_pointer(int) -> (int, ...)
        C++: unsigned char *GetPointer(IdType id)"""
        ret = self._wrap_call(self._vtk_obj.GetPointer, *args)
        return ret

    def _get_value_range(self):
        return self._vtk_obj.GetValueRange()
    value_range = traits.Property(_get_value_range, help=\
        """
        
        """
    )

    def insert_next_typed_tuple(self, *args):
        """
        V.insert_next_typed_tuple((int, ...)) -> int
        C++: IdType InsertNextTypedTuple(const unsigned char *tuple)"""
        ret = self._wrap_call(self._vtk_obj.InsertNextTypedTuple, *args)
        return ret

    def insert_next_value(self, *args):
        """
        V.insert_next_value(int) -> int
        C++: IdType InsertNextValue(unsigned char f)"""
        ret = self._wrap_call(self._vtk_obj.InsertNextValue, *args)
        return ret

    def insert_typed_tuple(self, *args):
        """
        V.insert_typed_tuple(int, (int, ...))
        C++: void InsertTypedTuple(IdType i,
            const unsigned char *tuple)"""
        ret = self._wrap_call(self._vtk_obj.InsertTypedTuple, *args)
        return ret

    def insert_value(self, *args):
        """
        V.insert_value(int, int)
        C++: void InsertValue(IdType id, unsigned char f)"""
        ret = self._wrap_call(self._vtk_obj.InsertValue, *args)
        return ret

    def write_pointer(self, *args):
        """
        V.write_pointer(int, int) -> (int, ...)
        C++: unsigned char *WritePointer(IdType id, IdType number)"""
        ret = self._wrap_call(self._vtk_obj.WritePointer, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_values', 'GetNumberOfValues'),
    ('max_discrete_values', 'GetMaxDiscreteValues'), ('name', 'GetName'),
    ('number_of_components', 'GetNumberOfComponents'),
    ('number_of_tuples', 'GetNumberOfTuples'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'max_discrete_values', 'name',
    'number_of_components', 'number_of_tuples', 'number_of_values'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UnsignedCharArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UnsignedCharArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['max_discrete_values', 'name', 'number_of_components',
            'number_of_tuples', 'number_of_values']),
            title='Edit UnsignedCharArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnsignedCharArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


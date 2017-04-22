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


class BitArray(DataArray):
    """
    BitArray - dynamic, self-adjusting array of bits
    
    Superclass: DataArray
    
    BitArray is an array of bits (0/1 data value). The array is packed
    so that each byte stores eight bits. BitArray provides methods for
    insertion and retrieval of bits, and will automatically resize itself
    to hold new data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBitArray, obj, update, **traits)
    
    def get_component(self, *args):
        """
        V.get_component(int, int) -> float
        C++: virtual double GetComponent(IdType tupleIdx, int compIdx)
        Return the data component at the location specified by tuple_idx
        and comp_idx.
        """
        ret = self._wrap_call(self._vtk_obj.GetComponent, *args)
        return ret

    def set_component(self, *args):
        """
        V.set_component(int, int, float)
        
        Set the data component at the ith tuple and jth component
        location. Note that i is less then number_of_tuples and j is less
        then number_of_components. Make sure enough memory has been
        allocated (use set_number_of_tuples() and  set_number_of_components()).
        """
        ret = self._wrap_call(self._vtk_obj.SetComponent, *args)
        return ret

    number_of_tuples = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of n-tuples in the array.
        """
    )

    def _number_of_tuples_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTuples,
                        self.number_of_tuples)

    number_of_values = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Fast method based setting of values without memory checks. First
        use set_number_of_values then use set_value to actually set them.
        Specify the number of values for this object to hold. Does an
        allocation as well as setting the max_id ivar. Used in conjunction
        with set_value() method for fast insertion.
        """
    )

    def _number_of_values_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfValues,
                        self.number_of_values)

    def get_tuple(self, *args):
        """
        V.get_tuple(int) -> (float, ...)
        V.get_tuple(int, [float, ...])
        
        Get a pointer to a tuple at the ith location. This is a dangerous
        method (it is not thread safe since a pointer is returned).
        """
        ret = self._wrap_call(self._vtk_obj.GetTuple, *args)
        return ret

    def set_tuple(self, *args):
        """
        V.set_tuple(int, int, AbstractArray)
        C++: void SetTuple(IdType i, IdType j,
            AbstractArray *source) override;
        V.set_tuple(int, (float, ...))
        
        Set the tuple at the ith location using the jth tuple in the
        source array. This method assumes that the two arrays have the
        same type and structure. Note that range checking and memory
        allocation is not performed; use in conjunction with
        set_number_of_tuples() to allocate space.
        """
        my_args = deref_array(args, [('int', 'int', 'vtkAbstractArray'), ('int', 'tuple')])
        ret = self._wrap_call(self._vtk_obj.SetTuple, *my_args)
        return ret

    def get_value(self, *args):
        """
        V.get_value(int) -> int
        C++: int GetValue(IdType id)
        Get the data at a particular index.
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, int)
        C++: void SetValue(IdType id, int value)
        Set the data at a particular index. Does not do range checking.
        Make sure you use the method set_number_of_values() before inserting
        data.
        """
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

    def get_variant_value(self, *args):
        """
        V.get_variant_value(int) -> Variant
        C++: virtual Variant GetVariantValue(IdType valueIdx)
        Retrieve value from the array as a variant.
        """
        ret = self._wrap_call(self._vtk_obj.GetVariantValue, *args)
        return wrap_vtk(ret)

    def set_variant_value(self, *args):
        """
        V.set_variant_value(int, Variant)
        C++: void SetVariantValue(IdType idx, Variant value)
            override;
        Set a value in the array from a variant.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetVariantValue, *my_args)
        return ret

    def get_pointer(self, *args):
        """
        V.get_pointer(int) -> (int, ...)
        C++: unsigned char *GetPointer(IdType id)
        Direct manipulation of the underlying data.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointer, *args)
        return ret

    def insert_next_value(self, *args):
        """
        V.insert_next_value(int) -> int
        C++: IdType InsertNextValue(int i)"""
        ret = self._wrap_call(self._vtk_obj.InsertNextValue, *args)
        return ret

    def insert_value(self, *args):
        """
        V.insert_value(int, int)
        C++: void InsertValue(IdType id, int i)
        Inserts values and checks to make sure there is enough memory
        """
        ret = self._wrap_call(self._vtk_obj.InsertValue, *args)
        return ret

    def write_pointer(self, *args):
        """
        V.write_pointer(int, int) -> (int, ...)
        C++: unsigned char *WritePointer(IdType id, IdType number)
        Get the address of a particular data index. Make sure data is
        allocated for the number of items requested. Set max_id according
        to the number of data values requested.
        """
        ret = self._wrap_call(self._vtk_obj.WritePointer, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_tuples', 'GetNumberOfTuples'),
    ('number_of_values', 'GetNumberOfValues'), ('max_discrete_values',
    'GetMaxDiscreteValues'), ('name', 'GetName'), ('number_of_components',
    'GetNumberOfComponents'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'max_discrete_values', 'name',
    'number_of_components', 'number_of_tuples', 'number_of_values'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BitArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BitArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['max_discrete_values', 'name', 'number_of_components',
            'number_of_tuples', 'number_of_values']),
            title='Edit BitArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BitArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


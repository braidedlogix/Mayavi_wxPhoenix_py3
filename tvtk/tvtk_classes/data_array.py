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

from tvtk.tvtk_classes.abstract_array import AbstractArray


class DataArray(AbstractArray):
    """
    DataArray - abstract superclass for arrays of numeric data
    
    Superclass: AbstractArray
    
    DataArray is an abstract superclass for data array objects
    containing numeric data.  It extends the API defined in
    AbstractArray.  DataArray is an abstract superclass for data
    array objects. This class defines an API that all array objects must
    support. Note that the concrete subclasses of this class represent
    data in native form (char, int, etc.) and often have specialized more
    efficient methods for operating on this data (for example, getting
    pointers to data or getting/inserting data in native form). 
    Subclasses of DataArray are assumed to contain data whose
    components are meaningful when cast to and from double.
    
    @sa
    BitArray GenericDataArray
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataArray, obj, update, **traits)
    
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
        C++: virtual void SetComponent(IdType tupleIdx, int compIdx,
            double value)
        Set the data component at the location specified by tuple_idx and
        comp_idx to value. Note that i is less than number_of_tuples and j
        is less than number_of_components. Make sure enough memory has been
        allocated (use set_number_of_tuples() and set_number_of_components()).
        """
        ret = self._wrap_call(self._vtk_obj.SetComponent, *args)
        return ret

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Set/get the lookup table associated with this scalar data, if
        any.
        """
    )

    def get_tuple(self, *args):
        """
        V.get_tuple(int) -> (float, ...)
        C++: virtual double *GetTuple(IdType tupleIdx)
        V.get_tuple(int, [float, ...])
        C++: virtual void GetTuple(IdType tupleIdx, double *tuple)
        Get the data tuple at tuple_idx. Return it as a pointer to an
        array. Note: this method is not thread-safe, and the pointer is
        only valid as long as another method invocation to a vtk object
        is not performed.
        """
        ret = self._wrap_call(self._vtk_obj.GetTuple, *args)
        return ret

    def set_tuple(self, *args):
        """
        V.set_tuple(int, int, AbstractArray)
        C++: void SetTuple(IdType dstTupleIdx, IdType srcTupleIdx,
            AbstractArray *source) override;
        V.set_tuple(int, (float, ...))
        C++: virtual void SetTuple(IdType tupleIdx,
            const double *tuple)"""
        my_args = deref_array(args, [('int', 'int', 'vtkAbstractArray'), ('int', 'tuple')])
        ret = self._wrap_call(self._vtk_obj.SetTuple, *my_args)
        return ret

    def get_tuple1(self, *args):
        """
        V.get_tuple1(int) -> float
        C++: double GetTuple1(IdType tupleIdx)
        These methods are included as convenience for the wrappers.
        get_tuple() and set_tuple() which return/take arrays can not be
        used from wrapped languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.GetTuple1, *args)
        return ret

    def set_tuple1(self, *args):
        """
        V.set_tuple1(int, float)
        C++: void SetTuple1(IdType tupleIdx, double value)
        These methods are included as convenience for the wrappers.
        get_tuple() and set_tuple() which return/take arrays can not be
        used from wrapped languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.SetTuple1, *args)
        return ret

    def get_tuple2(self, *args):
        """
        V.get_tuple2(int) -> (float, float)
        C++: double *GetTuple2(IdType tupleIdx)
        These methods are included as convenience for the wrappers.
        get_tuple() and set_tuple() which return/take arrays can not be
        used from wrapped languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.GetTuple2, *args)
        return ret

    def set_tuple2(self, *args):
        """
        V.set_tuple2(int, float, float)
        C++: void SetTuple2(IdType tupleIdx, double val0, double val1)
        These methods are included as convenience for the wrappers.
        get_tuple() and set_tuple() which return/take arrays can not be
        used from wrapped languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.SetTuple2, *args)
        return ret

    def get_tuple3(self, *args):
        """
        V.get_tuple3(int) -> (float, float, float)
        C++: double *GetTuple3(IdType tupleIdx)
        These methods are included as convenience for the wrappers.
        get_tuple() and set_tuple() which return/take arrays can not be
        used from wrapped languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.GetTuple3, *args)
        return ret

    def set_tuple3(self, *args):
        """
        V.set_tuple3(int, float, float, float)
        C++: void SetTuple3(IdType tupleIdx, double val0, double val1,
            double val2)
        These methods are included as convenience for the wrappers.
        get_tuple() and set_tuple() which return/take arrays can not be
        used from wrapped languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.SetTuple3, *args)
        return ret

    def get_tuple4(self, *args):
        """
        V.get_tuple4(int) -> (float, float, float, float)
        C++: double *GetTuple4(IdType tupleIdx)
        These methods are included as convenience for the wrappers.
        get_tuple() and set_tuple() which return/take arrays can not be
        used from wrapped languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.GetTuple4, *args)
        return ret

    def set_tuple4(self, *args):
        """
        V.set_tuple4(int, float, float, float, float)
        C++: void SetTuple4(IdType tupleIdx, double val0, double val1,
            double val2, double val3)
        These methods are included as convenience for the wrappers.
        get_tuple() and set_tuple() which return/take arrays can not be
        used from wrapped languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.SetTuple4, *args)
        return ret

    def get_tuple6(self, *args):
        """
        V.get_tuple6(int) -> (float, float, float, float, float, float)
        C++: double *GetTuple6(IdType tupleIdx)
        These methods are included as convenience for the wrappers.
        get_tuple() and set_tuple() which return/take arrays can not be
        used from wrapped languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.GetTuple6, *args)
        return ret

    def set_tuple6(self, *args):
        """
        V.set_tuple6(int, float, float, float, float, float, float)
        C++: void SetTuple6(IdType tupleIdx, double val0, double val1,
            double val2, double val3, double val4, double val5)
        These methods are included as convenience for the wrappers.
        get_tuple() and set_tuple() which return/take arrays can not be
        used from wrapped languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.SetTuple6, *args)
        return ret

    def get_tuple9(self, *args):
        """
        V.get_tuple9(int) -> (float, float, float, float, float, float,
            float, float, float)
        C++: double *GetTuple9(IdType tupleIdx)
        These methods are included as convenience for the wrappers.
        get_tuple() and set_tuple() which return/take arrays can not be
        used from wrapped languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.GetTuple9, *args)
        return ret

    def set_tuple9(self, *args):
        """
        V.set_tuple9(int, float, float, float, float, float, float, float,
            float, float)
        C++: void SetTuple9(IdType tupleIdx, double val0, double val1,
            double val2, double val3, double val4, double val5,
            double val6, double val7, double val8)
        These methods are included as convenience for the wrappers.
        get_tuple() and set_tuple() which return/take arrays can not be
        used from wrapped languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.SetTuple9, *args)
        return ret

    def get_data(self, *args):
        """
        V.get_data(int, int, int, int, DoubleArray)
        C++: virtual void GetData(IdType tupleMin, IdType tupleMax,
            int compMin, int compMax, DoubleArray *data)
        Get the data as a double array in the range (tuple_min,tuple_max)
        and (comp_min, comp_max). The resulting double array consists of
        all data in the tuple range specified and only the component
        range specified. This process typically requires casting the data
        from native form into doubleing point values. This method is
        provided as a convenience for data exchange, and is not very
        fast.
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'int', 'vtkDoubleArray')])
        ret = self._wrap_call(self._vtk_obj.GetData, *my_args)
        return ret

    def _get_data_type_max(self):
        return self._vtk_obj.GetDataTypeMax()
    data_type_max = traits.Property(_get_data_type_max, help=\
        """
        These methods return the Min and Max possible range of the native
        data type. For example if a Scalars consists of unsigned char
        data these will return (0,255).
        """
    )

    def _get_data_type_min(self):
        return self._vtk_obj.GetDataTypeMin()
    data_type_min = traits.Property(_get_data_type_min, help=\
        """
        These methods return the Min and Max possible range of the native
        data type. For example if a Scalars consists of unsigned char
        data these will return (0,255).
        """
    )

    def get_data_type_range(self, *args):
        """
        V.get_data_type_range([float, float])
        C++: void GetDataTypeRange(double range[2])
        V.get_data_type_range(int, [float, float])
        C++: static void GetDataTypeRange(int type, double range[2])
        These methods return the Min and Max possible range of the native
        data type. For example if a Scalars consists of unsigned char
        data these will return (0,255).
        """
        ret = self._wrap_call(self._vtk_obj.GetDataTypeRange, *args)
        return ret

    def _get_max_norm(self):
        return self._vtk_obj.GetMaxNorm()
    max_norm = traits.Property(_get_max_norm, help=\
        """
        Return the maximum norm for the tuples. Note that the max. is
        computed every time get_max_norm is called.
        """
    )

    def _get_range(self):
        return self._vtk_obj.GetRange()
    range = traits.Property(_get_range, help=\
        """
        The range of the data array values for the given component will
        be returned in the provided range array argument. If comp is -1,
        the range of the magnitude (L2 norm) over all components will be
        provided. The range is computed and then cached, and will not be
        re-computed on subsequent calls to get_range() unless the array is
        modified or the requested component changes. THIS METHOD IS NOT
        THREAD SAFE.
        """
    )

    def COMPONENT_RANGE(self):
        """
        V.component__range() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *COMPONENT_RANGE()
        This key is used to hold tight bounds on the range of one
        component over all tuples of the array. Two values (a minimum and
        maximum) are stored for each component. When get_range() is called
        when no tuples are present in the array this value is set to {
        VTK_DOUBLE_MAX, VTK_DOUBLE_MIN }.
        """
        ret = wrap_vtk(self._vtk_obj.COMPONENT_RANGE())
        return ret
        

    def copy_component(self, *args):
        """
        V.copy_component(int, DataArray, int)
        C++: virtual void CopyComponent(int dstComponent,
            DataArray *src, int srcComponent)
        Copy a component from one data array into a component on this
        data array. This method copies the specified component
        ("src_component") from the specified data array ("src") to the
        specified component ("dst_component") over all the tuples in this
        data array.  This method can be used to extract a component
        (column) from one data array and paste that data into a component
        on this data array.
        """
        my_args = deref_array(args, [('int', 'vtkDataArray', 'int')])
        ret = self._wrap_call(self._vtk_obj.CopyComponent, *my_args)
        return ret

    def create_data_array(self, *args):
        """
        V.create_data_array(int) -> DataArray
        C++: static DataArray *CreateDataArray(int dataType)
        Creates an array for data_type where data_type is one of VTK_BIT,
        VTK_CHAR, VTK_SIGNED_CHAR, VTK_UNSIGNED_CHAR, VTK_SHORT,
        VTK_UNSIGNED_SHORT, VTK_INT, VTK_UNSIGNED_INT, VTK_LONG,
        VTK_UNSIGNED_LONG, VTK_DOUBLE, VTK_DOUBLE, VTK_ID_TYPE. Note that
        the data array returned has be deleted by the user.
        """
        ret = self._wrap_call(self._vtk_obj.CreateDataArray, *args)
        return wrap_vtk(ret)

    def create_default_lookup_table(self):
        """
        V.create_default_lookup_table()
        C++: void CreateDefaultLookupTable()
        Create default lookup table. Generally used to create one when
        none is available.
        """
        ret = self._vtk_obj.CreateDefaultLookupTable()
        return ret
        

    def fast_down_cast(self, *args):
        """
        V.fast_down_cast(AbstractArray) -> DataArray
        C++: static DataArray *FastDownCast(AbstractArray *source)
        Perform a fast, safe cast from a AbstractArray to a
        DataArray. This method checks if source->_get_array_type()
        returns data_array or a more derived type, and performs a
        static_cast to return source as a DataArray pointer.
        Otherwise, NULL is returned.
        """
        my_args = deref_array(args, [['vtkAbstractArray']])
        ret = self._wrap_call(self._vtk_obj.FastDownCast, *my_args)
        return wrap_vtk(ret)

    def fill_component(self, *args):
        """
        V.fill_component(int, float)
        C++: virtual void FillComponent(int compIdx, double value)
        Fill a component of a data array with a specified value. This
        method sets the specified component to specified value for all
        tuples in the data array.  This methods can be used to initialize
        or reinitialize a single component of a multi-component array.
        """
        ret = self._wrap_call(self._vtk_obj.FillComponent, *args)
        return ret

    def insert_component(self, *args):
        """
        V.insert_component(int, int, float)
        C++: virtual void InsertComponent(IdType tupleIdx, int compIdx,
             double value)
        Insert value at the location specified by tuple_idx and comp_idx.
        Note that memory allocation is performed as necessary to hold the
        data.
        """
        ret = self._wrap_call(self._vtk_obj.InsertComponent, *args)
        return ret

    def insert_next_tuple1(self, *args):
        """
        V.insert_next_tuple1(float)
        C++: void InsertNextTuple1(double value)
        These methods are included as convenience for the wrappers.
        insert_tuple() which takes arrays can not be used from wrapped
        languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextTuple1, *args)
        return ret

    def insert_next_tuple2(self, *args):
        """
        V.insert_next_tuple2(float, float)
        C++: void InsertNextTuple2(double val0, double val1)
        These methods are included as convenience for the wrappers.
        insert_tuple() which takes arrays can not be used from wrapped
        languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextTuple2, *args)
        return ret

    def insert_next_tuple3(self, *args):
        """
        V.insert_next_tuple3(float, float, float)
        C++: void InsertNextTuple3(double val0, double val1, double val2)
        These methods are included as convenience for the wrappers.
        insert_tuple() which takes arrays can not be used from wrapped
        languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextTuple3, *args)
        return ret

    def insert_next_tuple4(self, *args):
        """
        V.insert_next_tuple4(float, float, float, float)
        C++: void InsertNextTuple4(double val0, double val1, double val2,
            double val3)
        These methods are included as convenience for the wrappers.
        insert_tuple() which takes arrays can not be used from wrapped
        languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextTuple4, *args)
        return ret

    def insert_next_tuple6(self, *args):
        """
        V.insert_next_tuple6(float, float, float, float, float, float)
        C++: void InsertNextTuple6(double val0, double val1, double val2,
            double val3, double val4, double val5)
        These methods are included as convenience for the wrappers.
        insert_tuple() which takes arrays can not be used from wrapped
        languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextTuple6, *args)
        return ret

    def insert_next_tuple9(self, *args):
        """
        V.insert_next_tuple9(float, float, float, float, float, float,
            float, float, float)
        C++: void InsertNextTuple9(double val0, double val1, double val2,
            double val3, double val4, double val5, double val6,
            double val7, double val8)
        These methods are included as convenience for the wrappers.
        insert_tuple() which takes arrays can not be used from wrapped
        languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextTuple9, *args)
        return ret

    def insert_tuple1(self, *args):
        """
        V.insert_tuple1(int, float)
        C++: void InsertTuple1(IdType tupleIdx, double value)
        These methods are included as convenience for the wrappers.
        insert_tuple() which takes arrays can not be used from wrapped
        languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.InsertTuple1, *args)
        return ret

    def insert_tuple2(self, *args):
        """
        V.insert_tuple2(int, float, float)
        C++: void InsertTuple2(IdType tupleIdx, double val0,
            double val1)
        These methods are included as convenience for the wrappers.
        insert_tuple() which takes arrays can not be used from wrapped
        languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.InsertTuple2, *args)
        return ret

    def insert_tuple3(self, *args):
        """
        V.insert_tuple3(int, float, float, float)
        C++: void InsertTuple3(IdType tupleIdx, double val0,
            double val1, double val2)
        These methods are included as convenience for the wrappers.
        insert_tuple() which takes arrays can not be used from wrapped
        languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.InsertTuple3, *args)
        return ret

    def insert_tuple4(self, *args):
        """
        V.insert_tuple4(int, float, float, float, float)
        C++: void InsertTuple4(IdType tupleIdx, double val0,
            double val1, double val2, double val3)
        These methods are included as convenience for the wrappers.
        insert_tuple() which takes arrays can not be used from wrapped
        languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.InsertTuple4, *args)
        return ret

    def insert_tuple6(self, *args):
        """
        V.insert_tuple6(int, float, float, float, float, float, float)
        C++: void InsertTuple6(IdType tupleIdx, double val0,
            double val1, double val2, double val3, double val4,
            double val5)
        These methods are included as convenience for the wrappers.
        insert_tuple() which takes arrays can not be used from wrapped
        languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.InsertTuple6, *args)
        return ret

    def insert_tuple9(self, *args):
        """
        V.insert_tuple9(int, float, float, float, float, float, float,
            float, float, float)
        C++: void InsertTuple9(IdType tupleIdx, double val0,
            double val1, double val2, double val3, double val4,
            double val5, double val6, double val7, double val8)
        These methods are included as convenience for the wrappers.
        insert_tuple() which takes arrays can not be used from wrapped
        languages. These methods can be used instead.
        """
        ret = self._wrap_call(self._vtk_obj.InsertTuple9, *args)
        return ret

    def L2_NORM_RANGE(self):
        """
        V.l2__norm__range() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *L2_NORM_RANGE()
        This key is used to hold tight bounds on the $L_2$ norm of tuples
        in the array. Two values (a minimum and maximum) are stored for
        each component. When get_range() is called when no tuples are
        present in the array this value is set to { VTK_DOUBLE_MAX,
        VTK_DOUBLE_MIN }.
        """
        ret = wrap_vtk(self._vtk_obj.L2_NORM_RANGE())
        return ret
        

    def remove_first_tuple(self):
        """
        V.remove_first_tuple()
        C++: virtual void RemoveFirstTuple()
        These methods remove tuples from the data array. They shift data
        and resize array, so the data array is still valid after this
        operation. Note, this operation is fairly slow.
        """
        ret = self._vtk_obj.RemoveFirstTuple()
        return ret
        

    def remove_last_tuple(self):
        """
        V.remove_last_tuple()
        C++: virtual void RemoveLastTuple()
        These methods remove tuples from the data array. They shift data
        and resize array, so the data array is still valid after this
        operation. Note, this operation is fairly slow.
        """
        ret = self._vtk_obj.RemoveLastTuple()
        return ret
        

    def remove_tuple(self, *args):
        """
        V.remove_tuple(int)
        C++: virtual void RemoveTuple(IdType tupleIdx)
        These methods remove tuples from the data array. They shift data
        and resize array, so the data array is still valid after this
        operation. Note, this operation is fairly slow.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveTuple, *args)
        return ret

    def shallow_copy(self, *args):
        """
        V.shallow_copy(DataArray)
        C++: virtual void ShallowCopy(DataArray *other)
        Create a shallow copy of other into this, if possible. Shallow
        copies are only possible: (a) if both arrays are the same data
        type (b) if both arrays are the same array type (e.g. AOS vs.
        SOA) (c) if both arrays support shallow copies (e.g. BitArray
        currently does not.) If a shallow copy is not possible, a deep
        copy will be performed instead.
        """
        my_args = deref_array(args, [['vtkDataArray']])
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    def UNITS_LABEL(self):
        """
        V.units__label() -> InformationStringKey
        C++: static InformationStringKey *UNITS_LABEL()
        A human-readable string indicating the units for the array data.
        """
        ret = wrap_vtk(self._vtk_obj.UNITS_LABEL())
        return ret
        

    def write_void_pointer(self, *args):
        """
        V.write_void_pointer(int, int) -> void
        C++: virtual void *WriteVoidPointer(IdType valueIdx,
            IdType numValues)
        Get the address of a particular data index. Make sure data is
        allocated for the number of items requested. If needed, increase
        max_id to mark any new value ranges as in-use.
        """
        ret = self._wrap_call(self._vtk_obj.WriteVoidPointer, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('max_discrete_values',
    'GetMaxDiscreteValues'), ('name', 'GetName'), ('number_of_components',
    'GetNumberOfComponents'), ('number_of_tuples', 'GetNumberOfTuples'),
    ('number_of_values', 'GetNumberOfValues'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'max_discrete_values', 'name',
    'number_of_components', 'number_of_tuples', 'number_of_values'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DataArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['max_discrete_values', 'name', 'number_of_components',
            'number_of_tuples', 'number_of_values']),
            title='Edit DataArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
    def __len__(self):
        return self._vtk_obj.GetNumberOfTuples()
    
    def __iter__(self):
        obj = self._vtk_obj
        n = obj.GetNumberOfTuples()
        nc = obj.GetNumberOfComponents()
        if nc in [1,2,3,4,9]:
            meth = getattr(obj, 'GetTuple%d'%nc)
            for i in range(n):
                yield meth(i)
        else:
            for i in range(n):
                yield tuple([obj.GetComponent(i, x) for x in range(nc)])
    
    def _check_key(self, key, n):
        if type(key) not in [int, long]:
            raise TypeError("Only integers are valid keys.")
        if key < 0:
            key =  n + key
        if key < 0 or key >= n:
            raise IndexError("Index %s out of range."%key)
        return key
    
    def __getitem__(self, key):
        obj = self._vtk_obj
        n = obj.GetNumberOfTuples()
        key = self._check_key(key, n)
        nc = obj.GetNumberOfComponents()
        if nc in [1,2,3,4,9]:
            return getattr(obj, 'GetTuple%d'%nc)(key)
        else:
            return tuple([obj.GetComponent(key, x) for x in range(nc)])
    
    def __setitem__(self, key, val):
        obj = self._vtk_obj
        n = obj.GetNumberOfTuples()
        key = self._check_key(key, n)
        nc = obj.GetNumberOfComponents()
        if nc == 1:
            obj.SetValue(key, val)
        elif nc in [2,3,4,9]:
            getattr(obj, 'SetTuple%d'%nc)(key, *val)
        else:
            assert len(val) == nc,                        'length of %s != %s.'%(val, nc)
            for x in range(nc):
                obj.SetComponent(key, x, val[x])
    
    def __repr__(self):
        obj = self._vtk_obj
        n = obj.GetNumberOfTuples()
        if n <= 10:
            return repr([x for x in self])
        else:
            first, last = self[0], self[-1]
            return '[%s, ..., %s], length = %s'%(first, last, n)
    
    def append(self, val):
        obj = self._vtk_obj
        nc = obj.GetNumberOfComponents()
        if nc == 1:
            obj.InsertNextTuple1(val)
        elif nc in [2,3,4,9]:
            meth = getattr(obj, 'InsertNextTuple%d'%nc)
            meth(*val)
        else:
            n = obj.GetNumberOfTuples()
            for x in range(nc):
                obj.InsertComponent(n, x, val[x])
        self.update_traits()
    
    def extend(self, arr):
        obj = self._vtk_obj
        nc = obj.GetNumberOfComponents()
        if nc == 1:
            for i in arr:
                obj.InsertNextTuple1(i)
        elif nc in [2,3,4,9]:
            meth = getattr(obj, 'InsertNextTuple%d'%nc)
            for i in arr:
                meth(*i)
        else:
            n = obj.GetNumberOfTuples()
            for i in range(len(arr)):
                for x in range(nc):
                    obj.InsertComponent(n+i, x, arr[i][x])
        self.update_traits()
    
    def from_array(self, arr):
        '''Set the value of the data array using the passed
        Numeric array or Python list.  This is implemented
        efficiently.
        '''
        array_handler.array2vtk(arr, self._vtk_obj)
        self.update_traits()
    
    def to_array(self):
        '''Return the object as a Numeric array.'''
        return array_handler.vtk2array(self._vtk_obj)
    


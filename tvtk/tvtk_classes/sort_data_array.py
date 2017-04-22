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

from tvtk.tvtk_classes.object import Object


class SortDataArray(Object):
    """
    SortDataArray - provides several methods for sorting VTK arrays.
    
    Superclass: Object
    
    SortDataArray is used to sort data, based on its value, or with an
    associated key, into either ascending or descending order. This is
    useful for operations like selection, or analysis, when evaluating
    and processing data. A variety of sorting functions are provided,
    treating both arrays (i.e., AbstractArray) and id lists
    (vtk_id_list). Note that complex arrays like variants and string arrays
    are also handled.
    
    Additional functionality is provided to generate data ordering,
    without necessarily shuffling the data into a final, sorted position.
    Hence, the sorting process is organized into three steps because of
    the complexity of dealing with multiple types and multiple component
    data arrays. The first step involves creating and initializing a
    sorted index array, and then (second step) sorting this array to
    produce a map indicating the sorting order.  In other words, the
    sorting index array is a permutation which can be applied to other,
    associated data to shuffle it (third step) into an order consistent
    with the sorting operation. Note that the generation of the sorted
    index array is useful unto itself (even without the final shuffling
    of data) because it generates an ordered list (from the data values
    of any component in any array). So for example, it is possible to
    find the top N cells with the largest scalar value simply by
    generating the sorting index array from the call scalar values.
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly on
    multi-core machines.
    
    @warning
    The sort methods below are static, hence the sorting methods can be
    used without instantiating the class. All methods are thread safe.
    
    @sa
    SortFieldData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSortDataArray, obj, update, **traits)
    
    def generate_sort_indices(self, *args):
        """
        V.generate_sort_indices(int, void, int, int, int, [int, ...])
        C++: static void GenerateSortIndices(int dataType, void *dataIn,
            IdType numKeys, int numComp, int k, IdType *idx)
        The following are general functions which can be used to produce
        an ordering, and/or sort various types of VTK arrays. Don't use
        these methods unless you really know what you are doing. The
        basic idea is that an initial set of indices
        (_initialize_sort_indices() that refer to the data contained in a
        AbstractArray or IdList) are sorted (_generate_sort_indices()
        based on the data values in the array). The result of the sort is
        the creation of a permutation array (the sort array idx) that
        indicates where the data tuples originated (e.g., after the sort,
        idx[0] indicates where in the array the tuple was originally
        located prior to sorting.) This sorted index array can be used to
        shuffle various types of VTK arrays (the types supported
        correspond to the various arrays which are subclasses of
        DataArrayTemplate, use shuffle_array() or for IdList, use
        shuffle_id_list()). Also, the sort array, being an IdType*
        (i.e., id list), can also be used to identify points or cells in
        sorted order (based on the data in the originating data_in array).
        Note that sorting is always performed in ascending order, and the
        sorted index array reflects this; however the shuffling of data
        can be specified as either ascending (dir=0) or descending
        (dir=1) order. The user is responsible for taking ownership of
        the sort indices (i.e., free the idx array).
        """
        ret = self._wrap_call(self._vtk_obj.GenerateSortIndices, *args)
        return ret

    def initialize_sort_indices(self, *args):
        """
        V.initialize_sort_indices(int) -> (int, ...)
        C++: static IdType *InitializeSortIndices(IdType numKeys)
        The following are general functions which can be used to produce
        an ordering, and/or sort various types of VTK arrays. Don't use
        these methods unless you really know what you are doing. The
        basic idea is that an initial set of indices
        (_initialize_sort_indices() that refer to the data contained in a
        AbstractArray or IdList) are sorted (_generate_sort_indices()
        based on the data values in the array). The result of the sort is
        the creation of a permutation array (the sort array idx) that
        indicates where the data tuples originated (e.g., after the sort,
        idx[0] indicates where in the array the tuple was originally
        located prior to sorting.) This sorted index array can be used to
        shuffle various types of VTK arrays (the types supported
        correspond to the various arrays which are subclasses of
        DataArrayTemplate, use shuffle_array() or for IdList, use
        shuffle_id_list()). Also, the sort array, being an IdType*
        (i.e., id list), can also be used to identify points or cells in
        sorted order (based on the data in the originating data_in array).
        Note that sorting is always performed in ascending order, and the
        sorted index array reflects this; however the shuffling of data
        can be specified as either ascending (dir=0) or descending
        (dir=1) order. The user is responsible for taking ownership of
        the sort indices (i.e., free the idx array).
        """
        ret = self._wrap_call(self._vtk_obj.InitializeSortIndices, *args)
        return ret

    def shuffle_array(self, *args):
        """
        V.shuffle_array([int, ...], int, int, int, AbstractArray, void,
            int)
        C++: static void ShuffleArray(IdType *idx, int dataType,
            IdType numKeys, int numComp, AbstractArray *arr,
            void *dataIn, int dir)
        The following are general functions which can be used to produce
        an ordering, and/or sort various types of VTK arrays. Don't use
        these methods unless you really know what you are doing. The
        basic idea is that an initial set of indices
        (_initialize_sort_indices() that refer to the data contained in a
        AbstractArray or IdList) are sorted (_generate_sort_indices()
        based on the data values in the array). The result of the sort is
        the creation of a permutation array (the sort array idx) that
        indicates where the data tuples originated (e.g., after the sort,
        idx[0] indicates where in the array the tuple was originally
        located prior to sorting.) This sorted index array can be used to
        shuffle various types of VTK arrays (the types supported
        correspond to the various arrays which are subclasses of
        DataArrayTemplate, use shuffle_array() or for IdList, use
        shuffle_id_list()). Also, the sort array, being an IdType*
        (i.e., id list), can also be used to identify points or cells in
        sorted order (based on the data in the originating data_in array).
        Note that sorting is always performed in ascending order, and the
        sorted index array reflects this; however the shuffling of data
        can be specified as either ascending (dir=0) or descending
        (dir=1) order. The user is responsible for taking ownership of
        the sort indices (i.e., free the idx array).
        """
        my_args = deref_array(args, [(['int', Ellipsis], 'int', 'int', 'int', 'vtkAbstractArray', 'void', 'int')])
        ret = self._wrap_call(self._vtk_obj.ShuffleArray, *my_args)
        return ret

    def shuffle_id_list(self, *args):
        """
        V.shuffle_id_list([int, ...], int, IdList, [int, ...], int)
        C++: static void ShuffleIdList(IdType *idx, IdType sze,
            IdList *arrayIn, IdType *dataIn, int dir)
        The following are general functions which can be used to produce
        an ordering, and/or sort various types of VTK arrays. Don't use
        these methods unless you really know what you are doing. The
        basic idea is that an initial set of indices
        (_initialize_sort_indices() that refer to the data contained in a
        AbstractArray or IdList) are sorted (_generate_sort_indices()
        based on the data values in the array). The result of the sort is
        the creation of a permutation array (the sort array idx) that
        indicates where the data tuples originated (e.g., after the sort,
        idx[0] indicates where in the array the tuple was originally
        located prior to sorting.) This sorted index array can be used to
        shuffle various types of VTK arrays (the types supported
        correspond to the various arrays which are subclasses of
        DataArrayTemplate, use shuffle_array() or for IdList, use
        shuffle_id_list()). Also, the sort array, being an IdType*
        (i.e., id list), can also be used to identify points or cells in
        sorted order (based on the data in the originating data_in array).
        Note that sorting is always performed in ascending order, and the
        sorted index array reflects this; however the shuffling of data
        can be specified as either ascending (dir=0) or descending
        (dir=1) order. The user is responsible for taking ownership of
        the sort indices (i.e., free the idx array).
        """
        my_args = deref_array(args, [(['int', Ellipsis], 'int', 'vtkIdList', ['int', Ellipsis], 'int')])
        ret = self._wrap_call(self._vtk_obj.ShuffleIdList, *my_args)
        return ret

    def sort(self, *args):
        """
        V.sort(IdList)
        C++: static void Sort(IdList *keys)
        V.sort(AbstractArray)
        C++: static void Sort(AbstractArray *keys)
        V.sort(IdList, int)
        C++: static void Sort(IdList *keys, int dir)
        V.sort(AbstractArray, int)
        C++: static void Sort(AbstractArray *keys, int dir)
        V.sort(AbstractArray, AbstractArray)
        C++: static void Sort(AbstractArray *keys,
            AbstractArray *values)
        V.sort(AbstractArray, IdList)
        C++: static void Sort(AbstractArray *keys, IdList *values)
        V.sort(AbstractArray, AbstractArray, int)
        C++: static void Sort(AbstractArray *keys,
            AbstractArray *values, int dir)
        V.sort(AbstractArray, IdList, int)
        C++: static void Sort(AbstractArray *keys, IdList *values,
            int dir)
        Sorts the given array in ascending order. For this method, the
        keys must be single-component tuples.
        """
        my_args = deref_array(args, [['vtkIdList'], ['vtkAbstractArray'], ('vtkIdList', 'int'), ('vtkAbstractArray', 'int'), ('vtkAbstractArray', 'vtkAbstractArray'), ('vtkAbstractArray', 'vtkIdList'), ('vtkAbstractArray', 'vtkAbstractArray', 'int'), ('vtkAbstractArray', 'vtkIdList', 'int')])
        ret = self._wrap_call(self._vtk_obj.Sort, *my_args)
        return ret

    def sort_array_by_component(self, *args):
        """
        V.sort_array_by_component(AbstractArray, int)
        C++: static void SortArrayByComponent(AbstractArray *arr,
            int k)
        V.sort_array_by_component(AbstractArray, int, int)
        C++: static void SortArrayByComponent(AbstractArray *arr,
            int k, int dir)
        Sorts the given data array using the specified component as a
        key. Think of the array as a 2-D grid with each tuple
        representing a row. Tuples are swapped until the k-th column of
        the grid is monotonically increasing. Where two tuples have the
        same value for the k-th component, their order in the final
        result is unspecified.
        """
        my_args = deref_array(args, [('vtkAbstractArray', 'int'), ('vtkAbstractArray', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.SortArrayByComponent, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SortDataArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SortDataArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit SortDataArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SortDataArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.array_iterator import ArrayIterator


class BitArrayIterator(ArrayIterator):
    """
    BitArrayIterator - Iterator for BitArray.
    
    Superclass: ArrayIterator
    
    This iterator iterates over a BitArray. It uses the double
    interface to get/set bit values.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBitArrayIterator, obj, update, **traits)
    
    def get_value(self, *args):
        """
        V.get_value(int) -> int
        C++: int GetValue(IdType id)
        Must be called only after Initialize.
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, int)
        C++: void SetValue(IdType id, int value)
        Sets the value at the index. This does not verify if the index is
        valid. The caller must ensure that id is less than the maximum
        number of values.
        """
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

    def _get_array(self):
        return wrap_vtk(self._vtk_obj.GetArray())
    array = traits.Property(_get_array, help=\
        """
        Get the array.
        """
    )

    def _get_data_type_size(self):
        return self._vtk_obj.GetDataTypeSize()
    data_type_size = traits.Property(_get_data_type_size, help=\
        """
        Get the data type size from the underlying array.
        """
    )

    def _get_number_of_components(self):
        return self._vtk_obj.GetNumberOfComponents()
    number_of_components = traits.Property(_get_number_of_components, help=\
        """
        Must be called only after Initialize.
        """
    )

    def _get_number_of_tuples(self):
        return self._vtk_obj.GetNumberOfTuples()
    number_of_tuples = traits.Property(_get_number_of_tuples, help=\
        """
        Must be called only after Initialize.
        """
    )

    def _get_number_of_values(self):
        return self._vtk_obj.GetNumberOfValues()
    number_of_values = traits.Property(_get_number_of_values, help=\
        """
        Must be called only after Initialize.
        """
    )

    def get_tuple(self, *args):
        """
        V.get_tuple(int) -> (int, ...)
        C++: int *GetTuple(IdType id)
        Must be called only after Initialize.
        """
        ret = self._wrap_call(self._vtk_obj.GetTuple, *args)
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
            return super(BitArrayIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BitArrayIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit BitArrayIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BitArrayIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


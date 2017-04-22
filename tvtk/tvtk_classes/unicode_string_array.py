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


class UnicodeStringArray(AbstractArray):
    """
    UnicodeStringArray - Subclass of AbstractArray that holds
    UnicodeStrings
    
    Superclass: AbstractArray
    
    @par Thanks: Developed by Timothy M. Shead (tshead@sandia.gov) at
    Sandia National Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnicodeStringArray, obj, update, **traits)
    
    number_of_tuples = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _number_of_tuples_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTuples,
                        self.number_of_tuples)

    def get_utf8_value(self, *args):
        """
        V.get_utf8_value(int) -> string
        C++: const char *GetUTF8Value(IdType i)"""
        ret = self._wrap_call(self._vtk_obj.GetUTF8Value, *args)
        return ret

    def set_utf8_value(self, *args):
        """
        V.set_utf8_value(int, string)
        C++: void SetUTF8Value(IdType i, const char *)"""
        ret = self._wrap_call(self._vtk_obj.SetUTF8Value, *args)
        return ret

    def get_value(self, *args):
        """
        V.get_value(int) -> unicode
        C++: UnicodeString &GetValue(IdType i)"""
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, unicode)
        C++: void SetValue(IdType i, const UnicodeString &)"""
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

    def get_variant_value(self, *args):
        """
        V.get_variant_value(int) -> Variant
        """
        ret = self._wrap_call(self._vtk_obj.GetVariantValue, *args)
        return wrap_vtk(ret)

    def set_variant_value(self, *args):
        """
        V.set_variant_value(int, Variant)
        C++: void SetVariantValue(IdType idx, Variant value)
            override;"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetVariantValue, *my_args)
        return ret

    def insert_next_utf8_value(self, *args):
        """
        V.insert_next_utf8_value(string)
        C++: void InsertNextUTF8Value(const char *)"""
        ret = self._wrap_call(self._vtk_obj.InsertNextUTF8Value, *args)
        return ret

    def insert_next_value(self, *args):
        """
        V.insert_next_value(unicode) -> int
        C++: IdType InsertNextValue(const UnicodeString &)"""
        ret = self._wrap_call(self._vtk_obj.InsertNextValue, *args)
        return ret

    def insert_value(self, *args):
        """
        V.insert_value(int, unicode)
        C++: void InsertValue(IdType idx, const UnicodeString &)"""
        ret = self._wrap_call(self._vtk_obj.InsertValue, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_tuples', 'GetNumberOfTuples'),
    ('max_discrete_values', 'GetMaxDiscreteValues'), ('name', 'GetName'),
    ('number_of_components', 'GetNumberOfComponents'),
    ('number_of_values', 'GetNumberOfValues'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'max_discrete_values', 'name',
    'number_of_components', 'number_of_tuples', 'number_of_values'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UnicodeStringArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UnicodeStringArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['max_discrete_values', 'name', 'number_of_components',
            'number_of_tuples', 'number_of_values']),
            title='Edit UnicodeStringArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnicodeStringArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


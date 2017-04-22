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


class Information(Object):
    """
    Information - Store Algorithm input/output information.
    
    Superclass: Object
    
    Information represents information and/or data for one input or
    one output of a Algorithm.  It maps from keys to values of several
    data types.  Instances of this class are collected in
    InformationVector instances and passed to
    Algorithm::ProcessRequest calls.  The information and data
    referenced by the instance on a particular input or output define the
    request made to the Algorithm instance.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInformation, obj, update, **traits)
    
    def _get_request(self):
        return wrap_vtk(self._vtk_obj.GetRequest())
    def _set_request(self, arg):
        old_val = self._get_request()
        self._wrap_call(self._vtk_obj.SetRequest,
                        deref_vtk(arg))
        self.trait_property_changed('request', old_val, arg)
    request = traits.Property(_get_request, _set_request, help=\
        """
        Get/Set the Request ivar
        """
    )

    def get_key(self, *args):
        """
        V.get_key(InformationDataObjectKey) -> InformationKey
        C++: static InformationKey *GetKey(
            InformationDataObjectKey *key)
        V.get_key(InformationDoubleKey) -> InformationKey
        C++: static InformationKey *GetKey(
            InformationDoubleKey *key)
        V.get_key(InformationDoubleVectorKey) -> InformationKey
        C++: static InformationKey *GetKey(
            InformationDoubleVectorKey *key)
        V.get_key(InformationInformationKey) -> InformationKey
        C++: static InformationKey *GetKey(
            InformationInformationKey *key)
        V.get_key(InformationInformationVectorKey) -> InformationKey
        C++: static InformationKey *GetKey(
            InformationInformationVectorKey *key)
        V.get_key(InformationIntegerKey) -> InformationKey
        C++: static InformationKey *GetKey(
            InformationIntegerKey *key)
        V.get_key(InformationIntegerVectorKey) -> InformationKey
        C++: static InformationKey *GetKey(
            InformationIntegerVectorKey *key)
        V.get_key(InformationRequestKey) -> InformationKey
        C++: static InformationKey *GetKey(
            InformationRequestKey *key)
        V.get_key(InformationStringKey) -> InformationKey
        C++: static InformationKey *GetKey(
            InformationStringKey *key)
        V.get_key(InformationStringVectorKey) -> InformationKey
        C++: static InformationKey *GetKey(
            InformationStringVectorKey *key)
        V.get_key(InformationKey) -> InformationKey
        C++: static InformationKey *GetKey(InformationKey *key)
        V.get_key(InformationUnsignedLongKey) -> InformationKey
        C++: static InformationKey *GetKey(
            InformationUnsignedLongKey *key)
        V.get_key(InformationVariantKey) -> InformationKey
        C++: static InformationKey *GetKey(
            InformationVariantKey *key)
        V.get_key(InformationVariantVectorKey) -> InformationKey
        C++: static InformationKey *GetKey(
            InformationVariantVectorKey *key)
        Upcast the given key instance.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetKey, *my_args)
        return wrap_vtk(ret)

    def _get_number_of_keys(self):
        return self._vtk_obj.GetNumberOfKeys()
    number_of_keys = traits.Property(_get_number_of_keys, help=\
        """
        Return the number of keys in this information object (as would be
        returned by iterating over the keys).
        """
    )

    def append(self, *args):
        """
        V.append(Information, int)
        C++: void Append(Information *from, int deep=0)
        V.append(InformationIntegerVectorKey, int)
        C++: void Append(InformationIntegerVectorKey *key, int value)
        V.append(InformationStringVectorKey, string)
        C++: void Append(InformationStringVectorKey *key,
            const std::string &value)
        V.append(InformationDoubleVectorKey, float)
        C++: void Append(InformationDoubleVectorKey *key, double value)
        V.append(InformationVariantVectorKey, Variant)
        C++: void Append(InformationVariantVectorKey *key,
            const Variant &value)
        V.append(InformationKeyVectorKey, InformationKey)
        C++: void Append(InformationKeyVectorKey *key,
            InformationKey *value)
        V.append(InformationKeyVectorKey, InformationDataObjectKey)
        C++: void Append(InformationKeyVectorKey *key,
            InformationDataObjectKey *value)
        V.append(InformationKeyVectorKey, InformationDoubleKey)
        C++: void Append(InformationKeyVectorKey *key,
            InformationDoubleKey *value)
        V.append(InformationKeyVectorKey,
            InformationDoubleVectorKey)
        C++: void Append(InformationKeyVectorKey *key,
            InformationDoubleVectorKey *value)
        V.append(InformationKeyVectorKey, InformationInformationKey)
        C++: void Append(InformationKeyVectorKey *key,
            InformationInformationKey *value)
        V.append(InformationKeyVectorKey,
            InformationInformationVectorKey)
        C++: void Append(InformationKeyVectorKey *key,
            InformationInformationVectorKey *value)
        V.append(InformationKeyVectorKey, InformationIntegerKey)
        C++: void Append(InformationKeyVectorKey *key,
            InformationIntegerKey *value)
        V.append(InformationKeyVectorKey,
            InformationIntegerVectorKey)
        C++: void Append(InformationKeyVectorKey *key,
            InformationIntegerVectorKey *value)
        Append all information entries from the given Information
        instance. If deep==1, a deep copy of the information structure is
        performed (new instances of  ...
         [Truncated]
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Append, *my_args)
        return ret

    def append_unique(self, *args):
        """
        V.append_unique(InformationKeyVectorKey, InformationKey)
        C++: void AppendUnique(InformationKeyVectorKey *key,
            InformationKey *value)
        V.append_unique(InformationKeyVectorKey,
            InformationDataObjectKey)
        C++: void AppendUnique(InformationKeyVectorKey *key,
            InformationDataObjectKey *value)
        V.append_unique(InformationKeyVectorKey,
            InformationDoubleKey)
        C++: void AppendUnique(InformationKeyVectorKey *key,
            InformationDoubleKey *value)
        V.append_unique(InformationKeyVectorKey,
            InformationDoubleVectorKey)
        C++: void AppendUnique(InformationKeyVectorKey *key,
            InformationDoubleVectorKey *value)
        V.append_unique(InformationKeyVectorKey,
            InformationInformationKey)
        C++: void AppendUnique(InformationKeyVectorKey *key,
            InformationInformationKey *value)
        V.append_unique(InformationKeyVectorKey,
            InformationInformationVectorKey)
        C++: void AppendUnique(InformationKeyVectorKey *key,
            InformationInformationVectorKey *value)
        V.append_unique(InformationKeyVectorKey,
            InformationIntegerKey)
        C++: void AppendUnique(InformationKeyVectorKey *key,
            InformationIntegerKey *value)
        V.append_unique(InformationKeyVectorKey,
            InformationIntegerVectorKey)
        C++: void AppendUnique(InformationKeyVectorKey *key,
            InformationIntegerVectorKey *value)
        V.append_unique(InformationKeyVectorKey,
            InformationStringKey)
        C++: void AppendUnique(InformationKeyVectorKey *key,
            InformationStringKey *value)
        V.append_unique(InformationKeyVectorKey,
            InformationStringVectorKey)
        C++: void AppendUnique(InformationKeyVectorKey *key,
            InformationStringVectorKey *value)
        V.append_unique(InformationKeyVectorKey,
            InformationObjectBaseKey)
        C++: void AppendUnique(InformationKeyVectorKey *key,
            InformationObjectBaseKey *value)
        Get/Set an information_key-vector-valued entry.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AppendUnique, *my_args)
        return ret

    def clear(self):
        """
        V.clear()
        C++: void Clear()
        Clear all information entries.
        """
        ret = self._vtk_obj.Clear()
        return ret
        

    def copy(self, *args):
        """
        V.copy(Information, int)
        C++: void Copy(Information *from, int deep=0)
        Copy all information entries from the given Information
        instance.  Any previously existing entries are removed.  If
        deep==1, a deep copy of the information structure is performed
        (new instances of any contained Information and
        InformationVector objects are created).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Copy, *my_args)
        return ret

    def copy_entries(self, *args):
        """
        V.copy_entries(Information, InformationKeyVectorKey, int)
        C++: void CopyEntries(Information *from,
            InformationKeyVectorKey *key, int deep=0)
        Use the given key to lookup a list of other keys in the given
        information object.  The key/value pairs associated with these
        other keys will be copied.  If deep==1, a deep copy of the
        information structure is performed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyEntries, *my_args)
        return ret

    def copy_entry(self, *args):
        """
        V.copy_entry(Information, InformationKey, int)
        C++: void CopyEntry(Information *from, InformationKey *key,
            int deep=0)
        V.copy_entry(Information, InformationDataObjectKey, int)
        C++: void CopyEntry(Information *from,
            InformationDataObjectKey *key, int deep=0)
        V.copy_entry(Information, InformationDoubleVectorKey, int)
        C++: void CopyEntry(Information *from,
            InformationDoubleVectorKey *key, int deep=0)
        V.copy_entry(Information, InformationVariantKey, int)
        C++: void CopyEntry(Information *from,
            InformationVariantKey *key, int deep=0)
        V.copy_entry(Information, InformationVariantVectorKey, int)
        C++: void CopyEntry(Information *from,
            InformationVariantVectorKey *key, int deep=0)
        V.copy_entry(Information, InformationInformationKey, int)
        C++: void CopyEntry(Information *from,
            InformationInformationKey *key, int deep=0)
        V.copy_entry(Information, InformationInformationVectorKey,
            int)
        C++: void CopyEntry(Information *from,
            InformationInformationVectorKey *key, int deep=0)
        V.copy_entry(Information, InformationIntegerKey, int)
        C++: void CopyEntry(Information *from,
            InformationIntegerKey *key, int deep=0)
        V.copy_entry(Information, InformationIntegerVectorKey, int)
        C++: void CopyEntry(Information *from,
            InformationIntegerVectorKey *key, int deep=0)
        V.copy_entry(Information, InformationObjectBaseVectorKey,
            int)
        C++: void CopyEntry(Information *from,
            InformationObjectBaseVectorKey *key, int deep=0)
        V.copy_entry(Information, InformationRequestKey, int)
        C++: void CopyEntry(Information *from,
            InformationRequestKey *key, int deep=0)
        V.copy_entry(Information, InformationStringKey, int)
        C++: void CopyEntry(Information *from,
            InformationStringKey *key, int deep=0)
        Copy the key/value pair associated with the given key in the
        given information object.  If deep=1, a deep copy of the
        informati ...
         [Truncated]
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyEntry, *my_args)
        return ret

    def get(self, *args):
        """
        V.get(InformationIntegerKey) -> int
        C++: int Get(InformationIntegerKey *key)
        V.get(InformationIdTypeKey) -> int
        C++: IdType Get(InformationIdTypeKey *key)
        V.get(InformationDoubleKey) -> float
        C++: double Get(InformationDoubleKey *key)
        V.get(InformationVariantKey) -> Variant
        C++: const Variant &Get(InformationVariantKey *key)
        V.get(InformationIntegerVectorKey) -> (int, ...)
        C++: int *Get(InformationIntegerVectorKey *key)
        V.get(InformationIntegerVectorKey, int) -> int
        C++: int Get(InformationIntegerVectorKey *key, int idx)
        V.get(InformationIntegerVectorKey, [int, ...])
        C++: void Get(InformationIntegerVectorKey *key, int *value)
        V.get(InformationStringVectorKey, int) -> string
        C++: const char *Get(InformationStringVectorKey *key,
            int idx=0)
        V.get(InformationIntegerPointerKey) -> (int, ...)
        C++: int *Get(InformationIntegerPointerKey *key)
        V.get(InformationIntegerPointerKey, [int, ...])
        C++: void Get(InformationIntegerPointerKey *key, int *value)
        V.get(InformationUnsignedLongKey) -> int
        C++: unsigned long Get(InformationUnsignedLongKey *key)
        V.get(InformationDoubleVectorKey) -> (float, ...)
        C++: double *Get(InformationDoubleVectorKey *key)
        V.get(InformationDoubleVectorKey, int) -> float
        C++: double Get(InformationDoubleVectorKey *key, int idx)
        V.get(InformationDoubleVectorKey, [float, ...])
        C++: void Get(InformationDoubleVectorKey *key, double *value)
        V.get(InformationVariantVectorKey, int) -> Variant
        C++: const Variant &Get(InformationVariantVectorKey *key,
            int idx)
        V.get(InformationKeyVectorKey, int) -> InformationKey
        C++: InformationKey *Get(InformationKeyVectorKey *key,
            int idx)
        V.get(InformationStringKey) -> string
        C++: const char *Get(InformationStringKey *key)
        V.get(InformationInformationKey) -> Information
        C++: Information *Get(InformationInformationKey *key)
        Get/Set an integer-valued entry.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Get, *my_args)
        return wrap_vtk(ret)

    def has(self, *args):
        """
        V.has(InformationKey) -> int
        C++: int Has(InformationKey *key)
        V.has(InformationRequestKey) -> int
        C++: int Has(InformationRequestKey *key)
        V.has(InformationIntegerKey) -> int
        C++: int Has(InformationIntegerKey *key)
        V.has(InformationIdTypeKey) -> int
        C++: int Has(InformationIdTypeKey *key)
        V.has(InformationDoubleKey) -> int
        C++: int Has(InformationDoubleKey *key)
        V.has(InformationVariantKey) -> int
        C++: int Has(InformationVariantKey *key)
        V.has(InformationIntegerVectorKey) -> int
        C++: int Has(InformationIntegerVectorKey *key)
        V.has(InformationStringVectorKey) -> int
        C++: int Has(InformationStringVectorKey *key)
        V.has(InformationIntegerPointerKey) -> int
        C++: int Has(InformationIntegerPointerKey *key)
        V.has(InformationUnsignedLongKey) -> int
        C++: int Has(InformationUnsignedLongKey *key)
        V.has(InformationDoubleVectorKey) -> int
        C++: int Has(InformationDoubleVectorKey *key)
        V.has(InformationVariantVectorKey) -> int
        C++: int Has(InformationVariantVectorKey *key)
        V.has(InformationKeyVectorKey) -> int
        C++: int Has(InformationKeyVectorKey *key)
        V.has(InformationStringKey) -> int
        C++: int Has(InformationStringKey *key)
        V.has(InformationInformationKey) -> int
        C++: int Has(InformationInformationKey *key)
        V.has(InformationInformationVectorKey) -> int
        C++: int Has(InformationInformationVectorKey *key)
        V.has(InformationObjectBaseKey) -> int
        C++: int Has(InformationObjectBaseKey *key)
        V.has(InformationObjectBaseVectorKey) -> int
        C++: int Has(InformationObjectBaseVectorKey *key)
        V.has(InformationDataObjectKey) -> int
        C++: int Has(InformationDataObjectKey *key)
        Check whether the given key appears in this information object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Has, *my_args)
        return ret

    def length(self, *args):
        """
        V.length(InformationIntegerVectorKey) -> int
        C++: int Length(InformationIntegerVectorKey *key)
        V.length(InformationStringVectorKey) -> int
        C++: int Length(InformationStringVectorKey *key)
        V.length(InformationIntegerPointerKey) -> int
        C++: int Length(InformationIntegerPointerKey *key)
        V.length(InformationDoubleVectorKey) -> int
        C++: int Length(InformationDoubleVectorKey *key)
        V.length(InformationVariantVectorKey) -> int
        C++: int Length(InformationVariantVectorKey *key)
        V.length(InformationKeyVectorKey) -> int
        C++: int Length(InformationKeyVectorKey *key)
        V.length(InformationObjectBaseVectorKey) -> int
        C++: int Length(InformationObjectBaseVectorKey *key)
        Get/Set an integer-vector-valued entry.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Length, *my_args)
        return ret

    def remove(self, *args):
        """
        V.remove(InformationKey)
        C++: void Remove(InformationKey *key)
        V.remove(InformationRequestKey)
        C++: void Remove(InformationRequestKey *key)
        V.remove(InformationIntegerKey)
        C++: void Remove(InformationIntegerKey *key)
        V.remove(InformationIdTypeKey)
        C++: void Remove(InformationIdTypeKey *key)
        V.remove(InformationDoubleKey)
        C++: void Remove(InformationDoubleKey *key)
        V.remove(InformationVariantKey)
        C++: void Remove(InformationVariantKey *key)
        V.remove(InformationIntegerVectorKey)
        C++: void Remove(InformationIntegerVectorKey *key)
        V.remove(InformationStringVectorKey)
        C++: void Remove(InformationStringVectorKey *key)
        V.remove(InformationIntegerPointerKey)
        C++: void Remove(InformationIntegerPointerKey *key)
        V.remove(InformationUnsignedLongKey)
        C++: void Remove(InformationUnsignedLongKey *key)
        V.remove(InformationDoubleVectorKey)
        C++: void Remove(InformationDoubleVectorKey *key)
        V.remove(InformationVariantVectorKey)
        C++: void Remove(InformationVariantVectorKey *key)
        V.remove(InformationKeyVectorKey, InformationKey)
        C++: void Remove(InformationKeyVectorKey *key,
            InformationKey *value)
        V.remove(InformationKeyVectorKey)
        C++: void Remove(InformationKeyVectorKey *key)
        V.remove(InformationStringKey)
        C++: void Remove(InformationStringKey *key)
        V.remove(InformationInformationKey)
        C++: void Remove(InformationInformationKey *key)
        V.remove(InformationInformationVectorKey)
        C++: void Remove(InformationInformationVectorKey *key)
        V.remove(InformationObjectBaseKey)
        C++: void Remove(InformationObjectBaseKey *key)
        V.remove(InformationObjectBaseVectorKey)
        C++: void Remove(InformationObjectBaseVectorKey *key)
        V.remove(InformationObjectBaseVectorKey, ObjectBase)
        C++: void Remove(InformationObjectBaseVectorKey *key,
            ObjectBase *objectToRemove)
        Remove the given key and its data from this information object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Remove, *my_args)
        return ret

    def set(self, *args):
        """
        V.set(InformationRequestKey)
        C++: void Set(InformationRequestKey *key)
        V.set(InformationIntegerKey, int)
        C++: void Set(InformationIntegerKey *key, int value)
        V.set(InformationIdTypeKey, int)
        C++: void Set(InformationIdTypeKey *key, IdType value)
        V.set(InformationDoubleKey, float)
        C++: void Set(InformationDoubleKey *key, double value)
        V.set(InformationVariantKey, Variant)
        C++: void Set(InformationVariantKey *key,
            const Variant &value)
        V.set(InformationIntegerVectorKey, (int, ...), int)
        C++: void Set(InformationIntegerVectorKey *key,
            const int *value, int length)
        V.set(InformationIntegerVectorKey, int, int, int)
        C++: void Set(InformationIntegerVectorKey *key, int value1,
            int value2, int value3)
        V.set(InformationIntegerVectorKey, int, int, int, int, int,
            int)
        C++: void Set(InformationIntegerVectorKey *key, int value1,
            int value2, int value3, int value4, int value5, int value6)
        V.set(InformationStringVectorKey, string, int)
        C++: void Set(InformationStringVectorKey *key,
            const std::string &value, int idx=0)
        V.set(InformationIntegerPointerKey, [int, ...], int)
        C++: void Set(InformationIntegerPointerKey *key, int *value,
            int length)
        V.set(InformationUnsignedLongKey, int)
        C++: void Set(InformationUnsignedLongKey *key,
            unsigned long value)
        V.set(InformationDoubleVectorKey, (float, ...), int)
        C++: void Set(InformationDoubleVectorKey *key,
            const double *value, int length)
        V.set(InformationDoubleVectorKey, float, float, float)
        C++: void Set(InformationDoubleVectorKey *key, double value1,
            double value2, double value3)
        V.set(InformationDoubleVectorKey, float, float, float, float,
            float, float)
        C++: void Set(InformationDoubleVectorKey *key, double value1,
            double value2, double value3, double value4, double value5,
            double value6)
        Get/Set a request-valued entry.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Set, *my_args)
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
            return super(Information, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Information properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit Information properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Information properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.object_base import ObjectBase


class InformationKey(ObjectBase):
    """
    InformationKey - Superclass for Information keys.
    
    Superclass: ObjectBase
    
    InformationKey is the superclass for all keys used to access the
    map represented by Information.  The Information::Set and
    Information::Get methods of Information are accessed by
    information keys.  A key is a pointer to an instance of a subclass of
    InformationKey.  The type of the subclass determines the overload
    of Set/Get that is selected.  This ensures that the type of value
    stored in a Information instance corresponding to a given key
    matches the type expected for that key.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInformationKey, obj, update, **traits)
    
    def _get_location(self):
        return self._vtk_obj.GetLocation()
    location = traits.Property(_get_location, help=\
        """
        Get the location of the key.  This is the name of the class in
        which the key is defined.
        """
    )

    def _get_name(self):
        return self._vtk_obj.GetName()
    name = traits.Property(_get_name, help=\
        """
        Get the name of the key.  This is not the type of the key, but
        the name of the key instance.
        """
    )

    def copy_default_information(self, *args):
        """
        V.copy_default_information(Information, Information,
            Information)
        C++: virtual void CopyDefaultInformation(Information *request,
            Information *fromInfo, Information *toInfo)
        This function is only relevant when the pertaining key is used in
        a VTK pipeline. By overwriting this method, a key can decide
        if/how to copy itself downstream or upstream during a particular
        pipeline pass. For example, meta-data keys can copy themselves
        during REQUEST_INFORMATION whereas request keys can copy
        themselves during REQUEST_UPDATE_EXTENT.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyDefaultInformation, *my_args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(Information, Information)
        C++: virtual void DeepCopy(Information *from,
            Information *to)
        Duplicate (new instance created) the entry associated with this
        key from one information object to another (new instances of any
        contained Information and InformationVector objects are
        created). Default implementation simply calls shallow_copy().
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def has(self, *args):
        """
        V.has(Information) -> int
        C++: virtual int Has(Information *info)
        Check whether this key appears in the given information object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Has, *my_args)
        return ret

    def need_to_execute(self, *args):
        """
        V.need_to_execute(Information, Information) -> bool
        C++: virtual bool NeedToExecute(Information *pipelineInfo,
            Information *dobjInfo)
        This function is only relevant when the pertaining key is used in
        a VTK pipeline. Specific keys that handle pipeline data requests
        (for example, UPDATE_PIECE_NUMBER) can overwrite this method to
        notify the pipeline that a a filter should be (re-)executed
        because what is in the current output is different that what is
        being requested by the key. For example, DATA_PIECE_NUMBER !=
        UPDATE_PIECE_NUMBER.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.NeedToExecute, *my_args)
        return ret

    def new_instance(self):
        """
        V.new_instance() -> InformationKey
        C++: InformationKey *NewInstance()"""
        ret = wrap_vtk(self._vtk_obj.NewInstance())
        return ret
        

    def print(self, *args):
        """
        V.print(Information)
        C++: void Print(Information *info)
        Print the key's value in an information object to a stream.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Print, *my_args)
        return ret

    def remove(self, *args):
        """
        V.remove(Information)
        C++: virtual void Remove(Information *info)
        Remove this key from the given information object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Remove, *my_args)
        return ret

    def report(self, *args):
        """
        V.report(Information, GarbageCollector)
        C++: virtual void Report(Information *info,
            GarbageCollector *collector)
        Report a reference this key has in the given information object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Report, *my_args)
        return ret

    def safe_down_cast(self, *args):
        """
        V.safe_down_cast(ObjectBase) -> InformationKey
        C++: static InformationKey *SafeDownCast(ObjectBase *o)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SafeDownCast, *my_args)
        return wrap_vtk(ret)

    def shallow_copy(self, *args):
        """
        V.shallow_copy(Information, Information)
        C++: virtual void ShallowCopy(Information *from,
            Information *to)
        Copy the entry associated with this key from one information
        object to another.  If there is no entry in the first information
        object for this key, the value is removed from the second.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    def store_meta_data(self, *args):
        """
        V.store_meta_data(Information, Information, Information)
        C++: virtual void StoreMetaData(Information *request,
            Information *pipelineInfo, Information *dobjInfo)
        This function is only relevant when the pertaining key is used in
        a VTK pipeline. Specific keys that handle pipeline data requests
        (for example, UPDATE_PIECE_NUMBER) can overwrite this method to
        store in the data information meta-data about the request that
        led to the current filter execution. This meta-data can later be
        used to compare what is being requested to decide whether the
        filter needs to re-execute. For example, a filter may store the
        current UPDATE_PIECE_NUMBER in the data object's information as
        the DATA_PIECE_NUMBER. DATA_PIECE_NUMBER can later be compared to
        a new UPDATA_PIECE_NUMBER to decide whether a filter should
        re-execute.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.StoreMetaData, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'),)
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    ([])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InformationKey, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InformationKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit InformationKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InformationKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


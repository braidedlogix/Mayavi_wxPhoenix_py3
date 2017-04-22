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

from tvtk.tvtk_classes.information_key import InformationKey


class InformationStringVectorKey(InformationKey):
    """
    InformationStringVectorKey - Key for String vector values.
    
    Superclass: InformationKey
    
    InformationStringVectorKey is used to represent keys for String
    vector values in Information.h
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInformationStringVectorKey, obj, update, **traits)
    
    def append(self, *args):
        """
        V.append(Information, string)
        C++: void Append(Information *info, const std::string &value)
        Get/Set the value associated with this key in the given
        information object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Append, *my_args)
        return ret

    def get(self, *args):
        """
        V.get(Information, int) -> string
        C++: const char *Get(Information *info, int idx=0)
        Get/Set the value associated with this key in the given
        information object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Get, *my_args)
        return ret

    def length(self, *args):
        """
        V.length(Information) -> int
        C++: int Length(Information *info)
        Get/Set the value associated with this key in the given
        information object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Length, *my_args)
        return ret

    def make_key(self, *args):
        """
        V.make_key(string, string, int) -> InformationStringVectorKey
        C++: static InformationStringVectorKey *MakeKey(
            const char *name, const char *location, int length=-1)
        This method simply returns a new InformationStringVectorKey,
        given a name, a location and a required length. This method is
        provided for wrappers. Use the constructor directly from C++
        instead.
        """
        ret = self._wrap_call(self._vtk_obj.MakeKey, *args)
        return wrap_vtk(ret)

    def set(self, *args):
        """
        V.set(Information, string, int)
        C++: void Set(Information *info, const std::string &value,
            int idx=0)
        Get/Set the value associated with this key in the given
        information object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Set, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'),)
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    ([])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InformationStringVectorKey, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InformationStringVectorKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit InformationStringVectorKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InformationStringVectorKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


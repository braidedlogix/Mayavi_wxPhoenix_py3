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


class InformationObjectBaseVectorKey(InformationKey):
    """
    InformationObjectBaseVectorKey - Key for ObjectBase vector
    values.
    
    Superclass: InformationKey
    
    InformationObjectBaseVectorKey is used to represent keys for
    double vector values in Information.h. NOTE the interface in this
    key differs from that in other similar keys because of our internal
    use of smart pointers.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInformationObjectBaseVectorKey, obj, update, **traits)
    
    def append(self, *args):
        """
        V.append(Information, ObjectBase)
        C++: void Append(Information *info, ObjectBase *value)
        Put the value on the back of the vector, with ref counting.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Append, *my_args)
        return ret

    def clear(self, *args):
        """
        V.clear(Information)
        C++: void Clear(Information *info)
        Clear the vector.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Clear, *my_args)
        return ret

    def get(self, *args):
        """
        V.get(Information, int) -> ObjectBase
        C++: ObjectBase *Get(Information *info, int idx)
        Get the ObjectBase at a specific location in the vector.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Get, *my_args)
        return wrap_vtk(ret)

    def length(self, *args):
        """
        V.length(Information) -> int
        C++: int Length(Information *info)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Length, *my_args)
        return ret

    def make_key(self, *args):
        """
        V.make_key(string, string, string)
            -> InformationObjectBaseVectorKey
        C++: static InformationObjectBaseVectorKey *MakeKey(
            const char *name, const char *location,
            const char *requiredClass=0)
        This method simply returns a new
        InformationObjectBaseVectorKey, given a name, location and
        optionally a required class (a classname to restrict which class
        types can be set with this key). This method is provided for
        wrappers. Use the constructor directly from C++ instead.
        """
        ret = self._wrap_call(self._vtk_obj.MakeKey, *args)
        return wrap_vtk(ret)

    def resize(self, *args):
        """
        V.resize(Information, int)
        C++: void Resize(Information *info, int n)
        Resize (extend) the vector to hold n objects. Any new elements
        created will be null initialized.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Resize, *my_args)
        return ret

    def set(self, *args):
        """
        V.set(Information, ObjectBase, int)
        C++: void Set(Information *info, ObjectBase *value, int i)
        Set element i of the vector to value. Resizes the vector if
        needed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Set, *my_args)
        return ret

    def size(self, *args):
        """
        V.size(Information) -> int
        C++: int Size(Information *info)
        Get the vector's length.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Size, *my_args)
        return ret

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'),)
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    ([])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InformationObjectBaseVectorKey, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InformationObjectBaseVectorKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit InformationObjectBaseVectorKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InformationObjectBaseVectorKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class InformationInformationKey(InformationKey):
    """
    InformationInformationKey - Key for Information values.
    
    Superclass: InformationKey
    
    InformationInformationKey is used to represent keys in
    Information for other information objects.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInformationInformationKey, obj, update, **traits)
    
    def get(self, *args):
        """
        V.get(Information) -> Information
        C++: Information *Get(Information *info)
        Get/Set the value associated with this key in the given
        information object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Get, *my_args)
        return wrap_vtk(ret)

    def make_key(self, *args):
        """
        V.make_key(string, string) -> InformationInformationKey
        C++: static InformationInformationKey *MakeKey(
            const char *name, const char *location)
        This method simply returns a new InformationInformationKey,
        given a name and a location. This method is provided for
        wrappers. Use the constructor directly from C++ instead.
        """
        ret = self._wrap_call(self._vtk_obj.MakeKey, *args)
        return wrap_vtk(ret)

    def set(self, *args):
        """
        V.set(Information, Information)
        C++: void Set(Information *info, Information *)
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
            return super(InformationInformationKey, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InformationInformationKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit InformationInformationKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InformationInformationKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


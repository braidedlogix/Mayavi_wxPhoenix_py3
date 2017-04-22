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


class CollectionIterator(Object):
    """
    CollectionIterator - iterator through a Collection.
    
    Superclass: Object
    
    CollectionIterator provides an alternative way to traverse through
    the objects in a Collection.  Unlike the collection's built in
    interface, this allows multiple iterators to simultaneously traverse
    the collection.  If items are removed from the collection, only the
    iterators currently pointing to those items are invalidated.  Other
    iterators will still continue to function normally.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCollectionIterator, obj, update, **traits)
    
    def _get_collection(self):
        return wrap_vtk(self._vtk_obj.GetCollection())
    def _set_collection(self, arg):
        old_val = self._get_collection()
        self._wrap_call(self._vtk_obj.SetCollection,
                        deref_vtk(arg))
        self.trait_property_changed('collection', old_val, arg)
    collection = traits.Property(_get_collection, _set_collection, help=\
        """
        Set/Get the collection over which to iterate.
        """
    )

    def _get_current_object(self):
        return wrap_vtk(self._vtk_obj.GetCurrentObject())
    current_object = traits.Property(_get_current_object, help=\
        """
        Get the item at the current iterator position.  Valid only when
        is_done_with_traversal() returns 1.
        """
    )

    def go_to_first_item(self):
        """
        V.go_to_first_item()
        C++: void GoToFirstItem()
        Position the iterator at the first item in the collection.
        """
        ret = self._vtk_obj.GoToFirstItem()
        return ret
        

    def go_to_next_item(self):
        """
        V.go_to_next_item()
        C++: void GoToNextItem()
        Move the iterator to the next item in the collection.
        """
        ret = self._vtk_obj.GoToNextItem()
        return ret
        

    def init_traversal(self):
        """
        V.init_traversal()
        C++: void InitTraversal()
        Position the iterator at the first item in the collection.
        """
        ret = self._vtk_obj.InitTraversal()
        return ret
        

    def is_done_with_traversal(self):
        """
        V.is_done_with_traversal() -> int
        C++: int IsDoneWithTraversal()
        Test whether the iterator is currently positioned at a valid
        item. Returns 1 for yes, 0 for no.
        """
        ret = self._vtk_obj.IsDoneWithTraversal()
        return ret
        

    def _iter__(self, *args):
        """
        Implement iter(self)
        mplement iter(self)."""
        ret = self._wrap_call(self._vtk_obj.__iter__, *args)
        return ret

    def _next__(self, *args):
        """
        Implement next(self)
        mplement next(self)."""
        ret = self._wrap_call(self._vtk_obj.__next__, *args)
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
            return super(CollectionIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CollectionIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit CollectionIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CollectionIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


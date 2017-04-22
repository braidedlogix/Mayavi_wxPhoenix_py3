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

from tvtk.tvtk_classes.collection_iterator import CollectionIterator


class DataArrayCollectionIterator(CollectionIterator):
    """
    DataArrayCollectionIterator - iterator through a
    DataArrayCollection.
    
    Superclass: CollectionIterator
    
    DataArrayCollectionIterator provides an implementation of
    CollectionIterator which allows the items to be retrieved with the
    proper subclass pointer type for DataArrayCollection.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataArrayCollectionIterator, obj, update, **traits)
    
    def _get_collection(self):
        return wrap_vtk(self._vtk_obj.GetCollection())
    def _set_collection(self, arg):
        old_val = self._get_collection()
        my_arg = deref_array([arg], [['vtkCollection'], ['vtkDataArrayCollection']])
        self._wrap_call(self._vtk_obj.SetCollection,
                        my_arg[0])
        self.trait_property_changed('collection', old_val, arg)
    collection = traits.Property(_get_collection, _set_collection, help=\
        """
        Set/Get the collection over which to iterate.
        """
    )

    def _get_data_array(self):
        return wrap_vtk(self._vtk_obj.GetDataArray())
    data_array = traits.Property(_get_data_array, help=\
        """
        Get the item at the current iterator position.  Valid only when
        is_done_with_traversal() returns 1.
        """
    )

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataArrayCollectionIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DataArrayCollectionIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit DataArrayCollectionIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataArrayCollectionIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


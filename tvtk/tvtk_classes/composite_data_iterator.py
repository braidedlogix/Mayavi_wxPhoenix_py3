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


class CompositeDataIterator(Object):
    """
    CompositeDataIterator - superclass for composite data iterators
    
    Superclass: Object
    
    CompositeDataIterator provides an interface for accessing datasets
    in a collection (vtk_composite_data_iterator).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCompositeDataIterator, obj, update, **traits)
    
    skip_empty_nodes = tvtk_base.true_bool_trait(help=\
        """
        If skip_empty_nodes is true, then NULL datasets will be skipped.
        Default is true.
        """
    )

    def _skip_empty_nodes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSkipEmptyNodes,
                        self.skip_empty_nodes_)

    def _get_data_set(self):
        return wrap_vtk(self._vtk_obj.GetDataSet())
    def _set_data_set(self, arg):
        old_val = self._get_data_set()
        self._wrap_call(self._vtk_obj.SetDataSet,
                        deref_vtk(arg))
        self.trait_property_changed('data_set', old_val, arg)
    data_set = traits.Property(_get_data_set, _set_data_set, help=\
        """
        Set the composite dataset this iterator is iterating over. Must
        be set before traversal begins.
        """
    )

    def _get_current_data_object(self):
        return wrap_vtk(self._vtk_obj.GetCurrentDataObject())
    current_data_object = traits.Property(_get_current_data_object, help=\
        """
        Returns the current item. Valid only when is_done_with_traversal()
        returns 0.
        """
    )

    def _get_current_flat_index(self):
        return self._vtk_obj.GetCurrentFlatIndex()
    current_flat_index = traits.Property(_get_current_flat_index, help=\
        """
        Flat index is an index to identify the data in a composite data
        structure
        """
    )

    def _get_current_meta_data(self):
        return wrap_vtk(self._vtk_obj.GetCurrentMetaData())
    current_meta_data = traits.Property(_get_current_meta_data, help=\
        """
        Returns the meta-data associated with the current item. This will
        allocate a new Information object is none is already present.
        Use has_current_meta_data to avoid unnecessary creation of
        Information objects.
        """
    )

    def _get_reverse(self):
        return self._vtk_obj.GetReverse()
    reverse = traits.Property(_get_reverse, help=\
        """
        Returns if the iteration is in reverse order.
        """
    )

    def go_to_first_item(self):
        """
        V.go_to_first_item()
        C++: virtual void GoToFirstItem()
        Move the iterator to the beginning of the collection.
        """
        ret = self._vtk_obj.GoToFirstItem()
        return ret
        

    def go_to_next_item(self):
        """
        V.go_to_next_item()
        C++: virtual void GoToNextItem()
        Move the iterator to the next item in the collection.
        """
        ret = self._vtk_obj.GoToNextItem()
        return ret
        

    def has_current_meta_data(self):
        """
        V.has_current_meta_data() -> int
        C++: virtual int HasCurrentMetaData()
        Returns if the a meta-data information object is present for the
        current item. Return 1 on success, 0 otherwise.
        """
        ret = self._vtk_obj.HasCurrentMetaData()
        return ret
        

    def init_reverse_traversal(self):
        """
        V.init_reverse_traversal()
        C++: virtual void InitReverseTraversal()
        Begin iterating over the composite dataset structure in reverse
        order.
        """
        ret = self._vtk_obj.InitReverseTraversal()
        return ret
        

    def init_traversal(self):
        """
        V.init_traversal()
        C++: virtual void InitTraversal()
        Begin iterating over the composite dataset structure.
        """
        ret = self._vtk_obj.InitTraversal()
        return ret
        

    def is_done_with_traversal(self):
        """
        V.is_done_with_traversal() -> int
        C++: virtual int IsDoneWithTraversal()
        Test whether the iterator is finished with the traversal. Returns
        1 for yes, and 0 for no. It is safe to call any of the
        get_current...() methods only when is_done_with_traversal() returns
        0.
        """
        ret = self._vtk_obj.IsDoneWithTraversal()
        return ret
        

    _updateable_traits_ = \
    (('skip_empty_nodes', 'GetSkipEmptyNodes'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'skip_empty_nodes'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CompositeDataIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CompositeDataIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['skip_empty_nodes'], [], []),
            title='Edit CompositeDataIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CompositeDataIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


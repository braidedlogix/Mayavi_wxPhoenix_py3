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

from tvtk.tvtk_classes.composite_data_set import CompositeDataSet


class DataObjectTree(CompositeDataSet):
    """
    DataObjectTree - provides implementation for most abstract methods
    in the superclass CompositeDataSet
    
    Superclass: CompositeDataSet
    
    DataObjectTree is represents a collection of datasets (including
    other composite datasets). It provides an interface to access the
    datasets through iterators. DataObjectTree provides methods that
    are used by subclasses to store the datasets. DataObjectTree
    provides the datastructure for a full tree representation. Subclasses
    provide the semantics for it and control how this tree is built.
    
    @sa
    DataObjectTreeIterator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataObjectTree, obj, update, **traits)
    
    def get_data_set(self, *args):
        """
        V.get_data_set(CompositeDataIterator) -> DataObject
        C++: DataObject *GetDataSet(CompositeDataIterator *iter)
            override;
        Returns the dataset located at the positiong pointed by the
        iterator. The iterator does not need to be iterating over this
        dataset itself. It can be an iterator for composite dataset with
        similar structure (achieved by using copy_structure).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetDataSet, *my_args)
        return wrap_vtk(ret)

    def set_data_set(self, *args):
        """
        V.set_data_set(CompositeDataIterator, DataObject)
        C++: void SetDataSet(CompositeDataIterator *iter,
            DataObject *dataObj) override;
        Sets the data set at the location pointed by the iterator. The
        iterator does not need to be iterating over this dataset itself.
        It can be any composite datasite with similar structure (achieved
        by using copy_structure).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDataSet, *my_args)
        return ret

    def get_meta_data(self, *args):
        """
        V.get_meta_data(CompositeDataIterator) -> Information
        C++: virtual Information *GetMetaData(
            CompositeDataIterator *iter)
        Returns the meta-data associated with the position pointed by the
        iterator. This will create a new Information object if none
        already exists. Use has_meta_data to avoid creating the
        Information object unnecessarily. The iterator does not need
        to be iterating over this dataset itself. It can be an iterator
        for composite dataset with similar structure (achieved by using
        copy_structure).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetMetaData, *my_args)
        return wrap_vtk(ret)

    def has_meta_data(self, *args):
        """
        V.has_meta_data(CompositeDataIterator) -> int
        C++: virtual int HasMetaData(CompositeDataIterator *iter)
        Returns if any meta-data associated with the position pointed by
        the iterator. The iterator does not need to be iterating over
        this dataset itself. It can be an iterator for composite dataset
        with similar structure (achieved by using copy_structure).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HasMetaData, *my_args)
        return ret

    def new_tree_iterator(self):
        """
        V.new_tree_iterator() -> DataObjectTreeIterator
        C++: virtual DataObjectTreeIterator *NewTreeIterator()
        Return a new iterator (the iterator has to be deleted by user).
        """
        ret = wrap_vtk(self._vtk_obj.NewTreeIterator())
        return ret
        

    def set_data_set_from(self, *args):
        """
        V.set_data_set_from(DataObjectTreeIterator, DataObject)
        C++: void SetDataSetFrom(DataObjectTreeIterator *iter,
            DataObject *dataObj)
        Sets the data at the location provided by a
        DataObjectTreeIterator
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDataSetFrom, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataObjectTree, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DataObjectTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit DataObjectTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataObjectTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.data_object import DataObject


class CompositeDataSet(DataObject):
    """
    CompositeDataSet - abstract superclass for composite (multi-block
    or AMR) datasets
    
    Superclass: DataObject
    
    CompositeDataSet is an abstract class that represents a collection
    of datasets (including other composite datasets). It provides an
    interface to access the datasets through iterators.
    CompositeDataSet provides methods that are used by subclasses to
    store the datasets. CompositeDataSet provides the datastructure
    for a full tree representation. Subclasses provide the semantics for
    it and control how this tree is built.
    
    @sa
    CompositeDataIterator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCompositeDataSet, obj, update, **traits)
    
    def get_data_set(self, *args):
        """
        V.get_data_set(CompositeDataIterator) -> DataObject
        C++: virtual DataObject *GetDataSet(
            CompositeDataIterator *iter)
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
        C++: virtual void SetDataSet(CompositeDataIterator *iter,
            DataObject *dataObj)
        Sets the data set at the location pointed by the iterator. The
        iterator does not need to be iterating over this dataset itself.
        It can be any composite datasite with similar structure (achieved
        by using copy_structure).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDataSet, *my_args)
        return ret

    def _get_number_of_points(self):
        return self._vtk_obj.GetNumberOfPoints()
    number_of_points = traits.Property(_get_number_of_points, help=\
        """
        Returns the total number of points of all blocks. This will
        iterate over all blocks and call get_number_of_points() so it might
        be expansive.
        """
    )

    def CURRENT_PROCESS_CAN_LOAD_BLOCK(self):
        """
        V.current__process__can__load__block() -> InformationIntegerKey
        C++: static InformationIntegerKey *CURRENT_PROCESS_CAN_LOAD_BLOCK(
            )
        Key used to indicate that the current process can load the data
        in the node.  Used for parallel readers where the nodes are
        assigned to the processes by the reader to indicate further down
        the pipeline which nodes will be on which processes.
        ***THIS IS AN EXPERIMENTAL KEY SUBJECT TO CHANGE WITHOUT
            NOTICE***
        """
        ret = wrap_vtk(self._vtk_obj.CURRENT_PROCESS_CAN_LOAD_BLOCK())
        return ret
        

    def copy_structure(self, *args):
        """
        V.copy_structure(CompositeDataSet)
        C++: virtual void CopyStructure(CompositeDataSet *input)
        Copies the tree structure from the input. All pointers to
        non-composite data objects are intialized to NULL. This also
        shallow copies the meta data associated with all the nodes.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyStructure, *my_args)
        return ret

    def NAME(self):
        """
        V.name() -> InformationStringKey
        C++: static InformationStringKey *NAME()
        Key used to put node name in the meta-data associated with a
        node.
        """
        ret = wrap_vtk(self._vtk_obj.NAME())
        return ret
        

    def new_iterator(self):
        """
        V.new_iterator() -> CompositeDataIterator
        C++: virtual CompositeDataIterator *NewIterator()
        Return a new iterator (the iterator has to be deleted by user).
        """
        ret = wrap_vtk(self._vtk_obj.NewIterator())
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
            return super(CompositeDataSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CompositeDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit CompositeDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CompositeDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


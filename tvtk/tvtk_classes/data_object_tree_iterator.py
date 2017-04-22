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

from tvtk.tvtk_classes.composite_data_iterator import CompositeDataIterator


class DataObjectTreeIterator(CompositeDataIterator):
    """
    DataObjectTreeIterator - superclass for composite data iterators
    
    Superclass: CompositeDataIterator
    
    DataObjectTreeIterator provides an interface for accessing
    datasets in a collection (vtk_data_object_tree_iterator).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataObjectTreeIterator, obj, update, **traits)
    
    traverse_sub_tree = tvtk_base.true_bool_trait(help=\
        """
        If traverse_sub_tree is set to true, the iterator will visit the
        entire tree structure, otherwise it only visits the first level
        children. Set to 1 by default.
        """
    )

    def _traverse_sub_tree_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTraverseSubTree,
                        self.traverse_sub_tree_)

    visit_only_leaves = tvtk_base.true_bool_trait(help=\
        """
        If visit_only_leaves is true, the iterator will only visit nodes
        (sub-datasets) that are not composite. If it encounters a
        composite data set, it will automatically traverse that composite
        dataset until it finds non-composite datasets. With this options,
        it is possible to visit all non-composite datasets in tree of
        composite datasets (composite of composite of composite for
        example :-) ) If visit_only_leaves is false, get_current_data_object()
        may return CompositeDataSet. By default, visit_only_leaves is 1.
        """
    )

    def _visit_only_leaves_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVisitOnlyLeaves,
                        self.visit_only_leaves_)

    _updateable_traits_ = \
    (('traverse_sub_tree', 'GetTraverseSubTree'), ('visit_only_leaves',
    'GetVisitOnlyLeaves'), ('skip_empty_nodes', 'GetSkipEmptyNodes'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'skip_empty_nodes',
    'traverse_sub_tree', 'visit_only_leaves'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataObjectTreeIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DataObjectTreeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['skip_empty_nodes', 'traverse_sub_tree', 'visit_only_leaves'],
            [], []),
            title='Edit DataObjectTreeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataObjectTreeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


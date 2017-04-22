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


class Selection(DataObject):
    """
    Selection - A node in a selection tree.
    
    Superclass: DataObject
    
    Used to store selection results.
    
    Selection is a collection of SelectionNode objects, each of
    which contains information about a piece of the whole selection. Each
    selection node may contain different types of selections.
    
    @sa
    SelectionNode
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSelection, obj, update, **traits)
    
    def get_node(self, *args):
        """
        V.get_node(int) -> SelectionNode
        C++: virtual SelectionNode *GetNode(unsigned int idx)
        Returns a node given it's index. Performs bound checking and will
        return 0 if out-of-bounds.
        """
        ret = self._wrap_call(self._vtk_obj.GetNode, *args)
        return wrap_vtk(ret)

    def _get_number_of_nodes(self):
        return self._vtk_obj.GetNumberOfNodes()
    number_of_nodes = traits.Property(_get_number_of_nodes, help=\
        """
        Returns the number of nodes in this selection. Each node contains
        information about part of the selection.
        """
    )

    def add_node(self, *args):
        """
        V.add_node(SelectionNode)
        C++: virtual void AddNode(SelectionNode *)
        Adds a selection node.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddNode, *my_args)
        return ret

    def dump(self):
        """
        V.dump()
        C++: virtual void Dump()
        Dumps the contents of the selection, giving basic information
        only.
        """
        ret = self._vtk_obj.Dump()
        return ret
        

    def remove_all_nodes(self):
        """
        V.remove_all_nodes()
        C++: virtual void RemoveAllNodes()
        Removes a selection node.
        """
        ret = self._vtk_obj.RemoveAllNodes()
        return ret
        

    def remove_node(self, *args):
        """
        V.remove_node(int)
        C++: virtual void RemoveNode(unsigned int idx)
        V.remove_node(SelectionNode)
        C++: virtual void RemoveNode(SelectionNode *)
        Removes a selection node.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveNode, *my_args)
        return ret

    def subtract(self, *args):
        """
        V.subtract(Selection)
        C++: virtual void Subtract(Selection *selection)
        V.subtract(SelectionNode)
        C++: virtual void Subtract(SelectionNode *node)
        Remove the nodes from the specified selection from this
        selection. Assumes that selection node internal arrays are
        IdTypeArrays.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Subtract, *my_args)
        return ret

    def union(self, *args):
        """
        V.union(Selection)
        C++: virtual void Union(Selection *selection)
        V.union(SelectionNode)
        C++: virtual void Union(SelectionNode *node)
        Union this selection with the specified selection. Attempts to
        reuse selection nodes in this selection if properties match
        exactly. Otherwise, creates new selection nodes.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Union, *my_args)
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
            return super(Selection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Selection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit Selection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Selection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


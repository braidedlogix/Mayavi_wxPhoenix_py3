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


class HyperTreeCursor(Object):
    """
    HyperTreeCursor - Objects that can traverse hypertree nodes.
    
    Superclass: Object
    
    Objects that can traverse hyper_3tree nodes. It is an abstract class.
    Cursors are created by the hyper_3tree.
    @sa
    DataObject FieldData Hyper3TREEAlgorithm@par Thanks: This
    class was written by Philippe Pebay, Joachim Pouderoux and Charles
    Law, Kitware 2013 This work was supported in part by Commissariat a
    l'Energie Atomique (CEA/DIF)
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHyperTreeCursor, obj, update, **traits)
    
    def _get_child_index(self):
        return self._vtk_obj.GetChildIndex()
    child_index = traits.Property(_get_child_index, help=\
        """
        Return the child number of the current node relative to its
        parent.
        \pre not_root: !_is_root().
        \post valid_range: result>=0 && result<_get_number_of_children()
        """
    )

    def _get_current_level(self):
        return self._vtk_obj.GetCurrentLevel()
    current_level = traits.Property(_get_current_level, help=\
        """
        Return the level of the node pointed by the cursor.
        \post positive_result: result>=0
        """
    )

    def _get_dimension(self):
        return self._vtk_obj.GetDimension()
    dimension = traits.Property(_get_dimension, help=\
        """
        Return the dimension of the tree.
        \post positive_result: result>0
        """
    )

    def get_index(self, *args):
        """
        V.get_index(int) -> int
        C++: virtual int GetIndex(int d)
        Return the index in dimension `d', as if the node was a cell of a
        uniform grid of 1<<_get_current_level() cells in each dimension.
        \pre valid_range: d>=0 && d<_get_dimension()
        \post valid_result: result>=0 && result<(_1<<_get_current_level())
        """
        ret = self._wrap_call(self._vtk_obj.GetIndex, *args)
        return ret

    def _get_leaf_id(self):
        return self._vtk_obj.GetLeafId()
    leaf_id = traits.Property(_get_leaf_id, help=\
        """
        Return the index of the current leaf in the data arrays.
        \pre is_leaf: is_leaf()
        """
    )

    def _get_node_id(self):
        return self._vtk_obj.GetNodeId()
    node_id = traits.Property(_get_node_id, help=\
        """
        Return the index of the current node in the data arrays.
        """
    )

    def _get_number_of_children(self):
        return self._vtk_obj.GetNumberOfChildren()
    number_of_children = traits.Property(_get_number_of_children, help=\
        """
        Return the number of children for each node of the tree.
        \post positive_number: result>0
        """
    )

    def _get_tree(self):
        return wrap_vtk(self._vtk_obj.GetTree())
    tree = traits.Property(_get_tree, help=\
        """
        Return the hyper_tree on which the cursor points to.
        """
    )

    def clone(self):
        """
        V.clone() -> HyperTreeCursor
        C++: virtual HyperTreeCursor *Clone()
        Create a copy of `this'.
        \post results_exists:result!=0
        \post same_tree: result->_same_tree(this)
        """
        ret = wrap_vtk(self._vtk_obj.Clone())
        return ret
        

    def found(self):
        """
        V.found() -> bool
        C++: virtual bool Found()
        Did the last call to move_to_node succeed?
        """
        ret = self._vtk_obj.Found()
        return ret
        

    def is_equal(self, *args):
        """
        V.is_equal(HyperTreeCursor) -> bool
        C++: virtual bool IsEqual(HyperTreeCursor *other)
        Is `this' equal to `other'?
        \pre other_exists: other!=0
        \pre same_hyper_3tree: this->_same_tree(other);
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsEqual, *my_args)
        return ret

    def is_leaf(self):
        """
        V.is_leaf() -> bool
        C++: virtual bool IsLeaf()
        Is the node pointed by the cursor a leaf?
        """
        ret = self._vtk_obj.IsLeaf()
        return ret
        

    def is_root(self):
        """
        V.is_root() -> bool
        C++: virtual bool IsRoot()
        Is the node pointed by the cursor the root?
        """
        ret = self._vtk_obj.IsRoot()
        return ret
        

    def is_terminal_node(self):
        """
        V.is_terminal_node() -> bool
        C++: virtual bool IsTerminalNode()"""
        ret = self._vtk_obj.IsTerminalNode()
        return ret
        

    def move_to_node(self, *args):
        """
        V.move_to_node([int, ...], int)
        C++: virtual void MoveToNode(int *indices, int level)
        Move to the node described by its indices in each dimension and
        at a given level. If there is actually a node or a leaf at this
        location, Found() returns true. Otherwise, Found() returns false
        and the cursor moves to the closest parent of the query. It can
        be the root in the worst case.
        \pre indices_exists: indices!=0
        \pre valid_size: sizeof(indices)==_get_dimension()
        \pre valid_level: level>=0
        """
        ret = self._wrap_call(self._vtk_obj.MoveToNode, *args)
        return ret

    def same_tree(self, *args):
        """
        V.same_tree(HyperTreeCursor) -> int
        C++: virtual int SameTree(HyperTreeCursor *other)
        Are `this' and `other' pointing on the same hyper_3tree?
        \pre other_exists: other!=0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SameTree, *my_args)
        return ret

    def to_child(self, *args):
        """
        V.to_child(int)
        C++: virtual void ToChild(int child)
        Move the cursor to child `child' of the current node.
        \pre not_leaf: !_is_leaf()
        \pre valid_child: child>=0 && child<this->_get_number_of_children()
        """
        ret = self._wrap_call(self._vtk_obj.ToChild, *args)
        return ret

    def to_parent(self):
        """
        V.to_parent()
        C++: virtual void ToParent()
        Move the cursor to the parent of the current node.
        \pre not_root: !_is_root()
        """
        ret = self._vtk_obj.ToParent()
        return ret
        

    def to_root(self):
        """
        V.to_root()
        C++: virtual void ToRoot()
        Move the cursor to the root node.
        \pre can be root
        \post is_root: is_root()
        """
        ret = self._vtk_obj.ToRoot()
        return ret
        

    def to_same_node(self, *args):
        """
        V.to_same_node(HyperTreeCursor)
        C++: virtual void ToSameNode(HyperTreeCursor *other)
        Move the cursor to the same node pointed by `other'.
        \pre other_exists: other!=0
        \pre same_hyper_3tree: this->_same_tree(other);
        \post equal: this->_is_equal(other)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ToSameNode, *my_args)
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
            return super(HyperTreeCursor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HyperTreeCursor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit HyperTreeCursor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HyperTreeCursor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


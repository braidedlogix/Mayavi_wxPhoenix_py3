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


class TreeIterator(Object):
    """
    TreeIterator - Abstract class for iterator over a Tree.
    
    Superclass: Object
    
    The base class for tree iterators TreeBFSIterator and
    TreeDFSIterator.
    
    After setting up the iterator, the normal mode of operation is to set
    up a while(iter->_has_next())loop, with the statement IdType vertex
    = iter->Next()inside the loop.
    
    @sa
    TreeBFSIterator TreeDFSIterator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeIterator, obj, update, **traits)
    
    start_vertex = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        The start vertex of the traversal. The tree iterator will only
        iterate over the subtree rooted at vertex. If not set (or set to
        a negative value), starts at the root of the tree.
        """
    )

    def _start_vertex_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartVertex,
                        self.start_vertex)

    def _get_tree(self):
        return wrap_vtk(self._vtk_obj.GetTree())
    def _set_tree(self, arg):
        old_val = self._get_tree()
        self._wrap_call(self._vtk_obj.SetTree,
                        deref_vtk(arg))
        self.trait_property_changed('tree', old_val, arg)
    tree = traits.Property(_get_tree, _set_tree, help=\
        """
        Set/get the graph to iterate over.
        """
    )

    def has_next(self):
        """
        V.has_next() -> bool
        C++: bool HasNext()
        Return true when all vertices have been visited.
        """
        ret = self._vtk_obj.HasNext()
        return ret
        

    def next(self):
        """
        V.next() -> int
        C++: IdType Next()
        The next vertex visited in the graph.
        """
        ret = self._vtk_obj.Next()
        return ret
        

    def restart(self):
        """
        V.restart()
        C++: void Restart()
        Reset the iterator to its start vertex.
        """
        ret = self._vtk_obj.Restart()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('start_vertex', 'GetStartVertex'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'start_vertex'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['start_vertex']),
            title='Edit TreeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


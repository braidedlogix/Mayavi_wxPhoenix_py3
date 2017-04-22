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

from tvtk.tvtk_classes.tree_iterator import TreeIterator


class TreeDFSIterator(TreeIterator):
    """
    TreeDFSIterator - depth first iterator through a Graph
    
    Superclass: TreeIterator
    
    TreeDFSIterator performs a depth first search traversal of a tree.
    
    First, you must set the tree on which you are going to iterate, and
    then optionally set the starting vertex and mode. The mode is either
    DISCOVER (default), in which case vertices are visited as they are
    first reached, or FINISH, in which case vertices are visited when
    they are done, i.e. all adjacent vertices have been discovered
    already.
    
    After setting up the iterator, the normal mode of operation is to set
    up a while(iter->_has_next())loop, with the statement IdType vertex
    = iter->Next()inside the loop.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeDFSIterator, obj, update, **traits)
    
    mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the visit mode of the iterator.  Mode can be DISCOVER (0):
        Order by discovery time FINISH   (1): Order by finish time
        Default is DISCOVER. Use DISCOVER for top-down algorithms where
        parents need to be processed before children. Use FINISH for
        bottom-up algorithms where children need to be processed before
        parents.
        """
    )

    def _mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMode,
                        self.mode)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('mode', 'GetMode'), ('start_vertex',
    'GetStartVertex'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'mode', 'start_vertex'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeDFSIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeDFSIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['mode', 'start_vertex']),
            title='Edit TreeDFSIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeDFSIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


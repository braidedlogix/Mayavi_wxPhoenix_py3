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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class ExtractBlock(MultiBlockDataSetAlgorithm):
    """
    ExtractBlock - extracts blocks from a multiblock dataset.
    
    Superclass: MultiBlockDataSetAlgorithm
    
    ExtractBlock is a filter that extracts blocks from a multiblock
    dataset. Each node in the multi-block tree is identified by an index.
    The index can be obtained by performing a preorder traversal of the
    tree (including empty nodes). eg. A(B (D, E), C(F, G)). Inorder
    traversal yields: A, B, D, E, C, F, G Index of A is 0, while index of
    C is 4.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractBlock, obj, update, **traits)
    
    maintain_structure = tvtk_base.false_bool_trait(help=\
        """
        This is used only when prune_output is ON. By default, when
        pruning the output i.e. remove empty blocks, if node has only 1
        non-null child block, then that node is removed. To preserve
        these parent nodes, set this flag to true. Off by default.
        """
    )

    def _maintain_structure_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaintainStructure,
                        self.maintain_structure_)

    prune_output = tvtk_base.true_bool_trait(help=\
        """
        When set, the output mutliblock dataset will be pruned to remove
        empty nodes. On by default.
        """
    )

    def _prune_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPruneOutput,
                        self.prune_output_)

    def add_index(self, *args):
        """
        V.add_index(int)
        C++: void AddIndex(unsigned int index)
        Select the block indices to extract. Each node in the multi-block
        tree is identified by an index. The index can be obtained by
        performing a preorder traversal of the tree (including empty
        nodes). eg. A(B (D, E), C(F, G)). Inorder traversal yields: A, B,
        D, E, C, F, G Index of A is 0, while index of C is 4.
        """
        ret = self._wrap_call(self._vtk_obj.AddIndex, *args)
        return ret

    def remove_all_indices(self):
        """
        V.remove_all_indices()
        C++: void RemoveAllIndices()
        Select the block indices to extract. Each node in the multi-block
        tree is identified by an index. The index can be obtained by
        performing a preorder traversal of the tree (including empty
        nodes). eg. A(B (D, E), C(F, G)). Inorder traversal yields: A, B,
        D, E, C, F, G Index of A is 0, while index of C is 4.
        """
        ret = self._vtk_obj.RemoveAllIndices()
        return ret
        

    def remove_index(self, *args):
        """
        V.remove_index(int)
        C++: void RemoveIndex(unsigned int index)
        Select the block indices to extract. Each node in the multi-block
        tree is identified by an index. The index can be obtained by
        performing a preorder traversal of the tree (including empty
        nodes). eg. A(B (D, E), C(F, G)). Inorder traversal yields: A, B,
        D, E, C, F, G Index of A is 0, while index of C is 4.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveIndex, *args)
        return ret

    _updateable_traits_ = \
    (('maintain_structure', 'GetMaintainStructure'), ('prune_output',
    'GetPruneOutput'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'maintain_structure', 'prune_output', 'release_data_flag',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractBlock, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractBlock properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['maintain_structure', 'prune_output'], [], []),
            title='Edit ExtractBlock properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractBlock properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class UniformGridPartitioner(MultiBlockDataSetAlgorithm):
    """
    UniformGridPartitioner -  A concrete implementation of
    MultiBlockDataSetAlgorithm that provides
     functionality for partitioning a uniform grid.
    
    Superclass: MultiBlockDataSetAlgorithm
    
    The partitioning method
     that is used is Recursive Coordinate Bisection (RCB) where each time
     the longest dimension is split.
    
    @sa
    StructuredGridPartitioner RectilinearGridPartitioner
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUniformGridPartitioner, obj, update, **traits)
    
    duplicate_nodes = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )

    def _duplicate_nodes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDuplicateNodes,
                        self.duplicate_nodes_)

    number_of_ghost_layers = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get macro for the number of ghost layers.
        """
    )

    def _number_of_ghost_layers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfGhostLayers,
                        self.number_of_ghost_layers)

    number_of_partitions = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set/Get macro for the number of subdivisions.
        """
    )

    def _number_of_partitions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPartitions,
                        self.number_of_partitions)

    _updateable_traits_ = \
    (('duplicate_nodes', 'GetDuplicateNodes'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_ghost_layers',
    'GetNumberOfGhostLayers'), ('number_of_partitions',
    'GetNumberOfPartitions'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'duplicate_nodes',
    'global_warning_display', 'release_data_flag',
    'number_of_ghost_layers', 'number_of_partitions', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UniformGridPartitioner, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UniformGridPartitioner properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['duplicate_nodes'], [], ['number_of_ghost_layers',
            'number_of_partitions']),
            title='Edit UniformGridPartitioner properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UniformGridPartitioner properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


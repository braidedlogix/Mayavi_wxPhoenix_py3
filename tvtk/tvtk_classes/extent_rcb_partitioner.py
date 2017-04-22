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


class ExtentRCBPartitioner(Object):
    """
    ExtentRCBPartitioner -  This method partitions a global extent to
    N partitions where N is a user
     supplied parameter.
    
    Superclass: Object
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtentRCBPartitioner, obj, update, **traits)
    
    duplicate_nodes = tvtk_base.true_bool_trait(help=\
        """
        On/Off duplicate_nodes between partitions. Default is On.
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

    def _get_num_extents(self):
        return self._vtk_obj.GetNumExtents()
    num_extents = traits.Property(_get_num_extents, help=\
        """
        Returns the number of extents.
        """
    )

    def get_partition_extent(self, *args):
        """
        V.get_partition_extent(int, [int, int, int, int, int, int])
        C++: void GetPartitionExtent(const int idx, int ext[6])
        Returns the extent of the partition corresponding to the given
        ID.
        """
        ret = self._wrap_call(self._vtk_obj.GetPartitionExtent, *args)
        return ret

    def partition(self):
        """
        V.partition()
        C++: void Partition()
        Partitions the extent
        """
        ret = self._vtk_obj.Partition()
        return ret
        

    def set_global_extent(self, *args):
        """
        V.set_global_extent(int, int, int, int, int, int)
        C++: void SetGlobalExtent(int imin, int imax, int jmin, int jmax,
            int kmin, int kmax)
        V.set_global_extent([int, int, int, int, int, int])
        C++: void SetGlobalExtent(int ext[6])
        Set/Get the global extent array to be partitioned. The global
        extent is packed as follows: [imin,imax,jmin,jmax,kmin,kmax]
        """
        ret = self._wrap_call(self._vtk_obj.SetGlobalExtent, *args)
        return ret

    def set_number_of_partitions(self, *args):
        """
        V.set_number_of_partitions(int)
        C++: void SetNumberOfPartitions(const int N)
        Set/Get the number of requested partitions
        """
        ret = self._wrap_call(self._vtk_obj.SetNumberOfPartitions, *args)
        return ret

    _updateable_traits_ = \
    (('duplicate_nodes', 'GetDuplicateNodes'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_ghost_layers', 'GetNumberOfGhostLayers'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'duplicate_nodes', 'global_warning_display',
    'number_of_ghost_layers'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtentRCBPartitioner, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtentRCBPartitioner properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['duplicate_nodes'], [], ['number_of_ghost_layers']),
            title='Edit ExtentRCBPartitioner properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtentRCBPartitioner properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


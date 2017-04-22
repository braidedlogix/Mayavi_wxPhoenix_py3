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


class SubGroup(Object):
    """
    SubGroup - scalable collective communication for a
         subset of members of a parallel VTK application
    
    Superclass: Object
    
    This class provides scalable broadcast, reduce, etc. using
        only a MultiProcessController. It does not require MPI.
        Users are PKdTree and DistributedDataFilter.
    
    @attention This class will be deprecated soon.  Instead of using this
    class, use the collective and subgrouping operations now built into
    MultiProcessController.  The only reason this class is not
    deprecated already is because PKdTree relies heavily on this class
    in ways that are not easy to work around.  Since PKdTree is due
    for a major overhaul anyway, we are leaving things the way they are
    for now.
    
    @sa
         PKdTree DistributedDataFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSubGroup, obj, update, **traits)
    
    def barrier(self):
        """
        V.barrier() -> int
        C++: int Barrier()"""
        ret = self._vtk_obj.Barrier()
        return ret
        

    def broadcast(self, *args):
        """
        V.broadcast([float, ...], int, int) -> int
        C++: int Broadcast(double *data, int length, int root)
        V.broadcast([int, ...], int, int) -> int
        C++: int Broadcast(int *data, int length, int root)
        V.broadcast(string, int, int) -> int
        C++: int Broadcast(char *data, int length, int root)
        V.broadcast([int, ...], int, int) -> int
        C++: int Broadcast(IdType *data, int length, int root)"""
        ret = self._wrap_call(self._vtk_obj.Broadcast, *args)
        return ret

    def gather(self, *args):
        """
        V.gather([int, ...], [int, ...], int, int) -> int
        C++: int Gather(int *data, int *to, int length, int root)
        V.gather(string, string, int, int) -> int
        C++: int Gather(char *data, char *to, int length, int root)
        V.gather([float, ...], [float, ...], int, int) -> int
        C++: int Gather(float *data, float *to, int length, int root)
        V.gather([int, ...], [int, ...], int, int) -> int
        C++: int Gather(IdType *data, IdType *to, int length,
            int root)"""
        ret = self._wrap_call(self._vtk_obj.Gather, *args)
        return ret

    def initialize(self, *args):
        """
        V.initialize(int, int, int, int, Communicator) -> int
        C++: int Initialize(int p0, int p1, int me, int tag,
            Communicator *c)
        Initialize a communication subgroup for the processes with rank
        p0 through p1 of the given communicator.  (So SubGroup is
        limited to working with subgroups that are identified by a
        contiguous set of rank IDs.) The third argument is the callers
        rank, which must in the range from p0 through p1.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Initialize, *my_args)
        return ret

    def print_sub_group(self):
        """
        V.print_sub_group()
        C++: void PrintSubGroup()"""
        ret = self._vtk_obj.PrintSubGroup()
        return ret
        

    def reduce_max(self, *args):
        """
        V.reduce_max([float, ...], [float, ...], int, int) -> int
        C++: int ReduceMax(double *data, double *to, int length, int root)
        V.reduce_max([int, ...], [int, ...], int, int) -> int
        C++: int ReduceMax(int *data, int *to, int length, int root)"""
        ret = self._wrap_call(self._vtk_obj.ReduceMax, *args)
        return ret

    def reduce_min(self, *args):
        """
        V.reduce_min([float, ...], [float, ...], int, int) -> int
        C++: int ReduceMin(double *data, double *to, int length, int root)
        V.reduce_min([int, ...], [int, ...], int, int) -> int
        C++: int ReduceMin(int *data, int *to, int length, int root)"""
        ret = self._wrap_call(self._vtk_obj.ReduceMin, *args)
        return ret

    def reduce_sum(self, *args):
        """
        V.reduce_sum([int, ...], [int, ...], int, int) -> int
        C++: int ReduceSum(int *data, int *to, int length, int root)"""
        ret = self._wrap_call(self._vtk_obj.ReduceSum, *args)
        return ret

    def get_local_rank(self, *args):
        """
        V.get_local_rank(int) -> int
        C++: int getLocalRank(int processID)"""
        ret = self._wrap_call(self._vtk_obj.getLocalRank, *args)
        return ret

    def set_gather_pattern(self, *args):
        """
        V.set_gather_pattern(int, int)
        C++: void setGatherPattern(int root, int length)"""
        ret = self._wrap_call(self._vtk_obj.setGatherPattern, *args)
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
            return super(SubGroup, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SubGroup properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit SubGroup properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SubGroup properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class ProcessGroup(Object):
    """
    ProcessGroup - A subgroup of processes from a communicator.
    
    Superclass: Object
    
    This class is used for creating groups of processes.  A
    ProcessGroup is initialized by passing the controller or
    communicator on which the group is based off of.  You can then use
    the group to subset and reorder the the processes.  Eventually, you
    can pass the group object to the create_sub_controller method of
    MultiProcessController to create a controller for the defined
    group of processes.  You must use the same controller (or attached
    communicator) from which this group was initialized with.
    
    @sa
    MultiProcessController, Communicator
    
    @par Thanks: This class was originally written by Kenneth Moreland
    (kmorel@sandia.gov) from Sandia National Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProcessGroup, obj, update, **traits)
    
    def _get_communicator(self):
        return wrap_vtk(self._vtk_obj.GetCommunicator())
    def _set_communicator(self, arg):
        old_val = self._get_communicator()
        self._wrap_call(self._vtk_obj.SetCommunicator,
                        deref_vtk(arg))
        self.trait_property_changed('communicator', old_val, arg)
    communicator = traits.Property(_get_communicator, _set_communicator, help=\
        """
        Get the communicator on which this group is based on.
        """
    )

    def _get_local_process_id(self):
        return self._vtk_obj.GetLocalProcessId()
    local_process_id = traits.Property(_get_local_process_id, help=\
        """
        Get the process id for the local process (as defined by the
        group's communicator).  Returns -1 if the local process is not in
        the group.
        """
    )

    def _get_number_of_process_ids(self):
        return self._vtk_obj.GetNumberOfProcessIds()
    number_of_process_ids = traits.Property(_get_number_of_process_ids, help=\
        """
        Returns the size of this group (the number of processes defined
        in it).
        """
    )

    def get_process_id(self, *args):
        """
        V.get_process_id(int) -> int
        C++: int GetProcessId(int pos)
        Given a position in the group, returns the id of the process in
        the communicator this group is based on.  For example, if this
        group contains {6, 2, 8, 1}, then get_process_id(_2) will return 8
        and get_process_id(_3) will return 1.
        """
        ret = self._wrap_call(self._vtk_obj.GetProcessId, *args)
        return ret

    def add_process_id(self, *args):
        """
        V.add_process_id(int) -> int
        C++: int AddProcessId(int processId)
        Add a process id to the end of the group (if it is not already in
        the group).  Returns the location where the id was stored.
        """
        ret = self._wrap_call(self._vtk_obj.AddProcessId, *args)
        return ret

    def copy(self, *args):
        """
        V.copy(ProcessGroup)
        C++: void Copy(ProcessGroup *group)
        Copies the given group's communicator and process ids.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Copy, *my_args)
        return ret

    def find_process_id(self, *args):
        """
        V.find_process_id(int) -> int
        C++: int FindProcessId(int processId)
        Given a process id in the communicator, this method returns its
        location in the group or -1 if it is not in the group.  For
        example, if this group contains {6, 2, 8, 1}, then
        find_process_id(_2) will return 1 and find_process_id(_3) will return
        -1.
        """
        ret = self._wrap_call(self._vtk_obj.FindProcessId, *args)
        return ret

    def initialize(self, *args):
        """
        V.initialize(MultiProcessController)
        C++: void Initialize(MultiProcessController *controller)
        V.initialize(Communicator)
        C++: void Initialize(Communicator *communicator)
        Initialize the group to the given controller or communicator. 
        The group will be set to contain all of the processes in the
        controller/communicator in the same order.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Initialize, *my_args)
        return ret

    def remove_all_process_ids(self):
        """
        V.remove_all_process_ids()
        C++: void RemoveAllProcessIds()
        Removes all the processes ids from the group, leaving the group
        empty.
        """
        ret = self._vtk_obj.RemoveAllProcessIds()
        return ret
        

    def remove_process_id(self, *args):
        """
        V.remove_process_id(int) -> int
        C++: int RemoveProcessId(int processId)
        Remove the given process id from the group (assuming it is in the
        group). All ids to the "right" of the removed id are shifted
        over.  Returns 1 if the process id was removed, 0 if the process
        id was not in the group in the first place.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveProcessId, *args)
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
            return super(ProcessGroup, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ProcessGroup properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ProcessGroup properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProcessGroup properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class MultiProcessController(Object):
    """
    MultiProcessController - Multiprocessing communication superclass
    
    Superclass: Object
    
    MultiProcessController is used to control multiple processes in a
    distributed computing environment. It has methods for executing
    single/multiple method(s) on multiple processors, triggering
    registered callbacks (Remote Methods) (_add_rmi(), trigger_rmi()) and
    communication. Please note that the communication is done using the
    communicator which is accessible to the user. Therefore it is
    possible to get the communicator with get_communicator() and use it to
    send and receive data. This is the encouraged communication method.
    The internal (RMI) communications are done using a second internal
    communicator (called RMICommunicator).
    
    There are two modes for RMI communication: (1) Send/Receive mode and
    (2) Broadcast (collective) mode. The Send/Receive mode arranges
    processes in a binary tree using post-order traversal and propagates
    the RMI trigger starting from the root (rank 0) to the children. It
    is commonly employed to communicate between client/server over TCP.
    Although, the Send/Receive mode can be employed transparently over
    TCP or MPI, it is not optimal for triggering the RMIs on the
    satellite ranks. The Broadcast mode provides a more desirable
    alternative, namely, it uses MPI_Broadcast for communication, which
    is the nominal way of achieving this in an MPI context. The
    underlying communication mode used for triggering RMIs is controlled
    by the "_broadcast_trigger_rmi" variable. Note, that mixing between the
    two modes for RMI communication is not correct behavior. All
    processes within the MultiProcessController must use the same mode
    for triggering RMI.
    
    @sa
    MPIController Communicator MPICommunicator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMultiProcessController, obj, update, **traits)
    
    broadcast_trigger_rmi = tvtk_base.false_bool_trait(help=\
        """
        Setting this flag to 1 will cause the trigger_rmi_on_all_children to
        use a collective broadcast operation to communicate the RMI tag
        to the sattelites.
        """
    )

    def _broadcast_trigger_rmi_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBroadcastTriggerRMI,
                        self.broadcast_trigger_rmi_)

    break_flag = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Setting this flag to 1 will cause the process_rm_is loop to return.
        This also causes UpStreamPorts to return from their
        wait_for_update loops.
        """
    )

    def _break_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBreakFlag,
                        self.break_flag)

    def _get_global_controller(self):
        return wrap_vtk(self._vtk_obj.GetGlobalController())
    def _set_global_controller(self, arg):
        old_val = self._get_global_controller()
        self._wrap_call(self._vtk_obj.SetGlobalController,
                        deref_vtk(arg))
        self.trait_property_changed('global_controller', old_val, arg)
    global_controller = traits.Property(_get_global_controller, _set_global_controller, help=\
        """
        This convenience method returns the controller associated with
        the local process.  It returns NULL until the processes are
        spawned. It is better if you hang on to the controller passed as
        an argument to the single_method or multiple_method functions.
        """
    )

    number_of_processes = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the number of processes you will be using.  This defaults to
        the maximum number available.  If you set this to a value higher
        than the default, you will get an error.
        """
    )

    def _number_of_processes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfProcesses,
                        self.number_of_processes)

    def _get_break_rmi_tag(self):
        return self._vtk_obj.GetBreakRMITag()
    break_rmi_tag = traits.Property(_get_break_rmi_tag, help=\
        """
        Accessor to some default tags.
        """
    )

    def _get_communicator(self):
        return wrap_vtk(self._vtk_obj.GetCommunicator())
    communicator = traits.Property(_get_communicator, help=\
        """
        Returns the communicator associated with this controller. A
        default communicator is created in constructor.
        """
    )

    def _get_count(self):
        return self._vtk_obj.GetCount()
    count = traits.Property(_get_count, help=\
        """
        Returns the number of words received by the most recent
        Receive(). Note that this is not the number of bytes received,
        but the number of items of the data-type received by the most
        recent Receive() eg. if Receive(int*,..) was used, then this
        returns the number of ints received; if Receive(double*,..) was
        used, then this returns the number of doubles received etc. The
        return value is valid only after a successful Receive().
        """
    )

    def _get_local_process_id(self):
        return self._vtk_obj.GetLocalProcessId()
    local_process_id = traits.Property(_get_local_process_id, help=\
        """
        Tells you which process [0, num_process) you are in.
        """
    )

    def _get_rmi_arg_tag(self):
        return self._vtk_obj.GetRMIArgTag()
    rmi_arg_tag = traits.Property(_get_rmi_arg_tag, help=\
        """
        
        """
    )

    def _get_rmi_tag(self):
        return self._vtk_obj.GetRMITag()
    rmi_tag = traits.Property(_get_rmi_tag, help=\
        """
        
        """
    )

    def all_gather(self, *args):
        """
        V.all_gather((int, ...), [int, ...], int) -> int
        C++: int AllGather(const int *sendBuffer, int *recvBuffer,
            IdType length)
        V.all_gather((int, ...), [int, ...], int) -> int
        C++: int AllGather(const long *sendBuffer, long *recvBuffer,
            IdType length)
        V.all_gather(string, string, int) -> int
        C++: int AllGather(const char *sendBuffer, char *recvBuffer,
            IdType length)
        V.all_gather((float, ...), [float, ...], int) -> int
        C++: int AllGather(const double *sendBuffer, double *recvBuffer,
            IdType length)
        V.all_gather((int, ...), [int, ...], int) -> int
        C++: int AllGather(const long long *sendBuffer,
            long long *recvBuffer, IdType length)
        V.all_gather(DataArray, DataArray) -> int
        C++: int AllGather(DataArray *sendBuffer,
            DataArray *recvBuffer)
        Same as gather except that the result ends up on all processes.
        """
        my_args = deref_array(args, [(('int', Ellipsis), ['int', Ellipsis], 'int'), (('int', Ellipsis), ['int', Ellipsis], 'int'), ('string', 'string', 'int'), (('float', Ellipsis), 'tuple', 'int'), (('int', Ellipsis), ['int', Ellipsis], 'int'), ('vtkDataArray', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.AllGather, *my_args)
        return ret

    def all_gather_v(self, *args):
        """
        V.all_gather_v((int, ...), [int, ...], int, [int, ...], [int, ...])
            -> int
        C++: int AllGatherV(const int *sendBuffer, int *recvBuffer,
            IdType sendLength, IdType *recvLengths,
            IdType *offsets)
        V.all_gather_v((int, ...), [int, ...], int, [int, ...], [int, ...])
            -> int
        C++: int AllGatherV(const long *sendBuffer, long *recvBuffer,
            IdType sendLength, IdType *recvLengths,
            IdType *offsets)
        V.all_gather_v(string, string, int, [int, ...], [int, ...]) -> int
        C++: int AllGatherV(const char *sendBuffer, char *recvBuffer,
            IdType sendLength, IdType *recvLengths,
            IdType *offsets)
        V.all_gather_v((float, ...), [float, ...], int, [int, ...], [int,
            ...]) -> int
        C++: int AllGatherV(const double *sendBuffer, double *recvBuffer,
            IdType sendLength, IdType *recvLengths,
            IdType *offsets)
        V.all_gather_v((int, ...), [int, ...], int, [int, ...], [int, ...])
            -> int
        C++: int AllGatherV(const long long *sendBuffer,
            long long *recvBuffer, IdType sendLength,
            IdType *recvLengths, IdType *offsets)
        V.all_gather_v(DataArray, DataArray, [int, ...], [int, ...])
            -> int
        C++: int AllGatherV(DataArray *sendBuffer,
            DataArray *recvBuffer, IdType *recvLengths,
            IdType *offsets)
        V.all_gather_v(DataArray, DataArray) -> int
        C++: int AllGatherV(DataArray *sendBuffer,
            DataArray *recvBuffer)
        Same as gather_v except that the result is placed in all
        processes.
        """
        my_args = deref_array(args, [(('int', Ellipsis), ['int', Ellipsis], 'int', ['int', Ellipsis], ['int', Ellipsis]), (('int', Ellipsis), ['int', Ellipsis], 'int', ['int', Ellipsis], ['int', Ellipsis]), ('string', 'string', 'int', ['int', Ellipsis], ['int', Ellipsis]), (('float', Ellipsis), 'tuple', 'int', ['int', Ellipsis], ['int', Ellipsis]), (('int', Ellipsis), ['int', Ellipsis], 'int', ['int', Ellipsis], ['int', Ellipsis]), ('vtkDataArray', 'vtkDataArray', ['int', Ellipsis], ['int', Ellipsis]), ('vtkDataArray', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.AllGatherV, *my_args)
        return ret

    def all_reduce(self, *args):
        """
        V.all_reduce((int, ...), [int, ...], int, int) -> int
        C++: int AllReduce(const int *sendBuffer, int *recvBuffer,
            IdType length, int operation)
        V.all_reduce((int, ...), [int, ...], int, int) -> int
        C++: int AllReduce(const long *sendBuffer, long *recvBuffer,
            IdType length, int operation)
        V.all_reduce(string, string, int, int) -> int
        C++: int AllReduce(const char *sendBuffer, char *recvBuffer,
            IdType length, int operation)
        V.all_reduce((float, ...), [float, ...], int, int) -> int
        C++: int AllReduce(const double *sendBuffer, double *recvBuffer,
            IdType length, int operation)
        V.all_reduce((int, ...), [int, ...], int, int) -> int
        C++: int AllReduce(const long long *sendBuffer,
            long long *recvBuffer, IdType length, int operation)
        V.all_reduce(DataArray, DataArray, int) -> int
        C++: int AllReduce(DataArray *sendBuffer,
            DataArray *recvBuffer, int operation)
        Same as Reduce except that the result is placed in all of the
        processes.
        """
        my_args = deref_array(args, [(('int', Ellipsis), ['int', Ellipsis], 'int', 'int'), (('int', Ellipsis), ['int', Ellipsis], 'int', 'int'), ('string', 'string', 'int', 'int'), (('float', Ellipsis), 'tuple', 'int', 'int'), (('int', Ellipsis), ['int', Ellipsis], 'int', 'int'), ('vtkDataArray', 'vtkDataArray', 'int')])
        ret = self._wrap_call(self._vtk_obj.AllReduce, *my_args)
        return ret

    def barrier(self):
        """
        V.barrier()
        C++: void Barrier()
        This method can be used to synchronize processes.
        """
        ret = self._vtk_obj.Barrier()
        return ret
        

    def broadcast(self, *args):
        """
        V.broadcast([int, ...], int, int) -> int
        C++: int Broadcast(int *data, IdType length, int srcProcessId)
        V.broadcast([int, ...], int, int) -> int
        C++: int Broadcast(long *data, IdType length, int srcProcessId)
        V.broadcast(string, int, int) -> int
        C++: int Broadcast(char *data, IdType length, int srcProcessId)
        V.broadcast([float, ...], int, int) -> int
        C++: int Broadcast(double *data, IdType length,
            int srcProcessId)
        V.broadcast([int, ...], int, int) -> int
        C++: int Broadcast(long long *data, IdType length,
            int srcProcessId)
        V.broadcast(DataObject, int) -> int
        C++: int Broadcast(DataObject *data, int srcProcessId)
        V.broadcast(DataArray, int) -> int
        C++: int Broadcast(DataArray *data, int srcProcessId)
        V.broadcast(MultiProcessStream, int) -> int
        C++: int Broadcast(MultiProcessStream &stream,
            int srcProcessId)
        Broadcast sends the array in the process with id src_process_id to
        all of the other processes.  All processes must call these method
        with the same arguments in order for it to complete.
        """
        my_args = deref_array(args, [(['int', Ellipsis], 'int', 'int'), (['int', Ellipsis], 'int', 'int'), ('string', 'int', 'int'), ('tuple', 'int', 'int'), (['int', Ellipsis], 'int', 'int'), ('vtkDataObject', 'int'), ('vtkDataArray', 'int'), ('vtkMultiProcessStream', 'int')])
        ret = self._wrap_call(self._vtk_obj.Broadcast, *my_args)
        return ret

    def broadcast_process_rm_is(self, *args):
        """
        V.broadcast_process_rm_is(int, int) -> int
        C++: int BroadcastProcessRMIs(int reportErrors, int dont_loop=0)
        Calling this method gives control to the controller to start
        processing RMIs. Possible return values are: RMI_NO_ERROR,
        RMI_TAG_ERROR : rmi tag could not be received, RMI_ARG_ERROR :
        rmi arg could not be received. If report_errors is false, no
        ErrorMacro is called. process_rm_is() calls process_rm_is(int)
        with report_errors = 0. If dont_loop is 1, this call just process
        one RMI message and exits.
        """
        ret = self._wrap_call(self._vtk_obj.BroadcastProcessRMIs, *args)
        return ret

    def broadcast_trigger_rmi_on_all_children(self, *args):
        """
        V.broadcast_trigger_rmi_on_all_children(void, int, int)
        C++: void BroadcastTriggerRMIOnAllChildren(void *arg,
            int argLength, int tag)
        This is a convenicence method to trigger an RMI call on all the
        "children" of the current node. The children of the current node
        can be determined by drawing a binary tree starting at node 0 and
        then assigned nodes ids incrementally in a breadth-first fashion
        from left to right. This is designed to be used when trigger an
        RMI call on all satellites from the root node.
        """
        ret = self._wrap_call(self._vtk_obj.BroadcastTriggerRMIOnAllChildren, *args)
        return ret

    def create_output_window(self):
        """
        V.create_output_window()
        C++: virtual void CreateOutputWindow()
        This method can be used to tell the controller to create a
        special output window in which all messages are preceded by the
        process id.
        """
        ret = self._vtk_obj.CreateOutputWindow()
        return ret
        

    def create_sub_controller(self, *args):
        """
        V.create_sub_controller(ProcessGroup)
            -> MultiProcessController
        C++: virtual MultiProcessController *CreateSubController(
            ProcessGroup *group)
        Creates a new controller with the processes specified by the
        given group. The new controller will already be initialized for
        you.  You are responsible for deleting the controller once you
        are done.  It is invalid to pass this method a group with a
        different communicator than is used by this controller.  This
        operation is collective across all processes defined in the
        group.  It is undefined what will happen if the group is not the
        same on all processes.  This method must be called by all
        processes in the controller regardless of whether they are in the
        group.  NULL is returned on all process not in the group.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CreateSubController, *my_args)
        return wrap_vtk(ret)

    def finalize(self, *args):
        """
        V.finalize()
        C++: virtual void Finalize()
        V.finalize(int)
        C++: virtual void Finalize(int finalizedExternally)
        This method is for cleaning up. If a subclass needs to clean up
        process communication (i.e. MPI) it would over ride this method.
        """
        ret = self._wrap_call(self._vtk_obj.Finalize, *args)
        return ret

    def gather(self, *args):
        """
        V.gather((int, ...), [int, ...], int, int) -> int
        C++: int Gather(const int *sendBuffer, int *recvBuffer,
            IdType length, int destProcessId)
        V.gather((int, ...), [int, ...], int, int) -> int
        C++: int Gather(const long *sendBuffer, long *recvBuffer,
            IdType length, int destProcessId)
        V.gather(string, string, int, int) -> int
        C++: int Gather(const char *sendBuffer, char *recvBuffer,
            IdType length, int destProcessId)
        V.gather((float, ...), [float, ...], int, int) -> int
        C++: int Gather(const double *sendBuffer, double *recvBuffer,
            IdType length, int destProcessId)
        V.gather((int, ...), [int, ...], int, int) -> int
        C++: int Gather(const long long *sendBuffer,
            long long *recvBuffer, IdType length, int destProcessId)
        V.gather(DataArray, DataArray, int) -> int
        C++: int Gather(DataArray *sendBuffer,
            DataArray *recvBuffer, int destProcessId)
        Gather collects arrays in the process with id dest_process_id. 
        Each process (including the destination) sends the contents of
        its send buffer to the destination process.  The destination
        process receives the messages and stores them in rank order.  The
        length argument (which must be the same on all processes) is the
        length of the send_buffers.  The recv_buffer (on te destination
        process) must be of length length*num_processes.  Gather is the
        inverse operation of Scatter.
        """
        my_args = deref_array(args, [(('int', Ellipsis), ['int', Ellipsis], 'int', 'int'), (('int', Ellipsis), ['int', Ellipsis], 'int', 'int'), ('string', 'string', 'int', 'int'), (('float', Ellipsis), 'tuple', 'int', 'int'), (('int', Ellipsis), ['int', Ellipsis], 'int', 'int'), ('vtkDataArray', 'vtkDataArray', 'int')])
        ret = self._wrap_call(self._vtk_obj.Gather, *my_args)
        return ret

    def gather_v(self, *args):
        """
        V.gather_v((int, ...), [int, ...], int, [int, ...], [int, ...],
            int) -> int
        C++: int GatherV(const int *sendBuffer, int *recvBuffer,
            IdType sendLength, IdType *recvLengths,
            IdType *offsets, int destProcessId)
        V.gather_v((int, ...), [int, ...], int, [int, ...], [int, ...],
            int) -> int
        C++: int GatherV(const long *sendBuffer, long *recvBuffer,
            IdType sendLength, IdType *recvLengths,
            IdType *offsets, int destProcessId)
        V.gather_v(string, string, int, [int, ...], [int, ...], int) -> int
        C++: int GatherV(const char *sendBuffer, char *recvBuffer,
            IdType sendLength, IdType *recvLengths,
            IdType *offsets, int destProcessId)
        V.gather_v((float, ...), [float, ...], int, [int, ...], [int, ...],
             int) -> int
        C++: int GatherV(const double *sendBuffer, double *recvBuffer,
            IdType sendLength, IdType *recvLengths,
            IdType *offsets, int destProcessId)
        V.gather_v((int, ...), [int, ...], int, [int, ...], [int, ...],
            int) -> int
        C++: int GatherV(const long long *sendBuffer,
            long long *recvBuffer, IdType sendLength,
            IdType *recvLengths, IdType *offsets, int destProcessId)
        V.gather_v(DataArray, DataArray, [int, ...], [int, ...], int)
             -> int
        C++: int GatherV(DataArray *sendBuffer,
            DataArray *recvBuffer, IdType *recvLengths,
            IdType *offsets, int destProcessId)
        V.gather_v(DataArray, DataArray, IdTypeArray,
            IdTypeArray, int) -> int
        C++: int GatherV(DataArray *sendBuffer,
            DataArray *recvBuffer, IdTypeArray *recvLengths,
            IdTypeArray *offsets, int destProcessId)
        V.gather_v(DataArray, DataArray, int) -> int
        C++: int GatherV(DataArray *sendBuffer,
            DataArray *recvBuffer, int destProcessId)
        gather_v is the vector variant of Gather.  It extends the
        functionality of Gather by allowing a varying count of data from
        each process. gather_v collects arrays in the process with id
        dest_process_id.  Each process (including t ...
         [Truncated]
        """
        my_args = deref_array(args, [(('int', Ellipsis), ['int', Ellipsis], 'int', ['int', Ellipsis], ['int', Ellipsis], 'int'), (('int', Ellipsis), ['int', Ellipsis], 'int', ['int', Ellipsis], ['int', Ellipsis], 'int'), ('string', 'string', 'int', ['int', Ellipsis], ['int', Ellipsis], 'int'), (('float', Ellipsis), 'tuple', 'int', ['int', Ellipsis], ['int', Ellipsis], 'int'), (('int', Ellipsis), ['int', Ellipsis], 'int', ['int', Ellipsis], ['int', Ellipsis], 'int'), ('vtkDataArray', 'vtkDataArray', ['int', Ellipsis], ['int', Ellipsis], 'int'), ('vtkDataArray', 'vtkDataArray', 'vtkIdTypeArray', 'vtkIdTypeArray', 'int'), ('vtkDataArray', 'vtkDataArray', 'int')])
        ret = self._wrap_call(self._vtk_obj.GatherV, *my_args)
        return ret

    def multiple_method_execute(self):
        """
        V.multiple_method_execute()
        C++: virtual void MultipleMethodExecute()
        Execute the multiple_methods (as define by calling
        set_multiple_method for each of the required
        this->_number_of_processes methods) using this->_number_of_processes
        processes.
        """
        ret = self._vtk_obj.MultipleMethodExecute()
        return ret
        

    def partition_controller(self, *args):
        """
        V.partition_controller(int, int) -> MultiProcessController
        C++: virtual MultiProcessController *PartitionController(
            int localColor, int localKey)
        Partitions this controller based on a coloring.  That is, each
        process passes in a color.  All processes with the same color are
        grouped into the same partition.  The processes are ordered by
        their self-assigned key. Lower keys have lower process ids.  Ties
        are broken by the current process ids.  (For example, if all the
        keys are 0, then the resulting processes will be ordered in the
        same way.)  This method returns a new controller to each process
        that represents the local partition.  This is basically the same
        operation as MPI_Comm_split.
        """
        ret = self._wrap_call(self._vtk_obj.PartitionController, *args)
        return wrap_vtk(ret)

    def process_rm_is(self, *args):
        """
        V.process_rm_is(int, int) -> int
        C++: int ProcessRMIs(int reportErrors, int dont_loop=0)
        V.process_rm_is() -> int
        C++: int ProcessRMIs()
        Calling this method gives control to the controller to start
        processing RMIs. Possible return values are: RMI_NO_ERROR,
        RMI_TAG_ERROR : rmi tag could not be received, RMI_ARG_ERROR :
        rmi arg could not be received. If report_errors is false, no
        ErrorMacro is called. process_rm_is() calls process_rm_is(int)
        with report_errors = 0. If dont_loop is 1, this call just process
        one RMI message and exits.
        """
        ret = self._wrap_call(self._vtk_obj.ProcessRMIs, *args)
        return ret

    def receive(self, *args):
        """
        V.receive([int, ...], int, int, int) -> int
        C++: int Receive(int *data, IdType maxlength,
            int remoteProcessId, int tag)
        V.receive([int, ...], int, int, int) -> int
        C++: int Receive(long *data, IdType maxlength,
            int remoteProcessId, int tag)
        V.receive(string, int, int, int) -> int
        C++: int Receive(char *data, IdType maxlength,
            int remoteProcessId, int tag)
        V.receive([float, ...], int, int, int) -> int
        C++: int Receive(double *data, IdType maxlength,
            int remoteProcessId, int tag)
        V.receive([int, ...], int, int, int) -> int
        C++: int Receive(long long *data, IdType maxLength,
            int remoteProcessId, int tag)
        V.receive(DataObject, int, int) -> int
        C++: int Receive(DataObject *data, int remoteId, int tag)
        V.receive(DataArray, int, int) -> int
        C++: int Receive(DataArray *data, int remoteId, int tag)
        V.receive(MultiProcessStream, int, int) -> int
        C++: int Receive(MultiProcessStream &stream, int remoteId,
            int tag)
        This method receives data from a corresponding send. It blocks
        until the receive is finished.  It calls methods in "data" to
        communicate the sending data. In the overrloads that take in a \c
        maxlength argument, this length is the maximum length of the
        message to receive. If the maxlength is less than the length of
        the message sent by the sender, an error will be flagged. Once a
        message is received, use the get_count() method to determine the
        actual size of the data received.
        """
        my_args = deref_array(args, [(['int', Ellipsis], 'int', 'int', 'int'), (['int', Ellipsis], 'int', 'int', 'int'), ('string', 'int', 'int', 'int'), ('tuple', 'int', 'int', 'int'), (['int', Ellipsis], 'int', 'int', 'int'), ('vtkDataObject', 'int', 'int'), ('vtkDataArray', 'int', 'int'), ('vtkMultiProcessStream', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.Receive, *my_args)
        return ret

    def receive_data_object(self, *args):
        """
        V.receive_data_object(int, int) -> DataObject
        C++: DataObject *ReceiveDataObject(int remoteId, int tag)"""
        ret = self._wrap_call(self._vtk_obj.ReceiveDataObject, *args)
        return wrap_vtk(ret)

    def reduce(self, *args):
        """
        V.reduce((int, ...), [int, ...], int, int, int) -> int
        C++: int Reduce(const int *sendBuffer, int *recvBuffer,
            IdType length, int operation, int destProcessId)
        V.reduce((int, ...), [int, ...], int, int, int) -> int
        C++: int Reduce(const long *sendBuffer, long *recvBuffer,
            IdType length, int operation, int destProcessId)
        V.reduce(string, string, int, int, int) -> int
        C++: int Reduce(const char *sendBuffer, char *recvBuffer,
            IdType length, int operation, int destProcessId)
        V.reduce((float, ...), [float, ...], int, int, int) -> int
        C++: int Reduce(const double *sendBuffer, double *recvBuffer,
            IdType length, int operation, int destProcessId)
        V.reduce((int, ...), [int, ...], int, int, int) -> int
        C++: int Reduce(const long long *sendBuffer,
            long long *recvBuffer, IdType length, int operation,
            int destProcessId)
        V.reduce(DataArray, DataArray, int, int) -> int
        C++: int Reduce(DataArray *sendBuffer,
            DataArray *recvBuffer, int operation, int destProcessId)
        Reduce an array to the given destination process.  This version
        of Reduce takes an identifier defined in the
        Communicator::StandardOperations enum to define the operation.
        """
        my_args = deref_array(args, [(('int', Ellipsis), ['int', Ellipsis], 'int', 'int', 'int'), (('int', Ellipsis), ['int', Ellipsis], 'int', 'int', 'int'), ('string', 'string', 'int', 'int', 'int'), (('float', Ellipsis), 'tuple', 'int', 'int', 'int'), (('int', Ellipsis), ['int', Ellipsis], 'int', 'int', 'int'), ('vtkDataArray', 'vtkDataArray', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.Reduce, *my_args)
        return ret

    def remove_all_rmi_callbacks(self, *args):
        """
        V.remove_all_rmi_callbacks(int)
        C++: virtual void RemoveAllRMICallbacks(int tag)
        These methods are a part of the newer API to add multiple rmi
        callbacks. When the RMI is triggered, all the callbacks are
        called Removes all callbacks for the tag.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveAllRMICallbacks, *args)
        return ret

    def remove_first_rmi(self, *args):
        """
        V.remove_first_rmi(int) -> int
        C++: virtual int RemoveFirstRMI(int tag)
        Remove the first RMI matching the tag.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveFirstRMI, *args)
        return ret

    def remove_rmi(self, *args):
        """
        V.remove_rmi(int) -> int
        C++: virtual int RemoveRMI(unsigned long id)
        Remove the  RMI matching the id. The id is the same id returned
        by add_rmi().
        """
        ret = self._wrap_call(self._vtk_obj.RemoveRMI, *args)
        return ret

    def remove_rmi_callback(self, *args):
        """
        V.remove_rmi_callback(int) -> bool
        C++: virtual bool RemoveRMICallback(unsigned long id)
        Remove a callback. Returns true is the remove was successful.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveRMICallback, *args)
        return ret

    def scatter(self, *args):
        """
        V.scatter((int, ...), [int, ...], int, int) -> int
        C++: int Scatter(const int *sendBuffer, int *recvBuffer,
            IdType length, int srcProcessId)
        V.scatter((int, ...), [int, ...], int, int) -> int
        C++: int Scatter(const long *sendBuffer, long *recvBuffer,
            IdType length, int srcProcessId)
        V.scatter(string, string, int, int) -> int
        C++: int Scatter(const char *sendBuffer, char *recvBuffer,
            IdType length, int srcProcessId)
        V.scatter((float, ...), [float, ...], int, int) -> int
        C++: int Scatter(const double *sendBuffer, double *recvBuffer,
            IdType length, int srcProcessId)
        V.scatter((int, ...), [int, ...], int, int) -> int
        C++: int Scatter(const long long *sendBuffer,
            long long *recvBuffer, IdType length, int srcProcessId)
        V.scatter(DataArray, DataArray, int) -> int
        C++: int Scatter(DataArray *sendBuffer,
            DataArray *recvBuffer, int srcProcessId)
        Scatter takes an array in the process with id src_process_id and
        distributes it.  Each process (including the source) receives a
        portion of the send buffer.  Process 0 receives the first length
        values, process 1 receives the second length values, and so on. 
        Scatter is the inverse operation of Gather.
        """
        my_args = deref_array(args, [(('int', Ellipsis), ['int', Ellipsis], 'int', 'int'), (('int', Ellipsis), ['int', Ellipsis], 'int', 'int'), ('string', 'string', 'int', 'int'), (('float', Ellipsis), 'tuple', 'int', 'int'), (('int', Ellipsis), ['int', Ellipsis], 'int', 'int'), ('vtkDataArray', 'vtkDataArray', 'int')])
        ret = self._wrap_call(self._vtk_obj.Scatter, *my_args)
        return ret

    def scatter_v(self, *args):
        """
        V.scatter_v((int, ...), [int, ...], [int, ...], [int, ...], int,
            int) -> int
        C++: int ScatterV(const int *sendBuffer, int *recvBuffer,
            IdType *sendLengths, IdType *offsets,
            IdType recvLength, int srcProcessId)
        V.scatter_v((int, ...), [int, ...], [int, ...], [int, ...], int,
            int) -> int
        C++: int ScatterV(const long *sendBuffer, long *recvBuffer,
            IdType *sendLengths, IdType *offsets,
            IdType recvLength, int srcProcessId)
        V.scatter_v(string, string, [int, ...], [int, ...], int, int)
            -> int
        C++: int ScatterV(const char *sendBuffer, char *recvBuffer,
            IdType *sendLengths, IdType *offsets,
            IdType recvLength, int srcProcessId)
        V.scatter_v((float, ...), [float, ...], [int, ...], [int, ...],
            int, int) -> int
        C++: int ScatterV(const double *sendBuffer, double *recvBuffer,
            IdType *sendLengths, IdType *offsets,
            IdType recvLength, int srcProcessId)
        V.scatter_v((int, ...), [int, ...], [int, ...], [int, ...], int,
            int) -> int
        C++: int ScatterV(const long long *sendBuffer,
            long long *recvBuffer, IdType *sendLengths,
            IdType *offsets, IdType recvLength, int srcProcessId)
        scatter_v is the vector variant of Scatter.  It extends the
        functionality of Scatter by allowing a varying count of data to
        each process. scatter_v takes an array in the process with id
        src_process_id and distributes it.  Each process (including the
        source) receives a portion of the send buffer defined by the
        send_lengths and offsets arrays.
        """
        ret = self._wrap_call(self._vtk_obj.ScatterV, *args)
        return ret

    def send(self, *args):
        """
        V.send((int, ...), int, int, int) -> int
        C++: int Send(const int *data, IdType length,
            int remoteProcessId, int tag)
        V.send((int, ...), int, int, int) -> int
        C++: int Send(const long *data, IdType length,
            int remoteProcessId, int tag)
        V.send(string, int, int, int) -> int
        C++: int Send(const char *data, IdType length,
            int remoteProcessId, int tag)
        V.send((float, ...), int, int, int) -> int
        C++: int Send(const double *data, IdType length,
            int remoteProcessId, int tag)
        V.send((int, ...), int, int, int) -> int
        C++: int Send(const long long *data, IdType length,
            int remoteProcessId, int tag)
        V.send(DataObject, int, int) -> int
        C++: int Send(DataObject *data, int remoteId, int tag)
        V.send(DataArray, int, int) -> int
        C++: int Send(DataArray *data, int remoteId, int tag)
        V.send(MultiProcessStream, int, int) -> int
        C++: int Send(const MultiProcessStream &stream, int remoteId,
            int tag)
        This method sends data to another process.  Tag eliminates
        ambiguity when multiple sends or receives exist in the same
        process. It is recommended to use custom tag number over 100.
        MultiProcessController has reserved tags between 1 and 4.
        Communicator has reserved tags between 10 and 16.
        """
        my_args = deref_array(args, [(('int', Ellipsis), 'int', 'int', 'int'), (('int', Ellipsis), 'int', 'int', 'int'), ('string', 'int', 'int', 'int'), ('tuple', 'int', 'int', 'int'), (('int', Ellipsis), 'int', 'int', 'int'), ('vtkDataObject', 'int', 'int'), ('vtkDataArray', 'int', 'int'), ('vtkMultiProcessStream', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.Send, *my_args)
        return ret

    def set_single_process_object(self, *args):
        """
        V.set_single_process_object(Process)
        C++: void SetSingleProcessObject(Process *p)
        Object-oriented flavor of set_single_method(). Instead of passing
        some function pointer and user data, a Process object is
        passed where the method to execute is Execute() and the data the
        object itself.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSingleProcessObject, *my_args)
        return ret

    def single_method_execute(self):
        """
        V.single_method_execute()
        C++: virtual void SingleMethodExecute()
        Execute the single_method (as define by set_single_method) using
        this->_number_of_processes processes.  This will only return when
        all the processes finish executing their methods.
        """
        ret = self._vtk_obj.SingleMethodExecute()
        return ret
        

    def trigger_break_rm_is(self):
        """
        V.trigger_break_rm_is()
        C++: void TriggerBreakRMIs()
        A conveniance method.  Called on process 0 to break "_process_rm_is"
        loop on all other processes.
        """
        ret = self._vtk_obj.TriggerBreakRMIs()
        return ret
        

    def trigger_rmi(self, *args):
        """
        V.trigger_rmi(int, void, int, int)
        C++: void TriggerRMI(int remoteProcessId, void *arg,
            int argLength, int tag)
        V.trigger_rmi(int, string, int)
        C++: void TriggerRMI(int remoteProcessId, const char *arg,
            int tag)
        V.trigger_rmi(int, int)
        C++: void TriggerRMI(int remoteProcessId, int tag)
        A method to trigger a method invocation in another process.
        """
        ret = self._wrap_call(self._vtk_obj.TriggerRMI, *args)
        return ret

    def trigger_rmi_on_all_children(self, *args):
        """
        V.trigger_rmi_on_all_children(void, int, int)
        C++: void TriggerRMIOnAllChildren(void *arg, int argLength,
            int tag)
        V.trigger_rmi_on_all_children(string, int)
        C++: void TriggerRMIOnAllChildren(const char *arg, int tag)
        V.trigger_rmi_on_all_children(int)
        C++: void TriggerRMIOnAllChildren(int tag)
        This is a convenicence method to trigger an RMI call on all the
        "children" of the current node. The children of the current node
        can be determined by drawing a binary tree starting at node 0 and
        then assigned nodes ids incrementally in a breadth-first fashion
        from left to right. This is designed to be used when trigger an
        RMI call on all satellites from the root node.
        """
        ret = self._wrap_call(self._vtk_obj.TriggerRMIOnAllChildren, *args)
        return ret

    _updateable_traits_ = \
    (('broadcast_trigger_rmi', 'GetBroadcastTriggerRMI'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('break_flag', 'GetBreakFlag'), ('number_of_processes',
    'GetNumberOfProcesses'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['broadcast_trigger_rmi', 'debug', 'global_warning_display',
    'break_flag', 'number_of_processes'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MultiProcessController, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MultiProcessController properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['broadcast_trigger_rmi'], [], ['break_flag',
            'number_of_processes']),
            title='Edit MultiProcessController properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MultiProcessController properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


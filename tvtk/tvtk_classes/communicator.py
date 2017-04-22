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


class Communicator(Object):
    """
    Communicator - Used to send/receive messages in a multiprocess
    environment.
    
    Superclass: Object
    
    This is an abstact class which contains functionality for sending and
    receiving inter-process messages. It contains methods for marshaling
    an object into a string (currently used by the MPI communicator but
    not the shared memory communicator).
    
    @warning
    Communication between systems with different IdTypes is not
    supported. All machines have to have the same IdType.
    
    @sa
    MPICommunicator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCommunicator, obj, update, **traits)
    
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

    def get_left_child_processor(self, *args):
        """
        V.get_left_child_processor(int) -> int
        C++: static int GetLeftChildProcessor(int pid)
        Some helper functions when dealing with heap tree - based
        algorthims - we don't need a function for getting the right
        processor since it is 1 + the_left_processor
        """
        ret = self._wrap_call(self._vtk_obj.GetLeftChildProcessor, *args)
        return ret

    def _get_local_process_id(self):
        return self._vtk_obj.GetLocalProcessId()
    local_process_id = traits.Property(_get_local_process_id, help=\
        """
        Tells you which process [0, num_process) you are in.
        """
    )

    def get_parent_processor(self, *args):
        """
        V.get_parent_processor(int) -> int
        C++: static int GetParentProcessor(int pid)
        Some helper functions when dealing with heap tree - based
        algorthims - we don't need a function for getting the right
        processor since it is 1 + the_left_processor
        """
        ret = self._wrap_call(self._vtk_obj.GetParentProcessor, *args)
        return ret

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

    def all_gather_v_void_array(self, *args):
        """
        V.all_gather_v_void_array(void, void, int, [int, ...], [int, ...],
            int) -> int
        C++: virtual int AllGatherVVoidArray(const void *sendBuffer,
            void *recvBuffer, IdType sendLength,
            IdType *recvLengths, IdType *offsets, int type)
        Subclasses should reimplement these if they have a more efficient
        implementation.
        """
        ret = self._wrap_call(self._vtk_obj.AllGatherVVoidArray, *args)
        return ret

    def all_gather_void_array(self, *args):
        """
        V.all_gather_void_array(void, void, int, int) -> int
        C++: virtual int AllGatherVoidArray(const void *sendBuffer,
            void *recvBuffer, IdType length, int type)
        Subclasses should reimplement these if they have a more efficient
        implementation.
        """
        ret = self._wrap_call(self._vtk_obj.AllGatherVoidArray, *args)
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

    def all_reduce_void_array(self, *args):
        """
        V.all_reduce_void_array(void, void, int, int, int) -> int
        C++: virtual int AllReduceVoidArray(const void *sendBuffer,
            void *recvBuffer, IdType length, int type, int operation)
        Subclasses should reimplement these if they have a more efficient
        implementation.
        """
        ret = self._wrap_call(self._vtk_obj.AllReduceVoidArray, *args)
        return ret

    def barrier(self):
        """
        V.barrier()
        C++: virtual void Barrier()
        Will block the processes until all other processes reach the
        Barrier function.
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

    def broadcast_void_array(self, *args):
        """
        V.broadcast_void_array(void, int, int, int) -> int
        C++: virtual int BroadcastVoidArray(void *data, IdType length,
            int type, int srcProcessId)
        Subclasses should reimplement these if they have a more efficient
        implementation.
        """
        ret = self._wrap_call(self._vtk_obj.BroadcastVoidArray, *args)
        return ret

    def compute_global_bounds(self, *args):
        """
        V.compute_global_bounds(int, int, BoundingBox, [int, ...], [int,
            ...], int, int, int) -> int
        C++: virtual int ComputeGlobalBounds(int processorId,
            int numProcesses, BoundingBox *bounds,
            int *rightHasBounds=0, int *leftHasBounds=0,
            int hasBoundsTag=288402, int localBoundsTag=288403,
            int globalBoundsTag=288404)
        Determine the global bounds for a set of processes.  BBox is
        initially set (outside of the call to the local bounds of the
        process and will be modified to be the global bounds - this
        default implementation views the processors as a heap tree with
        the root being process_id = 0 If either right_has_bounds or
        left_has_bounds is not 0 then the corresponding int will be set to
        1 if the right/left processor has bounds else it will be set to 0
        The last three arguments are the tags to be used when performing
        the operation
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeGlobalBounds, *my_args)
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

    def gather_v_void_array(self, *args):
        """
        V.gather_v_void_array(void, void, int, [int, ...], [int, ...], int,
            int) -> int
        C++: virtual int GatherVVoidArray(const void *sendBuffer,
            void *recvBuffer, IdType sendLength,
            IdType *recvLengths, IdType *offsets, int type,
            int destProcessId)
        Subclasses should reimplement these if they have a more efficient
        implementation.
        """
        ret = self._wrap_call(self._vtk_obj.GatherVVoidArray, *args)
        return ret

    def gather_void_array(self, *args):
        """
        V.gather_void_array(void, void, int, int, int) -> int
        C++: virtual int GatherVoidArray(const void *sendBuffer,
            void *recvBuffer, IdType length, int type,
            int destProcessId)
        Subclasses should reimplement these if they have a more efficient
        implementation.
        """
        ret = self._wrap_call(self._vtk_obj.GatherVoidArray, *args)
        return ret

    def marshal_data_object(self, *args):
        """
        V.marshal_data_object(DataObject, CharArray) -> int
        C++: static int MarshalDataObject(DataObject *object,
            CharArray *buffer)
        Convert a data object into a string that can be transmitted and
        vice versa. Returns 1 for success and 0 for failure. WARNING:
        This will only work for types that have a DataWriter class.
        """
        my_args = deref_array(args, [('vtkDataObject', 'vtkCharArray')])
        ret = self._wrap_call(self._vtk_obj.MarshalDataObject, *my_args)
        return ret

    def receive(self, *args):
        """
        V.receive(DataObject, int, int) -> int
        C++: int Receive(DataObject *data, int remoteHandle, int tag)
        V.receive(DataArray, int, int) -> int
        C++: int Receive(DataArray *data, int remoteHandle, int tag)
        V.receive([int, ...], int, int, int) -> int
        C++: int Receive(int *data, IdType maxlength, int remoteHandle,
             int tag)
        V.receive([int, ...], int, int, int) -> int
        C++: int Receive(long *data, IdType maxlength,
            int remoteHandle, int tag)
        V.receive(string, int, int, int) -> int
        C++: int Receive(char *data, IdType maxlength,
            int remoteHandle, int tag)
        V.receive([float, ...], int, int, int) -> int
        C++: int Receive(double *data, IdType maxlength,
            int remoteHandle, int tag)
        V.receive([int, ...], int, int, int) -> int
        C++: int Receive(long long *data, IdType maxlength,
            int remoteHandle, int tag)
        V.receive(MultiProcessStream, int, int) -> int
        C++: int Receive(MultiProcessStream &stream, int remoteId,
            int tag)
        This method receives a data object from a corresponding send. It
        blocks until the receive is finished.
        """
        my_args = deref_array(args, [('vtkDataObject', 'int', 'int'), ('vtkDataArray', 'int', 'int'), (['int', Ellipsis], 'int', 'int', 'int'), (['int', Ellipsis], 'int', 'int', 'int'), ('string', 'int', 'int', 'int'), ('tuple', 'int', 'int', 'int'), (['int', Ellipsis], 'int', 'int', 'int'), ('vtkMultiProcessStream', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.Receive, *my_args)
        return ret

    def receive_data_object(self, *args):
        """
        V.receive_data_object(int, int) -> DataObject
        C++: DataObject *ReceiveDataObject(int remoteHandle, int tag)
        The caller does not have to know the data type before this call
        is made. It returns the newly created object.
        """
        ret = self._wrap_call(self._vtk_obj.ReceiveDataObject, *args)
        return wrap_vtk(ret)

    def receive_void_array(self, *args):
        """
        V.receive_void_array(void, int, int, int, int) -> int
        C++: virtual int ReceiveVoidArray(void *data, IdType maxlength,
             int type, int remoteHandle, int tag)
        Subclasses have to supply this method to receive various arrays
        of data. The type arg is one of the VTK type constants recognized
        by the TemplateMacro (VTK_FLOAT, VTK_INT, etc.).  maxlength is
        measured in number of values (as opposed to number of bytes) and
        is the maxmum length of the data to receive.  If the maxlength is
        less than the length of the message sent by the sender, an error
        will be flagged. Once a message is received, use the get_count()
        method to determine the actual size of the data received.
        """
        ret = self._wrap_call(self._vtk_obj.ReceiveVoidArray, *args)
        return ret

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

    def reduce_void_array(self, *args):
        """
        V.reduce_void_array(void, void, int, int, int, int) -> int
        C++: virtual int ReduceVoidArray(const void *sendBuffer,
            void *recvBuffer, IdType length, int type, int operation,
            int destProcessId)
        Subclasses should reimplement these if they have a more efficient
        implementation.
        """
        ret = self._wrap_call(self._vtk_obj.ReduceVoidArray, *args)
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

    def scatter_v_void_array(self, *args):
        """
        V.scatter_v_void_array(void, void, [int, ...], [int, ...], int, int,
            int) -> int
        C++: virtual int ScatterVVoidArray(const void *sendBuffer,
            void *recvBuffer, IdType *sendLengths, IdType *offsets,
            IdType recvLength, int type, int srcProcessId)
        Subclasses should reimplement these if they have a more efficient
        implementation.
        """
        ret = self._wrap_call(self._vtk_obj.ScatterVVoidArray, *args)
        return ret

    def scatter_void_array(self, *args):
        """
        V.scatter_void_array(void, void, int, int, int) -> int
        C++: virtual int ScatterVoidArray(const void *sendBuffer,
            void *recvBuffer, IdType length, int type,
            int srcProcessId)
        Subclasses should reimplement these if they have a more efficient
        implementation.
        """
        ret = self._wrap_call(self._vtk_obj.ScatterVoidArray, *args)
        return ret

    def send(self, *args):
        """
        V.send(DataObject, int, int) -> int
        C++: int Send(DataObject *data, int remoteHandle, int tag)
        V.send(DataArray, int, int) -> int
        C++: int Send(DataArray *data, int remoteHandle, int tag)
        V.send((int, ...), int, int, int) -> int
        C++: int Send(const int *data, IdType length, int remoteHandle,
             int tag)
        V.send((int, ...), int, int, int) -> int
        C++: int Send(const long *data, IdType length,
            int remoteHandle, int tag)
        V.send(string, int, int, int) -> int
        C++: int Send(const char *data, IdType length,
            int remoteHandle, int tag)
        V.send((float, ...), int, int, int) -> int
        C++: int Send(const double *data, IdType length,
            int remoteHandle, int tag)
        V.send((int, ...), int, int, int) -> int
        C++: int Send(const long long *data, IdType length,
            int remoteHandle, int tag)
        V.send(MultiProcessStream, int, int) -> int
        C++: int Send(const MultiProcessStream &stream, int remoteId,
            int tag)
        This method sends a data object to a destination. Tag eliminates
        ambiguity and is used to match sends to receives.
        """
        my_args = deref_array(args, [('vtkDataObject', 'int', 'int'), ('vtkDataArray', 'int', 'int'), (('int', Ellipsis), 'int', 'int', 'int'), (('int', Ellipsis), 'int', 'int', 'int'), ('string', 'int', 'int', 'int'), ('tuple', 'int', 'int', 'int'), (('int', Ellipsis), 'int', 'int', 'int'), ('vtkMultiProcessStream', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.Send, *my_args)
        return ret

    def send_void_array(self, *args):
        """
        V.send_void_array(void, int, int, int, int) -> int
        C++: virtual int SendVoidArray(const void *data, IdType length,
             int type, int remoteHandle, int tag)
        Subclasses have to supply this method to send various arrays of
        data. The type arg is one of the VTK type constants recognized by
        the TemplateMacro (VTK_FLOAT, VTK_INT, etc.).  length is
        measured in number of values (as opposed to number of bytes).
        """
        ret = self._wrap_call(self._vtk_obj.SendVoidArray, *args)
        return ret

    def set_use_copy(self, *args):
        """
        V.set_use_copy(int)
        C++: static void SetUseCopy(int useCopy)"""
        ret = self._wrap_call(self._vtk_obj.SetUseCopy, *args)
        return ret

    def un_marshal_data_object(self, *args):
        """
        V.un_marshal_data_object(CharArray, DataObject) -> int
        C++: static int UnMarshalDataObject(CharArray *buffer,
            DataObject *object)
        Convert a data object into a string that can be transmitted and
        vice versa. Returns 1 for success and 0 for failure. WARNING:
        This will only work for types that have a DataWriter class.
        """
        my_args = deref_array(args, [('vtkCharArray', 'vtkDataObject')])
        ret = self._wrap_call(self._vtk_obj.UnMarshalDataObject, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_processes',
    'GetNumberOfProcesses'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'number_of_processes'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Communicator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Communicator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['number_of_processes']),
            title='Edit Communicator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Communicator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.communicator import Communicator


class SocketCommunicator(Communicator):
    """
    SocketCommunicator - Process communication using Sockets
    
    Superclass: Communicator
    
    This is a concrete implementation of Communicator which supports
    interprocess communication using BSD style sockets. It supports byte
    swapping for the communication of  machines with different
    endianness.
    
    @warning
    Communication between 32 bit and 64 bit systems is not fully
    supported. If a type does not have the same length on both systems,
    this communicator can not be used to transfer data of that type.
    
    @sa
    Communicator SocketController
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSocketCommunicator, obj, update, **traits)
    
    perform_handshake = tvtk_base.true_bool_trait(help=\
        """
        Set or get the perform_handshake ivar. If it is on, the
        communicator will try to perform a handshake when connected. It
        is on by default.
        """
    )

    def _perform_handshake_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPerformHandshake,
                        self.perform_handshake_)

    number_of_processes = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set the number of processes you will be using.
        """
    )

    def _number_of_processes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfProcesses,
                        self.number_of_processes)

    report_errors = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        If report_errors if false, all ErrorMacros are suppressed.
        """
    )

    def _report_errors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReportErrors,
                        self.report_errors)

    def _get_socket(self):
        return wrap_vtk(self._vtk_obj.GetSocket())
    def _set_socket(self, arg):
        old_val = self._get_socket()
        self._wrap_call(self._vtk_obj.SetSocket,
                        deref_vtk(arg))
        self.trait_property_changed('socket', old_val, arg)
    socket = traits.Property(_get_socket, _set_socket, help=\
        """
        Get/Set the actual socket used for communication.
        """
    )

    def _get_is_connected(self):
        return self._vtk_obj.GetIsConnected()
    is_connected = traits.Property(_get_is_connected, help=\
        """
        Is the communicator connected?.
        """
    )

    def _get_is_server(self):
        return self._vtk_obj.GetIsServer()
    is_server = traits.Property(_get_is_server, help=\
        """
        Returns true if this side of the socket is the server.  The
        result is invalid if the socket is not connected.
        """
    )

    def _get_perform_handshake_max_value(self):
        return self._vtk_obj.GetPerformHandshakeMaxValue()
    perform_handshake_max_value = traits.Property(_get_perform_handshake_max_value, help=\
        """
        Set or get the perform_handshake ivar. If it is on, the
        communicator will try to perform a handshake when connected. It
        is on by default.
        """
    )

    def _get_perform_handshake_min_value(self):
        return self._vtk_obj.GetPerformHandshakeMinValue()
    perform_handshake_min_value = traits.Property(_get_perform_handshake_min_value, help=\
        """
        Set or get the perform_handshake ivar. If it is on, the
        communicator will try to perform a handshake when connected. It
        is on by default.
        """
    )

    def _get_swap_bytes_in_received_data(self):
        return self._vtk_obj.GetSwapBytesInReceivedData()
    swap_bytes_in_received_data = traits.Property(_get_swap_bytes_in_received_data, help=\
        """
        Returns 1 if bytes must be swapped in received ints, floats, etc
        """
    )

    def _get_version(self):
        return self._vtk_obj.GetVersion()
    version = traits.Property(_get_version, help=\
        """
        Uniquely identifies the version of this class.  If the versions
        match, then the socket communicators should be compatible.
        """
    )

    def buffer_current_message(self):
        """
        V.buffer_current_message()
        C++: void BufferCurrentMessage()
        This flag is cleared before Command::WrongTagEvent is fired
        when ever a message with mismatched tag is received. If the
        handler wants the message to be buffered for later use, it should
        set this flag to true. In which case the SocketCommunicator
        will  buffer the messsage and it will be automatically processed
        the next time one does a receive_tagged() with a matching tag.
        """
        ret = self._vtk_obj.BufferCurrentMessage()
        return ret
        

    def client_side_handshake(self):
        """
        V.client_side_handshake() -> int
        C++: int ClientSideHandshake()
        Performs client_side handshake. One should preferably use
        Handshake() which calls server_side_handshake or
        client_side_handshake as required.
        """
        ret = self._vtk_obj.ClientSideHandshake()
        return ret
        

    def close_connection(self):
        """
        V.close_connection()
        C++: virtual void CloseConnection()
        Close a connection.
        """
        ret = self._vtk_obj.CloseConnection()
        return ret
        

    def connect_to(self, *args):
        """
        V.connect_to(string, int) -> int
        C++: virtual int ConnectTo(const char *hostName, int port)
        Open a connection to host.
        """
        ret = self._wrap_call(self._vtk_obj.ConnectTo, *args)
        return ret

    def handshake(self):
        """
        V.handshake() -> int
        C++: int Handshake()
        Performs handshake. This uses ClientSocket::ConnectingSide to
        decide whether to perform server_side_handshake or
        client_side_handshake.
        """
        ret = self._vtk_obj.Handshake()
        return ret
        

    def has_bufferred_messages(self):
        """
        V.has_bufferred_messages() -> bool
        C++: bool HasBufferredMessages()
        Returns true if there are any messages in the receive buffer.
        """
        ret = self._vtk_obj.HasBufferredMessages()
        return ret
        

    def log_to_file(self, *args):
        """
        V.log_to_file(string) -> int
        C++: virtual int LogToFile(const char *name)
        V.log_to_file(string, int) -> int
        C++: virtual int LogToFile(const char *name, int append)
        Log messages to the given file.  The file is truncated unless the
        second argument is non-zero (default is to truncate).  If the
        file name is empty or NULL, logging is disabled.  Returns 0 if
        the file failed to open, and 1 otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.LogToFile, *args)
        return ret

    def server_side_handshake(self):
        """
        V.server_side_handshake() -> int
        C++: int ServerSideHandshake()
        Performs server_side handshake. One should preferably use
        Handshake() which calls server_side_handshake or
        client_side_handshake as required.
        """
        ret = self._vtk_obj.ServerSideHandshake()
        return ret
        

    def wait_for_connection(self, *args):
        """
        V.wait_for_connection(int) -> int
        C++: virtual int WaitForConnection(int port)
        V.wait_for_connection(ServerSocket, int) -> int
        C++: virtual int WaitForConnection(ServerSocket *socket,
            unsigned long msec=0)
        Wait for connection on a given port. These methods return 1 on
        success, 0 on error.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.WaitForConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('perform_handshake', 'GetPerformHandshake'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_processes', 'GetNumberOfProcesses'), ('report_errors',
    'GetReportErrors'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'perform_handshake',
    'number_of_processes', 'report_errors'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SocketCommunicator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SocketCommunicator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['perform_handshake'], [], ['number_of_processes',
            'report_errors']),
            title='Edit SocketCommunicator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SocketCommunicator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


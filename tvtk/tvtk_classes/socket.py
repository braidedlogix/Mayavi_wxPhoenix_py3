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


class Socket(Object):
    """
    Socket - BSD socket encapsulation.
    
    Superclass: Object
    
    This abstract class encapsulates a BSD socket. It provides an API for
    basic socket operations.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSocket, obj, update, **traits)
    
    def _get_connected(self):
        return self._vtk_obj.GetConnected()
    connected = traits.Property(_get_connected, help=\
        """
        Check is the socket is alive.
        """
    )

    def _get_socket_descriptor(self):
        return self._vtk_obj.GetSocketDescriptor()
    socket_descriptor = traits.Property(_get_socket_descriptor, help=\
        """
        Provides access to  the internal socket descriptor. This is valid
        only when get_connected() returns true.
        """
    )

    def close_socket(self):
        """
        V.close_socket()
        C++: void CloseSocket()
        Close the socket.
        """
        ret = self._vtk_obj.CloseSocket()
        return ret
        

    def receive(self, *args):
        """
        V.receive(void, int, int) -> int
        C++: int Receive(void *data, int length, int readFully=1)
        Receive data from the socket. This call blocks until some data is
        read from the socket. When read_fully is set, this call will block
        until all the requested data is read from the socket. 0 on error,
        else number of bytes read is returned. On error,
        Command::ErrorEvent is raised.
        """
        ret = self._wrap_call(self._vtk_obj.Receive, *args)
        return ret

    def select_sockets(self, *args):
        """
        V.select_sockets((int, ...), int, int, [int, ...]) -> int
        C++: static int SelectSockets(const int *sockets_to_select,
            int size, unsigned long msec, int *selected_index)
        Selects set of sockets. Returns 0 on timeout, -1 on error. 1 on
        success. Selected socket's index is returned thru selected_index
        """
        ret = self._wrap_call(self._vtk_obj.SelectSockets, *args)
        return ret

    def send(self, *args):
        """
        V.send(void, int) -> int
        C++: int Send(const void *data, int length)
        These methods send data over the socket. Returns 1 on success, 0
        on error and raises Command::ErrorEvent.
        """
        ret = self._wrap_call(self._vtk_obj.Send, *args)
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
            return super(Socket, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Socket properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit Socket properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Socket properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


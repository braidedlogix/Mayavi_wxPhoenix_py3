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

from tvtk.tvtk_classes.multi_process_controller import MultiProcessController


class SocketController(MultiProcessController):
    """
    SocketController - Process communication using Sockets
    
    Superclass: MultiProcessController
    
    This is a concrete implementation of MultiProcessController. It
    supports one-to-one communication using sockets. Note that process 0
    will always correspond to self and process 1 to the remote process.
    This class is best used with ports.
    
    @bug Note that because process 0 will always correspond to self, this
    class breaks assumptions usually implied when using ad-hoc
    polymorphism.  That is, the SocketController will behave
    differently than other subclasses of MultiProcessController.  If
    you upcast SocketController to MultiProcessController and send
    it to a method that does not know that the object is actually a
    SocketController, the object may not behave as intended.  For
    example, if that oblivious class chose to identify a "root" based on
    the local process id, then both sides of the controller will think
    they are the root (and that will probably lead to deadlock).  If you
    plan to upcast to MultiProcessController, you should probably use
    the create_compliant_controller instead.
    
    @sa
    MultiProcessController SocketCommunicator InputPort
    OutputPort
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSocketController, obj, update, **traits)
    
    def _get_communicator(self):
        return wrap_vtk(self._vtk_obj.GetCommunicator())
    def _set_communicator(self, arg):
        old_val = self._get_communicator()
        self._wrap_call(self._vtk_obj.SetCommunicator,
                        deref_vtk(arg))
        self.trait_property_changed('communicator', old_val, arg)
    communicator = traits.Property(_get_communicator, _set_communicator, help=\
        """
        Returns the communicator associated with this controller. A
        default communicator is created in constructor.
        """
    )

    def _get_swap_bytes_in_received_data(self):
        return self._vtk_obj.GetSwapBytesInReceivedData()
    swap_bytes_in_received_data = traits.Property(_get_swap_bytes_in_received_data, help=\
        """
        
        """
    )

    def close_connection(self):
        """
        V.close_connection()
        C++: virtual void CloseConnection()
        Close a connection, forwarded to the communicator
        """
        ret = self._vtk_obj.CloseConnection()
        return ret
        

    def connect_to(self, *args):
        """
        V.connect_to(string, int) -> int
        C++: virtual int ConnectTo(const char *hostName, int port)
        Open a connection to a give machine, forwarded to the
        communicator
        """
        ret = self._wrap_call(self._vtk_obj.ConnectTo, *args)
        return ret

    def create_compliant_controller(self):
        """
        V.create_compliant_controller() -> MultiProcessController
        C++: MultiProcessController *CreateCompliantController()
        FOOLISH MORTALS!  Thou hast forsaken the sacred laws of ad-hoc
        polymorphism when thou broke a critical assumption of the
        superclass (namely, each process has thine own id).  The time
        frame to fix thy error has passed. Too much code has come to rely
        on this abhorrent behavior.  Instead, we offer this gift: a
        method for creating an equivalent communicator with correct
        process id semantics.  The calling code is responsible for
        deleting this controller.
        """
        ret = wrap_vtk(self._vtk_obj.CreateCompliantController())
        return ret
        

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()"""
        ret = self._vtk_obj.Initialize()
        return ret
        

    def wait_for_connection(self, *args):
        """
        V.wait_for_connection(int) -> int
        C++: virtual int WaitForConnection(int port)
        Wait for connection on a given port, forwarded to the
        communicator
        """
        ret = self._wrap_call(self._vtk_obj.WaitForConnection, *args)
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
            return super(SocketController, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SocketController properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['broadcast_trigger_rmi'], [], ['break_flag',
            'number_of_processes']),
            title='Edit SocketController properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SocketController properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


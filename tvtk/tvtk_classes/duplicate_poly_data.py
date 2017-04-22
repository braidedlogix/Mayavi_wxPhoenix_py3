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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class DuplicatePolyData(PolyDataAlgorithm):
    """
    DuplicatePolyData - For distributed tiled displays.
    
    Superclass: PolyDataAlgorithm
    
    This filter collects poly data and duplicates it on every node.
    Converts data parallel so every node has a complete copy of the data.
    The filter is used at the end of a pipeline for driving a tiled
    display.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDuplicatePolyData, obj, update, **traits)
    
    synchronous = tvtk_base.true_bool_trait(help=\
        """
        This flag causes sends and receives to be matched. When this flag
        is off, two sends occur then two receives. I want to see if it
        makes a difference in performance. The flag is on by default.
        """
    )

    def _synchronous_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSynchronous,
                        self.synchronous_)

    client_flag = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This duplicate filter works in client server mode when this
        controller is set.  We have a client flag to diferentiate the
        client and server because the socket controller is odd: Proth
        processes think their id is 0.
        """
    )

    def _client_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClientFlag,
                        self.client_flag)

    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        By defualt this filter uses the global controller, but this
        method can be used to set another instead.
        """
    )

    def _get_socket_controller(self):
        return wrap_vtk(self._vtk_obj.GetSocketController())
    def _set_socket_controller(self, arg):
        old_val = self._get_socket_controller()
        self._wrap_call(self._vtk_obj.SetSocketController,
                        deref_vtk(arg))
        self.trait_property_changed('socket_controller', old_val, arg)
    socket_controller = traits.Property(_get_socket_controller, _set_socket_controller, help=\
        """
        This duplicate filter works in client server mode when this
        controller is set.  We have a client flag to diferentiate the
        client and server because the socket controller is odd: Proth
        processes think their id is 0.
        """
    )

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_memory_size(self):
        return self._vtk_obj.GetMemorySize()
    memory_size = traits.Property(_get_memory_size, help=\
        """
        This returns to size of the output (on this process). This method
        is not really used.  It is needed to have the same API as
        CollectPolyData.
        """
    )

    def initialize_schedule(self, *args):
        """
        V.initialize_schedule(int)
        C++: void InitializeSchedule(int numProcs)"""
        ret = self._wrap_call(self._vtk_obj.InitializeSchedule, *args)
        return ret

    _updateable_traits_ = \
    (('synchronous', 'GetSynchronous'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('client_flag', 'GetClientFlag'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'synchronous', 'client_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DuplicatePolyData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DuplicatePolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['synchronous'], [], ['client_flag']),
            title='Edit DuplicatePolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DuplicatePolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


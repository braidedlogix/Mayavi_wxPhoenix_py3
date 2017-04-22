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


class DummyController(MultiProcessController):
    """
    DummyController - Dummy controller for single process applications
    
    Superclass: MultiProcessController
    
    This is a dummy controller which can be used by applications which
    always require a controller but are also compile on systems without
    threads or mpi.
    @sa
    MultiProcessController
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDummyController, obj, update, **traits)
    
    def _get_communicator(self):
        return wrap_vtk(self._vtk_obj.GetCommunicator())
    def _set_communicator(self, arg):
        old_val = self._get_communicator()
        self._wrap_call(self._vtk_obj.SetCommunicator,
                        deref_vtk(arg))
        self.trait_property_changed('communicator', old_val, arg)
    communicator = traits.Property(_get_communicator, _set_communicator, help=\
        """
        If you don't need any special functionality from the controller,
        you can swap out the dummy communicator for another one.
        """
    )

    def _get_rmi_communicator(self):
        return wrap_vtk(self._vtk_obj.GetRMICommunicator())
    def _set_rmi_communicator(self, arg):
        old_val = self._get_rmi_communicator()
        self._wrap_call(self._vtk_obj.SetRMICommunicator,
                        deref_vtk(arg))
        self.trait_property_changed('rmi_communicator', old_val, arg)
    rmi_communicator = traits.Property(_get_rmi_communicator, _set_rmi_communicator, help=\
        """
        If you don't need any special functionality from the controller,
        you can swap out the dummy communicator for another one.
        """
    )

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
            return super(DummyController, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DummyController properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['broadcast_trigger_rmi'], [], ['break_flag',
            'number_of_processes']),
            title='Edit DummyController properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DummyController properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


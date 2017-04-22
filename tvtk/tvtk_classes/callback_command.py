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

from tvtk.tvtk_classes.command import Command


class CallbackCommand(Command):
    """
    CallbackCommand - supports function callbacks
    
    Superclass: Command
    
    Use CallbackCommand for generic function callbacks. That is, this
    class can be used when you wish to execute a function (of the
    signature described below) using the Command/Observer design pattern
    in VTK. The callback function should have the form
    
    void func(vtk_object*, unsigned long eid, void* clientdata, void
    *calldata)  where the parameter Object* is the object invoking the
    event; eid is the event id (see Command.h); clientdata is special
    data that should is associated with this instance of
    CallbackCommand; and calldata is data that the
    Object::InvokeEvent() may send with the callback. For example, the
    invocation of the progress_event sends along the progress value as
    calldata.
    
    @sa
    Command OldStyleCallbackCommand
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCallbackCommand, obj, update, **traits)
    
    abort_flag_on_execute = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the abort flag on execute. If this is set to true the
        abort_flag will be set to On automatically when the Execute method
        is triggered *and* a callback is set.
        """
    )

    def _abort_flag_on_execute_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAbortFlagOnExecute,
                        self.abort_flag_on_execute_)

    def _get_client_data(self):
        return self._vtk_obj.GetClientData()
    def _set_client_data(self, arg):
        old_val = self._get_client_data()
        self._wrap_call(self._vtk_obj.SetClientData,
                        arg)
        self.trait_property_changed('client_data', old_val, arg)
    client_data = traits.Property(_get_client_data, _set_client_data, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('abort_flag_on_execute', 'GetAbortFlagOnExecute'), ('abort_flag',
    'GetAbortFlag'), ('passive_observer', 'GetPassiveObserver'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_flag', 'abort_flag_on_execute', 'passive_observer'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CallbackCommand, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CallbackCommand properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['abort_flag', 'abort_flag_on_execute', 'passive_observer'], [],
            []),
            title='Edit CallbackCommand properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CallbackCommand properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class ExecutionTimer(Object):
    """
    ExecutionTimer - Time filter execution
    
    Superclass: Object
    
    This object monitors a single filter for start_event and end_event.
    Each time it hears start_event it records the time.  Each time it
    hears end_event it measures the elapsed time (both CPU and wall-clock)
    since the most recent start_event.  Internally we use TimerLog for
    measurements.
    
    By default we simply store the elapsed time.  You are welcome to
    subclass and override timer_finished() to do anything you want.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExecutionTimer, obj, update, **traits)
    
    def _get_filter(self):
        return wrap_vtk(self._vtk_obj.GetFilter())
    def _set_filter(self, arg):
        old_val = self._get_filter()
        self._wrap_call(self._vtk_obj.SetFilter,
                        deref_vtk(arg))
        self.trait_property_changed('filter', old_val, arg)
    filter = traits.Property(_get_filter, _set_filter, help=\
        """
        Set/get the filter to be monitored.  The only real constraint
        here is that the Executive associated with the filter must
        fire start_event and end_event before and after the filter is
        executed.  All VTK executives should do this.
        """
    )

    def _get_elapsed_cpu_time(self):
        return self._vtk_obj.GetElapsedCPUTime()
    elapsed_cpu_time = traits.Property(_get_elapsed_cpu_time, help=\
        """
        Get the total CPU time (in seconds) that elapsed between
        start_event and end_event.  This is undefined before the filter has
        finished executing.
        """
    )

    def _get_elapsed_wall_clock_time(self):
        return self._vtk_obj.GetElapsedWallClockTime()
    elapsed_wall_clock_time = traits.Property(_get_elapsed_wall_clock_time, help=\
        """
        Get the total wall clock time (in seconds) that elapsed between
        start_event and end_event.  This is undefined before the filter has
        finished executing.
        """
    )

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExecutionTimer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExecutionTimer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ExecutionTimer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExecutionTimer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


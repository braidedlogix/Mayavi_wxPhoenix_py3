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

from tvtk.tvtk_classes.streamer import Streamer


class StreamPoints(Streamer):
    """
    StreamPoints - generate points along streamer separated by
    constant time increment
    
    Superclass: Streamer
    
    StreamPoints is a filter that generates points along a streamer.
    The points are separated by a constant time increment. The resulting
    visual effect (especially when coupled with Glyph3D) is an
    indication of particle speed.
    
    @sa
    Streamer StreamLine DashedStreamLine
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStreamPoints, obj, update, **traits)
    
    time_increment = traits.Trait(1.0, traits.Range(1e-06, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Specify the separation of points in terms of absolute time.
        """
    )

    def _time_increment_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeIncrement,
                        self.time_increment)

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

    _updateable_traits_ = \
    (('orientation_scalars', 'GetOrientationScalars'), ('speed_scalars',
    'GetSpeedScalars'), ('vorticity', 'GetVorticity'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('integration_direction',
    'GetIntegrationDirection'), ('time_increment', 'GetTimeIncrement'),
    ('epsilon', 'GetEpsilon'), ('integration_step_length',
    'GetIntegrationStepLength'), ('maximum_propagation_time',
    'GetMaximumPropagationTime'), ('number_of_threads',
    'GetNumberOfThreads'), ('save_point_interval',
    'GetSavePointInterval'), ('start_position', 'GetStartPosition'),
    ('terminal_speed', 'GetTerminalSpeed'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'orientation_scalars', 'release_data_flag', 'speed_scalars',
    'vorticity', 'integration_direction', 'epsilon',
    'integration_step_length', 'maximum_propagation_time',
    'number_of_threads', 'progress_text', 'save_point_interval',
    'start_position', 'terminal_speed', 'time_increment'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StreamPoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StreamPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['orientation_scalars', 'speed_scalars', 'vorticity'],
            ['integration_direction'], ['epsilon', 'integration_step_length',
            'maximum_propagation_time', 'number_of_threads',
            'save_point_interval', 'start_position', 'terminal_speed',
            'time_increment']),
            title='Edit StreamPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StreamPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.stream_line import StreamLine


class DashedStreamLine(StreamLine):
    """
    DashedStreamLine - generate constant-time dashed streamline in
    arbitrary dataset
    
    Superclass: StreamLine
    
    DashedStreamLine is a filter that generates a "dashed" streamline
    for an arbitrary dataset. The streamline consists of a series of
    dashes, each of which represents (approximately) a constant time
    increment. Thus, in the resulting visual representation, relatively
    long dashes represent areas of high velocity, and small dashes
    represent areas of low velocity.
    
    DashedStreamLine introduces the instance variable dash_factor.
    dash_factor interacts with its superclass' instance variable
    step_length to create the dashes. dash_factor is the percentage of the
    step_length line segment that is visible. Thus, if the
    dash_factor=_0._75, the dashes will be "three-quarters on" and "one-quarter
    off".
    
    @sa
    Streamer StreamLine StreamPoints
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDashedStreamLine, obj, update, **traits)
    
    dash_factor = traits.Trait(0.75, traits.Range(0.01, 1.0, enter_set=True, auto_set=False), help=\
        """
        For each dash, specify the fraction of the dash that is "on". A
        factor of 1.0 will result in a continuous line, a factor of 0.5
        will result in dashed that are half on and half off.
        """
    )

    def _dash_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDashFactor,
                        self.dash_factor)

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
    'GetIntegrationDirection'), ('dash_factor', 'GetDashFactor'),
    ('step_length', 'GetStepLength'), ('epsilon', 'GetEpsilon'),
    ('integration_step_length', 'GetIntegrationStepLength'),
    ('maximum_propagation_time', 'GetMaximumPropagationTime'),
    ('number_of_threads', 'GetNumberOfThreads'), ('save_point_interval',
    'GetSavePointInterval'), ('start_position', 'GetStartPosition'),
    ('terminal_speed', 'GetTerminalSpeed'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'orientation_scalars', 'release_data_flag', 'speed_scalars',
    'vorticity', 'integration_direction', 'dash_factor', 'epsilon',
    'integration_step_length', 'maximum_propagation_time',
    'number_of_threads', 'progress_text', 'save_point_interval',
    'start_position', 'step_length', 'terminal_speed'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DashedStreamLine, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DashedStreamLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['orientation_scalars', 'speed_scalars', 'vorticity'],
            ['integration_direction'], ['dash_factor', 'epsilon',
            'integration_step_length', 'maximum_propagation_time',
            'number_of_threads', 'save_point_interval', 'start_position',
            'step_length', 'terminal_speed']),
            title='Edit DashedStreamLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DashedStreamLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


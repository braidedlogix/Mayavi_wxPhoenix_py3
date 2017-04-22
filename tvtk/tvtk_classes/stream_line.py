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


class StreamLine(Streamer):
    """
    StreamLine - generate streamline in arbitrary dataset
    
    Superclass: Streamer
    
    StreamLine is a filter that generates a streamline for an
    arbitrary dataset. A streamline is a line that is everywhere tangent
    to the vector field. Scalar values also are calculated along the
    streamline and can be used to color the line. Streamlines are
    calculated by integrating from a starting point through the vector
    field. Integration can be performed forward in time (see where the
    line goes), backward in time (see where the line came from), or in
    both directions. It also is possible to compute vorticity along the
    streamline. Vorticity is the projection (i.e., dot product) of the
    flow rotation on the velocity vector, i.e., the rotation of flow
    around the streamline.
    
    StreamLine defines the instance variable step_length. This
    parameter controls the time increment used to generate individual
    points along the streamline(s). Smaller values result in more line
    primitives but smoother streamlines. The step_length instance variable
    is defined in terms of time (i.e., the distance that the particle
    travels in the specified time period). Thus, the line segments will
    be smaller in areas of low velocity and larger in regions of high
    velocity. (NOTE: This is different than the integration_step_length
    defined by the superclass Streamer. integration_step_length is used
    to control integration step size and is expressed as a fraction of
    the cell length.) The step_length instance variable is important
    because subclasses of StreamLine (e.g., DashedStreamLine)
    depend on this value to build their representation.
    
    @sa
    Streamer DashedStreamLine StreamPoints
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStreamLine, obj, update, **traits)
    
    step_length = traits.Trait(1.0, traits.Range(1e-06, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Specify the length of a line segment. The length is expressed in
        terms of elapsed time. Smaller values result in smoother
        appearing streamlines, but greater numbers of line primitives.
        """
    )

    def _step_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStepLength,
                        self.step_length)

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
    'GetIntegrationDirection'), ('step_length', 'GetStepLength'),
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
    'start_position', 'step_length', 'terminal_speed'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StreamLine, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StreamLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['orientation_scalars', 'speed_scalars', 'vorticity'],
            ['integration_direction'], ['epsilon', 'integration_step_length',
            'maximum_propagation_time', 'number_of_threads',
            'save_point_interval', 'start_position', 'step_length',
            'terminal_speed']),
            title='Edit StreamLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StreamLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


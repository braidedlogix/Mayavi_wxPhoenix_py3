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


class Streamer(PolyDataAlgorithm):
    """
    Streamer - abstract object implements integration of massless
    particle through vector field
    
    Superclass: PolyDataAlgorithm
    
    Streamer is a filter that integrates a massless particle through a
    vector field. The integration is performed using second order
    Runge-Kutta method. Streamer often serves as a base class for
    other classes that perform numerical integration through a vector
    field (e.g., StreamLine).
    
    Note that Streamer can integrate both forward and backward in
    time, or in both directions. The length of the streamer is controlled
    by specifying an elapsed time. (The elapsed time is the time each
    particle travels.) Otherwise, the integration terminates after
    exiting the dataset or if the particle speed is reduced to a value
    less than the terminal speed.
    
    Streamer integrates through any type of dataset. As a result, if
    the dataset contains 2d cells such as polygons or triangles, the
    integration is constrained to lie on the surface defined by the 2d
    cells.
    
    The starting point of streamers may be defined in three different
    ways. Starting from global x-y-z "position" allows you to start a
    single streamer at a specified x-y-z coordinate. Starting from
    "location" allows you to start at a specified cell, sub_id, and
    parametric coordinate. Finally, you may specify a source object to
    start multiple streamers. If you start streamers using a source
    object, for each point in the source that is inside the dataset a
    streamer is created.
    
    Streamer implements the integration process in the Integrate()
    method. Because Streamer does not implement the Execute() method
    that its superclass (i.e., Filter) requires, it is an abstract class.
    Its subclasses implement the execute method and use the Integrate()
    method, and then build their own representation of the integration
    path (i.e., lines, dashed lines, points, etc.).
    
    @sa
    StreamLine DashedStreamLine StreamPoints
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStreamer, obj, update, **traits)
    
    orientation_scalars = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the creation of scalar data from vorticity
        information. The scalar information is currently the orientation
        value "theta" used in rotating stream tubes. If off, and input
        dataset has scalars, then input dataset scalars are used, unless
        speed_scalars is also on. speed_scalars takes precedence over
        orientation_scalars.
        """
    )

    def _orientation_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientationScalars,
                        self.orientation_scalars_)

    speed_scalars = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the creation of scalar data from velocity magnitude.
        If off, and input dataset has scalars, input dataset scalars are
        used.
        """
    )

    def _speed_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpeedScalars,
                        self.speed_scalars_)

    vorticity = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the computation of vorticity. Vorticity is an
        indication of the rotation of the flow. In combination with
        StreamLine and TubeFilter can be used to create rotated
        tubes. If vorticity is turned on, in the output, the velocity
        vectors are replaced by vorticity vectors.
        """
    )

    def _vorticity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVorticity,
                        self.vorticity_)

    integration_direction = traits.Trait('forward',
    tvtk_base.TraitRevPrefixMap({'forward': 0, 'backward': 1, 'integrate_both_directions': 2}), help=\
        """
        Specify the direction in which to integrate the Streamer.
        """
    )

    def _integration_direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntegrationDirection,
                        self.integration_direction_)

    epsilon = traits.Float(1e-12, enter_set=True, auto_set=False, help=\
        """
        A positive value, as small as possible for numerical comparison.
        The initial value is 1e-_12.
        """
    )

    def _epsilon_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEpsilon,
                        self.epsilon)

    integration_step_length = traits.Trait(0.2, traits.Range(1e-07, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Specify a nominal integration step size (expressed as a fraction
        of the size of each cell). This value can be larger than 1.
        """
    )

    def _integration_step_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntegrationStepLength,
                        self.integration_step_length)

    def _get_integrator(self):
        return wrap_vtk(self._vtk_obj.GetIntegrator())
    def _set_integrator(self, arg):
        old_val = self._get_integrator()
        self._wrap_call(self._vtk_obj.SetIntegrator,
                        deref_vtk(arg))
        self.trait_property_changed('integrator', old_val, arg)
    integrator = traits.Property(_get_integrator, _set_integrator, help=\
        """
        Set/get the integrator type to be used in the stream line
        calculation. The object passed is not actually used but is cloned
        with new_instance by each thread/process in the process of
        integration (prototype pattern). The default is 2nd order Runge
        Kutta.
        """
    )

    maximum_propagation_time = traits.Trait(100.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Specify the maximum length of the Streamer expressed in elapsed
        time.
        """
    )

    def _maximum_propagation_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumPropagationTime,
                        self.maximum_propagation_time)

    number_of_threads = traits.Int(12, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _number_of_threads_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfThreads,
                        self.number_of_threads)

    save_point_interval = traits.Float(1e-05, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _save_point_interval_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSavePointInterval,
                        self.save_point_interval)

    def get_start_location(self, *args):
        """
        V.get_start_location(int, [float, float, float]) -> int
        C++: IdType GetStartLocation(int &subId, double pcoords[3])
        Get the starting location of the streamline in the cell
        coordinate system.
        """
        ret = self._wrap_call(self._vtk_obj.GetStartLocation, *args)
        return ret

    def set_start_location(self, *args):
        """
        V.set_start_location(int, int, [float, float, float])
        C++: void SetStartLocation(IdType cellId, int subId,
            double pcoords[3])
        V.set_start_location(int, int, float, float, float)
        C++: void SetStartLocation(IdType cellId, int subId, double r,
            double s, double t)
        Specify the start of the streamline in the cell coordinate
        system. That is, cell_id and sub_id (if composite cell), and
        parametric coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetStartLocation, *args)
        return ret

    start_position = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Specify the start of the streamline in the global coordinate
        system. Search must be performed to find initial cell to start
        integration from.
        """
    )

    def _start_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartPosition,
                        self.start_position)

    terminal_speed = traits.Trait(0.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set/get terminal speed (i.e., speed is velocity magnitude). 
        Terminal speed is speed at which streamer will terminate
        propagation.
        """
    )

    def _terminal_speed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTerminalSpeed,
                        self.terminal_speed)

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

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    source = traits.Property(_get_source, help=\
        """
        Specify the source object used to generate starting points.
        """
    )

    def set_source_connection(self, *args):
        """
        V.set_source_connection(AlgorithmOutput)
        C++: void SetSourceConnection(AlgorithmOutput *algOutput)
        Specify the source object used to generate starting points by
        making a pipeline connection
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceConnection, *my_args)
        return ret

    def set_source_data(self, *args):
        """
        V.set_source_data(DataSet)
        C++: void SetSourceData(DataSet *source)
        Specify the source object used to generate starting points.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceData, *my_args)
        return ret

    _updateable_traits_ = \
    (('orientation_scalars', 'GetOrientationScalars'), ('speed_scalars',
    'GetSpeedScalars'), ('vorticity', 'GetVorticity'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('integration_direction',
    'GetIntegrationDirection'), ('epsilon', 'GetEpsilon'),
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
    'vorticity', 'integration_direction', 'epsilon',
    'integration_step_length', 'maximum_propagation_time',
    'number_of_threads', 'progress_text', 'save_point_interval',
    'start_position', 'terminal_speed'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Streamer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Streamer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['orientation_scalars', 'speed_scalars', 'vorticity'],
            ['integration_direction'], ['epsilon', 'integration_step_length',
            'maximum_propagation_time', 'number_of_threads',
            'save_point_interval', 'start_position', 'terminal_speed']),
            title='Edit Streamer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Streamer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


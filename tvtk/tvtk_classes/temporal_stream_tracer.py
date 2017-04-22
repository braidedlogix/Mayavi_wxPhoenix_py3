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

from tvtk.tvtk_classes.stream_tracer import StreamTracer


class TemporalStreamTracer(StreamTracer):
    """
    TemporalStreamTracer - A Parallel Particle tracer for unsteady
    vector fields
    
    Superclass: StreamTracer
    
    TemporalStreamTracer is a filter that integrates a vector field to
    generate
    
    @sa
    RibbonFilter RuledSurfaceFilter InitialValueProblemSolver
    RungeKutta2 RungeKutta4 RungeKutta45 StreamTracer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTemporalStreamTracer, obj, update, **traits)
    
    enable_particle_writing = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the filename to be used with the particle writer when
        dumping particles to disk
        """
    )

    def _enable_particle_writing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableParticleWriting,
                        self.enable_particle_writing_)

    ignore_pipeline_time = tvtk_base.false_bool_trait(help=\
        """
        To get around problems with the Paraview Animation controls we
        can just animate the time step and ignore the TIME_ requests
        """
    )

    def _ignore_pipeline_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIgnorePipelineTime,
                        self.ignore_pipeline_time_)

    static_mesh = tvtk_base.true_bool_trait(help=\
        """
        if static_mesh is set, many optimizations for cell caching can be
        assumed. if static_mesh is not set, the algorithm will attempt to
        find out if optimizations can be used, but setting it to true
        will force all optimizations. Do not Set static_mesh to true if a
        dynamic mesh is being used as this will invalidate all results.
        """
    )

    def _static_mesh_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStaticMesh,
                        self.static_mesh_)

    static_seeds = tvtk_base.true_bool_trait(help=\
        """
        if static_seeds is set and the mesh is static, then every time
        particles are injected we can re-use the same injection
        information. We classify particles according to processor just
        once before start. If static_seeds is set and a moving seed source
        is specified the motion will be ignored and results will not be
        as expected.
        """
    )

    def _static_seeds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStaticSeeds,
                        self.static_seeds_)

    termination_time_unit = traits.Trait('step_unit',
    tvtk_base.TraitRevPrefixMap({'step_unit': 1, 'time_unit': 0}), help=\
        """
        The units of termination_time may be actual 'Time' units as
        described by the data, or just time_steps of iteration.
        """
    )

    def _termination_time_unit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTerminationTimeUnit,
                        self.termination_time_unit_)

    force_reinjection_every_n_steps = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        When animating particles, it is nice to inject new ones every Nth
        step to produce a continuous flow. Setting
        force_reinjection_every_n_steps to a non zero value will cause the
        particle source to reinject particles every Nth step even if it
        is otherwise unchanged. Note that if the particle source is also
        animated, this flag will be redundant as the particles will be
        reinjected whenever the source changes anyway
        """
    )

    def _force_reinjection_every_n_steps_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForceReinjectionEveryNSteps,
                        self.force_reinjection_every_n_steps)

    particle_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the filename to be used with the particle writer when
        dumping particles to disk
        """
    )

    def _particle_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetParticleFileName,
                        self.particle_file_name)

    def _get_particle_writer(self):
        return wrap_vtk(self._vtk_obj.GetParticleWriter())
    def _set_particle_writer(self, arg):
        old_val = self._get_particle_writer()
        self._wrap_call(self._vtk_obj.SetParticleWriter,
                        deref_vtk(arg))
        self.trait_property_changed('particle_writer', old_val, arg)
    particle_writer = traits.Property(_get_particle_writer, _set_particle_writer, help=\
        """
        Set/Get the Writer associated with this Particle Tracer Ideally a
        parallel IO capable H5PartWriter should be used which will
        collect particles from all parallel processes and write them to a
        single HDF5 file.
        """
    )

    termination_time = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Setting termination_time to a positive value will cause particles
        to terminate when the time is reached. Use a vlue of zero to
        diable termination. The units of time should be consistent with
        the primary time variable.
        """
    )

    def _termination_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTerminationTime,
                        self.termination_time)

    time_step = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the time_step. This is the primary means of advancing the
        particles. The time_step should be animated and this will drive
        the pipeline forcing timesteps to be fetched from upstream.
        """
    )

    def _time_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStep,
                        self.time_step)

    time_step_resolution = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        If the data source does not have the correct time values present
        on each time step - setting this value to non unity can be used
        to adjust the time step size from 1s pre step to
        1x__time_step_resolution : Not functional in this version. Broke it
        @todo, put back time scaling
        """
    )

    def _time_step_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStepResolution,
                        self.time_step_resolution)

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

    def add_source_connection(self, *args):
        """
        V.add_source_connection(AlgorithmOutput)
        C++: void AddSourceConnection(AlgorithmOutput *input)
        Provide support for multiple see sources
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddSourceConnection, *my_args)
        return ret

    def remove_all_sources(self):
        """
        V.remove_all_sources()
        C++: void RemoveAllSources()
        Provide support for multiple see sources
        """
        ret = self._vtk_obj.RemoveAllSources()
        return ret
        

    _updateable_traits_ = \
    (('enable_particle_writing', 'GetEnableParticleWriting'),
    ('ignore_pipeline_time', 'GetIgnorePipelineTime'), ('static_mesh',
    'GetStaticMesh'), ('static_seeds', 'GetStaticSeeds'),
    ('surface_streamlines', 'GetSurfaceStreamlines'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('termination_time_unit',
    'GetTerminationTimeUnit'), ('integration_direction',
    'GetIntegrationDirection'), ('integrator_type', 'GetIntegratorType'),
    ('force_reinjection_every_n_steps', 'GetForceReinjectionEveryNSteps'),
    ('particle_file_name', 'GetParticleFileName'), ('termination_time',
    'GetTerminationTime'), ('time_step', 'GetTimeStep'),
    ('time_step_resolution', 'GetTimeStepResolution'),
    ('compute_vorticity', 'GetComputeVorticity'),
    ('initial_integration_step', 'GetInitialIntegrationStep'),
    ('integration_step_unit', 'GetIntegrationStepUnit'), ('maximum_error',
    'GetMaximumError'), ('maximum_integration_step',
    'GetMaximumIntegrationStep'), ('maximum_number_of_steps',
    'GetMaximumNumberOfSteps'), ('maximum_propagation',
    'GetMaximumPropagation'), ('minimum_integration_step',
    'GetMinimumIntegrationStep'), ('rotation_scale', 'GetRotationScale'),
    ('start_position', 'GetStartPosition'), ('terminal_speed',
    'GetTerminalSpeed'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'enable_particle_writing',
    'global_warning_display', 'ignore_pipeline_time', 'release_data_flag',
    'static_mesh', 'static_seeds', 'surface_streamlines',
    'integration_direction', 'integrator_type', 'termination_time_unit',
    'compute_vorticity', 'force_reinjection_every_n_steps',
    'initial_integration_step', 'integration_step_unit', 'maximum_error',
    'maximum_integration_step', 'maximum_number_of_steps',
    'maximum_propagation', 'minimum_integration_step',
    'particle_file_name', 'progress_text', 'rotation_scale',
    'start_position', 'terminal_speed', 'termination_time', 'time_step',
    'time_step_resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TemporalStreamTracer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TemporalStreamTracer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enable_particle_writing', 'ignore_pipeline_time',
            'static_mesh', 'static_seeds', 'surface_streamlines'],
            ['integration_direction', 'integrator_type', 'termination_time_unit'],
            ['compute_vorticity', 'force_reinjection_every_n_steps',
            'initial_integration_step', 'integration_step_unit', 'maximum_error',
            'maximum_integration_step', 'maximum_number_of_steps',
            'maximum_propagation', 'minimum_integration_step',
            'particle_file_name', 'rotation_scale', 'start_position',
            'terminal_speed', 'termination_time', 'time_step',
            'time_step_resolution']),
            title='Edit TemporalStreamTracer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TemporalStreamTracer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


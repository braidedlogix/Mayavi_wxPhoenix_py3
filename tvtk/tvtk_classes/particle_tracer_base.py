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


class ParticleTracerBase(PolyDataAlgorithm):
    """
    ParticleTracerBase - A particle tracer for vector fields
    
    Superclass: PolyDataAlgorithm
    
    ParticleTracerBase is the base class for filters that advect
    particles in a vector field. Note that the input PointData
    structure must be identical on all datasets.
    
    @sa
    RibbonFilter RuledSurfaceFilter InitialValueProblemSolver
    RungeKutta2 RungeKutta4 RungeKutta45 StreamTracer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParticleTracerBase, obj, update, **traits)
    
    disable_reset_cache = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the flag to disable cache This is off by default and
        turned on in special circumstances such as in a coprocessing
        workflow
        """
    )

    def _disable_reset_cache_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisableResetCache,
                        self.disable_reset_cache_)

    enable_particle_writing = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the filename to be used with the particle writer when
        dumping particles to disk
        """
    )

    def _enable_particle_writing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableParticleWriting,
                        self.enable_particle_writing_)

    ignore_pipeline_time = tvtk_base.true_bool_trait(help=\
        """
        To get around problems with the Paraview Animation controls we
        can just animate the time step and ignore the TIME_ requests
        """
    )

    def _ignore_pipeline_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIgnorePipelineTime,
                        self.ignore_pipeline_time_)

    compute_vorticity = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Turn on/off vorticity computation at streamline points (necessary
        for generating proper stream-ribbons using the RibbonFilter.
        """
    )

    def _compute_vorticity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeVorticity,
                        self.compute_vorticity)

    force_reinjection_every_n_steps = traits.Int(0, enter_set=True, auto_set=False, help=\
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

    def _get_integrator(self):
        return wrap_vtk(self._vtk_obj.GetIntegrator())
    def _set_integrator(self, arg):
        old_val = self._get_integrator()
        self._wrap_call(self._vtk_obj.SetIntegrator,
                        deref_vtk(arg))
        self.trait_property_changed('integrator', old_val, arg)
    integrator = traits.Property(_get_integrator, _set_integrator, help=\
        """
        
        """
    )

    integrator_type = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _integrator_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntegratorType,
                        self.integrator_type)

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

    rotation_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        This can be used to scale the rate with which the streamribbons
        twist. The default is 1.
        """
    )

    def _rotation_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRotationScale,
                        self.rotation_scale)

    start_time = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the time value for particle tracing to begin. The units of
        time should be consistent with the primary time variable.
        """
    )

    def _start_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartTime,
                        self.start_time)

    static_mesh = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        if static_mesh is set, many optimizations for cell caching can be
        assumed. if static_mesh is not set, the algorithm will attempt to
        find out if optimizations can be used, but setting it to true
        will force all optimizations. Do not Set static_mesh to true if a
        dynamic mesh is being used as this will invalidate all results.
        The default is that static_mesh is 0.
        """
    )

    def _static_mesh_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStaticMesh,
                        self.static_mesh)

    static_seeds = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        if static_seeds is set and the mesh is static, then every time
        particles are injected we can re-use the same injection
        information. We classify particles according to processor just
        once before start. If static_seeds is set and a moving seed source
        is specified the motion will be ignored and results will not be
        as expected. The default is that static_seeds is 0.
        """
    )

    def _static_seeds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStaticSeeds,
                        self.static_seeds)

    terminal_speed = traits.Float(1e-12, enter_set=True, auto_set=False, help=\
        """
        Specify the terminal speed value, below which integration is
        terminated.
        """
    )

    def _terminal_speed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTerminalSpeed,
                        self.terminal_speed)

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
        Provide support for multiple seed sources
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddSourceConnection, *my_args)
        return ret

    def print_particle_histories(self):
        """
        V.print_particle_histories()
        C++: void PrintParticleHistories()"""
        ret = self._vtk_obj.PrintParticleHistories()
        return ret
        

    def remove_all_sources(self):
        """
        V.remove_all_sources()
        C++: void RemoveAllSources()
        Provide support for multiple seed sources
        """
        ret = self._vtk_obj.RemoveAllSources()
        return ret
        

    _updateable_traits_ = \
    (('disable_reset_cache', 'GetDisableResetCache'),
    ('enable_particle_writing', 'GetEnableParticleWriting'),
    ('ignore_pipeline_time', 'GetIgnorePipelineTime'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('compute_vorticity',
    'GetComputeVorticity'), ('force_reinjection_every_n_steps',
    'GetForceReinjectionEveryNSteps'), ('integrator_type',
    'GetIntegratorType'), ('particle_file_name', 'GetParticleFileName'),
    ('rotation_scale', 'GetRotationScale'), ('start_time',
    'GetStartTime'), ('static_mesh', 'GetStaticMesh'), ('static_seeds',
    'GetStaticSeeds'), ('terminal_speed', 'GetTerminalSpeed'),
    ('termination_time', 'GetTerminationTime'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'disable_reset_cache',
    'enable_particle_writing', 'global_warning_display',
    'ignore_pipeline_time', 'release_data_flag', 'compute_vorticity',
    'force_reinjection_every_n_steps', 'integrator_type',
    'particle_file_name', 'progress_text', 'rotation_scale', 'start_time',
    'static_mesh', 'static_seeds', 'terminal_speed', 'termination_time'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParticleTracerBase, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ParticleTracerBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['disable_reset_cache', 'enable_particle_writing',
            'ignore_pipeline_time'], [], ['compute_vorticity',
            'force_reinjection_every_n_steps', 'integrator_type',
            'particle_file_name', 'rotation_scale', 'start_time', 'static_mesh',
            'static_seeds', 'terminal_speed', 'termination_time']),
            title='Edit ParticleTracerBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParticleTracerBase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


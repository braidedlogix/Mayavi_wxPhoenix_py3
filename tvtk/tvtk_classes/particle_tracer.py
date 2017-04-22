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

from tvtk.tvtk_classes.particle_tracer_base import ParticleTracerBase


class ParticleTracer(ParticleTracerBase):
    """
    ParticleTracer - A Parallel Particle tracer for unsteady vector
    fields
    
    Superclass: ParticleTracerBase
    
    ParticleTracer is a filter that integrates a vector field to
    advect particles
    
    @sa
    ParticleTracerBase has the details of the algorithms
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParticleTracer, obj, update, **traits)
    
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
            return super(ParticleTracer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ParticleTracer properties', scrollable=True, resizable=True,
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
            title='Edit ParticleTracer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParticleTracer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class AMRBaseParticlesReader(MultiBlockDataSetAlgorithm):
    """
    AMRBaseParticlesReader -  An abstract base class that implements
    all the common functionality for
     all particle readers.
    
    Superclass: MultiBlockDataSetAlgorithm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAMRBaseParticlesReader, obj, update, **traits)
    
    filter_location = tvtk_base.false_bool_trait(help=\
        """
        Set & Get for filter location and boolean macro
        """
    )

    def _filter_location_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilterLocation,
                        self.filter_location_)

    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        Set & Get the multi-process controller.
        """
    )

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    frequency = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set & Get the frequency.
        """
    )

    def _frequency_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrequency,
                        self.frequency)

    def get_particle_array_status(self, *args):
        """
        V.get_particle_array_status(string) -> int
        C++: int GetParticleArrayStatus(const char *name)
        Get/Set whether the particle array status.
        """
        ret = self._wrap_call(self._vtk_obj.GetParticleArrayStatus, *args)
        return ret

    def set_particle_array_status(self, *args):
        """
        V.set_particle_array_status(string, int)
        C++: void SetParticleArrayStatus(const char *name, int status)
        Get/Set whether the particle array status.
        """
        ret = self._wrap_call(self._vtk_obj.SetParticleArrayStatus, *args)
        return ret

    def _get_number_of_particle_arrays(self):
        return self._vtk_obj.GetNumberOfParticleArrays()
    number_of_particle_arrays = traits.Property(_get_number_of_particle_arrays, help=\
        """
        Get the number of particles arrays available in the input.
        """
    )

    def get_particle_array_name(self, *args):
        """
        V.get_particle_array_name(int) -> string
        C++: const char *GetParticleArrayName(int index)
        Get the particle array name of the array associated with the
        given index.
        """
        ret = self._wrap_call(self._vtk_obj.GetParticleArrayName, *args)
        return ret

    def _get_particle_data_array_selection(self):
        return wrap_vtk(self._vtk_obj.GetParticleDataArraySelection())
    particle_data_array_selection = traits.Property(_get_particle_data_array_selection, help=\
        """
        Get the data array selection tables used to configure which data
        arrays are loaded by the reader.
        """
    )

    def _get_total_number_of_particles(self):
        return self._vtk_obj.GetTotalNumberOfParticles()
    total_number_of_particles = traits.Property(_get_total_number_of_particles, help=\
        """
        Returns the total number of particles
        """
    )

    def set_max_location(self, *args):
        """
        V.set_max_location(float, float, float)
        C++: void SetMaxLocation(const double maxx, const double maxy,
            const double maxz)
        Sets the max location
        """
        ret = self._wrap_call(self._vtk_obj.SetMaxLocation, *args)
        return ret

    def set_min_location(self, *args):
        """
        V.set_min_location(float, float, float)
        C++: void SetMinLocation(const double minx, const double miny,
            const double minz)
        Sets the min location
        """
        ret = self._wrap_call(self._vtk_obj.SetMinLocation, *args)
        return ret

    _updateable_traits_ = \
    (('filter_location', 'GetFilterLocation'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('file_name', 'GetFileName'),
    ('frequency', 'GetFrequency'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'filter_location',
    'global_warning_display', 'release_data_flag', 'file_name',
    'frequency', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AMRBaseParticlesReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AMRBaseParticlesReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['filter_location'], [], ['file_name', 'frequency']),
            title='Edit AMRBaseParticlesReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AMRBaseParticlesReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.writer import Writer


class EnSightWriter(Writer):
    """
    EnSightWriter - write vtk unstructured grid data as an en_sight file
    
    Superclass: Writer
    
    EnSightWriter is a source object that writes binary unstructured
    grid data files in en_sight format. See en_sight Manual for format
    details
    
    @warning
    Binary files written on one system may not be readable on other
    systems. Be sure to specify the endian-ness of the file when reading
    it into en_sight
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEnSightWriter, obj, update, **traits)
    
    base_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify base name of en_sight data files to write.
        """
    )

    def _base_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBaseName,
                        self.base_name)

    def _get_block_i_ds(self):
        return self._vtk_obj.GetBlockIDs()
    def _set_block_i_ds(self, arg):
        old_val = self._get_block_i_ds()
        self._wrap_call(self._vtk_obj.SetBlockIDs,
                        arg)
        self.trait_property_changed('block_i_ds', old_val, arg)
    block_i_ds = traits.Property(_get_block_i_ds, _set_block_i_ds, help=\
        """
        set the array of Block ID's this class keeps a reference to the
        array and will not delete it
        """
    )

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the path and base name of the output files.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    ghost_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify the number of ghost levels to include in output files
        """
    )

    def _ghost_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGhostLevel,
                        self.ghost_level)

    number_of_blocks = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        set the number of block ID's
        """
    )

    def _number_of_blocks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfBlocks,
                        self.number_of_blocks)

    path = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify path of en_sight data files to write.
        """
    )

    def _path_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPath,
                        self.path)

    process_number = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify which process this writer is
        """
    )

    def _process_number_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProcessNumber,
                        self.process_number)

    time_step = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify the Timestep that this data is for
        """
    )

    def _time_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStep,
                        self.time_step)

    transient_geometry = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Specify whether the geoemtry changes each timestep if false,
        geometry is only written at timestep 0
        """
    )

    def _transient_geometry_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTransientGeometry,
                        self.transient_geometry)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Specify the input data or filter.
        """
    )

    def write_case_file(self, *args):
        """
        V.write_case_file(int)
        C++: virtual void WriteCaseFile(int TotalTimeSteps)
        Writes the case file that en_sight is capable of reading The other
        data files must be written before the case file and the input
        must be one of the time steps variables must be the same for all
        time steps or the case file will be missing variables
        """
        ret = self._wrap_call(self._vtk_obj.WriteCaseFile, *args)
        return ret

    def write_sos_case_file(self, *args):
        """
        V.write_sos_case_file(int)
        C++: virtual void WriteSOSCaseFile(int NumProcs)
        Writes the case file that en_sight is capable of reading The other
        data files must be written before the case file and the input
        must be one of the time steps variables must be the same for all
        time steps or the case file will be missing variables
        """
        ret = self._wrap_call(self._vtk_obj.WriteSOSCaseFile, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('base_name',
    'GetBaseName'), ('file_name', 'GetFileName'), ('ghost_level',
    'GetGhostLevel'), ('number_of_blocks', 'GetNumberOfBlocks'), ('path',
    'GetPath'), ('process_number', 'GetProcessNumber'), ('time_step',
    'GetTimeStep'), ('transient_geometry', 'GetTransientGeometry'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'base_name', 'file_name', 'ghost_level',
    'number_of_blocks', 'path', 'process_number', 'progress_text',
    'time_step', 'transient_geometry'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EnSightWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit EnSightWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['base_name', 'file_name', 'ghost_level',
            'number_of_blocks', 'path', 'process_number', 'time_step',
            'transient_geometry']),
            title='Edit EnSightWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EnSightWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


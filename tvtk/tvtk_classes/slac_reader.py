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


class SLACReader(MultiBlockDataSetAlgorithm):
    """
    SLACReader - A reader for a data format used by Omega3p, Tau3p,
    and several other tools used at the Standford Linear Accelerator
    Center (SLAC).
    
    Superclass: MultiBlockDataSetAlgorithm
    
    The underlying format uses net_cdf to store arrays, but also imposes
    several conventions to form an unstructured grid of elements.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSLACReader, obj, update, **traits)
    
    read_external_surface = tvtk_base.true_bool_trait(help=\
        """
        If on, reads the external surfaces of the data set.  Set to on by
        default.
        """
    )

    def _read_external_surface_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadExternalSurface,
                        self.read_external_surface_)

    read_internal_volume = tvtk_base.false_bool_trait(help=\
        """
        If on, reads the internal volume of the data set.  Set to off by
        default.
        """
    )

    def _read_internal_volume_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadInternalVolume,
                        self.read_internal_volume_)

    read_midpoints = tvtk_base.true_bool_trait(help=\
        """
        If on, reads midpoint information for external surfaces and
        builds quadratic surface triangles.  Set to on by default.
        """
    )

    def _read_midpoints_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadMidpoints,
                        self.read_midpoints_)

    mesh_file_name = tvtk_base.vtk_file_name("", help=\
        """
        
        """
    )

    def _mesh_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMeshFileName,
                        self.mesh_file_name)

    def get_variable_array_status(self, *args):
        """
        V.get_variable_array_status(string) -> int
        C++: virtual int GetVariableArrayStatus(const char *name)
        Variable array selection.
        """
        ret = self._wrap_call(self._vtk_obj.GetVariableArrayStatus, *args)
        return ret

    def set_variable_array_status(self, *args):
        """
        V.set_variable_array_status(string, int)
        C++: virtual void SetVariableArrayStatus(const char *name,
            int status)
        Variable array selection.
        """
        ret = self._wrap_call(self._vtk_obj.SetVariableArrayStatus, *args)
        return ret

    def _get_frequency_scales(self):
        return wrap_vtk(self._vtk_obj.GetFrequencyScales())
    frequency_scales = traits.Property(_get_frequency_scales, help=\
        """
        NOTE: This is not thread-safe.
        """
    )

    def get_mode_file_name(self, *args):
        """
        V.get_mode_file_name(int) -> string
        C++: virtual const char *GetModeFileName(unsigned int idx)
        There may be one mode file (usually for actual modes) or multiple
        mode files (which usually actually represent time series).  These
        methods set and clear the list of mode files (which can be a
        single mode file).
        """
        ret = self._wrap_call(self._vtk_obj.GetModeFileName, *args)
        return ret

    def _get_number_of_mode_file_names(self):
        return self._vtk_obj.GetNumberOfModeFileNames()
    number_of_mode_file_names = traits.Property(_get_number_of_mode_file_names, help=\
        """
        There may be one mode file (usually for actual modes) or multiple
        mode files (which usually actually represent time series).  These
        methods set and clear the list of mode files (which can be a
        single mode file).
        """
    )

    def _get_number_of_variable_arrays(self):
        return self._vtk_obj.GetNumberOfVariableArrays()
    number_of_variable_arrays = traits.Property(_get_number_of_variable_arrays, help=\
        """
        Variable array selection.
        """
    )

    def _get_phase_shifts(self):
        return wrap_vtk(self._vtk_obj.GetPhaseShifts())
    phase_shifts = traits.Property(_get_phase_shifts, help=\
        """
        NOTE: This is not thread-safe.
        """
    )

    def get_variable_array_name(self, *args):
        """
        V.get_variable_array_name(int) -> string
        C++: virtual const char *GetVariableArrayName(int idx)
        Variable array selection.
        """
        ret = self._wrap_call(self._vtk_obj.GetVariableArrayName, *args)
        return ret

    def add_mode_file_name(self, *args):
        """
        V.add_mode_file_name(string)
        C++: virtual void AddModeFileName(const char *fname)
        There may be one mode file (usually for actual modes) or multiple
        mode files (which usually actually represent time series).  These
        methods set and clear the list of mode files (which can be a
        single mode file).
        """
        ret = self._wrap_call(self._vtk_obj.AddModeFileName, *args)
        return ret

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: static int CanReadFile(const char *filename)
        Returns true if the given file can be read by this reader.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    def IS_EXTERNAL_SURFACE(self):
        """
        V.is__external__surface() -> InformationIntegerKey
        C++: static InformationIntegerKey *IS_EXTERNAL_SURFACE()
        This key is attached to the metadata information of all data sets
        in the output that are part of the external surface.
        """
        ret = wrap_vtk(self._vtk_obj.IS_EXTERNAL_SURFACE())
        return ret
        

    def IS_INTERNAL_VOLUME(self):
        """
        V.is__internal__volume() -> InformationIntegerKey
        C++: static InformationIntegerKey *IS_INTERNAL_VOLUME()
        This key is attached to the metadata information of all data sets
        in the output that are part of the internal volume.
        """
        ret = wrap_vtk(self._vtk_obj.IS_INTERNAL_VOLUME())
        return ret
        

    def POINTS(self):
        """
        V.points() -> InformationObjectBaseKey
        C++: static InformationObjectBaseKey *POINTS()
        All the data sets stored in the multiblock output share the same
        point data.  For convienience, the point coordinates (vtk_points)
        and point data (vtk_point_data) are saved under these keys in the
        Information of the output data set.
        """
        ret = wrap_vtk(self._vtk_obj.POINTS())
        return ret
        

    def POINT_DATA(self):
        """
        V.point__data() -> InformationObjectBaseKey
        C++: static InformationObjectBaseKey *POINT_DATA()
        All the data sets stored in the multiblock output share the same
        point data.  For convienience, the point coordinates (vtk_points)
        and point data (vtk_point_data) are saved under these keys in the
        Information of the output data set.
        """
        ret = wrap_vtk(self._vtk_obj.POINT_DATA())
        return ret
        

    def remove_all_mode_file_names(self):
        """
        V.remove_all_mode_file_names()
        C++: virtual void RemoveAllModeFileNames()
        There may be one mode file (usually for actual modes) or multiple
        mode files (which usually actually represent time series).  These
        methods set and clear the list of mode files (which can be a
        single mode file).
        """
        ret = self._vtk_obj.RemoveAllModeFileNames()
        return ret
        

    def reset_frequency_scales(self):
        """
        V.reset_frequency_scales()
        C++: virtual void ResetFrequencyScales()
        Sets the scale factor for each mode. Each scale factor is reset
        to 1.
        """
        ret = self._vtk_obj.ResetFrequencyScales()
        return ret
        

    def reset_phase_shifts(self):
        """
        V.reset_phase_shifts()
        C++: virtual void ResetPhaseShifts()
        Sets the phase offset for each mode. Each shift is reset to 0.
        """
        ret = self._vtk_obj.ResetPhaseShifts()
        return ret
        

    def set_frequency_scale(self, *args):
        """
        V.set_frequency_scale(int, float)
        C++: virtual void SetFrequencyScale(int index, double scale)
        Sets the scale factor for each mode. Each scale factor is reset
        to 1.
        """
        ret = self._wrap_call(self._vtk_obj.SetFrequencyScale, *args)
        return ret

    def set_phase_shift(self, *args):
        """
        V.set_phase_shift(int, float)
        C++: virtual void SetPhaseShift(int index, double shift)
        Sets the phase offset for each mode. Each shift is reset to 0.
        """
        ret = self._wrap_call(self._vtk_obj.SetPhaseShift, *args)
        return ret

    _updateable_traits_ = \
    (('read_external_surface', 'GetReadExternalSurface'),
    ('read_internal_volume', 'GetReadInternalVolume'), ('read_midpoints',
    'GetReadMidpoints'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('mesh_file_name', 'GetMeshFileName'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'read_external_surface', 'read_internal_volume', 'read_midpoints',
    'release_data_flag', 'mesh_file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SLACReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SLACReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['read_external_surface', 'read_internal_volume',
            'read_midpoints'], [], ['mesh_file_name']),
            title='Edit SLACReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SLACReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


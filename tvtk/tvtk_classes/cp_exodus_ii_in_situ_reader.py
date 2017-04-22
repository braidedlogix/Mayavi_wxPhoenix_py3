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


class CPExodusIIInSituReader(MultiBlockDataSetAlgorithm):
    """
    CPExodusIIInSituReader - Read an Exodus II file into data
    structures that map the raw arrays returned by the Exodus II library
    into a multi-block data set containing UnstructuredGridBase
    subclasses.
    
    Superclass: MultiBlockDataSetAlgorithm
    
    This class can be used to import Exodus II files into VTK without
    repacking the data into the standard VTK memory layout, avoiding the
    cost of a deep copy.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCPExodusIIInSituReader, obj, update, **traits)
    
    current_time_step = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the current timestep to read as a zero-based index.
        """
    )

    def _current_time_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCurrentTimeStep,
                        self.current_time_step)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Get/Set the name of the Exodus file to read.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_time_step_range(self):
        return self._vtk_obj.GetTimeStepRange()
    time_step_range = traits.Property(_get_time_step_range, help=\
        """
        
        """
    )

    def get_time_step_value(self, *args):
        """
        V.get_time_step_value(int) -> float
        C++: double GetTimeStepValue(int step)
        Get the floating point tag associated with the timestep at
        'step'.
        """
        ret = self._wrap_call(self._vtk_obj.GetTimeStepValue, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('current_time_step', 'GetCurrentTimeStep'), ('file_name',
    'GetFileName'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'current_time_step', 'file_name',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CPExodusIIInSituReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CPExodusIIInSituReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['current_time_step', 'file_name']),
            title='Edit CPExodusIIInSituReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CPExodusIIInSituReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


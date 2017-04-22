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

from tvtk.tvtk_classes.pass_input_type_algorithm import PassInputTypeAlgorithm


class ExtractTimeSteps(PassInputTypeAlgorithm):
    """
    ExtractTimeSteps - extract specific time-steps from dataset
    
    Superclass: PassInputTypeAlgorithm
    
    ExtractTimeSteps extracts the specified time steps from the input
    dataset. The timesteps to be extracted are specified by their
    indices. If no time step is specified, all of the input time steps
    are extracted. This filter is useful when one wants to work with only
    a sub-set of the input time steps.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractTimeSteps, obj, update, **traits)
    
    def get_time_step_indices(self, *args):
        """
        V.get_time_step_indices([int, ...])
        C++: void GetTimeStepIndices(int *timeStepIndices)
        Get/Set an array of time step indices. For the Get function,
        time_step_indices should be big enough for get_number_of_time_steps()
        values.
        """
        ret = self._wrap_call(self._vtk_obj.GetTimeStepIndices, *args)
        return ret

    def set_time_step_indices(self, *args):
        """
        V.set_time_step_indices(int, (int, ...))
        C++: void SetTimeStepIndices(int count,
            const int *timeStepIndices)
        Get/Set an array of time step indices. For the Get function,
        time_step_indices should be big enough for get_number_of_time_steps()
        values.
        """
        ret = self._wrap_call(self._vtk_obj.SetTimeStepIndices, *args)
        return ret

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def _get_number_of_time_steps(self):
        return self._vtk_obj.GetNumberOfTimeSteps()
    number_of_time_steps = traits.Property(_get_number_of_time_steps, help=\
        """
        Get the number of time steps that will be extracted
        """
    )

    def add_time_step_index(self, *args):
        """
        V.add_time_step_index(int)
        C++: void AddTimeStepIndex(int timeStepIndex)
        Add a time step index. Not added if the index already exists.
        """
        ret = self._wrap_call(self._vtk_obj.AddTimeStepIndex, *args)
        return ret

    def clear_time_step_indices(self):
        """
        V.clear_time_step_indices()
        C++: void ClearTimeStepIndices()
        Clear the time step indices
        """
        ret = self._vtk_obj.ClearTimeStepIndices()
        return ret
        

    def generate_time_step_indices(self, *args):
        """
        V.generate_time_step_indices(int, int, int)
        C++: void GenerateTimeStepIndices(int begin, int end, int step)
        Generate a range of indices in [begin, end) with a step size of
        'step'
        """
        ret = self._wrap_call(self._vtk_obj.GenerateTimeStepIndices, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractTimeSteps, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractTimeSteps properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ExtractTimeSteps properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractTimeSteps properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


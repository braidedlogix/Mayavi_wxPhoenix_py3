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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class ExtractTemporalFieldData(DataObjectAlgorithm):
    """
    ExtractTemporalFieldData - Extract temporal arrays from input
    field data
    
    Superclass: DataObjectAlgorithm
    
    ExtractTemporalFieldData extracts arrays from the input
    FieldData. These arrays are assumed to contain temporal data,
    where the nth tuple contains the value for the nth timestep.
    
    For composite datasets, the filter has two modes, it can treat each
    block in the dataset individually (default) or just look at the first
    non-empty field data (common for readers ExodusIIReader). For
    latter, set handle_composite_data_blocks_individually to false.
    
    The output is a Table (or a multiblock of Tables) based of
    whether handle_composite_data_blocks_individually is true and input is a
    composite dataset.
    
    This algorithm does not produce a TIME_STEPS or TIME_RANGE
    information because it works across time.
    
    @par Caveat: This algorithm works only with source that produce
    TIME_STEPS(). Continuous time range is not yet supported.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractTemporalFieldData, obj, update, **traits)
    
    handle_composite_data_blocks_individually = tvtk_base.true_bool_trait(help=\
        """
        When set to true (default), if the input is a
        CompositeDataSet, then each block in the input dataset in
        processed separately. If false, then the first non-empty
        field_data is considered.
        """
    )

    def _handle_composite_data_blocks_individually_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleCompositeDataBlocksIndividually,
                        self.handle_composite_data_blocks_individually_)

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

    def _get_number_of_time_steps(self):
        return self._vtk_obj.GetNumberOfTimeSteps()
    number_of_time_steps = traits.Property(_get_number_of_time_steps, help=\
        """
        Get the number of time steps
        """
    )

    _updateable_traits_ = \
    (('handle_composite_data_blocks_individually',
    'GetHandleCompositeDataBlocksIndividually'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'handle_composite_data_blocks_individually', 'release_data_flag',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractTemporalFieldData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractTemporalFieldData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['handle_composite_data_blocks_individually'], [], []),
            title='Edit ExtractTemporalFieldData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractTemporalFieldData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


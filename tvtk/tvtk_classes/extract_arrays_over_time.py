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


class ExtractArraysOverTime(MultiBlockDataSetAlgorithm):
    """
    ExtractArraysOverTime - extracts a selection over time.
    
    Superclass: MultiBlockDataSetAlgorithm
    
    ExtractArraysOverTime extracts a selection over time. The output
    is a multiblock dataset. If selection content type is
    Selection::Locations, then each output block corresponds to each
    probed location. Otherwise, each output block corresponds to an
    extracted cell/point depending on whether the selection field type is
    CELL or POINT. Each block is a Table with a column named Time (or
    time_data if Time exists in the input). When extracting point data,
    the input point coordinates are copied to a column named Point
    Coordinates or Points (if Point Coordinates exists in the input).
    This algorithm does not produce a TIME_STEPS or TIME_RANGE
    information because it works across time.@par Caveat: This algorithm
    works only with source that produce TIME_STEPS(). Continuous time
    range is not yet supported.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractArraysOverTime, obj, update, **traits)
    
    report_statistics_only = tvtk_base.false_bool_trait(help=\
        """
        Instead of breaking a selection into a separate time-history
        table for each (block,ID)-tuple, you may call
        report_statistics_only_on(). Then a single table per block of the
        input dataset will report the minimum, maximum, quartiles, and
        (for numerical arrays) the average and standard deviation of the
        selection over time.
        
        * The default is off to preserve backwards-compatibility.
        """
    )

    def _report_statistics_only_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReportStatisticsOnly,
                        self.report_statistics_only_)

    def _get_selection_extractor(self):
        return wrap_vtk(self._vtk_obj.GetSelectionExtractor())
    def _set_selection_extractor(self, arg):
        old_val = self._get_selection_extractor()
        self._wrap_call(self._vtk_obj.SetSelectionExtractor,
                        deref_vtk(arg))
        self.trait_property_changed('selection_extractor', old_val, arg)
    selection_extractor = traits.Property(_get_selection_extractor, _set_selection_extractor, help=\
        """
        Set/get the ExtractSelection instance used to obtain array
        values at each time step. An instance of ExtractSelection is
        created on demand when the filter is first executed.
        
        * This is used by para_view to override the default
        * extractor with one that supports Python-based QUERY
        * selection.
        """
    )

    def _get_number_of_time_steps(self):
        return self._vtk_obj.GetNumberOfTimeSteps()
    number_of_time_steps = traits.Property(_get_number_of_time_steps, help=\
        """
        Get the number of time steps
        """
    )

    def set_selection_connection(self, *args):
        """
        V.set_selection_connection(AlgorithmOutput)
        C++: void SetSelectionConnection(AlgorithmOutput *algOutput)
        Convenience method to specify the selection connection (2nd input
        port)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSelectionConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('report_statistics_only', 'GetReportStatisticsOnly'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'report_statistics_only', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractArraysOverTime, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractArraysOverTime properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['report_statistics_only'], [], []),
            title='Edit ExtractArraysOverTime properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractArraysOverTime properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


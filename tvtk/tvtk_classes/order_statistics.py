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

from tvtk.tvtk_classes.statistics_algorithm import StatisticsAlgorithm


class OrderStatistics(StatisticsAlgorithm):
    """
    OrderStatistics - A class for univariate order statistics
    
    Superclass: StatisticsAlgorithm
    
    Given a selection of columns of interest in an input data table, this
    class provides the following functionalities, depending on the
    execution mode it is executed in:
    * Learn: calculate histogram.
    * Derive: calculate PDFs and arbitrary quantiles. Provide specific
      names when 5-point statistics (minimum, 1st quartile, median, third
    quartile, maximum) requested.
    * Assess: given an input data set and a set of q-quantiles, label
      each datum either with the quantile interval to which it belongs,
      or 0 if it is smaller than smaller quantile, or q if it is larger
      than largest quantile.
    * Test: calculate Kolmogorov-Smirnov goodness-of-fit statistic
      between CDF based on model quantiles, and empirical CDF
    
    @par Thanks: Thanks to Philippe Pebay and David Thompson from Sandia
    National Laboratories for implementing this class. Updated by
    Philippe Pebay, Kitware SAS 2012
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOrderStatistics, obj, update, **traits)
    
    maximum_histogram_size = traits.Int(1000, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum histogram size. This maximum size is enforced
        only when Quantize is TRUE.
        """
    )

    def _maximum_histogram_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumHistogramSize,
                        self.maximum_histogram_size)

    number_of_intervals = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of quantiles (with uniform spacing).
        """
    )

    def _number_of_intervals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfIntervals,
                        self.number_of_intervals)

    quantile_definition = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the quantile definition.
        """
    )

    def _quantile_definition_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuantileDefinition,
                        self.quantile_definition)

    quantize = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Set/Get whether quantization will be allowed to enforce maximum
        histogram size.
        """
    )

    def _quantize_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuantize,
                        self.quantize)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_histogram_size', 'GetMaximumHistogramSize'),
    ('number_of_intervals', 'GetNumberOfIntervals'),
    ('quantile_definition', 'GetQuantileDefinition'), ('quantize',
    'GetQuantize'), ('assess_option', 'GetAssessOption'),
    ('derive_option', 'GetDeriveOption'), ('learn_option',
    'GetLearnOption'), ('number_of_primary_tables',
    'GetNumberOfPrimaryTables'), ('test_option', 'GetTestOption'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'assess_option', 'derive_option', 'learn_option',
    'maximum_histogram_size', 'number_of_intervals',
    'number_of_primary_tables', 'progress_text', 'quantile_definition',
    'quantize', 'test_option'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OrderStatistics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OrderStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['assess_option', 'derive_option', 'learn_option',
            'maximum_histogram_size', 'number_of_intervals',
            'number_of_primary_tables', 'quantile_definition', 'quantize',
            'test_option']),
            title='Edit OrderStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OrderStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


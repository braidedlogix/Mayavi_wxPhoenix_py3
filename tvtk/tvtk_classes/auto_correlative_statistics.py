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


class AutoCorrelativeStatistics(StatisticsAlgorithm):
    """
    AutoCorrelativeStatistics - A class for univariate
    auto-correlative statistics
    
    Superclass: StatisticsAlgorithm
    
    Given a selection of columns of interest in an input data table, this
    class provides the following functionalities, depending on the chosen
    execution options:
    * Learn: calculate sample mean and M2 aggregates for each variable
      w.r.t. itself (cf. P. Pebay, Formulas for robust, one-pass parallel
    computation of covariances and Arbitrary-Order Statistical Moments,
      Sandia Report SAND2008-6212, Sep 2008,
      http://infoserve.sandia.gov/sand_doc/2008/086212.pdf for details)
      for each specified time lag.
    * Derive: calculate unbiased autocovariance matrix estimators and its
    determinant, linear regressions, and Pearson correlation coefficient,
    for each specified time lag.
    * Assess: given an input data set, two means and a 2x2 covariance
      matrix, mark each datum with corresponding relative deviation
      (2-dimensional Mahlanobis distance).
    
    @par Thanks: This class was written by Philippe Pebay, Kitware SAS
    2012
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAutoCorrelativeStatistics, obj, update, **traits)
    
    slice_cardinality = traits.Trait(0, traits.Range(0, 9223372036854775807, enter_set=True, auto_set=False), help=\
        """
        Set/get the cardinality of the data set at given time, i.e., of
        any given time slice. It cannot be negative. The input data set
        is assumed to have a cardinality which is a multiple of this
        value. The default is 0, meaning that the user must specify a
        value that is consistent with the input data set.
        """
    )

    def _slice_cardinality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceCardinality,
                        self.slice_cardinality)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('slice_cardinality', 'GetSliceCardinality'), ('assess_option',
    'GetAssessOption'), ('derive_option', 'GetDeriveOption'),
    ('learn_option', 'GetLearnOption'), ('number_of_primary_tables',
    'GetNumberOfPrimaryTables'), ('test_option', 'GetTestOption'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'assess_option', 'derive_option', 'learn_option',
    'number_of_primary_tables', 'progress_text', 'slice_cardinality',
    'test_option'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AutoCorrelativeStatistics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AutoCorrelativeStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['assess_option', 'derive_option', 'learn_option',
            'number_of_primary_tables', 'slice_cardinality', 'test_option']),
            title='Edit AutoCorrelativeStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AutoCorrelativeStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


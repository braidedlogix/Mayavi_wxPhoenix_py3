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


class MultiCorrelativeStatistics(StatisticsAlgorithm):
    """
    MultiCorrelativeStatistics - A class for multivariate linear
    correlation
    
    Superclass: StatisticsAlgorithm
    
    Given a selection of sets of columns of interest, this class provides
    the following functionalities, depending on the operation in which it
    is executed:
    * Learn: calculates means, unbiased variance and covariance
      estimators of column pairs coefficient. More precisely, Learn
      calculates the averages and centered variance/covariance sums; if
      finalize is set to true (default), the final statistics are
      calculated. The output metadata on port OUTPUT_MODEL is a
      multiblock dataset containing at a minimum one Table holding the
    raw sums in a sparse matrix style. If finalize is true, then one
      additional Table will be present for each requested set of
      column correlations. These additional tables contain column
      averages, the upper triangular portion of the covariance matrix (in
    the upper right hand portion of the table) and the Cholesky
      decomposition of the covariance matrix (in the lower portion of the
    table beneath the covariance triangle). The leftmost column will be a
    vector of column averages. The last entry in the column averages
      vector is the number of samples. As an example, consider a request
      for a 3-column correlation with columns named col_a, col_b, and col_c.
      The resulting table will look like this:
    
    
         Column  |Mean     |_col_a     |_col_b     |_col_c
    --------+---------+---------+---------+--------- col_a    |avg(A)  
        |cov(A,A) |cov(A,B) |cov(A,C) col_b    |avg(B)  
        |chol(1,1)|cov(B,B) |cov(B,C) col_c    |avg(C)  
        |chol(2,1)|chol(2,2)|cov(C,C)
        Cholesky|length(A)|chol(3,1)|chol(3,2)|chol(3,3)  The mean point
        and the covariance matrix can be replaced by the median point and
    the MAD matrix (Median Absolute Deviation) thanks to the
        median_absolute_deviation boolean. In this mode, the resulting
        table will look like this:
    
    
         Column  |Mean     |_col_a     |_col_b     |_col_c
    --------+---------+---------+---------+--------- col_a    |med(A)  
        |MAD(A,A) |MAD(A,B) |MAD(A,C) col_b    |med(B)  
        |chol(1,1)|MAD(B,B) |MAD(B,C) col_c    |med(C)  
        |chol(2,1)|chol(2,2)|MAD(C,C)
        Cholesky|length(A)|chol(3,1)|chol(3,2)|chol(3,3)  The Median
        Absolute Deviation is known to be more robust than the
        covariance. It is used in the robust PCA computation for
        instance.
    * Assess: given a set of results matrices as specified above in input
    port INPUT_MODEL and tabular data on input port INPUT_DATA that
      contains column names matching those of the tables on input port
      INPUT_MODEL, the assess mode computes the relative deviation of
      each observation in port INPUT_DATA's table according to the linear
      correlations implied by each table in port INPUT_MODEL.
    
    @par Thanks: Thanks to Philippe Pebay, Jackson Mayo, and David
    Thompson of Sandia National Laboratories for implementing this class.
    Updated by Philippe Pebay, Kitware SAS 2012 Updated by Tristan
    Coulange and Joachim Pouderoux, Kitware SAS 2013
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMultiCorrelativeStatistics, obj, update, **traits)
    
    median_absolute_deviation = tvtk_base.false_bool_trait(help=\
        """
        If set to true, the covariance matrix is replaced by the Median
        Absolute Deviation matrix. Default is false.
        """
    )

    def _median_absolute_deviation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMedianAbsoluteDeviation,
                        self.median_absolute_deviation_)

    _updateable_traits_ = \
    (('median_absolute_deviation', 'GetMedianAbsoluteDeviation'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('assess_option', 'GetAssessOption'), ('derive_option',
    'GetDeriveOption'), ('learn_option', 'GetLearnOption'),
    ('number_of_primary_tables', 'GetNumberOfPrimaryTables'),
    ('test_option', 'GetTestOption'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'median_absolute_deviation', 'release_data_flag', 'assess_option',
    'derive_option', 'learn_option', 'number_of_primary_tables',
    'progress_text', 'test_option'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MultiCorrelativeStatistics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MultiCorrelativeStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['median_absolute_deviation'], [], ['assess_option',
            'derive_option', 'learn_option', 'number_of_primary_tables',
            'test_option']),
            title='Edit MultiCorrelativeStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MultiCorrelativeStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class ContingencyStatistics(StatisticsAlgorithm):
    """
    ContingencyStatistics - A class for bivariate correlation
    contigency tables, conditional probabilities, and information entropy
    
    Superclass: StatisticsAlgorithm
    
    Given a pair of columns of interest, this class provides the
    following functionalities, depending on the operation in which it is
    executed:
    * Learn: calculate contigency tables and corresponding discrete joint
      probability distribution.
    * Derive: calculate conditional probabilities, information entropies,
    and pointwise mutual information.
    * Assess: given two columns of interest with the same number of
      entries as input in port INPUT_DATA, and a corresponding bivariate
      probability distribution,
    * Test: calculate Chi-square independence statistic and, if VTK to R
      interface is available, retrieve corresponding p-value for
      independence testing.
    
    @par Thanks: Thanks to Philippe Pebay and David Thompson from Sandia
    National Laboratories for implementing this class. Updated by
    Philippe Pebay, Kitware SAS 2012
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContingencyStatistics, obj, update, **traits)
    
    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
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
    'release_data_flag', 'assess_option', 'derive_option', 'learn_option',
    'number_of_primary_tables', 'progress_text', 'test_option'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContingencyStatistics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ContingencyStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['assess_option', 'derive_option', 'learn_option',
            'number_of_primary_tables', 'test_option']),
            title='Edit ContingencyStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContingencyStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


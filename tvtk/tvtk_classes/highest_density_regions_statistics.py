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


class HighestDensityRegionsStatistics(StatisticsAlgorithm):
    """
    HighestDensityRegionsStatistics - Compute a random vector of
    density f from input observations points.
    
    Superclass: StatisticsAlgorithm
    
    f is computed using a smooth kernel method.
    
    Given a selection of pairs of columns of interest, this class
    provides the following functionalities, depending on the chosen
    execution options:
    * Learn: calculates density estimator f of a random vector using a
      smooth gaussian kernel. The output metadata on port OUTPUT_MODEL is
    a multiblock dataset containing at one Table holding three columns
    which are for the first columns the input columns of interest and for
    the last columns the density estimators of each input pair of columns
    of interest.
    * Derive: calculate normalized (as a percentage) quantiles coming
      from Learn output. The second block of the multibloc dataset
      contains a Table holding some pairs of columns which are for the
    second one the quantiles ordered from the stronger to the lower and
      for the first one the correspondand quantile index.
    * Assess: not implemented.
    * Test: not implemented.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHighestDensityRegionsStatistics, obj, update, **traits)
    
    def compute_hdr(self, *args):
        """
        V.compute_hdr(DataArray, DataArray) -> float
        C++: double ComputeHDR(DataArray *inObservations,
            DataArray *outDensity)
        V.compute_hdr(DataArray, DataArray, DataArray) -> float
        C++: double ComputeHDR(DataArray *inObs, DataArray *inPOI,
            DataArray *outDensity)
        Fill out_density with density vector that is computed from
        in_observations values. This method uses a Gaussian kernel. For n
        observations and with X an observation point: f(X) = (1 / n) *
        Sum(KH(X -Xi)) for (i = 1 to n). Look compute_smooth_gaussian_kernel
        for KH kernel definition.
        """
        my_args = deref_array(args, [('vtkDataArray', 'vtkDataArray'), ('vtkDataArray', 'vtkDataArray', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.ComputeHDR, *my_args)
        return ret

    def set_sigma(self, *args):
        """
        V.set_sigma(float)
        C++: void SetSigma(double sigma)
        Set the width of the gaussian kernel.
        """
        ret = self._wrap_call(self._vtk_obj.SetSigma, *args)
        return ret

    def set_sigma_matrix(self, *args):
        """
        V.set_sigma_matrix(float, float, float, float)
        C++: void SetSigmaMatrix(double s11, double s12, double s21,
            double s22)
        Set the gaussian kernel matrix.
        """
        ret = self._wrap_call(self._vtk_obj.SetSigmaMatrix, *args)
        return ret

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
            return super(HighestDensityRegionsStatistics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HighestDensityRegionsStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['assess_option', 'derive_option', 'learn_option',
            'number_of_primary_tables', 'test_option']),
            title='Edit HighestDensityRegionsStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HighestDensityRegionsStatistics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


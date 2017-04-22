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


class PairwiseExtractHistogram2D(StatisticsAlgorithm):
    """
    PairwiseExtractHistogram2D - compute a 2d histogram between
     all adjacent columns of an input Table.
    
    Superclass: StatisticsAlgorithm
    
    This class computes a 2d histogram between all adjacent pairs of
    columns
     of an input Table. Internally it creates multiple
    ExtractHistogram2D
     instances (one for each pair of adjacent table columns).  It also
     manages updating histogram computations intelligently, only
    recomputing
     those histograms for whom a relevant property has been altered.
    
    
     Note that there are two different outputs from this filter.  One is
    a
     table for which each column contains a flattened 2d histogram array.
     The other is a MultiBlockDataSet for which each block is a
     ImageData representation of the 2d histogram.
    
    @sa
     ExtractHistogram2D PPairwiseExtractHistogram2D
    
    @par Thanks:
     Developed by David Feng and Philippe Pebay at Sandia National
    Laboratories
    ----------------------------------------------------------------------
        --------
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPairwiseExtractHistogram2D, obj, update, **traits)
    
    scalar_type = traits.Trait('unsigned_int',
    tvtk_base.TraitRevPrefixMap({'unsigned_int': 7, 'unsigned_char': 3, 'unsigned_long': 9, 'unsigned_short': 5}), help=\
        """
        Set the scalar type for each of the computed histograms.
        """
    )

    def _scalar_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarType,
                        self.scalar_type_)

    number_of_bins = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _number_of_bins_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfBins,
                        self.number_of_bins)

    def get_bin_range(self, *args):
        """
        V.get_bin_range(int, int, int, [float, float, float, float]) -> int
        C++: int GetBinRange(int idx, IdType binX, IdType binY,
            double range[4])
        V.get_bin_range(int, int, [float, float, float, float]) -> int
        C++: int GetBinRange(int idx, IdType bin, double range[4])
        Compute the range of the bin located at position (bin_x,bin_y) in
        the 2d histogram at idx.
        """
        ret = self._wrap_call(self._vtk_obj.GetBinRange, *args)
        return ret

    def get_bin_width(self, *args):
        """
        V.get_bin_width(int, [float, float])
        C++: void GetBinWidth(int idx, double bw[2])
        Get the width of all of the bins. Also stored in the spacing ivar
        of the histogram image output at idx.
        """
        ret = self._wrap_call(self._vtk_obj.GetBinWidth, *args)
        return ret

    def get_histogram_extents(self, *args):
        """
        V.get_histogram_extents(int) -> (float, ...)
        C++: double *GetHistogramExtents(int idx)
        Get the histogram extents currently in use, either computed or
        set by the user for the idx'th histogram.
        """
        ret = self._wrap_call(self._vtk_obj.GetHistogramExtents, *args)
        return ret

    def get_histogram_filter(self, *args):
        """
        V.get_histogram_filter(int) -> ExtractHistogram2D
        C++: ExtractHistogram2D *GetHistogramFilter(int idx)
        Get a pointer to the idx'th histogram filter.
        """
        ret = self._wrap_call(self._vtk_obj.GetHistogramFilter, *args)
        return wrap_vtk(ret)

    def _get_maximum_bin_count(self):
        return self._vtk_obj.GetMaximumBinCount()
    maximum_bin_count = traits.Property(_get_maximum_bin_count, help=\
        """
        Get the maximum bin count for a single histogram
        """
    )

    def get_output_histogram_image(self, *args):
        """
        V.get_output_histogram_image(int) -> ImageData
        C++: ImageData *GetOutputHistogramImage(int idx)
        Get the ImageData output of the idx'th histogram filter
        """
        ret = self._wrap_call(self._vtk_obj.GetOutputHistogramImage, *args)
        return wrap_vtk(ret)

    def set_custom_column_range(self, *args):
        """
        V.set_custom_column_range(int, [float, float])
        C++: void SetCustomColumnRange(int col, double range[2])
        V.set_custom_column_range(int, float, float)
        C++: void SetCustomColumnRange(int col, double rmin, double rmax)
        More standard way to set the custom range for a particular
        column. This makes sure that only the affected histograms know
        that they need to be updated.
        """
        ret = self._wrap_call(self._vtk_obj.SetCustomColumnRange, *args)
        return ret

    def set_custom_column_range_by_index(self, *args):
        """
        V.set_custom_column_range_by_index(float, float)
        C++: void SetCustomColumnRangeByIndex(double, double)
        Strange method for setting an index to be used for setting custom
        column range. This was (probably) necessary to get this class to
        interact with the para_view client/server message passing
        interface.
        """
        ret = self._wrap_call(self._vtk_obj.SetCustomColumnRangeByIndex, *args)
        return ret

    def set_custom_column_range_index(self, *args):
        """
        V.set_custom_column_range_index(int)
        C++: void SetCustomColumnRangeIndex(int a)
        Strange method for setting an index to be used for setting custom
        column range. This was (probably) necessary to get this class to
        interact with the para_view client/server message passing
        interface.
        """
        ret = self._wrap_call(self._vtk_obj.SetCustomColumnRangeIndex, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('scalar_type',
    'GetScalarType'), ('number_of_bins', 'GetNumberOfBins'),
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
    'release_data_flag', 'scalar_type', 'assess_option', 'derive_option',
    'learn_option', 'number_of_bins', 'number_of_primary_tables',
    'progress_text', 'test_option'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PairwiseExtractHistogram2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PairwiseExtractHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['scalar_type'], ['assess_option', 'derive_option',
            'learn_option', 'number_of_bins', 'number_of_primary_tables',
            'test_option']),
            title='Edit PairwiseExtractHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PairwiseExtractHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


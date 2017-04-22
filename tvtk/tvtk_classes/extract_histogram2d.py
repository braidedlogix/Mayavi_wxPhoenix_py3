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


class ExtractHistogram2D(StatisticsAlgorithm):
    """
    ExtractHistogram2D - compute a 2d histogram between two columns
     of an input Table.
    
    Superclass: StatisticsAlgorithm
    
    This class computes a 2d histogram between two columns of an input
     Table. Just as with a 1d histogram, a 2d histogram breaks
     up the input domain into bins, and each pair of values (row in
     the table) fits into a single bin and increments a row counter
     for that bin.
    
    
     To use this class, set the input with a table and call
    add_column_pair(name_x,name_y),
     where name_x and name_y are the names of the two columns to be used.
    
    
     In addition to the number of bins (in X and Y), the domain of
     the histogram can be customized by toggling the
    use_custom_histogram_extents
     flag and setting the custom_histogram_extents variable to the
     desired value.
    
    @sa
     PExtractHistogram2D
    
    @par Thanks:
     Developed by David Feng and Philippe Pebay at Sandia National
    Laboratories
    ----------------------------------------------------------------------
        --------
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractHistogram2D, obj, update, **traits)
    
    swap_columns = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _swap_columns_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSwapColumns,
                        self.swap_columns_)

    use_custom_histogram_extents = tvtk_base.false_bool_trait(help=\
        """
        Use the extents in custom_histogram_extents when computing the
        histogram, rather than the simple range of the input columns.
        """
    )

    def _use_custom_histogram_extents_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseCustomHistogramExtents,
                        self.use_custom_histogram_extents_)

    scalar_type = traits.Trait('unsigned_int',
    tvtk_base.TraitRevPrefixMap({'unsigned_int': 7, 'double': 11, 'float': 10, 'unsigned_char': 3, 'unsigned_long': 9, 'unsigned_short': 5}), help=\
        """
        Control the scalar type of the output histogram.  If the input is
        relatively small, you can save space by using a smaller data
        type.  Defaults to unsigned integer.
        """
    )

    def _scalar_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarType,
                        self.scalar_type_)

    components_to_process = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _components_to_process_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponentsToProcess,
                        self.components_to_process)

    custom_histogram_extents = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _custom_histogram_extents_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCustomHistogramExtents,
                        self.custom_histogram_extents)

    number_of_bins = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _number_of_bins_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfBins,
                        self.number_of_bins)

    def _get_row_mask(self):
        return wrap_vtk(self._vtk_obj.GetRowMask())
    def _set_row_mask(self, arg):
        old_val = self._get_row_mask()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetRowMask,
                        my_arg[0])
        self.trait_property_changed('row_mask', old_val, arg)
    row_mask = traits.Property(_get_row_mask, _set_row_mask, help=\
        """
        Get/Set an optional mask that can ignore rows of the table
        """
    )

    def get_bin_range(self, *args):
        """
        V.get_bin_range(int, int, [float, float, float, float]) -> int
        C++: int GetBinRange(IdType binX, IdType binY,
            double range[4])
        V.get_bin_range(int, [float, float, float, float]) -> int
        C++: int GetBinRange(IdType bin, double range[4])
        Compute the range of the bin located at position (bin_x,bin_y) in
        the 2d histogram.
        """
        ret = self._wrap_call(self._vtk_obj.GetBinRange, *args)
        return ret

    def get_bin_width(self, *args):
        """
        V.get_bin_width([float, float])
        C++: void GetBinWidth(double bw[2])
        Get the width of all of the bins. Also stored in the spacing ivar
        of the histogram image output.
        """
        ret = self._wrap_call(self._vtk_obj.GetBinWidth, *args)
        return ret

    def _get_histogram_extents(self):
        return self._vtk_obj.GetHistogramExtents()
    histogram_extents = traits.Property(_get_histogram_extents, help=\
        """
        Get the histogram extents currently in use, either computed or
        set by the user.
        """
    )

    def _get_maximum_bin_count(self):
        return self._vtk_obj.GetMaximumBinCount()
    maximum_bin_count = traits.Property(_get_maximum_bin_count, help=\
        """
        Access the count of the histogram bin containing the largest
        number of input rows.
        """
    )

    def _get_output_histogram_image(self):
        return wrap_vtk(self._vtk_obj.GetOutputHistogramImage())
    output_histogram_image = traits.Property(_get_output_histogram_image, help=\
        """
        Gets the data object at the histogram image output port and casts
        it to a ImageData.
        """
    )

    _updateable_traits_ = \
    (('swap_columns', 'GetSwapColumns'), ('use_custom_histogram_extents',
    'GetUseCustomHistogramExtents'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('scalar_type',
    'GetScalarType'), ('components_to_process', 'GetComponentsToProcess'),
    ('custom_histogram_extents', 'GetCustomHistogramExtents'),
    ('number_of_bins', 'GetNumberOfBins'), ('assess_option',
    'GetAssessOption'), ('derive_option', 'GetDeriveOption'),
    ('learn_option', 'GetLearnOption'), ('number_of_primary_tables',
    'GetNumberOfPrimaryTables'), ('test_option', 'GetTestOption'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'swap_columns', 'use_custom_histogram_extents',
    'scalar_type', 'assess_option', 'components_to_process',
    'custom_histogram_extents', 'derive_option', 'learn_option',
    'number_of_bins', 'number_of_primary_tables', 'progress_text',
    'test_option'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractHistogram2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['swap_columns', 'use_custom_histogram_extents'],
            ['scalar_type'], ['assess_option', 'components_to_process',
            'custom_histogram_extents', 'derive_option', 'learn_option',
            'number_of_bins', 'number_of_primary_tables', 'test_option']),
            title='Edit ExtractHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


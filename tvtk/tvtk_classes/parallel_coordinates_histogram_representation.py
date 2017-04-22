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

from tvtk.tvtk_classes.parallel_coordinates_representation import ParallelCoordinatesRepresentation


class ParallelCoordinatesHistogramRepresentation(ParallelCoordinatesRepresentation):
    """
    ParallelCoordinatesHistogramRepresentation - Data representation
     that takes generic multivariate data and produces a parallel
    coordinates plot.
    
    Superclass: ParallelCoordinatesRepresentation
    
    This plot optionally can draw a histogram-based plot summary.
    
    
     A parallel coordinates plot represents each variable in a
    multivariate
     data set as a separate axis.  Individual samples of that data set
    are
     represented as a polyline that pass through each variable axis at
     positions that correspond to data values.  This class can generate
     parallel coordinates plots identical to its superclass
     (vtk_parallel_coordinates_representation) and has the same interaction
     styles.
    
    
     In addition to the standard parallel coordinates plot, this class
    also
     can draw a histogram summary of the parallel coordinates plot.
     Rather than draw every row in an input data set, first it computes
     a 2d histogram for all neighboring variable axes, then it draws
     bar (thickness corresponds to bin size) for each bin the histogram
     with opacity weighted by the number of rows contained in the bin.
     The result is essentially a density map.
    
    
     Because this emphasizes dense regions over sparse outliers, this
    class
     also uses a ComputeHistogram2DOutliers instance to identify
    outlier
     table rows and draws those as standard parallel coordinates lines.
    
    @sa
     ParallelCoordinatesView ParallelCoordinatesRepresentation
     ExtractHistogram2D ComputeHistogram2DOutliers
    
    @par Thanks:
     Developed by David Feng at Sandia National Laboratories
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParallelCoordinatesHistogramRepresentation, obj, update, **traits)
    
    show_outliers = tvtk_base.false_bool_trait(help=\
        """
        Whether to compute and show outlier lines
        """
    )

    def _show_outliers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowOutliers,
                        self.show_outliers_)

    use_histograms = tvtk_base.false_bool_trait(help=\
        """
        Whether to use the histogram rendering mode or the superclass's
        line rendering mode
        """
    )

    def _use_histograms_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseHistograms,
                        self.use_histograms_)

    histogram_lookup_table_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 10.0), cols=2, help=\
        """
        
        """
    )

    def _histogram_lookup_table_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHistogramLookupTableRange,
                        self.histogram_lookup_table_range)

    number_of_histogram_bins = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(10, 10), cols=2, help=\
        """
        The number of histogram bins on either side of each pair of axes.
        """
    )

    def _number_of_histogram_bins_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfHistogramBins,
                        self.number_of_histogram_bins)

    preferred_number_of_outliers = traits.Int(100, enter_set=True, auto_set=False, help=\
        """
        Target maximum number of outliers to be drawn, although not
        guaranteed.
        """
    )

    def _preferred_number_of_outliers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreferredNumberOfOutliers,
                        self.preferred_number_of_outliers)

    def get_range_at_position(self, *args):
        """
        V.get_range_at_position(int, [float, float]) -> int
        C++: int GetRangeAtPosition(int position, double range[2])
        Set/get the value range of the axis at a particular screen
        position
        """
        ret = self._wrap_call(self._vtk_obj.GetRangeAtPosition, *args)
        return ret

    def set_range_at_position(self, *args):
        """
        V.set_range_at_position(int, [float, float]) -> int
        C++: virtual int SetRangeAtPosition(int position, double range[2])
        Calls the superclass method, and assures that only the two
        histograms affect by this call get recomputed.
        """
        ret = self._wrap_call(self._vtk_obj.SetRangeAtPosition, *args)
        return ret

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    _updateable_traits_ = \
    (('show_outliers', 'GetShowOutliers'), ('use_histograms',
    'GetUseHistograms'), ('use_curves', 'GetUseCurves'), ('selectable',
    'GetSelectable'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('histogram_lookup_table_range', 'GetHistogramLookupTableRange'),
    ('number_of_histogram_bins', 'GetNumberOfHistogramBins'),
    ('preferred_number_of_outliers', 'GetPreferredNumberOfOutliers'),
    ('angle_brush_threshold', 'GetAngleBrushThreshold'), ('axis_color',
    'GetAxisColor'), ('axis_label_color', 'GetAxisLabelColor'),
    ('curve_resolution', 'GetCurveResolution'), ('font_size',
    'GetFontSize'), ('function_brush_threshold',
    'GetFunctionBrushThreshold'), ('line_color', 'GetLineColor'),
    ('line_opacity', 'GetLineOpacity'), ('number_of_axis_labels',
    'GetNumberOfAxisLabels'), ('label_render_mode', 'GetLabelRenderMode'),
    ('selection_array_name', 'GetSelectionArrayName'), ('selection_type',
    'GetSelectionType'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'selectable', 'show_outliers', 'use_curves',
    'use_histograms', 'angle_brush_threshold', 'axis_color',
    'axis_label_color', 'curve_resolution', 'font_size',
    'function_brush_threshold', 'histogram_lookup_table_range',
    'label_render_mode', 'line_color', 'line_opacity',
    'number_of_axis_labels', 'number_of_histogram_bins',
    'preferred_number_of_outliers', 'progress_text',
    'selection_array_name', 'selection_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParallelCoordinatesHistogramRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ParallelCoordinatesHistogramRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['selectable', 'show_outliers', 'use_curves', 'use_histograms'],
            [], ['angle_brush_threshold', 'axis_color', 'axis_label_color',
            'curve_resolution', 'font_size', 'function_brush_threshold',
            'histogram_lookup_table_range', 'label_render_mode', 'line_color',
            'line_opacity', 'number_of_axis_labels', 'number_of_histogram_bins',
            'preferred_number_of_outliers', 'selection_array_name',
            'selection_type']),
            title='Edit ParallelCoordinatesHistogramRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParallelCoordinatesHistogramRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


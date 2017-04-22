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

from tvtk.tvtk_classes.chart_xy import ChartXY


class ChartHistogram2D(ChartXY):
    """
    ChartHistogram2D - no description provided.
    
    Superclass: ChartXY
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkChartHistogram2D, obj, update, **traits)
    
    def set_input_data(self, *args):
        """
        V.set_input_data(ImageData, int)
        C++: virtual void SetInputData(ImageData *data, IdType z=0)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    def set_transfer_function(self, *args):
        """
        V.set_transfer_function(ScalarsToColors)
        C++: virtual void SetTransferFunction(
            ScalarsToColors *function)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTransferFunction, *my_args)
        return ret

    _updateable_traits_ = \
    (('adjust_lower_bound_for_log_plot', 'GetAdjustLowerBoundForLogPlot'),
    ('auto_axes', 'GetAutoAxes'), ('draw_axes_at_origin',
    'GetDrawAxesAtOrigin'), ('force_axes_to_bounds',
    'GetForceAxesToBounds'), ('zoom_with_mouse_wheel',
    'GetZoomWithMouseWheel'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('bar_width_fraction', 'GetBarWidthFraction'), ('hidden_axis_border',
    'GetHiddenAxisBorder'), ('selection_method', 'GetSelectionMethod'),
    ('show_legend', 'GetShowLegend'), ('auto_size', 'GetAutoSize'),
    ('geometry', 'GetGeometry'), ('layout_strategy', 'GetLayoutStrategy'),
    ('point1', 'GetPoint1'), ('point2', 'GetPoint2'), ('render_empty',
    'GetRenderEmpty'), ('selection_mode', 'GetSelectionMode'), ('title',
    'GetTitle'), ('opacity', 'GetOpacity'), ('interactive',
    'GetInteractive'), ('visible', 'GetVisible'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['adjust_lower_bound_for_log_plot', 'auto_axes', 'debug',
    'draw_axes_at_origin', 'force_axes_to_bounds',
    'global_warning_display', 'zoom_with_mouse_wheel', 'auto_size',
    'bar_width_fraction', 'geometry', 'hidden_axis_border', 'interactive',
    'layout_strategy', 'opacity', 'point1', 'point2', 'render_empty',
    'selection_method', 'selection_mode', 'show_legend', 'title',
    'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ChartHistogram2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ChartHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['adjust_lower_bound_for_log_plot', 'auto_axes',
            'draw_axes_at_origin', 'force_axes_to_bounds',
            'zoom_with_mouse_wheel'], [], ['auto_size', 'bar_width_fraction',
            'geometry', 'hidden_axis_border', 'interactive', 'layout_strategy',
            'opacity', 'point1', 'point2', 'render_empty', 'selection_method',
            'selection_mode', 'show_legend', 'title', 'visible']),
            title='Edit ChartHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ChartHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


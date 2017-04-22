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

from tvtk.tvtk_classes.plot_points import PlotPoints


class PlotLine(PlotPoints):
    """
    PlotLine - Class for drawing an XY line plot given two columns
    from a Table.
    
    Superclass: PlotPoints
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlotLine, obj, update, **traits)
    
    poly_line = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off flag to control whether the points define a poly line
        (true) or multiple line segments (false). If true (default), a
        segment is drawn between each points (e.g. [_p1p2, p2p3,
        p3p4...].) If false, a segment is drawn for each pair of points
        (e.g. [_p1p2, p3p4,...].)
        """
    )

    def _poly_line_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolyLine,
                        self.poly_line_)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input table used by the plot.
        """
    )

    _updateable_traits_ = \
    (('poly_line', 'GetPolyLine'), ('scalar_visibility',
    'GetScalarVisibility'), ('legend_visibility', 'GetLegendVisibility'),
    ('selectable', 'GetSelectable'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('marker_size',
    'GetMarkerSize'), ('marker_style', 'GetMarkerStyle'),
    ('valid_point_mask_name', 'GetValidPointMaskName'), ('label',
    'GetLabel'), ('tooltip_label_format', 'GetTooltipLabelFormat'),
    ('tooltip_notation', 'GetTooltipNotation'), ('tooltip_precision',
    'GetTooltipPrecision'), ('use_index_for_x_series',
    'GetUseIndexForXSeries'), ('width', 'GetWidth'), ('opacity',
    'GetOpacity'), ('interactive', 'GetInteractive'), ('visible',
    'GetVisible'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'legend_visibility', 'poly_line',
    'scalar_visibility', 'selectable', 'interactive', 'label',
    'marker_size', 'marker_style', 'opacity', 'tooltip_label_format',
    'tooltip_notation', 'tooltip_precision', 'use_index_for_x_series',
    'valid_point_mask_name', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlotLine, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PlotLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['legend_visibility', 'poly_line', 'scalar_visibility',
            'selectable'], [], ['interactive', 'label', 'marker_size',
            'marker_style', 'opacity', 'tooltip_label_format', 'tooltip_notation',
            'tooltip_precision', 'use_index_for_x_series',
            'valid_point_mask_name', 'visible', 'width']),
            title='Edit PlotLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlotLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


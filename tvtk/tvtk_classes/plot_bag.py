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


class PlotBag(PlotPoints):
    """
    PlotBag - Class for drawing an a bagplot.
    
    Superclass: PlotPoints
    
    This class allows to draw a bagplot given three columns from a
    Table. The first two columns will represent X,Y as it is for
    PlotPoints. The third one will have to specify if the density
    assigned to each point (generally obtained by the
    HighestDensityRegionsStatistics filter). Points are drawn in a
    plot points fashion and 2 convex hull polygons are drawn around the
    median and the 3 quartile of the density field.
    
    @sa
    HighestDensityRegionsStatistics
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlotBag, obj, update, **traits)
    
    bag_visible = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Set/get the visibility of the bags. True by default.
        """
    )

    def _bag_visible_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBagVisible,
                        self.bag_visible)

    def _get_labels(self):
        return wrap_vtk(self._vtk_obj.GetLabels())
    def _set_labels(self, arg):
        old_val = self._get_labels()
        my_arg = deref_array([arg], [['vtkStringArray']])
        self._wrap_call(self._vtk_obj.SetLabels,
                        my_arg[0])
        self.trait_property_changed('labels', old_val, arg)
    labels = traits.Property(_get_labels, _set_labels, help=\
        """
        Get the plot labels. If this array has a length greater than 1
        the index refers to the stacked objects in the plot. See
        PlotBar for example.
        """
    )

    def _get_line_pen(self):
        return wrap_vtk(self._vtk_obj.GetLinePen())
    def _set_line_pen(self, arg):
        old_val = self._get_line_pen()
        self._wrap_call(self._vtk_obj.SetLinePen,
                        deref_vtk(arg))
        self.trait_property_changed('line_pen', old_val, arg)
    line_pen = traits.Property(_get_line_pen, _set_line_pen, help=\
        """
        Set/get the Pen object that controls how this plot draws
        boundary lines.
        """
    )

    def _get_point_pen(self):
        return wrap_vtk(self._vtk_obj.GetPointPen())
    def _set_point_pen(self, arg):
        old_val = self._get_point_pen()
        self._wrap_call(self._vtk_obj.SetPointPen,
                        deref_vtk(arg))
        self.trait_property_changed('point_pen', old_val, arg)
    point_pen = traits.Property(_get_point_pen, _set_point_pen, help=\
        """
        
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input table used by the plot.
        """
    )

    _updateable_traits_ = \
    (('scalar_visibility', 'GetScalarVisibility'), ('legend_visibility',
    'GetLegendVisibility'), ('selectable', 'GetSelectable'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('bag_visible', 'GetBagVisible'), ('marker_size', 'GetMarkerSize'),
    ('marker_style', 'GetMarkerStyle'), ('valid_point_mask_name',
    'GetValidPointMaskName'), ('label', 'GetLabel'),
    ('tooltip_label_format', 'GetTooltipLabelFormat'),
    ('tooltip_notation', 'GetTooltipNotation'), ('tooltip_precision',
    'GetTooltipPrecision'), ('use_index_for_x_series',
    'GetUseIndexForXSeries'), ('width', 'GetWidth'), ('opacity',
    'GetOpacity'), ('interactive', 'GetInteractive'), ('visible',
    'GetVisible'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'legend_visibility',
    'scalar_visibility', 'selectable', 'bag_visible', 'interactive',
    'label', 'marker_size', 'marker_style', 'opacity',
    'tooltip_label_format', 'tooltip_notation', 'tooltip_precision',
    'use_index_for_x_series', 'valid_point_mask_name', 'visible',
    'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlotBag, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PlotBag properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['legend_visibility', 'scalar_visibility', 'selectable'], [],
            ['bag_visible', 'interactive', 'label', 'marker_size', 'marker_style',
            'opacity', 'tooltip_label_format', 'tooltip_notation',
            'tooltip_precision', 'use_index_for_x_series',
            'valid_point_mask_name', 'visible', 'width']),
            title='Edit PlotBag properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlotBag properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


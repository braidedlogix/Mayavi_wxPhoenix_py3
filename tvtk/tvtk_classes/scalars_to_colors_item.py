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

from tvtk.tvtk_classes.plot import Plot


class ScalarsToColorsItem(Plot):
    """
    ScalarsToColorsItem - Abstract class for scalars_to_colors items.
    
    Superclass: Plot
    
    ScalarsToColorsItem implements item bounds and painting for
    inherited classes that provide a texture (_compute_texture()) and
    optionally a shape
    @sa
    ControlPointsItem LookupTableItem ColorTransferFunctionItem
    CompositeTransferFunctionItem PiecewiseItemFunctionItem
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScalarsToColorsItem, obj, update, **traits)
    
    mask_above_curve = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Don't fill in the part above the transfer function. If true
        texture is not visible above the shape provided by subclasses,
        otherwise the whole rectangle defined by the bounds is filled
        with the transfer function. Note: only 2d transfer functions (RGB
        tf + alpha tf ) support the feature.
        """
    )

    def _mask_above_curve_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaskAboveCurve,
                        self.mask_above_curve)

    user_bounds = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, -1.0, 0.0, -1.0), cols=3, help=\
        """
        
        """
    )

    def _user_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUserBounds,
                        self.user_bounds)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input table used by the plot.
        """
    )

    def _get_poly_line_pen(self):
        return wrap_vtk(self._vtk_obj.GetPolyLinePen())
    poly_line_pen = traits.Property(_get_poly_line_pen, help=\
        """
        Get a pointer to the Pen object that controls the drawing of
        the edge of the shape if any. poly_line_pen type is Pen::NO_PEN
        by default.
        """
    )

    _updateable_traits_ = \
    (('legend_visibility', 'GetLegendVisibility'), ('selectable',
    'GetSelectable'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('mask_above_curve', 'GetMaskAboveCurve'),
    ('user_bounds', 'GetUserBounds'), ('label', 'GetLabel'),
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
    'selectable', 'interactive', 'label', 'mask_above_curve', 'opacity',
    'tooltip_label_format', 'tooltip_notation', 'tooltip_precision',
    'use_index_for_x_series', 'user_bounds', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScalarsToColorsItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ScalarsToColorsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['legend_visibility', 'selectable'], [], ['interactive',
            'label', 'mask_above_curve', 'opacity', 'tooltip_label_format',
            'tooltip_notation', 'tooltip_precision', 'use_index_for_x_series',
            'user_bounds', 'visible', 'width']),
            title='Edit ScalarsToColorsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScalarsToColorsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


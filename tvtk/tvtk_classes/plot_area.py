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


class PlotArea(Plot):
    """
    PlotArea - draws an area plot.
    
    Superclass: Plot
    
    PlotArea is used to render an area plot. An area plot (sometimes
    called a range plot) renders a filled region between the selected
    ymin and ymax arrays. To specify the x array and ymin/ymax arrays,
    use the set_input_array method with array index as 0, 1, or 2,
    respectively.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlotArea, obj, update, **traits)
    
    def get_color(self, *args):
        """
        V.get_color([float, float, float])
        C++: virtual void GetColor(double rgb[3])
        V.get_color([int, int, int])
        C++: void GetColor(unsigned char rgb[3])
        Set the plot color
        """
        ret = self._wrap_call(self._vtk_obj.GetColor, *args)
        return ret

    def set_color(self, *args):
        """
        V.set_color(int, int, int, int)
        C++: virtual void SetColor(unsigned char r, unsigned char g,
            unsigned char b, unsigned char a)
        V.set_color(float, float, float)
        C++: virtual void SetColor(double r, double g, double b)
        Overridden to set the brush color.
        """
        ret = self._wrap_call(self._vtk_obj.SetColor, *args)
        return ret

    valid_point_mask_name = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Get/set the valid point mask array name.
        """
    )

    def _valid_point_mask_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValidPointMaskName,
                        self.valid_point_mask_name)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input table used by the plot.
        """
    )

    _updateable_traits_ = \
    (('legend_visibility', 'GetLegendVisibility'), ('selectable',
    'GetSelectable'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('valid_point_mask_name',
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
    'selectable', 'interactive', 'label', 'opacity',
    'tooltip_label_format', 'tooltip_notation', 'tooltip_precision',
    'use_index_for_x_series', 'valid_point_mask_name', 'visible',
    'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlotArea, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PlotArea properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['legend_visibility', 'selectable'], [], ['interactive',
            'label', 'opacity', 'tooltip_label_format', 'tooltip_notation',
            'tooltip_precision', 'use_index_for_x_series',
            'valid_point_mask_name', 'visible', 'width']),
            title='Edit PlotArea properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlotArea properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


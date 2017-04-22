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

from tvtk.tvtk_classes.chart_legend import ChartLegend


class ColorLegend(ChartLegend):
    """
    ColorLegend - Legend item to display ScalarsToColors.
    
    Superclass: ChartLegend
    
    ColorLegend is an item that will display the ScalarsToColors
    using a 1d texture, and a Axis to show both the color and
    numerical range.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkColorLegend, obj, update, **traits)
    
    draw_border = tvtk_base.false_bool_trait(help=\
        """
        Toggle whether or not a border should be drawn around this
        legend. The default behavior is to not draw a border.
        """
    )

    def _draw_border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawBorder,
                        self.draw_border_)

    orientation = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get the orientation of the legend. Valid orientations are
        VERTICAL (default) and HORIZONTAL.
        """
    )

    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation)

    point = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 0.0), cols=2, help=\
        """
        Set the point this legend is anchored to.
        """
    )

    def _point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint,
                        self.point)

    title = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Get/set the title text of the legend.
        """
    )

    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    def _get_transfer_function(self):
        return wrap_vtk(self._vtk_obj.GetTransferFunction())
    def _set_transfer_function(self, arg):
        old_val = self._get_transfer_function()
        self._wrap_call(self._vtk_obj.SetTransferFunction,
                        deref_vtk(arg))
        self.trait_property_changed('transfer_function', old_val, arg)
    transfer_function = traits.Property(_get_transfer_function, _set_transfer_function, help=\
        """
        Set/Get the transfer function that is used to draw the scalar bar
        within this legend.
        """
    )

    def get_bounds(self, *args):
        """
        V.get_bounds([float, float, float, float])
        C++: virtual void GetBounds(double bounds[4])
        Bounds of the item, by default (0, 1, 0, 1) but it mainly depends
        on the range of the ScalarsToColors function.
        """
        ret = self._wrap_call(self._vtk_obj.GetBounds, *args)
        return ret

    def set_texture_size(self, *args):
        """
        V.set_texture_size(float, float)
        C++: virtual void SetTextureSize(float w, float h)
        Set the size of the scalar bar drawn by this legend.
        """
        ret = self._wrap_call(self._vtk_obj.SetTextureSize, *args)
        return ret

    _updateable_traits_ = \
    (('draw_border', 'GetDrawBorder'), ('cache_bounds', 'GetCacheBounds'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('orientation', 'GetOrientation'),
    ('point', 'GetPoint'), ('title', 'GetTitle'), ('drag_enabled',
    'GetDragEnabled'), ('horizontal_alignment', 'GetHorizontalAlignment'),
    ('inline', 'GetInline'), ('label_size', 'GetLabelSize'), ('padding',
    'GetPadding'), ('symbol_width', 'GetSymbolWidth'),
    ('vertical_alignment', 'GetVerticalAlignment'), ('opacity',
    'GetOpacity'), ('interactive', 'GetInteractive'), ('visible',
    'GetVisible'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['cache_bounds', 'debug', 'draw_border', 'global_warning_display',
    'drag_enabled', 'horizontal_alignment', 'inline', 'interactive',
    'label_size', 'opacity', 'orientation', 'padding', 'point',
    'symbol_width', 'title', 'vertical_alignment', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ColorLegend, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ColorLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['cache_bounds', 'draw_border'], [], ['drag_enabled',
            'horizontal_alignment', 'inline', 'interactive', 'label_size',
            'opacity', 'orientation', 'padding', 'point', 'symbol_width', 'title',
            'vertical_alignment', 'visible']),
            title='Edit ColorLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ColorLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


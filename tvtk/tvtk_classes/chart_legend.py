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

from tvtk.tvtk_classes.context_item import ContextItem


class ChartLegend(ContextItem):
    """
    ChartLegend - draw the chart legend
    
    Superclass: ContextItem
    
    The ChartLegend is drawn in screen coordinates. It is usually one
    of the last elements of a chart to be drawn. It renders the the
    mark/line for each plot, and the plot labels.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkChartLegend, obj, update, **traits)
    
    cache_bounds = tvtk_base.true_bool_trait(help=\
        """
        Toggle whether or not this legend should attempt to cache its
        position and size.  The default value is true.  If this value is
        set to false, the legend will recalculate its position and bounds
        every time it is drawn.  If users will be able to zoom in or out
        on your legend, you may want to set this to false.  Otherwise,
        the border around the legend may not resize appropriately.
        """
    )

    def _cache_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCacheBounds,
                        self.cache_bounds_)

    def _get_chart(self):
        return wrap_vtk(self._vtk_obj.GetChart())
    def _set_chart(self, arg):
        old_val = self._get_chart()
        self._wrap_call(self._vtk_obj.SetChart,
                        deref_vtk(arg))
        self.trait_property_changed('chart', old_val, arg)
    chart = traits.Property(_get_chart, _set_chart, help=\
        """
        Get the chart that the legend belongs to and will draw the legend
        for.
        """
    )

    drag_enabled = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Get/set if the legend can be dragged with the mouse button, or
        not. True results in left click and drag causing the legend to
        move around the scene. False disables response to mouse events.
        The default is true.
        """
    )

    def _drag_enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDragEnabled,
                        self.drag_enabled)

    horizontal_alignment = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set the horizontal alignment of the legend to the point
        specified. Valid values are LEFT, CENTER and RIGHT.
        """
    )

    def _horizontal_alignment_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHorizontalAlignment,
                        self.horizontal_alignment)

    inline = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Get/set if the legend should be drawn inline (inside the chart),
        or not. True would generally request that the chart draws it
        inside the chart, false would adjust the chart axes and make
        space to draw the axes outside.
        """
    )

    def _inline_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInline,
                        self.inline)

    label_size = traits.Int(12, enter_set=True, auto_set=False, help=\
        """
        Set the point size of the label text.
        """
    )

    def _label_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelSize,
                        self.label_size)

    padding = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        Set the padding between legend marks, default is 5.
        """
    )

    def _padding_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPadding,
                        self.padding)

    point = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 0.0), cols=2, help=\
        """
        
        """
    )

    def _point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint,
                        self.point)

    symbol_width = traits.Int(25, enter_set=True, auto_set=False, help=\
        """
        Set the symbol width, default is 15.
        """
    )

    def _symbol_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSymbolWidth,
                        self.symbol_width)

    vertical_alignment = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Set the vertical alignment of the legend to the point specified.
        Valid values are TOP, CENTER and BOTTOM.
        """
    )

    def _vertical_alignment_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVerticalAlignment,
                        self.vertical_alignment)

    def get_bounding_rect(self, *args):
        """
        V.get_bounding_rect(Context2D) -> Rectf
        C++: virtual Rectf GetBoundingRect(Context2D *painter)
        Request the space the legend requires to be drawn. This is
        returned as a Rect4f, with the corner being the offset from
        Point, and the width/ height being the total width/height
        required by the axis. In order to ensure the numbers are correct,
        Update() should be called first.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetBoundingRect, *my_args)
        return wrap_vtk(ret)

    def _get_brush(self):
        return wrap_vtk(self._vtk_obj.GetBrush())
    brush = traits.Property(_get_brush, help=\
        """
        Get the brush used to draw the legend background.
        """
    )

    def _get_label_properties(self):
        return wrap_vtk(self._vtk_obj.GetLabelProperties())
    label_properties = traits.Property(_get_label_properties, help=\
        """
        Get the TextProperty for the legend's labels.
        """
    )

    def _get_pen(self):
        return wrap_vtk(self._vtk_obj.GetPen())
    pen = traits.Property(_get_pen, help=\
        """
        Get the pen used to draw the legend outline.
        """
    )

    def _get_point_vector(self):
        return wrap_vtk(self._vtk_obj.GetPointVector())
    point_vector = traits.Property(_get_point_vector, help=\
        """
        Get point the legend box is anchored to.
        """
    )

    _updateable_traits_ = \
    (('cache_bounds', 'GetCacheBounds'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('drag_enabled', 'GetDragEnabled'), ('horizontal_alignment',
    'GetHorizontalAlignment'), ('inline', 'GetInline'), ('label_size',
    'GetLabelSize'), ('padding', 'GetPadding'), ('point', 'GetPoint'),
    ('symbol_width', 'GetSymbolWidth'), ('vertical_alignment',
    'GetVerticalAlignment'), ('opacity', 'GetOpacity'), ('interactive',
    'GetInteractive'), ('visible', 'GetVisible'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['cache_bounds', 'debug', 'global_warning_display', 'drag_enabled',
    'horizontal_alignment', 'inline', 'interactive', 'label_size',
    'opacity', 'padding', 'point', 'symbol_width', 'vertical_alignment',
    'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ChartLegend, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ChartLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['cache_bounds'], [], ['drag_enabled', 'horizontal_alignment',
            'inline', 'interactive', 'label_size', 'opacity', 'padding', 'point',
            'symbol_width', 'vertical_alignment', 'visible']),
            title='Edit ChartLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ChartLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


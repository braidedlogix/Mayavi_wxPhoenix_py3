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


class CategoryLegend(ChartLegend):
    """
    CategoryLegend - Legend item to display categorical data.
    
    Superclass: ChartLegend
    
    CategoryLegend will display a label and color patch for each value
    in a categorical data set.  To use this class, you must first
    populate a ScalarsToColors by using the set_annotation() method. 
    The other input to this class is a VariantArray.  This should
    contain the annotated values from the ScalarsToColors that you
    wish to include within the legend.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCategoryLegend, obj, update, **traits)
    
    outlier_label = traits.String('outliers', enter_set=True, auto_set=False, help=\
        """
        Get/set the label to use for outlier data.
        """
    )

    def _outlier_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutlierLabel,
                        self.outlier_label)

    def _get_scalars_to_colors(self):
        return wrap_vtk(self._vtk_obj.GetScalarsToColors())
    def _set_scalars_to_colors(self, arg):
        old_val = self._get_scalars_to_colors()
        self._wrap_call(self._vtk_obj.SetScalarsToColors,
                        deref_vtk(arg))
        self.trait_property_changed('scalars_to_colors', old_val, arg)
    scalars_to_colors = traits.Property(_get_scalars_to_colors, _set_scalars_to_colors, help=\
        """
        Get/Set the ScalarsToColors used to draw this legend. Since
        this legend represents categorical data, this ScalarsToColors
        must have been populated using set_annotation().
        """
    )

    title = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Get/set the title text of the legend.
        """
    )

    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    def _get_values(self):
        return wrap_vtk(self._vtk_obj.GetValues())
    def _set_values(self, arg):
        old_val = self._get_values()
        my_arg = deref_array([arg], [['vtkVariantArray']])
        self._wrap_call(self._vtk_obj.SetValues,
                        my_arg[0])
        self.trait_property_changed('values', old_val, arg)
    values = traits.Property(_get_values, _set_values, help=\
        """
        Get/Set the array of values that will be represented by this
        legend. This array must contain distinct annotated values from
        the scalars_to_colors. Each value in this array will be drawn as a
        separate entry within this legend.
        """
    )

    _updateable_traits_ = \
    (('cache_bounds', 'GetCacheBounds'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('outlier_label', 'GetOutlierLabel'), ('title', 'GetTitle'),
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
    'opacity', 'outlier_label', 'padding', 'point', 'symbol_width',
    'title', 'vertical_alignment', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CategoryLegend, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CategoryLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['cache_bounds'], [], ['drag_enabled', 'horizontal_alignment',
            'inline', 'interactive', 'label_size', 'opacity', 'outlier_label',
            'padding', 'point', 'symbol_width', 'title', 'vertical_alignment',
            'visible']),
            title='Edit CategoryLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CategoryLegend properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


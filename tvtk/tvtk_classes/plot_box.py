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


class PlotBox(Plot):
    """
    PlotBox - Class for drawing box plots.
    
    Superclass: Plot
    
    Plots to draw box plots given columns from a Table that may
    contains 5 lines with quartiles and median.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlotBox, obj, update, **traits)
    
    box_width = traits.Float(20.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the width of boxes.
        """
    )

    def _box_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoxWidth,
                        self.box_width)

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
        the index refers to the stacked objects in the plot.
        """
    )

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Specify a lookup table for the mapper to use.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input table used by the plot.
        """
    )

    def _get_title_properties(self):
        return wrap_vtk(self._vtk_obj.GetTitleProperties())
    title_properties = traits.Property(_get_title_properties, help=\
        """
        Get the TextProperty that governs how the plot title is
        displayed.
        """
    )

    def create_default_lookup_table(self):
        """
        V.create_default_lookup_table()
        C++: virtual void CreateDefaultLookupTable()
        Create default lookup table. Generally used to create one when
        none is available with the scalar data.
        """
        ret = self._vtk_obj.CreateDefaultLookupTable()
        return ret
        

    def set_column_color(self, *args):
        """
        V.set_column_color(string, [float, ...])
        C++: void SetColumnColor(const StdString &colName, double *rgb)
        Helper function to set the color of a given column.
        """
        ret = self._wrap_call(self._vtk_obj.SetColumnColor, *args)
        return ret

    _updateable_traits_ = \
    (('legend_visibility', 'GetLegendVisibility'), ('selectable',
    'GetSelectable'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('box_width', 'GetBoxWidth'), ('label',
    'GetLabel'), ('tooltip_label_format', 'GetTooltipLabelFormat'),
    ('tooltip_notation', 'GetTooltipNotation'), ('tooltip_precision',
    'GetTooltipPrecision'), ('use_index_for_x_series',
    'GetUseIndexForXSeries'), ('width', 'GetWidth'), ('opacity',
    'GetOpacity'), ('interactive', 'GetInteractive'), ('visible',
    'GetVisible'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'legend_visibility',
    'selectable', 'box_width', 'interactive', 'label', 'opacity',
    'tooltip_label_format', 'tooltip_notation', 'tooltip_precision',
    'use_index_for_x_series', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlotBox, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PlotBox properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['legend_visibility', 'selectable'], [], ['box_width',
            'interactive', 'label', 'opacity', 'tooltip_label_format',
            'tooltip_notation', 'tooltip_precision', 'use_index_for_x_series',
            'visible', 'width']),
            title='Edit PlotBox properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlotBox properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class PlotPoints(Plot):
    """
    PlotPoints - Class for drawing an points given two columns from a
    Table.
    
    Superclass: Plot
    
    This class draws points in a plot given two columns from a table. If
    you need a line as well you should use PlotLine which derives from
    PlotPoints and is capable of drawing both points and a line.
    
    @sa
    PlotLine
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlotPoints, obj, update, **traits)
    
    scalar_visibility = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off flag to control whether scalar data is used to color
        objects.
        """
    )

    def _scalar_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarVisibility,
                        self.scalar_visibility_)

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

    marker_size = traits.Float(-1.0, enter_set=True, auto_set=False, help=\
        """
        Get/set the marker size that should be used. The default is
        negative, and in that case it is 2.3 times the pen width, if less
        than 8 will be used.
        """
    )

    def _marker_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMarkerSize,
                        self.marker_size)

    marker_style = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        Get/set the marker style that should be used. The default is
        none, the enum in this class is used as a parameter.
        """
    )

    def _marker_style_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMarkerStyle,
                        self.marker_style)

    valid_point_mask_name = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Get/set the valid point mask array name.
        """
    )

    def _valid_point_mask_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValidPointMaskName,
                        self.valid_point_mask_name)

    def _get_color_array_name(self):
        return self._vtk_obj.GetColorArrayName()
    color_array_name = traits.Property(_get_color_array_name, help=\
        """
        Get the array name to color by.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input table used by the plot.
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
        

    def select_color_array(self, *args):
        """
        V.select_color_array(int)
        C++: void SelectColorArray(IdType arrayNum)
        V.select_color_array(string)
        C++: void SelectColorArray(const StdString &arrayName)
        When scalar_mode is set to use_point_field_data or use_cell_field_data,
        you can specify which array to use for coloring using these
        methods. The lookup table will decide how to convert vectors to
        colors.
        """
        ret = self._wrap_call(self._vtk_obj.SelectColorArray, *args)
        return ret

    _updateable_traits_ = \
    (('scalar_visibility', 'GetScalarVisibility'), ('legend_visibility',
    'GetLegendVisibility'), ('selectable', 'GetSelectable'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('marker_size', 'GetMarkerSize'), ('marker_style', 'GetMarkerStyle'),
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
    (['debug', 'global_warning_display', 'legend_visibility',
    'scalar_visibility', 'selectable', 'interactive', 'label',
    'marker_size', 'marker_style', 'opacity', 'tooltip_label_format',
    'tooltip_notation', 'tooltip_precision', 'use_index_for_x_series',
    'valid_point_mask_name', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlotPoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PlotPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['legend_visibility', 'scalar_visibility', 'selectable'], [],
            ['interactive', 'label', 'marker_size', 'marker_style', 'opacity',
            'tooltip_label_format', 'tooltip_notation', 'tooltip_precision',
            'use_index_for_x_series', 'valid_point_mask_name', 'visible',
            'width']),
            title='Edit PlotPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlotPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


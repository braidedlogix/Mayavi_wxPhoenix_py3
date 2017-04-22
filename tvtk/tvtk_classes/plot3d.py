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


class Plot3D(ContextItem):
    """
    Plot3D - Abstract class for 3d plots.
    
    Superclass: ContextItem
    
    The base class for all plot types used in Chart derived charts.
    
    @sa
    Plot3DPoints Plot3DLine Plot3DBar Chart ChartXY
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlot3D, obj, update, **traits)
    
    def _get_chart(self):
        return wrap_vtk(self._vtk_obj.GetChart())
    def _set_chart(self, arg):
        old_val = self._get_chart()
        self._wrap_call(self._vtk_obj.SetChart,
                        deref_vtk(arg))
        self.trait_property_changed('chart', old_val, arg)
    chart = traits.Property(_get_chart, _set_chart, help=\
        """
        Get/set the chart for this plot.
        """
    )

    def _get_pen(self):
        return wrap_vtk(self._vtk_obj.GetPen())
    def _set_pen(self, arg):
        old_val = self._get_pen()
        self._wrap_call(self._vtk_obj.SetPen,
                        deref_vtk(arg))
        self.trait_property_changed('pen', old_val, arg)
    pen = traits.Property(_get_pen, _set_pen, help=\
        """
        Set/get the Pen object that controls how this plot draws
        (out)lines.
        """
    )

    def _get_selection(self):
        return wrap_vtk(self._vtk_obj.GetSelection())
    def _set_selection(self, arg):
        old_val = self._get_selection()
        my_arg = deref_array([arg], [['vtkIdTypeArray']])
        self._wrap_call(self._vtk_obj.SetSelection,
                        my_arg[0])
        self.trait_property_changed('selection', old_val, arg)
    selection = traits.Property(_get_selection, _set_selection, help=\
        """
        Set/get the selection array for the plot.
        """
    )

    def _get_selection_pen(self):
        return wrap_vtk(self._vtk_obj.GetSelectionPen())
    def _set_selection_pen(self, arg):
        old_val = self._get_selection_pen()
        self._wrap_call(self._vtk_obj.SetSelectionPen,
                        deref_vtk(arg))
        self.trait_property_changed('selection_pen', old_val, arg)
    selection_pen = traits.Property(_get_selection_pen, _set_selection_pen, help=\
        """
        Set/get the Pen object that controls how this plot draws
        (out)lines.
        """
    )

    def _get_x_axis_label(self):
        return self._vtk_obj.GetXAxisLabel()
    x_axis_label = traits.Property(_get_x_axis_label, help=\
        """
        Get the label for the X axis.
        """
    )

    def _get_y_axis_label(self):
        return self._vtk_obj.GetYAxisLabel()
    y_axis_label = traits.Property(_get_y_axis_label, help=\
        """
        Get the label for the Y axis.
        """
    )

    def _get_z_axis_label(self):
        return self._vtk_obj.GetZAxisLabel()
    z_axis_label = traits.Property(_get_z_axis_label, help=\
        """
        Get the label for the Z axis.
        """
    )

    def set_colors(self, *args):
        """
        V.set_colors(DataArray)
        C++: virtual void SetColors(DataArray *colorArr)
        Set the color of each point in the plot.  The input is a single
        component scalar array.  The values of this array will be passed
        through a lookup table to generate the color for each data point
        in the plot.
        """
        my_args = deref_array(args, [['vtkDataArray']])
        ret = self._wrap_call(self._vtk_obj.SetColors, *my_args)
        return ret

    def set_input_data(self, *args):
        """
        V.set_input_data(Table)
        C++: virtual void SetInputData(Table *input)
        V.set_input_data(Table, string, string, string)
        C++: virtual void SetInputData(Table *input,
            const StdString &xName, const StdString &yName,
            const StdString &zName)
        V.set_input_data(Table, string, string, string, string)
        C++: virtual void SetInputData(Table *input,
            const StdString &xName, const StdString &yName,
            const StdString &zName, const StdString &colorName)
        V.set_input_data(Table, int, int, int)
        C++: virtual void SetInputData(Table *input, IdType xColumn,
             IdType yColumn, IdType zColumn)
        Set the input to the plot.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('opacity', 'GetOpacity'), ('interactive',
    'GetInteractive'), ('visible', 'GetVisible'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'interactive', 'opacity',
    'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Plot3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Plot3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['interactive', 'opacity', 'visible']),
            title='Edit Plot3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Plot3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


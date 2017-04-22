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

from tvtk.tvtk_classes.control_points_item import ControlPointsItem


class ColorTransferControlPointsItem(ControlPointsItem):
    """
    ColorTransferControlPointsItem - Control points for
    ColorTransferFunction.
    
    Superclass: ControlPointsItem
    
    ColorTransferControlPointsItem draws the control points of a
    ColorTransferFunction.
    @sa
    ControlPointsItem ColorTransferFunctionItem
    CompositeTransferFunctionItem
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkColorTransferControlPointsItem, obj, update, **traits)
    
    color_fill = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        If color_fill is true, the control point brush color is set with
        the matching color in the color transfer function. False by
        default.
        """
    )

    def _color_fill_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorFill,
                        self.color_fill)

    def _get_color_transfer_function(self):
        return wrap_vtk(self._vtk_obj.GetColorTransferFunction())
    def _set_color_transfer_function(self, arg):
        old_val = self._get_color_transfer_function()
        self._wrap_call(self._vtk_obj.SetColorTransferFunction,
                        deref_vtk(arg))
        self.trait_property_changed('color_transfer_function', old_val, arg)
    color_transfer_function = traits.Property(_get_color_transfer_function, _set_color_transfer_function, help=\
        """
        Get the piecewise function
        """
    )

    def get_control_point(self, *args):
        """
        V.get_control_point(int, [float, ...])
        C++: virtual void GetControlPoint(IdType index, double *point)
        Returns the x and y coordinates as well as the midpoint and
        sharpness of the control point corresponding to the index. Note:
        The y (point[1]) is always 0.5
        """
        ret = self._wrap_call(self._vtk_obj.GetControlPoint, *args)
        return ret

    def set_control_point(self, *args):
        """
        V.set_control_point(int, [float, ...])
        C++: virtual void SetControlPoint(IdType index, double *point)
        Sets the x and y coordinates as well as the midpoint and
        sharpness of the control point corresponding to the index.
        Changing the y has no effect, it will always be 0.5
        """
        ret = self._wrap_call(self._vtk_obj.SetControlPoint, *args)
        return ret

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
    'GetGlobalWarningDisplay'), ('color_fill', 'GetColorFill'),
    ('current_point', 'GetCurrentPoint'), ('end_points_removable',
    'GetEndPointsRemovable'), ('end_points_x_movable',
    'GetEndPointsXMovable'), ('end_points_y_movable',
    'GetEndPointsYMovable'), ('label_format', 'GetLabelFormat'),
    ('screen_point_radius', 'GetScreenPointRadius'), ('show_labels',
    'GetShowLabels'), ('switch_points_mode', 'GetSwitchPointsMode'),
    ('user_bounds', 'GetUserBounds'), ('valid_bounds', 'GetValidBounds'),
    ('label', 'GetLabel'), ('tooltip_label_format',
    'GetTooltipLabelFormat'), ('tooltip_notation', 'GetTooltipNotation'),
    ('tooltip_precision', 'GetTooltipPrecision'),
    ('use_index_for_x_series', 'GetUseIndexForXSeries'), ('width',
    'GetWidth'), ('opacity', 'GetOpacity'), ('interactive',
    'GetInteractive'), ('visible', 'GetVisible'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'legend_visibility',
    'selectable', 'color_fill', 'current_point', 'end_points_removable',
    'end_points_x_movable', 'end_points_y_movable', 'interactive',
    'label', 'label_format', 'opacity', 'screen_point_radius',
    'show_labels', 'switch_points_mode', 'tooltip_label_format',
    'tooltip_notation', 'tooltip_precision', 'use_index_for_x_series',
    'user_bounds', 'valid_bounds', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ColorTransferControlPointsItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ColorTransferControlPointsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['legend_visibility', 'selectable'], [], ['color_fill',
            'current_point', 'end_points_removable', 'end_points_x_movable',
            'end_points_y_movable', 'interactive', 'label', 'label_format',
            'opacity', 'screen_point_radius', 'show_labels', 'switch_points_mode',
            'tooltip_label_format', 'tooltip_notation', 'tooltip_precision',
            'use_index_for_x_series', 'user_bounds', 'valid_bounds', 'visible',
            'width']),
            title='Edit ColorTransferControlPointsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ColorTransferControlPointsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


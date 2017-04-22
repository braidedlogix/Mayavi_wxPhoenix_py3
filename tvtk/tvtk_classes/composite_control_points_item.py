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

from tvtk.tvtk_classes.color_transfer_control_points_item import ColorTransferControlPointsItem


class CompositeControlPointsItem(ColorTransferControlPointsItem):
    """
    CompositeControlPointsItem - Control points for
    CompositeFunction.
    
    Superclass: ColorTransferControlPointsItem
    
    CompositeControlPointsItem draws the control points of a
    PiecewiseFunction and a ColorTransferFunction.
    @sa
    ControlPointsItem ColorTransferControlPointsItem
    CompositeTransferFunctionItem PiecewisePointHandleItem
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCompositeControlPointsItem, obj, update, **traits)
    
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

    def _get_opacity_function(self):
        return wrap_vtk(self._vtk_obj.GetOpacityFunction())
    def _set_opacity_function(self, arg):
        old_val = self._get_opacity_function()
        self._wrap_call(self._vtk_obj.SetOpacityFunction,
                        deref_vtk(arg))
        self.trait_property_changed('opacity_function', old_val, arg)
    opacity_function = traits.Property(_get_opacity_function, _set_opacity_function, help=\
        """
        Utility function that calls set_piecewise_function()
        """
    )

    points_function = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        points_function controls wether the points represent the
        color_transfer_function, opacity_transfer_function or both. If
        color_points_function, only the points of the color_transfer
        function are used. If opacity_points_function, only the points of
        the Opacity function are used If color_and_opacity_points_function,
        the points of both functions are shared by both functions.
        color_and_opacity_points_function by default. Note: Set the mode
        before the functions are set. color_points_function is not fully
        supported.
        """
    )

    def _points_function_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointsFunction,
                        self.points_function)

    use_opacity_point_handles = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        If use_opacity_point_handles is true, when the current point is
        double clicked, a PiecewisePointHandleItem will show up so
        that the sharpness and mid point can be adjusted in the scene
        with those handles False by default.
        """
    )

    def _use_opacity_point_handles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseOpacityPointHandles,
                        self.use_opacity_point_handles)

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
    'GetGlobalWarningDisplay'), ('points_function', 'GetPointsFunction'),
    ('use_opacity_point_handles', 'GetUseOpacityPointHandles'),
    ('color_fill', 'GetColorFill'), ('current_point', 'GetCurrentPoint'),
    ('end_points_removable', 'GetEndPointsRemovable'),
    ('end_points_x_movable', 'GetEndPointsXMovable'),
    ('end_points_y_movable', 'GetEndPointsYMovable'), ('label_format',
    'GetLabelFormat'), ('screen_point_radius', 'GetScreenPointRadius'),
    ('show_labels', 'GetShowLabels'), ('switch_points_mode',
    'GetSwitchPointsMode'), ('user_bounds', 'GetUserBounds'),
    ('valid_bounds', 'GetValidBounds'), ('label', 'GetLabel'),
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
    'selectable', 'color_fill', 'current_point', 'end_points_removable',
    'end_points_x_movable', 'end_points_y_movable', 'interactive',
    'label', 'label_format', 'opacity', 'points_function',
    'screen_point_radius', 'show_labels', 'switch_points_mode',
    'tooltip_label_format', 'tooltip_notation', 'tooltip_precision',
    'use_index_for_x_series', 'use_opacity_point_handles', 'user_bounds',
    'valid_bounds', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CompositeControlPointsItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CompositeControlPointsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['legend_visibility', 'selectable'], [], ['color_fill',
            'current_point', 'end_points_removable', 'end_points_x_movable',
            'end_points_y_movable', 'interactive', 'label', 'label_format',
            'opacity', 'points_function', 'screen_point_radius', 'show_labels',
            'switch_points_mode', 'tooltip_label_format', 'tooltip_notation',
            'tooltip_precision', 'use_index_for_x_series',
            'use_opacity_point_handles', 'user_bounds', 'valid_bounds', 'visible',
            'width']),
            title='Edit CompositeControlPointsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CompositeControlPointsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


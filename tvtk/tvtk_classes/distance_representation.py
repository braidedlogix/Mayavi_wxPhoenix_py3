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

from tvtk.tvtk_classes.widget_representation import WidgetRepresentation


class DistanceRepresentation(WidgetRepresentation):
    """
    DistanceRepresentation - represent the DistanceWidget
    
    Superclass: WidgetRepresentation
    
    The DistanceRepresentation is a superclass for various types of
    representations for the DistanceWidget. Logically subclasses
    consist of an axis and two handles for placing/manipulating the end
    points.
    
    @sa
    DistanceWidget HandleRepresentation DistanceRepresentation2D
    DistanceRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDistanceRepresentation, obj, update, **traits)
    
    ruler_mode = tvtk_base.false_bool_trait(help=\
        """
        Enable or disable ruler mode. When enabled, the ticks on the
        distance widget are separated by the amount specified by
        ruler_distance. Otherwise, the ivar number_of_ruler_ticks is used to
        draw the tick marks.
        """
    )

    def _ruler_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRulerMode,
                        self.ruler_mode_)

    label_format = traits.String('%-#6.3g', enter_set=True, auto_set=False, help=\
        """
        Specify the format to use for labelling the distance. Note that
        an empty string results in no label, or a format string without a
        "%" character will not print the distance value.
        """
    )

    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    number_of_ruler_ticks = traits.Trait(5, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the number of major ruler ticks. This overrides any
        subclasses (e.g., DistanceRepresentation2D) that have
        alternative methods to specify the number of major ticks. Note:
        the number of ticks is the number between the two handle
        endpoints. This ivar only has effect when the ruler_mode is off.
        """
    )

    def _number_of_ruler_ticks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfRulerTicks,
                        self.number_of_ruler_ticks)

    def get_point1display_position(self, *args):
        """
        V.get_point1display_position([float, float, float])
        C++: virtual void GetPoint1DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint1DisplayPosition, *args)
        return ret

    def set_point1display_position(self, *args):
        """
        V.set_point1display_position([float, float, float])
        C++: virtual void SetPoint1DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint1DisplayPosition, *args)
        return ret

    point1_world_position = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
    )

    def _point1_world_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1WorldPosition,
                        self.point1_world_position)

    def get_point2display_position(self, *args):
        """
        V.get_point2display_position([float, float, float])
        C++: virtual void GetPoint2DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint2DisplayPosition, *args)
        return ret

    def set_point2display_position(self, *args):
        """
        V.set_point2display_position([float, float, float])
        C++: virtual void SetPoint2DisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint2DisplayPosition, *args)
        return ret

    point2_world_position = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
    )

    def _point2_world_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2WorldPosition,
                        self.point2_world_position)

    ruler_distance = traits.Trait(1.0, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Specify the ruler_distance which indicates the spacing of the
        major ticks. This ivar only has effect when the ruler_mode is on.
        """
    )

    def _ruler_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRulerDistance,
                        self.ruler_distance)

    scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the scale factor from VTK world coordinates. The ruler marks
        and label will be defined in terms of the scaled space. For
        example, if the VTK world coordinates are assumed to be in
        inches, but the desired distance units should be defined in terms
        of centimeters, the scale factor should be set to 2.54. The ruler
        marks will then be spaced in terms of centimeters, and the label
        will show the measurement in centimeters.
        """
    )

    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale)

    tolerance = traits.Trait(5, traits.Range(1, 100, enter_set=True, auto_set=False), help=\
        """
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered near enough to the end points
        of the widget to be active.
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def _get_distance(self):
        return self._vtk_obj.GetDistance()
    distance = traits.Property(_get_distance, help=\
        """
        This representation and all subclasses must keep a distance
        consistent with the state of the widget.
        """
    )

    def _get_point1_representation(self):
        return wrap_vtk(self._vtk_obj.GetPoint1Representation())
    point1_representation = traits.Property(_get_point1_representation, help=\
        """
        Set/Get the two handle representations used for the
        DistanceWidget. (Note: properties can be set by grabbing these
        representations and setting the properties appropriately.)
        """
    )

    def _get_point2_representation(self):
        return wrap_vtk(self._vtk_obj.GetPoint2Representation())
    point2_representation = traits.Property(_get_point2_representation, help=\
        """
        Set/Get the two handle representations used for the
        DistanceWidget. (Note: properties can be set by grabbing these
        representations and setting the properties appropriately.)
        """
    )

    def instantiate_handle_representation(self):
        """
        V.instantiate_handle_representation()
        C++: void InstantiateHandleRepresentation()
        This method is used to specify the type of handle representation
        to use for the two internal HandleWidgets within
        DistanceWidget. To use this method, create a dummy
        HandleWidget (or subclass), and then invoke this method with
        this dummy. Then the DistanceRepresentation uses this dummy to
        clone two HandleWidgets of the same type. Make sure you set
        the handle representation before the widget is enabled. (The
        method instantiate_handle_representation() is invoked by the
        Distance widget.)
        """
        ret = self._vtk_obj.InstantiateHandleRepresentation()
        return ret
        

    def set_handle_representation(self, *args):
        """
        V.set_handle_representation(HandleRepresentation)
        C++: void SetHandleRepresentation(HandleRepresentation *handle)
        This method is used to specify the type of handle representation
        to use for the two internal HandleWidgets within
        DistanceWidget. To use this method, create a dummy
        HandleWidget (or subclass), and then invoke this method with
        this dummy. Then the DistanceRepresentation uses this dummy to
        clone two HandleWidgets of the same type. Make sure you set
        the handle representation before the widget is enabled. (The
        method instantiate_handle_representation() is invoked by the
        Distance widget.)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetHandleRepresentation, *my_args)
        return ret

    _updateable_traits_ = \
    (('ruler_mode', 'GetRulerMode'), ('need_to_render',
    'GetNeedToRender'), ('picking_managed', 'GetPickingManaged'),
    ('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('label_format', 'GetLabelFormat'),
    ('number_of_ruler_ticks', 'GetNumberOfRulerTicks'), ('ruler_distance',
    'GetRulerDistance'), ('scale', 'GetScale'), ('tolerance',
    'GetTolerance'), ('handle_size', 'GetHandleSize'), ('place_factor',
    'GetPlaceFactor'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'picking_managed', 'ruler_mode', 'use_bounds',
    'visibility', 'estimated_render_time', 'handle_size', 'label_format',
    'number_of_ruler_ticks', 'place_factor', 'render_time_multiplier',
    'ruler_distance', 'scale', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DistanceRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DistanceRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['need_to_render', 'picking_managed', 'ruler_mode',
            'use_bounds', 'visibility'], [], ['estimated_render_time',
            'handle_size', 'label_format', 'number_of_ruler_ticks',
            'place_factor', 'render_time_multiplier', 'ruler_distance', 'scale',
            'tolerance']),
            title='Edit DistanceRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DistanceRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


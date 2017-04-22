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

from tvtk.tvtk_classes.slider_representation import SliderRepresentation


class SliderRepresentation3D(SliderRepresentation):
    """
    SliderRepresentation3D - provide the representation for a
    SliderWidget with a 3d skin
    
    Superclass: SliderRepresentation
    
    This class is used to represent and render a SliderWidget. To use
    this class, you must at a minimum specify the end points of the
    slider. Optional instance variable can be used to modify the
    appearance of the widget.
    
    @sa
    SliderWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSliderRepresentation3D, obj, update, **traits)
    
    slider_shape = traits.Trait('sphere',
    tvtk_base.TraitRevPrefixMap({'sphere': 0, 'cylinder': 1}), help=\
        """
        Specify whether to use a sphere or cylinder slider shape. By
        default, a sphere shape is used.
        """
    )

    def _slider_shape_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliderShape,
                        self.slider_shape_)

    rotation = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the rotation of the slider widget around the axis of the
        widget. This is used to control which way the widget is initially
        oriented. (This is especially important for the label and title.)
        """
    )

    def _rotation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRotation,
                        self.rotation)

    title_text = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Specify the title text for this widget. If the value is not set,
        or set to the empty string "", then the title text is not
        displayed.
        """
    )

    def _title_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitleText,
                        self.title_text)

    def _get_cap_property(self):
        return wrap_vtk(self._vtk_obj.GetCapProperty())
    cap_property = traits.Property(_get_cap_property, help=\
        """
        Get the properties for the tube and end caps.
        """
    )

    def _get_point1_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPoint1Coordinate())
    point1_coordinate = traits.Property(_get_point1_coordinate, help=\
        """
        Position the first end point of the slider. Note that this point
        is an instance of Coordinate, meaning that Point 1 can be
        specified in a variety of coordinate systems, and can even be
        relative to another point. To set the point, you'll want to get
        the point1_coordinate and then invoke the necessary methods to put
        it into the correct coordinate system and set the correct initial
        value.
        """
    )

    def _get_point2_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPoint2Coordinate())
    point2_coordinate = traits.Property(_get_point2_coordinate, help=\
        """
        Position the second end point of the slider. Note that this point
        is an instance of Coordinate, meaning that Point 1 can be
        specified in a variety of coordinate systems, and can even be
        relative to another point. To set the point, you'll want to get
        the point2_coordinate and then invoke the necessary methods to put
        it into the correct coordinate system and set the correct initial
        value.
        """
    )

    def _get_selected_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedProperty())
    selected_property = traits.Property(_get_selected_property, help=\
        """
        Get the selection property. This property is used to modify the
        appearance of selected objects (e.g., the slider).
        """
    )

    def _get_slider_property(self):
        return wrap_vtk(self._vtk_obj.GetSliderProperty())
    slider_property = traits.Property(_get_slider_property, help=\
        """
        Get the slider properties. The properties of the slider when
        selected and unselected can be manipulated.
        """
    )

    def _get_tube_property(self):
        return wrap_vtk(self._vtk_obj.GetTubeProperty())
    tube_property = traits.Property(_get_tube_property, help=\
        """
        Get the properties for the tube and end caps.
        """
    )

    def set_point1_in_world_coordinates(self, *args):
        """
        V.set_point1_in_world_coordinates(float, float, float)
        C++: void SetPoint1InWorldCoordinates(double x, double y,
            double z)
        Position the first end point of the slider. Note that this point
        is an instance of Coordinate, meaning that Point 1 can be
        specified in a variety of coordinate systems, and can even be
        relative to another point. To set the point, you'll want to get
        the point1_coordinate and then invoke the necessary methods to put
        it into the correct coordinate system and set the correct initial
        value.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint1InWorldCoordinates, *args)
        return ret

    def set_point2_in_world_coordinates(self, *args):
        """
        V.set_point2_in_world_coordinates(float, float, float)
        C++: void SetPoint2InWorldCoordinates(double x, double y,
            double z)
        Position the second end point of the slider. Note that this point
        is an instance of Coordinate, meaning that Point 1 can be
        specified in a variety of coordinate systems, and can even be
        relative to another point. To set the point, you'll want to get
        the point2_coordinate and then invoke the necessary methods to put
        it into the correct coordinate system and set the correct initial
        value.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint2InWorldCoordinates, *args)
        return ret

    _updateable_traits_ = \
    (('show_slider_label', 'GetShowSliderLabel'), ('need_to_render',
    'GetNeedToRender'), ('picking_managed', 'GetPickingManaged'),
    ('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('slider_shape', 'GetSliderShape'),
    ('rotation', 'GetRotation'), ('title_text', 'GetTitleText'),
    ('end_cap_length', 'GetEndCapLength'), ('end_cap_width',
    'GetEndCapWidth'), ('label_format', 'GetLabelFormat'),
    ('label_height', 'GetLabelHeight'), ('maximum_value',
    'GetMaximumValue'), ('minimum_value', 'GetMinimumValue'),
    ('slider_length', 'GetSliderLength'), ('slider_width',
    'GetSliderWidth'), ('title_height', 'GetTitleHeight'), ('tube_width',
    'GetTubeWidth'), ('value', 'GetValue'), ('handle_size',
    'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'picking_managed', 'show_slider_label', 'use_bounds',
    'visibility', 'slider_shape', 'end_cap_length', 'end_cap_width',
    'estimated_render_time', 'handle_size', 'label_format',
    'label_height', 'maximum_value', 'minimum_value', 'place_factor',
    'render_time_multiplier', 'rotation', 'slider_length', 'slider_width',
    'title_height', 'title_text', 'tube_width', 'value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SliderRepresentation3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SliderRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['need_to_render', 'picking_managed', 'show_slider_label',
            'use_bounds', 'visibility'], ['slider_shape'], ['end_cap_length',
            'end_cap_width', 'estimated_render_time', 'handle_size',
            'label_format', 'label_height', 'maximum_value', 'minimum_value',
            'place_factor', 'render_time_multiplier', 'rotation', 'slider_length',
            'slider_width', 'title_height', 'title_text', 'tube_width', 'value']),
            title='Edit SliderRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SliderRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


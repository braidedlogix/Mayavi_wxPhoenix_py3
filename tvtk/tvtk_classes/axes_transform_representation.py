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


class AxesTransformRepresentation(WidgetRepresentation):
    """
    AxesTransformRepresentation - represent the AxesTransformWidget
    
    Superclass: WidgetRepresentation
    
    The AxesTransformRepresentation is a representation for the
    AxesTransformWidget. This representation consists of a origin
    sphere with three tubed axes with cones at the end of the axes. In
    addition an optional lable provides delta values of motion. Note that
    this particular widget draws its representation in 3d space, so the
    widget can be occluded.
    @sa
    DistanceWidget DistanceRepresentation
    DistanceRepresentation2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAxesTransformRepresentation, obj, update, **traits)
    
    interaction_state = traits.Trait(0, traits.Range(0, 7, enter_set=True, auto_set=False), help=\
        """
        The interaction state may be set from a widget (e.g.,
        LineWidget2) or other object. This controls how the
        interaction with the widget proceeds. Normally this method is
        used as part of a handshaking process with the widget: First
        compute_interaction_state() is invoked that returns a state based
        on geometric considerations (i.e., cursor near a widget feature),
        then based on events, the widget may modify this further.
        """
    )

    def _interaction_state_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteractionState,
                        self.interaction_state)

    label_format = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify the format to use for labelling information during
        transformation. Note that an empty string results in no label, or
        a format string without a "%" character will not print numeric
        values.
        """
    )

    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    label_scale = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Scale text (font size along each dimension). This helps control
        the appearance of the 3d text.
        """
    )

    def _label_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelScale,
                        self.label_scale)

    def get_origin_display_position(self, *args):
        """
        V.get_origin_display_position([float, float, float])
        C++: void GetOriginDisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetOriginDisplayPosition, *args)
        return ret

    def set_origin_display_position(self, *args):
        """
        V.set_origin_display_position([float, float, float])
        C++: void SetOriginDisplayPosition(double pos[3])
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetOriginDisplayPosition, *args)
        return ret

    origin_world_position = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
    )

    def _origin_world_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginWorldPosition,
                        self.origin_world_position)

    tolerance = traits.Trait(1, traits.Range(1, 100), enter_set=True, auto_set=False, help=\
        """
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered near enough to the end points
        of the widget to be active.
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def _get_label_property(self):
        return wrap_vtk(self._vtk_obj.GetLabelProperty())
    label_property = traits.Property(_get_label_property, help=\
        """
        Get the distance annotation property
        """
    )

    def _get_origin_representation(self):
        return wrap_vtk(self._vtk_obj.GetOriginRepresentation())
    origin_representation = traits.Property(_get_origin_representation, help=\
        """
        Set/Get the two handle representations used for the
        AxesTransformWidget. (Note: properties can be set by grabbing
        these representations and setting the properties appropriately.)
        """
    )

    def _get_selection_representation(self):
        return wrap_vtk(self._vtk_obj.GetSelectionRepresentation())
    selection_representation = traits.Property(_get_selection_representation, help=\
        """
        Set/Get the two handle representations used for the
        AxesTransformWidget. (Note: properties can be set by grabbing
        these representations and setting the properties appropriately.)
        """
    )

    _updateable_traits_ = \
    (('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interaction_state',
    'GetInteractionState'), ('label_format', 'GetLabelFormat'),
    ('tolerance', 'GetTolerance'), ('handle_size', 'GetHandleSize'),
    ('place_factor', 'GetPlaceFactor'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ('tolerance',)
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'picking_managed', 'use_bounds', 'visibility',
    'estimated_render_time', 'handle_size', 'interaction_state',
    'label_format', 'place_factor', 'render_time_multiplier',
    'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AxesTransformRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AxesTransformRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['need_to_render', 'picking_managed', 'use_bounds',
            'visibility'], [], ['estimated_render_time', 'handle_size',
            'interaction_state', 'label_format', 'place_factor',
            'render_time_multiplier', 'tolerance']),
            title='Edit AxesTransformRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AxesTransformRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


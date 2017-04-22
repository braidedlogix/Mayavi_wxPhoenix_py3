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

from tvtk.tvtk_classes.button_representation import ButtonRepresentation


class Prop3DButtonRepresentation(ButtonRepresentation):
    """
    Prop3DButtonRepresentation - defines a representation for a
    ButtonWidget
    
    Superclass: ButtonRepresentation
    
    This class implements one type of ButtonRepresentation. Each
    button state can be represented with a separate instance of
    Prop3D. Thus buttons can be represented with Actor,
    ImageActor, volumes (e.g., Volume) and/or any other Prop3D.
    Also, the class invokes events when highlighting occurs (i.e.,
    hovering, selecting) so that appropriate action can be taken to
    highlight the button (if desired).
    
    To use this representation, always begin by specifying the number of
    button states.  Then provide, for each state, an instance of
    Prop3D.
    
    This widget representation uses the conventional placement method.
    The button is placed inside the bounding box defined by place_widget
    by translating and scaling the Prop3D to fit (each Prop3D is
    transformed). Therefore, you must define the number of button states
    and each state (i.e., Prop3D) prior to calling PlaceWidget.
    
    @sa
    ButtonWidget ButtonRepresentation ButtonSource
    EllipticalButtonSource RectangularButtonSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProp3DButtonRepresentation, obj, update, **traits)
    
    follow_camera = tvtk_base.false_bool_trait(help=\
        """
        Specify whether the button should always face the camera. If
        enabled, the button reorients itself towards the camera as the
        camera moves.
        """
    )

    def _follow_camera_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFollowCamera,
                        self.follow_camera_)

    def get_button_prop(self, *args):
        """
        V.get_button_prop(int) -> Prop3D
        C++: Prop3D *GetButtonProp(int i)
        Add the ith texture corresponding to the ith button state. The
        parameter i should be (0 <= i < number_of_states).
        """
        ret = self._wrap_call(self._vtk_obj.GetButtonProp, *args)
        return wrap_vtk(ret)

    def set_button_prop(self, *args):
        """
        V.set_button_prop(int, Prop3D)
        C++: void SetButtonProp(int i, Prop3D *prop)
        Add the ith texture corresponding to the ith button state. The
        parameter i should be (0 <= i < number_of_states).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetButtonProp, *my_args)
        return ret

    state = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Extend the ButtonRepresentation::SetState() method.
        """
    )

    def _state_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetState,
                        self.state)

    _updateable_traits_ = \
    (('follow_camera', 'GetFollowCamera'), ('need_to_render',
    'GetNeedToRender'), ('picking_managed', 'GetPickingManaged'),
    ('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('state', 'GetState'), ('handle_size',
    'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'follow_camera', 'global_warning_display',
    'need_to_render', 'pickable', 'picking_managed', 'use_bounds',
    'visibility', 'estimated_render_time', 'handle_size', 'place_factor',
    'render_time_multiplier', 'state'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Prop3DButtonRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Prop3DButtonRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['follow_camera', 'need_to_render', 'picking_managed',
            'use_bounds', 'visibility'], [], ['estimated_render_time',
            'handle_size', 'place_factor', 'render_time_multiplier', 'state']),
            title='Edit Prop3DButtonRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Prop3DButtonRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


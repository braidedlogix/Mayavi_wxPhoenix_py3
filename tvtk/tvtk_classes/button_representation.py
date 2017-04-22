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


class ButtonRepresentation(WidgetRepresentation):
    """
    ButtonRepresentation - abstract class defines the representation
    for a ButtonWidget
    
    Superclass: WidgetRepresentation
    
    This abstract class is used to specify how the ButtonWidget should
    interact with representations of the ButtonWidget. This class may
    be subclassed so that alternative representations can be created. The
    class defines an API, and a default implementation, that the
    ButtonWidget interacts with to render itself in the scene.
    
    The ButtonWidget assumes an n-state button so that traveral
    methods are available for changing, querying and manipulating state.
    Derived classed determine the actual appearance. The state is
    represented by an integral value 0<=state<num_states.
    
    To use this representation, always begin by specifying the number of
    states. Then follow with the necessary information to represent each
    state (done through a subclass API).
    
    @sa
    ButtonWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkButtonRepresentation, obj, update, **traits)
    
    state = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Manipulate the state. Note that the next_state() and
        previous_state() methods use modulo traveral. The "state" integral
        value will be clamped within the possible state values
        (_0<=state<_number_of_states). Note that subclasses will override
        these methods in many cases.
        """
    )

    def _state_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetState,
                        self.state)

    def _get_highlight_state(self):
        return self._vtk_obj.GetHighlightState()
    highlight_state = traits.Property(_get_highlight_state, help=\
        """
        These methods control the appearance of the button as it is being
        interacted with. Subclasses will behave differently depending on
        their particulars.  highlight_hovering is used when the mouse
        pointer moves over the button. highlight_selecting is set when the
        button is selected. Otherwise, the highlight_normal is used. The
        Highlight() method will throw a Command::HighlightEvent.
        """
    )

    def _get_number_of_states_max_value(self):
        return self._vtk_obj.GetNumberOfStatesMaxValue()
    number_of_states_max_value = traits.Property(_get_number_of_states_max_value, help=\
        """
        Retrieve the current button state.
        """
    )

    def _get_number_of_states_min_value(self):
        return self._vtk_obj.GetNumberOfStatesMinValue()
    number_of_states_min_value = traits.Property(_get_number_of_states_min_value, help=\
        """
        Retrieve the current button state.
        """
    )

    def next_state(self):
        """
        V.next_state()
        C++: virtual void NextState()
        Manipulate the state. Note that the next_state() and
        previous_state() methods use modulo traveral. The "state" integral
        value will be clamped within the possible state values
        (_0<=state<_number_of_states). Note that subclasses will override
        these methods in many cases.
        """
        ret = self._vtk_obj.NextState()
        return ret
        

    def previous_state(self):
        """
        V.previous_state()
        C++: virtual void PreviousState()
        Manipulate the state. Note that the next_state() and
        previous_state() methods use modulo traveral. The "state" integral
        value will be clamped within the possible state values
        (_0<=state<_number_of_states). Note that subclasses will override
        these methods in many cases.
        """
        ret = self._vtk_obj.PreviousState()
        return ret
        

    def set_number_of_states(self, *args):
        """
        V.set_number_of_states(int)
        C++: void SetNumberOfStates(int)
        Retrieve the current button state.
        """
        ret = self._wrap_call(self._vtk_obj.SetNumberOfStates, *args)
        return ret

    _updateable_traits_ = \
    (('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('state', 'GetState'), ('handle_size',
    'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'picking_managed', 'use_bounds', 'visibility',
    'estimated_render_time', 'handle_size', 'place_factor',
    'render_time_multiplier', 'state'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ButtonRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ButtonRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['need_to_render', 'picking_managed', 'use_bounds',
            'visibility'], [], ['estimated_render_time', 'handle_size',
            'place_factor', 'render_time_multiplier', 'state']),
            title='Edit ButtonRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ButtonRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


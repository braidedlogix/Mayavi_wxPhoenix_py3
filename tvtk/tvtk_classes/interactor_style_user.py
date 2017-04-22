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

from tvtk.tvtk_classes.interactor_style import InteractorStyle


class InteractorStyleUser(InteractorStyle):
    """
    InteractorStyleUser - provides customizable interaction routines
    
    Superclass: InteractorStyle
    
    The most common way to customize user interaction is to write a
    subclass of InteractorStyle: InteractorStyleUser allows you to
    customize the interaction to without subclassing InteractorStyle. 
    This is particularly useful for setting up custom interaction modes
    in scripting languages such as Tcl and Python.  This class allows you
    to hook into the mouse_move, button_press/_release, key_press/_release,
    etc. events.  If you want to hook into just a single mouse button,
    but leave the interaction modes for the others unchanged, you must
    use e.g. set_middle_button_press_method() instead of the more general
    set_button_press_method().
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleUser, obj, update, **traits)
    
    def _get_button(self):
        return self._vtk_obj.GetButton()
    button = traits.Property(_get_button, help=\
        """
        Get the mouse button that was last pressed inside the window
        (returns zero when the button is released).
        """
    )

    def _get_char(self):
        return self._vtk_obj.GetChar()
    char = traits.Property(_get_char, help=\
        """
        Get the character for a Char event.
        """
    )

    def _get_ctrl_key(self):
        return self._vtk_obj.GetCtrlKey()
    ctrl_key = traits.Property(_get_ctrl_key, help=\
        """
        Test whether modifiers were held down when mouse button or key
        was pressed
        """
    )

    def _get_key_sym(self):
        return self._vtk_obj.GetKeySym()
    key_sym = traits.Property(_get_key_sym, help=\
        """
        Get the key_sym (in the same format as Tk key_syms) for a key_press
        or key_release method.
        """
    )

    def _get_last_pos(self):
        return self._vtk_obj.GetLastPos()
    last_pos = traits.Property(_get_last_pos, help=\
        """
        
        """
    )

    def _get_old_pos(self):
        return self._vtk_obj.GetOldPos()
    old_pos = traits.Property(_get_old_pos, help=\
        """
        
        """
    )

    def _get_shift_key(self):
        return self._vtk_obj.GetShiftKey()
    shift_key = traits.Property(_get_shift_key, help=\
        """
        Test whether modifiers were held down when mouse button or key
        was pressed
        """
    )

    _updateable_traits_ = \
    (('auto_adjust_camera_clipping_range',
    'GetAutoAdjustCameraClippingRange'), ('handle_observers',
    'GetHandleObservers'), ('use_timers', 'GetUseTimers'), ('enabled',
    'GetEnabled'), ('key_press_activation', 'GetKeyPressActivation'),
    ('picking_managed', 'GetPickingManaged'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('mouse_wheel_motion_factor', 'GetMouseWheelMotionFactor'),
    ('pick_color', 'GetPickColor'), ('timer_duration',
    'GetTimerDuration'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('priority', 'GetPriority'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['auto_adjust_camera_clipping_range', 'debug', 'enabled',
    'global_warning_display', 'handle_observers', 'key_press_activation',
    'picking_managed', 'use_timers', 'key_press_activation_value',
    'mouse_wheel_motion_factor', 'pick_color', 'priority',
    'timer_duration'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorStyleUser, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleUser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'picking_managed',
            'use_timers'], [], ['key_press_activation_value',
            'mouse_wheel_motion_factor', 'pick_color', 'priority',
            'timer_duration']),
            title='Edit InteractorStyleUser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleUser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


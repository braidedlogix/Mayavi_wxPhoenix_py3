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

from tvtk.tvtk_classes.abstract_widget import AbstractWidget


class ImplicitPlaneWidget2(AbstractWidget):
    """
    ImplicitPlaneWidget2 - 3d widget for manipulating an infinite plane
    
    Superclass: AbstractWidget
    
    This 3d widget defines an infinite plane that can be interactively
    placed in a scene. The widget is assumed to consist of four parts: 1)
    a plane contained in a 2) bounding box, with a 3) plane normal, which
    is rooted at a 4) point on the plane. (The representation paired with
    this widget determines the actual geometry of the widget.)
    
    To use this widget, you generally pair it with a
    ImplicitPlaneRepresentation (or a subclass). Variuos options are
    available for controlling how the representation appears, and how the
    widget functions.
    
    @par Event Bindings: By default, the widget responds to the following
    VTK events (i.e., it watches the RenderWindowInteractor for these
    events):
    
    If the mouse is over the plane normal:
      left_button_press_event - select normal
      left_button_release_event - release normal
      mouse_move_event - orient the normal vector If the mouse is over the
    origin point (handle):
      left_button_press_event - select handle
      left_button_release_event - release handle (if selected)
      mouse_move_event - move the origin point (constrained to the plane)
    If the mouse is over the plane:
      left_button_press_event - select plane
      left_button_release_event - release plane (if selected)
      mouse_move_event - move the plane If the mouse is over the outline:
      left_button_press_event - select outline
      left_button_release_event - release outline (if selected)
      mouse_move_event - move the outline If the keypress characters are
    used
      'Down/Left' Move plane down
      'Up/Right' Move plane up In all the cases, independent of what is
    picked, the widget responds to the following VTK events:
      middle_button_press_event - move the plane
      middle_button_release_event - release the plane
      right_button_press_event - scale the widget's representation
      right_button_release_event - stop scaling the widget
      mouse_move_event - scale (if right button) or move (if middle button)
    the widget 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's WidgetEventTranslator. This class
    translates VTK events into the ImplicitPlaneWidget2's widget
    events:
    
    
      WidgetEvent::Select -- some part of the widget has been selected
      WidgetEvent::EndSelect -- the selection process has completed
      WidgetEvent::Move -- a request for widget motion has been
    invoked
      WidgetEvent::Up and WidgetEvent::Down -- move_plane_action 
    
    @par Event Bindings: In turn, when these widget events are processed,
    the ImplicitPlaneWidget2 invokes the following VTK events on
    itself (which observers can listen for):
    
    
      Command::StartInteractionEvent (on WidgetEvent::Select)
      Command::EndInteractionEvent (on WidgetEvent::EndSelect)
      Command::InteractionEvent (on WidgetEvent::Move) 
    
    @par Event Bindings: This class, and ImplicitPlaneRepresentation,
    are next generation VTK widgets. An earlier version of this
    functionality was defined in the class ImplicitPlaneWidget.
    
    @sa
    ThreeDWidget BoxWidget PlaneWidget LineWidget PointWidget
    SphereWidget ImagePlaneWidget ImplicitCylinderWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitPlaneWidget2, obj, update, **traits)
    
    def _get_representation(self):
        return wrap_vtk(self._vtk_obj.GetRepresentation())
    def _set_representation(self, arg):
        old_val = self._get_representation()
        self._wrap_call(self._vtk_obj.SetRepresentation,
                        deref_vtk(arg))
        self.trait_property_changed('representation', old_val, arg)
    representation = traits.Property(_get_representation, _set_representation, help=\
        """
        Return an instance of WidgetRepresentation used to represent
        this widget in the scene. Note that the representation is a
        subclass of Prop (typically a subclass of
        WidgetRepresenation) so it can be added to the renderer
        independent of the widget.
        """
    )

    def _get_implicit_plane_representation(self):
        return wrap_vtk(self._vtk_obj.GetImplicitPlaneRepresentation())
    implicit_plane_representation = traits.Property(_get_implicit_plane_representation, help=\
        """
        Return the representation as a ImplicitPlaneRepresentation.
        """
    )

    def set_lock_normal_to_camera(self, *args):
        """
        V.set_lock_normal_to_camera(int)
        C++: void SetLockNormalToCamera(int lock)
        Observe/Unobserve the camera if the widget is locked/unlocked to
        update the ImplicitePlaneRepresentation's normal.
        """
        ret = self._wrap_call(self._vtk_obj.SetLockNormalToCamera, *args)
        return ret

    _updateable_traits_ = \
    (('manages_cursor', 'GetManagesCursor'), ('process_events',
    'GetProcessEvents'), ('enabled', 'GetEnabled'),
    ('key_press_activation', 'GetKeyPressActivation'), ('picking_managed',
    'GetPickingManaged'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('priority',
    'GetPriority'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'manages_cursor', 'picking_managed',
    'process_events', 'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitPlaneWidget2, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitPlaneWidget2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'manages_cursor',
            'picking_managed', 'process_events'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit ImplicitPlaneWidget2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitPlaneWidget2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


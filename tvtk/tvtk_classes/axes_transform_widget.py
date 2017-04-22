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


class AxesTransformWidget(AbstractWidget):
    """
    AxesTransformWidget - 3d widget for performing 3d transformations
    around an axes
    
    Superclass: AbstractWidget
    
    This 3d widget defines an axes which is used to guide transformation.
    The widget can translate, scale, and rotate around one of the three
    coordinate axes. The widget consists of a handle at the origin (used
    for translation), three axes (around which rotations occur), and
    three end arrows (or cones depending on the representation) that can
    be stretched to scale an object.  Optionally a text label can be used
    to indicate the amount of the transformation.
    
    To use this widget, you generally pair it with a
    AxesTransformRepresentation (or a subclass). Various options are
    available in the representation for controlling how the widget
    appears, and how the widget functions.
    
    @par Event Bindings: By default, the widget responds to the following
    VTK events (i.e., it watches the RenderWindowInteractor for these
    events):
    
    If the origin handle is selected:
      left_button_press_event - activate the associated handle widget
      left_button_release_event - release the handle widget associated with
    the point
      mouse_move_event - move the handle and hence the origin and the
    widget If one of the lines is selected:
      left_button_press_event - activate rotation by selecting one of the
    three axes.
      left_button_release_event - end rotation
      mouse_move_event - moving along the selected axis causes rotation to
    occur. If one of the arrows/cones is selected:
      left_button_press_event - activate scaling by selecting the ends of
    one of the three axes.
      left_button_release_event - end scaling
      mouse_move_event - moving along the selected axis causes scaling to
    occur. 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's WidgetEventTranslator. This class
    translates VTK events into the AxesTransformWidget's widget
    events:
    
    
      WidgetEvent::Select -- some part of the widget has been selected
      WidgetEvent::EndSelect -- the selection process has completed
      WidgetEvent::Move -- a request for slider motion has been
    invoked 
    
    @par Event Bindings: In turn, when these widget events are processed,
    the AxesTransformWidget invokes the following VTK events on itself
    (which observers can listen for):
    
    
      Command::StartInteractionEvent (on WidgetEvent::Select)
      Command::EndInteractionEvent (on WidgetEvent::EndSelect)
      Command::InteractionEvent (on WidgetEvent::Move) 
    
    @warning
    Note that the widget can be picked even when it is "behind" other
    actors.  This is an intended feature and not a bug.
    
    @warning
    This class, and AxesTransformRepresentation, are next generation
    VTK widgets.
    
    @sa
    AxesTransformRepresentation AffineWidget BoxWidget2
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAxesTransformWidget, obj, update, **traits)
    
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

    def _get_line_representation(self):
        return wrap_vtk(self._vtk_obj.GetLineRepresentation())
    line_representation = traits.Property(_get_line_representation, help=\
        """
        Return the representation as a AxesTransformRepresentation.
        """
    )

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
            return super(AxesTransformWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AxesTransformWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'manages_cursor',
            'picking_managed', 'process_events'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit AxesTransformWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AxesTransformWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


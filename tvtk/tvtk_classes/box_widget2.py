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


class BoxWidget2(AbstractWidget):
    """
    BoxWidget2 - 3d widget for manipulating a box
    
    Superclass: AbstractWidget
    
    This 3d widget interacts with a BoxRepresentation class (i.e., it
    handles the events that drive its corresponding representation). The
    representation is assumed to represent a region of interest that is
    represented by an arbitrarily oriented hexahedron (or box) with
    interior face angles of 90 degrees (i.e., orthogonal faces). The
    representation manifests seven handles that can be moused on and
    manipulated, plus the six faces can also be interacted with. The
    first six handles are placed on the six faces, the seventh is in the
    center of the box. In addition, a bounding box outline is shown, the
    "faces" of which can be selected for object rotation or scaling. A
    nice feature of BoxWidget2, like any 3d widget, will work with the
    current interactor style. That is, if BoxWidget2 does not handle
    an event, then all other registered observers (including the
    interactor style) have an opportunity to process the event.
    Otherwise, the BoxWidget will terminate the processing of the
    event that it handles.
    
    To use this widget, you generally pair it with a BoxRepresentation
    (or a subclass). Variuos options are available in the representation
    for controlling how the widget appears, and how the widget functions.
    
    @par Event Bindings: By default, the widget responds to the following
    VTK events (i.e., it watches the RenderWindowInteractor for these
    events):
    
    If one of the seven handles are selected:
      left_button_press_event - select the appropriate handle
      left_button_release_event - release the currently selected handle
      mouse_move_event - move the handle If one of the faces is selected:
      left_button_press_event - select a box face
      left_button_release_event - release the box face
      mouse_move_event - rotate the box In all the cases, independent of
    what is picked, the widget responds to the following VTK events:
      middle_button_press_event - translate the widget
      middle_button_release_event - release the widget
      right_button_press_event - scale the widget's representation
      right_button_release_event - stop scaling the widget
      mouse_move_event - scale (if right button) or move (if middle button)
    the widget 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's WidgetEventTranslator. This class
    translates VTK events into the BoxWidget2's widget events:
    
    
      WidgetEvent::Select -- some part of the widget has been selected
      WidgetEvent::EndSelect -- the selection process has completed
      WidgetEvent::Scale -- some part of the widget has been selected
      WidgetEvent::EndScale -- the selection process has completed
      WidgetEvent::Translate -- some part of the widget has been
    selected
      WidgetEvent::EndTranslate -- the selection process has completed
      WidgetEvent::Move -- a request for motion has been invoked 
    
    @par Event Bindings: In turn, when these widget events are processed,
    the BoxWidget2 invokes the following VTK events on itself (which
    observers can listen for):
    
    
      Command::StartInteractionEvent (on WidgetEvent::Select)
      Command::EndInteractionEvent (on WidgetEvent::EndSelect)
      Command::InteractionEvent (on WidgetEvent::Move) 
    
    @par Event Bindings: This class, and the affiliated
    BoxRepresentation, are second generation VTK widgets. An earlier
    version of this functionality was defined in the class BoxWidget.
    
    @sa
    BoxRepresentation BoxWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBoxWidget2, obj, update, **traits)
    
    move_faces_enabled = tvtk_base.true_bool_trait(help=\
        """
        Control the behavior of the widget (i.e., how it processes
        events). Translation, rotation, scaling and face movement can all
        be enabled and disabled. Scaling refers to scaling of the whole
        widget at once, (default is through right mouse button) while
        face movement refers to scaling of the widget one face (axis) at
        a time (default through grabbing one of the representation
        spherical handles).
        """
    )

    def _move_faces_enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMoveFacesEnabled,
                        self.move_faces_enabled_)

    rotation_enabled = tvtk_base.true_bool_trait(help=\
        """
        Control the behavior of the widget (i.e., how it processes
        events). Translation, rotation, scaling and face movement can all
        be enabled and disabled. Scaling refers to scaling of the whole
        widget at once, (default is through right mouse button) while
        face movement refers to scaling of the widget one face (axis) at
        a time (default through grabbing one of the representation
        spherical handles).
        """
    )

    def _rotation_enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRotationEnabled,
                        self.rotation_enabled_)

    scaling_enabled = tvtk_base.true_bool_trait(help=\
        """
        Control the behavior of the widget (i.e., how it processes
        events). Translation, rotation, scaling and face movement can all
        be enabled and disabled. Scaling refers to scaling of the whole
        widget at once, (default is through right mouse button) while
        face movement refers to scaling of the widget one face (axis) at
        a time (default through grabbing one of the representation
        spherical handles).
        """
    )

    def _scaling_enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalingEnabled,
                        self.scaling_enabled_)

    translation_enabled = tvtk_base.true_bool_trait(help=\
        """
        Control the behavior of the widget (i.e., how it processes
        events). Translation, rotation, scaling and face movement can all
        be enabled and disabled. Scaling refers to scaling of the whole
        widget at once, (default is through right mouse button) while
        face movement refers to scaling of the widget one face (axis) at
        a time (default through grabbing one of the representation
        spherical handles).
        """
    )

    def _translation_enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslationEnabled,
                        self.translation_enabled_)

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

    _updateable_traits_ = \
    (('move_faces_enabled', 'GetMoveFacesEnabled'), ('rotation_enabled',
    'GetRotationEnabled'), ('scaling_enabled', 'GetScalingEnabled'),
    ('translation_enabled', 'GetTranslationEnabled'), ('manages_cursor',
    'GetManagesCursor'), ('process_events', 'GetProcessEvents'),
    ('enabled', 'GetEnabled'), ('key_press_activation',
    'GetKeyPressActivation'), ('picking_managed', 'GetPickingManaged'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('priority', 'GetPriority'),
    ('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'manages_cursor', 'move_faces_enabled',
    'picking_managed', 'process_events', 'rotation_enabled',
    'scaling_enabled', 'translation_enabled',
    'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BoxWidget2, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BoxWidget2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'manages_cursor',
            'move_faces_enabled', 'picking_managed', 'process_events',
            'rotation_enabled', 'scaling_enabled', 'translation_enabled'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit BoxWidget2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BoxWidget2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


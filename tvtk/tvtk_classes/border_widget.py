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


class BorderWidget(AbstractWidget):
    """
    BorderWidget - place a border around a 2d rectangular region
    
    Superclass: AbstractWidget
    
    This class is a superclass for 2d widgets that may require a
    rectangular border. Besides drawing a border, the widget provides
    methods for resizing and moving the rectangular region (and
    associated border). The widget provides methods and internal data
    members so that subclasses can take advantage of this widgets
    capabilities, requiring only that the subclass defines a
    "representation", i.e., some combination of props or actors that can
    be managed in the 2d rectangular region.
    
    The class defines basic positioning functionality, including the
    ability to size the widget with locked x/y proportions. The area
    within the border may be made "selectable" as well, meaning that a
    selection event interior to the widget invokes a virtual
    select_region() method, which can be used to pick objects or otherwise
    manipulate data interior to the widget.
    
    @par Event Bindings: By default, the widget responds to the following
    VTK events (i.e., it watches the RenderWindowInteractor for these
    events):
    
    On the boundary of the widget:
      left_button_press_event - select boundary
      left_button_release_event - deselect boundary
      mouse_move_event - move/resize widget depending on which portion of
    the
                       boundary was selected. On the interior of the
    widget:
      left_button_press_event - invoke select_button() callback (if the ivar
                             Selectable is on) Anywhere on the widget:
      middle_button_press_event - move the widget 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's WidgetEventTranslator. This class
    translates VTK events into the BorderWidget's widget events:
    
    
      WidgetEvent::Select -- some part of the widget has been selected
      WidgetEvent::EndSelect -- the selection process has completed
      WidgetEvent::Translate -- the widget is to be translated
      WidgetEvent::Move -- a request for slider motion has been
    invoked 
    
    @par Event Bindings: In turn, when these widget events are processed,
    this widget invokes the following VTK events on itself (which
    observers can listen for):
    
    
      Command::StartInteractionEvent (on WidgetEvent::Select)
      Command::EndInteractionEvent (on WidgetEvent::EndSelect)
      Command::InteractionEvent (on WidgetEvent::Move) 
    
    @sa
    InteractorObserver CameraInterpolator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBorderWidget, obj, update, **traits)
    
    resizable = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether the boundary of the widget can be resized. If
        not, the cursor will not change to "resize" type when mouse over
        the boundary.
        """
    )

    def _resizable_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResizable,
                        self.resizable_)

    selectable = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether the interior region of the widget can be
        selected or not. If not, then events (such as left mouse down)
        allow the user to "move" the widget, and no selection is
        possible. Otherwise the select_region() method is invoked.
        """
    )

    def _selectable_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectable,
                        self.selectable_)

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

    def _get_border_representation(self):
        return wrap_vtk(self._vtk_obj.GetBorderRepresentation())
    border_representation = traits.Property(_get_border_representation, help=\
        """
        Return the representation as a BorderRepresentation.
        """
    )

    _updateable_traits_ = \
    (('resizable', 'GetResizable'), ('selectable', 'GetSelectable'),
    ('manages_cursor', 'GetManagesCursor'), ('process_events',
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
    'process_events', 'resizable', 'selectable',
    'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BorderWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BorderWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'manages_cursor',
            'picking_managed', 'process_events', 'resizable', 'selectable'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit BorderWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BorderWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


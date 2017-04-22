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


class SeedWidget(AbstractWidget):
    """
    SeedWidget - place multiple seed points
    
    Superclass: AbstractWidget
    
    The SeedWidget is used to placed multiple seed points in the
    scene. The seed points can be used for operations like connectivity,
    segmentation, and region growing.
    
    To use this widget, specify an instance of SeedWidget and a
    representation (a subclass of SeedRepresentation). The widget is
    implemented using multiple instances of HandleWidget which can be
    used to position the seed points (after they are initially placed).
    The representations for these handle widgets are provided by the
    SeedRepresentation.
    
    @par Event Bindings: By default, the widget responds to the following
    VTK events (i.e., it watches the RenderWindowInteractor for these
    events):
    
    
      left_button_press_event - add a point or select a handle (i.e., seed)
      right_button_press_event - finish adding the seeds
      mouse_move_event - move a handle (i.e., seed)
      left_button_release_event - release the selected handle (seed) 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's WidgetEventTranslator. This class
    translates VTK events into the SeedWidget's widget events:
    
    
      WidgetEvent::AddPoint -- add one point; depending on the state
                                  it may the first or second point added.
    Or,
                                  if near handle, select handle.
      WidgetEvent::Completed -- finished adding seeds.
      WidgetEvent::Move -- move the second point or handle depending
    on the state.
      WidgetEvent::EndSelect -- the handle manipulation process has
    completed. 
    
    @par Event Bindings: This widget invokes the following VTK events on
    itself (which observers can listen for):
    
    
      Command::StartInteractionEvent (beginning to interact)
      Command::EndInteractionEvent (completing interaction)
      Command::InteractionEvent (moving after selecting something)
      Command::PlacePointEvent (after point is positioned;
                                   call data includes handle id (0,1)) 
    
    @sa
    HandleWidget SeedReoresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSeedWidget, obj, update, **traits)
    
    def _get_current_renderer(self):
        return wrap_vtk(self._vtk_obj.GetCurrentRenderer())
    def _set_current_renderer(self, arg):
        old_val = self._get_current_renderer()
        self._wrap_call(self._vtk_obj.SetCurrentRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('current_renderer', old_val, arg)
    current_renderer = traits.Property(_get_current_renderer, _set_current_renderer, help=\
        """
        Set/Get the current renderer. Normally when the widget is
        activated (_set_enabled(_1) or when keypress activation takes
        place), the renderer over which the mouse pointer is positioned
        is used and assigned to this Ivar. Alternatively, you might want
        to set the current_renderer explicitly. This is especially true
        with multiple viewports (renderers). WARNING: note that if the
        default_renderer Ivar is set (see above), it will always override
        the parameter passed to set_current_renderer, unless it is NULL.
        (i.e., set_current_renderer(foo) =
        set_current_renderer(_default_renderer).
        """
    )

    def _get_interactor(self):
        return wrap_vtk(self._vtk_obj.GetInteractor())
    def _set_interactor(self, arg):
        old_val = self._get_interactor()
        self._wrap_call(self._vtk_obj.SetInteractor,
                        deref_vtk(arg))
        self.trait_property_changed('interactor', old_val, arg)
    interactor = traits.Property(_get_interactor, _set_interactor, help=\
        """
        This method is used to associate the widget with the render
        window interactor.  Observers of the appropriate events invoked
        in the render window interactor are set up as a result of this
        method invocation. The set_interactor() method must be invoked
        prior to enabling the InteractorObserver. It automatically
        registers available pickers to the Picking Manager.
        """
    )

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

    def get_seed(self, *args):
        """
        V.get_seed(int) -> HandleWidget
        C++: HandleWidget *GetSeed(int n)
        Get the nth seed
        """
        ret = self._wrap_call(self._vtk_obj.GetSeed, *args)
        return wrap_vtk(ret)

    def _get_seed_representation(self):
        return wrap_vtk(self._vtk_obj.GetSeedRepresentation())
    seed_representation = traits.Property(_get_seed_representation, help=\
        """
        Return the representation as a SeedRepresentation.
        """
    )

    def _get_widget_state(self):
        return self._vtk_obj.GetWidgetState()
    widget_state = traits.Property(_get_widget_state, help=\
        """
        Get the widget state.
        """
    )

    def complete_interaction(self):
        """
        V.complete_interaction()
        C++: virtual void CompleteInteraction()
        Method to be called when the seed widget should stop responding
        to the place point interaction. The seed widget, when defined
        allows you place seeds by clicking on the render window. Use this
        method to indicate that you would like to stop placing seeds
        interactively. If you'd like the widget to stop responding to
        *any* user interaction simply disable event processing by the
        widget by calling widget->_process_events_off()
        """
        ret = self._vtk_obj.CompleteInteraction()
        return ret
        

    def create_new_handle(self):
        """
        V.create_new_handle() -> HandleWidget
        C++: virtual HandleWidget *CreateNewHandle()
        Use this method to programmatically create a new handle. In
        interactive mode, (when the widget is in the placing_seeds state)
        this method is automatically invoked. The method returns the
        handle created. A valid seed representation must exist for the
        widget to create a new handle.
        """
        ret = wrap_vtk(self._vtk_obj.CreateNewHandle())
        return ret
        

    def delete_seed(self, *args):
        """
        V.delete_seed(int)
        C++: void DeleteSeed(int n)
        Delete the nth seed.
        """
        ret = self._wrap_call(self._vtk_obj.DeleteSeed, *args)
        return ret

    def restart_interaction(self):
        """
        V.restart_interaction()
        C++: virtual void RestartInteraction()
        Method to be called when the seed widget should start responding
        to the interaction.
        """
        ret = self._vtk_obj.RestartInteraction()
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
            return super(SeedWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SeedWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'manages_cursor',
            'picking_managed', 'process_events'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit SeedWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SeedWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


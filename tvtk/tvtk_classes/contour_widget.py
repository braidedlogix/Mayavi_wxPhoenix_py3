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


class ContourWidget(AbstractWidget):
    """
    ContourWidget - create a contour with a set of points
    
    Superclass: AbstractWidget
    
    The ContourWidget is used to select a set of points, and draw
    lines between these points. The contour may be opened or closed,
    depending on how the last point is added. The widget handles all
    processing of widget events (that are triggered by VTK events). The
    ContourRepresentation is responsible for all placement of the
    points, calculation of the lines, and contour manipulation. This is
    done through two main helper classes: PointPlacer and
    ContourLineInterpolator. The representation is also responsible
    for drawing the points and lines.
    
    @par Event Bindings: By default, the widget responds to the following
    VTK events (i.e., it watches the RenderWindowInteractor for these
    events):
    
    
      left_button_press_event - triggers a Select event
      right_button_press_event - triggers a add_final_point event
      mouse_move_event - triggers a Move event
      left_button_release_event - triggers an end_select event
      Delete key event - triggers a Delete event
      Shift + Delete key event - triggers a Reset event 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's WidgetEventTranslator. This class
    translates VTK events into the ContourWidget's widget events:
    
    
      WidgetEvent::Select
           widget state is:
               Start or
               Define: If we already have at least 2 nodes, test
                    whether the current (X,Y) location is near an
    existing
                    node. If so, close the contour and change to
    Manipulate
                    state. Otherwise, attempt to add a node at this (X,Y)
                    location.
               Manipulate: If this (X,Y) location activates a node, then
                    set the current operation to Translate. Otherwise, if
                    this location is near the contour, attempt to add a
                    new node on the contour at this (X,Y) location.
    
    @par Event Bindings:
      WidgetEvent::AddFinalPoint
           widget state is:
               Start: Do nothing.
               Define: If we already have at least 2 nodes, test
                    whether the current (X,Y) location is near an
    existing
                    node. If so, close the contour and change to
    Manipulate
                    state. Otherwise, attempt to add a node at this (X,Y)
                    location. If we do, then leave the contour open and
                    change to Manipulate state.
               Manipulate: Do nothing.
    
    @par Event Bindings:
      WidgetEvent::Move
           widget state is:
               Start or
               Define: Do nothing.
               Manipulate: If our operation is Translate, then invoke
                     widget_interaction() on the representation. If our
                     operation is Inactive, then just attempt to activate
                     a node at this (X,Y) location.
    
    @par Event Bindings:
      WidgetEvent::EndSelect
           widget state is:
               Start or
               Define: Do nothing.
               Manipulate: If our operation is not Inactive, set it to
                     Inactive.
    
    @par Event Bindings:
      WidgetEvent::Delete
           widget state is:
               Start: Do nothing.
               Define: Remove the last point on the contour.
               Manipulate: Attempt to activate a node at (X,Y). If
                      we do activate a node, delete it. If we now
                      have less than 3 nodes, go back to Define state.
    
    @par Event Bindings:
      WidgetEvent::Reset
           widget state is:
               Start: Do nothing.
               Define: Remove all points and line segments of the
    contour.
                    Essentially calls Initialize(NULL)
               Manipulate: Do nothing. 
    
    @par Event Bindings: This widget invokes the following VTK events on
    itself (which observers can listen for):
    
    
      Command::StartInteractionEvent (beginning to interact)
      Command::EndInteractionEvent (completing interaction)
      Command::InteractionEvent (moving after selecting something)
      Command::PlacePointEvent (after point is positioned;
                                   call data includes handle id (0,1))
      Command::WidgetValueChangedEvent (Invoked when the contour is
    closed
                                           for the first time. ) 
    
    @sa
    HandleWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContourWidget, obj, update, **traits)
    
    allow_node_picking = tvtk_base.false_bool_trait(help=\
        """
        Set / Get the allow_node_picking value. This ivar indicates whether
        the nodes and points between nodes can be picked/un-picked by
        Ctrl+Click on the node.
        """
    )

    def _allow_node_picking_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllowNodePicking,
                        self.allow_node_picking_)

    continuous_draw = tvtk_base.false_bool_trait(help=\
        """
        Define a contour by continuously drawing with the mouse cursor.
        Press and hold the left mouse button down to continuously draw.
        Releasing the left mouse button switches into a snap drawing
        mode. Terminate the contour by pressing the right mouse button. 
        If you do not want to see the nodes as they are added to the
        contour, set the opacity to 0 of the representation's property. 
        If you do not want to see the last active node as it is being
        added, set the opacity to 0 of the representation's active
        property.
        """
    )

    def _continuous_draw_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetContinuousDraw,
                        self.continuous_draw_)

    follow_cursor = tvtk_base.false_bool_trait(help=\
        """
        Follow the cursor ? If this is ON, during definition, the last
        node of the contour will automatically follow the cursor, without
        waiting for the point to be dropped. This may be useful for some
        interpolators, such as the live-wire interpolator to see the
        shape of the contour that will be placed as you move the mouse
        cursor.
        """
    )

    def _follow_cursor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFollowCursor,
                        self.follow_cursor_)

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

    widget_state = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Convenient method to change what state the widget is in.
        """
    )

    def _widget_state_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWidgetState,
                        self.widget_state)

    def _get_contour_representation(self):
        return wrap_vtk(self._vtk_obj.GetContourRepresentation())
    contour_representation = traits.Property(_get_contour_representation, help=\
        """
        Return the representation as a ContourRepresentation.
        """
    )

    def close_loop(self):
        """
        V.close_loop()
        C++: void CloseLoop()
        Convenient method to close the contour loop.
        """
        ret = self._vtk_obj.CloseLoop()
        return ret
        

    def initialize(self, *args):
        """
        V.initialize(PolyData, int, IdList)
        C++: virtual void Initialize(PolyData *poly, int state=1,
            IdList *idList=NULL)
        V.initialize()
        C++: virtual void Initialize()
        Initialize the contour widget from a user supplied set of points.
        The state of the widget decides if you are still defining the
        widget, or if you've finished defining (added the last point) are
        manipulating it. Note that if the polydata supplied is closed,
        the state will be set to manipulate. State: Define = 0,
        Manipulate = 1.
        """
        my_args = deref_array(args, [('vtkPolyData', 'int', 'vtkIdList'), None])
        ret = self._wrap_call(self._vtk_obj.Initialize, *my_args)
        return ret

    _updateable_traits_ = \
    (('allow_node_picking', 'GetAllowNodePicking'), ('continuous_draw',
    'GetContinuousDraw'), ('follow_cursor', 'GetFollowCursor'),
    ('manages_cursor', 'GetManagesCursor'), ('process_events',
    'GetProcessEvents'), ('enabled', 'GetEnabled'),
    ('key_press_activation', 'GetKeyPressActivation'), ('picking_managed',
    'GetPickingManaged'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('widget_state', 'GetWidgetState'), ('priority', 'GetPriority'),
    ('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['allow_node_picking', 'continuous_draw', 'debug', 'enabled',
    'follow_cursor', 'global_warning_display', 'key_press_activation',
    'manages_cursor', 'picking_managed', 'process_events',
    'key_press_activation_value', 'priority', 'widget_state'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContourWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ContourWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['allow_node_picking', 'continuous_draw', 'enabled',
            'follow_cursor', 'key_press_activation', 'manages_cursor',
            'picking_managed', 'process_events'], [],
            ['key_press_activation_value', 'priority', 'widget_state']),
            title='Edit ContourWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContourWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


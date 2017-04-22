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


class BiDimensionalWidget(AbstractWidget):
    """
    BiDimensionalWidget - measure the bi-dimensional lengths of an
    object
    
    Superclass: AbstractWidget
    
    The BiDimensionalWidget is used to measure the bi-dimensional
    length of an object. The bi-dimensional measure is defined by two
    finite, orthogonal lines that intersect within the finite extent of
    both lines. The lengths of these two lines gives the bi-dimensional
    measure. Each line is defined by two handle widgets at the end points
    of each line.
    
    The orthogonal constraint on the two lines limits how the four end
    points can be positioned. The first two points can be placed
    arbitrarily to define the first line (similar to DistanceWidget).
    The placement of the third point is limited by the finite extent of
    the first line. As the third point is placed, the fourth point is
    placed on the opposite side of the first line. Once the third point
    is placed, the second line is defined since the fourth point is
    defined at the same time, but the fourth point can be moved along the
    second line (i.e., maintaining the orthogonal relationship between
    the two lines). Once defined, any of the four points can be moved
    along their constraint lines. Also, each line can be translated along
    the other line (in an orthogonal direction), and the whole
    bi-dimensional widget can be rotated about its center point (see the
    description of the event bindings). Finally, selecting the point
    where the two orthogonal axes intersect, the entire widget can be
    translated in any direction.
    
    Placement of any point results in a special place_point_event
    invocation so that special operations may be performed to reposition
    the point. Motion of any point, moving the lines, or rotating the
    widget cause interaction_events to be invoked. Note that the widget
    has two fundamental modes: a define mode (when initially placing the
    points) and a manipulate mode (after the points are placed). Line
    translation and rotation are only possible in manipulate mode.
    
    To use this widget, specify an instance of BiDimensionalWidget and
    a representation (e.g., BiDimensionalRepresentation2D). The widget
    is implemented using four instances of HandleWidget which are used
    to position the end points of the two intersecting lines. The
    representations for these handle widgets are provided by the
    BiDimensionalRepresentation class.
    
    @par Event Bindings: By default, the widget responds to the following
    VTK events (i.e., it watches the RenderWindowInteractor for these
    events):
    
    
      left_button_press_event - define a point or manipulate a handle, line,
                             perform rotation or translate the widget.
      mouse_move_event - position the points, move a line, rotate or
    translate the widget
      left_button_release_event - release the selected handle and end
    interaction 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's WidgetEventTranslator. This class
    translates VTK events into the BiDimensionalWidget's widget
    events:
    
    
      WidgetEvent::AddPoint -- (In Define mode:) Add one point;
    depending on the
                                  state it may the first, second, third
    or fourth
                                  point added. (In Manipulate mode:) If
    near a handle,
                                  select the handle. Or if near a line,
    select the line.
      WidgetEvent::Move -- (In Define mode:) Position the second,
    third or fourth
                              point. (In Manipulate mode:) Move the
    handle, line or widget.
      WidgetEvent::EndSelect -- the manipulation process has
    completed. 
    
    @par Event Bindings: This widget invokes the following VTK events on
    itself (which observers can listen for):
    
    
      Command::StartInteractionEvent (beginning to interact)
      Command::EndInteractionEvent (completing interaction)
      Command::InteractionEvent (moving a handle, line or performing
    rotation)
      Command::PlacePointEvent (after a point is positioned;
                                   call data includes handle id
    (0,1,2,4)) 
    
    @sa
    HandleWidget DistanceWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBiDimensionalWidget, obj, update, **traits)
    
    def get_widget_state(self):
        """
        V.get_widget_state() -> int
        C++: virtual int GetWidgetState()
        Return the current widget state.
        """
        ret = self._vtk_obj.GetWidgetState()
        return ret
        

    def set_widget_state_to_manipulate(self):
        """
        V.set_widget_state_to_manipulate()
        C++: virtual void SetWidgetStateToManipulate()
        Set the state of the widget. If the state is set to "Manipulate"
        then it is assumed that the widget and its representation will be
        initialized programmatically and is not interactively placed.
        Initially the widget state is set to "Start" which means nothing
        will appear and the user must interactively place the widget with
        repeated mouse selections. Set the state to "Start" if you want
        interactive placement. Generally state changes must be followed
        by a Render() for things to visually take effect.
        """
        self._vtk_obj.SetWidgetStateToManipulate()

    def set_widget_state_to_start(self):
        """
        V.set_widget_state_to_start()
        C++: virtual void SetWidgetStateToStart()
        Set the state of the widget. If the state is set to "Manipulate"
        then it is assumed that the widget and its representation will be
        initialized programmatically and is not interactively placed.
        Initially the widget state is set to "Start" which means nothing
        will appear and the user must interactively place the widget with
        repeated mouse selections. Set the state to "Start" if you want
        interactive placement. Generally state changes must be followed
        by a Render() for things to visually take effect.
        """
        self._vtk_obj.SetWidgetStateToStart()

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

    def _get_bi_dimensional_representation(self):
        return wrap_vtk(self._vtk_obj.GetBiDimensionalRepresentation())
    bi_dimensional_representation = traits.Property(_get_bi_dimensional_representation, help=\
        """
        Return the representation as a BiDimensionalRepresentation.
        """
    )

    def is_measure_valid(self):
        """
        V.is_measure_valid() -> int
        C++: int IsMeasureValid()
        A flag indicates whether the bi-dimensional measure is valid. The
        widget becomes valid after two of the four points are placed.
        """
        ret = self._vtk_obj.IsMeasureValid()
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
            return super(BiDimensionalWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BiDimensionalWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'manages_cursor',
            'picking_managed', 'process_events'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit BiDimensionalWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BiDimensionalWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


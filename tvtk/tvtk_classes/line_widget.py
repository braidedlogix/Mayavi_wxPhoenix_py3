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

from tvtk.tvtk_classes.three_d_widget import ThreeDWidget


class LineWidget(ThreeDWidget):
    """
    LineWidget - 3d widget for manipulating a line
    
    Superclass: ThreeDWidget
    
    This 3d widget defines a line that can be interactively placed in a
    scene. The line has two handles (at its endpoints), plus the line can
    be picked to translate it in the scene.  A nice feature of the object
    is that the LineWidget, like any 3d widget, will work with the
    current interactor style and any other widgets present in the scene.
    That is, if LineWidget does not handle an event, then all other
    registered observers (including the interactor style) have an
    opportunity to process the event. Otherwise, the LineWidget will
    terminate the processing of the event that it handles.
    
    To use this object, just invoke set_interactor() with the argument of
    the method a RenderWindowInteractor.  You may also wish to invoke
    "_place_widget()" to initially position the widget. The interactor will
    act normally until the "i" key (for "interactor") is pressed, at
    which point the LineWidget will appear. (See superclass
    documentation for information about changing this behavior.) By
    grabbing one of the two end point handles (use the left mouse
    button), the line can be oriented and stretched (the other end point
    remains fixed). By grabbing the line itself, or using the middle
    mouse button, the entire line can be translated.  Scaling (about the
    center of the line) is achieved by using the right mouse button. By
    moving the mouse "up" the render window the line will be made bigger;
    by moving "down" the render window the widget will be made smaller.
    Turn off the widget by pressing the "i" key again (or invoke the
    Off() method). (Note: picking the line or either one of the two end
    point handles causes a PointWidget to appear.  This widget has the
    ability to constrain motion to an axis by pressing the "shift" key
    while moving the mouse.)
    
    The LineWidget has several methods that can be used in conjunction
    with other VTK objects. The set/_get_resolution() methods control the
    number of subdivisions of the line; the get_poly_data() method can be
    used to get the polygonal representation and can be used for things
    like seeding streamlines. Typical usage of the widget is to make use
    of the start_interaction_event, interaction_event, and
    end_interaction_event events. The interaction_event is called on mouse
    motion; the other two events are called on button down and button up
    (either left or right button).
    
    Some additional features of this class include the ability to control
    the properties of the widget. You can set the properties of the
    selected and unselected representations of the line. For example, you
    can set the property for the handles and line. In addition there are
    methods to constrain the line so that it is aligned along the x-y-z
    axes.
    
    @sa
    ThreeDWidget BoxWidget PlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLineWidget, obj, update, **traits)
    
    def setup_observers(self):
        """Setup the observers for the object."""
        super(LineWidget, self).setup_observers()
        tvtk_base._object_cache.setup_observers(self._vtk_obj,
                                      'EndInteractionEvent',
                                      self.update_traits)
    clamp_to_bounds = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable clamping of the point end points to the bounding
        box of the data. The bounding box is defined from the last
        place_widget() invocation, and includes the effect of the
        place_factor which is used to gram/shrink the bounding box.
        """
    )

    def _clamp_to_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClampToBounds,
                        self.clamp_to_bounds_)

    align = traits.Trait('x_axis',
    tvtk_base.TraitRevPrefixMap({'x_axis': 0, 'none': 3, 'y_axis': 1, 'z_axis': 2}), help=\
        """
        Force the line widget to be aligned with one of the x-y-z axes.
        Remember that when the state changes, a modified_event is invoked.
        This can be used to snap the line to the axes if it is originally
        not aligned.
        """
    )

    def _align_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlign,
                        self.align_)

    point1 = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(-0.5, 0.0, 0.0), cols=3, help=\
        """
        Set/Get the position of first end point.
        """
    )

    def _point1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1,
                        self.point1)

    point2 = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.5, 0.0, 0.0), cols=3, help=\
        """
        Set position of other end point.
        """
    )

    def _point2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2,
                        self.point2)

    resolution = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the resolution (number of subdivisions) of the line.
        """
    )

    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

    def _get_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetHandleProperty())
    handle_property = traits.Property(_get_handle_property, help=\
        """
        Get the handle properties (the little balls are the handles). The
        properties of the handles when selected and normal can be
        manipulated.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Specify the input dataset. This is not required, but if supplied,
        and no Prop3D is specified, it is used to initially position
        the widget.
        """
    )

    def _get_line_property(self):
        return wrap_vtk(self._vtk_obj.GetLineProperty())
    line_property = traits.Property(_get_line_property, help=\
        """
        Get the line properties. The properties of the line when selected
        and unselected can be manipulated.
        """
    )

    def get_poly_data(self, *args):
        """
        V.get_poly_data(PolyData)
        C++: void GetPolyData(PolyData *pd)
        Grab the polydata (including points) that defines the line.  The
        polydata consists of n+1 points, where n is the resolution of the
        line. These point values are guaranteed to be up-to-date when
        either the interaction_event or end_interaction events are invoked.
        The user provides the PolyData and the points and polyline are
        added to it.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPolyData, *my_args)
        return ret

    def _get_selected_handle_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedHandleProperty())
    selected_handle_property = traits.Property(_get_selected_handle_property, help=\
        """
        Get the handle properties (the little balls are the handles). The
        properties of the handles when selected and normal can be
        manipulated.
        """
    )

    def _get_selected_line_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedLineProperty())
    selected_line_property = traits.Property(_get_selected_line_property, help=\
        """
        Get the line properties. The properties of the line when selected
        and unselected can be manipulated.
        """
    )

    _updateable_traits_ = \
    (('clamp_to_bounds', 'GetClampToBounds'), ('enabled', 'GetEnabled'),
    ('key_press_activation', 'GetKeyPressActivation'), ('picking_managed',
    'GetPickingManaged'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('align',
    'GetAlign'), ('point1', 'GetPoint1'), ('point2', 'GetPoint2'),
    ('resolution', 'GetResolution'), ('handle_size', 'GetHandleSize'),
    ('place_factor', 'GetPlaceFactor'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('priority', 'GetPriority'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['clamp_to_bounds', 'debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'picking_managed', 'align', 'handle_size',
    'key_press_activation_value', 'place_factor', 'point1', 'point2',
    'priority', 'resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LineWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit LineWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['clamp_to_bounds', 'enabled', 'key_press_activation',
            'picking_managed'], ['align'], ['handle_size',
            'key_press_activation_value', 'place_factor', 'point1', 'point2',
            'priority', 'resolution']),
            title='Edit LineWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LineWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


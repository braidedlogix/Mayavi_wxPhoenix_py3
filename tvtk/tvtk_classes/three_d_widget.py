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

from tvtk.tvtk_classes.interactor_observer import InteractorObserver


class ThreeDWidget(InteractorObserver):
    """
    ThreeDWidget - an abstract superclass for 3d widgets
    
    Superclass: InteractorObserver
    
    ThreeDWidget is an abstract superclass for 3d interactor observers.
    These 3d widgets represent themselves in the scene, and have special
    callbacks associated with them that allows interactive manipulation
    of the widget. Inparticular, the difference between a ThreeDWidget and
    its abstract superclass InteractorObserver is that ThreeDWidgets
    are "placed" in 3d space.  InteractorObservers have no notion of
    where they are placed, and may not exist in 3d space at all.  3d
    widgets also provide auxiliary functions like producing a
    transformation, creating polydata (for seeding streamlines, probes,
    etc.) or creating implicit functions. See the concrete subclasses for
    particulars.
    
    Typically the widget is used by specifying a Prop3D or VTK dataset
    as input, and then invoking the "On" method to activate it. (You can
    also specify a bounding box to help position the widget.) Prior to
    invoking the On() method, the user may also wish to use the
    place_widget() to initially position it. The 'i' (for "interactor")
    keypresses also can be used to turn the widgets on and off (methods
    exist to change the key value and enable keypress activiation).
    
    To support interactive manipulation of objects, this class (and
    subclasses) invoke the events start_interaction_event,
    interaction_event, and end_interaction_event.  These events are invoked
    when the ThreeDWidget enters a state where rapid response is desired:
    mouse motion, etc. The events can be used, for example, to set the
    desired update frame rate (_start_interaction_event), operate on the
    Prop3D or other object (_interaction_event), and set the desired
    frame rate back to normal values (_end_interaction_event).
    
    Note that the Priority attribute inherited from InteractorObserver
    has a new default value which is now 0.5 so that all 3d widgets have
    a higher priority than the usual interactor styles.
    
    @sa
    BoxWidget PlaneWidget LineWidget PointWidget
    SphereWidget ImplicitPlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtk3DWidget, obj, update, **traits)
    
    handle_size = traits.Trait(0.01, traits.Range(0.001, 0.5, enter_set=True, auto_set=False), help=\
        """
        Set/Get the factor that controls the size of the handles that
        appear as part of the widget. These handles (like spheres, etc.)
        are used to manipulate the widget, and are sized as a fraction of
        the screen diagonal.
        """
    )

    def _handle_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleSize,
                        self.handle_size)

    place_factor = traits.Trait(0.5, traits.Range(0.01, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get a factor representing the scaling of the widget upon
        placement (via the place_widget() method). Normally the widget is
        placed so that it just fits within the bounding box defined in
        place_widget(bounds). The place_factor will make the widget larger
        (_place_factor > 1) or smaller (_place_factor < 1). By default,
        place_factor is set to 0.5.
        """
    )

    def _place_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlaceFactor,
                        self.place_factor)

    def _get_prop3d(self):
        return wrap_vtk(self._vtk_obj.GetProp3D())
    def _set_prop3d(self, arg):
        old_val = self._get_prop3d()
        self._wrap_call(self._vtk_obj.SetProp3D,
                        deref_vtk(arg))
        self.trait_property_changed('prop3d', old_val, arg)
    prop3d = traits.Property(_get_prop3d, _set_prop3d, help=\
        """
        Specify a Prop3D around which to place the widget. This is not
        required, but if supplied, it is used to initially position the
        widget.
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

    def place_widget(self, *args):
        """
        V.place_widget([float, float, float, float, float, float])
        C++: virtual void PlaceWidget(double bounds[6])
        V.place_widget()
        C++: virtual void PlaceWidget()
        V.place_widget(float, float, float, float, float, float)
        C++: virtual void PlaceWidget(double xmin, double xmax,
            double ymin, double ymax, double zmin, double zmax)
        This method is used to initially place the widget.  The placement
        of the widget depends on whether a prop3d or input dataset is
        provided. If one of these two is provided, they will be used to
        obtain a bounding box, around which the widget is placed.
        Otherwise, you can manually specify a bounds with the
        place_widget(bounds) method. Note: place_widget(bounds) is required
        by all subclasses; the other methods are provided as convenience
        methods.
        """
        ret = self._wrap_call(self._vtk_obj.PlaceWidget, *args)
        return ret

    def set_input_connection(self, *args):
        """
        V.set_input_connection(AlgorithmOutput)
        C++: virtual void SetInputConnection(AlgorithmOutput *)
        Specify the input dataset. This is not required, but if supplied,
        and no Prop3D is specified, it is used to initially position
        the widget.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputConnection, *my_args)
        return ret

    def set_input_data(self, *args):
        """
        V.set_input_data(DataSet)
        C++: virtual void SetInputData(DataSet *)
        Specify the input dataset. This is not required, but if supplied,
        and no Prop3D is specified, it is used to initially position
        the widget.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    _updateable_traits_ = \
    (('enabled', 'GetEnabled'), ('key_press_activation',
    'GetKeyPressActivation'), ('picking_managed', 'GetPickingManaged'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('handle_size', 'GetHandleSize'),
    ('place_factor', 'GetPlaceFactor'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('priority', 'GetPriority'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'picking_managed', 'handle_size',
    'key_press_activation_value', 'place_factor', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ThreeDWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ThreeDWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'picking_managed'], [],
            ['handle_size', 'key_press_activation_value', 'place_factor',
            'priority']),
            title='Edit ThreeDWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ThreeDWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


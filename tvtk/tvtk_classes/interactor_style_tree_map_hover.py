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

from tvtk.tvtk_classes.interactor_style_image import InteractorStyleImage


class InteractorStyleTreeMapHover(InteractorStyleImage):
    """
    InteractorStyleTreeMapHover - An interactor style for a tree map
    view
    
    Superclass: InteractorStyleImage
    
    The InteractorStyleTreeMapHover specifically works with pipelines
    that create a tree map.  Such pipelines will have a TreeMapLayout
    filter and a TreeMapToPolyData filter, both of which must be
    passed to this interactor style for it to function correctly. This
    interactor style allows only 2d panning and zooming, and additionally
    provides a balloon containing the name of the vertex hovered over,
    and allows the user to highlight a vertex by clicking on it.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInteractorStyleTreeMapHover, obj, update, **traits)
    
    high_light_width = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The width of the line around the hovered vertex.
        """
    )

    def _high_light_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHighLightWidth,
                        self.high_light_width)

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

    label_field = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The name of the field to use when displaying text in the hover
        balloon.
        """
    )

    def _label_field_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelField,
                        self.label_field)

    def _get_layout(self):
        return wrap_vtk(self._vtk_obj.GetLayout())
    def _set_layout(self, arg):
        old_val = self._get_layout()
        self._wrap_call(self._vtk_obj.SetLayout,
                        deref_vtk(arg))
        self.trait_property_changed('layout', old_val, arg)
    layout = traits.Property(_get_layout, _set_layout, help=\
        """
        Must be set to the TreeMapLayout used to compute the bounds of
        each vertex for the tree map.
        """
    )

    selection_width = traits.Float(2.0, enter_set=True, auto_set=False, help=\
        """
        The width of the line around the selected vertex.
        """
    )

    def _selection_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionWidth,
                        self.selection_width)

    def _get_tree_map_to_poly_data(self):
        return wrap_vtk(self._vtk_obj.GetTreeMapToPolyData())
    def _set_tree_map_to_poly_data(self, arg):
        old_val = self._get_tree_map_to_poly_data()
        self._wrap_call(self._vtk_obj.SetTreeMapToPolyData,
                        deref_vtk(arg))
        self.trait_property_changed('tree_map_to_poly_data', old_val, arg)
    tree_map_to_poly_data = traits.Property(_get_tree_map_to_poly_data, _set_tree_map_to_poly_data, help=\
        """
        Must be set to the TreeMapToPolyData used to convert the tree
        map into polydata.
        """
    )

    def high_light_current_selected_item(self):
        """
        V.high_light_current_selected_item()
        C++: void HighLightCurrentSelectedItem()
        Highlights a specific vertex.
        """
        ret = self._vtk_obj.HighLightCurrentSelectedItem()
        return ret
        

    def high_light_item(self, *args):
        """
        V.high_light_item(int)
        C++: void HighLightItem(IdType id)
        Highlights a specific vertex.
        """
        ret = self._wrap_call(self._vtk_obj.HighLightItem, *args)
        return ret

    def set_high_light_color(self, *args):
        """
        V.set_high_light_color(float, float, float)
        C++: void SetHighLightColor(double r, double g, double b)
        Set the color used to highlight the hovered vertex.
        """
        ret = self._wrap_call(self._vtk_obj.SetHighLightColor, *args)
        return ret

    def set_selection_light_color(self, *args):
        """
        V.set_selection_light_color(float, float, float)
        C++: void SetSelectionLightColor(double r, double g, double b)
        Set the color used to highlight the selected vertex.
        """
        ret = self._wrap_call(self._vtk_obj.SetSelectionLightColor, *args)
        return ret

    _updateable_traits_ = \
    (('auto_adjust_camera_clipping_range',
    'GetAutoAdjustCameraClippingRange'), ('handle_observers',
    'GetHandleObservers'), ('use_timers', 'GetUseTimers'), ('enabled',
    'GetEnabled'), ('key_press_activation', 'GetKeyPressActivation'),
    ('picking_managed', 'GetPickingManaged'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('interaction_mode', 'GetInteractionMode'), ('high_light_width',
    'GetHighLightWidth'), ('label_field', 'GetLabelField'),
    ('selection_width', 'GetSelectionWidth'), ('current_image_number',
    'GetCurrentImageNumber'), ('x_view_right_vector',
    'GetXViewRightVector'), ('x_view_up_vector', 'GetXViewUpVector'),
    ('y_view_right_vector', 'GetYViewRightVector'), ('y_view_up_vector',
    'GetYViewUpVector'), ('z_view_right_vector', 'GetZViewRightVector'),
    ('z_view_up_vector', 'GetZViewUpVector'), ('motion_factor',
    'GetMotionFactor'), ('mouse_wheel_motion_factor',
    'GetMouseWheelMotionFactor'), ('pick_color', 'GetPickColor'),
    ('timer_duration', 'GetTimerDuration'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('priority', 'GetPriority'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['auto_adjust_camera_clipping_range', 'debug', 'enabled',
    'global_warning_display', 'handle_observers', 'key_press_activation',
    'picking_managed', 'use_timers', 'interaction_mode',
    'current_image_number', 'high_light_width',
    'key_press_activation_value', 'label_field', 'motion_factor',
    'mouse_wheel_motion_factor', 'pick_color', 'priority',
    'selection_width', 'timer_duration', 'x_view_right_vector',
    'x_view_up_vector', 'y_view_right_vector', 'y_view_up_vector',
    'z_view_right_vector', 'z_view_up_vector'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InteractorStyleTreeMapHover, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InteractorStyleTreeMapHover properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_adjust_camera_clipping_range', 'enabled',
            'handle_observers', 'key_press_activation', 'picking_managed',
            'use_timers'], ['interaction_mode'], ['current_image_number',
            'high_light_width', 'key_press_activation_value', 'label_field',
            'motion_factor', 'mouse_wheel_motion_factor', 'pick_color',
            'priority', 'selection_width', 'timer_duration',
            'x_view_right_vector', 'x_view_up_vector', 'y_view_right_vector',
            'y_view_up_vector', 'z_view_right_vector', 'z_view_up_vector']),
            title='Edit InteractorStyleTreeMapHover properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InteractorStyleTreeMapHover properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class ImageCroppingRegionsWidget(ThreeDWidget):
    """
    ImageCroppingRegionsWidget - widget for cropping an image
    
    Superclass: ThreeDWidget
    
    This widget displays a set of axis aligned lines that can be
    interactively manipulated to crop a volume. The region to be cropped
    away is displayed in a different highlight. Much like the
    VolumeMapper, this widget supports 27 possible configurations of
    cropping planes. (See cropping_region_flags). If a volume mapper is
    set, the cropping planes are directly propagated to the volume
    mapper. The widget invokes a cropping_planes_position_changed_event when
    the position of any of the cropping planes is changed. The widget
    also invokes an interaction_event in response to user interaction.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageCroppingRegionsWidget, obj, update, **traits)
    
    def setup_observers(self):
        """Setup the observers for the object."""
        super(ImageCroppingRegionsWidget, self).setup_observers()
        tvtk_base._object_cache.setup_observers(self._vtk_obj,
                                      'EndInteractionEvent',
                                      self.update_traits)
    slice_orientation = traits.Trait('xy',
    tvtk_base.TraitRevPrefixMap({'xy': 2, 'xz': 1, 'yz': 0}), help=\
        """
        
        """
    )

    def _slice_orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceOrientation,
                        self.slice_orientation_)

    cropping_region_flags = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the cropping region flags
        """
    )

    def _cropping_region_flags_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCroppingRegionFlags,
                        self.cropping_region_flags)

    line1_color = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Set/Get line 1 color
        """
    )

    def _line1_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLine1Color,
                        self.line1_color)

    line2_color = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Set/Get line 2 color
        """
    )

    def _line2_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLine2Color,
                        self.line2_color)

    line3_color = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Set/Get line 3 color
        """
    )

    def _line3_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLine3Color,
                        self.line3_color)

    line4_color = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Set/Get line 4 color
        """
    )

    def _line4_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLine4Color,
                        self.line4_color)

    plane_positions = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(0.0, 1.0, 0.0, 1.0, 0.0, 1.0), cols=3, help=\
        """
        Set/Get the plane positions that represent the cropped region.
        """
    )

    def _plane_positions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlanePositions,
                        self.plane_positions)

    slice = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the slice number
        """
    )

    def _slice_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSlice,
                        self.slice)

    def _get_volume_mapper(self):
        return wrap_vtk(self._vtk_obj.GetVolumeMapper())
    def _set_volume_mapper(self, arg):
        old_val = self._get_volume_mapper()
        self._wrap_call(self._vtk_obj.SetVolumeMapper,
                        deref_vtk(arg))
        self.trait_property_changed('volume_mapper', old_val, arg)
    volume_mapper = traits.Property(_get_volume_mapper, _set_volume_mapper, help=\
        """
        Set/Get the input volume mapper Update the widget according to
        its mapper
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

    def move_horizontal_line(self):
        """
        V.move_horizontal_line()
        C++: void MoveHorizontalLine()
        Callbacks for user interaction.
        """
        ret = self._vtk_obj.MoveHorizontalLine()
        return ret
        

    def move_intersecting_lines(self):
        """
        V.move_intersecting_lines()
        C++: void MoveIntersectingLines()
        Callbacks for user interaction.
        """
        ret = self._vtk_obj.MoveIntersectingLines()
        return ret
        

    def move_vertical_line(self):
        """
        V.move_vertical_line()
        C++: void MoveVerticalLine()
        Callbacks for user interaction.
        """
        ret = self._vtk_obj.MoveVerticalLine()
        return ret
        

    def on_button_press(self):
        """
        V.on_button_press()
        C++: void OnButtonPress()
        Callbacks for user interaction.
        """
        ret = self._vtk_obj.OnButtonPress()
        return ret
        

    def on_button_release(self):
        """
        V.on_button_release()
        C++: void OnButtonRelease()
        Callbacks for user interaction.
        """
        ret = self._vtk_obj.OnButtonRelease()
        return ret
        

    def on_mouse_move(self):
        """
        V.on_mouse_move()
        C++: void OnMouseMove()
        Callbacks for user interaction.
        """
        ret = self._vtk_obj.OnMouseMove()
        return ret
        

    def update_according_to_input(self):
        """
        V.update_according_to_input()
        C++: virtual void UpdateAccordingToInput()
        Set/Get the input volume mapper Update the widget according to
        its mapper
        """
        ret = self._vtk_obj.UpdateAccordingToInput()
        return ret
        

    def update_cursor_icon(self):
        """
        V.update_cursor_icon()
        C++: void UpdateCursorIcon()
        Callbacks for user interaction.
        """
        ret = self._vtk_obj.UpdateCursorIcon()
        return ret
        

    _updateable_traits_ = \
    (('enabled', 'GetEnabled'), ('key_press_activation',
    'GetKeyPressActivation'), ('picking_managed', 'GetPickingManaged'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('slice_orientation',
    'GetSliceOrientation'), ('cropping_region_flags',
    'GetCroppingRegionFlags'), ('plane_positions', 'GetPlanePositions'),
    ('slice', 'GetSlice'), ('handle_size', 'GetHandleSize'),
    ('place_factor', 'GetPlaceFactor'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('priority', 'GetPriority'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'picking_managed', 'slice_orientation',
    'cropping_region_flags', 'handle_size', 'key_press_activation_value',
    'place_factor', 'plane_positions', 'priority', 'slice'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageCroppingRegionsWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageCroppingRegionsWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'picking_managed'],
            ['slice_orientation'], ['cropping_region_flags', 'handle_size',
            'key_press_activation_value', 'place_factor', 'plane_positions',
            'priority', 'slice']),
            title='Edit ImageCroppingRegionsWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageCroppingRegionsWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


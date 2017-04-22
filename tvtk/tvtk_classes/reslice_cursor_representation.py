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

from tvtk.tvtk_classes.widget_representation import WidgetRepresentation


class ResliceCursorRepresentation(WidgetRepresentation):
    """
    ResliceCursorRepresentation - represent the ResliceCursorWidget
    
    Superclass: WidgetRepresentation
    
    This class is the base class for the reslice cursor representation
    subclasses. It represents a cursor that may be interactively
    translated, rotated through an image and perform thick / thick
    reformats.
    @sa
    ResliceCursorLineRepresentation
    ResliceCursorThickLineRepresentation ResliceCursorWidget
    ResliceCursor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkResliceCursorRepresentation, obj, update, **traits)
    
    display_text = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable text display of window-level, image coordinates
        and scalar values in a render window.
        """
    )

    def _display_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayText,
                        self.display_text_)

    restrict_plane_to_volume = tvtk_base.true_bool_trait(help=\
        """
        Make sure that the resliced image remains within the volume.
        Default is On.
        """
    )

    def _restrict_plane_to_volume_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRestrictPlaneToVolume,
                        self.restrict_plane_to_volume_)

    show_resliced_image = tvtk_base.true_bool_trait(help=\
        """
        Show the resliced image ?
        """
    )

    def _show_resliced_image_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowReslicedImage,
                        self.show_resliced_image_)

    use_image_actor = tvtk_base.false_bool_trait(help=\
        """
        Render as a 2d image, or render as a plane with a texture in
        physical space.
        """
    )

    def _use_image_actor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseImageActor,
                        self.use_image_actor_)

    def _get_color_map(self):
        return wrap_vtk(self._vtk_obj.GetColorMap())
    def _set_color_map(self, arg):
        old_val = self._get_color_map()
        self._wrap_call(self._vtk_obj.SetColorMap,
                        deref_vtk(arg))
        self.trait_property_changed('color_map', old_val, arg)
    color_map = traits.Property(_get_color_map, _set_color_map, help=\
        """
        Convenience method to get the ImageMapToColors filter used by
        this widget.  The user can properly render other transparent
        actors in a scene by calling the filter's set_output_format_to_rgb
        and pass_alpha_to_output_off.
        """
    )

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Set/Get the internal lookuptable (lut) to one defined by the
        user, or, alternatively, to the lut of another Reslice cusror
        widget.  In this way, a set of three orthogonal planes can share
        the same lut so that window-levelling is performed uniformly
        among planes.  The default internal lut can be re- set/allocated
        by setting to 0 (NULL).
        """
    )

    manipulation_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        INTERNAL - Do not use Set the manipulation mode. This is done by
        the widget
        """
    )

    def _manipulation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetManipulationMode,
                        self.manipulation_mode)

    def _get_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTextProperty())
    def _set_text_property(self, arg):
        old_val = self._get_text_property()
        self._wrap_call(self._vtk_obj.SetTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('text_property', old_val, arg)
    text_property = traits.Property(_get_text_property, _set_text_property, help=\
        """
        Set/Get the text property for the image data and window-level
        annotation.
        """
    )

    thickness_label_format = traits.String('%0.3g', enter_set=True, auto_set=False, help=\
        """
        Specify the format to use for labelling the distance. Note that
        an empty string results in no label, or a format string without a
        "%" character will not print the thickness value.
        """
    )

    def _thickness_label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThicknessLabelFormat,
                        self.thickness_label_format)

    tolerance = traits.Trait(5, traits.Range(1, 100, enter_set=True, auto_set=False), help=\
        """
        The tolerance representing the distance to the representation (in
        pixels) in which the cursor is considered near enough to the
        representation to be active.
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def get_window_level(self, *args):
        """
        V.get_window_level([float, float])
        C++: void GetWindowLevel(double wl[2])
        Set/Get the current window and level values.  set_window_level
        should only be called after set_input.  If a shared lookup table
        is being used, a callback is required to update the window level
        values without having to update the lookup table again.
        """
        ret = self._wrap_call(self._vtk_obj.GetWindowLevel, *args)
        return ret

    def set_window_level(self, *args):
        """
        V.set_window_level(float, float, int)
        C++: void SetWindowLevel(double window, double level, int copy=0)
        Set/Get the current window and level values.  set_window_level
        should only be called after set_input.  If a shared lookup table
        is being used, a callback is required to update the window level
        values without having to update the lookup table again.
        """
        ret = self._wrap_call(self._vtk_obj.SetWindowLevel, *args)
        return ret

    def _get_cursor_algorithm(self):
        return wrap_vtk(self._vtk_obj.GetCursorAlgorithm())
    cursor_algorithm = traits.Property(_get_cursor_algorithm, help=\
        """
        Get the underlying cursor source.
        """
    )

    def _get_image_actor(self):
        return wrap_vtk(self._vtk_obj.GetImageActor())
    image_actor = traits.Property(_get_image_actor, help=\
        """
        Get the displayed image actor
        """
    )

    def _get_level(self):
        return self._vtk_obj.GetLevel()
    level = traits.Property(_get_level, help=\
        """
        Set/Get the current window and level values.  set_window_level
        should only be called after set_input.  If a shared lookup table
        is being used, a callback is required to update the window level
        values without having to update the lookup table again.
        """
    )

    def _get_plane_source(self):
        return wrap_vtk(self._vtk_obj.GetPlaneSource())
    plane_source = traits.Property(_get_plane_source, help=\
        """
        Get the plane source on which the texture (the thin/thick
        resliced image is displayed)
        """
    )

    def _get_reslice(self):
        return wrap_vtk(self._vtk_obj.GetReslice())
    reslice = traits.Property(_get_reslice, help=\
        """
        Get the current reslice class and reslice axes
        """
    )

    def _get_reslice_axes(self):
        return wrap_vtk(self._vtk_obj.GetResliceAxes())
    reslice_axes = traits.Property(_get_reslice_axes, help=\
        """
        Get the current reslice class and reslice axes
        """
    )

    def _get_reslice_cursor(self):
        return wrap_vtk(self._vtk_obj.GetResliceCursor())
    reslice_cursor = traits.Property(_get_reslice_cursor, help=\
        """
        
        """
    )

    def _get_thickness_label_position(self):
        return self._vtk_obj.GetThicknessLabelPosition()
    thickness_label_position = traits.Property(_get_thickness_label_position, help=\
        """
        Get the position of the widget's label in display coordinates.
        """
    )

    def _get_thickness_label_text(self):
        return self._vtk_obj.GetThicknessLabelText()
    thickness_label_text = traits.Property(_get_thickness_label_text, help=\
        """
        Get the text shown in the widget's label.
        """
    )

    def _get_window(self):
        return self._vtk_obj.GetWindow()
    window = traits.Property(_get_window, help=\
        """
        Set/Get the current window and level values.  set_window_level
        should only be called after set_input.  If a shared lookup table
        is being used, a callback is required to update the window level
        values without having to update the lookup table again.
        """
    )

    def get_world_thickness_label_position(self, *args):
        """
        V.get_world_thickness_label_position([float, float, float])
        C++: virtual void GetWorldThicknessLabelPosition(double pos[3])
        Get the position of the widget's label in display coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetWorldThicknessLabelPosition, *args)
        return ret

    def activate_text(self, *args):
        """
        V.activate_text(int)
        C++: void ActivateText(int)
        INTERNAL - Do not use. Internal methods used by the widget to
        manage text displays for annotations.
        """
        ret = self._wrap_call(self._vtk_obj.ActivateText, *args)
        return ret

    def initialize_reslice_plane(self):
        """
        V.initialize_reslice_plane()
        C++: virtual void InitializeReslicePlane()
        Initialize the reslice planes and the camera center. This is done
        automatically, the first time we render.
        """
        ret = self._vtk_obj.InitializeReslicePlane()
        return ret
        

    def manage_text_display(self):
        """
        V.manage_text_display()
        C++: void ManageTextDisplay()
        INTERNAL - Do not use. Internal methods used by the widget to
        manage text displays for annotations.
        """
        ret = self._vtk_obj.ManageTextDisplay()
        return ret
        

    def reset_camera(self):
        """
        V.reset_camera()
        C++: virtual void ResetCamera()
        Initialize the reslice planes and the camera center. This is done
        automatically, the first time we render.
        """
        ret = self._vtk_obj.ResetCamera()
        return ret
        

    _updateable_traits_ = \
    (('display_text', 'GetDisplayText'), ('restrict_plane_to_volume',
    'GetRestrictPlaneToVolume'), ('show_resliced_image',
    'GetShowReslicedImage'), ('use_image_actor', 'GetUseImageActor'),
    ('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('manipulation_mode',
    'GetManipulationMode'), ('thickness_label_format',
    'GetThicknessLabelFormat'), ('tolerance', 'GetTolerance'),
    ('handle_size', 'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'display_text', 'dragable', 'global_warning_display',
    'need_to_render', 'pickable', 'picking_managed',
    'restrict_plane_to_volume', 'show_resliced_image', 'use_bounds',
    'use_image_actor', 'visibility', 'estimated_render_time',
    'handle_size', 'manipulation_mode', 'place_factor',
    'render_time_multiplier', 'thickness_label_format', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ResliceCursorRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ResliceCursorRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['display_text', 'need_to_render', 'picking_managed',
            'restrict_plane_to_volume', 'show_resliced_image', 'use_bounds',
            'use_image_actor', 'visibility'], [], ['estimated_render_time',
            'handle_size', 'manipulation_mode', 'place_factor',
            'render_time_multiplier', 'thickness_label_format', 'tolerance']),
            title='Edit ResliceCursorRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ResliceCursorRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


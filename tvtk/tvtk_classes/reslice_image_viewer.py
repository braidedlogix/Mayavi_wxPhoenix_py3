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

from tvtk.tvtk_classes.image_viewer2 import ImageViewer2


class ResliceImageViewer(ImageViewer2):
    """
    ResliceImageViewer - Display an image along with a reslice cursor
    
    Superclass: ImageViewer2
    
    This class is similar to ImageViewer2. It displays the image along
    with a two cross hairs for reslicing. The cross hairs may be
    interactively manipulated and are typically used to reslice two other
    views of ResliceImageViewer. See qt_vtk_render_windows for an
    example. The reslice cursor is used to perform thin or thick MPR
    through data. The class can also default to the behaviour of
    ImageViewer2 if the Reslice mode is set to RESLICE_AXIS_ALIGNED.
    @sa
    ResliceCursor ResliceCursorWidget
    ResliceCursorRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkResliceImageViewer, obj, update, **traits)
    
    slice_scroll_on_mouse_wheel = tvtk_base.true_bool_trait(help=\
        """
        Scroll slices on the mouse wheel ? In the case of MPR view, it
        moves one "normalized spacing" in the direction of the normal to
        the resliced plane, provided the new center will continue to lie
        within the volume.
        """
    )

    def _slice_scroll_on_mouse_wheel_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceScrollOnMouseWheel,
                        self.slice_scroll_on_mouse_wheel_)

    def get_reslice_mode(self):
        """
        V.get_reslice_mode() -> int
        C++: int GetResliceMode()"""
        ret = self._vtk_obj.GetResliceMode()
        return ret
        

    def set_reslice_mode_to_oblique(self):
        """
        V.set_reslice_mode_to_oblique()
        C++: virtual void SetResliceModeToOblique()"""
        self._vtk_obj.SetResliceModeToOblique()

    color_level = traits.Float(127.5, enter_set=True, auto_set=False, help=\
        """
        Set window and level for mapping pixels to colors.
        """
    )

    def _color_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorLevel,
                        self.color_level)

    color_window = traits.Float(255.0, enter_set=True, auto_set=False, help=\
        """
        Set window and level for mapping pixels to colors.
        """
    )

    def _color_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorWindow,
                        self.color_window)

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Set the lookup table
        """
    )

    def _get_reslice_cursor(self):
        return wrap_vtk(self._vtk_obj.GetResliceCursor())
    def _set_reslice_cursor(self, arg):
        old_val = self._get_reslice_cursor()
        self._wrap_call(self._vtk_obj.SetResliceCursor,
                        deref_vtk(arg))
        self.trait_property_changed('reslice_cursor', old_val, arg)
    reslice_cursor = traits.Property(_get_reslice_cursor, _set_reslice_cursor, help=\
        """
        Set/Get the reslice cursor.
        """
    )

    thick_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Switch to / from thick mode
        """
    )

    def _thick_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThickMode,
                        self.thick_mode)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input image to the viewer.
        """
    )

    def _get_interactor(self):
        return wrap_vtk(self._vtk_obj.GetInteractor())
    interactor = traits.Property(_get_interactor, help=\
        """
        Get the render window interactor
        """
    )

    def _get_measurements(self):
        return wrap_vtk(self._vtk_obj.GetMeasurements())
    measurements = traits.Property(_get_measurements, help=\
        """
        Get the measurements manager
        """
    )

    def _get_point_placer(self):
        return wrap_vtk(self._vtk_obj.GetPointPlacer())
    point_placer = traits.Property(_get_point_placer, help=\
        """
        Get the point placer.
        """
    )

    def _get_reslice_cursor_widget(self):
        return wrap_vtk(self._vtk_obj.GetResliceCursorWidget())
    reslice_cursor_widget = traits.Property(_get_reslice_cursor_widget, help=\
        """
        Get the internal render window, renderer, image actor, and image
        map instances.
        """
    )

    def increment_slice(self, *args):
        """
        V.increment_slice(int)
        C++: virtual void IncrementSlice(int n)
        Increment/Decrement slice by 'n' slices
        """
        ret = self._wrap_call(self._vtk_obj.IncrementSlice, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: virtual void Reset()
        Reset all views back to initial state
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    _updateable_traits_ = \
    (('slice_scroll_on_mouse_wheel', 'GetSliceScrollOnMouseWheel'),
    ('off_screen_rendering', 'GetOffScreenRendering'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('slice_orientation', 'GetSliceOrientation'), ('color_level',
    'GetColorLevel'), ('color_window', 'GetColorWindow'), ('thick_mode',
    'GetThickMode'), ('slice', 'GetSlice'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'off_screen_rendering',
    'slice_scroll_on_mouse_wheel', 'slice_orientation', 'color_level',
    'color_window', 'slice', 'thick_mode'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ResliceImageViewer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ResliceImageViewer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['off_screen_rendering', 'slice_scroll_on_mouse_wheel'],
            ['slice_orientation'], ['color_level', 'color_window', 'slice',
            'thick_mode']),
            title='Edit ResliceImageViewer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ResliceImageViewer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


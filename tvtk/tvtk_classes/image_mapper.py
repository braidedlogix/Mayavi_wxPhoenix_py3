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

from tvtk.tvtk_classes.mapper2d import Mapper2D


class ImageMapper(Mapper2D):
    """
    ImageMapper - 2d image display
    
    Superclass: Mapper2D
    
    ImageMapper provides 2d image display support for vtk. It is a
    mapper2d subclass that can be associated with an actor2d and placed
    within a render_window or image_window. The ImageMapper is a 2d
    mapper, which means that it displays images in display coordinates.
    In display coordinates, one image pixel is always one screen pixel.
    
    @sa
    Mapper2D Actor2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMapper, obj, update, **traits)
    
    render_to_rectangle = tvtk_base.false_bool_trait(help=\
        """
        If render_to_rectangle is set (by default not), then the
        imagemapper will render the image into the rectangle supplied by
        the actor2d's position_coordinate and position2_coordinate
        """
    )

    def _render_to_rectangle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRenderToRectangle,
                        self.render_to_rectangle_)

    use_custom_extents = tvtk_base.false_bool_trait(help=\
        """
        Usually, the entire image is displayed, if use_custom_extents is
        set (by default not), then the region supplied in the
        custom_display_extents is used in preference. Note that the Custom
        extents are x,y only and the zslice is still applied
        """
    )

    def _use_custom_extents_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseCustomExtents,
                        self.use_custom_extents_)

    color_level = traits.Float(1000.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the level value for window/level
        """
    )

    def _color_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorLevel,
                        self.color_level)

    color_window = traits.Float(2000.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the window value for window/level
        """
    )

    def _color_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorWindow,
                        self.color_window)

    custom_display_extents = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=int, value=(0, 0, 0, 0), cols=3, help=\
        """
        The image extents which should be displayed with use_custom_extents
        Note that the Custom extents are x,y only and the zslice is still
        applied
        """
    )

    def _custom_display_extents_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCustomDisplayExtents,
                        self.custom_display_extents)

    z_slice = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the current slice number. The axis Z in ZSlice does not
        necessarily have any relation to the z axis of the data on disk.
        It is simply the axis orthogonal to the x,y, display plane.
        get_whole_z_max and Min are convenience methods for obtaining the
        number of slices that can be displayed. Again the number of
        slices is in reference to the display z axis, which is not
        necessarily the z axis on disk. (due to reformatting etc)
        """
    )

    def _z_slice_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZSlice,
                        self.z_slice)

    def _get_color_scale(self):
        return self._vtk_obj.GetColorScale()
    color_scale = traits.Property(_get_color_scale, help=\
        """
        Methods used internally for performing the Window/Level mapping.
        """
    )

    def _get_color_shift(self):
        return self._vtk_obj.GetColorShift()
    color_shift = traits.Property(_get_color_shift, help=\
        """
        Methods used internally for performing the Window/Level mapping.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set the Input of a filter.
        """
    )

    def _get_whole_z_max(self):
        return self._vtk_obj.GetWholeZMax()
    whole_z_max = traits.Property(_get_whole_z_max, help=\
        """
        Set/Get the current slice number. The axis Z in ZSlice does not
        necessarily have any relation to the z axis of the data on disk.
        It is simply the axis orthogonal to the x,y, display plane.
        get_whole_z_max and Min are convenience methods for obtaining the
        number of slices that can be displayed. Again the number of
        slices is in reference to the display z axis, which is not
        necessarily the z axis on disk. (due to reformatting etc)
        """
    )

    def _get_whole_z_min(self):
        return self._vtk_obj.GetWholeZMin()
    whole_z_min = traits.Property(_get_whole_z_min, help=\
        """
        Set/Get the current slice number. The axis Z in ZSlice does not
        necessarily have any relation to the z axis of the data on disk.
        It is simply the axis orthogonal to the x,y, display plane.
        get_whole_z_max and Min are convenience methods for obtaining the
        number of slices that can be displayed. Again the number of
        slices is in reference to the display z axis, which is not
        necessarily the z axis on disk. (due to reformatting etc)
        """
    )

    def render_data(self, *args):
        """
        V.render_data(Viewport, ImageData, Actor2D)
        C++: virtual void RenderData(Viewport *, ImageData *,
            Actor2D *)
        Function called by Render to actually draw the image to to the
        screen
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderData, *my_args)
        return ret

    def render_start(self, *args):
        """
        V.render_start(Viewport, Actor2D)
        C++: void RenderStart(Viewport *viewport, Actor2D *actor)
        Draw the image to the screen.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderStart, *my_args)
        return ret

    def set_input_data(self, *args):
        """
        V.set_input_data(ImageData)
        C++: virtual void SetInputData(ImageData *input)
        Set the Input of a filter.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    _updateable_traits_ = \
    (('render_to_rectangle', 'GetRenderToRectangle'),
    ('use_custom_extents', 'GetUseCustomExtents'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('color_level', 'GetColorLevel'),
    ('color_window', 'GetColorWindow'), ('custom_display_extents',
    'GetCustomDisplayExtents'), ('z_slice', 'GetZSlice'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'render_to_rectangle', 'use_custom_extents',
    'color_level', 'color_window', 'custom_display_extents',
    'progress_text', 'z_slice'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['render_to_rectangle', 'use_custom_extents'], [],
            ['color_level', 'color_window', 'custom_display_extents', 'z_slice']),
            title='Edit ImageMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


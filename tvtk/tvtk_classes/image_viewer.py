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

from tvtk.tvtk_classes.object import Object


class ImageViewer(Object):
    """
    ImageViewer - Display a 2d image.
    
    Superclass: Object
    
    ImageViewer is a convenience class for displaying a 2d image.  It
    packages up the functionality found in RenderWindow, Renderer,
    Actor2D and ImageMapper into a single easy to use class. 
    Behind the scenes these four classes are actually used to to provide
    the required functionality. ImageViewer is simply a wrapper around
    them.
    
    @sa
    RenderWindow Renderer ImageMapper Actor2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageViewer, obj, update, **traits)
    
    off_screen_rendering = tvtk_base.false_bool_trait(help=\
        """
        Create a window in memory instead of on the screen. This may not
        be supported for every type of window and on some windows you may
        need to invoke this prior to the first render.
        """
    )

    def _off_screen_rendering_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffScreenRendering,
                        self.off_screen_rendering_)

    color_level = traits.Float(1000.0, enter_set=True, auto_set=False, help=\
        """
        Sets window/level for mapping pixels to colors.
        """
    )

    def _color_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorLevel,
                        self.color_level)

    color_window = traits.Float(2000.0, enter_set=True, auto_set=False, help=\
        """
        Sets window/level for mapping pixels to colors.
        """
    )

    def _color_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorWindow,
                        self.color_window)

    position = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        Set/Get the position in screen coordinates of the rendering
        window.
        """
    )

    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        Set/Get the size of the window in screen coordinates in pixels.
        """
    )

    def _size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSize,
                        self.size)

    z_slice = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the current Z Slice to display
        """
    )

    def _z_slice_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZSlice,
                        self.z_slice)

    def _get_actor2d(self):
        return wrap_vtk(self._vtk_obj.GetActor2D())
    actor2d = traits.Property(_get_actor2d, help=\
        """
        Get the internal objects
        """
    )

    def _get_image_mapper(self):
        return wrap_vtk(self._vtk_obj.GetImageMapper())
    image_mapper = traits.Property(_get_image_mapper, help=\
        """
        Get the internal objects
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input to the viewer.
        """
    )

    def _get_render_window(self):
        return wrap_vtk(self._vtk_obj.GetRenderWindow())
    render_window = traits.Property(_get_render_window, help=\
        """
        Get the internal objects
        """
    )

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    renderer = traits.Property(_get_renderer, help=\
        """
        Get the internal objects
        """
    )

    def _get_whole_z_max(self):
        return self._vtk_obj.GetWholeZMax()
    whole_z_max = traits.Property(_get_whole_z_max, help=\
        """
        What is the possible Min/ Max z slices available.
        """
    )

    def _get_whole_z_min(self):
        return self._vtk_obj.GetWholeZMin()
    whole_z_min = traits.Property(_get_whole_z_min, help=\
        """
        What is the possible Min/ Max z slices available.
        """
    )

    def _get_window_name(self):
        return self._vtk_obj.GetWindowName()
    window_name = traits.Property(_get_window_name, help=\
        """
        Get name of rendering window
        """
    )

    def render(self):
        """
        V.render()
        C++: virtual void Render(void)
        Render the resulting image.
        """
        ret = self._vtk_obj.Render()
        return ret
        

    def set_display_id(self, *args):
        """
        V.set_display_id(void)
        C++: void SetDisplayId(void *a)
        These are here for using a tk window.
        """
        ret = self._wrap_call(self._vtk_obj.SetDisplayId, *args)
        return ret

    def set_input_connection(self, *args):
        """
        V.set_input_connection(AlgorithmOutput)
        C++: virtual void SetInputConnection(AlgorithmOutput *input)
        Set/Get the input to the viewer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputConnection, *my_args)
        return ret

    def set_input_data(self, *args):
        """
        V.set_input_data(ImageData)
        C++: void SetInputData(ImageData *in)
        Set/Get the input to the viewer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    def set_parent_id(self, *args):
        """
        V.set_parent_id(void)
        C++: void SetParentId(void *a)
        These are here for using a tk window.
        """
        ret = self._wrap_call(self._vtk_obj.SetParentId, *args)
        return ret

    def set_window_id(self, *args):
        """
        V.set_window_id(void)
        C++: void SetWindowId(void *a)
        These are here for using a tk window.
        """
        ret = self._wrap_call(self._vtk_obj.SetWindowId, *args)
        return ret

    def setup_interactor(self, *args):
        """
        V.setup_interactor(RenderWindowInteractor)
        C++: void SetupInteractor(RenderWindowInteractor *)
        Create and attach an interactor for this window
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetupInteractor, *my_args)
        return ret

    _updateable_traits_ = \
    (('off_screen_rendering', 'GetOffScreenRendering'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('color_level', 'GetColorLevel'), ('color_window', 'GetColorWindow'),
    ('position', 'GetPosition'), ('size', 'GetSize'), ('z_slice',
    'GetZSlice'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'off_screen_rendering',
    'color_level', 'color_window', 'position', 'size', 'z_slice'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageViewer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageViewer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['off_screen_rendering'], [], ['color_level', 'color_window',
            'position', 'size', 'z_slice']),
            title='Edit ImageViewer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageViewer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


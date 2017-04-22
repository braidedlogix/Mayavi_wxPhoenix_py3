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


class ImageViewer2(Object):
    """
    ImageViewer2 - Display a 2d image.
    
    Superclass: Object
    
    ImageViewer2 is a convenience class for displaying a 2d image.  It
    packages up the functionality found in RenderWindow, Renderer,
    ImageActor and ImageMapToWindowLevelColors into a single easy
    to use class.  This class also creates an image interactor style
    (vtk_interactor_style_image) that allows zooming and panning of images,
    and supports interactive window/level operations on the image. Note
    that ImageViewer2 is simply a wrapper around these classes.
    
    ImageViewer2 uses the 3d rendering and texture mapping engine to
    draw an image on a plane.  This allows for rapid rendering, zooming,
    and panning. The image is placed in the 3d scene at a depth based on
    the z-coordinate of the particular image slice. Each call to
    set_slice() changes the image data (slice) displayed AND changes the
    depth of the displayed slice in the 3d scene. This can be controlled
    by the auto_adjust_camera_clipping_range ivar of the interactor_style
    member.
    
    It is possible to mix images and geometry, using the methods:
    
    viewer->_set_input_connection( image_source->_get_output_port() ); // or
    viewer->_set_input_data ( image ); viewer->_get_renderer()->_add_actor(
    my_actor );
    
    This can be used to annotate an image with a poly_data of "edges" or
    or highlight sections of an image or display a 3d isosurface with a
    slice from the volume, etc. Any portions of your geometry that are in
    front of the displayed slice will be visible; any portions of your
    geometry that are behind the displayed slice will be obscured. A more
    general framework (with respect to viewing direction) for achieving
    this effect is provided by the ImagePlaneWidget .
    
    Note that pressing 'r' will reset the window/level and pressing
    shift+'r' or control+'r' will reset the camera.
    
    @sa
    RenderWindow Renderer ImageActor
    ImageMapToWindowLevelColors
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageViewer2, obj, update, **traits)
    
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

    slice_orientation = traits.Trait('xy',
    tvtk_base.TraitRevPrefixMap({'xy': 2, 'xz': 1, 'yz': 0}), help=\
        """
        
        """
    )

    def _slice_orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceOrientation,
                        self.slice_orientation_)

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

    position = traits.Trait((traits.Undefined, traits.Undefined), traits.Array(shape=(2,), dtype=int, value=(0, 0), cols=2), enter_set=True, auto_set=False, help=\
        """
        Set/Get the position in screen coordinates of the rendering
        window.
        """
    )

    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    def _get_render_window(self):
        return wrap_vtk(self._vtk_obj.GetRenderWindow())
    def _set_render_window(self, arg):
        old_val = self._get_render_window()
        self._wrap_call(self._vtk_obj.SetRenderWindow,
                        deref_vtk(arg))
        self.trait_property_changed('render_window', old_val, arg)
    render_window = traits.Property(_get_render_window, _set_render_window, help=\
        """
        Get the internal render window, renderer, image actor, and image
        map instances.
        """
    )

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        Get the internal render window, renderer, image actor, and image
        map instances.
        """
    )

    size = traits.Trait((traits.Undefined, traits.Undefined), traits.Array(shape=(2,), dtype=int, value=(0, 0), cols=2), enter_set=True, auto_set=False, help=\
        """
        Set/Get the size of the window in screen coordinates in pixels.
        """
    )

    def _size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSize,
                        self.size)

    slice = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the current slice to display (depending on the
        orientation this can be in X, Y or Z).
        """
    )

    def _slice_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSlice,
                        self.slice)

    def _get_image_actor(self):
        return wrap_vtk(self._vtk_obj.GetImageActor())
    image_actor = traits.Property(_get_image_actor, help=\
        """
        Get the internal render window, renderer, image actor, and image
        map instances.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input image to the viewer.
        """
    )

    def _get_interactor_style(self):
        return wrap_vtk(self._vtk_obj.GetInteractorStyle())
    interactor_style = traits.Property(_get_interactor_style, help=\
        """
        Get the internal render window, renderer, image actor, and image
        map instances.
        """
    )

    def _get_slice_max(self):
        return self._vtk_obj.GetSliceMax()
    slice_max = traits.Property(_get_slice_max, help=\
        """
        Return the minimum and maximum slice values (depending on the
        orientation this can be in X, Y or Z).
        """
    )

    def _get_slice_min(self):
        return self._vtk_obj.GetSliceMin()
    slice_min = traits.Property(_get_slice_min, help=\
        """
        Return the minimum and maximum slice values (depending on the
        orientation this can be in X, Y or Z).
        """
    )

    def _get_slice_range(self):
        return self._vtk_obj.GetSliceRange()
    slice_range = traits.Property(_get_slice_range, help=\
        """
        Return the minimum and maximum slice values (depending on the
        orientation this can be in X, Y or Z).
        """
    )

    def _get_window_level(self):
        return wrap_vtk(self._vtk_obj.GetWindowLevel())
    window_level = traits.Property(_get_window_level, help=\
        """
        Get the internal render window, renderer, image actor, and image
        map instances.
        """
    )

    def _get_window_name(self):
        return self._vtk_obj.GetWindowName()
    window_name = traits.Property(_get_window_name, help=\
        """
        Get the name of rendering window.
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
        C++: virtual void SetDisplayId(void *a)
        These are here when using a Tk window.
        """
        ret = self._wrap_call(self._vtk_obj.SetDisplayId, *args)
        return ret

    def set_input_connection(self, *args):
        """
        V.set_input_connection(AlgorithmOutput)
        C++: virtual void SetInputConnection(AlgorithmOutput *input)
        Set/Get the input image to the viewer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputConnection, *my_args)
        return ret

    def set_input_data(self, *args):
        """
        V.set_input_data(ImageData)
        C++: virtual void SetInputData(ImageData *in)
        Set/Get the input image to the viewer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    def set_parent_id(self, *args):
        """
        V.set_parent_id(void)
        C++: virtual void SetParentId(void *a)
        These are here when using a Tk window.
        """
        ret = self._wrap_call(self._vtk_obj.SetParentId, *args)
        return ret

    def set_window_id(self, *args):
        """
        V.set_window_id(void)
        C++: virtual void SetWindowId(void *a)
        These are here when using a Tk window.
        """
        ret = self._wrap_call(self._vtk_obj.SetWindowId, *args)
        return ret

    def setup_interactor(self, *args):
        """
        V.setup_interactor(RenderWindowInteractor)
        C++: virtual void SetupInteractor(RenderWindowInteractor *)
        Attach an interactor for the internal render window.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetupInteractor, *my_args)
        return ret

    def update_display_extent(self):
        """
        V.update_display_extent()
        C++: virtual void UpdateDisplayExtent()
        Update the display extent manually so that the proper slice for
        the given orientation is displayed. It will also try to set a
        reasonable camera clipping range. This method is called
        automatically when the Input is changed, but most of the time the
        input of this class is likely to remain the same, i.e. connected
        to the output of a filter, or an image reader. When the input of
        this filter or reader itself is changed, an error message might
        be displayed since the current display extent is probably outside
        the new whole extent. Calling this method will ensure that the
        display extent is reset properly.
        """
        ret = self._vtk_obj.UpdateDisplayExtent()
        return ret
        

    _updateable_traits_ = \
    (('off_screen_rendering', 'GetOffScreenRendering'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('slice_orientation', 'GetSliceOrientation'), ('color_level',
    'GetColorLevel'), ('color_window', 'GetColorWindow'), ('slice',
    'GetSlice'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'off_screen_rendering',
    'slice_orientation', 'color_level', 'color_window', 'slice'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageViewer2, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageViewer2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['off_screen_rendering'], ['slice_orientation'], ['color_level',
            'color_window', 'slice']),
            title='Edit ImageViewer2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageViewer2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


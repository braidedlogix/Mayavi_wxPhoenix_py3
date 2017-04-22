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

from tvtk.tvtk_classes.image_mapper import ImageMapper


class OpenGLImageMapper(ImageMapper):
    """
    OpenGLImageMapper - 2d image display support for open_gl
    
    Superclass: ImageMapper
    
    OpenGLImageMapper is a concrete subclass of ImageMapper that
    renders images under open_gl
    
    @warning
    OpenGLImageMapper does not support BitArray, you have to
    convert the array first to UnsignedCharArray (for example)
    
    @sa
    ImageMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLImageMapper, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set the Input of a filter.
        """
    )

    def draw_pixels(self, *args):
        """
        V.draw_pixels(Viewport, int, int, int, void)
        C++: void DrawPixels(Viewport *vp, int width, int height,
            int numComponents, void *data)
        draw the data once it has been converted to uchar, windowed
        leveled used internally by the templated functions
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DrawPixels, *my_args)
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
            return super(OpenGLImageMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLImageMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['render_to_rectangle', 'use_custom_extents'], [],
            ['color_level', 'color_window', 'custom_display_extents', 'z_slice']),
            title='Edit OpenGLImageMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLImageMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


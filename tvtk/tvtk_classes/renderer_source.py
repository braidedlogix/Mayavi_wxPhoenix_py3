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

from tvtk.tvtk_classes.algorithm import Algorithm


class RendererSource(Algorithm):
    """
    RendererSource - take a renderer's image and/or depth map into the
    pipeline
    
    Superclass: Algorithm
    
    RendererSource is a source object whose input is a renderer's
    image and/or depth map, which is then used to produce an output
    image. This output can then be used in the visualization pipeline.
    You must explicitly send a Modify() to this object to get it to
    reload its data from the renderer. Consider also using
    WindowToImageFilter instead of this class.
    
    By default, the data placed into the output is the renderer's image
    RGB values (these color scalars are represented by unsigned chars,
    one per color channel). Optionally, you can also grab the image depth
    (e.g., z-buffer) values, and include it in the output in one of three
    ways. 1) First, when the data member depth_values is enabled, a
    separate float array of these depth values is included in the output
    point data with array name "ZBuffer". 2) If depth_values_in_scalars is
    enabled, then the z-buffer values are shifted and scaled to fit into
    an unsigned char and included in the output image (so the output
    image pixels are four components RGBZ). Note that depth_values and and
    depth_values_in_scalars can be enabled simultaneously if desired.
    Finally 3) if depth_values_only is enabled, then the output image
    consists only of the z-buffer values represented by a single
    component float array; and the data members depth_values and
    depth_values_in_scalars are ignored.
    
    @sa
    WindowToImageFilter RendererPointCloudSource Renderer
    ImageData DepthImageToPointCloud
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRendererSource, obj, update, **traits)
    
    depth_values_in_scalars = tvtk_base.false_bool_trait(help=\
        """
        A boolean value to control whether to grab z-buffer (i.e., depth
        values) along with the image data. The z-buffer data is placed in
        the scalars as a fourth Z component (shift and scaled to map the
        full 0..255 range).
        """
    )

    def _depth_values_in_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepthValuesInScalars,
                        self.depth_values_in_scalars_)

    depth_values = tvtk_base.false_bool_trait(help=\
        """
        A boolean value to control whether to grab z-buffer (i.e., depth
        values) along with the image data. The z-buffer data is placed
        into a field data attributes named "ZBuffer" .
        """
    )

    def _depth_values_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepthValues,
                        self.depth_values_)

    depth_values_only = tvtk_base.false_bool_trait(help=\
        """
        A boolean value to control whether to grab only the z-buffer
        (i.e., depth values) without the associated image (color scalars)
        data. If enabled, the output data contains only a depth image
        which is the z-buffer values represented by float values. By
        default, this is disabled. Note that if enabled, then the
        depth_values and depth_values_in_scalars are ignored.
        """
    )

    def _depth_values_only_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepthValuesOnly,
                        self.depth_values_only_)

    render_flag = tvtk_base.false_bool_trait(help=\
        """
        If this flag is on, then filter execution causes a render first.
        """
    )

    def _render_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRenderFlag,
                        self.render_flag_)

    whole_window = tvtk_base.false_bool_trait(help=\
        """
        Use the entire render_window as a data source or just the
        Renderer. The default is zero, just the Renderer.
        """
    )

    def _whole_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWholeWindow,
                        self.whole_window_)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Returns which renderer is being used as the source for the pixel
        data.
        """
    )

    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    output = traits.Property(_get_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self):
        """
        V.get_output() -> ImageData
        C++: ImageData *GetOutput()
        Get the output data object for a port on this algorithm.
        """
        return wrap_vtk(self._vtk_obj.GetOutput())

    _updateable_traits_ = \
    (('depth_values_in_scalars', 'GetDepthValuesInScalars'),
    ('depth_values', 'GetDepthValues'), ('depth_values_only',
    'GetDepthValuesOnly'), ('render_flag', 'GetRenderFlag'),
    ('whole_window', 'GetWholeWindow'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'depth_values', 'depth_values_in_scalars',
    'depth_values_only', 'global_warning_display', 'release_data_flag',
    'render_flag', 'whole_window', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RendererSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RendererSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['depth_values', 'depth_values_in_scalars', 'depth_values_only',
            'render_flag', 'whole_window'], [], []),
            title='Edit RendererSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RendererSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


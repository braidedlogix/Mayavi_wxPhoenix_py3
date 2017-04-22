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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class DepthImageToPointCloud(PolyDataAlgorithm):
    """
    DepthImageToPointCloud - convert a depth image into a point cloud
    
    Superclass: PolyDataAlgorithm
    
    DepthImageToPointCloud is a filter that acquires its input from a
    depth image and converts it to point cloud represented as a
    PolyData. This can then be used in a visualization pipeline.
    
    The filter takes two input images, one of which is optional. The
    first image is a (required) depth image containing z-buffer values.
    The second image is an (optional) scalar image. The information in
    the z-buffer image, plus a specified camera, is used to generate
    x-y-z coordinates of the output point cloud (i.e., the points in a
    PolyData). The second scalar image is (optionally) output as
    scalars to the output point cloud. Note that the depth image must be
    a single component image, with values ranging between the near and
    far clipping range [-1,1].
    
    Note that if only a single input is provided, then the input is
    interpreted in one of two ways. First, if the "ZBuffer" point data is
    provided, then the input image is assumed to be color scalars with
    the depth data provided in the "ZBuffer" data array. (This is
    consistent with the RendererSource filter with depth_values
    enabled.) Otherwise, the input image is assumed to be a depth image.
    
    It is (optionally) possible to cull points located on the near and
    far clipping planes. This may better simulate the generation of a
    scanned object point cloud.
    
    @warning
    For the camera to transform the image depths into a point cloud, this
    filter makes assumptions about the origin of the depth image (and
    associated color scalar image). This class performs point by point
    transformation. The view matrix is used to transform each pixel.
    IMPORTANT NOTE: The transformation occurs by normalizing the image
    pixels into the (-1,1) view space (depth values are passed thru). The
    process follows the Coordinate class which is the standard for VTK
    rendering transformations. Subtle differences in whether the lower
    left pixel origin are at the center of the pixel versus the
    lower-left corner of the pixel will make slight differences in how
    pixels are transformed. (Similarly for the upper right pixel as
    well). This half pixel difference can cause transformation issues.
    (The code is commented appropriately.)
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    RendererSource WindowToImageFilter Camera PolyData
    Coordinate
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDepthImageToPointCloud, obj, update, **traits)
    
    cull_far_points = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether to cull points that are located on the far
        clipping plane. These typically are points that are part of the
        background. By default this is enabled.
        """
    )

    def _cull_far_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCullFarPoints,
                        self.cull_far_points_)

    cull_near_points = tvtk_base.false_bool_trait(help=\
        """
        Indicate whether to cull points that are located on the near
        clipping plane. These typically are points that are part of the
        clipped foreground. By default this is disabled.
        """
    )

    def _cull_near_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCullNearPoints,
                        self.cull_near_points_)

    produce_color_scalars = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether to output color scalar values along with the
        point cloud (assuming that the scalar values are available on
        input). By default this is enabled.
        """
    )

    def _produce_color_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProduceColorScalars,
                        self.produce_color_scalars_)

    produce_vertex_cell_array = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether to output a vertex cell array (i.e., Verts) in
        the output point cloud. Some filters require this vertex cells to
        be defined in order to execute properly. For example some mappers
        will only render points if the vertex cells are defined.
        """
    )

    def _produce_vertex_cell_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProduceVertexCellArray,
                        self.produce_vertex_cell_array_)

    def _get_camera(self):
        return wrap_vtk(self._vtk_obj.GetCamera())
    def _set_camera(self, arg):
        old_val = self._get_camera()
        self._wrap_call(self._vtk_obj.SetCamera,
                        deref_vtk(arg))
        self.trait_property_changed('camera', old_val, arg)
    camera = traits.Property(_get_camera, _set_camera, help=\
        """
        Returns the camera being used to generate the point cloud from
        the depth image.
        """
    )

    output_points_precision = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set the desired precision for the output points. See
        Algorithm::DesiredOutputPrecision for the available choices.
        The default is double precision.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('cull_far_points', 'GetCullFarPoints'), ('cull_near_points',
    'GetCullNearPoints'), ('produce_color_scalars',
    'GetProduceColorScalars'), ('produce_vertex_cell_array',
    'GetProduceVertexCellArray'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('output_points_precision', 'GetOutputPointsPrecision'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'cull_far_points', 'cull_near_points', 'debug',
    'global_warning_display', 'produce_color_scalars',
    'produce_vertex_cell_array', 'release_data_flag',
    'output_points_precision', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DepthImageToPointCloud, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DepthImageToPointCloud properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['cull_far_points', 'cull_near_points', 'produce_color_scalars',
            'produce_vertex_cell_array'], [], ['output_points_precision']),
            title='Edit DepthImageToPointCloud properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DepthImageToPointCloud properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


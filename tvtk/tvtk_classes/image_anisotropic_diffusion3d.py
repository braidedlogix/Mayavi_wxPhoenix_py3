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

from tvtk.tvtk_classes.image_spatial_algorithm import ImageSpatialAlgorithm


class ImageAnisotropicDiffusion3D(ImageSpatialAlgorithm):
    """
    ImageAnisotropicDiffusion3D - edge preserving smoothing.
    
    Superclass: ImageSpatialAlgorithm
    
    ImageAnisotropicDiffusion3D  diffuses an volume iteratively. The
    neighborhood of the diffusion is determined by the instance flags. if
    "Faces" is on, the 6 voxels adjoined by faces are included in the
    neighborhood.  If "Edges" is on the 12 edge connected voxels are
    included, and if "Corners" is on, the 8 corner connected voxels are
    included.  "_diffusion_factor" determines how far a pixel value moves
    toward its neighbors, and is insensitive to the number of neighbors
    chosen.  The diffusion is anisotropic because it only occurs when a
    gradient measure is below "_gradient_threshold".  Two gradient measures
    exist and are toggled by the "_gradient_magnitude_threshold" flag. When
    "_gradient_magnitude_threshold" is on, the magnitude of the gradient,
    computed by central differences, above "_diffusion_threshold" a voxel
    is not modified.  The alternative measure examines each neighbor
    independently.  The gradient between the voxel and the neighbor must
    be below the "_diffusion_threshold" for diffusion to occur with THAT
    neighbor.
    
    @sa
    ImageAnisotropicDiffusion2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageAnisotropicDiffusion3D, obj, update, **traits)
    
    corners = tvtk_base.true_bool_trait(help=\
        """
        Choose neighbors to diffuse (6 faces, 12 edges, 8 corners).
        """
    )

    def _corners_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCorners,
                        self.corners_)

    edges = tvtk_base.true_bool_trait(help=\
        """
        Choose neighbors to diffuse (6 faces, 12 edges, 8 corners).
        """
    )

    def _edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdges,
                        self.edges_)

    faces = tvtk_base.true_bool_trait(help=\
        """
        Choose neighbors to diffuse (6 faces, 12 edges, 8 corners).
        """
    )

    def _faces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFaces,
                        self.faces_)

    gradient_magnitude_threshold = tvtk_base.false_bool_trait(help=\
        """
        Switch between gradient magnitude threshold and pixel gradient
        threshold.
        """
    )

    def _gradient_magnitude_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGradientMagnitudeThreshold,
                        self.gradient_magnitude_threshold_)

    diffusion_factor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the difference factor
        """
    )

    def _diffusion_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiffusionFactor,
                        self.diffusion_factor)

    diffusion_threshold = traits.Float(5.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the difference threshold that stops diffusion. when the
        difference between two pixel is greater than this threshold, the
        pixels are not diffused.  This causes diffusion to avoid sharp
        edges. If the gradient_magnitude_threshold is set, then gradient
        magnitude is used for comparison instead of pixel differences.
        """
    )

    def _diffusion_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiffusionThreshold,
                        self.diffusion_threshold)

    number_of_iterations = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        This method sets the number of interations which also affects the
        input neighborhood needed to compute one output pixel.  Each
        iterations requires an extra pixel layer on the neighborhood. 
        This is only relavent when you are trying to stream or are
        requesting a sub extent of the "whole_extent".
        """
    )

    def _number_of_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfIterations,
                        self.number_of_iterations)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get a data object for one of the input port connections.  The use
        of this method is strongly discouraged, but some filters that
        were written a long time ago still use this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('corners', 'GetCorners'), ('edges', 'GetEdges'), ('faces',
    'GetFaces'), ('gradient_magnitude_threshold',
    'GetGradientMagnitudeThreshold'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('split_mode', 'GetSplitMode'),
    ('diffusion_factor', 'GetDiffusionFactor'), ('diffusion_threshold',
    'GetDiffusionThreshold'), ('number_of_iterations',
    'GetNumberOfIterations'), ('desired_bytes_per_piece',
    'GetDesiredBytesPerPiece'), ('enable_smp', 'GetEnableSMP'),
    ('global_default_enable_smp', 'GetGlobalDefaultEnableSMP'),
    ('minimum_piece_size', 'GetMinimumPieceSize'), ('number_of_threads',
    'GetNumberOfThreads'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'corners', 'debug', 'edges', 'faces',
    'global_warning_display', 'gradient_magnitude_threshold',
    'release_data_flag', 'split_mode', 'desired_bytes_per_piece',
    'diffusion_factor', 'diffusion_threshold', 'enable_smp',
    'global_default_enable_smp', 'minimum_piece_size',
    'number_of_iterations', 'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageAnisotropicDiffusion3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageAnisotropicDiffusion3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['corners', 'edges', 'faces', 'gradient_magnitude_threshold'],
            ['split_mode'], ['desired_bytes_per_piece', 'diffusion_factor',
            'diffusion_threshold', 'enable_smp', 'global_default_enable_smp',
            'minimum_piece_size', 'number_of_iterations', 'number_of_threads']),
            title='Edit ImageAnisotropicDiffusion3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageAnisotropicDiffusion3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


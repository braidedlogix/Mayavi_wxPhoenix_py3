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

from tvtk.tvtk_classes.image_reslice import ImageReslice


class ImageSlabReslice(ImageReslice):
    """
    ImageSlabReslice - Thick slab reformat through data.
    
    Superclass: ImageReslice
    
    This class derives from ImageResliceBase. Much like
    ImageReslice, it reslices the data. It is multi-threaded. It takes
    a three dimensional image as input and produces a two dimensional
    thick MPR along some direction.
    
    The class reslices the thick slab using a blending function.
    Supported blending functions are Minimum Intensity blend through the
    slab, maximum intensity blend and a Mean (average) intensity of
    values across the slab.
    
    The user can adjust the thickness of the slab by using the method
    set_slab_thickness. The distance between sample points used for
    blending across the thickness of the slab is controlled by the method
    set_slab_resolution. These two methods determine the number of slices
    used across the slab for blending, which is computed as {(2 x
    (int)(0.5 x slab_thickness/_slab_resolution)) + 1}. This value may be
    queried via get_num_blend_sample_points() and is always >= 1.
    
    Much like ImageReslice, the reslice axes direction cosines may be
    set via the methods set_reslice_axes or set_reslice_axes_direction_cosines.
    The output spacing is controlled by set_output_spacing and the output
    origin is controlled by set_output_origin. The default value to be set
    on pixels that lie outside the volume when reformatting is controlled
    by set_background_color or set_background_level. The
    set_reslice_axes_origin() method can also be used to provide an (x,y,z)
    point that the slice will pass through.
    @sa
    ImageReslice
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageSlabReslice, obj, update, **traits)
    
    blend_mode = traits.Trait('max',
    tvtk_base.TraitRevPrefixMap({'max': 1, 'mean': 2, 'min': 0}), help=\
        """
        Set/Get the blend mode. Default is MIP (ie Max)
        """
    )

    def _blend_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBlendMode,
                        self.blend_mode_)

    slab_resolution = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Spacing between slabs in world units. (Number of Slices, ie
        samples to blend is computed from slab_thickness and
        slab_resolution).
        """
    )

    def _slab_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSlabResolution,
                        self.slab_resolution)

    slab_thickness = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        slab_thickness of slab in world coords. slab_thickness must be
        non-zero and positive.
        """
    )

    def _slab_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSlabThickness,
                        self.slab_thickness)

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

    def _get_num_blend_sample_points(self):
        return self._vtk_obj.GetNumBlendSamplePoints()
    num_blend_sample_points = traits.Property(_get_num_blend_sample_points, help=\
        """
        Number of sample points used across the slab cross-section. If
        equal to 1, this ends up being a thin reslice through the data
        a.k.a. ImageReslice
        """
    )

    _updateable_traits_ = \
    (('auto_crop_output', 'GetAutoCropOutput'), ('border', 'GetBorder'),
    ('generate_stencil_output', 'GetGenerateStencilOutput'),
    ('interpolate', 'GetInterpolate'), ('mirror', 'GetMirror'),
    ('optimization', 'GetOptimization'), ('slab_trapezoid_integration',
    'GetSlabTrapezoidIntegration'), ('transform_input_sampling',
    'GetTransformInputSampling'), ('wrap', 'GetWrap'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('blend_mode', 'GetBlendMode'),
    ('interpolation_mode', 'GetInterpolationMode'), ('slab_mode',
    'GetSlabMode'), ('split_mode', 'GetSplitMode'), ('slab_resolution',
    'GetSlabResolution'), ('slab_thickness', 'GetSlabThickness'),
    ('background_color', 'GetBackgroundColor'), ('background_level',
    'GetBackgroundLevel'), ('output_dimensionality',
    'GetOutputDimensionality'), ('output_extent', 'GetOutputExtent'),
    ('output_origin', 'GetOutputOrigin'), ('output_scalar_type',
    'GetOutputScalarType'), ('output_spacing', 'GetOutputSpacing'),
    ('reslice_axes_direction_cosines', 'GetResliceAxesDirectionCosines'),
    ('reslice_axes_origin', 'GetResliceAxesOrigin'), ('scalar_scale',
    'GetScalarScale'), ('scalar_shift', 'GetScalarShift'),
    ('slab_number_of_slices', 'GetSlabNumberOfSlices'),
    ('slab_slice_spacing_fraction', 'GetSlabSliceSpacingFraction'),
    ('desired_bytes_per_piece', 'GetDesiredBytesPerPiece'), ('enable_smp',
    'GetEnableSMP'), ('global_default_enable_smp',
    'GetGlobalDefaultEnableSMP'), ('minimum_piece_size',
    'GetMinimumPieceSize'), ('number_of_threads', 'GetNumberOfThreads'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_crop_output', 'border', 'debug',
    'generate_stencil_output', 'global_warning_display', 'interpolate',
    'mirror', 'optimization', 'release_data_flag',
    'slab_trapezoid_integration', 'transform_input_sampling', 'wrap',
    'blend_mode', 'interpolation_mode', 'slab_mode', 'split_mode',
    'background_color', 'background_level', 'desired_bytes_per_piece',
    'enable_smp', 'global_default_enable_smp', 'minimum_piece_size',
    'number_of_threads', 'output_dimensionality', 'output_extent',
    'output_origin', 'output_scalar_type', 'output_spacing',
    'progress_text', 'reslice_axes_direction_cosines',
    'reslice_axes_origin', 'scalar_scale', 'scalar_shift',
    'slab_number_of_slices', 'slab_resolution',
    'slab_slice_spacing_fraction', 'slab_thickness'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageSlabReslice, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageSlabReslice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_crop_output', 'border', 'generate_stencil_output',
            'interpolate', 'mirror', 'optimization', 'slab_trapezoid_integration',
            'transform_input_sampling', 'wrap'], ['blend_mode',
            'interpolation_mode', 'slab_mode', 'split_mode'], ['background_color',
            'background_level', 'desired_bytes_per_piece', 'enable_smp',
            'global_default_enable_smp', 'minimum_piece_size',
            'number_of_threads', 'output_dimensionality', 'output_extent',
            'output_origin', 'output_scalar_type', 'output_spacing',
            'reslice_axes_direction_cosines', 'reslice_axes_origin',
            'scalar_scale', 'scalar_shift', 'slab_number_of_slices',
            'slab_resolution', 'slab_slice_spacing_fraction', 'slab_thickness']),
            title='Edit ImageSlabReslice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageSlabReslice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


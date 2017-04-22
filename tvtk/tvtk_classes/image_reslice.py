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

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageReslice(ThreadedImageAlgorithm):
    """
    ImageReslice - Reslices a volume along a new set of axes.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageReslice is the swiss-army-knife of image geometry filters: It
    can permute, rotate, flip, scale, resample, deform, and pad image
    data in any combination with reasonably high efficiency.  Simple
    operations such as permutation, resampling and padding are done with
    similar efficiently to the specialized ImagePermute,
    ImageResample, and ImagePad filters.  There are a number of
    tasks that ImageReslice is well suited for:
    
    1) Application of simple rotations, scales, and translations to an
    image. It is often a good idea to use ImageChangeInformation to
    center the image first, so that scales and rotations occur around the
    center rather than around the lower-left corner of the image.
    
    2) Resampling of one data set to match the voxel sampling of a second
    data set via the set_information_input() method, e.g. for the purpose
    of comparing two images or combining two images. A transformation,
    either linear or nonlinear, can be applied at the same time via the
    set_reslice_transform method if the two images are not in the same
    coordinate space.
    
    3) Extraction of slices from an image volume.  The most convenient
    way to do this is to use set_reslice_axes_direction_cosines() to specify
    the orientation of the slice.  The direction cosines give the x, y,
    and z axes for the output volume.  The method
    set_output_dimensionality(_2) is used to specify that want to output a
    slice rather than a volume.  The set_reslice_axes_origin() command is
    used to provide an (x,y,z) point that the slice will pass through.
    You can use both the reslice_axes and the reslice_transform at the same
    time, in order to extract slices from a volume that you have applied
    a transformation to.
    @warning
    This filter is very inefficient if the output X dimension is 1.
    @sa
    AbstractTransform Matrix4x4
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageReslice, obj, update, **traits)
    
    auto_crop_output = tvtk_base.false_bool_trait(help=\
        """
        Turn this on if you want to guarantee that the extent of the
        output will be large enough to ensure that none of the data will
        be cropped (default: Off).
        """
    )

    def _auto_crop_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoCropOutput,
                        self.auto_crop_output_)

    border = tvtk_base.true_bool_trait(help=\
        """
        Extend the apparent input border by a half voxel (default: On).
        This changes how interpolation is handled at the borders of the
        input image: if the center of an output voxel is beyond the edge
        of the input image, but is within a half voxel width of the edge
        (using the input voxel width), then the value of the output voxel
        is calculated as if the input's edge voxels were duplicated past
        the edges of the input. This has no effect if Mirror or Wrap are
        on.
        """
    )

    def _border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorder,
                        self.border_)

    generate_stencil_output = tvtk_base.false_bool_trait(help=\
        """
        Generate an output stencil that defines which pixels were
        interpolated and which pixels were out-of-bounds of the input.
        """
    )

    def _generate_stencil_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateStencilOutput,
                        self.generate_stencil_output_)

    interpolate = tvtk_base.false_bool_trait(help=\
        """
        Convenient methods for switching between nearest-neighbor and
        linear interpolation. interpolate_on() is equivalent to
        set_interpolation_mode_to_linear() and interpolate_off() is equivalent
        to set_interpolation_mode_to_nearest_neighbor() You should not use
        these methods if you use the set_interpolation_mode methods.
        """
    )

    def _interpolate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolate,
                        self.interpolate_)

    mirror = tvtk_base.false_bool_trait(help=\
        """
        Turn on mirror-pad feature (default: Off). This will override the
        wrap-pad.
        """
    )

    def _mirror_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMirror,
                        self.mirror_)

    optimization = tvtk_base.true_bool_trait(help=\
        """
        Turn on and off optimizations (default on, they should only be
        turned off for testing purposes).
        """
    )

    def _optimization_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOptimization,
                        self.optimization_)

    slab_trapezoid_integration = tvtk_base.false_bool_trait(help=\
        """
        Use trapezoid integration for slab computation.  All this does is
        weigh the first and last slices by half when doing sum and mean.
        It is off by default.
        """
    )

    def _slab_trapezoid_integration_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSlabTrapezoidIntegration,
                        self.slab_trapezoid_integration_)

    transform_input_sampling = tvtk_base.true_bool_trait(help=\
        """
        Specify whether to transform the spacing, origin and extent of
        the Input (or the information_input) according to the direction
        cosines and origin of the reslice_axes before applying them as the
        default output spacing, origin and extent (default: On).
        """
    )

    def _transform_input_sampling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTransformInputSampling,
                        self.transform_input_sampling_)

    wrap = tvtk_base.false_bool_trait(help=\
        """
        Turn on wrap-pad feature (default: Off).
        """
    )

    def _wrap_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWrap,
                        self.wrap_)

    interpolation_mode = traits.Trait('nearest_neighbor',
    tvtk_base.TraitRevPrefixMap({'nearest_neighbor': 0, 'cubic': 2, 'linear': 1}), help=\
        """
        Set interpolation mode (default: nearest neighbor).
        """
    )

    def _interpolation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolationMode,
                        self.interpolation_mode_)

    slab_mode = traits.Trait('mean',
    tvtk_base.TraitRevPrefixMap({'mean': 2, 'max': 1, 'min': 0, 'sum': 3}), help=\
        """
        Set the slab mode, for generating thick slices. The default is
        Mean. If set_slab_number_of_slices(_n) is called with N greater than
        one, then each output slice will actually be a composite of N
        slices.  This method specifies the compositing mode to be used.
        """
    )

    def _slab_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSlabMode,
                        self.slab_mode_)

    background_color = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _background_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundColor,
                        self.background_color)

    background_level = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set background grey level (for single-component images).
        """
    )

    def _background_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundLevel,
                        self.background_level)

    def _get_information_input(self):
        return wrap_vtk(self._vtk_obj.GetInformationInput())
    def _set_information_input(self, arg):
        old_val = self._get_information_input()
        self._wrap_call(self._vtk_obj.SetInformationInput,
                        deref_vtk(arg))
        self.trait_property_changed('information_input', old_val, arg)
    information_input = traits.Property(_get_information_input, _set_information_input, help=\
        """
        Set a ImageData from which the default Spacing, Origin, and
        whole_extent of the output will be copied.  The spacing, origin,
        and extent will be permuted according to the reslice_axes.  Any
        values set via set_output_spacing, set_output_origin, and
        set_output_extent will override these values.  By default, the
        Spacing, Origin, and whole_extent of the Input are used.
        """
    )

    def _get_interpolator(self):
        return wrap_vtk(self._vtk_obj.GetInterpolator())
    def _set_interpolator(self, arg):
        old_val = self._get_interpolator()
        self._wrap_call(self._vtk_obj.SetInterpolator,
                        deref_vtk(arg))
        self.trait_property_changed('interpolator', old_val, arg)
    interpolator = traits.Property(_get_interpolator, _set_interpolator, help=\
        """
        Set the interpolator to use.  The default interpolator supports
        the Nearest, Linear, and Cubic interpolation modes.
        """
    )

    output_dimensionality = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Force the dimensionality of the output to either 1, 2, 3 or 0
        (default: 3).  If the dimensionality is 2d, then the Z extent of
        the output is forced to (0,0) and the Z origin of the output is
        forced to 0.0 (i.e. the output extent is confined to the xy
        plane).  If the dimensionality is 1d, the output extent is
        confined to the x axis. For 0d, the output extent consists of a
        single voxel at (0,0,0).
        """
    )

    def _output_dimensionality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputDimensionality,
                        self.output_dimensionality)

    output_extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(0, 0, 0, 0, 0, 0), cols=3, help=\
        """
        Set the extent for the output data.  The default output extent is
        the input extent permuted through the reslice_axes.
        """
    )

    def _output_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputExtent,
                        self.output_extent)

    output_origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set the origin for the output data.  The default output origin is
        the input origin permuted through the reslice_axes.
        """
    )

    def _output_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputOrigin,
                        self.output_origin)

    output_scalar_type = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the scalar type of the output to be different from the input.
        The default value is -1, which means that the input scalar type
        will be used to set the output scalar type.  Otherwise, this must
        be set to one of the following types: VTK_CHAR, VTK_SIGNED_CHAR,
        VTK_UNSIGNED_CHAR, VTK_SHORT, VTK_UNSIGNED_SHORT, VTK_INT,
        VTK_UNSIGNED_INT, VTK_FLOAT, or VTK_DOUBLE.  Other types are not
        permitted.  If the output type is an integer type, the output
        will be rounded and clamped to the limits of the type.
        """
    )

    def _output_scalar_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputScalarType,
                        self.output_scalar_type)

    output_spacing = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        Set the voxel spacing for the output data.  The default output
        spacing is the input spacing permuted through the reslice_axes.
        """
    )

    def _output_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputSpacing,
                        self.output_spacing)

    def _get_reslice_axes(self):
        return wrap_vtk(self._vtk_obj.GetResliceAxes())
    def _set_reslice_axes(self, arg):
        old_val = self._get_reslice_axes()
        self._wrap_call(self._vtk_obj.SetResliceAxes,
                        deref_vtk(arg))
        self.trait_property_changed('reslice_axes', old_val, arg)
    reslice_axes = traits.Property(_get_reslice_axes, _set_reslice_axes, help=\
        """
        This method is used to set up the axes for the output voxels. The
        output Spacing, Origin, and Extent specify the locations of the
        voxels within the coordinate system defined by the axes. The
        reslice_axes are used most often to permute the data, e.g. to
        extract ZY or XZ slices of a volume as 2d XY images.
        
        The first column of the matrix specifies the x-axis vector (the
        fourth element must be set to zero), the second column specifies
        the y-axis, and the third column the z-axis.  The fourth column
        is the origin of the axes (the fourth element must be set to
        one).
        
        An alternative to set_reslice_axes() is to use
        set_reslice_axes_direction_cosines() to set the directions of the
        axes and set_reslice_axes_origin() to set the origin of the axes.
        """
    )

    reslice_axes_direction_cosines = traits.Array(enter_set=True, auto_set=False, shape=(9,), dtype=float, value=(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0), cols=3, help=\
        """
        Specify the direction cosines for the reslice_axes (i.e. the first
        three elements of each of the first three columns of the
        reslice_axes matrix).  This will modify the current reslice_axes
        matrix, or create a new matrix if none exists.
        """
    )

    def _reslice_axes_direction_cosines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResliceAxesDirectionCosines,
                        self.reslice_axes_direction_cosines)

    reslice_axes_origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Specify the origin for the reslice_axes (i.e. the first three
        elements of the final column of the reslice_axes matrix). This
        will modify the current reslice_axes matrix, or create new matrix
        if none exists.
        """
    )

    def _reslice_axes_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResliceAxesOrigin,
                        self.reslice_axes_origin)

    def _get_reslice_transform(self):
        return wrap_vtk(self._vtk_obj.GetResliceTransform())
    def _set_reslice_transform(self, arg):
        old_val = self._get_reslice_transform()
        self._wrap_call(self._vtk_obj.SetResliceTransform,
                        deref_vtk(arg))
        self.trait_property_changed('reslice_transform', old_val, arg)
    reslice_transform = traits.Property(_get_reslice_transform, _set_reslice_transform, help=\
        """
        Set a transform to be applied to the resampling grid that has
        been defined via the reslice_axes and the output Origin, Spacing
        and Extent.  Note that applying a transform to the resampling
        grid (which lies in the output coordinate system) is equivalent
        to applying the inverse of that transform to the input volume. 
        Nonlinear transforms such as GridTransform and
        ThinPlateSplineTransform can be used here.
        """
    )

    scalar_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set multiplication factor to apply to all the output voxels.
        After a sample value has been interpolated from the input image,
        the equation u = (v + scalar_shift)*_scalar_scale will be applied to
        it before it is written to the output image.  The result will
        always be clamped to the limits of the output data type.
        """
    )

    def _scalar_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarScale,
                        self.scalar_scale)

    scalar_shift = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set a value to add to all the output voxels. After a sample value
        has been interpolated from the input image, the equation u = (v +
        scalar_shift)*_scalar_scale will be applied to it before it is
        written to the output image.  The result will always be clamped
        to the limits of the output data type.
        """
    )

    def _scalar_shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarShift,
                        self.scalar_shift)

    slab_number_of_slices = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the number of slices that will be combined to create the
        slab.
        """
    )

    def _slab_number_of_slices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSlabNumberOfSlices,
                        self.slab_number_of_slices)

    slab_slice_spacing_fraction = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The slab spacing as a fraction of the output slice spacing. When
        one of the various slab modes is chosen, each output slice is
        produced by generating several "temporary" output slices and then
        combining them according to the slab mode.  By default, the
        spacing between these temporary slices is the Z component of the
        output_spacing. This method sets the spacing between these
        temporary slices to be a fraction of the output spacing.
        """
    )

    def _slab_slice_spacing_fraction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSlabSliceSpacingFraction,
                        self.slab_slice_spacing_fraction)

    def _get_stencil_output(self):
        return wrap_vtk(self._vtk_obj.GetStencilOutput())
    def _set_stencil_output(self, arg):
        old_val = self._get_stencil_output()
        self._wrap_call(self._vtk_obj.SetStencilOutput,
                        deref_vtk(arg))
        self.trait_property_changed('stencil_output', old_val, arg)
    stencil_output = traits.Property(_get_stencil_output, _set_stencil_output, help=\
        """
        Get the output stencil.
        """
    )

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

    def _get_stencil(self):
        return wrap_vtk(self._vtk_obj.GetStencil())
    stencil = traits.Property(_get_stencil, help=\
        """
        Use a stencil to limit the calculations to a specific region of
        the output.  Portions of the output that are 'outside' the
        stencil will be cleared to the background color.
        """
    )

    def _get_stencil_output_port(self):
        return wrap_vtk(self._vtk_obj.GetStencilOutputPort())
    stencil_output_port = traits.Property(_get_stencil_output_port, help=\
        """
        Get the output stencil.
        """
    )

    def report_references(self, *args):
        """
        V.report_references(GarbageCollector)
        
        Report object referenced by instances of this class.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReportReferences, *my_args)
        return ret

    def set_output_extent_to_default(self):
        """
        V.set_output_extent_to_default()
        C++: void SetOutputExtentToDefault()
        Set the extent for the output data.  The default output extent is
        the input extent permuted through the reslice_axes.
        """
        ret = self._vtk_obj.SetOutputExtentToDefault()
        return ret
        

    def set_output_origin_to_default(self):
        """
        V.set_output_origin_to_default()
        C++: void SetOutputOriginToDefault()
        Set the origin for the output data.  The default output origin is
        the input origin permuted through the reslice_axes.
        """
        ret = self._vtk_obj.SetOutputOriginToDefault()
        return ret
        

    def set_output_spacing_to_default(self):
        """
        V.set_output_spacing_to_default()
        C++: void SetOutputSpacingToDefault()
        Set the voxel spacing for the output data.  The default output
        spacing is the input spacing permuted through the reslice_axes.
        """
        ret = self._vtk_obj.SetOutputSpacingToDefault()
        return ret
        

    def set_stencil_data(self, *args):
        """
        V.set_stencil_data(ImageStencilData)
        C++: void SetStencilData(ImageStencilData *stencil)
        Use a stencil to limit the calculations to a specific region of
        the output.  Portions of the output that are 'outside' the
        stencil will be cleared to the background color.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetStencilData, *my_args)
        return ret

    _updateable_traits_ = \
    (('auto_crop_output', 'GetAutoCropOutput'), ('border', 'GetBorder'),
    ('generate_stencil_output', 'GetGenerateStencilOutput'),
    ('interpolate', 'GetInterpolate'), ('mirror', 'GetMirror'),
    ('optimization', 'GetOptimization'), ('slab_trapezoid_integration',
    'GetSlabTrapezoidIntegration'), ('transform_input_sampling',
    'GetTransformInputSampling'), ('wrap', 'GetWrap'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interpolation_mode',
    'GetInterpolationMode'), ('slab_mode', 'GetSlabMode'), ('split_mode',
    'GetSplitMode'), ('background_color', 'GetBackgroundColor'),
    ('background_level', 'GetBackgroundLevel'), ('output_dimensionality',
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
    'interpolation_mode', 'slab_mode', 'split_mode', 'background_color',
    'background_level', 'desired_bytes_per_piece', 'enable_smp',
    'global_default_enable_smp', 'minimum_piece_size',
    'number_of_threads', 'output_dimensionality', 'output_extent',
    'output_origin', 'output_scalar_type', 'output_spacing',
    'progress_text', 'reslice_axes_direction_cosines',
    'reslice_axes_origin', 'scalar_scale', 'scalar_shift',
    'slab_number_of_slices', 'slab_slice_spacing_fraction'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageReslice, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageReslice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_crop_output', 'border', 'generate_stencil_output',
            'interpolate', 'mirror', 'optimization', 'slab_trapezoid_integration',
            'transform_input_sampling', 'wrap'], ['interpolation_mode',
            'slab_mode', 'split_mode'], ['background_color', 'background_level',
            'desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
            'minimum_piece_size', 'number_of_threads', 'output_dimensionality',
            'output_extent', 'output_origin', 'output_scalar_type',
            'output_spacing', 'reslice_axes_direction_cosines',
            'reslice_axes_origin', 'scalar_scale', 'scalar_shift',
            'slab_number_of_slices', 'slab_slice_spacing_fraction']),
            title='Edit ImageReslice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageReslice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


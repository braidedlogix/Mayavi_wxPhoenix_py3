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


class ImageFlip(ImageReslice):
    """
    ImageFlip - This flips an axis of an image.
    
    Superclass: ImageReslice
    
    Right becomes left ...
    
    ImageFlip will reflect the data along the filtered axis.  This
    filter is actually a thin wrapper around ImageReslice.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageFlip, obj, update, **traits)
    
    flip_about_origin = tvtk_base.false_bool_trait(help=\
        """
        By default the image will be flipped about its center, and the
        Origin, Spacing and Extent of the output will be identical to the
        input.  However, if you have a coordinate system associated with
        the image and you want to use the flip to convert +ve values
        along one axis to -ve values (and vice versa) then you actually
        want to flip the image about coordinate (0,0,0) instead of about
        the center of the image.  This method will adjust the Origin of
        the output such that the flip occurs about (0,0,0).  Note that
        this method only changes the Origin (and hence the coordinate
        system) the output data: the actual pixel values are the same
        whether or not this method is used.  Also note that the Origin in
        this method name refers to (0,0,0) in the coordinate system
        associated with the image, it does not refer to the Origin ivar
        that is associated with a ImageData.
        """
    )

    def _flip_about_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFlipAboutOrigin,
                        self.flip_about_origin_)

    preserve_image_extent = tvtk_base.true_bool_trait(help=\
        """
        preserve_image_extent_off wasn't covered by test scripts and its
        implementation was broken.  It is deprecated now and it has no
        effect (i.e. the image_extent is always preserved).
        """
    )

    def _preserve_image_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreserveImageExtent,
                        self.preserve_image_extent_)

    filtered_axes = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Keep the mis-named Axes variations around for compatibility with
        old scripts. Axis is singular, not plural...
        """
    )

    def _filtered_axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilteredAxes,
                        self.filtered_axes)

    filtered_axis = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify which axis will be flipped.  This must be an integer
        between 0 (for x) and 2 (for z). Initial value is 0.
        """
    )

    def _filtered_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilteredAxis,
                        self.filtered_axis)

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
    (('flip_about_origin', 'GetFlipAboutOrigin'),
    ('preserve_image_extent', 'GetPreserveImageExtent'),
    ('auto_crop_output', 'GetAutoCropOutput'), ('border', 'GetBorder'),
    ('generate_stencil_output', 'GetGenerateStencilOutput'),
    ('interpolate', 'GetInterpolate'), ('mirror', 'GetMirror'),
    ('optimization', 'GetOptimization'), ('slab_trapezoid_integration',
    'GetSlabTrapezoidIntegration'), ('transform_input_sampling',
    'GetTransformInputSampling'), ('wrap', 'GetWrap'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interpolation_mode',
    'GetInterpolationMode'), ('slab_mode', 'GetSlabMode'), ('split_mode',
    'GetSplitMode'), ('filtered_axes', 'GetFilteredAxes'),
    ('filtered_axis', 'GetFilteredAxis'), ('background_color',
    'GetBackgroundColor'), ('background_level', 'GetBackgroundLevel'),
    ('output_dimensionality', 'GetOutputDimensionality'),
    ('output_extent', 'GetOutputExtent'), ('output_origin',
    'GetOutputOrigin'), ('output_scalar_type', 'GetOutputScalarType'),
    ('output_spacing', 'GetOutputSpacing'),
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
    'flip_about_origin', 'generate_stencil_output',
    'global_warning_display', 'interpolate', 'mirror', 'optimization',
    'preserve_image_extent', 'release_data_flag',
    'slab_trapezoid_integration', 'transform_input_sampling', 'wrap',
    'interpolation_mode', 'slab_mode', 'split_mode', 'background_color',
    'background_level', 'desired_bytes_per_piece', 'enable_smp',
    'filtered_axes', 'filtered_axis', 'global_default_enable_smp',
    'minimum_piece_size', 'number_of_threads', 'output_dimensionality',
    'output_extent', 'output_origin', 'output_scalar_type',
    'output_spacing', 'progress_text', 'reslice_axes_direction_cosines',
    'reslice_axes_origin', 'scalar_scale', 'scalar_shift',
    'slab_number_of_slices', 'slab_slice_spacing_fraction'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageFlip, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageFlip properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_crop_output', 'border', 'flip_about_origin',
            'generate_stencil_output', 'interpolate', 'mirror', 'optimization',
            'preserve_image_extent', 'slab_trapezoid_integration',
            'transform_input_sampling', 'wrap'], ['interpolation_mode',
            'slab_mode', 'split_mode'], ['background_color', 'background_level',
            'desired_bytes_per_piece', 'enable_smp', 'filtered_axes',
            'filtered_axis', 'global_default_enable_smp', 'minimum_piece_size',
            'number_of_threads', 'output_dimensionality', 'output_extent',
            'output_origin', 'output_scalar_type', 'output_spacing',
            'reslice_axes_direction_cosines', 'reslice_axes_origin',
            'scalar_scale', 'scalar_shift', 'slab_number_of_slices',
            'slab_slice_spacing_fraction']),
            title='Edit ImageFlip properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageFlip properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


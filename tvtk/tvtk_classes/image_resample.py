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


class ImageResample(ImageReslice):
    """
    ImageResample - Resamples an image to be larger or smaller.
    
    Superclass: ImageReslice
    
    This filter produces an output with different spacing (and extent)
    than the input.  Linear interpolation can be used to resample the
    data. The Output spacing can be set explicitly or relative to input
    spacing with the set_axis_magnification_factor method.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageResample, obj, update, **traits)
    
    def get_axis_magnification_factor(self, *args):
        """
        V.get_axis_magnification_factor(int, Information) -> float
        C++: double GetAxisMagnificationFactor(int axis,
            Information *inInfo=0)
        Set/Get Magnification factors. Zero is a reserved value
        indicating values have not been computed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetAxisMagnificationFactor, *my_args)
        return ret

    def set_axis_magnification_factor(self, *args):
        """
        V.set_axis_magnification_factor(int, float)
        C++: void SetAxisMagnificationFactor(int axis, double factor)
        Set/Get Magnification factors. Zero is a reserved value
        indicating values have not been computed.
        """
        ret = self._wrap_call(self._vtk_obj.SetAxisMagnificationFactor, *args)
        return ret

    dimensionality = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Dimensionality is the number of axes which are considered during
        execution. To process images dimensionality would be set to 2.
        This has the same effect as setting the magnification of the
        third axis to 1.0
        """
    )

    def _dimensionality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimensionality,
                        self.dimensionality)

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

    def set_axis_output_spacing(self, *args):
        """
        V.set_axis_output_spacing(int, float)
        C++: void SetAxisOutputSpacing(int axis, double spacing)
        Set desired spacing. Zero is a reserved value indicating spacing
        has not been set.
        """
        ret = self._wrap_call(self._vtk_obj.SetAxisOutputSpacing, *args)
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
    'GetSplitMode'), ('dimensionality', 'GetDimensionality'),
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
    'interpolation_mode', 'slab_mode', 'split_mode', 'background_color',
    'background_level', 'desired_bytes_per_piece', 'dimensionality',
    'enable_smp', 'global_default_enable_smp', 'minimum_piece_size',
    'number_of_threads', 'output_dimensionality', 'output_extent',
    'output_origin', 'output_scalar_type', 'output_spacing',
    'progress_text', 'reslice_axes_direction_cosines',
    'reslice_axes_origin', 'scalar_scale', 'scalar_shift',
    'slab_number_of_slices', 'slab_slice_spacing_fraction'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageResample, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageResample properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_crop_output', 'border', 'generate_stencil_output',
            'interpolate', 'mirror', 'optimization', 'slab_trapezoid_integration',
            'transform_input_sampling', 'wrap'], ['interpolation_mode',
            'slab_mode', 'split_mode'], ['background_color', 'background_level',
            'desired_bytes_per_piece', 'dimensionality', 'enable_smp',
            'global_default_enable_smp', 'minimum_piece_size',
            'number_of_threads', 'output_dimensionality', 'output_extent',
            'output_origin', 'output_scalar_type', 'output_spacing',
            'reslice_axes_direction_cosines', 'reslice_axes_origin',
            'scalar_scale', 'scalar_shift', 'slab_number_of_slices',
            'slab_slice_spacing_fraction']),
            title='Edit ImageResample properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageResample properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


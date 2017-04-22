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


class ImagePermute(ImageReslice):
    """
    ImagePermute - Permutes axes of input.
    
    Superclass: ImageReslice
    
    ImagePermute reorders the axes of the input. Filtered axes specify
    the input axes which become X, Y, Z.  The input has to have the same
    scalar type of the output. The filter does copy the data when it
    executes. This filter is actually a very thin wrapper around
    ImageReslice.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImagePermute, obj, update, **traits)
    
    filtered_axes = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(0, 1, 2), cols=3, help=\
        """
        The filtered axes are the input axes that get relabeled to X,Y,Z.
        """
    )

    def _filtered_axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilteredAxes,
                        self.filtered_axes)

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
    'GetSplitMode'), ('filtered_axes', 'GetFilteredAxes'),
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
    'background_level', 'desired_bytes_per_piece', 'enable_smp',
    'filtered_axes', 'global_default_enable_smp', 'minimum_piece_size',
    'number_of_threads', 'output_dimensionality', 'output_extent',
    'output_origin', 'output_scalar_type', 'output_spacing',
    'progress_text', 'reslice_axes_direction_cosines',
    'reslice_axes_origin', 'scalar_scale', 'scalar_shift',
    'slab_number_of_slices', 'slab_slice_spacing_fraction'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImagePermute, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImagePermute properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_crop_output', 'border', 'generate_stencil_output',
            'interpolate', 'mirror', 'optimization', 'slab_trapezoid_integration',
            'transform_input_sampling', 'wrap'], ['interpolation_mode',
            'slab_mode', 'split_mode'], ['background_color', 'background_level',
            'desired_bytes_per_piece', 'enable_smp', 'filtered_axes',
            'global_default_enable_smp', 'minimum_piece_size',
            'number_of_threads', 'output_dimensionality', 'output_extent',
            'output_origin', 'output_scalar_type', 'output_spacing',
            'reslice_axes_direction_cosines', 'reslice_axes_origin',
            'scalar_scale', 'scalar_shift', 'slab_number_of_slices',
            'slab_slice_spacing_fraction']),
            title='Edit ImagePermute properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImagePermute properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class ImageResliceToColors(ImageReslice):
    """
    ImageResliceToColors - Reslice and produce color scalars.
    
    Superclass: ImageReslice
    
    ImageResliceToColors is an extension of ImageReslice that
    produces color scalars.  It should be provided with a lookup table
    that defines the output colors and the desired range of input values
    to map to those colors.  If the input has multiple components, then
    you should use the set_vector_mode() method of the lookup table to
    specify how the vectors will be colored.  If no lookup table is
    provided, then the input must already be color scalars, but they will
    be converted to the specified output format.
    @sa
    ImageMapToColors
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageResliceToColors, obj, update, **traits)
    
    bypass = tvtk_base.false_bool_trait(help=\
        """
        Bypass the color mapping operation and output the scalar values
        directly.  The output values will be float, rather than the input
        data type.
        """
    )

    def _bypass_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBypass,
                        self.bypass_)

    output_format = traits.Trait('rgba',
    tvtk_base.TraitRevPrefixMap({'rgba': 4, 'luminance': 1, 'luminance_alpha': 2, 'rgb': 3}), help=\
        """
        Set the output format, the default is RGBA.
        """
    )

    def _output_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputFormat,
                        self.output_format_)

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Set a lookup table to apply to the data.  Use the Range,
        vector_mode, and vector_components of the table to control the
        mapping of the input data to colors.  If any output voxel is
        transformed to a point outside the input volume, then that voxel
        will be set to the background_color.
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

    _updateable_traits_ = \
    (('bypass', 'GetBypass'), ('auto_crop_output', 'GetAutoCropOutput'),
    ('border', 'GetBorder'), ('generate_stencil_output',
    'GetGenerateStencilOutput'), ('interpolate', 'GetInterpolate'),
    ('mirror', 'GetMirror'), ('optimization', 'GetOptimization'),
    ('slab_trapezoid_integration', 'GetSlabTrapezoidIntegration'),
    ('transform_input_sampling', 'GetTransformInputSampling'), ('wrap',
    'GetWrap'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('output_format', 'GetOutputFormat'), ('interpolation_mode',
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
    (['abort_execute', 'auto_crop_output', 'border', 'bypass', 'debug',
    'generate_stencil_output', 'global_warning_display', 'interpolate',
    'mirror', 'optimization', 'release_data_flag',
    'slab_trapezoid_integration', 'transform_input_sampling', 'wrap',
    'interpolation_mode', 'output_format', 'slab_mode', 'split_mode',
    'background_color', 'background_level', 'desired_bytes_per_piece',
    'enable_smp', 'global_default_enable_smp', 'minimum_piece_size',
    'number_of_threads', 'output_dimensionality', 'output_extent',
    'output_origin', 'output_scalar_type', 'output_spacing',
    'progress_text', 'reslice_axes_direction_cosines',
    'reslice_axes_origin', 'scalar_scale', 'scalar_shift',
    'slab_number_of_slices', 'slab_slice_spacing_fraction'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageResliceToColors, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageResliceToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_crop_output', 'border', 'bypass',
            'generate_stencil_output', 'interpolate', 'mirror', 'optimization',
            'slab_trapezoid_integration', 'transform_input_sampling', 'wrap'],
            ['interpolation_mode', 'output_format', 'slab_mode', 'split_mode'],
            ['background_color', 'background_level', 'desired_bytes_per_piece',
            'enable_smp', 'global_default_enable_smp', 'minimum_piece_size',
            'number_of_threads', 'output_dimensionality', 'output_extent',
            'output_origin', 'output_scalar_type', 'output_spacing',
            'reslice_axes_direction_cosines', 'reslice_axes_origin',
            'scalar_scale', 'scalar_shift', 'slab_number_of_slices',
            'slab_slice_spacing_fraction']),
            title='Edit ImageResliceToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageResliceToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


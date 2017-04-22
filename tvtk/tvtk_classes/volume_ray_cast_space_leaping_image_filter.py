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


class VolumeRayCastSpaceLeapingImageFilter(ThreadedImageAlgorithm):
    """
    VolumeRayCastSpaceLeapingImageFilter - Builds the space leaping
    data structure.
    
    Superclass: ThreadedImageAlgorithm
    
    This is an optimized multi-threaded imaging filter that builds the
    space leaping datastructure, used by
    FixedPointVolumeRayCastMapper. Empty space leaping is used to skip
    large empty regions in the scalar opacity and/or the gradient opacity
    transfer functions. Depending on the various options set by
    FixedPointVolumeRayCastMapper, the class will internally invoke
    one of the many optmized routines to compute the min/max/gradient-max
    values within a fixed block size, trying to compute everything in a
    single multi-threaded pass through the data
    
    The block size may be changed at compile time. Its ifdef'ed to 4 in
    the CXX file.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeRayCastSpaceLeapingImageFilter, obj, update, **traits)
    
    compute_gradient_opacity = tvtk_base.false_bool_trait(help=\
        """
        Compute gradient opacity ?
        """
    )

    def _compute_gradient_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeGradientOpacity,
                        self.compute_gradient_opacity_)

    compute_min_max = tvtk_base.false_bool_trait(help=\
        """
        Compute the min max structure ?.
        """
    )

    def _compute_min_max_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeMinMax,
                        self.compute_min_max_)

    update_gradient_opacity_flags = tvtk_base.false_bool_trait(help=\
        """
        Update the gradient opacity flags. (The scalar opacity flags are
        always updated upon execution of this filter.)
        """
    )

    def _update_gradient_opacity_flags_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUpdateGradientOpacityFlags,
                        self.update_gradient_opacity_flags_)

    def _get_current_scalars(self):
        return wrap_vtk(self._vtk_obj.GetCurrentScalars())
    def _set_current_scalars(self, arg):
        old_val = self._get_current_scalars()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetCurrentScalars,
                        my_arg[0])
        self.trait_property_changed('current_scalars', old_val, arg)
    current_scalars = traits.Property(_get_current_scalars, _set_current_scalars, help=\
        """
        Set the scalars.
        """
    )

    independent_components = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Do we use independent components, or dependent components ?
        """
    )

    def _independent_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIndependentComponents,
                        self.independent_components)

    table_scale = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(1.0, 1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _table_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTableScale,
                        self.table_scale)

    table_shift = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _table_shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTableShift,
                        self.table_shift)

    table_size = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=int, value=(0, 0, 0, 0), cols=3, help=\
        """
        
        """
    )

    def _table_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTableSize,
                        self.table_size)

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

    def _get_last_min_max_build_time(self):
        return self._vtk_obj.GetLastMinMaxBuildTime()
    last_min_max_build_time = traits.Property(_get_last_min_max_build_time, help=\
        """
        Get the last execution time. This is updated every time the
        scalars or the gradient opacity values are computed
        """
    )

    def _get_last_min_max_flag_time(self):
        return self._vtk_obj.GetLastMinMaxFlagTime()
    last_min_max_flag_time = traits.Property(_get_last_min_max_flag_time, help=\
        """
        Get the last execution time. This is updated every time the flags
        bits are re-computed.
        """
    )

    def get_min_max_volume(self, *args):
        """
        V.get_min_max_volume([int, int, int, int]) -> (int, ...)
        C++: unsigned short *GetMinMaxVolume(int dims[4])
        Get the raw pointer to the final computed space leaping
        datastructure. The result is only valid after Update() has been
        called on the filter. Note that this filter holds onto its
        memory. The dimensions of the min- max volume are in dims. The
        4th value in the array indicates the number of independent
        components, (also queried via get_number_of_independent_components())
        """
        ret = self._wrap_call(self._vtk_obj.GetMinMaxVolume, *args)
        return ret

    def _get_min_non_zero_gradient_magnitude_index(self):
        return self._vtk_obj.GetMinNonZeroGradientMagnitudeIndex()
    min_non_zero_gradient_magnitude_index = traits.Property(_get_min_non_zero_gradient_magnitude_index, help=\
        """
        Get the first non-zero scalar opacity and gradient opacity
        indices for each independent copmonent INTERNAL - Do not use.
        """
    )

    def _get_min_non_zero_scalar_index(self):
        return self._vtk_obj.GetMinNonZeroScalarIndex()
    min_non_zero_scalar_index = traits.Property(_get_min_non_zero_scalar_index, help=\
        """
        Get the first non-zero scalar opacity and gradient opacity
        indices for each independent copmonent INTERNAL - Do not use.
        """
    )

    def _get_number_of_independent_components(self):
        return self._vtk_obj.GetNumberOfIndependentComponents()
    number_of_independent_components = traits.Property(_get_number_of_independent_components, help=\
        """
        Get the number of independent components for which we need to
        keep track of min/max
        """
    )

    def compute_input_extents_for_output(self, *args):
        """
        V.compute_input_extents_for_output([int, int, int, int, int, int],
            [int, int, int], [int, int, int, int, int, int], ImageData)
        C++: static void ComputeInputExtentsForOutput(int inExt[6],
            int inDim[3], int outExt[6], ImageData *inData)
        Compute the extents and dimensions of the input that's required
        to generate an output min-max structure given by out_ext. INTERNAL
        - Do not use
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeInputExtentsForOutput, *my_args)
        return ret

    def compute_offset(self, *args):
        """
        V.compute_offset((int, int, int, int, int, int), (int, int, int,
            int, int, int), int) -> int
        C++: IdType ComputeOffset(const int ext[6],
            const int wholeExt[6], int nComponents)
        INTERNAL - Do not use Compute the offset within an image of whole
        extents whole_ext, to access the data starting at extents ext.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeOffset, *args)
        return ret

    def set_cache(self, *args):
        """
        V.set_cache(ImageData)
        C++: virtual void SetCache(ImageData *imageCache)
        INTERNAL - Do not use Set the last cached min-max volume, as used
        by FixedPointVolumeRayCastMapper.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetCache, *my_args)
        return ret

    def set_gradient_opacity_table(self, *args):
        """
        V.set_gradient_opacity_table(int, [int, ...])
        C++: void SetGradientOpacityTable(int c, unsigned short *t)
        Set the scalar opacity and gradient opacity tables computed for
        each component by the FixedPointVolumeRayCastMapper
        """
        ret = self._wrap_call(self._vtk_obj.SetGradientOpacityTable, *args)
        return ret

    def set_scalar_opacity_table(self, *args):
        """
        V.set_scalar_opacity_table(int, [int, ...])
        C++: void SetScalarOpacityTable(int c, unsigned short *t)
        Set the scalar opacity and gradient opacity tables computed for
        each component by the FixedPointVolumeRayCastMapper
        """
        ret = self._wrap_call(self._vtk_obj.SetScalarOpacityTable, *args)
        return ret

    _updateable_traits_ = \
    (('compute_gradient_opacity', 'GetComputeGradientOpacity'),
    ('compute_min_max', 'GetComputeMinMax'),
    ('update_gradient_opacity_flags', 'GetUpdateGradientOpacityFlags'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('split_mode',
    'GetSplitMode'), ('independent_components',
    'GetIndependentComponents'), ('table_scale', 'GetTableScale'),
    ('table_shift', 'GetTableShift'), ('table_size', 'GetTableSize'),
    ('desired_bytes_per_piece', 'GetDesiredBytesPerPiece'), ('enable_smp',
    'GetEnableSMP'), ('global_default_enable_smp',
    'GetGlobalDefaultEnableSMP'), ('minimum_piece_size',
    'GetMinimumPieceSize'), ('number_of_threads', 'GetNumberOfThreads'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_gradient_opacity', 'compute_min_max',
    'debug', 'global_warning_display', 'release_data_flag',
    'update_gradient_opacity_flags', 'split_mode',
    'desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
    'independent_components', 'minimum_piece_size', 'number_of_threads',
    'progress_text', 'table_scale', 'table_shift', 'table_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeRayCastSpaceLeapingImageFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeRayCastSpaceLeapingImageFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_gradient_opacity', 'compute_min_max',
            'update_gradient_opacity_flags'], ['split_mode'],
            ['desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
            'independent_components', 'minimum_piece_size', 'number_of_threads',
            'table_scale', 'table_shift', 'table_size']),
            title='Edit VolumeRayCastSpaceLeapingImageFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeRayCastSpaceLeapingImageFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


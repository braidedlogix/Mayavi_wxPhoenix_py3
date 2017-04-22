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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class PointInterpolator(DataSetAlgorithm):
    """
    PointInterpolator - interpolate over point cloud using various
    kernels
    
    Superclass: DataSetAlgorithm
    
    PointInterpolator probes a point cloud Pc (the filter Source) with
    a set of points P (the filter Input), interpolating the data values
    from Pc onto P. Note however that the descriptive phrase "point
    cloud" is a misnomer: Pc can be represented by any DataSet type,
    with the points of the dataset forming Pc. Similary, the output P can
    also be represented by any DataSet type; and the topology/geometry
    structure of P is passed through to the output along with the newly
    interpolated arrays.
    
    A key input to this filter is the specification of the interpolation
    kernel, and the parameters which control the associated interpolation
    process. Interpolation kernels include Voronoi, Gaussian, Shepard,
    and SPH (smoothed particle hydrodynamics), with additional kernels to
    be added in the future.
    
    An overview of the algorithm is as follows. For each p from P, Np
    "close" points to p are found. (The meaning of what is "close" can be
    specified as either the N closest points, or all points within a
    given radius Rp. This depends on how the kernel is defined.) Once the
    Np close points are found, then the interpolation kernel is applied
    to compute new data values located on p. Note that for reasonable
    performance, finding the Np closest points requires a point locator.
    The locator may be specified as input to the algorithm. (By default,
    a StaticPointLocator is used because generally it is much faster
    to build, delete, and search with. However, with highly non-uniform
    point distributions, octree- or kd-tree based locators may perform
    better.)
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @warning
    For widely spaced points in Pc, or when p is located outside the
    bounding region of Pc, the interpolation may behave badly and the
    interpolation process will adapt as necessary to produce output. For
    example, if the N closest points within R are requested to
    interpolate p, if N=0 then the interpolation will switch to a
    different strategy (which can be controlled as in the
    null_points_strategy).
    
    @sa
    PointInterpolator2D ProbeFilter GaussianSplatter
    CheckerboardSplatter ShepardMethod VoronoiKernel
    ShepardKernel GaussianKernel SPHKernel
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointInterpolator, obj, update, **traits)
    
    pass_cell_arrays = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether to shallow copy the input cell data arrays to
        the output.  On by default.
        """
    )

    def _pass_cell_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassCellArrays,
                        self.pass_cell_arrays_)

    pass_field_arrays = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether to pass the field-data arrays from the input to
        the output. On by default.
        """
    )

    def _pass_field_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassFieldArrays,
                        self.pass_field_arrays_)

    pass_point_arrays = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether to shallow copy the input point data arrays to
        the output.  On by default.
        """
    )

    def _pass_point_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassPointArrays,
                        self.pass_point_arrays_)

    promote_output_arrays = tvtk_base.true_bool_trait(help=\
        """
        If enabled, then input arrays that are non-real types (i.e., not
        float or double) are promoted to float type on output. This is
        because the interpolation process may not be well behaved when
        integral types are combined using interpolation weights.
        """
    )

    def _promote_output_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPromoteOutputArrays,
                        self.promote_output_arrays_)

    null_points_strategy = traits.Trait('null_value',
    tvtk_base.TraitRevPrefixMap({'null_value': 1, 'closest_point': 2, 'mask_points': 0}), help=\
        """
        Specify a strategy to use when encountering a "null" point during
        the interpolation process. Null points occur when the local
        neighborhood (of nearby points to interpolate from) is empty. If
        the strategy is set to mask_points, then an output array is
        created that marks points as being valid (=1) or null (invalid
        =0) (and the null_value is set as well). If the strategy is set to
        null_value (this is the default), then the output data value(s)
        are set to the null_point value (specified in the output point
        data). Finally, the strategy closest_point is to simply use the
        closest point to perform the interpolation.
        """
    )

    def _null_points_strategy_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNullPointsStrategy,
                        self.null_points_strategy_)

    def _get_kernel(self):
        return wrap_vtk(self._vtk_obj.GetKernel())
    def _set_kernel(self, arg):
        old_val = self._get_kernel()
        self._wrap_call(self._vtk_obj.SetKernel,
                        deref_vtk(arg))
        self.trait_property_changed('kernel', old_val, arg)
    kernel = traits.Property(_get_kernel, _set_kernel, help=\
        """
        Specify an interpolation kernel. By default a LinearKernel is
        used (i.e., linear combination of closest points). The
        interpolation kernel changes the basis of the interpolation.
        """
    )

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Specify a point locator. By default a StaticPointLocator is
        used. The locator performs efficient searches to locate near a
        specified interpolation position.
        """
    )

    null_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Specify the null point value. When a null point is encountered
        then all components of each null tuple are set to this value. By
        default the null value is set to zero.
        """
    )

    def _null_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNullValue,
                        self.null_value)

    valid_points_mask_array_name = traits.String('vtkValidPointMask', enter_set=True, auto_set=False, help=\
        """
        If the null_points_strategy == MASK_POINTS, then an array is
        generated for each input point. This CharArray is placed into
        the output of the filter, with a non-zero value for a valid
        point, and zero otherwise. The name of this masking array is
        specified here.
        """
    )

    def _valid_points_mask_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValidPointsMaskArrayName,
                        self.valid_points_mask_array_name)

    def get_excluded_array(self, *args):
        """
        V.get_excluded_array(int) -> string
        C++: const char *GetExcludedArray(int i)
        Return the name of the ith excluded array.
        """
        ret = self._wrap_call(self._vtk_obj.GetExcludedArray, *args)
        return ret

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def _get_number_of_excluded_arrays(self):
        return self._vtk_obj.GetNumberOfExcludedArrays()
    number_of_excluded_arrays = traits.Property(_get_number_of_excluded_arrays, help=\
        """
        Return the number of excluded arrays.
        """
    )

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    source = traits.Property(_get_source, help=\
        """
        Specify the dataset Pc that will be probed by the input points P.
         The Input P defines the dataset structure (the points and cells)
        for the output, while the Source Pc is probed (interpolated) to
        generate the scalars, vectors, etc. for the output points based
        on the point locations.
        """
    )

    def add_excluded_array(self, *args):
        """
        V.add_excluded_array(string)
        C++: void AddExcludedArray(const StdString &excludedArray)
        Adds an array to the list of arrays which are to be excluded from
        the interpolation process.
        """
        ret = self._wrap_call(self._vtk_obj.AddExcludedArray, *args)
        return ret

    def clear_excluded_arrays(self):
        """
        V.clear_excluded_arrays()
        C++: void ClearExcludedArrays()
        Clears the contents of excluded array list.
        """
        ret = self._vtk_obj.ClearExcludedArrays()
        return ret
        

    def set_source_connection(self, *args):
        """
        V.set_source_connection(AlgorithmOutput)
        C++: void SetSourceConnection(AlgorithmOutput *algOutput)
        Specify the dataset Pc that will be probed by the input points P.
         The Input P defines the structure (the points and cells) for the
        output, while the Source Pc is probed (interpolated) to generate
        the scalars, vectors, etc. for the output points based on the
        point locations.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceConnection, *my_args)
        return ret

    def set_source_data(self, *args):
        """
        V.set_source_data(DataObject)
        C++: void SetSourceData(DataObject *source)
        Specify the dataset Pc that will be probed by the input points P.
         The Input P defines the dataset structure (the points and cells)
        for the output, while the Source Pc is probed (interpolated) to
        generate the scalars, vectors, etc. for the output points based
        on the point locations.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceData, *my_args)
        return ret

    _updateable_traits_ = \
    (('pass_cell_arrays', 'GetPassCellArrays'), ('pass_field_arrays',
    'GetPassFieldArrays'), ('pass_point_arrays', 'GetPassPointArrays'),
    ('promote_output_arrays', 'GetPromoteOutputArrays'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('null_points_strategy',
    'GetNullPointsStrategy'), ('null_value', 'GetNullValue'),
    ('valid_points_mask_array_name', 'GetValidPointsMaskArrayName'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'pass_cell_arrays', 'pass_field_arrays', 'pass_point_arrays',
    'promote_output_arrays', 'release_data_flag', 'null_points_strategy',
    'null_value', 'progress_text', 'valid_points_mask_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PointInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['pass_cell_arrays', 'pass_field_arrays', 'pass_point_arrays',
            'promote_output_arrays'], ['null_points_strategy'], ['null_value',
            'valid_points_mask_array_name']),
            title='Edit PointInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


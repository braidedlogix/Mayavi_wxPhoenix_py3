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


class SPHInterpolator(DataSetAlgorithm):
    """
    SPHInterpolator - interpolate over point cloud using SPH kernels
    
    Superclass: DataSetAlgorithm
    
    This filter uses SPH (smooth particle hydrodynamics) kernels to
    interpolate a data source onto an input structure. For example, while
    the data source is a set of particles, the data from these particles
    can be interpolated onto an input object such as a line, plane or
    volume. Then the output (which consists of the input structure plus
    interpolated data) can then be visualized using classical
    visualization techniques such as isocontouring, slicing, heat maps
    and so on.
    
    To use this filter, besides setting the input P and source Pc,
    specify a point locator (which accelerates queries about points and
    their neighbors) and an interpolation kernel (a subclass of
    SPHKernel). In addition, the name of the source's density and mass
    arrays can optionally be provided; however if not provided then the
    local volume is computed from the kernel's spatial step. Finally, a
    cutoff distance array can optionall be provided when the local
    neighborhood around each point varies. The cutoff distance defines a
    local neighborhood in which the points in that neighborhood are used
    to interpolate values. If not provided, then the cutoff distance is
    computed from the spatial step size times the cutoff factor (see
    SPHKernel).
    
    Other options to the filter include specifying which data attributes
    to interpolate from the source. By default, all data attributes
    contained in the source are interpolated. However, by adding array
    names to the exclusion list, these arrays will not be interpolated.
    Also, it is possible to use a SPH derivative formulation to
    interpolate from the source data attributes. This requires adding
    arrays (by name) to the derivative list, in which case the derivative
    formulation will be applied to create a new output array named
    "X_deriv" where X is the name of a source point attribute array.
    
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
    
    @warning
    For more information and technical reference, see D.J. Price,
    Smoothed particle hydrodynamics and magnetohydrodynamics, J. Comput.
    Phys. 231:759-794, 2012. Especially equation 49.
    
    @par Acknowledgments: The following work has been generously
    supported by Altair Engineering and flui_dyna gmb_h. Please contact
    Steve Cosgrove or Milos Stanic for more information.
    
    @sa
    PointInterpolator SPHKernel SPHQuinticKernel
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSPHInterpolator, obj, update, **traits)
    
    compute_shepard_sum = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether to compute the summation of weighting
        coefficients (the so-called Shepard sum). In the interior of a
        SPH point cloud, the Shephard summation value should be ~1.0. 
        Towards the boundary, the Shepard summation generally falls off
        <1.0. If compute_shepard_sum is specified, then the output will
        contain an array of summed Shepard weights for each output point.
        On by default.
        """
    )

    def _compute_shepard_sum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeShepardSum,
                        self.compute_shepard_sum_)

    pass_cell_arrays = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether to shallow copy the input cell data arrays to
        the output. On by default.
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
        the output. On by default.
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
    tvtk_base.TraitRevPrefixMap({'null_value': 1, 'mask_points': 0}), help=\
        """
        Specify a strategy to use when encountering a "null" point during
        the interpolation process. Null points occur when the local
        neighborhood (of nearby points to interpolate from) is empty. If
        the strategy is set to mask_points, then an output array is
        created that marks points as being valid (=1) or null (invalid
        =0) (and the null_value is set as well). If the strategy is set to
        null_value, then the output data value(s) are set to the null_point
        value.
        """
    )

    def _null_points_strategy_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNullPointsStrategy,
                        self.null_points_strategy_)

    cutoff_array_name = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Specify an (optional) cutoff distance for each point in the input
        P. If not specified, then the kernel cutoff is used.
        """
    )

    def _cutoff_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCutoffArrayName,
                        self.cutoff_array_name)

    density_array_name = traits.String('Rho', enter_set=True, auto_set=False, help=\
        """
        Specify the density array name. This is optional. Typically both
        the density and mass arrays are specified together (in order to
        compute the local volume). Both the mass and density arrays must
        consist of tuples of 1-component. (Note that the density array
        name specifies a point array found in the Pc source.)
        """
    )

    def _density_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDensityArrayName,
                        self.density_array_name)

    def _get_kernel(self):
        return wrap_vtk(self._vtk_obj.GetKernel())
    def _set_kernel(self, arg):
        old_val = self._get_kernel()
        self._wrap_call(self._vtk_obj.SetKernel,
                        deref_vtk(arg))
        self.trait_property_changed('kernel', old_val, arg)
    kernel = traits.Property(_get_kernel, _set_kernel, help=\
        """
        Specify an interpolation kernel. By default a SPHQuinticKernel
        is used (i.e., closest point). The interpolation kernel changes
        the basis of the interpolation.
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

    mass_array_name = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Specify the mass array name. This is optional. Typically both the
        density and mass arrays are specified together (in order to
        compute the local volume).  Both the mass and density arrays must
        consist of tuples of 1-component. (Note that the mass array name
        specifies a point array found in the Pc source.)
        """
    )

    def _mass_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMassArrayName,
                        self.mass_array_name)

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

    shepard_sum_array_name = traits.String('Shepard Summation', enter_set=True, auto_set=False, help=\
        """
        If compute_shepard_sum is on, then an array is generated with name
        shepard_sum_array_name for each input point. This FloatArray is
        placed into the output of the filter, and null_points have value
        =0.0. The default name is "Shepard Summation".
        """
    )

    def _shepard_sum_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShepardSumArrayName,
                        self.shepard_sum_array_name)

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

    def get_derivative_array(self, *args):
        """
        V.get_derivative_array(int) -> string
        C++: const char *GetDerivativeArray(int i)
        Return the name of the ith derivative array.
        """
        ret = self._wrap_call(self._vtk_obj.GetDerivativeArray, *args)
        return ret

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

    def _get_number_of_derivative_arrays(self):
        return self._vtk_obj.GetNumberOfDerivativeArrays()
    number_of_derivative_arrays = traits.Property(_get_number_of_derivative_arrays, help=\
        """
        Return the number of derivative arrays.
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

    def add_derivative_array(self, *args):
        """
        V.add_derivative_array(string)
        C++: void AddDerivativeArray(const StdString &derivArray)
        Adds an array to the list of arrays whose derivative is to be
        taken. If the name of the array is "deriv_array" this will produce
        an output array with the name "deriv_array_deriv" (after filter
        execution).
        """
        ret = self._wrap_call(self._vtk_obj.AddDerivativeArray, *args)
        return ret

    def add_excluded_array(self, *args):
        """
        V.add_excluded_array(string)
        C++: void AddExcludedArray(const StdString &excludedArray)
        Adds an array to the list of arrays which are to be excluded from
        the interpolation process.
        """
        ret = self._wrap_call(self._vtk_obj.AddExcludedArray, *args)
        return ret

    def clear_derivative_arrays(self):
        """
        V.clear_derivative_arrays()
        C++: void ClearDerivativeArrays()
        Clears the contents of derivative array list.
        """
        ret = self._vtk_obj.ClearDerivativeArrays()
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
    (('compute_shepard_sum', 'GetComputeShepardSum'), ('pass_cell_arrays',
    'GetPassCellArrays'), ('pass_field_arrays', 'GetPassFieldArrays'),
    ('pass_point_arrays', 'GetPassPointArrays'), ('promote_output_arrays',
    'GetPromoteOutputArrays'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('null_points_strategy', 'GetNullPointsStrategy'),
    ('cutoff_array_name', 'GetCutoffArrayName'), ('density_array_name',
    'GetDensityArrayName'), ('mass_array_name', 'GetMassArrayName'),
    ('null_value', 'GetNullValue'), ('shepard_sum_array_name',
    'GetShepardSumArrayName'), ('valid_points_mask_array_name',
    'GetValidPointsMaskArrayName'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_shepard_sum', 'debug',
    'global_warning_display', 'pass_cell_arrays', 'pass_field_arrays',
    'pass_point_arrays', 'promote_output_arrays', 'release_data_flag',
    'null_points_strategy', 'cutoff_array_name', 'density_array_name',
    'mass_array_name', 'null_value', 'progress_text',
    'shepard_sum_array_name', 'valid_points_mask_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SPHInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SPHInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_shepard_sum', 'pass_cell_arrays', 'pass_field_arrays',
            'pass_point_arrays', 'promote_output_arrays'],
            ['null_points_strategy'], ['cutoff_array_name', 'density_array_name',
            'mass_array_name', 'null_value', 'shepard_sum_array_name',
            'valid_points_mask_array_name']),
            title='Edit SPHInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SPHInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


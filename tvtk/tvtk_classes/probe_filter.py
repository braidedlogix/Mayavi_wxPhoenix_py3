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


class ProbeFilter(DataSetAlgorithm):
    """
    ProbeFilter - sample data values at specified point locations
    
    Superclass: DataSetAlgorithm
    
    ProbeFilter is a filter that computes point attributes (e.g.,
    scalars, vectors, etc.) at specified point positions. The filter has
    two inputs: the Input and Source. The Input geometric structure is
    passed through the filter. The point attributes are computed at the
    Input point positions by interpolating into the source data. For
    example, we can compute data values on a plane (plane specified as
    Input) from a volume (Source). The cell data of the source data is
    copied to the output based on in which source cell each input point
    is. If an array of the same name exists both in source's point and
    cell data, only the one from the point data is probed.
    
    This filter can be used to resample data, or convert one dataset form
    into another. For example, an unstructured grid (vtk_unstructured_grid)
    can be probed with a volume (three-dimensional ImageData), and
    then volume rendering techniques can be used to visualize the
    results. Another example: a line or curve can be used to probe data
    to produce x-y plots along that line or curve.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProbeFilter, obj, update, **traits)
    
    compute_tolerance = tvtk_base.true_bool_trait(help=\
        """
        Set whether to use the Tolerance field or precompute the
        tolerance. When on, the tolerance will be computed and the field
        value is ignored. Off by default.
        """
    )

    def _compute_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeTolerance,
                        self.compute_tolerance_)

    pass_cell_arrays = tvtk_base.false_bool_trait(help=\
        """
        Shallow copy the input cell data arrays to the output. Off by
        default.
        """
    )

    def _pass_cell_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassCellArrays,
                        self.pass_cell_arrays_)

    pass_field_arrays = tvtk_base.true_bool_trait(help=\
        """
        Set whether to pass the field-data arrays from the Input i.e. the
        input providing the geometry to the output. On by default.
        """
    )

    def _pass_field_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassFieldArrays,
                        self.pass_field_arrays_)

    pass_point_arrays = tvtk_base.false_bool_trait(help=\
        """
        Shallow copy the input point data arrays to the output Off by
        default.
        """
    )

    def _pass_point_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassPointArrays,
                        self.pass_point_arrays_)

    spatial_match = tvtk_base.false_bool_trait(help=\
        """
        This flag is used only when a piece is requested to update.  By
        default the flag is off.  Because no spatial correspondence
        between input pieces and source pieces is known, all of the
        source has to be requested no matter what piece of the output is
        requested.  When there is a spatial correspondence, the
        user/application can set this flag.  This hint allows the breakup
        of the probe operation to be much more efficient.  When piece m
        of n is requested for update by the user, then only n of m needs
        to be requested of the source.
        """
    )

    def _spatial_match_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpatialMatch,
                        self.spatial_match_)

    tolerance = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the tolerance used to compute whether a point in the source
        is in a cell of the input.  This value is only used if
        compute_tolerance is off.
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    valid_point_mask_array_name = traits.String('vtkValidPointMask', enter_set=True, auto_set=False, help=\
        """
        Returns the name of the char array added to the output with
        values 1 for valid points and 0 for invalid points. Set to
        "vtk_valid_point_mask" by default.
        """
    )

    def _valid_point_mask_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValidPointMaskArrayName,
                        self.valid_point_mask_array_name)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    source = traits.Property(_get_source, help=\
        """
        Specify the data set that will be probed at the input points. The
        Input gives the geometry (the points and cells) for the output,
        while the Source is probed (interpolated) to generate the
        scalars, vectors, etc. for the output points based on the point
        locations.
        """
    )

    def _get_valid_points(self):
        return wrap_vtk(self._vtk_obj.GetValidPoints())
    valid_points = traits.Property(_get_valid_points, help=\
        """
        Get the list of point ids in the output that contain attribute
        data interpolated from the source.
        """
    )

    def set_source_connection(self, *args):
        """
        V.set_source_connection(AlgorithmOutput)
        C++: void SetSourceConnection(AlgorithmOutput *algOutput)
        Specify the data set that will be probed at the input points. The
        Input gives the geometry (the points and cells) for the output,
        while the Source is probed (interpolated) to generate the
        scalars, vectors, etc. for the output points based on the point
        locations.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceConnection, *my_args)
        return ret

    def set_source_data(self, *args):
        """
        V.set_source_data(DataObject)
        C++: void SetSourceData(DataObject *source)
        Specify the data set that will be probed at the input points. The
        Input gives the geometry (the points and cells) for the output,
        while the Source is probed (interpolated) to generate the
        scalars, vectors, etc. for the output points based on the point
        locations.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceData, *my_args)
        return ret

    _updateable_traits_ = \
    (('compute_tolerance', 'GetComputeTolerance'), ('pass_cell_arrays',
    'GetPassCellArrays'), ('pass_field_arrays', 'GetPassFieldArrays'),
    ('pass_point_arrays', 'GetPassPointArrays'), ('spatial_match',
    'GetSpatialMatch'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('tolerance',
    'GetTolerance'), ('valid_point_mask_array_name',
    'GetValidPointMaskArrayName'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_tolerance', 'debug',
    'global_warning_display', 'pass_cell_arrays', 'pass_field_arrays',
    'pass_point_arrays', 'release_data_flag', 'spatial_match',
    'progress_text', 'tolerance', 'valid_point_mask_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProbeFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_tolerance', 'pass_cell_arrays', 'pass_field_arrays',
            'pass_point_arrays', 'spatial_match'], [], ['tolerance',
            'valid_point_mask_array_name']),
            title='Edit ProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


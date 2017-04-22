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

from tvtk.tvtk_classes.point_interpolator import PointInterpolator


class PointInterpolator2D(PointInterpolator):
    """
    PointInterpolator2D - interpolate point cloud attribute data onto
    x-y plane using various kernels
    
    Superclass: PointInterpolator
    
    PointInterpolator2D probes a point cloud Pc (the filter Source)
    with a set of points P (the filter Input), interpolating the data
    values from Pc onto P. Note however that the descriptive phrase "point
    cloud" is a misnomer: Pc can be represented by any DataSet type,
    with the points of the dataset forming Pc. Similary, the output P can
    also be represented by any DataSet type; and the topology/geometry
    structure of P is passed through to the output along with the newly
    interpolated arrays. However, this filter presumes that P lies on a
    plane z=0.0, thus z-coordinates are set accordingly during the
    interpolation process.
    
    The optional boolen flag interpolate_z is provided for convenience. In
    effect it turns the source z coordinates into an additional array
    that is interpolated onto the output data. For example, if the source
    is a x-y-z LIDAR point cloud, then z can be interpolated onto the
    output dataset as a vertical elevation(z-coordinate).
    
    A key input to this filter is the specification of the interpolation
    kernel, and the parameters which control the associated interpolation
    process. Interpolation kernels include Voronoi, Gaussian, Shepard,
    and SPH (smoothed particle hydrodynamics), with additional kernels to
    be added in the future. See PointInterpolator for more
    information.
    
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
    PointInterpolator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointInterpolator2D, obj, update, **traits)
    
    interpolate_z = tvtk_base.true_bool_trait(help=\
        """
        Specify whether to take the z-coordinate values of the source
        points as attributes to be interpolated. This is in addition to
        any other point attribute data associated with the source. By
        default this is enabled.
        """
    )

    def _interpolate_z_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolateZ,
                        self.interpolate_z_)

    z_array_name = traits.String('Elevation', enter_set=True, auto_set=False, help=\
        """
        Specify the name of the output array containing z values. This
        method is only applicable when interpolate_z is enabled. By
        default the output array name is "Elevation".
        """
    )

    def _z_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZArrayName,
                        self.z_array_name)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    _updateable_traits_ = \
    (('interpolate_z', 'GetInterpolateZ'), ('pass_cell_arrays',
    'GetPassCellArrays'), ('pass_field_arrays', 'GetPassFieldArrays'),
    ('pass_point_arrays', 'GetPassPointArrays'), ('promote_output_arrays',
    'GetPromoteOutputArrays'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('null_points_strategy', 'GetNullPointsStrategy'), ('z_array_name',
    'GetZArrayName'), ('null_value', 'GetNullValue'),
    ('valid_points_mask_array_name', 'GetValidPointsMaskArrayName'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'interpolate_z',
    'pass_cell_arrays', 'pass_field_arrays', 'pass_point_arrays',
    'promote_output_arrays', 'release_data_flag', 'null_points_strategy',
    'null_value', 'progress_text', 'valid_points_mask_array_name',
    'z_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointInterpolator2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PointInterpolator2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['interpolate_z', 'pass_cell_arrays', 'pass_field_arrays',
            'pass_point_arrays', 'promote_output_arrays'],
            ['null_points_strategy'], ['null_value',
            'valid_points_mask_array_name', 'z_array_name']),
            title='Edit PointInterpolator2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointInterpolator2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


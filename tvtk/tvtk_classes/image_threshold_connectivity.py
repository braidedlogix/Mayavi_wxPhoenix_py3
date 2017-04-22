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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ImageThresholdConnectivity(ImageAlgorithm):
    """
    ImageThresholdConnectivity - Flood fill an image region.
    
    Superclass: ImageAlgorithm
    
    ImageThresholdConnectivity will perform a flood fill on an image,
    given upper and lower pixel intensity thresholds. It works similarly
    to ImageThreshold, but also allows the user to set seed points to
    limit the threshold operation to contiguous regions of the image. The
    filled region, or the "inside", will be passed through to the output
    by default, while the "outside" will be replaced with zeros. This
    behavior can be changed by using the replace_in() and replace_out()
    methods.  The scalar type of the output is the same as the input.
    @sa
    ImageThreshold@par Thanks: Thanks to David Gobbi for contributing
    this class to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageThresholdConnectivity, obj, update, **traits)
    
    replace_in = tvtk_base.false_bool_trait(help=\
        """
        Replace the filled region by the value set by set_in_value().
        """
    )

    def _replace_in_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReplaceIn,
                        self.replace_in_)

    replace_out = tvtk_base.false_bool_trait(help=\
        """
        Replace the filled region by the value set by set_in_value().
        """
    )

    def _replace_out_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReplaceOut,
                        self.replace_out_)

    active_component = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        For multi-component images, you can set which component will be
        used for the threshold checks.
        """
    )

    def _active_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetActiveComponent,
                        self.active_component)

    in_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        If replace_in is set, the filled region will be replaced by this
        value.
        """
    )

    def _in_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInValue,
                        self.in_value)

    neighborhood_fraction = traits.Trait(0.5, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        The fraction of the neighborhood that must be within the
        thresholds. The default value is 0.5.
        """
    )

    def _neighborhood_fraction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNeighborhoodFraction,
                        self.neighborhood_fraction)

    neighborhood_radius = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _neighborhood_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNeighborhoodRadius,
                        self.neighborhood_radius)

    out_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        If replace_out is set, outside the fill will be replaced by this
        value.
        """
    )

    def _out_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutValue,
                        self.out_value)

    def _get_seed_points(self):
        return wrap_vtk(self._vtk_obj.GetSeedPoints())
    def _set_seed_points(self, arg):
        old_val = self._get_seed_points()
        my_arg = deref_array([arg], [['vtkPoints']])
        self._wrap_call(self._vtk_obj.SetSeedPoints,
                        my_arg[0])
        self.trait_property_changed('seed_points', old_val, arg)
    seed_points = traits.Property(_get_seed_points, _set_seed_points, help=\
        """
        Set the seeds.  The seeds are in real data coordinates, not in
        voxel index locations.
        """
    )

    slice_range_x = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(-2147483647, 2147483647), cols=2, help=\
        """
        
        """
    )

    def _slice_range_x_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceRangeX,
                        self.slice_range_x)

    slice_range_y = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(-2147483647, 2147483647), cols=2, help=\
        """
        
        """
    )

    def _slice_range_y_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceRangeY,
                        self.slice_range_y)

    slice_range_z = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(-2147483647, 2147483647), cols=2, help=\
        """
        
        """
    )

    def _slice_range_z_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceRangeZ,
                        self.slice_range_z)

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

    def _get_lower_threshold(self):
        return self._vtk_obj.GetLowerThreshold()
    lower_threshold = traits.Property(_get_lower_threshold, help=\
        """
        Get the Upper and Lower thresholds.
        """
    )

    def _get_number_of_in_voxels(self):
        return self._vtk_obj.GetNumberOfInVoxels()
    number_of_in_voxels = traits.Property(_get_number_of_in_voxels, help=\
        """
        After the filter has executed, use get_number_of_voxels() to find
        out how many voxels were filled.
        """
    )

    def _get_stencil(self):
        return wrap_vtk(self._vtk_obj.GetStencil())
    stencil = traits.Property(_get_stencil, help=\
        """
        Specify a stencil that will be used to limit the flood fill to an
        arbitrarily-shaped region of the image.
        """
    )

    def _get_upper_threshold(self):
        return self._vtk_obj.GetUpperThreshold()
    upper_threshold = traits.Property(_get_upper_threshold, help=\
        """
        Get the Upper and Lower thresholds.
        """
    )

    def set_stencil_data(self, *args):
        """
        V.set_stencil_data(ImageStencilData)
        C++: virtual void SetStencilData(ImageStencilData *stencil)
        Specify a stencil that will be used to limit the flood fill to an
        arbitrarily-shaped region of the image.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetStencilData, *my_args)
        return ret

    def threshold_between(self, *args):
        """
        V.threshold_between(float, float)
        C++: void ThresholdBetween(double lower, double upper)
        Values within this range will be filled, where the range inludes
        values that are exactly equal to the lower and upper thresholds.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdBetween, *args)
        return ret

    def threshold_by_lower(self, *args):
        """
        V.threshold_by_lower(float)
        C++: void ThresholdByLower(double thresh)
        Values less than or equal to this threshold will be filled.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdByLower, *args)
        return ret

    def threshold_by_upper(self, *args):
        """
        V.threshold_by_upper(float)
        C++: void ThresholdByUpper(double thresh)
        Values greater than or equal to this threshold will be filled.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdByUpper, *args)
        return ret

    _updateable_traits_ = \
    (('replace_in', 'GetReplaceIn'), ('replace_out', 'GetReplaceOut'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('active_component', 'GetActiveComponent'), ('in_value',
    'GetInValue'), ('neighborhood_fraction', 'GetNeighborhoodFraction'),
    ('neighborhood_radius', 'GetNeighborhoodRadius'), ('out_value',
    'GetOutValue'), ('slice_range_x', 'GetSliceRangeX'), ('slice_range_y',
    'GetSliceRangeY'), ('slice_range_z', 'GetSliceRangeZ'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'replace_in', 'replace_out', 'active_component',
    'in_value', 'neighborhood_fraction', 'neighborhood_radius',
    'out_value', 'progress_text', 'slice_range_x', 'slice_range_y',
    'slice_range_z'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageThresholdConnectivity, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageThresholdConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['replace_in', 'replace_out'], [], ['active_component',
            'in_value', 'neighborhood_fraction', 'neighborhood_radius',
            'out_value', 'slice_range_x', 'slice_range_y', 'slice_range_z']),
            title='Edit ImageThresholdConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageThresholdConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


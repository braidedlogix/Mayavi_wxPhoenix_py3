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


class ShepardMethod(ImageAlgorithm):
    """
    ShepardMethod - interpolate points and associated scalars onto
    volume using the method of Shepard
    
    Superclass: ImageAlgorithm
    
    ShepardMethod is a filter used to interpolate point scalar values
    using Shepard's method. The method works by resampling the scalars
    associated with points defined on an arbitrary dataset onto a volume
    (i.e., structured points) dataset. The influence functions are
    described as "inverse distance weighted". Once the interpolation is
    performed across the volume, the usual volume visualization
    techniques (e.g., iso-contouring or volume rendering) can be used.
    
    Note that this implementation also provides the ability to specify
    the power parameter p. Given the generalized Inverse Distance
    Weighting (IDW) function with distance between points measured as
    d(x,xi), p is defined as:
    
    u(x) = Sum(wi(x) * ui) / Sum(wi(x)) if d(x,xi) != 0 u(x) = ui        
                      if d(x,xi) == 0
    
    where wi(x) = 1 / (d(x,xi)^p  Typically p=2, so the weights wi(x) are
    the inverse of the distance squared. However, power parameters > 2
    can be used which assign higher weights for data closer to the
    interpolated point; or <2 which assigns greater weight to points
    further away. (Note that if p!=2, performance may be significantly
    impacted as the algorihm is tuned for p=2.)
    
    @warning
    Strictly speaking, this is a modified Shepard's methodsince only
    points within the maxium_distance are used for interpolation. By
    setting the maximum distance to include the entire bounding box and
    therefore all points, the class executes much slower but incorporates
    all points into the interpolation process (i.e., a pure Shepard
    method).
    
    @warning
    The input to this filter is any dataset type. This filter can be used
    to resample the points of any type of dataset onto the output volume;
    i.e., the input data need not be unstructured with explicit point
    representations.
    
    @warning
    The bounds of the data (i.e., the sample space) is automatically
    computed if not set by the user.
    
    @warning
    If you use a maximum distance less than 1.0 (i.e., using a modified
    Shephard's method), some output points may never receive a
    contribution. The final value of these points can be specified with
    the "_null_value" instance variable.
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    GaussianSplatter CheckerboardSplatter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkShepardMethod, obj, update, **traits)
    
    maximum_distance = traits.Trait(0.25, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify the maximum influence distance of each input point. This
        distance is a fraction of the length of the diagonal of the
        sample space. Thus, values of 1.0 will cause each input point to
        influence all points in the volume dataset. Values less than 1.0
        can improve performance significantly. By default the maximum
        distance is 0.25.
        """
    )

    def _maximum_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumDistance,
                        self.maximum_distance)

    model_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _model_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModelBounds,
                        self.model_bounds)

    null_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the value for output points not receiving a contribution from
        any input point(s). Output points may not receive a contribution
        when the maximum_distance < 1.
        """
    )

    def _null_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNullValue,
                        self.null_value)

    power_parameter = traits.Trait(2.0, traits.Range(0.001, 100.0, enter_set=True, auto_set=False), help=\
        """
        Set / Get the power parameter p. By default p=2. Values (which
        must be a positive, real value) != 2 may affect performance
        significantly.
        """
    )

    def _power_parameter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPowerParameter,
                        self.power_parameter)

    sample_dimensions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(50, 50, 50), cols=3, help=\
        """
        Set the i-j-k dimensions on which to interpolate the input
        points.
        """
    )

    def _sample_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleDimensions,
                        self.sample_dimensions)

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

    def compute_model_bounds(self, *args):
        """
        V.compute_model_bounds([float, float, float], [float, float, float])
             -> float
        C++: double ComputeModelBounds(double origin[3], double ar[3])
        Compute model_bounds from the input geometry.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeModelBounds, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_distance', 'GetMaximumDistance'), ('model_bounds',
    'GetModelBounds'), ('null_value', 'GetNullValue'), ('power_parameter',
    'GetPowerParameter'), ('sample_dimensions', 'GetSampleDimensions'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'maximum_distance', 'model_bounds', 'null_value',
    'power_parameter', 'progress_text', 'sample_dimensions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ShepardMethod, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ShepardMethod properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['maximum_distance', 'model_bounds', 'null_value',
            'power_parameter', 'sample_dimensions']),
            title='Edit ShepardMethod properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ShepardMethod properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


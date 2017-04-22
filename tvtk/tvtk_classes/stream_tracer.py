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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class StreamTracer(PolyDataAlgorithm):
    """
    StreamTracer - Streamline generator
    
    Superclass: PolyDataAlgorithm
    
    StreamTracer is a filter that integrates a vector field to
    generate streamlines. The integration is performed using a specified
    integrator, by default Runge-Kutta2.
    
    StreamTracer produces polylines as the output, with each cell
    (i.e., polyline) representing a streamline. The attribute values
    associated with each streamline are stored in the cell data, whereas
    those associated with streamline-points are stored in the point data.
    
    StreamTracer supports forward (the default), backward, and
    combined (i.e., BOTH) integration. The length of a streamline is
    governed by specifying a maximum value either in physical arc length
    or in (local) cell length. Otherwise, the integration terminates upon
    exiting the flow field domain, or if the particle speed is reduced to
    a value less than a specified terminal speed, or when a maximum
    number of steps is completed. The specific reason for the termination
    is stored in a cell array named reason_for_termination.
    
    Note that normalized vectors are adopted in streamline integration,
    which achieves high numerical accuracy/smoothness of flow lines that
    is particularly guaranteed for Runge-Kutta45 with adaptive step size
    and error control). In support of this feature, the underlying step
    size is ALWAYS in arc length unit (LENGTH_UNIT) while the 'real' time
    interval (virtual for steady flows) that a particle actually takes to
    trave in a single step is obtained by dividing the arc length by the
    LOCAL speed. The overall elapsed time (i.e., the life span) of the
    particle is the sum of those individual step-wise time intervals.
    
    The quality of streamline integration can be controlled by setting
    the initial integration step (_initial_integration_step), particularly
    for Runge-Kutta2 and Runge-Kutta4 (with a fixed step size), and in
    the case of Runge-Kutta45 (with an adaptive step size and error
    control) the minimum integration step, the maximum integration step,
    and the maximum error. These steps are in either LENGTH_UNIT or
    CELL_LENGTH_UNIT while the error is in physical arc length. For the
    former two integrators, there is a trade-off between integration
    speed and streamline quality.
    
    The integration time, vorticity, rotation and angular velocity are
    stored in point data arrays named "_integration_time", "Vorticity",
    "Rotation" and "_angular_velocity", respectively (vorticity, rotation
    and angular velocity are computed only when compute_vorticity is on).
    All point data attributes in the source dataset are interpolated on
    the new streamline points.
    
    StreamTracer supports integration through any type of dataset.
    Thus if the dataset contains 2d cells like polygons or triangles, the
    integration is constrained to lie on the surface defined by 2d cells.
    
    The starting point, or the so-called 'seed', of a streamline may be
    set in two different ways. Starting from global x-y-z "position"
    allows you to start a single trace at a specified x-y-z coordinate.
    If you specify a source object, traces will be generated from each
    point in the source that is inside the dataset.
    
    @sa
    RibbonFilter RuledSurfaceFilter InitialValueProblemSolver
    RungeKutta2 RungeKutta4 RungeKutta45 TemporalStreamTracer
    AbstractInterpolatedVelocityField InterpolatedVelocityField
    CellLocatorInterpolatedVelocityField
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStreamTracer, obj, update, **traits)
    
    surface_streamlines = tvtk_base.false_bool_trait(help=\
        """
        Set/Unset the streamlines to be computed on a surface
        """
    )

    def _surface_streamlines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSurfaceStreamlines,
                        self.surface_streamlines_)

    integration_direction = traits.Trait('forward',
    tvtk_base.TraitRevPrefixMap({'forward': 0, 'backward': 1, 'both': 2}), help=\
        """
        Specify whether the streamline is integrated in the upstream or
        downstream direction.
        """
    )

    def _integration_direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntegrationDirection,
                        self.integration_direction_)

    integrator_type = traits.Trait('runge_kutta2',
    tvtk_base.TraitRevPrefixMap({'runge_kutta2': 0, 'runge_kutta4': 1, 'runge_kutta45': 2}), help=\
        """
        Set/get the integrator type to be used for streamline generation.
        The object passed is not actually used but is cloned with
        new_instance in the process of integration  (prototype pattern).
        The default is Runge-Kutta2. The integrator can also be changed
        using set_integrator_type. The recognized solvers are: RUNGE_KUTTA2
         = 0 RUNGE_KUTTA4  = 1 RUNGE_KUTTA45 = 2
        """
    )

    def _integrator_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntegratorType,
                        self.integrator_type_)

    compute_vorticity = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Turn on/off vorticity computation at streamline points (necessary
        for generating proper stream-ribbons using the RibbonFilter.
        """
    )

    def _compute_vorticity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeVorticity,
                        self.compute_vorticity)

    initial_integration_step = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Specify the Initial step size used for line integration,
        expressed in: LENGTH_UNIT      = 1 CELL_LENGTH_UNIT = 2 (either
        the starting size for an adaptive integrator, e.g., RK45, or the
        constant / fixed size for non-adaptive ones, i.e., RK2 and RK4)
        """
    )

    def _initial_integration_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInitialIntegrationStep,
                        self.initial_integration_step)

    integration_step_unit = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Specify a uniform integration step unit for
        minimum_integration_step, initial_integration_step, and
        maximum_integration_step. NOTE: The valid unit is now limited to
        only LENGTH_UNIT (1) and CELL_LENGTH_UNIT (2), EXCLUDING the
        previously-supported TIME_UNIT.
        """
    )

    def _integration_step_unit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntegrationStepUnit,
                        self.integration_step_unit)

    def _get_integrator(self):
        return wrap_vtk(self._vtk_obj.GetIntegrator())
    def _set_integrator(self, arg):
        old_val = self._get_integrator()
        self._wrap_call(self._vtk_obj.SetIntegrator,
                        deref_vtk(arg))
        self.trait_property_changed('integrator', old_val, arg)
    integrator = traits.Property(_get_integrator, _set_integrator, help=\
        """
        Set/get the integrator type to be used for streamline generation.
        The object passed is not actually used but is cloned with
        new_instance in the process of integration  (prototype pattern).
        The default is Runge-Kutta2. The integrator can also be changed
        using set_integrator_type. The recognized solvers are: RUNGE_KUTTA2
         = 0 RUNGE_KUTTA4  = 1 RUNGE_KUTTA45 = 2
        """
    )

    maximum_error = traits.Float(1e-06, enter_set=True, auto_set=False, help=\
        """
        Specify the maximum error tolerated throughout streamline
        integration.
        """
    )

    def _maximum_error_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumError,
                        self.maximum_error)

    maximum_integration_step = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify the Maximum step size used for line integration,
        expressed in: LENGTH_UNIT      = 1 CELL_LENGTH_UNIT = 2 (Only
        valid for an adaptive integrator, e.g., RK45)
        """
    )

    def _maximum_integration_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumIntegrationStep,
                        self.maximum_integration_step)

    maximum_number_of_steps = traits.Int(2000, enter_set=True, auto_set=False, help=\
        """
        Specify the maximum number of steps for integrating a streamline.
        """
    )

    def _maximum_number_of_steps_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfSteps,
                        self.maximum_number_of_steps)

    maximum_propagation = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify the maximum length of a streamline expressed in
        LENGTH_UNIT.
        """
    )

    def _maximum_propagation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumPropagation,
                        self.maximum_propagation)

    minimum_integration_step = traits.Float(0.01, enter_set=True, auto_set=False, help=\
        """
        Specify the Minimum step size used for line integration,
        expressed in: LENGTH_UNIT      = 1 CELL_LENGTH_UNIT = 2 (Only
        valid for an adaptive integrator, e.g., RK45)
        """
    )

    def _minimum_integration_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumIntegrationStep,
                        self.minimum_integration_step)

    rotation_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        This can be used to scale the rate with which the streamribbons
        twist. The default is 1.
        """
    )

    def _rotation_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRotationScale,
                        self.rotation_scale)

    start_position = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _start_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartPosition,
                        self.start_position)

    terminal_speed = traits.Float(1e-12, enter_set=True, auto_set=False, help=\
        """
        Specify the terminal speed value, below which integration is
        terminated.
        """
    )

    def _terminal_speed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTerminalSpeed,
                        self.terminal_speed)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    source = traits.Property(_get_source, help=\
        """
        Specify the source object used to generate starting points
        (seeds). Note that this method does not connect the pipeline. The
        algorithm will work on the input data as it is without updating
        the producer of the data. See set_source_connection for connecting
        the pipeline.
        """
    )

    def set_interpolator_prototype(self, *args):
        """
        V.set_interpolator_prototype(AbstractInterpolatedVelocityField)
        C++: void SetInterpolatorPrototype(
            AbstractInterpolatedVelocityField *ivf)
        The object used to interpolate the velocity field during
        integration is of the same class as this prototype.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInterpolatorPrototype, *my_args)
        return ret

    def set_interpolator_type(self, *args):
        """
        V.set_interpolator_type(int)
        C++: void SetInterpolatorType(int interpType)
        Set the type of the velocity field interpolator to determine
        whether InterpolatedVelocityField
        (INTERPOLATOR_WITH_DATASET_POINT_LOCATOR) or
        CellLocatorInterpolatedVelocityField
        (INTERPOLATOR_WITH_CELL_LOCATOR) is employed for locating cells
        during streamline integration. The latter (adopting
        AbstractCellLocator sub-classes such as CellLocator and
        ModifiedBSPTree) is more robust then the former (through
        DataSet / PointSet::FindCell() coupled with
        PointLocator).
        """
        ret = self._wrap_call(self._vtk_obj.SetInterpolatorType, *args)
        return ret

    def set_interpolator_type_to_cell_locator(self):
        """
        V.set_interpolator_type_to_cell_locator()
        C++: void SetInterpolatorTypeToCellLocator()
        Set the velocity field interpolator type to the one involving a
        cell locator.
        """
        ret = self._vtk_obj.SetInterpolatorTypeToCellLocator()
        return ret
        

    def set_interpolator_type_to_data_set_point_locator(self):
        """
        V.set_interpolator_type_to_data_set_point_locator()
        C++: void SetInterpolatorTypeToDataSetPointLocator()
        Set the velocity field interpolator type to the one involving a
        dataset point locator.
        """
        ret = self._vtk_obj.SetInterpolatorTypeToDataSetPointLocator()
        return ret
        

    def set_source_connection(self, *args):
        """
        V.set_source_connection(AlgorithmOutput)
        C++: void SetSourceConnection(AlgorithmOutput *algOutput)
        Specify the source object used to generate starting points
        (seeds). New style.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceConnection, *my_args)
        return ret

    def set_source_data(self, *args):
        """
        V.set_source_data(DataSet)
        C++: void SetSourceData(DataSet *source)
        Specify the source object used to generate starting points
        (seeds). Note that this method does not connect the pipeline. The
        algorithm will work on the input data as it is without updating
        the producer of the data. See set_source_connection for connecting
        the pipeline.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceData, *my_args)
        return ret

    _updateable_traits_ = \
    (('surface_streamlines', 'GetSurfaceStreamlines'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('integration_direction',
    'GetIntegrationDirection'), ('integrator_type', 'GetIntegratorType'),
    ('compute_vorticity', 'GetComputeVorticity'),
    ('initial_integration_step', 'GetInitialIntegrationStep'),
    ('integration_step_unit', 'GetIntegrationStepUnit'), ('maximum_error',
    'GetMaximumError'), ('maximum_integration_step',
    'GetMaximumIntegrationStep'), ('maximum_number_of_steps',
    'GetMaximumNumberOfSteps'), ('maximum_propagation',
    'GetMaximumPropagation'), ('minimum_integration_step',
    'GetMinimumIntegrationStep'), ('rotation_scale', 'GetRotationScale'),
    ('start_position', 'GetStartPosition'), ('terminal_speed',
    'GetTerminalSpeed'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'surface_streamlines', 'integration_direction',
    'integrator_type', 'compute_vorticity', 'initial_integration_step',
    'integration_step_unit', 'maximum_error', 'maximum_integration_step',
    'maximum_number_of_steps', 'maximum_propagation',
    'minimum_integration_step', 'progress_text', 'rotation_scale',
    'start_position', 'terminal_speed'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StreamTracer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StreamTracer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['surface_streamlines'], ['integration_direction',
            'integrator_type'], ['compute_vorticity', 'initial_integration_step',
            'integration_step_unit', 'maximum_error', 'maximum_integration_step',
            'maximum_number_of_steps', 'maximum_propagation',
            'minimum_integration_step', 'rotation_scale', 'start_position',
            'terminal_speed']),
            title='Edit StreamTracer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StreamTracer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.object import Object


class InitialValueProblemSolver(Object):
    """
    InitialValueProblemSolver - Integrate a set of ordinary
    differential equations (initial value problem) in time.
    
    Superclass: Object
    
    Given a FunctionSet which returns d_f_i(x_j, t)/dt given x_j and t,
    InitialValueProblemSolver computes the value of F_i at t+deltat.
    
    @warning
    InitialValueProblemSolver and it's subclasses are not thread-safe.
    You should create a new integrator for each thread.
    
    @sa
    RungeKutta2 RungeKutta4
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInitialValueProblemSolver, obj, update, **traits)
    
    def _get_function_set(self):
        return wrap_vtk(self._vtk_obj.GetFunctionSet())
    def _set_function_set(self, arg):
        old_val = self._get_function_set()
        self._wrap_call(self._vtk_obj.SetFunctionSet,
                        deref_vtk(arg))
        self.trait_property_changed('function_set', old_val, arg)
    function_set = traits.Property(_get_function_set, _set_function_set, help=\
        """
        Set / get the dataset used for the implicit function evaluation.
        """
    )

    def compute_next_step(self, *args):
        """
        V.compute_next_step([float, ...], [float, ...], float, float, float,
             float) -> int
        C++: virtual int ComputeNextStep(double *xprev, double *xnext,
            double t, double &delT, double maxError, double &error)
        V.compute_next_step([float, ...], [float, ...], [float, ...], float,
             float, float, float) -> int
        C++: virtual int ComputeNextStep(double *xprev, double *dxprev,
            double *xnext, double t, double &delT, double maxError,
            double &error)
        V.compute_next_step([float, ...], [float, ...], float, float, float,
             float, float, float, float) -> int
        C++: virtual int ComputeNextStep(double *xprev, double *xnext,
            double t, double &delT, double &delTActual, double minStep,
            double maxStep, double maxError, double &error)
        V.compute_next_step([float, ...], [float, ...], [float, ...], float,
             float, float, float, float, float, float) -> int
        C++: virtual int ComputeNextStep(double *xprev, double *dxprev,
            double *xnext, double t, double &delT, double &delTActual,
            double minStep, double maxStep, double maxError,
            double &error)
        Given initial values, xprev , initial time, t and a requested
        time interval, del_t calculate values of x at t+del_t_actual
        (xnext). For certain concrete sub-classes del_t_actual != del_t.
        This occurs when the solver supports adaptive stepsize control.
        If this is the case, the solver tries to change to stepsize such
        that the (estimated) error of the integration is less than
        max_error. The solver will not set the stepsize smaller than
        min_step or larger than max_step. Also note that del_t is an in/out
        argument. Adaptive solvers will modify del_t to reflect the best
        (estimated) size for the next integration step. An estimated
        value for the error is returned (by reference) in error. Note
        that only some concrete sub-classes support this. Otherwise, the
        error is set to 0. This method returns an error code representing
        the nature of the failure: out_of_domain = 1, not_initialized = 2,
        unexpected_value = 3
        """
        ret = self._wrap_call(self._vtk_obj.ComputeNextStep, *args)
        return ret

    def is_adaptive(self):
        """
        V.is_adaptive() -> int
        C++: virtual int IsAdaptive()
        Returns 1 if the solver uses adaptive stepsize control, 0
        otherwise
        """
        ret = self._vtk_obj.IsAdaptive()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InitialValueProblemSolver, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InitialValueProblemSolver properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit InitialValueProblemSolver properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InitialValueProblemSolver properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


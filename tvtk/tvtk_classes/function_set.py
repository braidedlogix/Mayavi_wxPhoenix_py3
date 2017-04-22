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


class FunctionSet(Object):
    """
    FunctionSet - Abstract interface for sets of functions
    
    Superclass: Object
    
    FunctionSet specifies an abstract interface for set of functions
    of the form F_i = F_i(x_j) where F (with i=1..m) are the functions
    and x (with j=1..n) are the independent variables. The only supported
    operation is the  function evaluation at x_j.
    
    @sa
    ImplicitDataSet InterpolatedVelocityField
    InitialValueProblemSolver
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFunctionSet, obj, update, **traits)
    
    def _get_number_of_functions(self):
        return self._vtk_obj.GetNumberOfFunctions()
    number_of_functions = traits.Property(_get_number_of_functions, help=\
        """
        Return the number of functions. Note that this is constant for a
        given type of set of functions and can not be changed at run
        time.
        """
    )

    def _get_number_of_independent_variables(self):
        return self._vtk_obj.GetNumberOfIndependentVariables()
    number_of_independent_variables = traits.Property(_get_number_of_independent_variables, help=\
        """
        Return the number of independent variables. Note that this is
        constant for a given type of set of functions and can not be
        changed at run time.
        """
    )

    def function_values(self, *args):
        """
        V.function_values([float, ...], [float, ...]) -> int
        C++: virtual int FunctionValues(double *x, double *f)
        Evaluate functions at x_j. x and f have to point to valid double
        arrays of appropriate sizes obtained with get_number_of_functions()
        and get_number_of_independent_variables.
        """
        ret = self._wrap_call(self._vtk_obj.FunctionValues, *args)
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
            return super(FunctionSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FunctionSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit FunctionSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FunctionSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


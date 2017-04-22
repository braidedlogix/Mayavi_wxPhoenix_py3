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

from tvtk.tvtk_classes.implicit_function import ImplicitFunction


class ImplicitSum(ImplicitFunction):
    """
    ImplicitSum - implicit sum of other implicit functions
    
    Superclass: ImplicitFunction
    
    ImplicitSum produces a linear combination of other implicit
    functions. The contribution of each function is weighted by a scalar
    coefficient. The normalize_by_weight option normalizes the output so
    that the scalar weights add up to 1. Note that this function gives
    accurate sums and gradients only if the input functions are linear.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitSum, obj, update, **traits)
    
    normalize_by_weight = tvtk_base.false_bool_trait(help=\
        """
        When calculating the function and gradient values of the
        composite function, setting normalize_by_weight on will divide the
        final result by the total weight of the component functions. This
        process does not otherwise normalize the gradient vector. By
        default, normalize_by_weight is off.
        """
    )

    def _normalize_by_weight_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalizeByWeight,
                        self.normalize_by_weight_)

    def add_function(self, *args):
        """
        V.add_function(ImplicitFunction, float)
        C++: void AddFunction(ImplicitFunction *in, double weight)
        V.add_function(ImplicitFunction)
        C++: void AddFunction(ImplicitFunction *in)
        Add another implicit function to the list of functions, along
        with a weighting factor.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddFunction, *my_args)
        return ret

    def remove_all_functions(self):
        """
        V.remove_all_functions()
        C++: void RemoveAllFunctions()
        Remove all functions from the list.
        """
        ret = self._vtk_obj.RemoveAllFunctions()
        return ret
        

    def set_function_weight(self, *args):
        """
        V.set_function_weight(ImplicitFunction, float)
        C++: void SetFunctionWeight(ImplicitFunction *f, double weight)
        Set the weight (coefficient) of the given function to be weight.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetFunctionWeight, *my_args)
        return ret

    _updateable_traits_ = \
    (('normalize_by_weight', 'GetNormalizeByWeight'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'normalize_by_weight'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitSum, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitSum properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['normalize_by_weight'], [], []),
            title='Edit ImplicitSum properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitSum properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


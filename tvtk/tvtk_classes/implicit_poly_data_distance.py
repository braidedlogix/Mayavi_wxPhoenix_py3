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


class ImplicitPolyDataDistance(ImplicitFunction):
    """
    ImplicitPolyDataDistance - Implicit function that computes the
    distance from a point x to the nearest point p on an input
    PolyData.
    
    Superclass: ImplicitFunction
    
    The sign of the function is set to the sign of the dot product
    between the angle-weighted pseudonormal at the nearest surface point
    and the vector x - p. Points interior to the geometry have a negative
    distance, points on the exterior have a positive distance, and points
    on the input PolyData have a distance of zero. The gradient of the
    function is the angle-weighted pseudonormal at the nearest point.
    
    Baerentzen, J. A. and Aanaes, H. (2005). Signed distance computation
    using the angle weighted pseudonormal. IEEE Transactions on
    Visualization and Computer Graphics, 11:243-253.
    
    This code was contributed in the VTK Journal paper: "Boolean Operations on Surfaces in VTK Without External
    Libraries" by Cory Quammen, Chris Weigle C., Russ Taylor
    http://hdl.handle.net/10380/3262
    http://www.midasjournal.org/browse/publication/797
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImplicitPolyDataDistance, obj, update, **traits)
    
    no_closest_point = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _no_closest_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNoClosestPoint,
                        self.no_closest_point)

    no_gradient = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _no_gradient_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNoGradient,
                        self.no_gradient)

    no_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/get the function value to use if no input PolyData
        specified.
        """
    )

    def _no_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNoValue,
                        self.no_value)

    tolerance = traits.Float(1e-12, enter_set=True, auto_set=False, help=\
        """
        Set/get the tolerance usued for the locator.
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def evaluate_function_and_get_closest_point(self, *args):
        """
        V.evaluate_function_and_get_closest_point([float, float, float],
            [float, float, float]) -> float
        C++: double EvaluateFunctionAndGetClosestPoint(double x[3],
            double closestPoint[3])
        Evaluate plane equation of nearest triangle to point x[3] and
        provides closest point on an input PolyData.
        """
        ret = self._wrap_call(self._vtk_obj.EvaluateFunctionAndGetClosestPoint, *args)
        return ret

    def set_input(self, *args):
        """
        V.set_input(PolyData)
        C++: void SetInput(PolyData *input)
        Set the input PolyData used for the implicit function
        evaluation.  Passes input through an internal instance of
        TriangleFilter to remove vertices and lines, leaving only
        triangular polygons for evaluation as implicit planes.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('no_closest_point', 'GetNoClosestPoint'),
    ('no_gradient', 'GetNoGradient'), ('no_value', 'GetNoValue'),
    ('tolerance', 'GetTolerance'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'no_closest_point',
    'no_gradient', 'no_value', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImplicitPolyDataDistance, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImplicitPolyDataDistance properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['no_closest_point', 'no_gradient', 'no_value',
            'tolerance']),
            title='Edit ImplicitPolyDataDistance properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImplicitPolyDataDistance properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


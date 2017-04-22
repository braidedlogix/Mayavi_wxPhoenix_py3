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


class Sphere(ImplicitFunction):
    """
    Sphere - implicit function for a sphere
    
    Superclass: ImplicitFunction
    
    Sphere computes the implicit function and/or gradient for a
    sphere. Sphere is a concrete implementation of
    ImplicitFunction. Additional methods are available for
    sphere-related computations, such as computing bounding spheres for a
    set of points, or set of spheres.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSphere, obj, update, **traits)
    
    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    radius = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set / get the radius of the sphere. The default is 0.5.
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    def compute_bounding_sphere(self, *args):
        """
        V.compute_bounding_sphere([float, ...], int, [float, float, float,
            float], [int, int])
        C++: static void ComputeBoundingSphere(double *pts,
            IdType numPts, double sphere[4], IdType hints[2])
        Create a bounding sphere from a set of points. The set of points
        is defined by an array of doubles, in the order of x-y-z (which
        repeats for each point).  An optional hints array provides a
        guess for the initial bounding sphere; the two values in the
        hints array are the two points expected to be the furthest apart.
        The output sphere consists of a center (x-y-z) and a radius.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeBoundingSphere, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('center', 'GetCenter'), ('radius',
    'GetRadius'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'center', 'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Sphere, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Sphere properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['center', 'radius']),
            title='Edit Sphere properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Sphere properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


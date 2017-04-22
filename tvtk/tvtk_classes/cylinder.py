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


class Cylinder(ImplicitFunction):
    """
    Cylinder - implicit function for a cylinder
    
    Superclass: ImplicitFunction
    
    Cylinder computes the implicit function and function gradient for
    a cylinder using F(r)=r^2-Radius^2. Cylinder is a concrete
    implementation of ImplicitFunction. By default the Cylinder is
    centered at the origin and the axis of rotation is along the y-axis.
    You can redefine the center and axis of rotation by setting the
    Center and Axis data members. (Note that it is also possible to use
    the superclass' ImplicitFunction transformation matrix if
    necessary to reposition by using function_value() and
    function_gradient().)
    
    @warning
    The cylinder is infinite in extent. To truncate the cylinder in
    modeling operations use the ImplicitBoolean in combination with
    clipping planes.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCylinder, obj, update, **traits)
    
    axis = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 1.0, 0.0), cols=3, help=\
        """
        Set/Get the axis of the cylinder. If the axis is not specified as
        a unit vector, it will be normalized. If zero-length axis vector
        is used as input to this method, it will be ignored.
        """
    )

    def _axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxis,
                        self.axis)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    radius = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the cylinder radius.
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('axis', 'GetAxis'), ('center',
    'GetCenter'), ('radius', 'GetRadius'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'axis', 'center', 'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Cylinder, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Cylinder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['axis', 'center', 'radius']),
            title='Edit Cylinder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Cylinder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


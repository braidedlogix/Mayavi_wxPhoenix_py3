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

from tvtk.tvtk_classes.parametric_function import ParametricFunction


class ParametricSuperEllipsoid(ParametricFunction):
    """
    ParametricSuperEllipsoid - Generate a superellipsoid.
    
    Superclass: ParametricFunction
    
    ParametricSuperEllipsoid generates a superellipsoid.  A
    superellipsoid is a versatile primitive that is controlled by two
    parameters n1 and n2. As special cases it can represent a sphere,
    square box, and closed cylindrical can.
    
    For further information about this surface, please consult the
    technical description "Parametric surfaces" in
    http://www.vtk.org/publications in the "VTK Technical Documents"
    section in the VTk.org web pages.
    
    Also see: http://paulbourke.net/geometry/superellipse/
    
    @warning
    Care needs to be taken specifying the bounds correctly. You may need
    to carefully adjust minimum_u, minimum_v, maximum_u, maximum_v.
    
    @par Thanks: Andrew Maclean andrew.amaclean@gmail.com for creating
    and contributing the class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParametricSuperEllipsoid, obj, update, **traits)
    
    n1 = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the "squareness" parameter in the z axis.  Default is 1.
        """
    )

    def _n1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetN1,
                        self.n1)

    n2 = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the "squareness" parameter in the x-y plane. Default is
        1.
        """
    )

    def _n2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetN2,
                        self.n2)

    x_radius = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling factor for the x-axis. Default is 1.
        """
    )

    def _x_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXRadius,
                        self.x_radius)

    y_radius = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling factor for the y-axis. Default is 1.
        """
    )

    def _y_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYRadius,
                        self.y_radius)

    z_radius = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling factor for the z-axis. Default is 1.
        """
    )

    def _z_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZRadius,
                        self.z_radius)

    _updateable_traits_ = \
    (('clockwise_ordering', 'GetClockwiseOrdering'),
    ('derivatives_available', 'GetDerivativesAvailable'), ('join_u',
    'GetJoinU'), ('join_v', 'GetJoinV'), ('join_w', 'GetJoinW'),
    ('twist_u', 'GetTwistU'), ('twist_v', 'GetTwistV'), ('twist_w',
    'GetTwistW'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('n1', 'GetN1'), ('n2', 'GetN2'),
    ('x_radius', 'GetXRadius'), ('y_radius', 'GetYRadius'), ('z_radius',
    'GetZRadius'), ('maximum_u', 'GetMaximumU'), ('maximum_v',
    'GetMaximumV'), ('maximum_w', 'GetMaximumW'), ('minimum_u',
    'GetMinimumU'), ('minimum_v', 'GetMinimumV'), ('minimum_w',
    'GetMinimumW'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['clockwise_ordering', 'debug', 'derivatives_available',
    'global_warning_display', 'join_u', 'join_v', 'join_w', 'twist_u',
    'twist_v', 'twist_w', 'maximum_u', 'maximum_v', 'maximum_w',
    'minimum_u', 'minimum_v', 'minimum_w', 'n1', 'n2', 'x_radius',
    'y_radius', 'z_radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParametricSuperEllipsoid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ParametricSuperEllipsoid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['clockwise_ordering', 'derivatives_available', 'join_u',
            'join_v', 'join_w', 'twist_u', 'twist_v', 'twist_w'], [],
            ['maximum_u', 'maximum_v', 'maximum_w', 'minimum_u', 'minimum_v',
            'minimum_w', 'n1', 'n2', 'x_radius', 'y_radius', 'z_radius']),
            title='Edit ParametricSuperEllipsoid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParametricSuperEllipsoid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


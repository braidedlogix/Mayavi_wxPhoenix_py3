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


class ParametricSuperToroid(ParametricFunction):
    """
    ParametricSuperToroid - Generate a supertoroid.
    
    Superclass: ParametricFunction
    
    ParametricSuperToroid generates a supertoroid.  Essentially a
    supertoroid is a torus with the sine and cosine terms raised to a
    power. A supertoroid is a versatile primitive that is controlled by
    four parameters r0, r1, n1 and n2. r0, r1 determine the type of torus
    whilst the value of n1 determines the shape of the torus ring and n2
    determines the shape of the cross section of the ring. It is the
    different values of these powers which give rise to a family of 3d
    shapes that are all basically toroidal in shape.
    
    For further information about this surface, please consult the
    technical description "Parametric surfaces" in
    http://www.vtk.org/publications in the "VTK Technical Documents"
    section in the VTk.org web pages.
    
    Also see: http://paulbourke.net/geometry/torus/#super.
    
    @warning
    Care needs to be taken specifying the bounds correctly. You may need
    to carefully adjust minimum_u, minimum_v, maximum_u, maximum_v.
    
    @par Thanks: Andrew Maclean andrew.amaclean@gmail.com for creating
    and contributing the class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParametricSuperToroid, obj, update, **traits)
    
    cross_section_radius = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the radius of the cross section of ring of the
        supertoroid. Default = 0.5.
        """
    )

    def _cross_section_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCrossSectionRadius,
                        self.cross_section_radius)

    n1 = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the shape of the torus ring.  Default is 1.
        """
    )

    def _n1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetN1,
                        self.n1)

    n2 = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the shape of the cross section of the ring. Default is 1.
        """
    )

    def _n2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetN2,
                        self.n2)

    ring_radius = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the radius from the center to the middle of the ring of
        the supertoroid. Default is 1.
        """
    )

    def _ring_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRingRadius,
                        self.ring_radius)

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
    'GetGlobalWarningDisplay'), ('cross_section_radius',
    'GetCrossSectionRadius'), ('n1', 'GetN1'), ('n2', 'GetN2'),
    ('ring_radius', 'GetRingRadius'), ('x_radius', 'GetXRadius'),
    ('y_radius', 'GetYRadius'), ('z_radius', 'GetZRadius'), ('maximum_u',
    'GetMaximumU'), ('maximum_v', 'GetMaximumV'), ('maximum_w',
    'GetMaximumW'), ('minimum_u', 'GetMinimumU'), ('minimum_v',
    'GetMinimumV'), ('minimum_w', 'GetMinimumW'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['clockwise_ordering', 'debug', 'derivatives_available',
    'global_warning_display', 'join_u', 'join_v', 'join_w', 'twist_u',
    'twist_v', 'twist_w', 'cross_section_radius', 'maximum_u',
    'maximum_v', 'maximum_w', 'minimum_u', 'minimum_v', 'minimum_w', 'n1',
    'n2', 'ring_radius', 'x_radius', 'y_radius', 'z_radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParametricSuperToroid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ParametricSuperToroid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['clockwise_ordering', 'derivatives_available', 'join_u',
            'join_v', 'join_w', 'twist_u', 'twist_v', 'twist_w'], [],
            ['cross_section_radius', 'maximum_u', 'maximum_v', 'maximum_w',
            'minimum_u', 'minimum_v', 'minimum_w', 'n1', 'n2', 'ring_radius',
            'x_radius', 'y_radius', 'z_radius']),
            title='Edit ParametricSuperToroid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParametricSuperToroid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


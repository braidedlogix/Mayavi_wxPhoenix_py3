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

from tvtk.tvtk_classes.spline import Spline


class KochanekSpline(Spline):
    """
    KochanekSpline - computes an interpolating spline using a Kochanek
    basis.
    
    Superclass: Spline
    
    Implements the Kochanek interpolating spline described in: Kochanek,
    D., Bartels, R., "Interpolating Splines with Local Tension,
    Continuity, and Bias Control," Computer Graphics, vol. 18, no. 3, pp.
    33-41, July 1984. These splines give the user more control over the
    shape of the curve than the cardinal splines implemented in
    CardinalSpline. Three parameters can be specified. All have a
    range from -1 to 1.
    
    Tension controls how sharply the curve bends at an input point. A
    value of -1 produces more slack in the curve. A value of 1 tightens
    the curve.
    
    Continuity controls the continuity of the first derivative at input
    points.
    
    Bias controls the direction of the curve at it passes through an
    input point. A value of -1 undershoots the point while a value of 1
    overshoots the point.
    
    These three parameters give the user broad control over the shape of
    the interpolating spline. The original Kochanek paper describes the
    effects nicely and is recommended reading.
    
    @sa
    Spline CardinalSpline
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkKochanekSpline, obj, update, **traits)
    
    default_bias = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the bias for all points. Default is 0.
        """
    )

    def _default_bias_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultBias,
                        self.default_bias)

    default_continuity = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the continuity for all points. Default is 0.
        """
    )

    def _default_continuity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultContinuity,
                        self.default_continuity)

    default_tension = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the tension for all points. Default is 0.
        """
    )

    def _default_tension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultTension,
                        self.default_tension)

    _updateable_traits_ = \
    (('clamp_value', 'GetClampValue'), ('closed', 'GetClosed'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('default_bias', 'GetDefaultBias'), ('default_continuity',
    'GetDefaultContinuity'), ('default_tension', 'GetDefaultTension'),
    ('left_constraint', 'GetLeftConstraint'), ('left_value',
    'GetLeftValue'), ('right_constraint', 'GetRightConstraint'),
    ('right_value', 'GetRightValue'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['clamp_value', 'closed', 'debug', 'global_warning_display',
    'default_bias', 'default_continuity', 'default_tension',
    'left_constraint', 'left_value', 'right_constraint', 'right_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(KochanekSpline, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit KochanekSpline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['clamp_value', 'closed'], [], ['default_bias',
            'default_continuity', 'default_tension', 'left_constraint',
            'left_value', 'right_constraint', 'right_value']),
            title='Edit KochanekSpline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit KochanekSpline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


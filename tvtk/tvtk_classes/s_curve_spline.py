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


class SCurveSpline(Spline):
    """
    SCurveSpline - computes an interpolating spline using a a SCurve
    basis.
    
    Superclass: Spline
    
    SCurveSpline is a concrete implementation of Spline using a
    SCurve basis.
    
    @sa
    Spline KochanekSpline
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSCurveSpline, obj, update, **traits)
    
    node_weight = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _node_weight_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNodeWeight,
                        self.node_weight)

    _updateable_traits_ = \
    (('clamp_value', 'GetClampValue'), ('closed', 'GetClosed'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('node_weight', 'GetNodeWeight'), ('left_constraint',
    'GetLeftConstraint'), ('left_value', 'GetLeftValue'),
    ('right_constraint', 'GetRightConstraint'), ('right_value',
    'GetRightValue'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['clamp_value', 'closed', 'debug', 'global_warning_display',
    'left_constraint', 'left_value', 'node_weight', 'right_constraint',
    'right_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SCurveSpline, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SCurveSpline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['clamp_value', 'closed'], [], ['left_constraint', 'left_value',
            'node_weight', 'right_constraint', 'right_value']),
            title='Edit SCurveSpline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SCurveSpline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


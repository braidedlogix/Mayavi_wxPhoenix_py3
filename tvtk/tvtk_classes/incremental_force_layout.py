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


class IncrementalForceLayout(Object):
    """
    IncrementalForceLayout - incremental force-directed layout.
    
    Superclass: Object
    
    Performs an incremental force-directed layout of a graph. Set the
    graph then iteratively execute update_positions() to update the vertex
    positions. Note that this directly modifies the vertex locations in
    the graph.
    
    This layout is modeled after D3's force layout described at
    https://github.com/mbostock/d3/wiki/Force-Layout
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkIncrementalForceLayout, obj, update, **traits)
    
    alpha = traits.Float(0.10000000149011612, enter_set=True, auto_set=False, help=\
        """
        Set the level of activity in the simulation. Default is 0.1.
        """
    )

    def _alpha_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlpha,
                        self.alpha)

    charge = traits.Float(-50.0, enter_set=True, auto_set=False, help=\
        """
        Set the charge of each vertex. Higher negative values will repel
        vertices from each other more strongly. Default is -30.
        """
    )

    def _charge_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCharge,
                        self.charge)

    distance = traits.Float(20.0, enter_set=True, auto_set=False, help=\
        """
        Set the resting distance of each link in scene units, which is
        equal to pixels when there is no scene scaling. Default is 20.
        """
    )

    def _distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistance,
                        self.distance)

    fixed = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the id of the vertex that will not move during the
        simulation. Set to -1 to allow all the vertices to move.
        """
    )

    def _fixed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFixed,
                        self.fixed)

    friction = traits.Float(0.8999999761581421, enter_set=True, auto_set=False, help=\
        """
        Set the multiplier for scaling down velocity in the simulation,
        where values closer to 1 are more frictionless. Default is 0.95.
        """
    )

    def _friction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFriction,
                        self.friction)

    def _get_graph(self):
        return wrap_vtk(self._vtk_obj.GetGraph())
    def _set_graph(self, arg):
        old_val = self._get_graph()
        self._wrap_call(self._vtk_obj.SetGraph,
                        deref_vtk(arg))
        self.trait_property_changed('graph', old_val, arg)
    graph = traits.Property(_get_graph, _set_graph, help=\
        """
        Set the graph to be positioned.
        """
    )

    gravity = traits.Float(0.10000000149011612, enter_set=True, auto_set=False, help=\
        """
        Set the amount of gravitational pull toward the gravity point.
        Default is 0.01.
        """
    )

    def _gravity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGravity,
                        self.gravity)

    strength = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the rigitity of links in the simulation. Default is 2.
        """
    )

    def _strength_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStrength,
                        self.strength)

    theta = traits.Float(0.800000011920929, enter_set=True, auto_set=False, help=\
        """
        Set the Barnes-Hut threshold for the simulation. Higher values
        will speed the simulation at the expense of some accuracy.
        Default is 0.8.
        """
    )

    def _theta_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTheta,
                        self.theta)

    def update_positions(self):
        """
        V.update_positions()
        C++: void UpdatePositions()
        Perform one iteration of the force-directed layout.
        """
        ret = self._vtk_obj.UpdatePositions()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('alpha', 'GetAlpha'), ('charge',
    'GetCharge'), ('distance', 'GetDistance'), ('fixed', 'GetFixed'),
    ('friction', 'GetFriction'), ('gravity', 'GetGravity'), ('strength',
    'GetStrength'), ('theta', 'GetTheta'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'alpha', 'charge', 'distance',
    'fixed', 'friction', 'gravity', 'strength', 'theta'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(IncrementalForceLayout, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit IncrementalForceLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['alpha', 'charge', 'distance', 'fixed', 'friction',
            'gravity', 'strength', 'theta']),
            title='Edit IncrementalForceLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit IncrementalForceLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


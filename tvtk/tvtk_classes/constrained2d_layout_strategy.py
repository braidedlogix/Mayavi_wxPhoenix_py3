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

from tvtk.tvtk_classes.graph_layout_strategy import GraphLayoutStrategy


class Constrained2DLayoutStrategy(GraphLayoutStrategy):
    """
    Constrained2DLayoutStrategy - a simple fast 2d graph layout that
    looks for a 'constraint' array (vtk_double_array).
    
    Superclass: GraphLayoutStrategy
    
    Any entry in the constraint array will indicate the level of
    impedance a node has to the force calculations during the layout
    optimization. The array is assumed to be normalized between zero and
    one, with one being totally constrained, so no force will be applied
    to the node (i.e. no movement), and zero being full range of movement
    (no constraints).
    
    This class is a density grid based force directed layout strategy.
    Also please note that 'fast' is relative to quite slow. :) The layout
    running time is O(V+E) with an extremely high constant.@par Thanks:
    We would like to thank Mothra for distracting Godzilla while we wrote
    this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkConstrained2DLayoutStrategy, obj, update, **traits)
    
    cool_down_rate = traits.Trait(50.0, traits.Range(0.01, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the Cool-down rate. The higher this number is, the longer
        it will take to "cool-down", and thus, the more the graph will be
        modified. The default is '10' for no particular reason. Note: The
        strong recommendation is that you do not change this parameter.
        :)
        """
    )

    def _cool_down_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCoolDownRate,
                        self.cool_down_rate)

    initial_temperature = traits.Trait(5.0, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Set the initial temperature.  The temperature default is '5' for
        no particular reason Note: The strong recommendation is that you
        do not change this parameter. :)
        """
    )

    def _initial_temperature_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInitialTemperature,
                        self.initial_temperature)

    input_array_name = traits.String('constraint', enter_set=True, auto_set=False, help=\
        """
        Set/Get the input constraint array name. If no input array name
        is set then the name 'constraint' is used.
        """
    )

    def _input_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputArrayName,
                        self.input_array_name)

    iterations_per_layout = traits.Trait(1, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of iterations per layout. The only use for
        this ivar is for the application to do visualizations of the
        layout before it's complete. The default is '100' to match the
        default '_max_number_of_iterations' Note: Changing this parameter is
        just fine :)
        """
    )

    def _iterations_per_layout_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIterationsPerLayout,
                        self.iterations_per_layout)

    max_number_of_iterations = traits.Trait(200, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the maximum number of iterations to be used. The higher
        this number, the more iterations through the algorithm is
        possible, and thus, the more the graph gets modified. The default
        is '100' for no particular reason Note: The strong recommendation
        is that you do not change this parameter. :)
        """
    )

    def _max_number_of_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxNumberOfIterations,
                        self.max_number_of_iterations)

    random_seed = traits.Trait(123, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Seed the random number generator used to jitter point positions.
        This has a significant effect on their final positions when the
        layout is complete.
        """
    )

    def _random_seed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRandomSeed,
                        self.random_seed)

    rest_distance = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Manually set the resting distance. Otherwise the distance is
        computed automatically.
        """
    )

    def _rest_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRestDistance,
                        self.rest_distance)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('cool_down_rate', 'GetCoolDownRate'),
    ('initial_temperature', 'GetInitialTemperature'), ('input_array_name',
    'GetInputArrayName'), ('iterations_per_layout',
    'GetIterationsPerLayout'), ('max_number_of_iterations',
    'GetMaxNumberOfIterations'), ('random_seed', 'GetRandomSeed'),
    ('rest_distance', 'GetRestDistance'), ('edge_weight_field',
    'GetEdgeWeightField'), ('weight_edges', 'GetWeightEdges'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'cool_down_rate',
    'edge_weight_field', 'initial_temperature', 'input_array_name',
    'iterations_per_layout', 'max_number_of_iterations', 'random_seed',
    'rest_distance', 'weight_edges'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Constrained2DLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Constrained2DLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['cool_down_rate', 'edge_weight_field',
            'initial_temperature', 'input_array_name', 'iterations_per_layout',
            'max_number_of_iterations', 'random_seed', 'rest_distance',
            'weight_edges']),
            title='Edit Constrained2DLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Constrained2DLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


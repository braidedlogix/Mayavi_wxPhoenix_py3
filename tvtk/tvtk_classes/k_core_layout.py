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

from tvtk.tvtk_classes.graph_algorithm import GraphAlgorithm


class KCoreLayout(GraphAlgorithm):
    """
    KCoreLayout - Produces a layout for a graph labeled with K-Core
                           information.
    
    Superclass: GraphAlgorithm
    
    KCoreLayout creates coordinates for each vertex that can be used
    to perform a layout for a k-core view. Prerequisite:  Vertices must
    have an attribute array containing their
                   k-core number.  This layout is based on the algorithm
                   described in the paper: "k-core decomposition: a tool
                   for the visualization of large scale networks", by
                   Ignacio Alvarez-Hamelin et. al.
    
    
                   This graph algorithm appends either polar coordinates
    or cartesian coordinates
                   as vertex attributes to the graph giving the position
    of the vertex in a layout.
                   Input graphs must have the k-core number assigned to
    each vertex (default
                   attribute array storing kcore numbers is "kcore").
    
    
                   Epsilon - this factor is used to adjust the amount
    vertices are 'pulled' out of
                             their default ring radius based on the
    number of neighbors in higher
                             cores.  Default=0.2
                   unit_radius - Tweaks the base unit radius value. 
    Default=1.0
    
    
                   Still TODO: Still need to work on the
    connected-components within each shell and
                               associated layout issues with that.
    
    Input port 0: graph
    
    @par Thanks: Thanks to William mc_lendon from Sandia National
    Laboratories for providing this implementation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkKCoreLayout, obj, update, **traits)
    
    cartesian = tvtk_base.true_bool_trait(help=\
        """
        Set whether or not to convert output to cartesian coordinates. 
        If false, coordinates will be returned in polar coordinates
        (radius, angle). Default: True
        """
    )

    def _cartesian_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCartesian,
                        self.cartesian_)

    polar = tvtk_base.false_bool_trait(help=\
        """
        Output polar coordinates for vertices if True.  Default column
        names are coord_radius, coord_angle. Default: False
        """
    )

    def _polar_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolar,
                        self.polar_)

    cartesian_coords_x_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Cartesian coordinates array name for the X coordinates. This is
        only used if output_cartesian_coordinates is True. Default: coord_x
        """
    )

    def _cartesian_coords_x_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCartesianCoordsXArrayName,
                        self.cartesian_coords_x_array_name)

    cartesian_coords_y_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Cartesian coordinates array name for the Y coordinates. This is
        only used if output_cartesian_coordinates is True. Default: coord_y
        """
    )

    def _cartesian_coords_y_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCartesianCoordsYArrayName,
                        self.cartesian_coords_y_array_name)

    epsilon = traits.Float(0.20000000298023224, enter_set=True, auto_set=False, help=\
        """
        Epsilon value used in the algorithm. Default = 0.2
        """
    )

    def _epsilon_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEpsilon,
                        self.epsilon)

    polar_coords_angle_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Polar coordinates array name for angle values in radians. This is
        only used if output_cartesian_coordinates is False. Default:
        coord_angle
        """
    )

    def _polar_coords_angle_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarCoordsAngleArrayName,
                        self.polar_coords_angle_array_name)

    polar_coords_radius_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Polar coordinates array name for radius values. This is only used
        if output_cartesian_coordinates is False. Default: coord_radius
        """
    )

    def _polar_coords_radius_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarCoordsRadiusArrayName,
                        self.polar_coords_radius_array_name)

    unit_radius = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Unit Radius value used in the algorithm. Default = 1.0
        """
    )

    def _unit_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUnitRadius,
                        self.unit_radius)

    def fill_input_port_information(self, *args):
        """
        V.fill_input_port_information(int, Information) -> int
        C++: int FillInputPortInformation(int port, Information *info)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillInputPortInformation, *my_args)
        return ret

    def set_graph_connection(self, *args):
        """
        V.set_graph_connection(AlgorithmOutput)
        C++: void SetGraphConnection(AlgorithmOutput *)
        Convenience function provided for setting the graph input.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGraphConnection, *my_args)
        return ret

    def set_k_core_label_array_name(self, *args):
        """
        V.set_k_core_label_array_name(string)
        C++: void SetKCoreLabelArrayName(char *)
        Set the name of the vertex attribute array storing k-core labels.
        Default: kcore
        """
        ret = self._wrap_call(self._vtk_obj.SetKCoreLabelArrayName, *args)
        return ret

    _updateable_traits_ = \
    (('cartesian', 'GetCartesian'), ('polar', 'GetPolar'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('cartesian_coords_x_array_name', 'GetCartesianCoordsXArrayName'),
    ('cartesian_coords_y_array_name', 'GetCartesianCoordsYArrayName'),
    ('epsilon', 'GetEpsilon'), ('polar_coords_angle_array_name',
    'GetPolarCoordsAngleArrayName'), ('polar_coords_radius_array_name',
    'GetPolarCoordsRadiusArrayName'), ('unit_radius', 'GetUnitRadius'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'cartesian', 'debug', 'global_warning_display',
    'polar', 'release_data_flag', 'cartesian_coords_x_array_name',
    'cartesian_coords_y_array_name', 'epsilon',
    'polar_coords_angle_array_name', 'polar_coords_radius_array_name',
    'progress_text', 'unit_radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(KCoreLayout, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit KCoreLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['cartesian', 'polar'], [], ['cartesian_coords_x_array_name',
            'cartesian_coords_y_array_name', 'epsilon',
            'polar_coords_angle_array_name', 'polar_coords_radius_array_name',
            'unit_radius']),
            title='Edit KCoreLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit KCoreLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


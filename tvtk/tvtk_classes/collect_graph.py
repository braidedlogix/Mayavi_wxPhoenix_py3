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


class CollectGraph(GraphAlgorithm):
    """
    CollectGraph - Collect distributed graph.
    
    Superclass: GraphAlgorithm
    
    This filter has code to collect a graph from across processes onto
    vertex 0. Collection can be turned on or off using the "_pass_through"
    flag.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCollectGraph, obj, update, **traits)
    
    pass_through = tvtk_base.false_bool_trait(help=\
        """
        To collect or just copy input to output. Off (collect) by
        default.
        """
    )

    def _pass_through_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassThrough,
                        self.pass_through_)

    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        By defualt this filter uses the global controller, but this
        method can be used to set another instead.
        """
    )

    output_type = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Directedness flag, used to signal whether the output graph is
        directed or undirected. DIRECTED_OUTPUT expects that this filter
        is generating a directed graph. UNDIRECTED_OUTPUT expects that
        this filter is generating an undirected graph. DIRECTED_OUTPUT
        and UNDIRECTED_OUTPUT flags should only be set on the client
        filter.  Server filters should be set to USE_INPUT_TYPE since
        they have valid input and the directedness is determined from the
        input type.
        """
    )

    def _output_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputType,
                        self.output_type)

    def _get_socket_controller(self):
        return wrap_vtk(self._vtk_obj.GetSocketController())
    def _set_socket_controller(self, arg):
        old_val = self._get_socket_controller()
        self._wrap_call(self._vtk_obj.SetSocketController,
                        deref_vtk(arg))
        self.trait_property_changed('socket_controller', old_val, arg)
    socket_controller = traits.Property(_get_socket_controller, _set_socket_controller, help=\
        """
        When this filter is being used in client-server mode, this is the
        controller used to communicate between client and server.  Client
        should not set the other controller.
        """
    )

    _updateable_traits_ = \
    (('pass_through', 'GetPassThrough'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('output_type', 'GetOutputType'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'pass_through',
    'release_data_flag', 'output_type', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CollectGraph, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CollectGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['pass_through'], [], ['output_type']),
            title='Edit CollectGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CollectGraph properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


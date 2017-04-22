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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class CollectPolyData(PolyDataAlgorithm):
    """
    CollectPolyData - Collect distributed polydata.
    
    Superclass: PolyDataAlgorithm
    
    This filter has code to collect polydat from across processes onto
    node 0. Collection can be turned on or off using the "_pass_through"
    flag.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCollectPolyData, obj, update, **traits)
    
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

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('pass_through', 'GetPassThrough'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'pass_through',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CollectPolyData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CollectPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['pass_through'], [], []),
            title='Edit CollectPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CollectPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


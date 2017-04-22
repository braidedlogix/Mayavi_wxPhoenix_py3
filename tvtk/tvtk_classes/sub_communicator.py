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

from tvtk.tvtk_classes.communicator import Communicator


class SubCommunicator(Communicator):
    """
    SubCommunicator - Provides communication on a process group.
    
    Superclass: Communicator
    
    This class provides an implementation for communicating on process
    groups. In general, you should never use this class directly. 
    Instead, use the MultiProcessController::CreateSubController
    method.
    
    @bug Because all communication is delegated to the original
    communicator, any error will report process ids with respect to the
    original communicator, not this communicator that was actually used.
    
    @sa
    Communicator, MultiProcessController
    
    @par Thanks: This class was originally written by Kenneth Moreland
    (kmorel@sandia.gov) from Sandia National Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSubCommunicator, obj, update, **traits)
    
    def _get_group(self):
        return wrap_vtk(self._vtk_obj.GetGroup())
    def _set_group(self, arg):
        old_val = self._get_group()
        self._wrap_call(self._vtk_obj.SetGroup,
                        deref_vtk(arg))
        self.trait_property_changed('group', old_val, arg)
    group = traits.Property(_get_group, _set_group, help=\
        """
        Set/get the group on which communication will happen.
        """
    )

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_processes',
    'GetNumberOfProcesses'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'number_of_processes'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SubCommunicator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SubCommunicator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['number_of_processes']),
            title='Edit SubCommunicator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SubCommunicator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


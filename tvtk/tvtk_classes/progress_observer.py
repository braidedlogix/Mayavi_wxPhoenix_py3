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


class ProgressObserver(Object):
    """
    ProgressObserver - Basic class to optionally replace Algorithm
    progress functionality.
    
    Superclass: Object
    
    When the basic functionality in Algorithm that reports progress is
    not enough, a subclass of ProgressObserver can be used to provide
    custom functionality. The main use case for this is when an
    algorithm's request_data() is called from multiple threads in parallel
    - the basic functionality in Algorithm is not thread safe.
    SMPProgressObserver can handle this situation by routing progress
    from each thread to a thread local ProgressObserver, which will
    invoke events separately for each thread.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProgressObserver, obj, update, **traits)
    
    def _get_progress(self):
        return self._vtk_obj.GetProgress()
    progress = traits.Property(_get_progress, help=\
        """
        Returns the progress reported by the algorithm.
        """
    )

    def update_progress(self, *args):
        """
        V.update_progress(float)
        C++: virtual void UpdateProgress(double amount)
        The default behavior is to update the Progress data member and
        invoke a progress_event. This is designed to be overwritten.
        """
        ret = self._wrap_call(self._vtk_obj.UpdateProgress, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProgressObserver, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ProgressObserver properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ProgressObserver properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProgressObserver properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.algorithm import Algorithm


class TemporalDataSetCache(Algorithm):
    """
    TemporalDataSetCache - cache time steps
    
    Superclass: Algorithm
    
    TemporalDataSetCache cache time step requests of a temporal
    dataset, when cached data is requested it is returned using a shallow
    copy.@par Thanks: Ken Martin (Kitware) and John Bidiscombe of CSCS -
    Swiss National Supercomputing Centre for creating and contributing
    this class. For related material, please refer to : John Biddiscombe,
    Berk Geveci, Ken Martin, Kenneth Moreland, David Thompson, "Time Dependent Processing in a Parallel Pipeline
    Architecture", IEEE Visualization 2007.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTemporalDataSetCache, obj, update, **traits)
    
    cache_size = traits.Int(10, enter_set=True, auto_set=False, help=\
        """
        This is the maximum number of time steps that can be retained in
        memory. it defaults to 10.
        """
    )

    def _cache_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCacheSize,
                        self.cache_size)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('cache_size',
    'GetCacheSize'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'cache_size', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TemporalDataSetCache, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TemporalDataSetCache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['cache_size']),
            title='Edit TemporalDataSetCache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TemporalDataSetCache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


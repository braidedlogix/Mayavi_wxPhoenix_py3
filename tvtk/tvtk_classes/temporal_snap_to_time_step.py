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


class TemporalSnapToTimeStep(Algorithm):
    """
    TemporalSnapToTimeStep - modify the time range/steps of temporal
    data
    
    Superclass: Algorithm
    
    TemporalSnapToTimeStep  modify the time range or time steps of the
    data without changing the data itself. The data is not resampled by
    this filter, only the information accompanying the data is modified.
    
    @par Thanks: John Bidiscombe of CSCS - Swiss National Supercomputing
    Centre for creating and contributing this class. For related
    material, please refer to : John Biddiscombe, Berk Geveci, Ken
    Martin, Kenneth Moreland, David Thompson, "Time Dependent Processing in a Parallel Pipeline
    Architecture", IEEE Visualization 2007.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTemporalSnapToTimeStep, obj, update, **traits)
    
    snap_mode = traits.Trait('nearest',
    tvtk_base.TraitRevPrefixMap({'nearest': 0, 'next_above_or_equal': 2, 'next_below_or_equal': 1}), help=\
        """
        
        """
    )

    def _snap_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSnapMode,
                        self.snap_mode_)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('snap_mode',
    'GetSnapMode'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'snap_mode', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TemporalSnapToTimeStep, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TemporalSnapToTimeStep properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['snap_mode'], []),
            title='Edit TemporalSnapToTimeStep properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TemporalSnapToTimeStep properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


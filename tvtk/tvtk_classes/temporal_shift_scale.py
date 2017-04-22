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


class TemporalShiftScale(Algorithm):
    """
    TemporalShiftScale - modify the time range/steps of temporal data
    
    Superclass: Algorithm
    
    TemporalShiftScale  modify the time range or time steps of the
    data without changing the data itself. The data is not resampled by
    this filter, only the information accompanying the data is modified.
    
    @par Thanks: Ken Martin (Kitware) and John Bidiscombe of CSCS - Swiss
    National Supercomputing Centre for creating and contributing this
    class. For related material, please refer to : John Biddiscombe, Berk
    Geveci, Ken Martin, Kenneth Moreland, David Thompson, "Time Dependent Processing in a Parallel Pipeline
    Architecture", IEEE Visualization 2007.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTemporalShiftScale, obj, update, **traits)
    
    periodic_end_correction = tvtk_base.true_bool_trait(help=\
        """
        if Periodic time is enabled, this flag determines if the last
        time step is the same as the first. If periodic_end_correction is
        true, then it is assumed that the input data goes from 0-1 (or
        whatever scaled/shifted actual time) and time 1 is the same as
        time 0 so that steps will be 0,1,2,3...N,1,2,3...N,1,2,3 where
        step N is the same as 0 and step 0 is not repeated. When this
        flag is false the data is assumed to be literal and output is of
        the form 0,1,2,3...N,0,1,2,3... By default this flag is ON
        """
    )

    def _periodic_end_correction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPeriodicEndCorrection,
                        self.periodic_end_correction_)

    periodic = tvtk_base.false_bool_trait(help=\
        """
        If Periodic is true, requests for time will be wrapped around so
        that the source appears to be a periodic time source. If data
        exists for times {0,N-1}, setting periodic to true will cause
        time 0 to be produced when time N, 2n, 2n etc is requested. This
        effectively gives the source the ability to generate time data
        indefinitely in a loop. When combined with Shift/Scale, the time
        becomes periodic in the shifted and scaled time frame of
        reference. Note: Since the input time may not start at zero, the
        wrapping of time from the end of one period to the start of the
        next, will subtract the initial time - a source with T{5..6}
        repeated periodicaly will have output time {5..6..7..8} etc.
        """
    )

    def _periodic_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPeriodic,
                        self.periodic_)

    maximum_number_of_periods = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        if Periodic time is enabled, this controls how many time periods
        time is reported for. A filter cannot output an infinite number
        of time steps and therefore a finite number of periods is
        generated when reporting time.
        """
    )

    def _maximum_number_of_periods_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfPeriods,
                        self.maximum_number_of_periods)

    post_shift = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Apply a translation to the time
        """
    )

    def _post_shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPostShift,
                        self.post_shift)

    pre_shift = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Apply a translation to the data before scaling. To convert
        T{5,100} to T{0,1} use Preshift=-5, Scale=1/95, post_shift=_0 To
        convert T{5,105} to T{5,10} use Preshift=-5, Scale=5/100,
        post_shift=_5
        """
    )

    def _pre_shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreShift,
                        self.pre_shift)

    scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Apply a scale to the time.
        """
    )

    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale)

    _updateable_traits_ = \
    (('periodic_end_correction', 'GetPeriodicEndCorrection'), ('periodic',
    'GetPeriodic'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_number_of_periods', 'GetMaximumNumberOfPeriods'),
    ('post_shift', 'GetPostShift'), ('pre_shift', 'GetPreShift'),
    ('scale', 'GetScale'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'periodic',
    'periodic_end_correction', 'release_data_flag',
    'maximum_number_of_periods', 'post_shift', 'pre_shift',
    'progress_text', 'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TemporalShiftScale, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TemporalShiftScale properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['periodic', 'periodic_end_correction'], [],
            ['maximum_number_of_periods', 'post_shift', 'pre_shift', 'scale']),
            title='Edit TemporalShiftScale properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TemporalShiftScale properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


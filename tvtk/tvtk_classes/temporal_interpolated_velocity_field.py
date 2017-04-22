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

from tvtk.tvtk_classes.function_set import FunctionSet


class TemporalInterpolatedVelocityField(FunctionSet):
    """
    TemporalInterpolatedVelocityField - A helper class for
    interpolating between times during particle tracing
    
    Superclass: FunctionSet
    
    TemporalInterpolatedVelocityField is a general purpose helper for
    the temporal particle tracing code (vtk_temporal_stream_tracer)
    
    It maintains two copies of CachingInterpolatedVelocityField
    internally and uses them to obtain velocity values at time T0 and T1.
    
    In fact the class does quite a bit more than this because when the
    geometry of the datasets is the same at T0 and T1, we can re-use
    cached cell Ids and weights used in the cell interpolation routines.
    Additionally, the same weights can be used when interpolating (point)
    scalar values and computing vorticity etc.
    
    @warning
    TemporalInterpolatedVelocityField is probably not thread safe. A
    new instance should be created by each thread.
    
    @warning
    Datasets are added in lists. The list for T1 must be idential to that
    for T0 in structure/topology and dataset order, and any datasets
    marked as static, must remain so for all T - changing a dataset from
    static to dynamic between time steps will result in undefined
    behaviour (=crash probably)
    
    @sa
    CachingInterpolatedVelocityField TemporalStreamTracer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTemporalInterpolatedVelocityField, obj, update, **traits)
    
    def get_cached_cell_ids(self, *args):
        """
        V.get_cached_cell_ids([int, int], [int, int]) -> bool
        C++: bool GetCachedCellIds(IdType id[2], int ds[2])
        Between iterations of the Particle Tracer, Id's of the Cell are
        stored and then at the start of the next particle the Ids are set
        to 'pre-fill' the cache.
        """
        ret = self._wrap_call(self._vtk_obj.GetCachedCellIds, *args)
        return ret

    def set_cached_cell_ids(self, *args):
        """
        V.set_cached_cell_ids([int, int], [int, int])
        C++: void SetCachedCellIds(IdType id[2], int ds[2])
        Between iterations of the Particle Tracer, Id's of the Cell are
        stored and then at the start of the next particle the Ids are set
        to 'pre-fill' the cache.
        """
        ret = self._wrap_call(self._vtk_obj.SetCachedCellIds, *args)
        return ret

    def _get_current_weight(self):
        return self._vtk_obj.GetCurrentWeight()
    current_weight = traits.Property(_get_current_weight, help=\
        """
        Get the most recent weight between 0->1 from T1->T2. Initial
        value is 0.
        """
    )

    def _get_last_good_velocity(self):
        return self._vtk_obj.GetLastGoodVelocity()
    last_good_velocity = traits.Property(_get_last_good_velocity, help=\
        """
        
        """
    )

    def advance_one_time_step(self):
        """
        V.advance_one_time_step()
        C++: void AdvanceOneTimeStep()"""
        ret = self._vtk_obj.AdvanceOneTimeStep()
        return ret
        

    def clear_cache(self):
        """
        V.clear_cache()
        C++: void ClearCache()
        Set the last cell id to -1 so that the next search does not start
        from the previous cell
        """
        ret = self._vtk_obj.ClearCache()
        return ret
        

    def function_values_at_t(self, *args):
        """
        V.function_values_at_t(int, [float, ...], [float, ...]) -> int
        C++: int FunctionValuesAtT(int T, double *x, double *u)
        Evaluate the velocity field, f, at (x, y, z, t). For now, t is
        ignored.
        """
        ret = self._wrap_call(self._vtk_obj.FunctionValuesAtT, *args)
        return ret

    def interpolate_point(self, *args):
        """
        V.interpolate_point(PointData, PointData, int) -> bool
        C++: bool InterpolatePoint(PointData *outPD1,
            PointData *outPD2, IdType outIndex)
        V.interpolate_point(int, PointData, int) -> bool
        C++: bool InterpolatePoint(int T, PointData *outPD1,
            IdType outIndex)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InterpolatePoint, *my_args)
        return ret

    def is_static(self, *args):
        """
        V.is_static(int) -> bool
        C++: bool IsStatic(int datasetIndex)"""
        ret = self._wrap_call(self._vtk_obj.IsStatic, *args)
        return ret

    def quick_test_point(self, *args):
        """
        V.quick_test_point([float, ...]) -> int
        C++: int QuickTestPoint(double *x)
        A utility function which evaluates the point at T1, T2 to see if
        it is inside the data at both times or only one.
        """
        ret = self._wrap_call(self._vtk_obj.QuickTestPoint, *args)
        return ret

    def select_vectors(self, *args):
        """
        V.select_vectors(string)
        C++: void SelectVectors(const char *fieldName)
        If you want to work with an arbitrary vector array, then set its
        name here. By default this is NULL and the filter will use the
        active vector array.
        """
        ret = self._wrap_call(self._vtk_obj.SelectVectors, *args)
        return ret

    def set_data_set_at_time(self, *args):
        """
        V.set_data_set_at_time(int, int, float, DataSet, bool)
        C++: void SetDataSetAtTime(int I, int N, double T,
            DataSet *dataset, bool staticdataset)
        In order to use this class, two sets of data must be supplied,
        corresponding to times T1 and T2. Data is added via this
        function.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDataSetAtTime, *my_args)
        return ret

    def show_cache_results(self):
        """
        V.show_cache_results()
        C++: void ShowCacheResults()"""
        ret = self._vtk_obj.ShowCacheResults()
        return ret
        

    def test_point(self, *args):
        """
        V.test_point([float, ...]) -> int
        C++: int TestPoint(double *x)
        A utility function which evaluates the point at T1, T2 to see if
        it is inside the data at both times or only one.
        """
        ret = self._wrap_call(self._vtk_obj.TestPoint, *args)
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
            return super(TemporalInterpolatedVelocityField, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TemporalInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit TemporalInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TemporalInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


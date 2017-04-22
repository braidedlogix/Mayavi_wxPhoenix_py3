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


class CachingInterpolatedVelocityField(FunctionSet):
    """
    CachingInterpolatedVelocityField - Interface for obtaining
    interpolated velocity values
    
    Superclass: FunctionSet
    
    CachingInterpolatedVelocityField acts as a continuous velocity
    field by performing cell interpolation on the underlying DataSet.
    This is a concrete sub-class of FunctionSet with
    number_of_independent_variables = 4 (x,y,z,t) and number_of_functions = 3
    (u,v,w). Normally, every time an evaluation is performed, the cell
    which contains the point (x,y,z) has to be found by calling find_cell.
    This is a computationally expensive operation. In certain cases, the
    cell search can be avoided or shortened by providing a guess for the
    cell id. For example, in streamline integration, the next evaluation
    is usually in the same or a neighbour cell. For this reason,
    CachingInterpolatedVelocityField stores the last cell id. If
    caching is turned on, it uses this id as the starting point.
    
    @warning
    CachingInterpolatedVelocityField is not thread safe. A new
    instance should be created by each thread.
    
    @sa
    FunctionSet StreamTracer
    
    @todo Need to clean up style to match vtk/Kitware standards. Please
    help.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCachingInterpolatedVelocityField, obj, update, **traits)
    
    def _get_cache_miss(self):
        return self._vtk_obj.GetCacheMiss()
    cache_miss = traits.Property(_get_cache_miss, help=\
        """
        Caching statistics.
        """
    )

    def _get_cell_cache_hit(self):
        return self._vtk_obj.GetCellCacheHit()
    cell_cache_hit = traits.Property(_get_cell_cache_hit, help=\
        """
        Caching statistics.
        """
    )

    def _get_data_set_cache_hit(self):
        return self._vtk_obj.GetDataSetCacheHit()
    data_set_cache_hit = traits.Property(_get_data_set_cache_hit, help=\
        """
        Caching statistics.
        """
    )

    def get_last_local_coordinates(self, *args):
        """
        V.get_last_local_coordinates([float, float, float]) -> int
        C++: int GetLastLocalCoordinates(double pcoords[3])
        Returns the interpolation weights/pcoords cached from last
        evaluation if the cached cell is valid (returns 1). Otherwise, it
        does not change w and returns 0.
        """
        ret = self._wrap_call(self._vtk_obj.GetLastLocalCoordinates, *args)
        return ret

    def get_last_weights(self, *args):
        """
        V.get_last_weights([float, ...]) -> int
        C++: int GetLastWeights(double *w)
        Returns the interpolation weights/pcoords cached from last
        evaluation if the cached cell is valid (returns 1). Otherwise, it
        does not change w and returns 0.
        """
        ret = self._wrap_call(self._vtk_obj.GetLastWeights, *args)
        return ret

    def _get_vectors_selection(self):
        return self._vtk_obj.GetVectorsSelection()
    vectors_selection = traits.Property(_get_vectors_selection, help=\
        """
        If you want to work with an arbitrary vector array, then set its
        name here. By default this in NULL and the filter will use the
        active vector array.
        """
    )

    def clear_last_cell_info(self):
        """
        V.clear_last_cell_info()
        C++: void ClearLastCellInfo()
        Set last_cell_id to -1 and Cache to NULL so that the next search
        does not  start from the previous cell.
        """
        ret = self._vtk_obj.ClearLastCellInfo()
        return ret
        

    def inside_test(self, *args):
        """
        V.inside_test([float, ...]) -> int
        C++: virtual int InsideTest(double *x)
        Evaluate the velocity field, f={u,v,w}, at {x, y, z}. returns 1
        if valid, 0 if test failed
        """
        ret = self._wrap_call(self._vtk_obj.InsideTest, *args)
        return ret

    def select_vectors(self, *args):
        """
        V.select_vectors(string)
        C++: void SelectVectors(const char *fieldName)
        If you want to work with an arbitrary vector array, then set its
        name here. By default this in NULL and the filter will use the
        active vector array.
        """
        ret = self._wrap_call(self._vtk_obj.SelectVectors, *args)
        return ret

    def set_data_set(self, *args):
        """
        V.set_data_set(int, DataSet, bool, AbstractCellLocator)
        C++: virtual void SetDataSet(int I, DataSet *dataset,
            bool staticdataset, AbstractCellLocator *locator)
        Add a dataset used by the interpolation function evaluation.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDataSet, *my_args)
        return ret

    def set_last_cell_info(self, *args):
        """
        V.set_last_cell_info(int, int)
        C++: void SetLastCellInfo(IdType c, int datasetindex)
        Set last_cell_id to c and last_cache_index datasetindex, cached from
        last evaluation. If c isn't -1 then the corresponding cell is
        stored in Cache->Cell. These values should be valid or an
        assertion will be triggered.
        """
        ret = self._wrap_call(self._vtk_obj.SetLastCellInfo, *args)
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
            return super(CachingInterpolatedVelocityField, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CachingInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit CachingInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CachingInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


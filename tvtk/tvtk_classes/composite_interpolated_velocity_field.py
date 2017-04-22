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

from tvtk.tvtk_classes.abstract_interpolated_velocity_field import AbstractInterpolatedVelocityField


class CompositeInterpolatedVelocityField(AbstractInterpolatedVelocityField):
    """
    CompositeInterpolatedVelocityField - An abstract class for
     obtaining the interpolated velocity values at a point
    
    Superclass: AbstractInterpolatedVelocityField
    
    CompositeInterpolatedVelocityField acts as a continuous velocity
    field
     by performing cell interpolation on the underlying DataSet. This
    is an
     abstract sub-class of FunctionSet, number_of_independent_variables =
    4
     (x,y,z,t) and number_of_functions = 3 (u,v,w). With a brute-force
    scheme,
     every time an evaluation is performed, the target cell containing
    point
     (x,y,z) needs to be found by calling find_cell(), via either
    DataSet or
     AbstractCelllocator's sub-classes (vtk_cell_locator &
    ModifiedBSPTree).
     As it incurs a large cost, one (for
    CellLocatorInterpolatedVelocityField
     via AbstractCellLocator) or two (for InterpolatedVelocityField
    via
     DataSet that involves PointLocator in addressing PointSet)
    levels
     of cell caching may be exploited to increase the performance.
    
    
     For InterpolatedVelocityField, level #0 begins with intra-cell
    caching.
     Specifically if the previous cell is valid and the next point is
    still in
     it ( i.e., Cell::EvaluatePosition() returns 1, coupled with newly
    created
     parametric coordinates & weights ), the function values can be
    interpolated
     and only Cell::EvaluatePosition() is invoked. If this fails, then
    level #1
     follows by inter-cell search for the target cell that contains the
    next point.
     By an inter-cell search, the previous cell provides an important
    clue or serves
     as an immediate neighbor to aid in locating the target cell via
    PointSet::
     find_cell(). If this still fails, a global cell location / search is
    invoked via
     PointSet::FindCell(). Here regardless of either inter-cell or
    global search,
     PointLocator is in fact employed (for datasets of type
    PointSet only, note
     ImageData and RectilinearGrid are able to provide rapid and
    robust cell
     location due to the simple mesh topology) as a crucial tool
    underlying the cell
     locator. However, the use of PointLocator makes
    InterpolatedVelocityField
     non-robust in cell location for PointSet.
    
    
     For CellLocatorInterpolatedVelocityField, the only caching (level
    #0) works
     by intra-cell trial. In case of failure, a global search for the
    target cell is
     invoked via AbstractCellLocator::FindCell() and the actual work
    is done by
     either CellLocator or ModifiedBSPTree (for datasets of type
    PointSet
     only, while ImageData and RectilinearGrid themselves are able
    to provide
     fast robust cell location). Without the involvement of
    PointLocator, robust
     cell location is achieved for PointSet.
    
    @warning
     CompositeInterpolatedVelocityField is not thread safe. A new
    instance
     should be created by each thread.
    
    @sa
     InterpolatedVelocityField CellLocatorInterpolatedVelocityField
     GenericInterpolatedVelocityField
    CachingInterpolatedVelocityField
     TemporalInterpolatedVelocityField FunctionSet StreamTracer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCompositeInterpolatedVelocityField, obj, update, **traits)
    
    def _get_last_data_set_index(self):
        return self._vtk_obj.GetLastDataSetIndex()
    last_data_set_index = traits.Property(_get_last_data_set_index, help=\
        """
        Get the most recently visited dataset and it id. The dataset is
        used for a guess regarding where the next point will be, without
        searching through all datasets. When setting the last dataset,
        care is needed as no reference counting or checks are performed.
        This feature is intended for custom interpolators only that cache
        datasets independently.
        """
    )

    def add_data_set(self, *args):
        """
        V.add_data_set(DataSet)
        C++: virtual void AddDataSet(DataSet *dataset)
        Add a dataset for implicit velocity function evaluation. If more
        than one dataset is added, the evaluation point is searched in
        all until a match is found. THIS FUNCTION DOES NOT CHANGE THE
        REFERENCE COUNT OF dataset FOR THREAD SAFETY REASONS.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddDataSet, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('caching', 'GetCaching'),
    ('force_surface_tangent_vector', 'GetForceSurfaceTangentVector'),
    ('last_cell_id', 'GetLastCellId'), ('normalize_vector',
    'GetNormalizeVector'), ('surface_dataset', 'GetSurfaceDataset'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'caching',
    'force_surface_tangent_vector', 'last_cell_id', 'normalize_vector',
    'surface_dataset'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CompositeInterpolatedVelocityField, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CompositeInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['caching', 'force_surface_tangent_vector',
            'last_cell_id', 'normalize_vector', 'surface_dataset']),
            title='Edit CompositeInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CompositeInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


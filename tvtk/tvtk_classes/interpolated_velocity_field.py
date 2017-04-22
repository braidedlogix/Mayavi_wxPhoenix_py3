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

from tvtk.tvtk_classes.composite_interpolated_velocity_field import CompositeInterpolatedVelocityField


class InterpolatedVelocityField(CompositeInterpolatedVelocityField):
    """
    InterpolatedVelocityField - A concrete class for obtaining
     the interpolated velocity values at a point.
    
    Superclass: CompositeInterpolatedVelocityField
    
    InterpolatedVelocityField acts as a continuous velocity field via
     cell interpolation on a DataSet, number_of_independent_variables = 4
     (x,y,z,t) and number_of_functions = 3 (u,v,w). As a concrete sub-class
     of CompositeInterpolatedVelocityField, this class adopts two
    levels
     of cell caching for faster though less robust cell location than its
     sibling class CellLocatorInterpolatedVelocityField. Level #0
    begins
     with intra-cell caching. Specifically, if the previous cell is valid
     and the nex point is still within it, ( Cell::EvaluatePosition()
     returns 1, coupled with the new parametric coordinates and weights
    ),
     the function values are interpolated and Cell::EvaluatePosition()
     is invoked only. If it fails, level #1 follows by inter-cell
    location
     of the target cell (that contains the next point). By inter-cell,
    the
     previous cell gives an important clue / guess or serves as an
    immediate
     neighbor to aid in the location of the target cell (as is typically
    the
     case with integrating a streamline across cells) by means of
    DataSet::
     find_cell(). If this still fails, a global cell search is invoked via
     DataSet::FindCell().
    
    
     Regardless of inter-cell or global search, PointLocator is
    employed
     as a crucial tool underlying the cell locator. The use of
    PointLocator
     casues InterpolatedVelocityField to return false target cells for
     datasets defined on complex grids.
    
    @warning
     InterpolatedVelocityField is not thread safe. A new instance
    should be
     created by each thread.
    
    @sa
     CompositeInterpolatedVelocityField
    CellLocatorInterpolatedVelocityField
     GenericInterpolatedVelocityField
    CachingInterpolatedVelocityField
     TemporalInterpolatedVelocityField FunctionSet StreamTracer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInterpolatedVelocityField, obj, update, **traits)
    
    last_cell_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the cell id cached by the last evaluation within a specified
        dataset.
        """
    )

    def _last_cell_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLastCellId,
                        self.last_cell_id)

    def snap_point_on_cell(self, *args):
        """
        V.snap_point_on_cell([float, ...], [float, ...]) -> int
        C++: virtual int SnapPointOnCell(double *pOrigin, double *pProj)
        Project the provided point on current cell, current dataset.
        """
        ret = self._wrap_call(self._vtk_obj.SnapPointOnCell, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('last_cell_id', 'GetLastCellId'),
    ('caching', 'GetCaching'), ('force_surface_tangent_vector',
    'GetForceSurfaceTangentVector'), ('normalize_vector',
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
            return super(InterpolatedVelocityField, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['caching', 'force_surface_tangent_vector',
            'last_cell_id', 'normalize_vector', 'surface_dataset']),
            title='Edit InterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


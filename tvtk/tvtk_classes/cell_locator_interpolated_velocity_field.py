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


class CellLocatorInterpolatedVelocityField(CompositeInterpolatedVelocityField):
    """
    CellLocatorInterpolatedVelocityField - A concrete class for
     obtaining the interpolated velocity values at a point.
    
    Superclass: CompositeInterpolatedVelocityField
    
    CellLocatorInterpolatedVelocityField acts as a continuous velocity
     field via cell interpolation on a DataSet,
    number_of_independent_variables
     = 4 (x,y,z,t) and number_of_functions = 3 (u,v,w). As a concrete
    sub-class
     of CompositeInterpolatedVelocityField, it adopts
    AbstractCellLocator's
     sub-classes, e.g., CellLocator and ModifiedBSPTree, without
    the use
     of PointLocator ( employed by DataSet/vtkPointSet::FindCell()
    in
     InterpolatedVelocityField ).
    CellLocatorInterpolatedVelocityField
     adopts one level of cell caching. Specifically, if the next point is
    still
     within the previous cell, cell location is then simply skipped and
    Cell::
     evaluate_position() is called to obtain the new parametric
    coordinates and
     weights that are used to interpolate the velocity function values
    across the
     vertices of this cell. Otherwise a global cell (the target
    containing the next
     point) location is instead directly invoked, without exploiting the
    clue that
     InterpolatedVelocityField makes use of from the previous cell (an
    immediate
     neighbor). Although ignoring the neighbor cell may incur a
    relatively high
     computational cost, CellLocatorInterpolatedVelocityField is more
    robust in
     locating the target cell than its sibling class
    InterpolatedVelocityField.
    
    @warning
     CellLocatorInterpolatedVelocityField is not thread safe. A new
    instance
     should be created by each thread.
    
    @sa
     CompositeInterpolatedVelocityField InterpolatedVelocityField
     GenericInterpolatedVelocityField
    CachingInterpolatedVelocityField
     TemporalInterpolatedVelocityField FunctionSet StreamTracer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellLocatorInterpolatedVelocityField, obj, update, **traits)
    
    def _get_cell_locator_prototype(self):
        return wrap_vtk(self._vtk_obj.GetCellLocatorPrototype())
    def _set_cell_locator_prototype(self, arg):
        old_val = self._get_cell_locator_prototype()
        self._wrap_call(self._vtk_obj.SetCellLocatorPrototype,
                        deref_vtk(arg))
        self.trait_property_changed('cell_locator_prototype', old_val, arg)
    cell_locator_prototype = traits.Property(_get_cell_locator_prototype, _set_cell_locator_prototype, help=\
        """
        Get the prototype of the cell locator that is used for
        interpolating the velocity field during integration.
        """
    )

    last_cell_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the cell id cached by the last evaluation within a specified
        dataset.
        """
    )

    def _last_cell_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLastCellId,
                        self.last_cell_id)

    def _get_last_cell_locator(self):
        return wrap_vtk(self._vtk_obj.GetLastCellLocator())
    last_cell_locator = traits.Property(_get_last_cell_locator, help=\
        """
        Get the cell locator attached to the most recently visited
        dataset.
        """
    )

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
            return super(CellLocatorInterpolatedVelocityField, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CellLocatorInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['caching', 'force_surface_tangent_vector',
            'last_cell_id', 'normalize_vector', 'surface_dataset']),
            title='Edit CellLocatorInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellLocatorInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


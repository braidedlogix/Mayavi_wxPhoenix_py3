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


class UnstructuredGridVolumeRayCastIterator(Object):
    """
    UnstructuredGridVolumeRayCastIterator -
    UnstructuredGridVolumeRayCastIterator is a superclass for
    iterating over the intersections of a viewing ray with a group of
    unstructured cells.
    
    Superclass: Object
    
    These iterators are created with a
    UnstructuredGridVolumeRayCastFunction.
    
    @sa
    UnstructuredGridVolumeRayCastFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGridVolumeRayCastIterator, obj, update, **traits)
    
    bounds = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 0.0), cols=2, help=\
        """
        
        """
    )

    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    max_number_of_intersections = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _max_number_of_intersections_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxNumberOfIntersections,
                        self.max_number_of_intersections)

    def get_next_intersections(self, *args):
        """
        V.get_next_intersections(IdList, DoubleArray, DataArray,
            DataArray, DataArray) -> int
        C++: virtual IdType GetNextIntersections(
            IdList *intersectedCells,
            DoubleArray *intersectionLengths, DataArray *scalars,
            DataArray *nearIntersections,
            DataArray *farIntersections)
        Get the intersections of the next several cells.  The cell ids
        are stored in intersected_cells and the length of each ray segment
        within the cell is stored in intersection_lengths.  The point
        scalars scalars are interpolated and stored in near_intersections
        and far_intersections.  intersected_cells, intersection_lengths, or
        scalars may be NULL to suppress passing the associated
        information.  The number of intersections actually encountered is
        returned.  0 is returned if and only if no more intersections are
        to be found.
        """
        my_args = deref_array(args, [('vtkIdList', 'vtkDoubleArray', 'vtkDataArray', 'vtkDataArray', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.GetNextIntersections, *my_args)
        return ret

    def initialize(self, *args):
        """
        V.initialize(int, int)
        C++: virtual void Initialize(int x, int y)
        Initializes the iteration to the start of the ray at the given
        screen coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.Initialize, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('bounds', 'GetBounds'),
    ('max_number_of_intersections', 'GetMaxNumberOfIntersections'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'bounds',
    'max_number_of_intersections'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UnstructuredGridVolumeRayCastIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGridVolumeRayCastIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['bounds', 'max_number_of_intersections']),
            title='Edit UnstructuredGridVolumeRayCastIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGridVolumeRayCastIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


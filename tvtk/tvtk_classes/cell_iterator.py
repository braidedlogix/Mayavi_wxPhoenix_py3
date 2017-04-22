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


class CellIterator(Object):
    """
    CellIterator - Efficient cell iterator for DataSet topologies.
    
    Superclass: Object
    
    CellIterator provides a method for traversing cells in a data set.
    Call the DataSet::NewCellIterator() method to use this class.
    
    The cell is represented as a set of three pieces of information: The
    cell type, the ids of the points constituting the cell, and the
    points themselves. This iterator fetches these as needed. If only the
    cell type is used, the type is not looked up until get_cell_type is
    called, and the point information is left uninitialized. This allows
    efficient screening of cells, since expensive point lookups may be
    skipped depending on the cell type/etc.
    
    An example usage of this class: ~~~ void my_worker_function(vtk_data_set
    *ds) {
      CellIterator *it = ds->_new_cell_iterator();
      for (it->_init_traversal(); !it->_is_done_with_traversal();
    it->_go_to_next_cell())
        {
        if (it->_get_cell_type() != VTK_TETRA)
          {
          continue; // Skip non-tetrahedral cells
          }
    
    
        IdList *point_ids = it->_get_point_ids();
        // Do screening on the point ids, maybe figure out scalar range
    and skip
           cells that do not lie in a certain range?
    
    
        Points *points = it->_get_points();
        // Do work using the cell points, or ...
    
    
        GenericCell *cell = ...;
        it->_get_cell(cell);
        // ... do work with a Cell.
        }
      it->Delete(); } ~~~
    
    The example above pulls in bits of information as needed to filter
    out cells that aren't relevent. The least expensive lookups are
    performed first (cell type, then point ids, then points/full cell) to
    prevent wasted cycles fetching unnecessary data. Also note that at
    the end of the loop, the iterator must be deleted as these iterators
    are Object subclasses.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellIterator, obj, update, **traits)
    
    def get_cell(self, *args):
        """
        V.get_cell(GenericCell)
        C++: void GetCell(GenericCell *cell)
        Write the current full cell information into the argument. This
        is usually a very expensive call, and should be avoided when
        possible. This should only be called when is_done_with_traversal()
        returns false.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetCell, *my_args)
        return ret

    def _get_cell_dimension(self):
        return self._vtk_obj.GetCellDimension()
    cell_dimension = traits.Property(_get_cell_dimension, help=\
        """
        Get the current cell dimension (0, 1, 2, or 3). This should only
        be called when is_done_with_traversal() returns false.
        """
    )

    def _get_cell_id(self):
        return self._vtk_obj.GetCellId()
    cell_id = traits.Property(_get_cell_id, help=\
        """
        Get the id of the current cell.
        """
    )

    def _get_cell_type(self):
        return self._vtk_obj.GetCellType()
    cell_type = traits.Property(_get_cell_type, help=\
        """
        Get the current cell type (e.g. VTK_LINE, VTK_VERTEX, VTK_TETRA,
        etc). This should only be called when is_done_with_traversal()
        returns false.
        """
    )

    def _get_faces(self):
        return wrap_vtk(self._vtk_obj.GetFaces())
    faces = traits.Property(_get_faces, help=\
        """
        Get the faces for a polyhedral cell. This is only valid when
        cell_type is VTK_POLYHEDRON.
        """
    )

    def _get_number_of_faces(self):
        return self._vtk_obj.GetNumberOfFaces()
    number_of_faces = traits.Property(_get_number_of_faces, help=\
        """
        Return the number of faces in the current cell. This should only
        be called when is_done_with_traversal() returns false.
        """
    )

    def _get_number_of_points(self):
        return self._vtk_obj.GetNumberOfPoints()
    number_of_points = traits.Property(_get_number_of_points, help=\
        """
        Return the number of points in the current cell. This should only
        be called when is_done_with_traversal() returns false.
        """
    )

    def _get_point_ids(self):
        return wrap_vtk(self._vtk_obj.GetPointIds())
    point_ids = traits.Property(_get_point_ids, help=\
        """
        Get the ids of the points in the current cell. This should only
        be called when is_done_with_traversal() returns false.
        """
    )

    def _get_points(self):
        return wrap_vtk(self._vtk_obj.GetPoints())
    points = traits.Property(_get_points, help=\
        """
        Get the points in the current cell. This is usually a very
        expensive call, and should be avoided when possible. This should
        only be called when is_done_with_traversal() returns false.
        """
    )

    def go_to_next_cell(self):
        """
        V.go_to_next_cell()
        C++: void GoToNextCell()
        Increment to next cell. Always safe to call.
        """
        ret = self._vtk_obj.GoToNextCell()
        return ret
        

    def init_traversal(self):
        """
        V.init_traversal()
        C++: void InitTraversal()
        Reset to the first cell.
        """
        ret = self._vtk_obj.InitTraversal()
        return ret
        

    def is_done_with_traversal(self):
        """
        V.is_done_with_traversal() -> bool
        C++: virtual bool IsDoneWithTraversal()
        Returns false while the iterator is valid. Always safe to call.
        """
        ret = self._vtk_obj.IsDoneWithTraversal()
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
            return super(CellIterator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CellIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit CellIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellIterator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.point_set import PointSet


class StructuredGrid(PointSet):
    """
    StructuredGrid - topologically regular array of data
    
    Superclass: PointSet
    
    StructuredGrid is a data object that is a concrete implementation
    of DataSet. StructuredGrid represents a geometric structure
    that is a topologically regular array of points. The topology is that
    of a cube that has been subdivided into a regular array of smaller
    cubes. Each point/cell can be addressed with i-j-k indices. Examples
    include finite difference grids.
    
    The order and number of points must match that specified by the
    dimensions of the grid. The point order increases in i fastest (from
    0<=i<dims[0]), then j (0<=j<dims[1]), then k (0<=k<dims[2]) where
    dims[] are the dimensions of the grid in the i-j-k topological
    directions. The number of points is dims[0]*dims[1]*dims[2]. The same
    is true for the cells of the grid. The order and number of cells must
    match that specified by the dimensions of the grid. The cell order
    increases in i fastest (from 0<=i<(dims[0]-1)), then j
    (0<=j<(dims[1]-1)), then k (0<=k<(dims[2]-1)) The number of cells is
    (dims[0]-1)*(dims[1]-1)*(dims[2]-1).
    
    StructuredGrid has the ability to blank, or "turn-off" points and
    cells in the dataset. This is done by setting
    DataSetAttributes::HIDDENPOINT or DataSetAttributes::HIDDENCELL
    in the ghost array for each point / cell that needs to be blanked.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStructuredGrid, obj, update, **traits)
    
    dimensions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(0, 0, 0), cols=3, help=\
        """
        following methods are specific to structured grid
        """
    )

    def _dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimensions,
                        self.dimensions)

    extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(0, -1, 0, -1, 0, -1), cols=3, help=\
        """
        Different ways to set the extent of the data array.  The extent
        should be set before the "Scalars" are set or allocated. The
        Extent is stored  in the order (X, Y, Z).
        """
    )

    def _extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtent,
                        self.extent)

    def get_cell_dims(self, *args):
        """
        V.get_cell_dims([int, int, int])
        C++: void GetCellDims(int cellDims[3])
        Given the node dimensions of this grid instance, this method
        computes the node dimensions. The value in each dimension can
        will have a lowest value of "1" such that computing the total
        number of cells can be achieved by simply by
        cell_dims[_0]*cell_dims[_1]*cell_dims[_2].
        """
        ret = self._wrap_call(self._vtk_obj.GetCellDims, *args)
        return ret

    def _get_data_dimension(self):
        return self._vtk_obj.GetDataDimension()
    data_dimension = traits.Property(_get_data_dimension, help=\
        """
        Return the dimensionality of the data.
        """
    )

    def blank_cell(self, *args):
        """
        V.blank_cell(int)
        C++: void BlankCell(IdType ptId)
        Methods for supporting blanking of cells. Blanking turns on or
        off cells in the structured grid, and hence the points connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.BlankCell, *args)
        return ret

    def blank_point(self, *args):
        """
        V.blank_point(int)
        C++: void BlankPoint(IdType ptId)
        Methods for supporting blanking of cells. Blanking turns on or
        off points in the structured grid, and hence the cells connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.BlankPoint, *args)
        return ret

    def is_cell_visible(self, *args):
        """
        V.is_cell_visible(int) -> int
        C++: unsigned char IsCellVisible(IdType cellId)
        Return non-zero value if specified point is visible. These
        methods should be called only after the dimensions of the grid
        are set.
        """
        ret = self._wrap_call(self._vtk_obj.IsCellVisible, *args)
        return ret

    def is_point_visible(self, *args):
        """
        V.is_point_visible(int) -> int
        C++: unsigned char IsPointVisible(IdType ptId)
        Return non-zero value if specified point is visible. These
        methods should be called only after the dimensions of the grid
        are set.
        """
        ret = self._wrap_call(self._vtk_obj.IsPointVisible, *args)
        return ret

    def un_blank_cell(self, *args):
        """
        V.un_blank_cell(int)
        C++: void UnBlankCell(IdType ptId)
        Methods for supporting blanking of cells. Blanking turns on or
        off cells in the structured grid, and hence the points connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.UnBlankCell, *args)
        return ret

    def un_blank_point(self, *args):
        """
        V.un_blank_point(int)
        C++: void UnBlankPoint(IdType ptId)
        Methods for supporting blanking of cells. Blanking turns on or
        off points in the structured grid, and hence the cells connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.UnBlankPoint, *args)
        return ret

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('dimensions', 'GetDimensions'), ('extent', 'GetExtent'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'dimensions', 'extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StructuredGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], ['dimensions', 'extent']),
            title='Edit StructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


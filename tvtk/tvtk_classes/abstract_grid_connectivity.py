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


class AbstractGridConnectivity(Object):
    """
    AbstractGridConnectivity -  A superclass that defines the
    interface to be implemented by all
     concrete grid connectivity classes.
    
    Superclass: Object
    
    Grid connectivity classes provide the
     mechanism to achieve the following:
     
       
         Handling of partitioned/distributed data
    
    
          Construct the neighboring topology information for each
    partition,e.g.,
          used for creating communication lists and in computing
    statistics,i.e.,
          average, mean, etc.
         
         Creation of ghost layers
    
    
          Provides the mechanism for automatically generating ghost
    information
          given a partitioned/distributed grid configuration.
         
       
     
    
    @sa
     StructuredGridConnectivity StructuredAMRGridConnectivity
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractGridConnectivity, obj, update, **traits)
    
    number_of_ghost_layers = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of ghost layers
        """
    )

    def _number_of_ghost_layers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfGhostLayers,
                        self.number_of_ghost_layers)

    number_of_grids = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Sets the total number of grids in the domain. Note: This method
        is implemented by concrete classes. NOTE: Concrete classes
        implementing this pure virtual method must set the number of
        grids and call allocate_user_register_data_structures in addition to
        defining any other additional functionality.
        """
    )

    def _number_of_grids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfGrids,
                        self.number_of_grids)

    def get_ghosted_cell_ghost_array(self, *args):
        """
        V.get_ghosted_cell_ghost_array(int) -> UnsignedCharArray
        C++: UnsignedCharArray *GetGhostedCellGhostArray(
            const int gridID)
        Returns the ghosted cells ghost array for the grid associated
        with the given grid ID. The return pointer is a shallow-copy of
        the internal data-structure. The pointer may be NULL iff there is
        no ghosted cells ghost array for the requested grid.
        """
        ret = self._wrap_call(self._vtk_obj.GetGhostedCellGhostArray, *args)
        return wrap_vtk(ret)

    def get_ghosted_grid_cell_data(self, *args):
        """
        V.get_ghosted_grid_cell_data(int) -> CellData
        C++: CellData *GetGhostedGridCellData(const int gridID)
        Returns the ghosted grid cell data for the grid associated with
        the given grid ID. The return pointer is a shallow-copy of the
        internal data-structure. The pointer may be NULL iff there is no
        ghosted cell data for the requested grid.
        """
        ret = self._wrap_call(self._vtk_obj.GetGhostedGridCellData, *args)
        return wrap_vtk(ret)

    def get_ghosted_grid_point_data(self, *args):
        """
        V.get_ghosted_grid_point_data(int) -> PointData
        C++: PointData *GetGhostedGridPointData(const int gridID)
        Returns the ghosted grid point data for the grid associated with
        the given grid ID. The return pointer is a shallow-copy of the
        internal data-structure. The pointer may be NULL iff there is no
        ghosted point data for the requested grid.
        """
        ret = self._wrap_call(self._vtk_obj.GetGhostedGridPointData, *args)
        return wrap_vtk(ret)

    def get_ghosted_point_ghost_array(self, *args):
        """
        V.get_ghosted_point_ghost_array(int) -> UnsignedCharArray
        C++: UnsignedCharArray *GetGhostedPointGhostArray(
            const int gridID)
        Returns the ghosted points ghost array for the grid associated
        with the given grid ID. The return pointer is a shallow-copy of
        the internal data-structure. The pointer may be NULL iff there is
        no ghosted points ghost array for the requested grid.
        """
        ret = self._wrap_call(self._vtk_obj.GetGhostedPointGhostArray, *args)
        return wrap_vtk(ret)

    def get_ghosted_points(self, *args):
        """
        V.get_ghosted_points(int) -> Points
        C++: Points *GetGhostedPoints(const int gridID)
        Returns the ghosted grid points for the grid associated with the
        given grid ID. The return pointer is a shallow-copy of the
        internal data structure. The pointer may be NULL iff there are no
        ghosted points created for the requested grid.
        """
        ret = self._wrap_call(self._vtk_obj.GetGhostedPoints, *args)
        return wrap_vtk(ret)

    def compute_neighbors(self):
        """
        V.compute_neighbors()
        C++: virtual void ComputeNeighbors()
        Computes the grid neighboring topology for the domain
        """
        ret = self._vtk_obj.ComputeNeighbors()
        return ret
        

    def create_ghost_layers(self, *args):
        """
        V.create_ghost_layers(int)
        C++: virtual void CreateGhostLayers(const int N=1)
        Creates N layers of ghost layers where N is the number of cells
        that will be added to each grid. If no parameter is supplied, N
        has a nominal value of 1, in which case 1 layer of cells would be
        added. NOTE: This method is implemented by concrete
        implementations
        """
        ret = self._wrap_call(self._vtk_obj.CreateGhostLayers, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_ghost_layers',
    'GetNumberOfGhostLayers'), ('number_of_grids', 'GetNumberOfGrids'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'number_of_ghost_layers',
    'number_of_grids'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AbstractGridConnectivity, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractGridConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['number_of_ghost_layers', 'number_of_grids']),
            title='Edit AbstractGridConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractGridConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


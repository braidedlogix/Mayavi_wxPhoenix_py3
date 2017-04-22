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

from tvtk.tvtk_classes.abstract_grid_connectivity import AbstractGridConnectivity


class StructuredAMRGridConnectivity(AbstractGridConnectivity):
    """
    StructuredAMRGridConnectivity -  grid connectivity.
    
    Superclass: AbstractGridConnectivity
    
    A concrete instance of AbstractGridConnectivity that implements
     functionality for computing the neighboring topology within a
    structured
     AMR grid, as well as, generating ghost-layers. Support is provided
    for
     1-D, 2-D (XY,XZ,YZ) and 3-D cell-centered datasets. This
    implementation
     does not have any support for distributed data. For the parallel
     implementation see PStructuredAMRGridConnectivity.
    
    @sa
     GhostArray PStructuredAMRGridConnectivity
    AbstractGridConnectivity
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStructuredAMRGridConnectivity, obj, update, **traits)
    
    balanced_refinement = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Get/Set macro for balanced_refinement property, default is true.
        If the refinement is balanced, then, adjacent grids in the AMR
        hierarchy can only differ by one level. By default, a balanced
        refinement is assumed.
        """
    )

    def _balanced_refinement_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBalancedRefinement,
                        self.balanced_refinement)

    cell_centered = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Get/Set cell_centered property which indicates if the data is
        cell-centered By default, cell-centered is set to true.
        """
    )

    def _cell_centered_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellCentered,
                        self.cell_centered)

    node_centered = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Get/Set macor node_centered property which indicates if the data
        is node-centered or cell-centered. By default, node-centered is
        set to false since AMR datasets are primarily cell-centered.
        """
    )

    def _node_centered_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNodeCentered,
                        self.node_centered)

    def get_ghosted_extent(self, *args):
        """
        V.get_ghosted_extent(int, [int, int, int, int, int, int])
        C++: void GetGhostedExtent(const int gridID, int ext[6])
        Returns the ghost extend for the grid corresponding to the given
        grid ID.
        """
        ret = self._wrap_call(self._vtk_obj.GetGhostedExtent, *args)
        return ret

    def get_neighbor(self, *args):
        """
        V.get_neighbor(int, int) -> StructuredAMRNeighbor
        C++: StructuredAMRNeighbor GetNeighbor(const int gridID,
            const int nei)
        Returns the AMR neighbor for the patch with the corresponding
        grid ID.
        """
        ret = self._wrap_call(self._vtk_obj.GetNeighbor, *args)
        return wrap_vtk(ret)

    def get_number_of_neighbors(self, *args):
        """
        V.get_number_of_neighbors(int) -> int
        C++: int GetNumberOfNeighbors(const int gridID)
        Returns the number of neighbors for the grid corresponding to the
        given grid ID.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfNeighbors, *args)
        return ret

    def initialize(self, *args):
        """
        V.initialize(int, int, int)
        C++: void Initialize(const unsigned int NumberOfLevels,
            const unsigned int N, const int RefinementRatio=-1)
        Initializes this instance of StructuredAMRGridConnectivity
        where N is the total number of grids in the AMR hierarchy.
        Optionally, if the AMR dataset has a constant refinement, it
        should be specified during initialization as the code optimizes
        for it. If a -1 or no refinement ratio is specified a varying
        refinement ratio is assumed.
        """
        ret = self._wrap_call(self._vtk_obj.Initialize, *args)
        return ret

    def register_grid(self, *args):
        """
        V.register_grid(int, int, int, [int, int, int, int, int, int],
            UnsignedCharArray, UnsignedCharArray, PointData,
            CellData, Points)
        C++: virtual void RegisterGrid(const int gridIdx, const int level,
             const int refinementRatio, int extents[6],
            UnsignedCharArray *nodesGhostArray,
            UnsignedCharArray *cellGhostArray, PointData *pointData,
             CellData *cellData, Points *gridNodes)
        V.register_grid(int, int, [int, int, int, int, int, int],
            UnsignedCharArray, UnsignedCharArray, PointData,
            CellData, Points)
        C++: virtual void RegisterGrid(const int gridIdx, const int level,
             int extents[6], UnsignedCharArray *nodesGhostArray,
            UnsignedCharArray *cellGhostArray, PointData *pointData,
             CellData *cellData, Points *gridNodes)
        Registers the AMR grid with the given global linear grid ID
        (starting numbering from 0) and level and refinement ratio. This
        method is to be used when the refinement ratio is not constant.
        """
        my_args = deref_array(args, [('int', 'int', 'int', ['int', 'int', 'int', 'int', 'int', 'int'], 'vtkUnsignedCharArray', 'vtkUnsignedCharArray', 'vtkPointData', 'vtkCellData', 'vtkPoints'), ('int', 'int', ['int', 'int', 'int', 'int', 'int', 'int'], 'vtkUnsignedCharArray', 'vtkUnsignedCharArray', 'vtkPointData', 'vtkCellData', 'vtkPoints')])
        ret = self._wrap_call(self._vtk_obj.RegisterGrid, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('balanced_refinement',
    'GetBalancedRefinement'), ('cell_centered', 'GetCellCentered'),
    ('node_centered', 'GetNodeCentered'), ('number_of_ghost_layers',
    'GetNumberOfGhostLayers'), ('number_of_grids', 'GetNumberOfGrids'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'balanced_refinement',
    'cell_centered', 'node_centered', 'number_of_ghost_layers',
    'number_of_grids'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StructuredAMRGridConnectivity, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StructuredAMRGridConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['balanced_refinement', 'cell_centered',
            'node_centered', 'number_of_ghost_layers', 'number_of_grids']),
            title='Edit StructuredAMRGridConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StructuredAMRGridConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


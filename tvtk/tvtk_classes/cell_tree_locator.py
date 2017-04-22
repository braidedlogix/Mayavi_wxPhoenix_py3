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

from tvtk.tvtk_classes.abstract_cell_locator import AbstractCellLocator


class CellTreeLocator(AbstractCellLocator):
    """
    CellTreeLocator - This class implements the data structures,
    construction algorithms for fast cell location presented in "Fast,
    Memory-Efficient Cell location in Unstructured Grids for
    Visualization" by Christop Garth and Kenneth
    
    Superclass: AbstractCellLocator
    
    I. Joy in vis_week, 2011.
    
    Cell Tree is a bounding interval hierarchy based data structure,
    where child boxes do not form an exact split of the parent boxes
    along a dimension.  Therefore two axis- aligned bounding planes (left
    max and right min) are stored for each node along a dimension. This
    class implements the data structure (Cell Tree Node) and its build
    and traversal algorithms described in the paper. Some methods in
    building and traversing the cell tree in this class were derived
    avt_cell_locator_bih class in the vis_it Visualization Tool
    
    @sa
    Locator CellLocator ModifiedBSPTree
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellTreeLocator, obj, update, **traits)
    
    def build_locator_if_needed(self):
        """
        V.build_locator_if_needed()
        C++: virtual void BuildLocatorIfNeeded()
        Satisfy Locator abstract interface.
        """
        ret = self._vtk_obj.BuildLocatorIfNeeded()
        return ret
        

    def build_locator_internal(self):
        """
        V.build_locator_internal()
        C++: virtual void BuildLocatorInternal()
        Satisfy Locator abstract interface.
        """
        ret = self._vtk_obj.BuildLocatorInternal()
        return ret
        

    def force_build_locator(self):
        """
        V.force_build_locator()
        C++: virtual void ForceBuildLocator()
        Satisfy Locator abstract interface.
        """
        ret = self._vtk_obj.ForceBuildLocator()
        return ret
        

    _updateable_traits_ = \
    (('cache_cell_bounds', 'GetCacheCellBounds'), ('lazy_evaluation',
    'GetLazyEvaluation'), ('retain_cell_lists', 'GetRetainCellLists'),
    ('use_existing_search_structure', 'GetUseExistingSearchStructure'),
    ('automatic', 'GetAutomatic'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_cells_per_node', 'GetNumberOfCellsPerNode'), ('max_level',
    'GetMaxLevel'), ('tolerance', 'GetTolerance'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['automatic', 'cache_cell_bounds', 'debug', 'global_warning_display',
    'lazy_evaluation', 'retain_cell_lists',
    'use_existing_search_structure', 'max_level',
    'number_of_cells_per_node', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CellTreeLocator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CellTreeLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic', 'cache_cell_bounds', 'lazy_evaluation',
            'retain_cell_lists', 'use_existing_search_structure'], [],
            ['max_level', 'number_of_cells_per_node', 'tolerance']),
            title='Edit CellTreeLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellTreeLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


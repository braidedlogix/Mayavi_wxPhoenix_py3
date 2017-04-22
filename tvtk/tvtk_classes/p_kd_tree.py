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

from tvtk.tvtk_classes.kd_tree import KdTree


class PKdTree(KdTree):
    """
    PKdTree - Build a k-d tree decomposition of a list of points.
    
    Superclass: KdTree
    
    Build, in parallel, a k-d tree decomposition of one or more
         DataSets distributed across processors.  We assume each
         process has read in one portion of a large distributed data set.
         When done, each process has access to the k-d tree structure,
         can obtain information about which process contains
         data for each spatial region, and can depth sort the spatial
         regions.
    
    
         This class can also assign spatial regions to processors, based
         on one of several region assignment schemes.  By default
         a contiguous, convex region is assigned to each process. 
    Several
         queries return information about how many and what cells I have
         that lie in a region assigned to another process.
    
    @sa
         KdTree
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPKdTree, obj, update, **traits)
    
    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        Set/Get the communicator object
        """
    )

    def get_all_processes_bordering_on_point(self, *args):
        """
        V.get_all_processes_bordering_on_point(float, float, float,
            IntArray)
        C++: void GetAllProcessesBorderingOnPoint(float x, float y,
            float z, IntArray *list)
        The k-d tree spatial regions have been assigned to processes.
        Given a point on the boundary of one of the regions, this method
        creates a list of all processes whose region boundaries include
        that point.  This may be required when looking for processes that
        have cells adjacent to the cells of a given process.
        """
        my_args = deref_array(args, [('float', 'float', 'float', 'vtkIntArray')])
        ret = self._wrap_call(self._vtk_obj.GetAllProcessesBorderingOnPoint, *my_args)
        return ret

    def get_cell_array_global_range(self, *args):
        """
        V.get_cell_array_global_range(string, [float, float]) -> int
        C++: int GetCellArrayGlobalRange(const char *name,
            double range[2])
        V.get_cell_array_global_range(int, [float, float]) -> int
        C++: int GetCellArrayGlobalRange(int arrayIndex, double range[2])"""
        ret = self._wrap_call(self._vtk_obj.GetCellArrayGlobalRange, *args)
        return ret

    def get_cell_lists_for_process_regions(self, *args):
        """
        V.get_cell_lists_for_process_regions(int, int, IdList, IdList)
            -> int
        C++: IdType GetCellListsForProcessRegions(int ProcessId,
            int set, IdList *inRegionCells, IdList *onBoundaryCells)
        V.get_cell_lists_for_process_regions(int, DataSet, IdList,
            IdList) -> int
        C++: IdType GetCellListsForProcessRegions(int ProcessId,
            DataSet *set, IdList *inRegionCells,
            IdList *onBoundaryCells)
        V.get_cell_lists_for_process_regions(int, IdList, IdList) -> int
        C++: IdType GetCellListsForProcessRegions(int ProcessId,
            IdList *inRegionCells, IdList *onBoundaryCells)
        After regions have been assigned to processes, I may want to know
        which cells I have that are in the regions assigned to a
        particular process.
        
        * This method takes a process ID and two IdLists.  It
        * writes to the first list the IDs of the cells
        * contained in the process' regions.  (That is, their cell
        * centroid is contained in the region.)  To the second list it
        * write the IDs of the cells which intersect the process' regions
        * but whose cell centroid lies elsewhere.
        
        * The total number of cell IDs written to both lists is returned.
        * Either list pointer passed in can be NULL, and it will be
          ignored.
        * If there are multiple data sets, you must specify which data
          set
        * you wish cell IDs for.
        
        * The caller should delete these two lists when done.  This
          method
        * uses the cell lists created in KdTree::CreateCellLists().
        * If the cell lists for the process' regions do not exist, this
        * method will first build the cell lists for all regions by
          calling
        * create_cell_lists().  You must remember to delete_cell_lists() when
        * done with all calls to this method, as cell lists can require a
        * great deal of memory.
        """
        my_args = deref_array(args, [('int', 'int', 'vtkIdList', 'vtkIdList'), ('int', 'vtkDataSet', 'vtkIdList', 'vtkIdList'), ('int', 'vtkIdList', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetCellListsForProcessRegions, *my_args)
        return ret

    def get_point_array_global_range(self, *args):
        """
        V.get_point_array_global_range(string, [float, float]) -> int
        C++: int GetPointArrayGlobalRange(const char *name,
            double range[2])
        V.get_point_array_global_range(int, [float, float]) -> int
        C++: int GetPointArrayGlobalRange(int arrayIndex, double range[2])"""
        ret = self._wrap_call(self._vtk_obj.GetPointArrayGlobalRange, *args)
        return ret

    def get_process_assigned_to_region(self, *args):
        """
        V.get_process_assigned_to_region(int) -> int
        C++: int GetProcessAssignedToRegion(int regionId)
        Returns the ID of the process assigned to the region.
        """
        ret = self._wrap_call(self._vtk_obj.GetProcessAssignedToRegion, *args)
        return ret

    def get_process_cell_count_for_region(self, *args):
        """
        V.get_process_cell_count_for_region(int, int) -> int
        C++: int GetProcessCellCountForRegion(int processId, int regionId)
        Returns the number of cells the specified process has in the
        specified region.
        """
        ret = self._wrap_call(self._vtk_obj.GetProcessCellCountForRegion, *args)
        return ret

    def get_process_list_for_region(self, *args):
        """
        V.get_process_list_for_region(int, IntArray) -> int
        C++: int GetProcessListForRegion(int regionId,
            IntArray *processes)
        Adds the list of processes having data for the given region to
        the supplied list, returns the number of processes added.
        """
        my_args = deref_array(args, [('int', 'vtkIntArray')])
        ret = self._wrap_call(self._vtk_obj.GetProcessListForRegion, *my_args)
        return ret

    def get_processes_cell_count_for_region(self, *args):
        """
        V.get_processes_cell_count_for_region(int, [int, ...], int) -> int
        C++: int GetProcessesCellCountForRegion(int regionId, int *count,
            int len)
        Writes the number of cells each process has for the region to the
        supplied list of length len.  Returns the number of cell counts
        written.  The order of the cell counts corresponds to the order
        of process IDs in the process list returned by
        get_process_list_for_region.
        """
        ret = self._wrap_call(self._vtk_obj.GetProcessesCellCountForRegion, *args)
        return ret

    def _get_region_assignment(self):
        return self._vtk_obj.GetRegionAssignment()
    region_assignment = traits.Property(_get_region_assignment, help=\
        """
        The p_kd_tree class can assign spatial regions to processors after
        building the k-d tree, using one of several partitioning
        criteria. These functions Set/Get whether this assignment is
        computed. The default is "Off", no assignment is computed.   If
        "On", and no assignment scheme is specified, contiguous
        assignment will be computed.  Specifying an assignment scheme
        (with assign_regions*()) automatically turns on region_assignment.
        """
    )

    def get_region_assignment_list(self, *args):
        """
        V.get_region_assignment_list(int, IntArray) -> int
        C++: int GetRegionAssignmentList(int procId, IntArray *list)
        Writes the list of region IDs assigned to the specified process. 
        Regions IDs start at 0 and increase by 1 from there. Returns the
        number of regions in the list.
        """
        my_args = deref_array(args, [('int', 'vtkIntArray')])
        ret = self._wrap_call(self._vtk_obj.GetRegionAssignmentList, *my_args)
        return ret

    def _get_region_assignment_map(self):
        return self._vtk_obj.GetRegionAssignmentMap()
    region_assignment_map = traits.Property(_get_region_assignment_map, help=\
        """
        Returns the region assignment map where index is the region and
        value is the processes id for that region.
        """
    )

    def _get_region_assignment_map_length(self):
        return self._vtk_obj.GetRegionAssignmentMapLength()
    region_assignment_map_length = traits.Property(_get_region_assignment_map_length, help=\
        """
        / Returns the number of regions in the region assignment map.
        """
    )

    def get_region_list_for_process(self, *args):
        """
        V.get_region_list_for_process(int, IntArray) -> int
        C++: int GetRegionListForProcess(int processId,
            IntArray *regions)
        Adds the region IDs for which this process has data to the
        supplied IntArray.  Retruns the number of regions.
        """
        my_args = deref_array(args, [('int', 'vtkIntArray')])
        ret = self._wrap_call(self._vtk_obj.GetRegionListForProcess, *my_args)
        return ret

    def get_regions_cell_count_for_process(self, *args):
        """
        V.get_regions_cell_count_for_process(int, [int, ...], int) -> int
        C++: int GetRegionsCellCountForProcess(int ProcessId, int *count,
            int len)
        Writes to the supplied integer array the number of cells this
        process has for each region.  Returns the number of cell counts
        written.  The order of the cell counts corresponds to the order
        of region IDs in the region list returned by
        get_region_list_for_process.
        """
        ret = self._wrap_call(self._vtk_obj.GetRegionsCellCountForProcess, *args)
        return ret

    def _get_total_number_of_cells(self):
        return self._vtk_obj.GetTotalNumberOfCells()
    total_number_of_cells = traits.Property(_get_total_number_of_cells, help=\
        """
        Get the total number of cells distributed across the data files
        read by all processes.  You must have called build_locator before
        calling this method.
        """
    )

    def get_total_processes_in_region(self, *args):
        """
        V.get_total_processes_in_region(int) -> int
        C++: int GetTotalProcessesInRegion(int regionId)
        Returns the total number of processes that have data falling
        within this spatial region.
        """
        ret = self._wrap_call(self._vtk_obj.GetTotalProcessesInRegion, *args)
        return ret

    def get_total_regions_for_process(self, *args):
        """
        V.get_total_regions_for_process(int) -> int
        C++: int GetTotalRegionsForProcess(int processId)
        Returns the total number of spatial regions that a given process
        has data for.
        """
        ret = self._wrap_call(self._vtk_obj.GetTotalRegionsForProcess, *args)
        return ret

    def assign_regions(self, *args):
        """
        V.assign_regions([int, ...], int) -> int
        C++: int AssignRegions(int *map, int numRegions)
        Assign spatial regions to processes via a user defined map. The
        user-supplied map is indexed by region ID, and provides a process
        ID for each region.
        """
        ret = self._wrap_call(self._vtk_obj.AssignRegions, *args)
        return ret

    def assign_regions_contiguous(self):
        """
        V.assign_regions_contiguous() -> int
        C++: int AssignRegionsContiguous()
        Let the p_kd_tree class assign a process to each region by
        assigning contiguous sets of spatial regions to each process. 
        The set of regions assigned to each process will always have a
        union that is a convex space (a box). If the k-d tree has not yet
        been built, the regions will be assigned after build_locator
        executes.
        """
        ret = self._vtk_obj.AssignRegionsContiguous()
        return ret
        

    def assign_regions_round_robin(self):
        """
        V.assign_regions_round_robin() -> int
        C++: int AssignRegionsRoundRobin()
        Let the p_kd_tree class assign a process to each region in a round
        robin fashion.  If the k-d tree has not yet been built, the
        regions will be assigned after build_locator executes.
        """
        ret = self._vtk_obj.AssignRegionsRoundRobin()
        return ret
        

    def create_global_data_array_bounds(self):
        """
        V.create_global_data_array_bounds() -> int
        C++: int CreateGlobalDataArrayBounds()
        A convenience function which compiles the global bounds of the
        data arrays across processes. These bounds can be accessed with
        "_get_cell_array_global_range" and "_get_point_array_global_range". This
        method must be called by all processes or it will hang. Returns 1
        on error, 0 when no error.
        """
        ret = self._vtk_obj.CreateGlobalDataArrayBounds()
        return ret
        

    def create_process_cell_count_data(self):
        """
        V.create_process_cell_count_data() -> int
        C++: int CreateProcessCellCountData()
        Create tables of counts of cells per process per region. These
        tables can be accessed with queries like "_has_data",
        "_get_process_cell_count_for_region", and so on. You must have called
        build_locator() beforehand.  This method must be called by all
        processes or it will hang. Returns 1 on error, 0 when no error.
        """
        ret = self._vtk_obj.CreateProcessCellCountData()
        return ret
        

    def has_data(self, *args):
        """
        V.has_data(int, int) -> int
        C++: int HasData(int processId, int regionId)
        Returns 1 if the process has data for the given region, 0
        otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.HasData, *args)
        return ret

    def view_order_all_processes_from_position(self, *args):
        """
        V.view_order_all_processes_from_position((float, float, float),
            IntArray) -> int
        C++: int ViewOrderAllProcessesFromPosition(
            const double cameraPosition[3], IntArray *orderedList)
        Return a list of all processes in order from front to back given
        a camera position.  Use this to do visibility sorts in
        perspective projection mode. `ordered_list' will be resized to the
        number of processes. The return value is the number of processes.
        \pre ordered_list_exists: ordered_list!=_0
        """
        my_args = deref_array(args, [(('float', 'float', 'float'), 'vtkIntArray')])
        ret = self._wrap_call(self._vtk_obj.ViewOrderAllProcessesFromPosition, *my_args)
        return ret

    def view_order_all_processes_in_direction(self, *args):
        """
        V.view_order_all_processes_in_direction((float, float, float),
            IntArray) -> int
        C++: int ViewOrderAllProcessesInDirection(
            const double directionOfProjection[3],
            IntArray *orderedList)
        Return a list of all processes in order from front to back given
        a vector direction of projection.  Use this to do visibility
        sorts in parallel projection mode. `ordered_list' will be resized
        to the number of processes. The return value is the number of
        processes.
        \pre ordered_list_exists: ordered_list!=_0
        """
        my_args = deref_array(args, [(('float', 'float', 'float'), 'vtkIntArray')])
        ret = self._wrap_call(self._vtk_obj.ViewOrderAllProcessesInDirection, *my_args)
        return ret

    _updateable_traits_ = \
    (('generate_representation_using_data_bounds',
    'GetGenerateRepresentationUsingDataBounds'),
    ('include_region_boundary_cells', 'GetIncludeRegionBoundaryCells'),
    ('timing', 'GetTiming'), ('automatic', 'GetAutomatic'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('fudge_factor', 'GetFudgeFactor'), ('min_cells', 'GetMinCells'),
    ('number_of_regions_or_less', 'GetNumberOfRegionsOrLess'),
    ('number_of_regions_or_more', 'GetNumberOfRegionsOrMore'),
    ('max_level', 'GetMaxLevel'), ('tolerance', 'GetTolerance'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['automatic', 'debug', 'generate_representation_using_data_bounds',
    'global_warning_display', 'include_region_boundary_cells', 'timing',
    'fudge_factor', 'max_level', 'min_cells', 'number_of_regions_or_less',
    'number_of_regions_or_more', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PKdTree, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PKdTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic', 'generate_representation_using_data_bounds',
            'include_region_boundary_cells', 'timing'], [], ['fudge_factor',
            'max_level', 'min_cells', 'number_of_regions_or_less',
            'number_of_regions_or_more', 'tolerance']),
            title='Edit PKdTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PKdTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


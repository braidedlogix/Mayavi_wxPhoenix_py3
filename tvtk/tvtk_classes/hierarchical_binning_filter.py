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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class HierarchicalBinningFilter(PolyDataAlgorithm):
    """
    HierarchicalBinningFilter - uniform binning of points into a
    hierarchical structure
    
    Superclass: PolyDataAlgorithm
    
    HierarchicalBinningFilter creates a spatial, hierarchical ordering
    of input points. This hierarchy is suitable for level-of-detail
    rendering, or multiresolution processing. Each level of the hierarchy
    is based on uniform binning of space, where deeper levels (and its
    bins) are repeatedly subdivided by a given branching factor. Points
    are associated with bins at different levels, with the number of
    points in each level proportional to the number of bins in that
    level. The output points are sorted according to a bin number, where
    the bin number is unique, monotonically increasing number
    representing the breadth first ordering of all of the levels and
    their bins. Thus all points in a bin (or even a level) are segmented
    into contiguous runs.
    
    Note that points are associated with different bins using a pseudo
    random process. No points are repeated, and no new points are
    created, thus the effect of executing this filter is simply to
    reorder the input points.
    
    The algorithm proceeds as follows: Given an initial bounding box, the
    space is uniformally subdivided into bins of (M x N x O) dimensions;
    in turn each subsequent level in the tree is further divided into (M
    x N x O) bins (note that level 0 is a single, root bin). Thus the
    number of bins at level L of the hierachical tree is: Nbins=(M^L x
    N^L x O^L). Once the binning is created to a specified depth, then
    points are placed in the bins using a pseudo-random sampling
    proportional to the number of bins in each level. All input points
    are sorted in the order described above, with no points repeated.
    
    The output of this filter are sorted points and associated point
    attributes represented by a PolyData. In addition, an offest
    integral array is associated with the field data of the output,
    providing offsets into the points list via a breadth-first traversal
    order. Metadata describing the output is provided in the field data.
    Convenience functions are also provided here to access the data in a
    particular bin or across a level. (Using the offset array directly
    may result in higher performance.)
    
    While any PointSet type can be provided as input, the output is
    represented by an explicit representation of points via a
    PolyData. This output polydata will populate its instance of
    Points, but no cells will be defined (i.e., no Vertex or
    PolyVertex are contained in the output).
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    PointCloudFilter QuadricClustering StaticPointLocator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHierarchicalBinningFilter, obj, update, **traits)
    
    automatic = tvtk_base.true_bool_trait(help=\
        """
        Specify whether to determine the determine the level divisions,
        and the bounding box automatically (by default this is on). If
        off, then the user must specify both the bounding box and bin
        divisions. (Computing the bounding box can be slow for large
        point clouds, manual specification can save time.)
        """
    )

    def _automatic_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutomatic,
                        self.automatic_)

    bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(0.0, 1.0, 0.0, 1.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    divisions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(2, 2, 2), cols=3, help=\
        """
        
        """
    )

    def _divisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDivisions,
                        self.divisions)

    number_of_levels = traits.Trait(3, traits.Range(1, 12, enter_set=True, auto_set=False), help=\
        """
        Specify the number of levels in the spatial hierachy. By default,
        the number of levels is three.
        """
    )

    def _number_of_levels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfLevels,
                        self.number_of_levels)

    def get_bin_bounds(self, *args):
        """
        V.get_bin_bounds(int, [float, float, float, float, float, float])
        C++: void GetBinBounds(int globalBin, double bounds[6])
        Convenience methods for extracting useful information about a bin
        tree. Given a global bin number, return the bounds
        (xmin,xmax,ymin,ymax,zmin,zmax) for that bin. Invoke this method
        after the bin tree has been built.
        """
        ret = self._wrap_call(self._vtk_obj.GetBinBounds, *args)
        return ret

    def get_bin_offset(self, *args):
        """
        V.get_bin_offset(int, int) -> int
        C++: IdType GetBinOffset(int globalBin, IdType &npts)
        Convenience methods for extracting useful information about this
        bin tree.  Given a global bin number, return the point id and
        number of points for that bin. Invoke this method after the bin
        tree has been built.
        """
        ret = self._wrap_call(self._vtk_obj.GetBinOffset, *args)
        return ret

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def get_level_offset(self, *args):
        """
        V.get_level_offset(int, int) -> int
        C++: IdType GetLevelOffset(int level, IdType &npts)
        Convenience methods for extracting useful information about this
        bin tree.  Given a level, return the beginning point id and
        number of points that level. Invoke this method after the bin
        tree has been built.
        """
        ret = self._wrap_call(self._vtk_obj.GetLevelOffset, *args)
        return ret

    def get_local_bin_bounds(self, *args):
        """
        V.get_local_bin_bounds(int, int, [float, float, float, float, float,
            float])
        C++: void GetLocalBinBounds(int level, int localBin,
            double bounds[6])
        Convenience methods for extracting useful information about a bin
        tree. Given a level, and a local bin number, return the bounds
        (xmin,xmax,ymin,ymax,zmin,zmax) for that bin. Invoke this method
        after the bin tree has been built.
        """
        ret = self._wrap_call(self._vtk_obj.GetLocalBinBounds, *args)
        return ret

    def get_local_bin_offset(self, *args):
        """
        V.get_local_bin_offset(int, int, int) -> int
        C++: IdType GetLocalBinOffset(int level, int localBin,
            IdType &npts)
        Convenience methods for extracting useful information about this
        bin tree.  Given a level, and the bin number in that level,
        return the offset point id and number of points for that bin.
        Invoke this method after the bin tree has been built.
        """
        ret = self._wrap_call(self._vtk_obj.GetLocalBinOffset, *args)
        return ret

    def get_number_of_bins(self, *args):
        """
        V.get_number_of_bins(int) -> int
        C++: int GetNumberOfBins(int level)
        Convenience methods for extracting useful information about this
        bin tree.  Return the number of bins in a particular level of the
        tree. Invoke this method after the bin tree has been built.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfBins, *args)
        return ret

    def _get_number_of_global_bins(self):
        return self._vtk_obj.GetNumberOfGlobalBins()
    number_of_global_bins = traits.Property(_get_number_of_global_bins, help=\
        """
        Convenience methods for extracting useful information about this
        bin tree.  Return the number of total bins across all levels
        (i.e., the total global bins). Invoke this method after the bin
        tree has been built.
        """
    )

    _updateable_traits_ = \
    (('automatic', 'GetAutomatic'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('bounds',
    'GetBounds'), ('divisions', 'GetDivisions'), ('number_of_levels',
    'GetNumberOfLevels'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'automatic', 'debug', 'global_warning_display',
    'release_data_flag', 'bounds', 'divisions', 'number_of_levels',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HierarchicalBinningFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HierarchicalBinningFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic'], [], ['bounds', 'divisions', 'number_of_levels']),
            title='Edit HierarchicalBinningFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HierarchicalBinningFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


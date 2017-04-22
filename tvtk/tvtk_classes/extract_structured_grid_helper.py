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


class ExtractStructuredGridHelper(Object):
    """
    ExtractStructuredGridHelper - helper for extracting/sub-sampling
     structured datasets.
    
    Superclass: Object
    
    ExtractStructuredGridHelper provides some common functionality
    that is used by filters that extract and sub-sample structured data.
    Specifically, it provides functionality for calculating the mapping
    from the output extent of each process to the input extent.
    
    @sa
    ExtractGrid ExtractVOI ExtractRectilinearGrid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractStructuredGridHelper, obj, update, **traits)
    
    def get_mapped_extent_value(self, *args):
        """
        V.get_mapped_extent_value(int, int) -> int
        C++: int GetMappedExtentValue(int dim, int outExtVal)
        Given a dimension and output extent value, return the
            corresponding
        input extent value. This method should be used to convert extent
        values.
        \param dim the data dimension.
        \param out_ext_val The output extent value along the given
            dimension.
        \pre dim >= 0 && dim < 3
        \pre out_ext_val >= this->_get_output_whole_extent()[_2*dim] &&
        out_ext_val <= this->_get_output_whole_extent()[_2*dim+_1]
        \return The input extent value along the given dimension.
        \sa get_mapped_index
        \sa get_mapped_extent_value_from_index
        """
        ret = self._wrap_call(self._vtk_obj.GetMappedExtentValue, *args)
        return ret

    def get_mapped_extent_value_from_index(self, *args):
        """
        V.get_mapped_extent_value_from_index(int, int) -> int
        C++: int GetMappedExtentValueFromIndex(int dim, int outIdx)
        Given a dimension and output extent index, return the
            corresponding
        input extent value. This method should be used to compute extent
        values from extent indices.
        \param dim the data dimension.
        \param out_idx The output index along the given dimension.
        \pre dim >= 0 && dim < 3
        \pre out_idx >= 0 && out_idx < this->_get_size( dim )
        \return The input extent value along the given dimension.
        \sa get_mapped_index
        \sa get_mapped_extent_value
        """
        ret = self._wrap_call(self._vtk_obj.GetMappedExtentValueFromIndex, *args)
        return ret

    def get_mapped_index(self, *args):
        """
        V.get_mapped_index(int, int) -> int
        C++: int GetMappedIndex(int dim, int outIdx)
        Given a dimension and output index, return the corresponding
        extent index. This method should be used to convert array
        indices, such as the coordinate arrays for rectilinear grids.
        \param dim the data dimension
        \param out_idx The output index along the given dimension.
        \pre dim >= 0 && dim < 3
        \pre out_idx >= 0 && out_idx < this->_get_size( dim )
        \return The input extent index along the given dimension.
        \sa get_mapped_extent_value
        \sa get_mapped_extent_value_from_index
        """
        ret = self._wrap_call(self._vtk_obj.GetMappedIndex, *args)
        return ret

    def get_mapped_index_from_extent_value(self, *args):
        """
        V.get_mapped_index_from_extent_value(int, int) -> int
        C++: int GetMappedIndexFromExtentValue(int dim, int outExtVal)
        Given a dimension and output extent value, return the
            corresponding
        input extent index. This method should be used to compute extent
        indices from extent values.
        \param dim the data dimension
        \param out_ext_val The output extent value along the given
            dimension.
        \pre dim >= 0 && dim < 3
        \pre out_ext_val >= this->_get_output_whole_extent()[_2*dim] &&
        out_ext_val <= this->_get_output_whole_extent()[_2*dim+_1]
        \return The input extent index along the given dimension.
        \sa get_mapped_extent_value
        \sa get_mapped_extent_value_from_index
        """
        ret = self._wrap_call(self._vtk_obj.GetMappedIndexFromExtentValue, *args)
        return ret

    def _get_output_whole_extent(self):
        return self._vtk_obj.GetOutputWholeExtent()
    output_whole_extent = traits.Property(_get_output_whole_extent, help=\
        """
        
        """
    )

    def get_partitioned_output_extent(self, *args):
        """
        V.get_partitioned_output_extent((int, int, int, int, int, int), (int,
             int, int, int, int, int), (int, int, int, int, int, int), (
            int, int, int), bool, [int, int, int, int, int, int])
        C++: static void GetPartitionedOutputExtent(
            const int globalVOI[6], const int partitionedVOI[6],
            const int outputWholeExtent[6], const int sampleRate[3],
            bool includeBoundary, int partitionedOutputExtent[6])
        Calculate the partitioned output extent for a partitioned
        structured dataset. This method sets partitioned_output_extent to
        the correct extent of an extracted dataset, such that it properly
        fits with the other partitioned pieces while considering the
        global_voi, thesample_rate, and the boundary conditions.
        \param global_voi The full VOI for the entire distributed dataset.
        \param partitioned_voi The VOI used in the serial extraction.
        \param output_whole_extent The output extent of the full dataset.
        \param sample_rate The sampling rate in each dimension.
        \param include_boundary Whether or not to include the boundary of
            the VOI,
        even if it doesn't fit the spacing.
        \param partitioned_output_extent The correct output extent of the
            extracted
        dataset.
        """
        ret = self._wrap_call(self._vtk_obj.GetPartitionedOutputExtent, *args)
        return ret

    def get_partitioned_voi(self, *args):
        """
        V.get_partitioned_voi((int, int, int, int, int, int), (int, int,
            int, int, int, int), (int, int, int), bool, [int, int, int,
            int, int, int])
        C++: static void GetPartitionedVOI(const int globalVOI[6],
            const int partitionedExtent[6], const int sampleRate[3],
            bool includeBoundary, int partitionedVOI[6])
        Calculate the VOI for a partitioned structured dataset. This
        method setspartitioned_voi to the VOI that extracts as much of
        thepartitioned_extent as possible while considering the global_voi,
        thesample_rate, and the boundary conditions.
        \param global_voi The full VOI for the entire distributed dataset.
        \param partitioned_extent Extent of the process's partitioned
            input data.
        \param sample_rate The sampling rate in each dimension.
        \param include_boundary Whether or not to include the boundary of
            the VOI,
        even if it doesn't fit the spacing.
        \param partitioned_voi The extent of the process's partitioned
            dataset that
        should be extracted by a serial extraction filter.
        """
        ret = self._wrap_call(self._vtk_obj.GetPartitionedVOI, *args)
        return ret

    def get_size(self, *args):
        """
        V.get_size(int) -> int
        C++: int GetSize(const int dim)
        Returns the size along a given dimension
        \param dim the dimension in query
        \pre dim >= 0 && dim < 3
        """
        ret = self._wrap_call(self._vtk_obj.GetSize, *args)
        return ret

    def compute_begin_and_end(self, *args):
        """
        V.compute_begin_and_end([int, int, int, int, int, int], [int, int,
            int, int, int, int], [int, int, int], [int, int, int])
        C++: void ComputeBeginAndEnd(int inExt[6], int voi[6],
            int begin[3], int end[3])
        Returns the begin & end extent that intersects with the VOI
        \param in_ext the input extent
        \param voi the volume of interest
        \param begin the begin extent
        \param end the end extent
        """
        ret = self._wrap_call(self._vtk_obj.ComputeBeginAndEnd, *args)
        return ret

    def copy_cell_data(self, *args):
        """
        V.copy_cell_data([int, int, int, int, int, int], [int, int, int,
            int, int, int], CellData, CellData)
        C++: void CopyCellData(int inExt[6], int outExt[6],
            CellData *cd, CellData *outCD)
        Copies the cell data to the output.
        \param in_ext the input grid extent.
        \param out_ext the output grid extent.
        \param cd the input cell data.
        \param out_cd the output cell data.
        \pre cd != NULL.
        \pre out_cd != NULL.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyCellData, *my_args)
        return ret

    def copy_points_and_point_data(self, *args):
        """
        V.copy_points_and_point_data([int, int, int, int, int, int], [int,
            int, int, int, int, int], PointData, Points,
            PointData, Points)
        C++: void CopyPointsAndPointData(int inExt[6], int outExt[6],
            PointData *pd, Points *inpnts, PointData *outPD,
            Points *outpnts)
        Copies the points & point data to the output.
        \param in_ext the input grid extent.
        \param out_ext the output grid extent.
        \param pd pointer to the input point data.
        \param inpnts pointer to the input points, or NULL if uniform
            grid.
        \param out_pd point to the output point data.
        \param outpnts pointer to the output points, or NULL if uniform
            grid.
        \pre pd != NULL.
        \pre out_pd != NULL.
        """
        my_args = deref_array(args, [(['int', 'int', 'int', 'int', 'int', 'int'], ['int', 'int', 'int', 'int', 'int', 'int'], 'vtkPointData', 'vtkPoints', 'vtkPointData', 'vtkPoints')])
        ret = self._wrap_call(self._vtk_obj.CopyPointsAndPointData, *my_args)
        return ret

    def initialize(self, *args):
        """
        V.initialize([int, int, int, int, int, int], [int, int, int, int,
            int, int], [int, int, int], bool)
        C++: void Initialize(int voi[6], int wholeExt[6],
            int sampleRate[3], bool includeBoundary)
        Initializes the index map.
        \param voi the extent of the volume of interest
        \param whole_ext the whole extent of the domain
        \param smaple_rate the sampling rate
        \param include_boundary indicates whether to include the boundary
            or not.
        """
        ret = self._wrap_call(self._vtk_obj.Initialize, *args)
        return ret

    def is_valid(self):
        """
        V.is_valid() -> bool
        C++: bool IsValid()
        Returns true if the helper is properly initialized.
        """
        ret = self._vtk_obj.IsValid()
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
            return super(ExtractStructuredGridHelper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractStructuredGridHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ExtractStructuredGridHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractStructuredGridHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


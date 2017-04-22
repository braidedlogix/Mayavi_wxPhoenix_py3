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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class MPASReader(UnstructuredGridAlgorithm):
    """
    MPASReader - Read an MPAS net_cdf file
    
    Superclass: UnstructuredGridAlgorithm
    
    This program reads an MPAS net_cdf data file to allow paraview to
    display a dual-grid sphere or latlon projection.  Also allows display
    of primal-grid sphere. The variables that have time dim are available
    to para_view.
    
    Assume all variables are of interest if they have dims (Time,
    n_cells|n_vertices, n_vert_levels, [n_tracers]). Does not deal with edge
    data.
    
    When using this reader, it is important that you remember to do the
    following:
    1.  When changing a selected variable, remember to select it also in
       the drop down box to "color by".  It doesn't color by that
       variable automatically.
    2.  When selecting multilayer sphere view, make layer thickness
       around 100,000.
    3.  When selecting multilayer lat/lon view, make layer thickness
       around 10.
    4.  Always click the -Z orientation after making a switch from
       lat/lon to sphere, from single to multilayer or changing
       thickness.
    5.  Be conservative on the number of changes you make before hitting
       Apply, since there may be bugs in this reader.  Just make one
       change and then hit Apply.
    
    Christine Ahrens (cahrens@lanl.gov) Version 1.3
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMPASReader, obj, update, **traits)
    
    use_dimensioned_array_names = tvtk_base.false_bool_trait(help=\
        """
        If true, dimension info is included in the array name. For
        instance, "tracers" will become "tracers(Time, n_cells, n_vert_levels,
        n_tracers)". This is useful for user-visible array selection, but
        is disabled by default for backwards compatibility.
        """
    )

    def _use_dimensioned_array_names_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseDimensionedArrayNames,
                        self.use_dimensioned_array_names_)

    def get_cell_array_status(self, *args):
        """
        V.get_cell_array_status(string) -> int
        C++: int GetCellArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetCellArrayStatus, *args)
        return ret

    def set_cell_array_status(self, *args):
        """
        V.set_cell_array_status(string, int)
        C++: void SetCellArrayStatus(const char *name, int status)"""
        ret = self._wrap_call(self._vtk_obj.SetCellArrayStatus, *args)
        return ret

    def get_dimension_current_index(self, *args):
        """
        V.get_dimension_current_index(string) -> int
        C++: int GetDimensionCurrentIndex(const std::string &dim)
        If the point/cell arrays contain dimensions other than Time,
        n_cells, or n_vertices, they are configured here. Use
        get_number_of_dimensions to get the number of arbitrary dimensions
        in the loaded arrays and get_dimension_name to retrieve the
        dimension names. get_dimension_size returns the number of values in
        the dimensions, and set/_get_dimension_current_index controls the
        value to fix a given dimension at when extracting slices of data.
        """
        ret = self._wrap_call(self._vtk_obj.GetDimensionCurrentIndex, *args)
        return ret

    def set_dimension_current_index(self, *args):
        """
        V.set_dimension_current_index(string, int)
        C++: void SetDimensionCurrentIndex(const std::string &dim,
            int idx)
        If the point/cell arrays contain dimensions other than Time,
        n_cells, or n_vertices, they are configured here. Use
        get_number_of_dimensions to get the number of arbitrary dimensions
        in the loaded arrays and get_dimension_name to retrieve the
        dimension names. get_dimension_size returns the number of values in
        the dimensions, and set/_get_dimension_current_index controls the
        value to fix a given dimension at when extracting slices of data.
        """
        ret = self._wrap_call(self._vtk_obj.SetDimensionCurrentIndex, *args)
        return ret

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of MPAS data file to read.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    is_atmosphere = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _is_atmosphere_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIsAtmosphere,
                        self.is_atmosphere)

    is_zero_centered = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _is_zero_centered_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIsZeroCentered,
                        self.is_zero_centered)

    layer_thickness = traits.Int(10000, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _layer_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLayerThickness,
                        self.layer_thickness)

    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    
    def _set_output(self, obj):
        old_val = self._get_output()
        self._wrap_call(self._vtk_obj.SetOutput, deref_vtk(obj))
        self.trait_property_changed('output', old_val, obj)
    output = traits.Property(_get_output, _set_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self, idx=None):
        """
        V.get_output() -> UnstructuredGrid
        C++: UnstructuredGrid *GetOutput()
        V.get_output(int) -> UnstructuredGrid
        C++: UnstructuredGrid *GetOutput(int index)
        Get the reader's output
        """
        if idx is None:
            return wrap_vtk(self._vtk_obj.GetOutput())
        else:
            return wrap_vtk(self._vtk_obj.GetOutput(idx))

    def set_output(self, obj):
        """
        V.set_output(DataObject)
        C++: virtual void SetOutput(DataObject *d)
        Get the output data object for a port on this algorithm.
        """
        old_val = self._get_output()
        self._wrap_call(self._vtk_obj.SetOutput, deref_vtk(obj))
        self.trait_property_changed('output', old_val, obj)

    def get_point_array_status(self, *args):
        """
        V.get_point_array_status(string) -> int
        C++: int GetPointArrayStatus(const char *name)
        The following methods allow selective reading of solutions
        fields. By default, ALL data fields on the nodes are read, but
        this can be modified.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayStatus, *args)
        return ret

    def set_point_array_status(self, *args):
        """
        V.set_point_array_status(string, int)
        C++: void SetPointArrayStatus(const char *name, int status)
        The following methods allow selective reading of solutions
        fields. By default, ALL data fields on the nodes are read, but
        this can be modified.
        """
        ret = self._wrap_call(self._vtk_obj.SetPointArrayStatus, *args)
        return ret

    project_lat_lon = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _project_lat_lon_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectLatLon,
                        self.project_lat_lon)

    show_multilayer_view = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _show_multilayer_view_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowMultilayerView,
                        self.show_multilayer_view)

    vertical_dimension = traits.String('nVertLevels', enter_set=True, auto_set=False, help=\
        """
        Get/Set the name to the dimension that identifies the vertical
        dimension. Defaults to "n_vert_levels".
        """
    )

    def _vertical_dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVerticalDimension,
                        self.vertical_dimension)

    vertical_level = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Convenience functon for setting/querying
        [_gs]et_dimension_current_index for the dimension returned by
        get_vertical_dimension.
        """
    )

    def _vertical_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVerticalLevel,
                        self.vertical_level)

    def _get_all_dimensions(self):
        return wrap_vtk(self._vtk_obj.GetAllDimensions())
    all_dimensions = traits.Property(_get_all_dimensions, help=\
        """
        If the point/cell arrays contain dimensions other than Time,
        n_cells, or n_vertices, they are configured here. Use
        get_number_of_dimensions to get the number of arbitrary dimensions
        in the loaded arrays and get_dimension_name to retrieve the
        dimension names. get_dimension_size returns the number of values in
        the dimensions, and set/_get_dimension_current_index controls the
        value to fix a given dimension at when extracting slices of data.
        """
    )

    def get_cell_array_name(self, *args):
        """
        V.get_cell_array_name(int) -> string
        C++: const char *GetCellArrayName(int index)"""
        ret = self._wrap_call(self._vtk_obj.GetCellArrayName, *args)
        return ret

    def _get_center_lon_range(self):
        return self._vtk_obj.GetCenterLonRange()
    center_lon_range = traits.Property(_get_center_lon_range, help=\
        """
        
        """
    )

    def get_dimension_name(self, *args):
        """
        V.get_dimension_name(int) -> string
        C++: std::string GetDimensionName(int idx)
        If the point/cell arrays contain dimensions other than Time,
        n_cells, or n_vertices, they are configured here. Use
        get_number_of_dimensions to get the number of arbitrary dimensions
        in the loaded arrays and get_dimension_name to retrieve the
        dimension names. get_dimension_size returns the number of values in
        the dimensions, and set/_get_dimension_current_index controls the
        value to fix a given dimension at when extracting slices of data.
        """
        ret = self._wrap_call(self._vtk_obj.GetDimensionName, *args)
        return ret

    def get_dimension_size(self, *args):
        """
        V.get_dimension_size(string) -> int
        C++: int GetDimensionSize(const std::string &dim)
        If the point/cell arrays contain dimensions other than Time,
        n_cells, or n_vertices, they are configured here. Use
        get_number_of_dimensions to get the number of arbitrary dimensions
        in the loaded arrays and get_dimension_name to retrieve the
        dimension names. get_dimension_size returns the number of values in
        the dimensions, and set/_get_dimension_current_index controls the
        value to fix a given dimension at when extracting slices of data.
        """
        ret = self._wrap_call(self._vtk_obj.GetDimensionSize, *args)
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
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_layer_thickness_range(self):
        return self._vtk_obj.GetLayerThicknessRange()
    layer_thickness_range = traits.Property(_get_layer_thickness_range, help=\
        """
        
        """
    )

    def _get_maximum_cells(self):
        return self._vtk_obj.GetMaximumCells()
    maximum_cells = traits.Property(_get_maximum_cells, help=\
        """
        Get the number of data cells
        """
    )

    def _get_maximum_points(self):
        return self._vtk_obj.GetMaximumPoints()
    maximum_points = traits.Property(_get_maximum_points, help=\
        """
        Get the number of points
        """
    )

    def _get_number_of_cell_arrays(self):
        return self._vtk_obj.GetNumberOfCellArrays()
    number_of_cell_arrays = traits.Property(_get_number_of_cell_arrays, help=\
        """
        
        """
    )

    def _get_number_of_cell_vars(self):
        return self._vtk_obj.GetNumberOfCellVars()
    number_of_cell_vars = traits.Property(_get_number_of_cell_vars, help=\
        """
        Get the number of data variables at the cell centers and points
        """
    )

    def _get_number_of_dimensions(self):
        return self._vtk_obj.GetNumberOfDimensions()
    number_of_dimensions = traits.Property(_get_number_of_dimensions, help=\
        """
        If the point/cell arrays contain dimensions other than Time,
        n_cells, or n_vertices, they are configured here. Use
        get_number_of_dimensions to get the number of arbitrary dimensions
        in the loaded arrays and get_dimension_name to retrieve the
        dimension names. get_dimension_size returns the number of values in
        the dimensions, and set/_get_dimension_current_index controls the
        value to fix a given dimension at when extracting slices of data.
        """
    )

    def _get_number_of_point_arrays(self):
        return self._vtk_obj.GetNumberOfPointArrays()
    number_of_point_arrays = traits.Property(_get_number_of_point_arrays, help=\
        """
        The following methods allow selective reading of solutions
        fields. By default, ALL data fields on the nodes are read, but
        this can be modified.
        """
    )

    def _get_number_of_point_vars(self):
        return self._vtk_obj.GetNumberOfPointVars()
    number_of_point_vars = traits.Property(_get_number_of_point_vars, help=\
        """
        Get the number of data variables at the cell centers and points
        """
    )

    def get_point_array_name(self, *args):
        """
        V.get_point_array_name(int) -> string
        C++: const char *GetPointArrayName(int index)
        The following methods allow selective reading of solutions
        fields. By default, ALL data fields on the nodes are read, but
        this can be modified.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayName, *args)
        return ret

    def _get_vertical_level_range(self):
        return self._vtk_obj.GetVerticalLevelRange()
    vertical_level_range = traits.Property(_get_vertical_level_range, help=\
        """
        
        """
    )

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: static int CanReadFile(const char *filename)
        Returns true if the given file can be read.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    def disable_all_cell_arrays(self):
        """
        V.disable_all_cell_arrays()
        C++: void DisableAllCellArrays()"""
        ret = self._vtk_obj.DisableAllCellArrays()
        return ret
        

    def disable_all_point_arrays(self):
        """
        V.disable_all_point_arrays()
        C++: void DisableAllPointArrays()
        The following methods allow selective reading of solutions
        fields. By default, ALL data fields on the nodes are read, but
        this can be modified.
        """
        ret = self._vtk_obj.DisableAllPointArrays()
        return ret
        

    def enable_all_cell_arrays(self):
        """
        V.enable_all_cell_arrays()
        C++: void EnableAllCellArrays()"""
        ret = self._vtk_obj.EnableAllCellArrays()
        return ret
        

    def enable_all_point_arrays(self):
        """
        V.enable_all_point_arrays()
        C++: void EnableAllPointArrays()
        The following methods allow selective reading of solutions
        fields. By default, ALL data fields on the nodes are read, but
        this can be modified.
        """
        ret = self._vtk_obj.EnableAllPointArrays()
        return ret
        

    def set_center_lon(self, *args):
        """
        V.set_center_lon(int)
        C++: void SetCenterLon(int val)"""
        ret = self._wrap_call(self._vtk_obj.SetCenterLon, *args)
        return ret

    _updateable_traits_ = \
    (('use_dimensioned_array_names', 'GetUseDimensionedArrayNames'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('is_atmosphere', 'GetIsAtmosphere'),
    ('is_zero_centered', 'GetIsZeroCentered'), ('layer_thickness',
    'GetLayerThickness'), ('project_lat_lon', 'GetProjectLatLon'),
    ('show_multilayer_view', 'GetShowMultilayerView'),
    ('vertical_dimension', 'GetVerticalDimension'), ('vertical_level',
    'GetVerticalLevel'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'use_dimensioned_array_names', 'file_name',
    'is_atmosphere', 'is_zero_centered', 'layer_thickness',
    'progress_text', 'project_lat_lon', 'show_multilayer_view',
    'vertical_dimension', 'vertical_level'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MPASReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MPASReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_dimensioned_array_names'], [], ['file_name',
            'is_atmosphere', 'is_zero_centered', 'layer_thickness',
            'project_lat_lon', 'show_multilayer_view', 'vertical_dimension',
            'vertical_level']),
            title='Edit MPASReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MPASReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


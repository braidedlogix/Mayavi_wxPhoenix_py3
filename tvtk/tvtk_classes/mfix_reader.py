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


class MFIXReader(UnstructuredGridAlgorithm):
    """
    MFIXReader - reads a dataset in MFIX file format
    
    Superclass: UnstructuredGridAlgorithm
    
    MFIXReader creates an unstructured grid dataset. It reads a
    restart file and a set of sp files.  The restart file contains the
    mesh information.  MFIX meshes are either cylindrical or rectilinear,
    but this reader will convert them to an unstructured grid.  The sp
    files contain transient data for the cells.  Each sp file has one or
    more variables stored inside it.
    
    @par Thanks: Thanks to Phil Nicoletti and Brian Dotson at the
    National Energy Technology Laboratory who developed this class.
    Please address all comments to Brian Dotson (brian.dotson
    
    etl.doe.gov)
    
    @sa
    GAMBITReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMFIXReader, obj, update, **traits)
    
    def get_cell_array_status(self, *args):
        """
        V.get_cell_array_status(string) -> int
        C++: int GetCellArrayStatus(const char *name)
        Get/Set whether the cell array with the given name is to be read.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellArrayStatus, *args)
        return ret

    def set_cell_array_status(self, *args):
        """
        V.set_cell_array_status(string, int)
        C++: void SetCellArrayStatus(const char *name, int status)
        Get/Set whether the cell array with the given name is to be read.
        """
        ret = self._wrap_call(self._vtk_obj.SetCellArrayStatus, *args)
        return ret

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the file name of the MFIX Restart data file to read.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    time_step = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Which time_step to read.
        """
    )

    def _time_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStep,
                        self.time_step)

    time_step_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _time_step_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStepRange,
                        self.time_step_range)

    def get_cell_array_name(self, *args):
        """
        V.get_cell_array_name(int) -> string
        C++: const char *GetCellArrayName(int index)
        Get the name of the  cell array with the given index in the
        input.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellArrayName, *args)
        return ret

    def get_cell_data_range(self, *args):
        """
        V.get_cell_data_range(int, [float, ...], [float, ...])
        C++: void GetCellDataRange(int cellComp, float *min, float *max)
        Get the range of cell data.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellDataRange, *args)
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

    def _get_number_of_cell_arrays(self):
        return self._vtk_obj.GetNumberOfCellArrays()
    number_of_cell_arrays = traits.Property(_get_number_of_cell_arrays, help=\
        """
        Get the number of cell arrays available in the input.
        """
    )

    def _get_number_of_cell_fields(self):
        return self._vtk_obj.GetNumberOfCellFields()
    number_of_cell_fields = traits.Property(_get_number_of_cell_fields, help=\
        """
        Get the number of data components at the nodes and cells.
        """
    )

    def _get_number_of_cells(self):
        return self._vtk_obj.GetNumberOfCells()
    number_of_cells = traits.Property(_get_number_of_cells, help=\
        """
        Get the total number of cells. The number of cells is only valid
        after a successful read of the data file is performed.
        """
    )

    def _get_number_of_points(self):
        return self._vtk_obj.GetNumberOfPoints()
    number_of_points = traits.Property(_get_number_of_points, help=\
        """
        Get the total number of nodes. The number of nodes is only valid
        after a successful read of the data file is performed.
        """
    )

    def _get_number_of_time_steps(self):
        return self._vtk_obj.GetNumberOfTimeSteps()
    number_of_time_steps = traits.Property(_get_number_of_time_steps, help=\
        """
        Returns the number of timesteps.
        """
    )

    def disable_all_cell_arrays(self):
        """
        V.disable_all_cell_arrays()
        C++: void DisableAllCellArrays()
        Turn on/off all cell arrays.
        """
        ret = self._vtk_obj.DisableAllCellArrays()
        return ret
        

    def enable_all_cell_arrays(self):
        """
        V.enable_all_cell_arrays()
        C++: void EnableAllCellArrays()
        Turn on/off all cell arrays.
        """
        ret = self._vtk_obj.EnableAllCellArrays()
        return ret
        

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('time_step', 'GetTimeStep'), ('time_step_range',
    'GetTimeStepRange'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'file_name', 'progress_text', 'time_step',
    'time_step_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MFIXReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MFIXReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['file_name', 'time_step', 'time_step_range']),
            title='Edit MFIXReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MFIXReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class AVSucdReader(UnstructuredGridAlgorithm):
    """
    AVSucdReader - reads a dataset in AVS "UCD" format
    
    Superclass: UnstructuredGridAlgorithm
    
    AVSucdReader creates an unstructured grid dataset. It reads binary
    or ASCII files stored in UCD format, with optional data stored at the
    nodes or at the cells of the model. A cell-based fielddata stores the
    material id. The class can automatically detect the endian-ness of
    the binary files.
    
    @par Thanks: Thanks to Guenole Harel and Emmanuel Colin (Supelec
    engineering school, France) and Jean M. Favre (CSCS, Switzerland) who
    co-developed this class. Thanks to Isabelle Surin (isabelle.surin at
    cea.fr, CEA-DAM, France) who supervised the internship of the first
    two authors. Thanks to Daniel Aguilera (daniel.aguilera at cea.fr,
    CEA-DAM, France) who contributed code and advice. Please address all
    comments to Jean Favre (jfavre at cscs.ch)
    
    @sa
    GAMBITReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAVSucdReader, obj, update, **traits)
    
    binary_file = tvtk_base.false_bool_trait(help=\
        """
        Is the file to be read written in binary format (as opposed to
        ascii).
        """
    )

    def _binary_file_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBinaryFile,
                        self.binary_file_)

    byte_order = traits.Trait('big_endian',
    tvtk_base.TraitRevPrefixMap({'big_endian': 0, 'little_endian': 1}), help=\
        """
        
        """
    )

    def _byte_order_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetByteOrder,
                        self.byte_order_)

    def get_cell_array_status(self, *args):
        """
        V.get_cell_array_status(string) -> int
        C++: int GetCellArrayStatus(const char *name)
        The following methods allow selective reading of solutions
        fields.  by default, ALL data fields are the nodes and cells are
        read, but this can be modified.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellArrayStatus, *args)
        return ret

    def set_cell_array_status(self, *args):
        """
        V.set_cell_array_status(string, int)
        C++: void SetCellArrayStatus(const char *name, int status)
        The following methods allow selective reading of solutions
        fields.  by default, ALL data fields are the nodes and cells are
        read, but this can be modified.
        """
        ret = self._wrap_call(self._vtk_obj.SetCellArrayStatus, *args)
        return ret

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of AVS UCD datafile to read
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def get_point_array_status(self, *args):
        """
        V.get_point_array_status(string) -> int
        C++: int GetPointArrayStatus(const char *name)
        The following methods allow selective reading of solutions
        fields.  by default, ALL data fields are the nodes and cells are
        read, but this can be modified.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayStatus, *args)
        return ret

    def set_point_array_status(self, *args):
        """
        V.set_point_array_status(string, int)
        C++: void SetPointArrayStatus(const char *name, int status)
        The following methods allow selective reading of solutions
        fields.  by default, ALL data fields are the nodes and cells are
        read, but this can be modified.
        """
        ret = self._wrap_call(self._vtk_obj.SetPointArrayStatus, *args)
        return ret

    def get_cell_array_name(self, *args):
        """
        V.get_cell_array_name(int) -> string
        C++: const char *GetCellArrayName(int index)
        The following methods allow selective reading of solutions
        fields.  by default, ALL data fields are the nodes and cells are
        read, but this can be modified.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellArrayName, *args)
        return ret

    def get_cell_data_range(self, *args):
        """
        V.get_cell_data_range(int, int, [float, ...], [float, ...])
        C++: void GetCellDataRange(int cellComp, int index, float *min,
            float *max)"""
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

    def get_node_data_range(self, *args):
        """
        V.get_node_data_range(int, int, [float, ...], [float, ...])
        C++: void GetNodeDataRange(int nodeComp, int index, float *min,
            float *max)"""
        ret = self._wrap_call(self._vtk_obj.GetNodeDataRange, *args)
        return ret

    def _get_number_of_cell_arrays(self):
        return self._vtk_obj.GetNumberOfCellArrays()
    number_of_cell_arrays = traits.Property(_get_number_of_cell_arrays, help=\
        """
        The following methods allow selective reading of solutions
        fields.  by default, ALL data fields are the nodes and cells are
        read, but this can be modified.
        """
    )

    def _get_number_of_cell_components(self):
        return self._vtk_obj.GetNumberOfCellComponents()
    number_of_cell_components = traits.Property(_get_number_of_cell_components, help=\
        """
        Get the number of data components at the nodes and cells.
        """
    )

    def _get_number_of_cell_fields(self):
        return self._vtk_obj.GetNumberOfCellFields()
    number_of_cell_fields = traits.Property(_get_number_of_cell_fields, help=\
        """
        Get the number of data fields at the cell centers.
        """
    )

    def _get_number_of_cells(self):
        return self._vtk_obj.GetNumberOfCells()
    number_of_cells = traits.Property(_get_number_of_cells, help=\
        """
        Get the total number of cells.
        """
    )

    def _get_number_of_fields(self):
        return self._vtk_obj.GetNumberOfFields()
    number_of_fields = traits.Property(_get_number_of_fields, help=\
        """
        Get the number of data fields for the model. Unused because VTK
        has no methods for it.
        """
    )

    def _get_number_of_node_components(self):
        return self._vtk_obj.GetNumberOfNodeComponents()
    number_of_node_components = traits.Property(_get_number_of_node_components, help=\
        """
        Get the number of data components at the nodes and cells.
        """
    )

    def _get_number_of_node_fields(self):
        return self._vtk_obj.GetNumberOfNodeFields()
    number_of_node_fields = traits.Property(_get_number_of_node_fields, help=\
        """
        Get the number of data fields at the nodes.
        """
    )

    def _get_number_of_nodes(self):
        return self._vtk_obj.GetNumberOfNodes()
    number_of_nodes = traits.Property(_get_number_of_nodes, help=\
        """
        Get the total number of nodes.
        """
    )

    def _get_number_of_point_arrays(self):
        return self._vtk_obj.GetNumberOfPointArrays()
    number_of_point_arrays = traits.Property(_get_number_of_point_arrays, help=\
        """
        The following methods allow selective reading of solutions
        fields.  by default, ALL data fields are the nodes and cells are
        read, but this can be modified.
        """
    )

    def get_point_array_name(self, *args):
        """
        V.get_point_array_name(int) -> string
        C++: const char *GetPointArrayName(int index)
        The following methods allow selective reading of solutions
        fields.  by default, ALL data fields are the nodes and cells are
        read, but this can be modified.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayName, *args)
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
        C++: void DisableAllPointArrays()"""
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
        C++: void EnableAllPointArrays()"""
        ret = self._vtk_obj.EnableAllPointArrays()
        return ret
        

    _updateable_traits_ = \
    (('binary_file', 'GetBinaryFile'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('byte_order', 'GetByteOrder'),
    ('file_name', 'GetFileName'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'binary_file', 'debug', 'global_warning_display',
    'release_data_flag', 'byte_order', 'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AVSucdReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AVSucdReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['binary_file'], ['byte_order'], ['file_name']),
            title='Edit AVSucdReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AVSucdReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


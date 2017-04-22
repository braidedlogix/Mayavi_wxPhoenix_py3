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

from tvtk.tvtk_classes.data_reader import DataReader


class UnstructuredGridReader(DataReader):
    """
    UnstructuredGridReader - read vtk unstructured grid data file
    
    Superclass: DataReader
    
    UnstructuredGridReader is a source object that reads ASCII or
    binary unstructured grid data files in vtk format. (see text for
    format details). The output of this reader is a single
    UnstructuredGrid data object. The superclass of this class,
    DataReader, provides many methods for controlling the reading of
    the data file, see DataReader for more information.
    @warning
    Binary files written on one system may not be readable on other
    systems.
    @sa
    UnstructuredGrid DataReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGridReader, obj, update, **traits)
    
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
        C++: UnstructuredGrid *GetOutput(int idx)
        Get the output of this reader.
        """
        if idx is None:
            return wrap_vtk(self._vtk_obj.GetOutput())
        else:
            return wrap_vtk(self._vtk_obj.GetOutput(idx))

    def set_output(self, obj):
        """
        V.set_output(UnstructuredGrid)
        C++: void SetOutput(UnstructuredGrid *output)
        Get the output of this reader.
        """
        old_val = self._get_output()
        self._wrap_call(self._vtk_obj.SetOutput, deref_vtk(obj))
        self.trait_property_changed('output', old_val, obj)

    _updateable_traits_ = \
    (('read_all_color_scalars', 'GetReadAllColorScalars'),
    ('read_all_fields', 'GetReadAllFields'), ('read_all_normals',
    'GetReadAllNormals'), ('read_all_scalars', 'GetReadAllScalars'),
    ('read_all_t_coords', 'GetReadAllTCoords'), ('read_all_tensors',
    'GetReadAllTensors'), ('read_all_vectors', 'GetReadAllVectors'),
    ('read_from_input_string', 'GetReadFromInputString'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('field_data_name', 'GetFieldDataName'), ('file_name', 'GetFileName'),
    ('input_string', 'GetInputString'), ('lookup_table_name',
    'GetLookupTableName'), ('normals_name', 'GetNormalsName'),
    ('scalars_name', 'GetScalarsName'), ('t_coords_name',
    'GetTCoordsName'), ('tensors_name', 'GetTensorsName'),
    ('vectors_name', 'GetVectorsName'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'read_all_color_scalars', 'read_all_fields', 'read_all_normals',
    'read_all_scalars', 'read_all_t_coords', 'read_all_tensors',
    'read_all_vectors', 'read_from_input_string', 'release_data_flag',
    'field_data_name', 'file_name', 'input_string', 'lookup_table_name',
    'normals_name', 'progress_text', 'scalars_name', 't_coords_name',
    'tensors_name', 'vectors_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UnstructuredGridReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGridReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['read_all_color_scalars', 'read_all_fields',
            'read_all_normals', 'read_all_scalars', 'read_all_t_coords',
            'read_all_tensors', 'read_all_vectors', 'read_from_input_string'], [],
            ['field_data_name', 'file_name', 'input_string', 'lookup_table_name',
            'normals_name', 'scalars_name', 't_coords_name', 'tensors_name',
            'vectors_name']),
            title='Edit UnstructuredGridReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGridReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


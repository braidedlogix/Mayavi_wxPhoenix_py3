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

from tvtk.tvtk_classes.data_writer import DataWriter


class StructuredGridWriter(DataWriter):
    """
    StructuredGridWriter - write vtk structured grid data file
    
    Superclass: DataWriter
    
    StructuredGridWriter is a source object that writes ASCII or
    binary structured grid data files in vtk format. See text for format
    details.
    
    @warning
    Binary files written on one system may not be readable on other
    systems.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStructuredGridWriter, obj, update, **traits)
    
    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> StructuredGrid
        C++: StructuredGrid *GetInput()
        V.get_input(int) -> StructuredGrid
        C++: StructuredGrid *GetInput(int port)
        Get the input to this writer.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('write_array_meta_data', 'GetWriteArrayMetaData'),
    ('write_to_output_string', 'GetWriteToOutputString'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_type',
    'GetFileType'), ('edge_flags_name', 'GetEdgeFlagsName'),
    ('field_data_name', 'GetFieldDataName'), ('file_name', 'GetFileName'),
    ('global_ids_name', 'GetGlobalIdsName'), ('header', 'GetHeader'),
    ('lookup_table_name', 'GetLookupTableName'), ('normals_name',
    'GetNormalsName'), ('pedigree_ids_name', 'GetPedigreeIdsName'),
    ('scalars_name', 'GetScalarsName'), ('t_coords_name',
    'GetTCoordsName'), ('tensors_name', 'GetTensorsName'),
    ('vectors_name', 'GetVectorsName'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'write_array_meta_data',
    'write_to_output_string', 'file_type', 'edge_flags_name',
    'field_data_name', 'file_name', 'global_ids_name', 'header',
    'lookup_table_name', 'normals_name', 'pedigree_ids_name',
    'progress_text', 'scalars_name', 't_coords_name', 'tensors_name',
    'vectors_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StructuredGridWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StructuredGridWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['write_array_meta_data', 'write_to_output_string'],
            ['file_type'], ['edge_flags_name', 'field_data_name', 'file_name',
            'global_ids_name', 'header', 'lookup_table_name', 'normals_name',
            'pedigree_ids_name', 'scalars_name', 't_coords_name', 'tensors_name',
            'vectors_name']),
            title='Edit StructuredGridWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StructuredGridWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


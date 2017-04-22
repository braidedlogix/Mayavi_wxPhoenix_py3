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

from tvtk.tvtk_classes.writer import Writer


class DataWriter(Writer):
    """
    DataWriter - helper class for objects that write vtk data files
    
    Superclass: Writer
    
    DataWriter is a helper class that opens and writes the vtk header
    and point data (e.g., scalars, vectors, normals, etc.) from a vtk
    data file. See text for various formats.
    
    @sa
    DataSetWriter PolyDataWriter StructuredGridWriter
    StructuredPointsWriter UnstructuredGridWriter
    FieldDataWriter RectilinearGridWriter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataWriter, obj, update, **traits)
    
    write_array_meta_data = tvtk_base.true_bool_trait(help=\
        """
        If true, Information objects attached to arrays and array
        component nameswill be written to the output. Default is true.
        """
    )

    def _write_array_meta_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteArrayMetaData,
                        self.write_array_meta_data_)

    write_to_output_string = tvtk_base.false_bool_trait(help=\
        """
        Enable writing to an output_string instead of the default, a file.
        """
    )

    def _write_to_output_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteToOutputString,
                        self.write_to_output_string_)

    file_type = traits.Trait('ascii',
    tvtk_base.TraitRevPrefixMap({'ascii': 1, 'binary': 2}), help=\
        """
        Specify file type (ASCII or BINARY) for vtk data file.
        """
    )

    def _file_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileType,
                        self.file_type_)

    edge_flags_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the edge flags data. If not specified, uses
        default name "edge_flags".
        """
    )

    def _edge_flags_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeFlagsName,
                        self.edge_flags_name)

    field_data_name = traits.String('FieldData', enter_set=True, auto_set=False, help=\
        """
        Give a name to the field data. If not specified, uses default
        name "field".
        """
    )

    def _field_data_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldDataName,
                        self.field_data_name)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of vtk polygon data file to write.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    global_ids_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the global ids data. If not specified, uses
        default name "global_ids".
        """
    )

    def _global_ids_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobalIdsName,
                        self.global_ids_name)

    header = traits.String('vtk output', enter_set=True, auto_set=False, help=\
        """
        Specify the header for the vtk data file.
        """
    )

    def _header_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeader,
                        self.header)

    lookup_table_name = traits.String('lookup_table', enter_set=True, auto_set=False, help=\
        """
        Give a name to the lookup table. If not specified, uses default
        name "lookup_table".
        """
    )

    def _lookup_table_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLookupTableName,
                        self.lookup_table_name)

    normals_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the normals data. If not specified, uses default
        name "normals".
        """
    )

    def _normals_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalsName,
                        self.normals_name)

    pedigree_ids_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the pedigree ids data. If not specified, uses
        default name "pedigree_ids".
        """
    )

    def _pedigree_ids_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPedigreeIdsName,
                        self.pedigree_ids_name)

    scalars_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the scalar data. If not specified, uses default
        name "scalars".
        """
    )

    def _scalars_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarsName,
                        self.scalars_name)

    t_coords_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the texture coordinates data. If not specified,
        uses default name "texture_coords".
        """
    )

    def _t_coords_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTCoordsName,
                        self.t_coords_name)

    tensors_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the tensors data. If not specified, uses default
        name "tensors".
        """
    )

    def _tensors_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTensorsName,
                        self.tensors_name)

    vectors_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Give a name to the vector data. If not specified, uses default
        name "vectors".
        """
    )

    def _vectors_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorsName,
                        self.vectors_name)

    def _get_binary_output_string(self):
        return self._vtk_obj.GetBinaryOutputString()
    binary_output_string = traits.Property(_get_binary_output_string, help=\
        """
        When write_to_output_string in on, then a string is allocated,
        written to, and can be retrieved with these methods.  The string
        is deleted during the next call to write ...
        """
    )

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

    def _get_output_std_string(self):
        return self._vtk_obj.GetOutputStdString()
    output_std_string = traits.Property(_get_output_std_string, help=\
        """
        When write_to_output_string is on, this method returns a copy of the
        output string in a StdString.
        """
    )

    def _get_output_string(self):
        return self._vtk_obj.GetOutputString()
    output_string = traits.Property(_get_output_string, help=\
        """
        When write_to_output_string in on, then a string is allocated,
        written to, and can be retrieved with these methods.  The string
        is deleted during the next call to write ...
        """
    )

    def _get_output_string_length(self):
        return self._vtk_obj.GetOutputStringLength()
    output_string_length = traits.Property(_get_output_string_length, help=\
        """
        When write_to_output_string in on, then a string is allocated,
        written to, and can be retrieved with these methods.  The string
        is deleted during the next call to write ...
        """
    )

    def register_and_get_output_string(self):
        """
        V.register_and_get_output_string() -> string
        C++: char *RegisterAndGetOutputString()
        This convenience method returns the string, sets the IVAR to
        NULL, so that the user is responsible for deleting the string. I
        am not sure what the name should be, so it may change in the
        future.
        """
        ret = self._vtk_obj.RegisterAndGetOutputString()
        return ret
        

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
            return super(DataWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DataWriter properties', scrollable=True, resizable=True,
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
            title='Edit DataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


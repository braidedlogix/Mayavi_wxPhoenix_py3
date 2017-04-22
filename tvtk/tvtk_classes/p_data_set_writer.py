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

from tvtk.tvtk_classes.data_set_writer import DataSetWriter


class PDataSetWriter(DataSetWriter):
    """
    PDataSetWriter - Manages writing pieces of a data set.
    
    Superclass: DataSetWriter
    
    PDataSetWriter will write a piece of a file, and will also create
    a metadata file that lists all of the files in a data set.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPDataSetWriter, obj, update, **traits)
    
    use_relative_file_names = tvtk_base.true_bool_trait(help=\
        """
        This flag determines whether to use absolute paths for the piece
        files. By default the pieces are put in the main directory, and
        the piece file names in the meta data pvtk file are relative to
        this directory. This should make moving the whole lot to another
        directory, an easier task.
        """
    )

    def _use_relative_file_names_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseRelativeFileNames,
                        self.use_relative_file_names_)

    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        Controller used to communicate data type of blocks. By default,
        the global controller is used. If you want another controller to
        be used, set it with this.
        """
    )

    end_piece = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This is the range of pieces that that this writer is responsible
        for writing.  All pieces must be written by some process.  The
        process that writes piece 0 also writes the pvtk file that lists
        all the piece file names.
        """
    )

    def _end_piece_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndPiece,
                        self.end_piece)

    file_pattern = traits.String('%s.%d.vtk', enter_set=True, auto_set=False, help=\
        """
        This file pattern uses the file name and piece number to contruct
        a file name for the piece file.
        """
    )

    def _file_pattern_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilePattern,
                        self.file_pattern)

    ghost_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Extra ghost cells will be written out to each piece file if this
        value is larger than 0.
        """
    )

    def _ghost_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGhostLevel,
                        self.ghost_level)

    number_of_pieces = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        This is how many pieces the whole data set will be divided into.
        """
    )

    def _number_of_pieces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPieces,
                        self.number_of_pieces)

    start_piece = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This is the range of pieces that that this writer is responsible
        for writing.  All pieces must be written by some process.  The
        process that writes piece 0 also writes the pvtk file that lists
        all the piece file names.
        """
    )

    def _start_piece_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartPiece,
                        self.start_piece)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataSet
        C++: DataSet *GetInput()
        V.get_input(int) -> DataSet
        C++: DataSet *GetInput(int port)
        Get the input to this writer.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('use_relative_file_names', 'GetUseRelativeFileNames'),
    ('write_array_meta_data', 'GetWriteArrayMetaData'),
    ('write_to_output_string', 'GetWriteToOutputString'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_type',
    'GetFileType'), ('end_piece', 'GetEndPiece'), ('file_pattern',
    'GetFilePattern'), ('ghost_level', 'GetGhostLevel'),
    ('number_of_pieces', 'GetNumberOfPieces'), ('start_piece',
    'GetStartPiece'), ('edge_flags_name', 'GetEdgeFlagsName'),
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
    'release_data_flag', 'use_relative_file_names',
    'write_array_meta_data', 'write_to_output_string', 'file_type',
    'edge_flags_name', 'end_piece', 'field_data_name', 'file_name',
    'file_pattern', 'ghost_level', 'global_ids_name', 'header',
    'lookup_table_name', 'normals_name', 'number_of_pieces',
    'pedigree_ids_name', 'progress_text', 'scalars_name', 'start_piece',
    't_coords_name', 'tensors_name', 'vectors_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PDataSetWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PDataSetWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_relative_file_names', 'write_array_meta_data',
            'write_to_output_string'], ['file_type'], ['edge_flags_name',
            'end_piece', 'field_data_name', 'file_name', 'file_pattern',
            'ghost_level', 'global_ids_name', 'header', 'lookup_table_name',
            'normals_name', 'number_of_pieces', 'pedigree_ids_name',
            'scalars_name', 'start_piece', 't_coords_name', 'tensors_name',
            'vectors_name']),
            title='Edit PDataSetWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PDataSetWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


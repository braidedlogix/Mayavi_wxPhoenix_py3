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

from tvtk.tvtk_classes.generic_en_sight_reader import GenericEnSightReader


class EnSightMasterServerReader(GenericEnSightReader):
    """
    EnSightMasterServerReader - reader for compund en_sight files
    
    Superclass: GenericEnSightReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEnSightMasterServerReader, obj, update, **traits)
    
    current_piece = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set or get the current piece.
        """
    )

    def _current_piece_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCurrentPiece,
                        self.current_piece)

    def _get_piece_case_file_name(self):
        return self._vtk_obj.GetPieceCaseFileName()
    piece_case_file_name = traits.Property(_get_piece_case_file_name, help=\
        """
        Get the file name that will be read.
        """
    )

    def determine_file_name(self, *args):
        """
        V.determine_file_name(int) -> int
        C++: int DetermineFileName(int piece)
        Determine which file should be read for piece
        """
        ret = self._wrap_call(self._vtk_obj.DetermineFileName, *args)
        return ret

    _updateable_traits_ = \
    (('particle_coordinates_by_index', 'GetParticleCoordinatesByIndex'),
    ('read_all_variables', 'GetReadAllVariables'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('byte_order', 'GetByteOrder'),
    ('current_piece', 'GetCurrentPiece'), ('case_file_name',
    'GetCaseFileName'), ('file_path', 'GetFilePath'), ('time_value',
    'GetTimeValue'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'particle_coordinates_by_index', 'read_all_variables',
    'release_data_flag', 'byte_order', 'case_file_name', 'current_piece',
    'file_path', 'progress_text', 'time_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EnSightMasterServerReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit EnSightMasterServerReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['particle_coordinates_by_index', 'read_all_variables'],
            ['byte_order'], ['case_file_name', 'current_piece', 'file_path',
            'time_value']),
            title='Edit EnSightMasterServerReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EnSightMasterServerReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


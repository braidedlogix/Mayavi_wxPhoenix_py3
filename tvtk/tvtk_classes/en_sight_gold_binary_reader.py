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

from tvtk.tvtk_classes.en_sight_reader import EnSightReader


class EnSightGoldBinaryReader(EnSightReader):
    """
    EnSightGoldBinaryReader - class to read binary en_sight Gold files
    
    Superclass: EnSightReader
    
    EnSightGoldBinaryReader is a class to read en_sight Gold files into
    vtk. Because the different parts of the en_sight data can be of
    various data types, this reader produces multiple outputs, one per
    part in the input file. All variable information is being stored in
    field data.  The descriptions listed in the case file are used as the
    array names in the field data. For complex vector variables, the
    description is appended with _r (for the array of real values) and _i
    (for the array if imaginary values).  Complex scalar variables are
    stored as a single array with 2 components, real and imaginary,
    listed in that order.
    @warning
    You must manually call Update on this reader and then connect the
    rest of the pipeline because (due to the nature of the file format)
    it is not possible to know ahead of time how many outputs you will
    have or what types they will be. This reader can only handle static
    en_sight datasets (both static geometry and variables).@par Thanks:
    Thanks to Yvan Fournier for providing the code to support nfaced
    elements.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEnSightGoldBinaryReader, obj, update, **traits)
    
    _updateable_traits_ = \
    (('particle_coordinates_by_index', 'GetParticleCoordinatesByIndex'),
    ('read_all_variables', 'GetReadAllVariables'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('byte_order', 'GetByteOrder'),
    ('case_file_name', 'GetCaseFileName'), ('file_path', 'GetFilePath'),
    ('time_value', 'GetTimeValue'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'particle_coordinates_by_index', 'read_all_variables',
    'release_data_flag', 'byte_order', 'case_file_name', 'file_path',
    'progress_text', 'time_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EnSightGoldBinaryReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit EnSightGoldBinaryReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['particle_coordinates_by_index', 'read_all_variables'],
            ['byte_order'], ['case_file_name', 'file_path', 'time_value']),
            title='Edit EnSightGoldBinaryReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EnSightGoldBinaryReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


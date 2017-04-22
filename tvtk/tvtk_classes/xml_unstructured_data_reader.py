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

from tvtk.tvtk_classes.xml_data_reader import XMLDataReader


class XMLUnstructuredDataReader(XMLDataReader):
    """
    XMLUnstructuredDataReader - Superclass for unstructured data XML
    readers.
    
    Superclass: XMLDataReader
    
    XMLUnstructuredDataReader provides functionality common to all
    unstructured data format readers.
    
    @sa
    XMLPolyDataReader XMLUnstructuredGridReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLUnstructuredDataReader, obj, update, **traits)
    
    def _get_number_of_pieces(self):
        return self._vtk_obj.GetNumberOfPieces()
    number_of_pieces = traits.Property(_get_number_of_pieces, help=\
        """
        Get the number of pieces in the file
        """
    )

    def setup_update_extent(self, *args):
        """
        V.setup_update_extent(int, int, int)
        C++: void SetupUpdateExtent(int piece, int numberOfPieces,
            int ghostLevel)
        Setup the reader as if the given update extent were requested by
        its output.  This can be used after an update_information to
        validate get_number_of_points() and get_number_of_cells() without
        actually reading data.
        """
        ret = self._wrap_call(self._vtk_obj.SetupUpdateExtent, *args)
        return ret

    _updateable_traits_ = \
    (('read_from_input_string', 'GetReadFromInputString'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('time_step', 'GetTimeStep'), ('time_step_range',
    'GetTimeStepRange'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'read_from_input_string', 'release_data_flag', 'file_name',
    'progress_text', 'time_step', 'time_step_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLUnstructuredDataReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLUnstructuredDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['read_from_input_string'], [], ['file_name', 'time_step',
            'time_step_range']),
            title='Edit XMLUnstructuredDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLUnstructuredDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.xml_unstructured_data_reader import XMLUnstructuredDataReader


class XMLPolyDataReader(XMLUnstructuredDataReader):
    """
    XMLPolyDataReader - Read VTK XML poly_data files.
    
    Superclass: XMLUnstructuredDataReader
    
    XMLPolyDataReader reads the VTK XML poly_data file format.  One
    polygonal data file can be read to produce one output.  Streaming is
    supported.  The standard extension for this reader's file format is
    "vtp".  This reader is also used to read a single piece of the
    parallel file format.
    
    @sa
    XMLPPolyDataReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLPolyDataReader, obj, update, **traits)
    
    def _get_number_of_lines(self):
        return self._vtk_obj.GetNumberOfLines()
    number_of_lines = traits.Property(_get_number_of_lines, help=\
        """
        Get the number of verts/lines/strips/polys in the output.
        """
    )

    def _get_number_of_polys(self):
        return self._vtk_obj.GetNumberOfPolys()
    number_of_polys = traits.Property(_get_number_of_polys, help=\
        """
        Get the number of verts/lines/strips/polys in the output.
        """
    )

    def _get_number_of_strips(self):
        return self._vtk_obj.GetNumberOfStrips()
    number_of_strips = traits.Property(_get_number_of_strips, help=\
        """
        Get the number of verts/lines/strips/polys in the output.
        """
    )

    def _get_number_of_verts(self):
        return self._vtk_obj.GetNumberOfVerts()
    number_of_verts = traits.Property(_get_number_of_verts, help=\
        """
        Get the number of verts/lines/strips/polys in the output.
        """
    )

    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    output = traits.Property(_get_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self, idx=None):
        """
        V.get_output() -> PolyData
        C++: PolyData *GetOutput()
        V.get_output(int) -> PolyData
        C++: PolyData *GetOutput(int idx)
        Get the reader's output.
        """
        if idx is None:
            return wrap_vtk(self._vtk_obj.GetOutput())
        else:
            return wrap_vtk(self._vtk_obj.GetOutput(idx))

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
            return super(XMLPolyDataReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLPolyDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['read_from_input_string'], [], ['file_name', 'time_step',
            'time_step_range']),
            title='Edit XMLPolyDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLPolyDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.xml_uniform_grid_amr_reader import XMLUniformGridAMRReader


class XMLHierarchicalBoxDataReader(XMLUniformGridAMRReader):
    """
    XMLHierarchicalBoxDataReader - Reader for hierarchical datasets
    (for backwards compatibility).
    
    Superclass: XMLUniformGridAMRReader
    
    XMLHierarchicalBoxDataReader is an empty subclass of
    XMLUniformGridAMRReader. This is only for backwards compatibility.
    Newer code should simply use XMLUniformGridAMRReader.
    
    @warning
    The reader supports reading v1.1 and above. For older versions, use
    XMLHierarchicalBoxDataFileConverter.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLHierarchicalBoxDataReader, obj, update, **traits)
    
    _updateable_traits_ = \
    (('read_from_input_string', 'GetReadFromInputString'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_levels_to_read_by_default',
    'GetMaximumLevelsToReadByDefault'), ('file_name', 'GetFileName'),
    ('time_step', 'GetTimeStep'), ('time_step_range', 'GetTimeStepRange'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'read_from_input_string', 'release_data_flag', 'file_name',
    'maximum_levels_to_read_by_default', 'progress_text', 'time_step',
    'time_step_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLHierarchicalBoxDataReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLHierarchicalBoxDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['read_from_input_string'], [], ['file_name',
            'maximum_levels_to_read_by_default', 'time_step', 'time_step_range']),
            title='Edit XMLHierarchicalBoxDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLHierarchicalBoxDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


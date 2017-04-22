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

from tvtk.tvtk_classes.xml_composite_data_reader import XMLCompositeDataReader


class XMLUniformGridAMRReader(XMLCompositeDataReader):
    """
    XMLUniformGridAMRReader - Reader for amr datasets
    (vtk_overlapping_amr or NonOverlappingAMR).
    
    Superclass: XMLCompositeDataReader
    
    XMLUniformGridAMRReader reads the VTK XML data files for all types
    of amr datasets including OverlappingAMR, NonOverlappingAMR and
    the legacy HierarchicalBoxDataSet. The reader uses information in
    the file to determine what type of dataset is actually being read and
    creates the output-data object accordingly.
    
    This reader can only read files with version 1.1 or greater. Older
    versions can be converted to the newer versions using
    XMLHierarchicalBoxDataFileConverter.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLUniformGridAMRReader, obj, update, **traits)
    
    maximum_levels_to_read_by_default = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        This reader supports demand-driven heavy data reading i.e.
        downstream pipeline can request specific blocks from the AMR
        using CompositeDataPipeline::UPDATE_COMPOSITE_INDICES() key in
        request_update_extent() pass. However, when down-stream doesn't
        provide any specific keys, the default behavior can be setup to
        read at-most N levels by default. The number of levels read can
        be set using this method. Set this to 0 to imply no limit.
        Default is 0.
        """
    )

    def _maximum_levels_to_read_by_default_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumLevelsToReadByDefault,
                        self.maximum_levels_to_read_by_default)

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
            return super(XMLUniformGridAMRReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLUniformGridAMRReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['read_from_input_string'], [], ['file_name',
            'maximum_levels_to_read_by_default', 'time_step', 'time_step_range']),
            title='Edit XMLUniformGridAMRReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLUniformGridAMRReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


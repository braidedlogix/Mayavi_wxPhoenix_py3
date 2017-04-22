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

from tvtk.tvtk_classes.data_set_ghost_generator import DataSetGhostGenerator


class StructuredGridGhostDataGenerator(DataSetGhostGenerator):
    """
    StructuredGridGhostDataGenerator -  A concrete implementation of
    DataSetGhostGenerator for generating ghost
     data on partitioned structured grids on a singled process.
    
    Superclass: DataSetGhostGenerator
    
    For a distributed
     data-set see PStructuredGridGhostDataGenerator.
    
    @warning
    
      
       The input multi-block dataset must:
       
         Have the whole-extent set 
         Each block must be an instance of StructuredGrid 
         Each block must have its corresponding global extent set in the
              meta-data using the PIECE_EXTENT() key 
         All blocks must have the same fields loaded 
       
      
      
       The code currently does not handle the following cases:
       
         Ghost cells along Periodic boundaries
         Growing ghost layers beyond the extents of the neighboring grid
       
       
    
    @sa
    DataSetGhostGenerator, PStructuredGridGhostDataGenerator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStructuredGridGhostDataGenerator, obj, update, **traits)
    
    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_ghost_layers', 'GetNumberOfGhostLayers'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_ghost_layers', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StructuredGridGhostDataGenerator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StructuredGridGhostDataGenerator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['number_of_ghost_layers']),
            title='Edit StructuredGridGhostDataGenerator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StructuredGridGhostDataGenerator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


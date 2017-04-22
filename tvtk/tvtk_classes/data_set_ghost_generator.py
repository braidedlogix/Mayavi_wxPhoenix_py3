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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class DataSetGhostGenerator(MultiBlockDataSetAlgorithm):
    """
    DataSetGhostGenerator -  An abstract class that provides common
    functionality and implements an
     interface for all ghost data generators.
    
    Superclass: MultiBlockDataSetAlgorithm
    
    Ghost data generators accept as
     input a partitioned data-set, defined by a MultiBlockDataSet,
    where each
     block corresponds to a partition. The output consists of
    MultiBlockDataSet
     where each block holds the corresponding ghosted data-set. For more
    details,
     see concrete implementations.
    
    @sa
    UniformGridGhostDataGenerator,
    StructuredGridGhostDataGenerator,
    RectilinearGridGhostDataGenerator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataSetGhostGenerator, obj, update, **traits)
    
    number_of_ghost_layers = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get for number of ghost layers to generate.
        """
    )

    def _number_of_ghost_layers_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfGhostLayers,
                        self.number_of_ghost_layers)

    def fill_input_port_information(self, *args):
        """
        V.fill_input_port_information(int, Information) -> int
        C++: int FillInputPortInformation(int port, Information *info)
            override;"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillInputPortInformation, *my_args)
        return ret

    def fill_output_port_information(self, *args):
        """
        V.fill_output_port_information(int, Information) -> int
        C++: int FillOutputPortInformation(int port, Information *info)
             override;"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillOutputPortInformation, *my_args)
        return ret

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
            return super(DataSetGhostGenerator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DataSetGhostGenerator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['number_of_ghost_layers']),
            title='Edit DataSetGhostGenerator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataSetGhostGenerator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


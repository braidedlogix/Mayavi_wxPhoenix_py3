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


class ExtractDataSets(MultiBlockDataSetAlgorithm):
    """
    ExtractDataSets - extracts a number of datasets.
    
    Superclass: MultiBlockDataSetAlgorithm
    
    ExtractDataSets accepts a HierarchicalBoxDataSet as input and
    extracts different datasets from different levels. The output is
    MultiBlockDataSet of MultiPiece datasets. Each block
    corresponds to a level in the vkt_hierarchical_box_data_set. Individual
    datasets, within a level, are stored in a MultiPiece dataset.
    
    @sa
    HierarchicalBoxDataSet, MultiBlockDataSet MultiPieceDataSet
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractDataSets, obj, update, **traits)
    
    def add_data_set(self, *args):
        """
        V.add_data_set(int, int)
        C++: void AddDataSet(unsigned int level, unsigned int idx)
        Add a dataset to be extracted.
        """
        ret = self._wrap_call(self._vtk_obj.AddDataSet, *args)
        return ret

    def clear_data_set_list(self):
        """
        V.clear_data_set_list()
        C++: void ClearDataSetList()
        Remove all entries from the list of datasets to be extracted.
        """
        ret = self._vtk_obj.ClearDataSetList()
        return ret
        

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractDataSets, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractDataSets properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ExtractDataSets properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractDataSets properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


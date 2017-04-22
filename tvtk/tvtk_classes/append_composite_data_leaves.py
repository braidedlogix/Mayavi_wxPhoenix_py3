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

from tvtk.tvtk_classes.composite_data_set_algorithm import CompositeDataSetAlgorithm


class AppendCompositeDataLeaves(CompositeDataSetAlgorithm):
    """
    AppendCompositeDataLeaves - appends one or more composite datasets
    with the same structure together into a single output composite
    dataset
    
    Superclass: CompositeDataSetAlgorithm
    
    AppendCompositeDataLeaves is a filter that takes input composite
    datasets with the same structure: (1) the same number of entries and
    -- if any children are composites -- the same constraint holds from
    them; and (2) the same type of dataset at each position. It then
    creates an output dataset with the same structure whose leaves
    contain all the cells from the datasets at the corresponding leaves
    of the input datasets.
    
    Currently, this filter only supports "appending" of a few types for
    the leaf nodes and the logic used for each supported data type is as
    follows:
    
    \li UnstructuredGrid - appends all unstructured grids from the
        leaf
        location on all inputs into a single unstructured grid for the
        corresponding location in the output composite dataset. point_data
    and
        cell_data arrays are extracted and appended only if they are
    available in
        all datasets.(For example, if one dataset has scalars but another
    does
        not, scalars will not be appended.)
    
    \li PolyData - appends all polydatas from the leaf location on all
    inputs
        into a single polydata for the corresponding location in the
    output
        composite dataset. point_data and cell_data arrays are extracted
    and
        appended only if they are available in all datasets.(For example,
    if one
        dataset has scalars but another does not, scalars will not be
    appended.)
    
    \li ImageData/vtkUniformGrid - simply passes the first non-null
        grid for a particular location to corresponding location in the
    output.
    
    \li Table - simply passes the first non-null Table for a
        particular
        location to the corresponding location in the output.
    
    Other types of leaf datasets will be ignored and their positions in
    the output dataset will be NULL pointers.
    
    @sa
    AppendPolyData AppendFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAppendCompositeDataLeaves, obj, update, **traits)
    
    append_field_data = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether the field data of each dataset in the composite
        dataset is copied to the output. If append_field_data is non-zero,
        then field data arrays from all the inputs are added to the
        output. If there are duplicates, the array on the first input
        encountered is taken.
        """
    )

    def _append_field_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAppendFieldData,
                        self.append_field_data_)

    _updateable_traits_ = \
    (('append_field_data', 'GetAppendFieldData'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'append_field_data', 'debug',
    'global_warning_display', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AppendCompositeDataLeaves, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AppendCompositeDataLeaves properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['append_field_data'], [], []),
            title='Edit AppendCompositeDataLeaves properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AppendCompositeDataLeaves properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


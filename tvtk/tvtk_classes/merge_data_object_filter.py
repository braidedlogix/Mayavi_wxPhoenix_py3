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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class MergeDataObjectFilter(DataSetAlgorithm):
    """
    MergeDataObjectFilter - merge dataset and data object field to
    create dataset with attribute data
    
    Superclass: DataSetAlgorithm
    
    MergeDataObjectFilter is a filter that merges the field from a
    DataObject with a DataSet. The resulting combined dataset can
    then be processed by other filters (e.g.,
    FieldDataToAttributeDataFilter) to create attribute data like
    scalars, vectors, etc.
    
    The filter operates as follows. The field data from the DataObject
    is merged with the input's DataSet and then placed in the output.
    You can choose to place the field data into the cell data field, the
    point data field, or the datasets field (i.e., the one inherited from
    DataSet's superclass DataObject). All this data shuffling
    occurs via reference counting, therefore memory is not copied.
    
    One of the uses of this filter is to allow you to read/generate the
    structure of a dataset independent of the attributes. So, for
    example, you could store the dataset geometry/topology in one file,
    and field data in another. Then use this filter in combination with
    FieldDataToAttributeData to create a dataset ready for processing
    in the visualization pipeline.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMergeDataObjectFilter, obj, update, **traits)
    
    output_field = traits.Trait('data_object_field',
    tvtk_base.TraitRevPrefixMap({'data_object_field': 0, 'cell_data_field': 2, 'point_data_field': 1}), help=\
        """
        Specify where to place the field data during the merge process. 
        There are three choices: the field data associated with the
        DataObject superclass; the point field attribute data; and the
        cell field attribute data.
        """
    )

    def _output_field_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputField,
                        self.output_field_)

    def _get_data_object(self):
        return wrap_vtk(self._vtk_obj.GetDataObject())
    data_object = traits.Property(_get_data_object, help=\
        """
        Specify the data object to merge with the input dataset.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def set_data_object_input_data(self, *args):
        """
        V.set_data_object_input_data(DataObject)
        C++: void SetDataObjectInputData(DataObject *object)
        Specify the data object to merge with the input dataset.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDataObjectInputData, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('output_field', 'GetOutputField'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'output_field', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MergeDataObjectFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MergeDataObjectFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['output_field'], []),
            title='Edit MergeDataObjectFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MergeDataObjectFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


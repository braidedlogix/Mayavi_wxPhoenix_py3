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


class AttributeDataToFieldDataFilter(DataSetAlgorithm):
    """
    AttributeDataToFieldDataFilter - map attribute data to field data
    
    Superclass: DataSetAlgorithm
    
    AttributeDataToFieldDataFilter is a class that maps attribute data
    into field data. Since this filter is a subclass of
    DataSetAlgorithm, the output dataset (whose structure is the same
    as the input dataset), will contain the field data that is generated.
    The filter will convert point and cell attribute data to field data
    and assign it as point and cell field data, replacing any point or
    field data that was there previously. By default, the original
    non-field point and cell attribute data will be passed to the output
    of the filter, although you can shut this behavior down.
    
    @warning
    Reference counting the underlying data arrays is used to create the
    field data.  Therefore, no extra memory is utilized.
    
    @warning
    The original field data (if any) associated with the point and cell
    attribute data is placed into the generated fields along with the
    scalars, vectors, etc.
    
    @sa
    FieldData DataObject DataSet
    FieldDataToAttributeDataFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAttributeDataToFieldDataFilter, obj, update, **traits)
    
    pass_attribute_data = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the passing of point and cell non-field attribute
        data to the output of the filter.
        """
    )

    def _pass_attribute_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassAttributeData,
                        self.pass_attribute_data_)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    _updateable_traits_ = \
    (('pass_attribute_data', 'GetPassAttributeData'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'pass_attribute_data', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AttributeDataToFieldDataFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AttributeDataToFieldDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['pass_attribute_data'], [], []),
            title='Edit AttributeDataToFieldDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AttributeDataToFieldDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


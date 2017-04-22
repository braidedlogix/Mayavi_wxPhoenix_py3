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


class ExtractVectorComponents(DataSetAlgorithm):
    """
    ExtractVectorComponents - extract components of vector as separate
    scalars
    
    Superclass: DataSetAlgorithm
    
    ExtractVectorComponents is a filter that extracts vector
    components as separate scalars. This is accomplished by creating
    three different outputs. Each output is the same as the input, except
    that the scalar values will be one of the three components of the
    vector. These can be found in the vx_component, vy_component, and
    vz_component. Alternatively, if the extract_to_field_data flag is set,
    the filter will put all the components in the field data. The first
    component will be the scalar and the others will be non-attribute
    arrays.
    
    @warning
    This filter is unusual in that it creates multiple outputs. If you
    use the get_output() method, you will be retrieving the x vector
    component.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractVectorComponents, obj, update, **traits)
    
    extract_to_field_data = tvtk_base.false_bool_trait(help=\
        """
        Determines whether the vector components will be put in separate
        outputs or in the first output's field data
        """
    )

    def _extract_to_field_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtractToFieldData,
                        self.extract_to_field_data_)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def _get_vx_component(self):
        return wrap_vtk(self._vtk_obj.GetVxComponent())
    vx_component = traits.Property(_get_vx_component, help=\
        """
        Get the output dataset representing velocity x-component. If
        output is NULL then input hasn't been set, which is necessary for
        abstract objects. (Note: this method returns the same information
        as the get_output() method with an index of 0.)
        """
    )

    def _get_vy_component(self):
        return wrap_vtk(self._vtk_obj.GetVyComponent())
    vy_component = traits.Property(_get_vy_component, help=\
        """
        Get the output dataset representing velocity y-component. If
        output is NULL then input hasn't been set, which is necessary for
        abstract objects. (Note: this method returns the same information
        as the get_output() method with an index of 1.) Note that if
        extract_to_field_data is true, this output will be empty.
        """
    )

    def _get_vz_component(self):
        return wrap_vtk(self._vtk_obj.GetVzComponent())
    vz_component = traits.Property(_get_vz_component, help=\
        """
        Get the output dataset representing velocity z-component. If
        output is NULL then input hasn't been set, which is necessary for
        abstract objects. (Note: this method returns the same information
        as the get_output() method with an index of 2.) Note that if
        extract_to_field_data is true, this output will be empty.
        """
    )

    _updateable_traits_ = \
    (('extract_to_field_data', 'GetExtractToFieldData'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'extract_to_field_data',
    'global_warning_display', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractVectorComponents, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractVectorComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['extract_to_field_data'], [], []),
            title='Edit ExtractVectorComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractVectorComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


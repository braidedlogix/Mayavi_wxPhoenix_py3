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

from tvtk.tvtk_classes.pass_input_type_algorithm import PassInputTypeAlgorithm


class ProgrammableFilter(PassInputTypeAlgorithm):
    """
    ProgrammableFilter - a user-programmable filter
    
    Superclass: PassInputTypeAlgorithm
    
    ProgrammableFilter is a filter that can be programmed by the user.
     To use the filter you define a function that retrieves input of the
    correct type, creates data, and then manipulates the output of the
    filter.  Using this filter avoids the need for subclassing - and the
    function can be defined in an interpreter wrapper language such as
    Tcl or Java.
    
    The trickiest part of using this filter is that the input and output
    methods are unusual and cannot be compile-time type checked. Instead,
    as a user of this filter it is your responsibility to set and get the
    correct input and output types.
    
    @warning
    The filter correctly manages modified time and network execution in
    most cases. However, if you change the definition of the filter
    function, you'll want to send a manual Modified() method to the
    filter to force it to reexecute.
    
    @sa
    ProgrammablePointDataFilter ProgrammableSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProgrammableFilter, obj, update, **traits)
    
    copy_arrays = tvtk_base.false_bool_trait(help=\
        """
        When copy_arrays is true, all arrays are copied to the output iff
        input and output are of the same type. False by default.
        """
    )

    def _copy_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCopyArrays,
                        self.copy_arrays_)

    def _get_graph_input(self):
        return wrap_vtk(self._vtk_obj.GetGraphInput())
    graph_input = traits.Property(_get_graph_input, help=\
        """
        Get the input as a concrete type.
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

    def _get_poly_data_input(self):
        return wrap_vtk(self._vtk_obj.GetPolyDataInput())
    poly_data_input = traits.Property(_get_poly_data_input, help=\
        """
        Get the input as a concrete type. This method is typically used
        by the writer of the filter function to get the input as a
        particular type (i.e., it essentially does type casting). It is
        the users responsibility to know the correct type of the input
        data.
        """
    )

    def _get_rectilinear_grid_input(self):
        return wrap_vtk(self._vtk_obj.GetRectilinearGridInput())
    rectilinear_grid_input = traits.Property(_get_rectilinear_grid_input, help=\
        """
        Get the input as a concrete type.
        """
    )

    def _get_structured_grid_input(self):
        return wrap_vtk(self._vtk_obj.GetStructuredGridInput())
    structured_grid_input = traits.Property(_get_structured_grid_input, help=\
        """
        Get the input as a concrete type.
        """
    )

    def _get_structured_points_input(self):
        return wrap_vtk(self._vtk_obj.GetStructuredPointsInput())
    structured_points_input = traits.Property(_get_structured_points_input, help=\
        """
        Get the input as a concrete type.
        """
    )

    def _get_table_input(self):
        return wrap_vtk(self._vtk_obj.GetTableInput())
    table_input = traits.Property(_get_table_input, help=\
        """
        Get the input as a concrete type.
        """
    )

    def _get_unstructured_grid_input(self):
        return wrap_vtk(self._vtk_obj.GetUnstructuredGridInput())
    unstructured_grid_input = traits.Property(_get_unstructured_grid_input, help=\
        """
        Get the input as a concrete type.
        """
    )

    def set_execute_method(self, *args):
        """
        V.set_execute_method(function)
        C++: void SetExecuteMethod(void (*f)(void *), void *arg)
        Specify the function to use to operate on the point attribute
        data. Note that the function takes a single (void *) argument.
        """
        ret = self._wrap_call(self._vtk_obj.SetExecuteMethod, *args)
        return ret

    _updateable_traits_ = \
    (('copy_arrays', 'GetCopyArrays'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'copy_arrays', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProgrammableFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ProgrammableFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['copy_arrays'], [], []),
            title='Edit ProgrammableFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProgrammableFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


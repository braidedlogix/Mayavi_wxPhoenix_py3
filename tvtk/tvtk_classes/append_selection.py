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

from tvtk.tvtk_classes.selection_algorithm import SelectionAlgorithm


class AppendSelection(SelectionAlgorithm):
    """
    AppendSelection - appends one or more selections together
    
    Superclass: SelectionAlgorithm
    
    AppendSelection is a filter that appends one of more selections
    into a single selection.  All selections must have the same content
    type unless append_by_union is false.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAppendSelection, obj, update, **traits)
    
    append_by_union = tvtk_base.true_bool_trait(help=\
        """
        When set to true, all the selections are combined together to
        form a single Selection output. When set to false, the output
        is a composite selection with input selections as the children of
        the composite selection. This allows for selections with
        different content types and properties. Default is true.
        """
    )

    def _append_by_union_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAppendByUnion,
                        self.append_by_union_)

    user_managed_inputs = tvtk_base.false_bool_trait(help=\
        """
        user_managed_inputs allows the user to set inputs by number instead
        of using the add_input/_remove_input functions. Calls to
        set_number_of_inputs/_set_input_by_number should not be mixed with calls
        to add_input/_remove_input. By default, user_managed_inputs is false.
        """
    )

    def _user_managed_inputs_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUserManagedInputs,
                        self.user_managed_inputs_)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> Selection
        C++: Selection *GetInput(int idx)
        V.get_input() -> Selection
        C++: Selection *GetInput()
        Get any input of this filter.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def add_input_data(self, *args):
        """
        V.add_input_data(Selection)
        C++: void AddInputData(Selection *)
        Add a dataset to the list of data to append. Should not be used
        when user_managed_inputs is true, use set_input_by_number instead.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddInputData, *my_args)
        return ret

    def remove_input_data(self, *args):
        """
        V.remove_input_data(Selection)
        C++: void RemoveInputData(Selection *)
        Remove a dataset from the list of data to append. Should not be
        used when user_managed_inputs is true, use set_input_by_number (NULL)
        instead.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveInputData, *my_args)
        return ret

    def set_input_connection_by_number(self, *args):
        """
        V.set_input_connection_by_number(int, AlgorithmOutput)
        C++: void SetInputConnectionByNumber(int num,
            AlgorithmOutput *input)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputConnectionByNumber, *my_args)
        return ret

    def set_number_of_inputs(self, *args):
        """
        V.set_number_of_inputs(int)
        C++: void SetNumberOfInputs(int num)
        Directly set(allocate) number of inputs, should only be used when
        user_managed_inputs is true.
        """
        ret = self._wrap_call(self._vtk_obj.SetNumberOfInputs, *args)
        return ret

    _updateable_traits_ = \
    (('append_by_union', 'GetAppendByUnion'), ('user_managed_inputs',
    'GetUserManagedInputs'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'append_by_union', 'debug',
    'global_warning_display', 'release_data_flag', 'user_managed_inputs',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AppendSelection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AppendSelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['append_by_union', 'user_managed_inputs'], [], []),
            title='Edit AppendSelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AppendSelection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


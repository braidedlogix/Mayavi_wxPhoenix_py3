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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class AppendPolyData(PolyDataAlgorithm):
    """
    AppendPolyData - appends one or more polygonal datasets together
    
    Superclass: PolyDataAlgorithm
    
    AppendPolyData is a filter that appends one of more polygonal
    datasets into a single polygonal dataset. All geometry is extracted
    and appended, but point and cell attributes (i.e., scalars, vectors,
    normals) are extracted and appended only if all datasets have the
    point and/or cell attributes available.  (For example, if one dataset
    has point scalars but another does not, point scalars will not be
    appended.)
    
    @sa
    AppendFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAppendPolyData, obj, update, **traits)
    
    parallel_streaming = tvtk_base.false_bool_trait(help=\
        """
        parallel_streaming is for a particular application. It causes this
        filter to ask for a different piece from each of its inputs.  If
        all the inputs are the same, then the output of this append
        filter is the whole dataset pieced back together.  Duplicate
        points are create along the seams.  The purpose of this feature
        is to get data parallelism at a course scale.  Each of the inputs
        can be generated in a different process at the same time.
        """
    )

    def _parallel_streaming_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetParallelStreaming,
                        self.parallel_streaming_)

    user_managed_inputs = tvtk_base.false_bool_trait(help=\
        """
        user_managed_inputs allows the user to set inputs by number instead
        of using the add_input/_remove_input functions. Calls to
        set_number_of_inputs/_set_input_connection_by_number should not be mixed
        with calls to add_input/_remove_input. By default, user_managed_inputs
        is false.
        """
    )

    def _user_managed_inputs_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUserManagedInputs,
                        self.user_managed_inputs_)

    output_points_precision = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set/get the desired precision for the output types. See the
        documentation for the Algorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> PolyData
        C++: PolyData *GetInput(int idx)
        V.get_input() -> PolyData
        C++: PolyData *GetInput()
        Get any input of this filter.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def remove_input_data(self, *args):
        """
        V.remove_input_data(PolyData)
        C++: void RemoveInputData(PolyData *)
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

    def set_input_data_by_number(self, *args):
        """
        V.set_input_data_by_number(int, PolyData)
        C++: void SetInputDataByNumber(int num, PolyData *ds)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputDataByNumber, *my_args)
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
    (('parallel_streaming', 'GetParallelStreaming'),
    ('user_managed_inputs', 'GetUserManagedInputs'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'parallel_streaming', 'release_data_flag', 'user_managed_inputs',
    'output_points_precision', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AppendPolyData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AppendPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['parallel_streaming', 'user_managed_inputs'], [],
            ['output_points_precision']),
            title='Edit AppendPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AppendPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class AppendFilter(UnstructuredGridAlgorithm):
    """
    AppendFilter - appends one or more datasets together into a single
    unstructured grid
    
    Superclass: UnstructuredGridAlgorithm
    
    AppendFilter is a filter that appends one of more datasets into a
    single unstructured grid. All geometry is extracted and appended, but
    point attributes (i.e., scalars, vectors, normals, field data, etc.)
    are extracted and appended only if all datasets have the point
    attributes available. (For example, if one dataset has scalars but
    another does not, scalars will not be appended.)
    
    @sa
    AppendPolyData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAppendFilter, obj, update, **traits)
    
    merge_points = tvtk_base.false_bool_trait(help=\
        """
        Set the filter to merge coincidental points. Note: The filter
        will only merge points if the ghost cell array doesn't exist
        Defaults to Off
        """
    )

    def _merge_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMergePoints,
                        self.merge_points_)

    output_points_precision = traits.Trait(2, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Set/get the desired precision for the output types. See the
        documentation for the Algorithm::Precision enum for an
        explanation of the available precision settings.
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
        V.get_input(int) -> DataSet
        C++: DataSet *GetInput(int idx)
        V.get_input() -> DataSet
        C++: DataSet *GetInput()
        Get any input of this filter.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_input_list(self):
        return wrap_vtk(self._vtk_obj.GetInputList())
    input_list = traits.Property(_get_input_list, help=\
        """
        Returns a copy of the input array.  Modifications to this list
        will not be reflected in the actual inputs.
        """
    )

    def remove_input_data(self, *args):
        """
        V.remove_input_data(DataSet)
        C++: void RemoveInputData(DataSet *in)
        Remove a dataset from the list of data to append.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveInputData, *my_args)
        return ret

    _updateable_traits_ = \
    (('merge_points', 'GetMergePoints'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'merge_points',
    'release_data_flag', 'output_points_precision', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AppendFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AppendFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['merge_points'], [], ['output_points_precision']),
            title='Edit AppendFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AppendFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


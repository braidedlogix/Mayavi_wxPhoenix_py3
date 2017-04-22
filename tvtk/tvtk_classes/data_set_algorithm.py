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

from tvtk.tvtk_classes.algorithm import Algorithm


class DataSetAlgorithm(Algorithm):
    """
    DataSetAlgorithm - Superclass for algorithms that produce output
    of the same type as input
    
    Superclass: Algorithm
    
    DataSetAlgorithm is a convenience class to make writing algorithms
    easier. It is also designed to help transition old algorithms to the
    new pipeline architecture. There are some assumptions and defaults
    made by this class you should be aware of. This class defaults such
    that your filter will have one input port and one output port. If
    that is not the case simply change it with set_number_of_input_ports etc.
    See this classes contstructor for the default. This class also
    provides a fill_input_port_info method that by default says that all
    inputs will be data_set. If that isn't the case then please override
    this method in your subclass. This class breaks out the downstream
    requests into separate functions such as request_data_object
    request_data and request_information. The default implementation of
    request_data_object will create an output data of the same type as the
    input.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataSetAlgorithm, obj, update, **traits)
    
    def _get_image_data_output(self):
        return wrap_vtk(self._vtk_obj.GetImageDataOutput())
    image_data_output = traits.Property(_get_image_data_output, help=\
        """
        Get the output as StructuredPoints.
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

    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    output = traits.Property(_get_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self, idx=None):
        """
        V.get_output() -> DataSet
        C++: DataSet *GetOutput()
        V.get_output(int) -> DataSet
        C++: DataSet *GetOutput(int)
        Get the output data object for a port on this algorithm.
        """
        if idx is None:
            return wrap_vtk(self._vtk_obj.GetOutput())
        else:
            return wrap_vtk(self._vtk_obj.GetOutput(idx))

    def _get_poly_data_output(self):
        return wrap_vtk(self._vtk_obj.GetPolyDataOutput())
    poly_data_output = traits.Property(_get_poly_data_output, help=\
        """
        Get the output as PolyData.
        """
    )

    def _get_rectilinear_grid_output(self):
        return wrap_vtk(self._vtk_obj.GetRectilinearGridOutput())
    rectilinear_grid_output = traits.Property(_get_rectilinear_grid_output, help=\
        """
        Get the output as RectilinearGrid.
        """
    )

    def _get_structured_grid_output(self):
        return wrap_vtk(self._vtk_obj.GetStructuredGridOutput())
    structured_grid_output = traits.Property(_get_structured_grid_output, help=\
        """
        Get the output as StructuredGrid.
        """
    )

    def _get_structured_points_output(self):
        return wrap_vtk(self._vtk_obj.GetStructuredPointsOutput())
    structured_points_output = traits.Property(_get_structured_points_output, help=\
        """
        Get the output as StructuredPoints.
        """
    )

    def _get_unstructured_grid_output(self):
        return wrap_vtk(self._vtk_obj.GetUnstructuredGridOutput())
    unstructured_grid_output = traits.Property(_get_unstructured_grid_output, help=\
        """
        Get the output as UnstructuredGrid.
        """
    )

    def add_input_data(self, *args):
        """
        V.add_input_data(DataObject)
        C++: void AddInputData(DataObject *)
        V.add_input_data(DataSet)
        C++: void AddInputData(DataSet *)
        V.add_input_data(int, DataSet)
        C++: void AddInputData(int, DataSet *)
        V.add_input_data(int, DataObject)
        C++: void AddInputData(int, DataObject *)
        Assign a data object as input. Note that this method does not
        establish a pipeline connection. Use add_input_connection() to
        setup a pipeline connection.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddInputData, *my_args)
        return ret

    def set_input_data(self, *args):
        """
        V.set_input_data(DataObject)
        C++: void SetInputData(DataObject *)
        V.set_input_data(int, DataObject)
        C++: void SetInputData(int, DataObject *)
        V.set_input_data(DataSet)
        C++: void SetInputData(DataSet *)
        V.set_input_data(int, DataSet)
        C++: void SetInputData(int, DataSet *)
        Assign a data object as input. Note that this method does not
        establish a pipeline connection. Use set_input_connection() to
        setup a pipeline connection.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
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
            return super(DataSetAlgorithm, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DataSetAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit DataSetAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataSetAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


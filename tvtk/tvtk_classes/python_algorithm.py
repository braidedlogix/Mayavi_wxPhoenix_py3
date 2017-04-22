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


class PythonAlgorithm(Algorithm):
    """
    PythonAlgorithm - algorithm that can be implemented in Python
    
    Superclass: Algorithm
    
    PythonAlgorithm is an algorithm that calls a Python object to do
    the actual work. It defers the following methods to Python:
    - process_request()
    - fill_input_port_information()
    - fill_output_port_information()
    
    Python signature of these methods is as follows:
    - process_request(self, vtkself, request, in_info, out_info) : vtkself
      is the vtk object, in_info is a tuple of information objects
    - fill_input_port_information(self, vtkself, port, info)
    - fill_output_port_information(self, vtkself, port, info)
    - Initialize(self, vtkself)
    
    In addition, it calls an Initialize() method when setting the Python
    object, which allows the initialization of number of input and output
    ports etc.
    
    @sa
    ProgrammableFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPythonAlgorithm, obj, update, **traits)
    
    number_of_input_ports = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of input ports used by the algorithm. This is made
        public so that it can be called from Python.
        """
    )

    def _number_of_input_ports_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfInputPorts,
                        self.number_of_input_ports)

    number_of_output_ports = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of output ports provided by the algorithm. This is
        made public so that it can be called from Python.
        """
    )

    def _number_of_output_ports_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfOutputPorts,
                        self.number_of_output_ports)

    def set_python_object(self, *args):
        """
        V.set_python_object(PyObject)
        C++: void SetPythonObject(PyObject *obj)
        Specify the Python object to use to operate on the data. A
        reference will be taken on the object. This will also invoke
        Initialize() on the Python object, which is commonly used to set
        the number of input and output ports as well as perform tasks
        commonly performed in the constructor of C++ algorithm subclass.
        """
        ret = self._wrap_call(self._vtk_obj.SetPythonObject, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_input_ports', 'GetNumberOfInputPorts'),
    ('number_of_output_ports', 'GetNumberOfOutputPorts'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_input_ports',
    'number_of_output_ports', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PythonAlgorithm, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PythonAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['number_of_input_ports', 'number_of_output_ports']),
            title='Edit PythonAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PythonAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


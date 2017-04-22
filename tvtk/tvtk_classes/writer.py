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


class Writer(Algorithm):
    """
    Writer - abstract class to write data to file(s)
    
    Superclass: Algorithm
    
    Writer is an abstract class for mapper objects that write their
    data to disk (or into a communications port). All writers respond to
    Write() method. This method insures that there is input and input is
    up to date.
    
    @warning
    Every subclass of Writer must implement a write_data() method. Most
    likely will have to create set_input() method as well.
    
    @sa
    XMLDataSetWriter DataSetWriter ImageWriter MCubesWriter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWriter, obj, update, **traits)
    
    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def encode_string(self, *args):
        """
        V.encode_string(string, string, bool)
        C++: void EncodeString(char *resname, const char *name,
            bool doublePercent)
        Encode the string so that the reader will not have problems. The
        resulting string is up to three times the size of the input
        string.  double_percent indicates whether to output a double '%'
        before escaped characters so the string may be used as a printf
        format string.
        """
        ret = self._wrap_call(self._vtk_obj.EncodeString, *args)
        return ret

    def set_input_data(self, *args):
        """
        V.set_input_data(DataObject)
        C++: void SetInputData(DataObject *input)
        V.set_input_data(int, DataObject)
        C++: void SetInputData(int index, DataObject *input)
        Set/get the input to this writer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    def write(self):
        """
        V.write() -> int
        C++: virtual int Write()
        Write data to output. Method executes subclasses write_data()
        method, as well as start_method() and end_method() methods. Returns
        1 on success and 0 on failure.
        """
        ret = self._vtk_obj.Write()
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
            return super(Writer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Writer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit Writer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Writer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


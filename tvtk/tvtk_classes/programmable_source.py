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


class ProgrammableSource(DataSetAlgorithm):
    """
    ProgrammableSource - generate source dataset via a user-specified
    function
    
    Superclass: DataSetAlgorithm
    
    ProgrammableSource is a source object that is programmable by the
    user. To use this object, you must specify a function that creates
    the output.  It is possible to generate an output dataset of any
    (concrete) type; it is up to the function to properly initialize and
    define the output. Typically, you use one of the methods to get a
    concrete output type (e.g., get_poly_data_output() or
    get_structured_points_output()), and then manipulate the output in the
    user-specified function.
    
    Example use of this include writing a function to read a data file or
    interface to another system. (You might want to do this in favor of
    deriving a new class.) Another important use of this class is that it
    allows users of interpreters (e.g., Tcl or Java) the ability to write
    source objects without having to recompile C++ code or generate new
    libraries.
    @sa
    ProgrammableFilter ProgrammableAttributeDataFilter
    ProgrammableDataObjectSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProgrammableSource, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def set_execute_method(self, *args):
        """
        V.set_execute_method(function)
        C++: void SetExecuteMethod(void (*f)(void *), void *arg)
        Specify the function to use to generate the source data. Note
        that the function takes a single (void *) argument.
        """
        ret = self._wrap_call(self._vtk_obj.SetExecuteMethod, *args)
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
            return super(ProgrammableSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ProgrammableSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ProgrammableSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProgrammableSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


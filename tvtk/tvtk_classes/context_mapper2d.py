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


class ContextMapper2D(Algorithm):
    """
    ContextMapper2D - Abstract class for 2d context mappers.
    
    Superclass: Algorithm
    
    This class provides an abstract base for 2d context mappers. They
    currently only accept Table objects as input.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContextMapper2D, obj, update, **traits)
    
    def get_input_array_to_process(self, *args):
        """
        V.get_input_array_to_process(int, DataObject) -> DataArray
        C++: DataArray *GetInputArrayToProcess(int idx,
            DataObject *input)
        Make the arrays accessible to the plot objects.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetInputArrayToProcess, *my_args)
        return wrap_vtk(ret)

    def set_input_array_to_process(self, *args):
        """
        V.set_input_array_to_process(int, int, int, int, string)
        C++: virtual void SetInputArrayToProcess(int idx, int port,
            int connection, int fieldAssociation, const char *name)
        V.set_input_array_to_process(int, int, int, int, int)
        C++: virtual void SetInputArrayToProcess(int idx, int port,
            int connection, int fieldAssociation, int fieldAttributeType)
        V.set_input_array_to_process(int, Information)
        C++: virtual void SetInputArrayToProcess(int idx,
            Information *info)
        V.set_input_array_to_process(int, int, int, string, string)
        C++: virtual void SetInputArrayToProcess(int idx, int port,
            int connection, const char *fieldAssociation,
            const char *attributeTypeorName)
        Set the input data arrays that this algorithm will process.
        Specifically the idx array that this algorithm will process
        (starting from 0) is the array on port, connection with the
        specified association and name or attribute type (such as
        SCALARS). The field_association refers to which field in the data
        object the array is stored. See DataObject::FieldAssociations
        for detail.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputArrayToProcess, *my_args)
        return ret

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input for this object - only accepts Table as
        input.
        """
    )

    def get_input_abstract_array_to_process(self, *args):
        """
        V.get_input_abstract_array_to_process(int, DataObject)
            -> AbstractArray
        C++: AbstractArray *GetInputAbstractArrayToProcess(int idx,
            DataObject *input)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetInputAbstractArrayToProcess, *my_args)
        return wrap_vtk(ret)

    def set_input_data(self, *args):
        """
        V.set_input_data(Table)
        C++: virtual void SetInputData(Table *input)
        Set/Get the input for this object - only accepts Table as
        input.
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
            return super(ContextMapper2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ContextMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ContextMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContextMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


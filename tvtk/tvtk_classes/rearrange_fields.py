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


class RearrangeFields(DataSetAlgorithm):
    """
    RearrangeFields - Move/copy fields between field data, point data
    and cell data
    
    Superclass: DataSetAlgorithm
    
    RearrangeFields is used to copy/move fields (vtk_data_arrays)
    between data object's field data, point data and cell data. To
    specify which fields are copied/moved, the user adds operations.
    There are two types of operations: 1. the type which copies/moves an
    attribute's data (i.e. the field will be copied but will not be an
    attribute in the target), 2. the type which copies/moves fields by
    name. For example:
     rf->_add_operation(vtk_rearrange_fields::_copy, "foo",
                      RearrangeFields::DATA_OBJECT,
                      RearrangeFields::POINT_DATA);
      adds an operation which copies a field (data array) called foo from
    the data object's field data to point data. From Tcl, the same
    operation can be added as follows:
     rf add_operation COPY foo DATA_OBJECT POINT_DATA
      The same can be done using Python and Java bindings by passing
    strings as arguments.
     Operation types: COPY, MOVE
     attribute_types: SCALARS, VECTORS, NORMALS, TCOORDS, TENSORS
     Field data locations: DATA_OBJECT, POINT_DATA, CELL_DATA
     
    
    @warning
    When using Tcl, Java, Python or Visual Basic bindings, the array name
    can not be one of the  attribute_types when calling add_operation()
    which takes strings as arguments. The Tcl (Java etc.) command will
    always assume the string corresponds to an attribute type when the
    argument is one of the attribute_types. In this situation, use the
    add_operation() which takes enums.
    
    @sa
    FieldData DataSet DataObjectToDataSetFilter
    DataSetAttributes DataArray AssignAttribute SplitField
    MergeFields
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRearrangeFields, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def add_operation(self, *args):
        """
        V.add_operation(int, int, int, int) -> int
        C++: int AddOperation(int operationType, int attributeType,
            int fromFieldLoc, int toFieldLoc)
        V.add_operation(int, string, int, int) -> int
        C++: int AddOperation(int operationType, const char *name,
            int fromFieldLoc, int toFieldLoc)
        V.add_operation(string, string, string, string) -> int
        C++: int AddOperation(const char *operationType,
            const char *attributeType, const char *fromFieldLoc,
            const char *toFieldLoc)
        Add an operation which copies an attribute's field (data array)
        from one field data to another. Returns an operation id which can
        later be used to remove the operation.
        """
        ret = self._wrap_call(self._vtk_obj.AddOperation, *args)
        return ret

    def remove_all_operations(self):
        """
        V.remove_all_operations()
        C++: void RemoveAllOperations()
        Remove all operations.
        """
        ret = self._vtk_obj.RemoveAllOperations()
        return ret
        

    def remove_operation(self, *args):
        """
        V.remove_operation(int) -> int
        C++: int RemoveOperation(int operationId)
        V.remove_operation(int, int, int, int) -> int
        C++: int RemoveOperation(int operationType, int attributeType,
            int fromFieldLoc, int toFieldLoc)
        V.remove_operation(int, string, int, int) -> int
        C++: int RemoveOperation(int operationType, const char *name,
            int fromFieldLoc, int toFieldLoc)
        V.remove_operation(string, string, string, string) -> int
        C++: int RemoveOperation(const char *operationType,
            const char *attributeType, const char *fromFieldLoc,
            const char *toFieldLoc)
        Remove an operation with the given id.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveOperation, *args)
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
            return super(RearrangeFields, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RearrangeFields properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit RearrangeFields properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RearrangeFields properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


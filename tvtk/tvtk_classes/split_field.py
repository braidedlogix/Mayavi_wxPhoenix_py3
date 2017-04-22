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


class SplitField(DataSetAlgorithm):
    """
    SplitField - Split a field into single component fields
    
    Superclass: DataSetAlgorithm
    
    SplitField is used to split a multi-component field (vtk_data_array)
    into multiple single component fields. The new fields are put in the
    same field data as the original field. The output arrays are of the
    same type as the input array. Example:
     sf->_set_input_field("gradient", SplitField::POINT_DATA);
     sf->Split(0, "firstcomponent");
      tells SplitField to extract the first component of the field
    called gradient and create an array called firstcomponent (the new
    field will be in the output's point data). The same can be done from
    Tcl:
     sf set_input_field gradient POINT_DATA
     sf Split 0 firstcomponent
    
     attribute_types: SCALARS, VECTORS, NORMALS, TCOORDS, TENSORS
     Field locations: DATA_OBJECT, POINT_DATA, CELL_DATA
      Note that, by default, the original array is also passed through.
    
    @warning
    When using Tcl, Java, Python or Visual Basic bindings, the array name
    can not be one of the  attribute_types when calling Split() which
    takes strings as arguments. The Tcl (Java etc.) command will always
    assume the string corresponds to an attribute type when the argument
    is one of the attribute_types. In this situation, use the Split()
    which takes enums.
    
    @sa
    FieldData DataSet DataObjectToDataSetFilter
    DataSetAttributes DataArray RearrangeFields
    AssignAttribute MergeFields
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSplitField, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def set_input_field(self, *args):
        """
        V.set_input_field(int, int)
        C++: void SetInputField(int attributeType, int fieldLoc)
        V.set_input_field(string, int)
        C++: void SetInputField(const char *name, int fieldLoc)
        V.set_input_field(string, string)
        C++: void SetInputField(const char *name, const char *fieldLoc)
        Use the  given attribute in the field data given by field_loc as
        input.
        """
        ret = self._wrap_call(self._vtk_obj.SetInputField, *args)
        return ret

    def split(self, *args):
        """
        V.split(int, string)
        C++: void Split(int component, const char *arrayName)
        Create a new array with the given component.
        """
        ret = self._wrap_call(self._vtk_obj.Split, *args)
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
            return super(SplitField, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SplitField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit SplitField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SplitField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


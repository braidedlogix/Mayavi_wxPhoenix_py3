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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class StringToNumeric(DataObjectAlgorithm):
    """
    StringToNumeric - Converts string arrays to numeric arrays
    
    Superclass: DataObjectAlgorithm
    
    StringToNumeric is a filter for converting a string array into a
    numeric arrays.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStringToNumeric, obj, update, **traits)
    
    convert_cell_data = tvtk_base.true_bool_trait(help=\
        """
        Whether to detect and convert point data arrays.  Default is on.
        """
    )

    def _convert_cell_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertCellData,
                        self.convert_cell_data_)

    convert_edge_data = tvtk_base.true_bool_trait(help=\
        """
        Whether to detect and convert edge data arrays.  Default is on.
        """
    )

    def _convert_edge_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertEdgeData,
                        self.convert_edge_data_)

    convert_field_data = tvtk_base.true_bool_trait(help=\
        """
        Whether to detect and convert field data arrays.  Default is on.
        """
    )

    def _convert_field_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertFieldData,
                        self.convert_field_data_)

    convert_point_data = tvtk_base.true_bool_trait(help=\
        """
        Whether to detect and convert cell data arrays.  Default is on.
        """
    )

    def _convert_point_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertPointData,
                        self.convert_point_data_)

    convert_row_data = tvtk_base.true_bool_trait(help=\
        """
        Whether to detect and convert row data arrays.  Default is on.
        """
    )

    def _convert_row_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertRowData,
                        self.convert_row_data_)

    convert_vertex_data = tvtk_base.true_bool_trait(help=\
        """
        Whether to detect and convert vertex data arrays.  Default is on.
        """
    )

    def _convert_vertex_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvertVertexData,
                        self.convert_vertex_data_)

    force_double = tvtk_base.false_bool_trait(help=\
        """
        Convert all numeric columns to DoubleArray, even if they
        contain only integer values. Default is off.
        """
    )

    def _force_double_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForceDouble,
                        self.force_double_)

    trim_whitespace_prior_to_numeric_conversion = tvtk_base.false_bool_trait(help=\
        """
        Whether to trim whitespace from strings prior to conversion to a
        numeric. Default is false to preserve backward compatibility.
        
        * Variant handles whitespace inconsistently, so trim it before
        we try to
        * convert it.  For example:
        
        * Variant("  2._0")._to_double() == 2.0 <-- leading whitespace is
        not a problem
        * Variant("  2.0  ")._to_double() == na_n <-- trailing whitespace
        is a problem
        * Variant("  infinity  ")._to_double() == na_n <-- any whitespace
        is a problem
        
        * In these cases, trimming the whitespace gives us the result we
          expect:
        * 2.0 and INF respectively.
        """
    )

    def _trim_whitespace_prior_to_numeric_conversion_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTrimWhitespacePriorToNumericConversion,
                        self.trim_whitespace_prior_to_numeric_conversion_)

    default_double_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the default double value assigned to arrays.  Default is 0.0
        """
    )

    def _default_double_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultDoubleValue,
                        self.default_double_value)

    default_integer_value = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the default integer value assigned to arrays.  Default is 0.
        """
    )

    def _default_integer_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultIntegerValue,
                        self.default_integer_value)

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

    _updateable_traits_ = \
    (('convert_cell_data', 'GetConvertCellData'), ('convert_edge_data',
    'GetConvertEdgeData'), ('convert_field_data', 'GetConvertFieldData'),
    ('convert_point_data', 'GetConvertPointData'), ('convert_row_data',
    'GetConvertRowData'), ('convert_vertex_data', 'GetConvertVertexData'),
    ('force_double', 'GetForceDouble'),
    ('trim_whitespace_prior_to_numeric_conversion',
    'GetTrimWhitespacePriorToNumericConversion'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('default_double_value',
    'GetDefaultDoubleValue'), ('default_integer_value',
    'GetDefaultIntegerValue'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'convert_cell_data', 'convert_edge_data',
    'convert_field_data', 'convert_point_data', 'convert_row_data',
    'convert_vertex_data', 'debug', 'force_double',
    'global_warning_display', 'release_data_flag',
    'trim_whitespace_prior_to_numeric_conversion', 'default_double_value',
    'default_integer_value', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StringToNumeric, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StringToNumeric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['convert_cell_data', 'convert_edge_data', 'convert_field_data',
            'convert_point_data', 'convert_row_data', 'convert_vertex_data',
            'force_double', 'trim_whitespace_prior_to_numeric_conversion'], [],
            ['default_double_value', 'default_integer_value']),
            title='Edit StringToNumeric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StringToNumeric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


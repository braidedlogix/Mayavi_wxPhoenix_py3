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


class Threshold(UnstructuredGridAlgorithm):
    """
    Threshold - extracts cells where scalar value in cell satisfies
    threshold criterion
    
    Superclass: UnstructuredGridAlgorithm
    
    Threshold is a filter that extracts cells from any dataset type
    that satisfy a threshold criterion. A cell satisfies the criterion if
    the scalar value of (every or any) point satisfies the criterion. The
    criterion can take three forms: 1) greater than a particular value;
    2) less than a particular value; or 3) between two values. The output
    of this filter is an unstructured grid.
    
    Note that scalar values are available from the point and cell
    attribute data.  By default, point data is used to obtain scalars,
    but you can control this behavior. See the attribute_mode ivar below.
    
    By default only the first scalar value is used in the decision. Use
    the component_mode and selected_component ivars to control this
    behavior.
    
    @sa
    ThresholdPoints ThresholdTextureCoords
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkThreshold, obj, update, **traits)
    
    all_scalars = tvtk_base.true_bool_trait(help=\
        """
        If using scalars from point data, all scalars for all points in a
        cell must satisfy the threshold criterion if all_scalars is set.
        Otherwise, just a single scalar value satisfying the threshold
        criterion enables will extract the cell.
        """
    )

    def _all_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllScalars,
                        self.all_scalars_)

    use_continuous_cell_range = tvtk_base.false_bool_trait(help=\
        """
        If this is on (default is off), we will use the continuous
        interval [minimum cell scalar, maxmimum cell scalar] to intersect
        the threshold bound , rather than the set of discrete scalar
        values from the vertices
        *WARNING*: For higher order cells, the scalar range of the cell
            is not the same as the vertex scalar interval used here, so
            the result will not be accurate.
        """
    )

    def _use_continuous_cell_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseContinuousCellRange,
                        self.use_continuous_cell_range_)

    attribute_mode = traits.Trait('default', -1,
    tvtk_base.TraitRevPrefixMap({'default': 0, 'use_cell_data': 2, 'use_point_data': 1}), help=\
        """
        Control how the filter works with scalar point data and cell
        attribute data.  By default (_attribute_mode_to_default), the filter
        will use point data, and if no point data is available, then cell
        data is used. Alternatively you can explicitly set the filter to
        use point data (_attribute_mode_to_use_point_data) or cell data
        (_attribute_mode_to_use_cell_data).
        """
    )

    def _attribute_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAttributeMode,
                        self.attribute_mode_)

    component_mode = traits.Trait('use_selected',
    tvtk_base.TraitRevPrefixMap({'use_selected': 0, 'use_all': 1, 'use_any': 2}), help=\
        """
        Control how the decision of in / out is made with multi-component
        data. The choices are to use the selected component (specified in
        the selected_component ivar), or to look at all components. When
        looking at all components, the evaluation can pass if all the
        components satisfy the rule (_use_all) or if any satisfy is
        (_use_any). The default value is use_selected.
        """
    )

    def _component_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponentMode,
                        self.component_mode_)

    def get_points_data_type(self):
        """
        V.get_points_data_type() -> int
        C++: int GetPointsDataType()
        Set the data type of the output points (See the data types
        defined in Type.h). The default data type is float.
        
        * These methods are deprecated. Please use the
          set_output_points_precision()
        * and get_output_points_precision() methods instead.
        """
        ret = self._vtk_obj.GetPointsDataType()
        return ret
        

    def set_points_data_type_to_float(self):
        """
        V.set_points_data_type_to_float()
        C++: void SetPointsDataTypeToFloat()
        Set the data type of the output points (See the data types
        defined in Type.h). The default data type is float.
        
        * These methods are deprecated. Please use the
          set_output_points_precision()
        * and get_output_points_precision() methods instead.
        """
        self._vtk_obj.SetPointsDataTypeToFloat()

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

    selected_component = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        When the component mode is use_selected, this ivar indicated the
        selected component. The default value is 0.
        """
    )

    def _selected_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectedComponent,
                        self.selected_component)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_lower_threshold(self):
        return self._vtk_obj.GetLowerThreshold()
    lower_threshold = traits.Property(_get_lower_threshold, help=\
        """
        Get the Upper and Lower thresholds.
        """
    )

    def _get_upper_threshold(self):
        return self._vtk_obj.GetUpperThreshold()
    upper_threshold = traits.Property(_get_upper_threshold, help=\
        """
        Get the Upper and Lower thresholds.
        """
    )

    def threshold_between(self, *args):
        """
        V.threshold_between(float, float)
        C++: void ThresholdBetween(double lower, double upper)
        Criterion is cells whose scalars are between lower and upper
        thresholds (inclusive of the end values).
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdBetween, *args)
        return ret

    def threshold_by_lower(self, *args):
        """
        V.threshold_by_lower(float)
        C++: void ThresholdByLower(double lower)
        Criterion is cells whose scalars are less or equal to lower
        threshold.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdByLower, *args)
        return ret

    def threshold_by_upper(self, *args):
        """
        V.threshold_by_upper(float)
        C++: void ThresholdByUpper(double upper)
        Criterion is cells whose scalars are greater or equal to upper
        threshold.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdByUpper, *args)
        return ret

    _updateable_traits_ = \
    (('all_scalars', 'GetAllScalars'), ('use_continuous_cell_range',
    'GetUseContinuousCellRange'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('attribute_mode', 'GetAttributeMode'), ('component_mode',
    'GetComponentMode'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('selected_component',
    'GetSelectedComponent'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'all_scalars', 'debug', 'global_warning_display',
    'release_data_flag', 'use_continuous_cell_range', 'attribute_mode',
    'component_mode', 'output_points_precision', 'progress_text',
    'selected_component'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Threshold, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Threshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['all_scalars', 'use_continuous_cell_range'], ['attribute_mode',
            'component_mode'], ['output_points_precision', 'selected_component']),
            title='Edit Threshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Threshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


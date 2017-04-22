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

from tvtk.tvtk_classes.extract_selection_base import ExtractSelectionBase


class ExtractSelectedThresholds(ExtractSelectionBase):
    """
    ExtractSelectedThresholds - extract a cells or points from a
    dataset that have values within a set of thresholds.
    
    Superclass: ExtractSelectionBase
    
    ExtractSelectedThresholds extracts all cells and points with
    attribute values that lie within a Selection's THRESHOLD contents.
    The selecion can specify to threshold a particular array within
    either the point or cell attribute data of the input. This is similar
    to Threshold but allows mutliple thresholds ranges. This filter
    adds a scalar array called OriginalCellIds that says what input
    cell produced each output cell. This is an example of a Pedigree ID
    which helps to trace back results.
    
    @sa
    Selection ExtractSelection Threshold
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractSelectedThresholds, obj, update, **traits)
    
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

    def evaluate_value(self, *args):
        """
        V.evaluate_value(DataArray, int, DataArray) -> int
        C++: static int EvaluateValue(DataArray *scalars, IdType id,
             DataArray *lims)
        V.evaluate_value(DataArray, int, int, DataArray) -> int
        C++: static int EvaluateValue(DataArray *array,
            int array_component_no, IdType id, DataArray *lims)
        V.evaluate_value(DataArray, int, DataArray, [int, ...], [int,
             ...], [int, ...]) -> int
        C++: static int EvaluateValue(DataArray *scalars, IdType id,
             DataArray *lims, int *AboveCount, int *BelowCount,
            int *InsideCount)
        V.evaluate_value(DataArray, int, int, DataArray, [int, ...],
            [int, ...], [int, ...]) -> int
        C++: static int EvaluateValue(DataArray *scalars,
            int array_component_no, IdType id, DataArray *lims,
            int *AboveCount, int *BelowCount, int *InsideCount)
        Function for determining whether a value in a data array passes
        the threshold test(s) provided in lims.  Returns 1 if the value
        passes at least one of the threshold tests. If scalars is NULL,
        then the id itself is used as the scalar value.
        """
        my_args = deref_array(args, [('vtkDataArray', 'int', 'vtkDataArray'), ('vtkDataArray', 'int', 'int', 'vtkDataArray'), ('vtkDataArray', 'int', 'vtkDataArray', ['int', Ellipsis], ['int', Ellipsis], ['int', Ellipsis]), ('vtkDataArray', 'int', 'int', 'vtkDataArray', ['int', Ellipsis], ['int', Ellipsis], ['int', Ellipsis])])
        ret = self._wrap_call(self._vtk_obj.EvaluateValue, *my_args)
        return ret

    _updateable_traits_ = \
    (('preserve_topology', 'GetPreserveTopology'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'preserve_topology', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractSelectedThresholds, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractSelectedThresholds properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['preserve_topology'], [], []),
            title='Edit ExtractSelectedThresholds properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractSelectedThresholds properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


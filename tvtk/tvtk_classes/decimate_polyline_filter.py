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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class DecimatePolylineFilter(PolyDataAlgorithm):
    """
    DecimatePolylineFilter - reduce the number of lines in a polyline
    
    Superclass: PolyDataAlgorithm
    
    DecimatePolylineFilter is a filter to reduce the number of lines
    in a polyline. The algorithm functions by evaluating an error metric
    for each vertex (i.e., the distance of the vertex to a line defined
    from the two vertices on either side of the vertex). Then, these
    vertices are placed into a priority queue, and those with larger
    errors are deleted first. The decimation continues until the target
    reduction is reached.
    
    @warning
    This algorithm is a very simple implementation that overlooks some
    potential complexities. For example, if a vertex is multiply
    connected, meaning that it is used by multiple distinct polylines,
    then the extra topological constraints are ignored. This can produce
    less than optimal results.
    
    @sa
    Decimate DecimateProp QuadricClustering QuadricDecimation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDecimatePolylineFilter, obj, update, **traits)
    
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

    target_reduction = traits.Trait(0.9, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify the desired reduction in the total number of polygons
        (e.g., if target_reduction is set to 0.9, this filter will try to
        reduce the data set to 10% of its original size).
        """
    )

    def _target_reduction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetReduction,
                        self.target_reduction)

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
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('output_points_precision', 'GetOutputPointsPrecision'),
    ('target_reduction', 'GetTargetReduction'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'output_points_precision', 'progress_text',
    'target_reduction'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DecimatePolylineFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DecimatePolylineFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['output_points_precision', 'target_reduction']),
            title='Edit DecimatePolylineFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DecimatePolylineFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


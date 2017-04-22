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


class BoundedPointSource(PolyDataAlgorithm):
    """
    BoundedPointSource - create a random cloud of points within a
    specified bounding box
    
    Superclass: PolyDataAlgorithm
    
    BoundedPointSource is a source object that creates a
    user-specified number of points within a specified bounding box. The
    points are scattered randomly throughout the box. Optionally, the
    user can produce a PolyVertex cell as well as random scalar values
    within a specified range. The class is typically used for debugging
    and testing, as well as seeding streamlines.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBoundedPointSource, obj, update, **traits)
    
    produce_cell_output = tvtk_base.false_bool_trait(help=\
        """
        Indicate whether to produce a PolyVertex cell to go along with
        the output Points generated. By default a cell is NOT
        produced. Some filters do not need the PolyVertex which just
        consumes a lot of memory.
        """
    )

    def _produce_cell_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProduceCellOutput,
                        self.produce_cell_output_)

    produce_random_scalars = tvtk_base.false_bool_trait(help=\
        """
        Indicate whether to produce random point scalars in the output.
        By default this is off.
        """
    )

    def _produce_random_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProduceRandomScalars,
                        self.produce_random_scalars_)

    bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    number_of_points = traits.Trait(100, traits.Range(1, 9223372036854775807, enter_set=True, auto_set=False), help=\
        """
        Set the number of points to generate.
        """
    )

    def _number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPoints,
                        self.number_of_points)

    output_points_precision = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get the desired precision for the output points.
        Algorithm::SINGLE_PRECISION - Output single-precision floating
        point. Algorithm::DOUBLE_PRECISION - Output double-precision
        floating point.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

    scalar_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 1.0), cols=2, help=\
        """
        
        """
    )

    def _scalar_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarRange,
                        self.scalar_range)

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
    (('produce_cell_output', 'GetProduceCellOutput'),
    ('produce_random_scalars', 'GetProduceRandomScalars'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('bounds',
    'GetBounds'), ('number_of_points', 'GetNumberOfPoints'),
    ('output_points_precision', 'GetOutputPointsPrecision'),
    ('scalar_range', 'GetScalarRange'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'produce_cell_output', 'produce_random_scalars', 'release_data_flag',
    'bounds', 'number_of_points', 'output_points_precision',
    'progress_text', 'scalar_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BoundedPointSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BoundedPointSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['produce_cell_output', 'produce_random_scalars'], [],
            ['bounds', 'number_of_points', 'output_points_precision',
            'scalar_range']),
            title='Edit BoundedPointSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BoundedPointSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


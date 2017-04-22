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


class VolumeOfRevolutionFilter(UnstructuredGridAlgorithm):
    """
    VolumeOfRevolutionFilter - sweep data about a line to create a
    volume
    
    Superclass: UnstructuredGridAlgorithm
    
    VolumeOfRevolutionFilter is a modeling filter. It takes a
    2-dimensional dataset as input and generates an unstructured grid on
    output. The input dataset is swept around the axis of rotation to
    create dimension-elevated primitives. For example, sweeping a vertex
    creates a series of lines; sweeping a line creates a series of quads,
    etc.
    
    @warning
    The user must take care to ensure that the axis of revolution does
    not cross through the geometry, otherwise there will be intersecting
    cells in the output.
    
    @sa
    RotationalExtrusionFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeOfRevolutionFilter, obj, update, **traits)
    
    axis_direction = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _axis_direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisDirection,
                        self.axis_direction)

    axis_position = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _axis_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisPosition,
                        self.axis_position)

    output_points_precision = traits.Trait(2, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Set/get the desired precision for the output types. See the
        documentation for the Algorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

    resolution = traits.Trait(12, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get resolution of sweep operation. Resolution controls the
        number of intermediate node points.
        """
    )

    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

    sweep_angle = traits.Trait(360.0, traits.Range(-360.0, 360.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get angle of rotation in degrees.
        """
    )

    def _sweep_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSweepAngle,
                        self.sweep_angle)

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

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('axis_direction', 'GetAxisDirection'), ('axis_position',
    'GetAxisPosition'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('resolution', 'GetResolution'),
    ('sweep_angle', 'GetSweepAngle'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'axis_direction', 'axis_position',
    'output_points_precision', 'progress_text', 'resolution',
    'sweep_angle'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeOfRevolutionFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeOfRevolutionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['axis_direction', 'axis_position',
            'output_points_precision', 'resolution', 'sweep_angle']),
            title='Edit VolumeOfRevolutionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeOfRevolutionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


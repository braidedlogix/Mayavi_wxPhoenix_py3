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

from tvtk.tvtk_classes.widget_representation import WidgetRepresentation


class TensorProbeRepresentation(WidgetRepresentation):
    """
    TensorProbeRepresentation - Abstract class that serves as a
    representation for TensorProbeWidget
    
    Superclass: WidgetRepresentation
    
    The class serves as an abstract geometrical representation for the
    TensorProbeWidget. It is left to the concrete implementation to
    render the tensors as it desires. For instance,
    EllipsoidTensorProbeRepresentation renders the tensors as
    ellipsoids.
    
    @sa
    TensorProbeWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTensorProbeRepresentation, obj, update, **traits)
    
    probe_cell_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the position of the Tensor probe.
        """
    )

    def _probe_cell_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProbeCellId,
                        self.probe_cell_id)

    probe_position = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1e+299, 1e+299, 1e+299), cols=3, help=\
        """
        
        """
    )

    def _probe_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProbePosition,
                        self.probe_position)

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Set the probe position to a reasonable location on the
        trajectory.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def move(self, *args):
        """
        V.move([float, float]) -> int
        C++: virtual int Move(double motionVector[2])
        INTERNAL - Do not use This method is invoked by the widget during
        user interaction. Move probe based on the position and the motion
        vector.
        """
        ret = self._wrap_call(self._vtk_obj.Move, *args)
        return ret

    def select_probe(self, *args):
        """
        V.select_probe([int, int]) -> int
        C++: virtual int SelectProbe(int pos[2])
        This method is invoked by the widget during user interaction. Can
        we pick the tensor glyph at the current cursor pos
        """
        ret = self._wrap_call(self._vtk_obj.SelectProbe, *args)
        return ret

    def set_trajectory(self, *args):
        """
        V.set_trajectory(PolyData)
        C++: virtual void SetTrajectory(PolyData *)
        Set the trajectory that we are trying to probe tensors on
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTrajectory, *my_args)
        return ret

    _updateable_traits_ = \
    (('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('probe_cell_id', 'GetProbeCellId'),
    ('probe_position', 'GetProbePosition'), ('handle_size',
    'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'picking_managed', 'use_bounds', 'visibility',
    'estimated_render_time', 'handle_size', 'place_factor',
    'probe_cell_id', 'probe_position', 'render_time_multiplier'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TensorProbeRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TensorProbeRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['need_to_render', 'picking_managed', 'use_bounds',
            'visibility'], [], ['estimated_render_time', 'handle_size',
            'place_factor', 'probe_cell_id', 'probe_position',
            'render_time_multiplier']),
            title='Edit TensorProbeRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TensorProbeRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


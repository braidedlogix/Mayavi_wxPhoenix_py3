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


class HyperTreeGridAxisCut(PolyDataAlgorithm):
    """
    HyperTreeGridAxisCut - Axis aligned hyper tree grid cut
    
    Superclass: PolyDataAlgorithm
    
    Cut along an axis aligned plane. Only works for 3d grids. Produces
    disjoint (no point sharing) quads for now. NB: If cut plane contains
    inter-cell boundaries, the output will contain superimposed faces as
    a result.
    
    @sa
    HyperTreeGrid
    
    @par Thanks: This class was written by Philippe Pebay and Charles
    Law, Kitware 2012 This work was supported in part by Commissariat a
    l'Energie Atomique (CEA/DIF)
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHyperTreeGridAxisCut, obj, update, **traits)
    
    plane_normal_axis = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Normal axis: 0=X, 1=Y, 2=Z. Default is 0
        """
    )

    def _plane_normal_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlaneNormalAxis,
                        self.plane_normal_axis)

    plane_position = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Position of plane: Axis constant. Default is 0.0
        """
    )

    def _plane_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlanePosition,
                        self.plane_position)

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
    ('plane_normal_axis', 'GetPlaneNormalAxis'), ('plane_position',
    'GetPlanePosition'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'plane_normal_axis', 'plane_position',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HyperTreeGridAxisCut, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HyperTreeGridAxisCut properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['plane_normal_axis', 'plane_position']),
            title='Edit HyperTreeGridAxisCut properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HyperTreeGridAxisCut properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


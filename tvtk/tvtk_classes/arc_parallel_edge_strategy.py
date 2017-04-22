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

from tvtk.tvtk_classes.edge_layout_strategy import EdgeLayoutStrategy


class ArcParallelEdgeStrategy(EdgeLayoutStrategy):
    """
    ArcParallelEdgeStrategy - routes parallel edges as arcs
    
    Superclass: EdgeLayoutStrategy
    
    Parallel edges are drawn as arcs, and self-loops are drawn as ovals.
    When only one edge connects two vertices it is drawn as a straight
    line.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkArcParallelEdgeStrategy, obj, update, **traits)
    
    number_of_subdivisions = traits.Int(10, enter_set=True, auto_set=False, help=\
        """
        Get/Set the number of subdivisions on each edge.
        """
    )

    def _number_of_subdivisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSubdivisions,
                        self.number_of_subdivisions)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_subdivisions',
    'GetNumberOfSubdivisions'), ('edge_weight_array_name',
    'GetEdgeWeightArrayName'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'edge_weight_array_name',
    'number_of_subdivisions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ArcParallelEdgeStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ArcParallelEdgeStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['edge_weight_array_name', 'number_of_subdivisions']),
            title='Edit ArcParallelEdgeStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ArcParallelEdgeStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


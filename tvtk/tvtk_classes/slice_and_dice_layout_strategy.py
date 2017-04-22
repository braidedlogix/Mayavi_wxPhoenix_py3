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

from tvtk.tvtk_classes.tree_map_layout_strategy import TreeMapLayoutStrategy


class SliceAndDiceLayoutStrategy(TreeMapLayoutStrategy):
    """
    SliceAndDiceLayoutStrategy - a horizontal and vertical slicing
    tree map layout
    
    Superclass: TreeMapLayoutStrategy
    
    Lays out a tree-map alternating between horizontal and vertical
    slices, taking into account the relative size of each vertex.
    
    @par Thanks: Slice and dice algorithm comes from: Shneiderman, B.
    1992. Tree visualization with tree-maps: 2-d space-filling approach.
    ACM Trans. Graph. 11, 1 (Jan. 1992), 92-99.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSliceAndDiceLayoutStrategy, obj, update, **traits)
    
    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('shrink_percentage',
    'GetShrinkPercentage'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'shrink_percentage'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SliceAndDiceLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SliceAndDiceLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['shrink_percentage']),
            title='Edit SliceAndDiceLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SliceAndDiceLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


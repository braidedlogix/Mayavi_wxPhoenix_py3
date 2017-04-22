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

from tvtk.tvtk_classes.circle_pack_layout_strategy import CirclePackLayoutStrategy


class CirclePackFrontChainLayoutStrategy(CirclePackLayoutStrategy):
    """
    CirclePackFrontChainLayoutStrategy - layout a Tree into packed
    circles using the front chain algorithm.
    
    Superclass: CirclePackLayoutStrategy
    
    CirclePackFrontChainLayoutStrategy assigns circles to each node of
    the input Tree using the front chain algorithm.  The algorithm
    packs circles by searching a "front chain" of circles around the
    perimeter of the circles that have already been packed for the
    current level in the tree hierarchy.  Searching the front chain is in
    general faster than searching all of the circles that have been
    packed at the current level.
    
    WARNING:  The algorithm tends to break down and produce packings with
    overlapping circles when there is a large difference in the radii of
    the circles at a given level of the tree hierarchy.  Roughly on the
    order a 1000:1 ratio of circle radii.
    
    Please see the following reference for more details on the algorithm.
    
    Title: "Visualization of large hierarchical data by circle packing"
    Authors:  Weixin Wang, Hui Wang, Guozhong Dai, Hongan Wang
    Conference: Proceedings of the SIGCHI conference on Human Factors in
    computing systems Year: 2006
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCirclePackFrontChainLayoutStrategy, obj, update, **traits)
    
    height = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Width and Height define the size of the output window that the
        circle packing is placed inside.  Defaults to Width 1, Height 1
        """
    )

    def _height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeight,
                        self.height)

    width = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Width and Height define the size of the output window that the
        circle packing is placed inside.  Defaults to Width 1, Height 1
        """
    )

    def _width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWidth,
                        self.width)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('height', 'GetHeight'), ('width',
    'GetWidth'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'height', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CirclePackFrontChainLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CirclePackFrontChainLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['height', 'width']),
            title='Edit CirclePackFrontChainLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CirclePackFrontChainLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


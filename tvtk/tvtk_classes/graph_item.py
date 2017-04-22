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

from tvtk.tvtk_classes.context_item import ContextItem


class GraphItem(ContextItem):
    """
    GraphItem - A 2d graphics item for rendering a graph.
    
    Superclass: ContextItem
    
    This item draws a graph as a part of a ContextScene. This simple
    class has minimal state and delegates the determination of visual
    vertex and edge properties like color, size, width, etc. to a set of
    virtual functions. To influence the rendering of the graph, subclass
    this item and override the property functions you wish to customize.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGraphItem, obj, update, **traits)
    
    def _get_graph(self):
        return wrap_vtk(self._vtk_obj.GetGraph())
    def _set_graph(self, arg):
        old_val = self._get_graph()
        self._wrap_call(self._vtk_obj.SetGraph,
                        deref_vtk(arg))
        self.trait_property_changed('graph', old_val, arg)
    graph = traits.Property(_get_graph, _set_graph, help=\
        """
        The graph that this item draws.
        """
    )

    def _get_layout(self):
        return wrap_vtk(self._vtk_obj.GetLayout())
    layout = traits.Property(_get_layout, help=\
        """
        Exposes the incremental graph layout for updating parameters.
        """
    )

    def start_layout_animation(self, *args):
        """
        V.start_layout_animation(RenderWindowInteractor)
        C++: virtual void StartLayoutAnimation(
            RenderWindowInteractor *interactor)
        Begins or ends the layout animation.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.StartLayoutAnimation, *my_args)
        return ret

    def stop_layout_animation(self):
        """
        V.stop_layout_animation()
        C++: virtual void StopLayoutAnimation()
        Begins or ends the layout animation.
        """
        ret = self._vtk_obj.StopLayoutAnimation()
        return ret
        

    def update_layout(self):
        """
        V.update_layout()
        C++: virtual void UpdateLayout()
        Incrementally updates the graph layout.
        """
        ret = self._vtk_obj.UpdateLayout()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('opacity', 'GetOpacity'), ('interactive',
    'GetInteractive'), ('visible', 'GetVisible'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'interactive', 'opacity',
    'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GraphItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GraphItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['interactive', 'opacity', 'visible']),
            title='Edit GraphItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GraphItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


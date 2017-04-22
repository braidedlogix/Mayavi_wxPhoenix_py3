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

from tvtk.tvtk_classes.collection import Collection


class RendererCollection(Collection):
    """
    RendererCollection - a list of renderers
    
    Superclass: Collection
    
    RendererCollection represents and provides methods to manipulate a
    list of renderers (i.e., Renderer and subclasses). The list is
    unsorted and duplicate entries are not prevented.
    
    @sa
    Renderer Collection
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRendererCollection, obj, update, **traits)
    
    def _get_first_renderer(self):
        return wrap_vtk(self._vtk_obj.GetFirstRenderer())
    first_renderer = traits.Property(_get_first_renderer, help=\
        """
        Get the first Renderer in the list. Return NULL when at the end
        of the list.
        """
    )

    def _get_next_item(self):
        return wrap_vtk(self._vtk_obj.GetNextItem())
    next_item = traits.Property(_get_next_item, help=\
        """
        Get the next Renderer in the list. Return NULL when at the end of
        the list.
        """
    )

    def render(self):
        """
        V.render()
        C++: void Render()
        Forward the Render() method to each renderer in the list.
        """
        ret = self._vtk_obj.Render()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RendererCollection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RendererCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit RendererCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RendererCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


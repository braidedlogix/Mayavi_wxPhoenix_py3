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

from tvtk.tvtk_classes.abstract_context_item import AbstractContextItem


class ContextClip(AbstractContextItem):
    """
    ContextClip - all children of this item are clipped by the
    specified area.
    
    Superclass: AbstractContextItem
    
    This class can be used to clip the rendering of an item inside a
    rectangular area.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContextClip, obj, update, **traits)
    
    def _get_height(self):
        return self._vtk_obj.GetHeight()
    height = traits.Property(_get_height, help=\
        """
        
        """
    )

    def get_rect(self, *args):
        """
        V.get_rect([float, float, float, float])
        C++: virtual void GetRect(float rect[4])
        Get the clipping rectangle parameters in pixel coordinates:
        """
        ret = self._wrap_call(self._vtk_obj.GetRect, *args)
        return ret

    def _get_width(self):
        return self._vtk_obj.GetWidth()
    width = traits.Property(_get_width, help=\
        """
        
        """
    )

    def _get_x(self):
        return self._vtk_obj.GetX()
    x = traits.Property(_get_x, help=\
        """
        
        """
    )

    def _get_y(self):
        return self._vtk_obj.GetY()
    y = traits.Property(_get_y, help=\
        """
        
        """
    )

    def set_clip(self, *args):
        """
        V.set_clip(float, float, float, float)
        C++: virtual void SetClip(float x, float y, float width,
            float height)
        Set the origin, width and height of the clipping rectangle. These
        are in pixel coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetClip, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interactive', 'GetInteractive'),
    ('visible', 'GetVisible'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'interactive', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContextClip, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ContextClip properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['interactive', 'visible']),
            title='Edit ContextClip properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContextClip properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


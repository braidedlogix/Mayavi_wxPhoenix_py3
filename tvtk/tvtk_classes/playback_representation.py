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

from tvtk.tvtk_classes.border_representation import BorderRepresentation


class PlaybackRepresentation(BorderRepresentation):
    """
    PlaybackRepresentation - represent the PlaybackWidget
    
    Superclass: BorderRepresentation
    
    This class is used to represent the PlaybackWidget. Besides
    defining geometry, this class defines a series of virtual method
    stubs that are meant to be subclassed by applications for controlling
    playback.
    
    @sa
    PlaybackWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlaybackRepresentation, obj, update, **traits)
    
    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    property = traits.Property(_get_property, help=\
        """
        By obtaining this property you can specify the properties of the
        representation.
        """
    )

    def backward_one_frame(self):
        """
        V.backward_one_frame()
        C++: virtual void BackwardOneFrame()"""
        ret = self._vtk_obj.BackwardOneFrame()
        return ret
        

    def forward_one_frame(self):
        """
        V.forward_one_frame()
        C++: virtual void ForwardOneFrame()"""
        ret = self._vtk_obj.ForwardOneFrame()
        return ret
        

    def jump_to_beginning(self):
        """
        V.jump_to_beginning()
        C++: virtual void JumpToBeginning()"""
        ret = self._vtk_obj.JumpToBeginning()
        return ret
        

    def jump_to_end(self):
        """
        V.jump_to_end()
        C++: virtual void JumpToEnd()"""
        ret = self._vtk_obj.JumpToEnd()
        return ret
        

    def play(self):
        """
        V.play()
        C++: virtual void Play()
        Virtual callbacks that subclasses should implement.
        """
        ret = self._vtk_obj.Play()
        return ret
        

    def stop(self):
        """
        V.stop()
        C++: virtual void Stop()"""
        ret = self._vtk_obj.Stop()
        return ret
        

    _updateable_traits_ = \
    (('moving', 'GetMoving'), ('proportional_resize',
    'GetProportionalResize'), ('need_to_render', 'GetNeedToRender'),
    ('picking_managed', 'GetPickingManaged'), ('dragable', 'GetDragable'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('show_border',
    'GetShowBorder'), ('maximum_size', 'GetMaximumSize'), ('minimum_size',
    'GetMinimumSize'), ('position', 'GetPosition'), ('position2',
    'GetPosition2'), ('show_horizontal_border',
    'GetShowHorizontalBorder'), ('show_vertical_border',
    'GetShowVerticalBorder'), ('tolerance', 'GetTolerance'),
    ('handle_size', 'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'moving',
    'need_to_render', 'pickable', 'picking_managed',
    'proportional_resize', 'use_bounds', 'visibility', 'show_border',
    'estimated_render_time', 'handle_size', 'maximum_size',
    'minimum_size', 'place_factor', 'position', 'position2',
    'render_time_multiplier', 'show_horizontal_border',
    'show_vertical_border', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlaybackRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PlaybackRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['moving', 'need_to_render', 'picking_managed',
            'proportional_resize', 'use_bounds', 'visibility'], ['show_border'],
            ['estimated_render_time', 'handle_size', 'maximum_size',
            'minimum_size', 'place_factor', 'position', 'position2',
            'render_time_multiplier', 'show_horizontal_border',
            'show_vertical_border', 'tolerance']),
            title='Edit PlaybackRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlaybackRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class CaptionRepresentation(BorderRepresentation):
    """
    CaptionRepresentation - represents CaptionWidget in the scene
    
    Superclass: BorderRepresentation
    
    This class represents CaptionWidget. A caption is defined by some
    text with a leader (e.g., arrow) that points from the text to a point
    in the scene. The caption is defined by an instance of
    CaptionActor2D. It uses the event bindings of its superclass
    (vtk_border_widget) to control the placement of the text, and adds the
    ability to move the attachment point around. In addition, when the
    caption text is selected, the widget emits a activate_event that
    observers can watch for. This is useful for opening GUI dialogoues to
    adjust font characteristics, etc. (Please see the superclass for a
    description of event bindings.)
    
    Note that this widget extends the behavior of its superclass
    BorderRepresentation.
    
    @sa
    CaptionWidget BorderWidget BorderRepresentation
    CaptionActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCaptionRepresentation, obj, update, **traits)
    
    def get_anchor_position(self, *args):
        """
        V.get_anchor_position([float, float, float])
        C++: void GetAnchorPosition(double pos[3])
        Specify the position of the anchor (i.e., the point that the
        caption is anchored to). Note that the position should be
        specified in world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetAnchorPosition, *args)
        return ret

    def set_anchor_position(self, *args):
        """
        V.set_anchor_position([float, float, float])
        C++: void SetAnchorPosition(double pos[3])
        Specify the position of the anchor (i.e., the point that the
        caption is anchored to). Note that the position should be
        specified in world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetAnchorPosition, *args)
        return ret

    def _get_anchor_representation(self):
        return wrap_vtk(self._vtk_obj.GetAnchorRepresentation())
    def _set_anchor_representation(self, arg):
        old_val = self._get_anchor_representation()
        self._wrap_call(self._vtk_obj.SetAnchorRepresentation,
                        deref_vtk(arg))
        self.trait_property_changed('anchor_representation', old_val, arg)
    anchor_representation = traits.Property(_get_anchor_representation, _set_anchor_representation, help=\
        """
        Set and get the instances of PointHandleRepresention3D used to
        implement this representation. Normally default representations
        are created, but you can specify the ones you want to use.
        """
    )

    def _get_caption_actor2d(self):
        return wrap_vtk(self._vtk_obj.GetCaptionActor2D())
    def _set_caption_actor2d(self, arg):
        old_val = self._get_caption_actor2d()
        self._wrap_call(self._vtk_obj.SetCaptionActor2D,
                        deref_vtk(arg))
        self.trait_property_changed('caption_actor2d', old_val, arg)
    caption_actor2d = traits.Property(_get_caption_actor2d, _set_caption_actor2d, help=\
        """
        Specify the CaptionActor2D to manage. If not specified, then
        one is automatically created.
        """
    )

    font_factor = traits.Trait(1.0, traits.Range(0.1, 10.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the factor that controls the overall size of the fonts of
        the caption when the text actor's scaled_text is OFF
        """
    )

    def _font_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFontFactor,
                        self.font_factor)

    _updateable_traits_ = \
    (('moving', 'GetMoving'), ('proportional_resize',
    'GetProportionalResize'), ('need_to_render', 'GetNeedToRender'),
    ('picking_managed', 'GetPickingManaged'), ('dragable', 'GetDragable'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('show_border',
    'GetShowBorder'), ('font_factor', 'GetFontFactor'), ('maximum_size',
    'GetMaximumSize'), ('minimum_size', 'GetMinimumSize'), ('position',
    'GetPosition'), ('position2', 'GetPosition2'),
    ('show_horizontal_border', 'GetShowHorizontalBorder'),
    ('show_vertical_border', 'GetShowVerticalBorder'), ('tolerance',
    'GetTolerance'), ('handle_size', 'GetHandleSize'), ('place_factor',
    'GetPlaceFactor'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'moving',
    'need_to_render', 'pickable', 'picking_managed',
    'proportional_resize', 'use_bounds', 'visibility', 'show_border',
    'estimated_render_time', 'font_factor', 'handle_size', 'maximum_size',
    'minimum_size', 'place_factor', 'position', 'position2',
    'render_time_multiplier', 'show_horizontal_border',
    'show_vertical_border', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CaptionRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CaptionRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['moving', 'need_to_render', 'picking_managed',
            'proportional_resize', 'use_bounds', 'visibility'], ['show_border'],
            ['estimated_render_time', 'font_factor', 'handle_size',
            'maximum_size', 'minimum_size', 'place_factor', 'position',
            'position2', 'render_time_multiplier', 'show_horizontal_border',
            'show_vertical_border', 'tolerance']),
            title='Edit CaptionRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CaptionRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


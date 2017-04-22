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

from tvtk.tvtk_classes.actor2d import Actor2D


class CaptionActor2D(Actor2D):
    """
    CaptionActor2D - draw text label associated with a point
    
    Superclass: Actor2D
    
    CaptionActor2D is a hybrid 2d/_3d actor that is used to associate
    text with a point (the attachment_point) in the scene. The caption can
    be drawn with a rectangular border and a leader connecting the
    caption to the attachment point. Optionally, the leader can be
    glyphed at its endpoint to create arrow heads or other indicators.
    
    To use the caption actor, you normally specify the Position and
    Position2 coordinates (these are inherited from the Actor2D
    superclass). (Note that Position2 can be set using Actor2D's
    set_width() and set_height() methods.)  Position and Position2 define
    the size of the caption, and a third point, the attachment_point,
    defines a point that the caption is associated with.  You must also
    define the caption text, whether you want a border around the
    caption, and whether you want a leader from the caption to the
    attachment point. The font attributes of the text can be set through
    the TextProperty associated to this actor. You also indicate
    whether you want the leader to be 2d or 3d. (_2d leaders are always
    drawn over the underlying geometry. 3d leaders may be occluded by the
    geometry.) The leader may also be terminated by an optional glyph
    (e.g., arrow).
    
    The trickiest part about using this class is setting Position,
    Position2, and attachment_point correctly. These instance variables
    are Coordinates, and can be set up in various ways. In default
    usage, the attachment_point is defined in the world coordinate system,
    Position is the lower-left corner of the caption and relative to
    attachment_point (defined in display coordaintes, i.e., pixels), and
    Position2 is relative to Position and is the upper-right corner (also
    in display coordinates). However, the user has full control over the
    coordinates, and can do things like place the caption in a fixed
    position in the renderer, with the leader moving with the
    attachment_point.
    
    @sa
    LegendBoxActor TextMapper TextActor TextProperty
    Coordinate
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCaptionActor2D, obj, update, **traits)
    
    attach_edge_only = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable whether to attach the arrow only to the edge, NOT
        the vertices of the caption border.
        """
    )

    def _attach_edge_only_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAttachEdgeOnly,
                        self.attach_edge_only_)

    border = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable the placement of a border around the text.
        """
    )

    def _border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorder,
                        self.border_)

    leader = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable drawing a "line" from the caption to the
        attachment point.
        """
    )

    def _leader_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLeader,
                        self.leader_)

    three_dimensional_leader = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether the leader is 2d (no hidden line) or 3d
        (z-buffered).
        """
    )

    def _three_dimensional_leader_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThreeDimensionalLeader,
                        self.three_dimensional_leader_)

    attachment_point = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set/Get the attachment point for the caption. By default, the
        attachment point is defined in world coordinates, but this can be
        changed using Coordinate methods.
        """
    )

    def _attachment_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAttachmentPoint,
                        self.attachment_point)

    caption = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Define the text to be placed in the caption. The text can be
        multiple lines (separated by "\n").
        """
    )

    def _caption_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCaption,
                        self.caption)

    def _get_caption_text_property(self):
        return wrap_vtk(self._vtk_obj.GetCaptionTextProperty())
    def _set_caption_text_property(self, arg):
        old_val = self._get_caption_text_property()
        self._wrap_call(self._vtk_obj.SetCaptionTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('caption_text_property', old_val, arg)
    caption_text_property = traits.Property(_get_caption_text_property, _set_caption_text_property, help=\
        """
        Set/Get the text property.
        """
    )

    leader_glyph_size = traits.Trait(0.025, traits.Range(0.0, 0.1, enter_set=True, auto_set=False), help=\
        """
        Specify the relative size of the leader head. This is expressed
        as a fraction of the size (diagonal length) of the renderer. The
        leader head is automatically scaled so that window resize,
        zooming or other camera motion results in proportional changes in
        size to the leader glyph.
        """
    )

    def _leader_glyph_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLeaderGlyphSize,
                        self.leader_glyph_size)

    maximum_leader_glyph_size = traits.Trait(20, traits.Range(1, 1000, enter_set=True, auto_set=False), help=\
        """
        Specify the maximum size of the leader head (if any) in pixels.
        This is used in conjunction with leader_glyph_size to cap the
        maximum size of the leader_glyph.
        """
    )

    def _maximum_leader_glyph_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumLeaderGlyphSize,
                        self.maximum_leader_glyph_size)

    padding = traits.Trait(3, traits.Range(0, 50, enter_set=True, auto_set=False), help=\
        """
        Set/Get the padding between the caption and the border. The value
        is specified in pixels.
        """
    )

    def _padding_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPadding,
                        self.padding)

    def _get_attachment_point_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetAttachmentPointCoordinate())
    attachment_point_coordinate = traits.Property(_get_attachment_point_coordinate, help=\
        """
        Set/Get the attachment point for the caption. By default, the
        attachment point is defined in world coordinates, but this can be
        changed using Coordinate methods.
        """
    )

    def _get_leader_glyph(self):
        return wrap_vtk(self._vtk_obj.GetLeaderGlyph())
    leader_glyph = traits.Property(_get_leader_glyph, help=\
        """
        Specify a glyph to be used as the leader "head". This could be
        something like an arrow or sphere. If not specified, no glyph is
        drawn. Note that the glyph is assumed to be aligned along the
        x-axis and is rotated about the origin. set_leader_glyph_data()
        directly uses the polydata without setting a pipeline connection.
        set_leader_glyph_connection() sets up a pipeline connection and
        causes an update to the input during render.
        """
    )

    def _get_text_actor(self):
        return wrap_vtk(self._vtk_obj.GetTextActor())
    text_actor = traits.Property(_get_text_actor, help=\
        """
        Get the text actor used by the caption. This is useful if you
        want to control justification and other characteristics of the
        text actor.
        """
    )

    def set_leader_glyph_connection(self, *args):
        """
        V.set_leader_glyph_connection(AlgorithmOutput)
        C++: virtual void SetLeaderGlyphConnection(AlgorithmOutput *)
        Specify a glyph to be used as the leader "head". This could be
        something like an arrow or sphere. If not specified, no glyph is
        drawn. Note that the glyph is assumed to be aligned along the
        x-axis and is rotated about the origin. set_leader_glyph_data()
        directly uses the polydata without setting a pipeline connection.
        set_leader_glyph_connection() sets up a pipeline connection and
        causes an update to the input during render.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetLeaderGlyphConnection, *my_args)
        return ret

    def set_leader_glyph_data(self, *args):
        """
        V.set_leader_glyph_data(PolyData)
        C++: virtual void SetLeaderGlyphData(PolyData *)
        Specify a glyph to be used as the leader "head". This could be
        something like an arrow or sphere. If not specified, no glyph is
        drawn. Note that the glyph is assumed to be aligned along the
        x-axis and is rotated about the origin. set_leader_glyph_data()
        directly uses the polydata without setting a pipeline connection.
        set_leader_glyph_connection() sets up a pipeline connection and
        causes an update to the input during render.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetLeaderGlyphData, *my_args)
        return ret

    _updateable_traits_ = \
    (('attach_edge_only', 'GetAttachEdgeOnly'), ('border', 'GetBorder'),
    ('leader', 'GetLeader'), ('three_dimensional_leader',
    'GetThreeDimensionalLeader'), ('dragable', 'GetDragable'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('attachment_point', 'GetAttachmentPoint'), ('caption', 'GetCaption'),
    ('leader_glyph_size', 'GetLeaderGlyphSize'),
    ('maximum_leader_glyph_size', 'GetMaximumLeaderGlyphSize'),
    ('padding', 'GetPadding'), ('height', 'GetHeight'), ('layer_number',
    'GetLayerNumber'), ('position', 'GetPosition'), ('position2',
    'GetPosition2'), ('width', 'GetWidth'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['attach_edge_only', 'border', 'debug', 'dragable',
    'global_warning_display', 'leader', 'pickable',
    'three_dimensional_leader', 'use_bounds', 'visibility',
    'attachment_point', 'caption', 'estimated_render_time', 'height',
    'layer_number', 'leader_glyph_size', 'maximum_leader_glyph_size',
    'padding', 'position', 'position2', 'render_time_multiplier',
    'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CaptionActor2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CaptionActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['attach_edge_only', 'border', 'leader',
            'three_dimensional_leader', 'use_bounds', 'visibility'], [],
            ['attachment_point', 'caption', 'estimated_render_time', 'height',
            'layer_number', 'leader_glyph_size', 'maximum_leader_glyph_size',
            'padding', 'position', 'position2', 'render_time_multiplier',
            'width']),
            title='Edit CaptionActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CaptionActor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class ScalarBarActor(Actor2D):
    """
    ScalarBarActor - Create a scalar bar with labels
    
    Superclass: Actor2D
    
    ScalarBarActor creates a scalar bar with tick marks. A scalar bar
    is a legend that indicates to the viewer the correspondence between
    color value and data value. The legend consists of a rectangular bar
    made of rectangular pieces each colored a constant value. Since
    ScalarBarActor is a subclass of Actor2D, it is drawn in the
    image plane (i.e., in the renderer's viewport) on top of the 3d
    graphics window.
    
    To use ScalarBarActor you must associate a ScalarsToColors (or
    subclass) with it. The lookup table defines the colors and the range
    of scalar values used to map scalar data.  Typically, the number of
    colors shown in the scalar bar is not equal to the number of colors
    in the lookup table, in which case sampling of the lookup table is
    performed.
    
    Other optional capabilities include specifying the fraction of the
    viewport size (both x and y directions) which will control the size
    of the scalar bar and the number of tick labels. The actual position
    of the scalar bar on the screen is controlled by using the
    Actor2D::SetPosition() method (by default the scalar bar is
    centered in the viewport).  Other features include the ability to
    orient the scalar bar horizontally of vertically and controlling the
    format (printf style) with which to print the labels on the scalar
    bar. Also, the ScalarBarActor's property is applied to the scalar
    bar and annotations (including layer, and compositing operator).
    
    Set the text property/attributes of the title and the labels through
    the TextProperty objects associated to this actor.
    
    @warning
    If a LogLookupTable is specified as the lookup table to use, then
    the labels are created using a logarithmic scale.
    
    @sa
    Actor2D TextProperty TextMapper PolyDataMapper2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScalarBarActor, obj, update, **traits)
    
    annotation_text_scaling = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether annotation labels should be scaled with the
        viewport.
        
        * The default value is 0 (no scaling).
        * If non-zero, the TextActor instances used to render
          annotation
        * labels will have their text_scale_mode set to viewport-based
          scaling,
        * which nonlinearly scales font size with the viewport size.
        """
    )

    def _annotation_text_scaling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAnnotationTextScaling,
                        self.annotation_text_scaling_)

    draw_above_range_swatch = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether the Above range swatch should be rendered or not.
        This only affects rendering when draw_annotations is true. The
        default is false.
        """
    )

    def _draw_above_range_swatch_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawAboveRangeSwatch,
                        self.draw_above_range_swatch_)

    draw_annotations = tvtk_base.true_bool_trait(help=\
        """
        Set/get whether text annotations should be rendered or not.
        Currently, this only affects rendering when indexed_lookup is
        true. The default is true.
        """
    )

    def _draw_annotations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawAnnotations,
                        self.draw_annotations_)

    draw_background = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether a background should be drawn around the scalar
        bar. Default is off.
        """
    )

    def _draw_background_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawBackground,
                        self.draw_background_)

    draw_below_range_swatch = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether the Below range swatch should be rendered or not.
        This only affects rendering when draw_annotations is true. The
        default is false.
        """
    )

    def _draw_below_range_swatch_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawBelowRangeSwatch,
                        self.draw_below_range_swatch_)

    draw_color_bar = tvtk_base.true_bool_trait(help=\
        """
        Set/Get whether the color bar should be drawn. If off, only the
        tickmarks and text will be drawn. Default is on.
        """
    )

    def _draw_color_bar_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawColorBar,
                        self.draw_color_bar_)

    draw_frame = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether a frame should be drawn around the scalar bar.
        Default is off.
        """
    )

    def _draw_frame_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawFrame,
                        self.draw_frame_)

    draw_nan_annotation = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether the na_n annotation should be rendered or not.
        This only affects rendering when draw_annotations is true. The
        default is false.
        """
    )

    def _draw_nan_annotation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawNanAnnotation,
                        self.draw_nan_annotation_)

    draw_tick_labels = tvtk_base.true_bool_trait(help=\
        """
        Set/Get whether the tick labels should be drawn. Default is on.
        """
    )

    def _draw_tick_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawTickLabels,
                        self.draw_tick_labels_)

    fixed_annotation_leader_line_color = tvtk_base.false_bool_trait(help=\
        """
        Set/get how leader lines connecting annotations to values should
        be colored.
        
        * When true, leader lines are all the same color (and match the
          label_text_property color).
        * When false, leader lines take on the color of the value they
          correspond to.
        * This only affects rendering when draw_annotations is true.
        * The default is false.
        """
    )

    def _fixed_annotation_leader_line_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFixedAnnotationLeaderLineColor,
                        self.fixed_annotation_leader_line_color_)

    unconstrained_font_size = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether the font size of title and labels is
        unconstrained. Default is off. When it is constrained, the size
        of the scalar bar will constrained the font size When it is not,
        the size of the font will always be respected
        """
    )

    def _unconstrained_font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUnconstrainedFontSize,
                        self.unconstrained_font_size_)

    use_opacity = tvtk_base.false_bool_trait(help=\
        """
        Should be display the opacity as well. This is displayed by
        changing the opacity of the scalar bar in accordance with the
        opacity of the given color. For clarity, a texture grid is placed
        in the background if Opacity is ON. You might also want to play
        with set_texture_grid_with in that case. [Default: off]
        """
    )

    def _use_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseOpacity,
                        self.use_opacity_)

    orientation = traits.Trait('vertical',
    tvtk_base.TraitRevPrefixMap({'vertical': 1, 'horizontal': 0}), help=\
        """
        Control the orientation of the scalar bar.
        """
    )

    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation_)

    text_position = traits.Trait('succeed_scalar_bar',
    tvtk_base.TraitRevPrefixMap({'succeed_scalar_bar': 1, 'precede_scalar_bar': 0}), help=\
        """
        Should the title and tick marks precede the scalar bar or succeed
        it? This is measured along the viewport coordinate direction
        perpendicular to the long axis of the scalar bar, not the reading
        direction. Thus, succeed implies the that the text is above
        scalar bar if the orientation is horizontal or right of scalar
        bar if the orientation is vertical. Precede is the opposite.
        """
    )

    def _text_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextPosition,
                        self.text_position_)

    above_range_annotation = traits.String('Above', enter_set=True, auto_set=False, help=\
        """
        Set/get the annotation text for "Above Range Swatch" values.
        """
    )

    def _above_range_annotation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAboveRangeAnnotation,
                        self.above_range_annotation)

    annotation_leader_padding = traits.Float(8.0, enter_set=True, auto_set=False, help=\
        """
        Set/get the padding between the scalar bar and the text
        annotations. This space is used to draw leader lines. The default
        is 8 pixels.
        """
    )

    def _annotation_leader_padding_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAnnotationLeaderPadding,
                        self.annotation_leader_padding)

    def _get_annotation_text_property(self):
        return wrap_vtk(self._vtk_obj.GetAnnotationTextProperty())
    def _set_annotation_text_property(self, arg):
        old_val = self._get_annotation_text_property()
        self._wrap_call(self._vtk_obj.SetAnnotationTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('annotation_text_property', old_val, arg)
    annotation_text_property = traits.Property(_get_annotation_text_property, _set_annotation_text_property, help=\
        """
        Set/Get the annotation text property.
        """
    )

    def _get_background_property(self):
        return wrap_vtk(self._vtk_obj.GetBackgroundProperty())
    def _set_background_property(self, arg):
        old_val = self._get_background_property()
        self._wrap_call(self._vtk_obj.SetBackgroundProperty,
                        deref_vtk(arg))
        self.trait_property_changed('background_property', old_val, arg)
    background_property = traits.Property(_get_background_property, _set_background_property, help=\
        """
        Set/Get the background property.
        """
    )

    bar_ratio = traits.Trait(0.375, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/get the thickness of the color bar relative to the widget
        frame. The default is 0.375 and must always be in the range ]0,
        1[.
        """
    )

    def _bar_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBarRatio,
                        self.bar_ratio)

    below_range_annotation = traits.String('Below', enter_set=True, auto_set=False, help=\
        """
        Set/get the annotation text for "Below Range" values.
        """
    )

    def _below_range_annotation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBelowRangeAnnotation,
                        self.below_range_annotation)

    component_title = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the title for the component that is selected,
        """
    )

    def _component_title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponentTitle,
                        self.component_title)

    def _get_frame_property(self):
        return wrap_vtk(self._vtk_obj.GetFrameProperty())
    def _set_frame_property(self, arg):
        old_val = self._get_frame_property()
        self._wrap_call(self._vtk_obj.SetFrameProperty,
                        deref_vtk(arg))
        self.trait_property_changed('frame_property', old_val, arg)
    frame_property = traits.Property(_get_frame_property, _set_frame_property, help=\
        """
        Set/Get the frame property.
        """
    )

    label_format = traits.String('%-#6.3g', enter_set=True, auto_set=False, help=\
        """
        Set/Get the format with which to print the labels on the scalar
        bar.
        """
    )

    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    def _get_label_text_property(self):
        return wrap_vtk(self._vtk_obj.GetLabelTextProperty())
    def _set_label_text_property(self, arg):
        old_val = self._get_label_text_property()
        self._wrap_call(self._vtk_obj.SetLabelTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('label_text_property', old_val, arg)
    label_text_property = traits.Property(_get_label_text_property, _set_label_text_property, help=\
        """
        Set/Get the labels text property.
        """
    )

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Set/Get the lookup table to use. The lookup table specifies the
        number of colors to use in the table (if not overridden), the
        scalar range, and any annotated values. Annotated values are
        rendered using TextActor.
        """
    )

    maximum_height_in_pixels = traits.Int(2147483647, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum width and height in pixels. Specifying the
        size as a relative fraction of the viewport can sometimes
        undesirably stretch the size of the actor too much. These methods
        allow the user to set bounds on the maximum size of the scalar
        bar in pixels along any direction. Defaults to unbounded.
        """
    )

    def _maximum_height_in_pixels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumHeightInPixels,
                        self.maximum_height_in_pixels)

    maximum_number_of_colors = traits.Trait(64, traits.Range(2, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the maximum number of scalar bar segments to show. This
        may differ from the number of colors in the lookup table, in
        which case the colors are samples from the lookup table.
        """
    )

    def _maximum_number_of_colors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfColors,
                        self.maximum_number_of_colors)

    maximum_width_in_pixels = traits.Int(2147483647, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum width and height in pixels. Specifying the
        size as a relative fraction of the viewport can sometimes
        undesirably stretch the size of the actor too much. These methods
        allow the user to set bounds on the maximum size of the scalar
        bar in pixels along any direction. Defaults to unbounded.
        """
    )

    def _maximum_width_in_pixels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumWidthInPixels,
                        self.maximum_width_in_pixels)

    nan_annotation = traits.String('NaN', enter_set=True, auto_set=False, help=\
        """
        Set/get the annotation text for "_na_n" values.
        """
    )

    def _nan_annotation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNanAnnotation,
                        self.nan_annotation)

    number_of_labels = traits.Trait(5, traits.Range(0, 64, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of tick labels to show.
        """
    )

    def _number_of_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfLabels,
                        self.number_of_labels)

    text_pad = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/get the amount of padding around text boxes. The default is 1
        pixel.
        """
    )

    def _text_pad_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextPad,
                        self.text_pad)

    texture_grid_width = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set the width of the texture grid. Used only if use_opacity is ON.
        """
    )

    def _texture_grid_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureGridWidth,
                        self.texture_grid_width)

    title = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the title of the scalar bar actor,
        """
    )

    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    title_ratio = traits.Trait(0.5, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/get the ratio of the title height to the tick label height
        (used only when the Orientation is horizontal). The default is
        0.5, which attempts to make the labels and title the same size.
        This must be a number in the range ]0, 1[.
        """
    )

    def _title_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitleRatio,
                        self.title_ratio)

    def _get_title_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTitleTextProperty())
    def _set_title_text_property(self, arg):
        old_val = self._get_title_text_property()
        self._wrap_call(self._vtk_obj.SetTitleTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('title_text_property', old_val, arg)
    title_text_property = traits.Property(_get_title_text_property, _set_title_text_property, help=\
        """
        Set/Get the title text property.
        """
    )

    vertical_title_separation = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get the margin in pixels, between the title and the bar, when
        the Orientation is vertical. The default is 0 pixels.
        """
    )

    def _vertical_title_separation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVerticalTitleSeparation,
                        self.vertical_title_separation)

    def get_scalar_bar_rect(self, *args):
        """
        V.get_scalar_bar_rect([int, int, int, int], Viewport)
        C++: virtual void GetScalarBarRect(int rect[4],
            Viewport *viewport)
        Fills rect with the dimensions of the scalar bar in viewport
        coordinates. Only the color bar is considered -- text labels are
        not considered. rect is {xmin, xmax, width, height}
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetScalarBarRect, *my_args)
        return ret

    def _get_texture_actor(self):
        return wrap_vtk(self._vtk_obj.GetTextureActor())
    texture_actor = traits.Property(_get_texture_actor, help=\
        """
        Get the texture actor.. you may want to change some properties on
        it
        """
    )

    _updateable_traits_ = \
    (('annotation_text_scaling', 'GetAnnotationTextScaling'),
    ('draw_above_range_swatch', 'GetDrawAboveRangeSwatch'),
    ('draw_annotations', 'GetDrawAnnotations'), ('draw_background',
    'GetDrawBackground'), ('draw_below_range_swatch',
    'GetDrawBelowRangeSwatch'), ('draw_color_bar', 'GetDrawColorBar'),
    ('draw_frame', 'GetDrawFrame'), ('draw_nan_annotation',
    'GetDrawNanAnnotation'), ('draw_tick_labels', 'GetDrawTickLabels'),
    ('fixed_annotation_leader_line_color',
    'GetFixedAnnotationLeaderLineColor'), ('unconstrained_font_size',
    'GetUnconstrainedFontSize'), ('use_opacity', 'GetUseOpacity'),
    ('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('orientation', 'GetOrientation'),
    ('text_position', 'GetTextPosition'), ('above_range_annotation',
    'GetAboveRangeAnnotation'), ('annotation_leader_padding',
    'GetAnnotationLeaderPadding'), ('bar_ratio', 'GetBarRatio'),
    ('below_range_annotation', 'GetBelowRangeAnnotation'),
    ('component_title', 'GetComponentTitle'), ('label_format',
    'GetLabelFormat'), ('maximum_height_in_pixels',
    'GetMaximumHeightInPixels'), ('maximum_number_of_colors',
    'GetMaximumNumberOfColors'), ('maximum_width_in_pixels',
    'GetMaximumWidthInPixels'), ('nan_annotation', 'GetNanAnnotation'),
    ('number_of_labels', 'GetNumberOfLabels'), ('text_pad', 'GetTextPad'),
    ('texture_grid_width', 'GetTextureGridWidth'), ('title', 'GetTitle'),
    ('title_ratio', 'GetTitleRatio'), ('vertical_title_separation',
    'GetVerticalTitleSeparation'), ('height', 'GetHeight'),
    ('layer_number', 'GetLayerNumber'), ('position', 'GetPosition'),
    ('position2', 'GetPosition2'), ('width', 'GetWidth'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['annotation_text_scaling', 'debug', 'dragable',
    'draw_above_range_swatch', 'draw_annotations', 'draw_background',
    'draw_below_range_swatch', 'draw_color_bar', 'draw_frame',
    'draw_nan_annotation', 'draw_tick_labels',
    'fixed_annotation_leader_line_color', 'global_warning_display',
    'pickable', 'unconstrained_font_size', 'use_bounds', 'use_opacity',
    'visibility', 'orientation', 'text_position',
    'above_range_annotation', 'annotation_leader_padding', 'bar_ratio',
    'below_range_annotation', 'component_title', 'estimated_render_time',
    'height', 'label_format', 'layer_number', 'maximum_height_in_pixels',
    'maximum_number_of_colors', 'maximum_width_in_pixels',
    'nan_annotation', 'number_of_labels', 'position', 'position2',
    'render_time_multiplier', 'text_pad', 'texture_grid_width', 'title',
    'title_ratio', 'vertical_title_separation', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScalarBarActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ScalarBarActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['annotation_text_scaling', 'draw_above_range_swatch',
            'draw_annotations', 'draw_background', 'draw_below_range_swatch',
            'draw_color_bar', 'draw_frame', 'draw_nan_annotation',
            'draw_tick_labels', 'fixed_annotation_leader_line_color',
            'unconstrained_font_size', 'use_bounds', 'use_opacity', 'visibility'],
            ['orientation', 'text_position'], ['above_range_annotation',
            'annotation_leader_padding', 'bar_ratio', 'below_range_annotation',
            'component_title', 'estimated_render_time', 'height', 'label_format',
            'layer_number', 'maximum_height_in_pixels',
            'maximum_number_of_colors', 'maximum_width_in_pixels',
            'nan_annotation', 'number_of_labels', 'position', 'position2',
            'render_time_multiplier', 'text_pad', 'texture_grid_width', 'title',
            'title_ratio', 'vertical_title_separation', 'width']),
            title='Edit ScalarBarActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScalarBarActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


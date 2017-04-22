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

from tvtk.tvtk_classes.textured_actor2d import TexturedActor2D


class TextActor(TexturedActor2D):
    """
    TextActor - An actor that displays text.
    
    Superclass: TexturedActor2D
    
    Scaled or unscaled
    
    TextActor can be used to place text annotation into a window. When
    text_scale_mode is NONE, the text is fixed font and operation is the
    same as a PolyDataMapper2D/vtkActor2D pair. When text_scale_mode is
    VIEWPORT, the font resizes such that it maintains a consistent size
    relative to the viewport in which it is rendered. When text_scale_mode
    is PROP, the font resizes such that the text fits inside the box
    defined by the position 1 & 2 coordinates. This class replaces the
    deprecated ScaledTextActor and acts as a convenient wrapper for a
    TextMapper/vtkActor2D pair. Set the text property/attributes
    through the TextProperty associated to this actor.
    
    @sa
    Actor2D PolyDataMapper TextProperty TextRenderer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextActor, obj, update, **traits)
    
    use_border_align = tvtk_base.false_bool_trait(help=\
        """
        Turn on or off the use_border_align option. When use_border_align is
        on, the bounding rectangle is used to align the text, which is
        the proper behavior when using TextRepresentation
        """
    )

    def _use_border_align_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseBorderAlign,
                        self.use_border_align_)

    text_scale_mode = traits.Trait('none',
    tvtk_base.TraitRevPrefixMap({'none': 0, 'prop': 1, 'viewport': 2}), help=\
        """
        Set how text should be scaled.  If set to
        TextActor::TEXT_SCALE_MODE_NONE, the the font size will be
        fixed by the size given in text_property.  If set to
        TextActor::TEXT_SCALE_MODE_PROP, the text will be scaled to
        fit exactly in the prop as specified by the position 1 & 2
        coordinates.  If set to TextActor::TEXT_SCALE_MODE_VIEWPORT,
        the text will be scaled based on the size of the viewport it is
        displayed in.
        """
    )

    def _text_scale_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextScaleMode,
                        self.text_scale_mode_)

    alignment_point = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This method is being depricated.  Use set_justification and
        set_vertical_justification in text property instead. Set/Get the
        Alignment point if zero (default), the text aligns itself to the
        bottom left corner (which is defined by the position_coordinate)
        otherwise the text aligns itself to corner/midpoint or centre
         6   7   8
         3   4   5
         0   1   2
          This is the same as setting the text_property's justification.
        Currently text_actor is not oriented around its alignment_point.
        """
    )

    def _alignment_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlignmentPoint,
                        self.alignment_point)

    def _get_input(self):
        return self._vtk_obj.GetInput()
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        arg)
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set the text string to be displayed. "\n" is recognized as a
        carriage return/linefeed (line separator). The characters must be
        in the UTF-8 encoding. Convenience method to the underlying
        mapper
        """
    )

    maximum_line_height = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum height of a line of text as a percentage of
        the vertical area allocated to this scaled text actor. Defaults
        to 1.0. Only valid when text_scale_mode is PROP.
        """
    )

    def _maximum_line_height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumLineHeight,
                        self.maximum_line_height)

    minimum_size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(10, 10), cols=2, help=\
        """
        
        """
    )

    def _minimum_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumSize,
                        self.minimum_size)

    orientation = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Counterclockwise rotation around the Alignment point. Units are
        in degrees and defaults to 0. The orientation in the text
        property rotates the text in the texture map.  It will proba ly
        not give you the effect you desire.
        """
    )

    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation)

    def _get_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTextProperty())
    def _set_text_property(self, arg):
        old_val = self._get_text_property()
        self._wrap_call(self._vtk_obj.SetTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('text_property', old_val, arg)
    text_property = traits.Property(_get_text_property, _set_text_property, help=\
        """
        Set/Get the text property.
        """
    )

    def get_bounding_box(self, *args):
        """
        V.get_bounding_box(Viewport, [float, float, float, float])
        C++: virtual void GetBoundingBox(Viewport *vport,
            double bbox[4])
        Return the bounding box coordinates of the text in viewport
        coordinates. The bbox array is populated with [ xmin, xmax, ymin,
        ymax ] values in that order.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetBoundingBox, *my_args)
        return ret

    def get_font_scale(self, *args):
        """
        V.get_font_scale(Viewport) -> float
        C++: static float GetFontScale(Viewport *viewport)
        Provide a font scaling based on a viewport.  This is the scaling
        factor used when the text_scale_mode is set to VIEWPORT and has
        been made public for other components to use.  This scaling
        assumes that the long dimension of the viewport is meant to be 6
        inches (a typical width of text in a paper) and then resizes
        based on if that long dimension was 72 DPI.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetFontScale, *my_args)
        return ret

    def _get_scaled_text_property(self):
        return wrap_vtk(self._vtk_obj.GetScaledTextProperty())
    scaled_text_property = traits.Property(_get_scaled_text_property, help=\
        """
        Get the scaled font.  Use compute_scaled_font to set the scale for
        a given viewport.
        """
    )

    def get_size(self, *args):
        """
        V.get_size(Viewport, [float, float])
        C++: virtual void GetSize(Viewport *vport, double size[2])
        Syntactic sugar to get the size of text instead of the entire
        bounding box.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetSize, *my_args)
        return ret

    def compute_scaled_font(self, *args):
        """
        V.compute_scaled_font(Viewport)
        C++: virtual void ComputeScaledFont(Viewport *viewport)
        Compute the scale the font should be given the viewport.  The
        result is placed in the scaled_text_property ivar.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeScaledFont, *my_args)
        return ret

    def display_to_specified(self, *args):
        """
        V.display_to_specified([float, ...], Viewport, int)
        C++: void DisplayToSpecified(double *pos, Viewport *vport,
            int specified)
        This is just a simple coordinate conversion method used in the
        render process.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DisplayToSpecified, *my_args)
        return ret

    def set_constrained_font_size(self, *args):
        """
        V.set_constrained_font_size(Viewport, int, int) -> int
        C++: virtual int SetConstrainedFontSize(Viewport *,
            int targetWidth, int targetHeight)
        V.set_constrained_font_size(TextActor, Viewport, int, int)
            -> int
        C++: static int SetConstrainedFontSize(TextActor *,
            Viewport *, int targetWidth, int targetHeight)
        Set and return the font size required to make this mapper fit in
        a given target rectangle (width x height, in pixels). A static
        version of the method is also available for convenience to other
        classes (e.g., widgets).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetConstrainedFontSize, *my_args)
        return ret

    def set_non_linear_font_scale(self, *args):
        """
        V.set_non_linear_font_scale(float, int)
        C++: virtual void SetNonLinearFontScale(double exponent,
            int target)
        Enable non-linear scaling of font sizes. This is useful in
        combination with scaled text. With small windows you want to use
        the entire scaled text area. With larger windows you want to
        reduce the font size some so that the entire area is not used.
        These values modify the computed font size as follows:
        new_font_size = pow(_font_size,exponent)*pow(target,_1._0 - exponent)
        typically exponent should be around 0.7 and target should be
        around 10
        """
        ret = self._wrap_call(self._vtk_obj.SetNonLinearFontScale, *args)
        return ret

    def specified_to_display(self, *args):
        """
        V.specified_to_display([float, ...], Viewport, int)
        C++: void SpecifiedToDisplay(double *pos, Viewport *vport,
            int specified)
        This is just a simple coordinate conversion method used in the
        render process.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SpecifiedToDisplay, *my_args)
        return ret

    _updateable_traits_ = \
    (('use_border_align', 'GetUseBorderAlign'), ('dragable',
    'GetDragable'), ('pickable', 'GetPickable'), ('use_bounds',
    'GetUseBounds'), ('visibility', 'GetVisibility'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('text_scale_mode', 'GetTextScaleMode'), ('alignment_point',
    'GetAlignmentPoint'), ('maximum_line_height', 'GetMaximumLineHeight'),
    ('minimum_size', 'GetMinimumSize'), ('orientation', 'GetOrientation'),
    ('height', 'GetHeight'), ('layer_number', 'GetLayerNumber'),
    ('position', 'GetPosition'), ('position2', 'GetPosition2'), ('width',
    'GetWidth'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_border_align', 'use_bounds', 'visibility', 'text_scale_mode',
    'alignment_point', 'estimated_render_time', 'height', 'layer_number',
    'maximum_line_height', 'minimum_size', 'orientation', 'position',
    'position2', 'render_time_multiplier', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_border_align', 'use_bounds', 'visibility'],
            ['text_scale_mode'], ['alignment_point', 'estimated_render_time',
            'height', 'layer_number', 'maximum_line_height', 'minimum_size',
            'orientation', 'position', 'position2', 'render_time_multiplier',
            'width']),
            title='Edit TextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


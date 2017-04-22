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

from tvtk.tvtk_classes.distance_representation import DistanceRepresentation


class DistanceRepresentation3D(DistanceRepresentation):
    """
    DistanceRepresentation3D - represent the DistanceWidget
    
    Superclass: DistanceRepresentation
    
    The DistanceRepresentation3D is a representation for the
    DistanceWidget. This representation consists of a measuring line
    (axis) and two HandleWidgets to place the end points of the line.
    Note that this particular widget draws its representation in 3d
    space, so the widget can be occluded.
    
    @sa
    DistanceWidget DistanceRepresentation
    DistanceRepresentation2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDistanceRepresentation3D, obj, update, **traits)
    
    glyph_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Scale the glyphs used as tick marks. By default it is 1/40th of
        the length.
        """
    )

    def _glyph_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlyphScale,
                        self.glyph_scale)

    label_position = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get position of the label title in normalized coordinates
        [0,1]. 0 is at the start of the line whereas 1 is at the end.
        """
    )

    def _label_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelPosition,
                        self.label_position)

    label_scale = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Scale text (font size along each dimension). This helps control
        the appearance of the 3d text.
        """
    )

    def _label_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelScale,
                        self.label_scale)

    maximum_number_of_ruler_ticks = traits.Trait(99, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the maximum number of ticks in ruler mode.
        """
    )

    def _maximum_number_of_ruler_ticks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfRulerTicks,
                        self.maximum_number_of_ruler_ticks)

    def get_point1display_position(self, *args):
        """
        V.get_point1display_position([float, float, float])
        C++: void GetPoint1DisplayPosition(double pos[3])"""
        ret = self._wrap_call(self._vtk_obj.GetPoint1DisplayPosition, *args)
        return ret

    def set_point1display_position(self, *args):
        """
        V.set_point1display_position([float, float, float])
        C++: void SetPoint1DisplayPosition(double pos[3])"""
        ret = self._wrap_call(self._vtk_obj.SetPoint1DisplayPosition, *args)
        return ret

    point1_world_position = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
    )

    def _point1_world_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1WorldPosition,
                        self.point1_world_position)

    def get_point2display_position(self, *args):
        """
        V.get_point2display_position([float, float, float])
        C++: void GetPoint2DisplayPosition(double pos[3])"""
        ret = self._wrap_call(self._vtk_obj.GetPoint2DisplayPosition, *args)
        return ret

    def set_point2display_position(self, *args):
        """
        V.set_point2display_position([float, float, float])
        C++: void SetPoint2DisplayPosition(double pos[3])"""
        ret = self._wrap_call(self._vtk_obj.SetPoint2DisplayPosition, *args)
        return ret

    point2_world_position = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
    )

    def _point2_world_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2WorldPosition,
                        self.point2_world_position)

    def _get_glyph_actor(self):
        return wrap_vtk(self._vtk_obj.GetGlyphActor())
    glyph_actor = traits.Property(_get_glyph_actor, help=\
        """
        Convenience method to get the glyph actor. Using this it is
        possible to control the appearance of the glyphs.
        """
    )

    def _get_label_actor(self):
        return wrap_vtk(self._vtk_obj.GetLabelActor())
    label_actor = traits.Property(_get_label_actor, help=\
        """
        Convenience method Get the label actor. It is possible to control
        the appearance of the label.
        """
    )

    def _get_label_property(self):
        return wrap_vtk(self._vtk_obj.GetLabelProperty())
    label_property = traits.Property(_get_label_property, help=\
        """
        Get the distance annotation property
        """
    )

    def _get_line_property(self):
        return wrap_vtk(self._vtk_obj.GetLineProperty())
    line_property = traits.Property(_get_line_property, help=\
        """
        Convenience method to get the line actor property.
        """
    )

    _updateable_traits_ = \
    (('ruler_mode', 'GetRulerMode'), ('need_to_render',
    'GetNeedToRender'), ('picking_managed', 'GetPickingManaged'),
    ('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('glyph_scale', 'GetGlyphScale'),
    ('label_position', 'GetLabelPosition'),
    ('maximum_number_of_ruler_ticks', 'GetMaximumNumberOfRulerTicks'),
    ('label_format', 'GetLabelFormat'), ('number_of_ruler_ticks',
    'GetNumberOfRulerTicks'), ('ruler_distance', 'GetRulerDistance'),
    ('scale', 'GetScale'), ('tolerance', 'GetTolerance'), ('handle_size',
    'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'picking_managed', 'ruler_mode', 'use_bounds',
    'visibility', 'estimated_render_time', 'glyph_scale', 'handle_size',
    'label_format', 'label_position', 'maximum_number_of_ruler_ticks',
    'number_of_ruler_ticks', 'place_factor', 'render_time_multiplier',
    'ruler_distance', 'scale', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DistanceRepresentation3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DistanceRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['need_to_render', 'picking_managed', 'ruler_mode',
            'use_bounds', 'visibility'], [], ['estimated_render_time',
            'glyph_scale', 'handle_size', 'label_format', 'label_position',
            'maximum_number_of_ruler_ticks', 'number_of_ruler_ticks',
            'place_factor', 'render_time_multiplier', 'ruler_distance', 'scale',
            'tolerance']),
            title='Edit DistanceRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DistanceRepresentation3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


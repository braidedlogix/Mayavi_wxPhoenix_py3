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

from tvtk.tvtk_classes.bi_dimensional_representation import BiDimensionalRepresentation


class BiDimensionalRepresentation2D(BiDimensionalRepresentation):
    """
    BiDimensionalRepresentation2D - represent the
    BiDimensionalWidget
    
    Superclass: BiDimensionalRepresentation
    
    The BiDimensionalRepresentation2D is used to represent the
    bi-dimensional measure in a 2d (overlay) context. This representation
    consists of two perpendicular lines defined by four
    HandleRepresentations. The four handles can be independently
    manipulated consistent with the orthogonal constraint on the lines.
    (Note: the four points are referred to as Point1, Point2, Point3 and
    Point4. Point1 and Point2 define the first line; and Point3 and
    Point4 define the second orthogonal line.)
    
    To create this widget, you click to place the first two points. The
    third point is mirrored with the fourth point; when you place the
    third point (which is orthogonal to the lined defined by the first
    two points), the fourth point is dropped as well. After definition,
    the four points can be moved (in constrained fashion, preserving
    orthogonality). Further, the entire widget can be translated by
    grabbing the center point of the widget; each line can be moved along
    the other line; and the entire widget can be rotated around its
    center point.
    
    @sa
    AngleWidget HandleRepresentation BiDimensionalRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBiDimensionalRepresentation2D, obj, update, **traits)
    
    def _get_line_property(self):
        return wrap_vtk(self._vtk_obj.GetLineProperty())
    line_property = traits.Property(_get_line_property, help=\
        """
        Retrieve the property used to control the appearance of the two
        orthogonal lines.
        """
    )

    def _get_selected_line_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedLineProperty())
    selected_line_property = traits.Property(_get_selected_line_property, help=\
        """
        Retrieve the property used to control the appearance of the two
        orthogonal lines.
        """
    )

    def _get_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTextProperty())
    text_property = traits.Property(_get_text_property, help=\
        """
        Retrieve the property used to control the appearance of the text
        labels.
        """
    )

    _updateable_traits_ = \
    (('line1_visibility', 'GetLine1Visibility'), ('line2_visibility',
    'GetLine2Visibility'), ('show_label_above_widget',
    'GetShowLabelAboveWidget'), ('need_to_render', 'GetNeedToRender'),
    ('picking_managed', 'GetPickingManaged'), ('dragable', 'GetDragable'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('id',
    'GetID'), ('label_format', 'GetLabelFormat'), ('tolerance',
    'GetTolerance'), ('handle_size', 'GetHandleSize'), ('place_factor',
    'GetPlaceFactor'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'line1_visibility',
    'line2_visibility', 'need_to_render', 'pickable', 'picking_managed',
    'show_label_above_widget', 'use_bounds', 'visibility',
    'estimated_render_time', 'handle_size', 'id', 'label_format',
    'place_factor', 'render_time_multiplier', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BiDimensionalRepresentation2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BiDimensionalRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['line1_visibility', 'line2_visibility', 'need_to_render',
            'picking_managed', 'show_label_above_widget', 'use_bounds',
            'visibility'], [], ['estimated_render_time', 'handle_size', 'id',
            'label_format', 'place_factor', 'render_time_multiplier',
            'tolerance']),
            title='Edit BiDimensionalRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BiDimensionalRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


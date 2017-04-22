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


class ContextArea(AbstractContextItem):
    """
    ContextArea - Clipped, transformed area with axes for context
    items.
    
    Superclass: AbstractContextItem
    
    ContextArea provides an clipped drawing area surrounded by four
    axes. The drawing area is transformed to map the 2d area described by
    draw_area_bounds into pixel coordinates. draw_area_bounds is also used to
    configure the axes. Item to be rendered in the draw area should be
    added to the context item returned by get_draw_area_item().
    
    The size and shape of the draw area is configured by the following
    member variables:
    - Geometry: The rect (pixel coordinates) defining the location of the
    context area in the scene. This includes the draw area and axis
      ticks/labels.
    - fill_viewport: If true (default), Geometry is set to span the size
      returned by ContextDevice2D::GetViewportSize().
    - draw_area_resize_behavior: Controls how the draw area should be
      shaped. Available options: Expand (default), fixed_aspect,
      fixed_rect, fixed_margins.
    - fixed_aspect: Aspect ratio to enforce for fixed_aspect resize
      behavior.
    - fixed_rect: Rect used to enforce for fixed_rect resize behavior.
    - fixed_margins: Margins to enforce for fixed_margins resize behavior.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContextArea, obj, update, **traits)
    
    fill_viewport = tvtk_base.true_bool_trait(help=\
        """
        If true, Geometry is set to (0, 0, vp_size[_0], vp_size[_1]) at the
        start of each Paint call. vp_size is
        ContextDevice2D::GetViewportSize. Default is true.
        """
    )

    def _fill_viewport_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFillViewport,
                        self.fill_viewport_)

    show_grid = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off grid visibility.
        """
    )

    def _show_grid_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowGrid,
                        self.show_grid_)

    fixed_aspect = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The fixed aspect ratio, if draw_area_resize_behavior is fixed_aspect.
        Defined as width/height. Default is 1. Setting the aspect ratio
        will also set draw_area_resize_behavior to fixed_aspect.
        """
    )

    def _fixed_aspect_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFixedAspect,
                        self.fixed_aspect)

    def get_axis(self, *args):
        """
        V.get_axis(Axis.Location) -> Axis
        C++: Axis *GetAxis(Axis::Location location)
        Get the Axis associated with the specified location.
        """
        ret = self._wrap_call(self._vtk_obj.GetAxis, *args)
        return ret

    def _get_draw_area_item(self):
        return wrap_vtk(self._vtk_obj.GetDrawAreaItem())
    draw_area_item = traits.Property(_get_draw_area_item, help=\
        """
        Returns the AbstractContextItem that will draw in the clipped,
        transformed space. This is the item to add children for.
        """
    )

    def _get_fixed_margins_array(self):
        return self._vtk_obj.GetFixedMarginsArray()
    fixed_margins_array = traits.Property(_get_fixed_margins_array, help=\
        """
        The left, right, bottom, and top margins for the draw area, if
        draw_area_resize_behavior is fixed_margins. Units are in pixels,
        default is { 0, 0, 0, 0 }. Setting the fixed margins will also
        set draw_area_resize_behavior to fixed_margins.
        """
    )

    _updateable_traits_ = \
    (('fill_viewport', 'GetFillViewport'), ('show_grid', 'GetShowGrid'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('fixed_aspect', 'GetFixedAspect'),
    ('interactive', 'GetInteractive'), ('visible', 'GetVisible'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'fill_viewport', 'global_warning_display', 'show_grid',
    'fixed_aspect', 'interactive', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContextArea, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ContextArea properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['fill_viewport', 'show_grid'], [], ['fixed_aspect',
            'interactive', 'visible']),
            title='Edit ContextArea properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContextArea properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


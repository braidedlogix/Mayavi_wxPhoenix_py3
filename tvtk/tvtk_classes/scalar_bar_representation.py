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


class ScalarBarRepresentation(BorderRepresentation):
    """
    ScalarBarRepresentation - represent scalar bar for
    ScalarBarWidget
    
    Superclass: BorderRepresentation
    
    This class represents a scalar bar for a ScalarBarWidget.  This
    class provides support for interactively placing a scalar bar on the
    2d overlay plane.  The scalar bar is defined by an instance of
    ScalarBarActor.
    
    One specialty of this class is that if the scalar bar is moved near
    enough to an edge, it's orientation is flipped to match that edge.
    
    @sa
    ScalarBarWidget WidgetRepresentation ScalarBarActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScalarBarRepresentation, obj, update, **traits)
    
    auto_orient = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        If true, the orientation will be updated based on the widget's
        position. Default is true.
        """
    )

    def _auto_orient_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoOrient,
                        self.auto_orient)

    orientation = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Get/Set the orientation.
        """
    )

    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation)

    def _get_scalar_bar_actor(self):
        return wrap_vtk(self._vtk_obj.GetScalarBarActor())
    def _set_scalar_bar_actor(self, arg):
        old_val = self._get_scalar_bar_actor()
        self._wrap_call(self._vtk_obj.SetScalarBarActor,
                        deref_vtk(arg))
        self.trait_property_changed('scalar_bar_actor', old_val, arg)
    scalar_bar_actor = traits.Property(_get_scalar_bar_actor, _set_scalar_bar_actor, help=\
        """
        The prop that is placed in the renderer.
        """
    )

    _updateable_traits_ = \
    (('moving', 'GetMoving'), ('proportional_resize',
    'GetProportionalResize'), ('need_to_render', 'GetNeedToRender'),
    ('picking_managed', 'GetPickingManaged'), ('dragable', 'GetDragable'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('show_border',
    'GetShowBorder'), ('auto_orient', 'GetAutoOrient'), ('orientation',
    'GetOrientation'), ('maximum_size', 'GetMaximumSize'),
    ('minimum_size', 'GetMinimumSize'), ('position', 'GetPosition'),
    ('position2', 'GetPosition2'), ('show_horizontal_border',
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
    'auto_orient', 'estimated_render_time', 'handle_size', 'maximum_size',
    'minimum_size', 'orientation', 'place_factor', 'position',
    'position2', 'render_time_multiplier', 'show_horizontal_border',
    'show_vertical_border', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScalarBarRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ScalarBarRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['moving', 'need_to_render', 'picking_managed',
            'proportional_resize', 'use_bounds', 'visibility'], ['show_border'],
            ['auto_orient', 'estimated_render_time', 'handle_size',
            'maximum_size', 'minimum_size', 'orientation', 'place_factor',
            'position', 'position2', 'render_time_multiplier',
            'show_horizontal_border', 'show_vertical_border', 'tolerance']),
            title='Edit ScalarBarRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScalarBarRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.handle_representation import HandleRepresentation


class SphereHandleRepresentation(HandleRepresentation):
    """
    SphereHandleRepresentation - A spherical rendition of point in 3d
    space
    
    Superclass: HandleRepresentation
    
    This class is a concrete implementation of HandleRepresentation.
    It renders handles as spherical blobs in 3d space.
    
    @sa
    HandleRepresentation HandleWidget SphereSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSphereHandleRepresentation, obj, update, **traits)
    
    translation_mode = tvtk_base.true_bool_trait(help=\
        """
        If translation mode is on, as the widget is moved the bounding
        box, shadows, and cursor are all translated simultaneously as the
        point moves (i.e., the left and middle mouse buttons act the
        same).  Otherwise, only the cursor focal point moves, which is
        constrained by the bounds of the point representation. (Note that
        the bounds can be scaled up using the right mouse button.)
        """
    )

    def _translation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslationMode,
                        self.translation_mode_)

    display_position = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set the position of the point in world and display coordinates.
        Note that if the position is set outside of the bounding box, it
        will be clamped to the boundary of the bounding box. This method
        overloads the superclasses' set_world_position() and
        set_display_position() in order to set the focal point of the
        cursor properly.
        """
    )

    def _display_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayPosition,
                        self.display_position)

    handle_size = traits.Float(15.0, enter_set=True, auto_set=False, help=\
        """
        Overload the superclasses set_handle_size() method to update
        internal variables.
        """
    )

    def _handle_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHandleSize,
                        self.handle_size)

    hot_spot_size = traits.Trait(0.05, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set the "hot spot" size; i.e., the region around the focus, in
        which the motion vector is used to control the constrained
        sliding action. Note the size is specified as a fraction of the
        length of the diagonal of the point widget's bounding box.
        """
    )

    def _hot_spot_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHotSpotSize,
                        self.hot_spot_size)

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    def _set_property(self, arg):
        old_val = self._get_property()
        self._wrap_call(self._vtk_obj.SetProperty,
                        deref_vtk(arg))
        self.trait_property_changed('property', old_val, arg)
    property = traits.Property(_get_property, _set_property, help=\
        """
        Set/Get the handle properties when unselected and selected.
        """
    )

    def _get_selected_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedProperty())
    def _set_selected_property(self, arg):
        old_val = self._get_selected_property()
        self._wrap_call(self._vtk_obj.SetSelectedProperty,
                        deref_vtk(arg))
        self.trait_property_changed('selected_property', old_val, arg)
    selected_property = traits.Property(_get_selected_property, _set_selected_property, help=\
        """
        Set/Get the handle properties when unselected and selected.
        """
    )

    sphere_radius = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _sphere_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSphereRadius,
                        self.sphere_radius)

    world_position = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set the position of the point in world and display coordinates.
        Note that if the position is set outside of the bounding box, it
        will be clamped to the boundary of the bounding box. This method
        overloads the superclasses' set_world_position() and
        set_display_position() in order to set the focal point of the
        cursor properly.
        """
    )

    def _world_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWorldPosition,
                        self.world_position)

    _updateable_traits_ = \
    (('translation_mode', 'GetTranslationMode'), ('active_representation',
    'GetActiveRepresentation'), ('constrained', 'GetConstrained'),
    ('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('display_position',
    'GetDisplayPosition'), ('handle_size', 'GetHandleSize'),
    ('hot_spot_size', 'GetHotSpotSize'), ('sphere_radius',
    'GetSphereRadius'), ('world_position', 'GetWorldPosition'),
    ('interaction_state', 'GetInteractionState'), ('tolerance',
    'GetTolerance'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['active_representation', 'constrained', 'debug', 'dragable',
    'global_warning_display', 'need_to_render', 'pickable',
    'picking_managed', 'translation_mode', 'use_bounds', 'visibility',
    'display_position', 'estimated_render_time', 'handle_size',
    'hot_spot_size', 'interaction_state', 'place_factor',
    'render_time_multiplier', 'sphere_radius', 'tolerance',
    'world_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SphereHandleRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SphereHandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['active_representation', 'constrained', 'need_to_render',
            'picking_managed', 'translation_mode', 'use_bounds', 'visibility'],
            [], ['display_position', 'estimated_render_time', 'handle_size',
            'hot_spot_size', 'interaction_state', 'place_factor',
            'render_time_multiplier', 'sphere_radius', 'tolerance',
            'world_position']),
            title='Edit SphereHandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SphereHandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


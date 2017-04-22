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

from tvtk.tvtk_classes.prop3d import Prop3D


class LightActor(Prop3D):
    """
    LightActor - a cone and a frustum to represent a spotlight.
    
    Superclass: Prop3D
    
    LightActor is a composite actor used to represent a spotlight. The
    cone angle is equal to the spotlight angle, the cone apex is at the
    position of the light, the direction of the light goes from the cone
    apex to the center of the base of the cone. The square frustum
    position is the light position, the frustum focal point is in the
    direction of the light direction. The frustum vertical view angle
    (aperture) (this is also the horizontal view angle as the frustum is
    square) is equal to twice the cone angle. The clipping range of the
    frustum is arbitrary set by the user (initially at 0.5,11.0).
    
    @warning
    Right now only spotlight are supported but directional light might be
    supported in the future.
    
    @sa
    Light ConeSource FrustumSource CameraActor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLightActor, obj, update, **traits)
    
    clipping_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.5, 10.0), cols=2, help=\
        """
        Set/Get the location of the near and far clipping planes along
        the direction of projection.  Both of these values must be
        positive. Initial values are  (0.5,11.0)
        """
    )

    def _clipping_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClippingRange,
                        self.clipping_range)

    def _get_light(self):
        return wrap_vtk(self._vtk_obj.GetLight())
    def _set_light(self, arg):
        old_val = self._get_light()
        self._wrap_call(self._vtk_obj.SetLight,
                        deref_vtk(arg))
        self.trait_property_changed('light', old_val, arg)
    light = traits.Property(_get_light, _set_light, help=\
        """
        The spotlight to represent. Initial value is NULL.
        """
    )

    _updateable_traits_ = \
    (('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('clipping_range', 'GetClippingRange'),
    ('orientation', 'GetOrientation'), ('origin', 'GetOrigin'),
    ('position', 'GetPosition'), ('scale', 'GetScale'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'clipping_range', 'estimated_render_time',
    'orientation', 'origin', 'position', 'render_time_multiplier',
    'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LightActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit LightActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_bounds', 'visibility'], [], ['clipping_range',
            'estimated_render_time', 'orientation', 'origin', 'position',
            'render_time_multiplier', 'scale']),
            title='Edit LightActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LightActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class Prop3DFollower(Prop3D):
    """
    Prop3DFollower - a Prop3D that always faces the camera
    
    Superclass: Prop3D
    
    Prop3DFollower is a type of Prop3D that always faces the
    camera. More specifically it will not change its position or scale,
    but it will continually update its orientation so that it is right
    side up and facing the camera. This is typically used for complex
    billboards or props that need to face the viewer at all times.
    
    Note: All of the transformations that can be made to a Prop3D will
    take effect with the follower. Thus, if you change the orientation of
    the follower by 90 degrees, then it will follow the camera, but be
    off by 90 degrees.
    
    @sa
    Follower Prop3D Camera Prop3DAxisFollower
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProp3DFollower, obj, update, **traits)
    
    def _get_camera(self):
        return wrap_vtk(self._vtk_obj.GetCamera())
    def _set_camera(self, arg):
        old_val = self._get_camera()
        self._wrap_call(self._vtk_obj.SetCamera,
                        deref_vtk(arg))
        self.trait_property_changed('camera', old_val, arg)
    camera = traits.Property(_get_camera, _set_camera, help=\
        """
        Set/Get the camera to follow. If this is not set, then the
        follower won't know what to follow and will act like a normal
        Prop3D.
        """
    )

    def _get_prop3d(self):
        return wrap_vtk(self._vtk_obj.GetProp3D())
    def _set_prop3d(self, arg):
        old_val = self._get_prop3d()
        self._wrap_call(self._vtk_obj.SetProp3D,
                        deref_vtk(arg))
        self.trait_property_changed('prop3d', old_val, arg)
    prop3d = traits.Property(_get_prop3d, _set_prop3d, help=\
        """
        Set/Get the Prop3D to control (i.e., face the camera).
        """
    )

    _updateable_traits_ = \
    (('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('orientation', 'GetOrientation'),
    ('origin', 'GetOrigin'), ('position', 'GetPosition'), ('scale',
    'GetScale'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'estimated_render_time', 'orientation',
    'origin', 'position', 'render_time_multiplier', 'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Prop3DFollower, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Prop3DFollower properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_bounds', 'visibility'], [], ['estimated_render_time',
            'orientation', 'origin', 'position', 'render_time_multiplier',
            'scale']),
            title='Edit Prop3DFollower properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Prop3DFollower properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


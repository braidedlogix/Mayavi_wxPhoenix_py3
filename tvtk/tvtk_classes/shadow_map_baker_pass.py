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

from tvtk.tvtk_classes.render_pass import RenderPass


class ShadowMapBakerPass(RenderPass):
    """
    ShadowMapBakerPass - Implement a builder of shadow map pass.
    
    Superclass: RenderPass
    
    Bake a list of shadow maps, once per spot light. It work in
    conjunction with the ShadowMapPass, which uses the shadow maps for
    rendering the opaque geometry (a technique to render hard shadows in
    hardware).
    
    This pass expects an initialized depth buffer and color buffer.
    Initialized buffers means they have been cleared with farest z-value
    and background color/gradient/transparent color. An opaque pass may
    have been performed right after the initialization.
    
    Its delegate is usually set to a OpaquePass.
    
    @par Implementation: The first pass of the algorithm is to generate a
    shadow map per light (depth map from the light point of view) by
    rendering the opaque objects
    
    @sa
    RenderPass, OpaquePass, ShadowMapPass
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkShadowMapBakerPass, obj, update, **traits)
    
    def _get_composite_z_pass(self):
        return wrap_vtk(self._vtk_obj.GetCompositeZPass())
    def _set_composite_z_pass(self, arg):
        old_val = self._get_composite_z_pass()
        self._wrap_call(self._vtk_obj.SetCompositeZPass,
                        deref_vtk(arg))
        self.trait_property_changed('composite_z_pass', old_val, arg)
    composite_z_pass = traits.Property(_get_composite_z_pass, _set_composite_z_pass, help=\
        """
        Delegate for compositing of the shadow maps across processors. If
        it is NULL, there is no z compositing. It is usually set to a
        CompositeZPass (Parallel package). Initial value is a NULL
        pointer.
        """
    )

    def _get_opaque_sequence(self):
        return wrap_vtk(self._vtk_obj.GetOpaqueSequence())
    def _set_opaque_sequence(self, arg):
        old_val = self._get_opaque_sequence()
        self._wrap_call(self._vtk_obj.SetOpaqueSequence,
                        deref_vtk(arg))
        self.trait_property_changed('opaque_sequence', old_val, arg)
    opaque_sequence = traits.Property(_get_opaque_sequence, _set_opaque_sequence, help=\
        """
        Delegate for rendering the camera, lights, and opaque geometry.
        If it is NULL, nothing will be rendered and a warning will be
        emitted. It defaults to a CameraPass with a sequence of
        LightPass/vtkOpaquePass.
        """
    )

    resolution = traits.Int(1024, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of pixels in each dimension of the shadow maps
        (shadow maps are square). Initial value is 256. The greater the
        better. Resolution does not have to be a power-of-two value.
        """
    )

    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

    def _get_has_shadows(self):
        return self._vtk_obj.GetHasShadows()
    has_shadows = traits.Property(_get_has_shadows, help=\
        """
        INTERNAL USE ONLY. Internally used by ShadowMapBakerPass and
        ShadowMapPass.
        
        * Tell if there is at least one shadow.
        * Initial value is false.
        """
    )

    def _get_need_update(self):
        return self._vtk_obj.GetNeedUpdate()
    need_update = traits.Property(_get_need_update, help=\
        """
        INTERNAL USE ONLY. Internally used by ShadowMapBakerPass and
        ShadowMapPass.
        
        * Do the shadows need to be updated?
        * Value changed by ShadowMapBakerPass and used by
          ShadowMapPass.
        * Initial value is true.
        """
    )

    def light_creates_shadow(self, *args):
        """
        V.light_creates_shadow(Light) -> bool
        C++: bool LightCreatesShadow(Light *l)
        INTERNAL USE ONLY. Internally used by ShadowMapBakerPass and
        ShadowMapPass.
        
        * Tell if the light `l' can create shadows.
        * The light has to not be a head light and to be directional or
        * positional with an angle less than 180 degrees.
        * \pre l_exists: l!=0
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.LightCreatesShadow, *my_args)
        return ret

    def set_up_to_date(self):
        """
        V.set_up_to_date()
        C++: void SetUpToDate()"""
        ret = self._vtk_obj.SetUpToDate()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('resolution', 'GetResolution'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ShadowMapBakerPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ShadowMapBakerPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['resolution']),
            title='Edit ShadowMapBakerPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ShadowMapBakerPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


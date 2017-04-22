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


class RenderStepsPass(RenderPass):
    """
    RenderStepsPass - Execute render passes sequentially.
    
    Superclass: RenderPass
    
    RenderStepsPass executes a standard list of render passes
    sequentially. This class allows to define a sequence of render passes
    at run time. You can set a step to NULL in order to skip that step.
    Likewise you can replace any of the default steps with your own step.
    Typically in such a case you would get the current step, replace it
    with your own and likely have your step call the current step as a
    delegate. For example to replace the translucent step with a
    depthpeeling step you would get the current tranlucent step and set
    it as a delegate on the depthpeeling step. Then set this classes
    translparent step to the depthpeelnig step.
    
    @sa
    RenderPass
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderStepsPass, obj, update, **traits)
    
    def _get_camera_pass(self):
        return wrap_vtk(self._vtk_obj.GetCameraPass())
    def _set_camera_pass(self, arg):
        old_val = self._get_camera_pass()
        self._wrap_call(self._vtk_obj.SetCameraPass,
                        deref_vtk(arg))
        self.trait_property_changed('camera_pass', old_val, arg)
    camera_pass = traits.Property(_get_camera_pass, _set_camera_pass, help=\
        """
        Get the render_pass used for the Camera Step
        """
    )

    def _get_lights_pass(self):
        return wrap_vtk(self._vtk_obj.GetLightsPass())
    def _set_lights_pass(self, arg):
        old_val = self._get_lights_pass()
        self._wrap_call(self._vtk_obj.SetLightsPass,
                        deref_vtk(arg))
        self.trait_property_changed('lights_pass', old_val, arg)
    lights_pass = traits.Property(_get_lights_pass, _set_lights_pass, help=\
        """
        Get the render_pass used for the Lights Step
        """
    )

    def _get_opaque_pass(self):
        return wrap_vtk(self._vtk_obj.GetOpaquePass())
    def _set_opaque_pass(self, arg):
        old_val = self._get_opaque_pass()
        self._wrap_call(self._vtk_obj.SetOpaquePass,
                        deref_vtk(arg))
        self.trait_property_changed('opaque_pass', old_val, arg)
    opaque_pass = traits.Property(_get_opaque_pass, _set_opaque_pass, help=\
        """
        Get the render_pass used for the Opaque Step
        """
    )

    def _get_overlay_pass(self):
        return wrap_vtk(self._vtk_obj.GetOverlayPass())
    def _set_overlay_pass(self, arg):
        old_val = self._get_overlay_pass()
        self._wrap_call(self._vtk_obj.SetOverlayPass,
                        deref_vtk(arg))
        self.trait_property_changed('overlay_pass', old_val, arg)
    overlay_pass = traits.Property(_get_overlay_pass, _set_overlay_pass, help=\
        """
        Get the render_pass used for the Overlay Step
        """
    )

    def _get_post_process_pass(self):
        return wrap_vtk(self._vtk_obj.GetPostProcessPass())
    def _set_post_process_pass(self, arg):
        old_val = self._get_post_process_pass()
        self._wrap_call(self._vtk_obj.SetPostProcessPass,
                        deref_vtk(arg))
        self.trait_property_changed('post_process_pass', old_val, arg)
    post_process_pass = traits.Property(_get_post_process_pass, _set_post_process_pass, help=\
        """
        Get the render_pass used for the post_process Step
        """
    )

    def _get_translucent_pass(self):
        return wrap_vtk(self._vtk_obj.GetTranslucentPass())
    def _set_translucent_pass(self, arg):
        old_val = self._get_translucent_pass()
        self._wrap_call(self._vtk_obj.SetTranslucentPass,
                        deref_vtk(arg))
        self.trait_property_changed('translucent_pass', old_val, arg)
    translucent_pass = traits.Property(_get_translucent_pass, _set_translucent_pass, help=\
        """
        Get the render_pass used for the translucent Step
        """
    )

    def _get_volumetric_pass(self):
        return wrap_vtk(self._vtk_obj.GetVolumetricPass())
    def _set_volumetric_pass(self, arg):
        old_val = self._get_volumetric_pass()
        self._wrap_call(self._vtk_obj.SetVolumetricPass,
                        deref_vtk(arg))
        self.trait_property_changed('volumetric_pass', old_val, arg)
    volumetric_pass = traits.Property(_get_volumetric_pass, _set_volumetric_pass, help=\
        """
        Get the render_pass used for the Volume Step
        """
    )

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderStepsPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderStepsPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit RenderStepsPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderStepsPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


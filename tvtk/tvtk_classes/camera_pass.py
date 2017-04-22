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


class CameraPass(RenderPass):
    """
    CameraPass - Implement the camera render pass.
    
    Superclass: RenderPass
    
    Render the camera.
    
    It setups the projection and modelview matrices and can clear the
    background It calls its delegate once. After its delegate returns, it
    restore the modelview matrix stack.
    
    Its delegate is usually set to a SequencePass with a LigthsPass
    and a list of passes for the geometry.
    
    @sa
    RenderPass
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCameraPass, obj, update, **traits)
    
    aspect_ratio_override = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Used to override the aspect ratio used when computing the
        projection matrix. This is useful when rendering for
        tile-displays for example.
        """
    )

    def _aspect_ratio_override_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAspectRatioOverride,
                        self.aspect_ratio_override)

    def _get_delegate_pass(self):
        return wrap_vtk(self._vtk_obj.GetDelegatePass())
    def _set_delegate_pass(self, arg):
        old_val = self._get_delegate_pass()
        self._wrap_call(self._vtk_obj.SetDelegatePass,
                        deref_vtk(arg))
        self.trait_property_changed('delegate_pass', old_val, arg)
    delegate_pass = traits.Property(_get_delegate_pass, _set_delegate_pass, help=\
        """
        Delegate for rendering the geometry. If it is NULL, nothing will
        be rendered and a warning will be emitted. It is usually set to a
        SequencePass with a LigthsPass and a list of passes for the
        geometry. Initial value is a NULL pointer.
        """
    )

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('aspect_ratio_override',
    'GetAspectRatioOverride'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'aspect_ratio_override'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CameraPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CameraPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['aspect_ratio_override']),
            title='Edit CameraPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CameraPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


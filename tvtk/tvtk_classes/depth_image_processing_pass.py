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

from tvtk.tvtk_classes.image_processing_pass import ImageProcessingPass


class DepthImageProcessingPass(ImageProcessingPass):
    """
    DepthImageProcessingPass - Convenient class for post-processing
    passes.
    
    Superclass: ImageProcessingPass
    
    Based on ImageProcessingPass, but writes depth as well in a
    texture
    
    Abstract class with some convenient methods frequently used in
    subclasses.
    
    @sa
    RenderPass DepthImageProcessingPass EDLShading
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDepthImageProcessingPass, obj, update, **traits)
    
    def _get_delegate_pass(self):
        return wrap_vtk(self._vtk_obj.GetDelegatePass())
    def _set_delegate_pass(self, arg):
        old_val = self._get_delegate_pass()
        self._wrap_call(self._vtk_obj.SetDelegatePass,
                        deref_vtk(arg))
        self.trait_property_changed('delegate_pass', old_val, arg)
    delegate_pass = traits.Property(_get_delegate_pass, _set_delegate_pass, help=\
        """
        Delegate for rendering the image to be processed. If it is NULL,
        nothing will be rendered and a warning will be emitted. It is
        usually set to a CameraPass or to a post-processing pass.
        Initial value is a NULL pointer.
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
            return super(DepthImageProcessingPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DepthImageProcessingPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit DepthImageProcessingPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DepthImageProcessingPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


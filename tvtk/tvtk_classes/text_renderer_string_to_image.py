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

from tvtk.tvtk_classes.string_to_image import StringToImage


class TextRendererStringToImage(StringToImage):
    """
    TextRendererStringToImage - uses TextRenderer to render the
    supplied text to an image.
    
    Superclass: StringToImage
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextRendererStringToImage, obj, update, **traits)
    
    scale_to_power_of_two = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Should we produce images at powers of 2, makes rendering on old
        open_gl hardware easier. Default is false.
        """
    )

    def _scale_to_power_of_two_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleToPowerOfTwo,
                        self.scale_to_power_of_two)

    def deep_copy(self, *args):
        """
        V.deep_copy(TextRendererStringToImage)
        C++: void DeepCopy(TextRendererStringToImage *utility)
        Make a deep copy of the supplied utility class.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('scale_to_power_of_two',
    'GetScaleToPowerOfTwo'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'scale_to_power_of_two'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextRendererStringToImage, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TextRendererStringToImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['scale_to_power_of_two']),
            title='Edit TextRendererStringToImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextRendererStringToImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.image_slice import ImageSlice


class ImageStack(ImageSlice):
    """
    ImageStack - manages a stack of composited images
    
    Superclass: ImageSlice
    
    ImageStack manages the compositing of a set of images. Each image
    is assigned a layer number through its property object, and it is
    this layer number that determines the compositing order: images with
    a higher layer number are drawn over top of images with a lower layer
    number.  The image stack has a set_active_layer method for controlling
    which layer to use for interaction and picking.@par Thanks: Thanks to
    David Gobbi at the Seaman Family MR Centre and Dept. of Clinical
    Neurosciences, Foothills Medical Centre, Calgary, for providing this
    class.
    @sa
    ImageMapper3D ImageProperty Prop3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageStack, obj, update, **traits)
    
    active_layer = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the active layer number.  This is the layer that will be used
        for picking and interaction.
        """
    )

    def _active_layer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetActiveLayer,
                        self.active_layer)

    def _get_mapper(self):
        return wrap_vtk(self._vtk_obj.GetMapper())
    def _set_mapper(self, arg):
        old_val = self._get_mapper()
        self._wrap_call(self._vtk_obj.SetMapper,
                        deref_vtk(arg))
        self.trait_property_changed('mapper', old_val, arg)
    mapper = traits.Property(_get_mapper, _set_mapper, help=\
        """
        Get the mapper for the currently active image.
        """
    )

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    def _set_property(self, arg):
        old_val = self._get_property()
        self._wrap_call(self._vtk_obj.SetProperty,
                        deref_vtk(arg))
        self.trait_property_changed('property', old_val, arg)
    property = traits.Property(_get_property, _set_property, help=\
        """
        Get the property for the currently active image.
        """
    )

    def _get_active_image(self):
        return wrap_vtk(self._vtk_obj.GetActiveImage())
    active_image = traits.Property(_get_active_image, help=\
        """
        Get the active image.  This will be the topmost image whose
        layer_number is the active_layer.  If no image matches, then NULL
        will be returned.
        """
    )

    def add_image(self, *args):
        """
        V.add_image(ImageSlice)
        C++: void AddImage(ImageSlice *prop)
        Add an image to the stack.  If the image is already present, then
        this method will do nothing.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddImage, *my_args)
        return ret

    def has_image(self, *args):
        """
        V.has_image(ImageSlice) -> int
        C++: int HasImage(ImageSlice *prop)
        Check if an image is present.  The returned value is one or zero.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HasImage, *my_args)
        return ret

    def remove_image(self, *args):
        """
        V.remove_image(ImageSlice)
        C++: void RemoveImage(ImageSlice *prop)
        Remove an image from the stack.  If the image is not present,
        then this method will do nothing.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveImage, *my_args)
        return ret

    _updateable_traits_ = \
    (('force_translucent', 'GetForceTranslucent'), ('dragable',
    'GetDragable'), ('pickable', 'GetPickable'), ('use_bounds',
    'GetUseBounds'), ('visibility', 'GetVisibility'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('active_layer', 'GetActiveLayer'), ('orientation', 'GetOrientation'),
    ('origin', 'GetOrigin'), ('position', 'GetPosition'), ('scale',
    'GetScale'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'force_translucent', 'global_warning_display',
    'pickable', 'use_bounds', 'visibility', 'active_layer',
    'estimated_render_time', 'orientation', 'origin', 'position',
    'render_time_multiplier', 'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageStack, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageStack properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['force_translucent', 'use_bounds', 'visibility'], [],
            ['active_layer', 'estimated_render_time', 'orientation', 'origin',
            'position', 'render_time_multiplier', 'scale']),
            title='Edit ImageStack properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageStack properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


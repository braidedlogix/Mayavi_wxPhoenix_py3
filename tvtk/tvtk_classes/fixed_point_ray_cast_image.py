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

from tvtk.tvtk_classes.object import Object


class FixedPointRayCastImage(Object):
    """
    FixedPointRayCastImage - helper class for a ray cast image
    
    Superclass: Object
    
    This is a helper class for storing the ray cast image including the
    underlying data and the size of the image. This class is not intended
    to be used directly - just as an internal class in the
    FixedPointVolumeRayCastMapper so that multiple mappers can share
    the same image. This class also stored the ZBuffer (if necessary due
    to intermixed geometry). Perhaps this class could be generalized in
    the future to be used for other ray cast methods other than the fixed
    point method.
    
    @sa
    FixedPointVolumeRayCastMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFixedPointRayCastImage, obj, update, **traits)
    
    use_z_buffer = tvtk_base.false_bool_trait(help=\
        """
        The use_z_buffer flag indicates whether the ZBuffer is in use. The
        ZBuffer is captured and used when intermix_intersecting_geometry is
        on in the mapper, and when there are props that have been
        rendered before the current volume.
        """
    )

    def _use_z_buffer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseZBuffer,
                        self.use_z_buffer_)

    image_in_use_size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _image_in_use_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageInUseSize,
                        self.image_in_use_size)

    image_memory_size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _image_memory_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageMemorySize,
                        self.image_memory_size)

    image_origin = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _image_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageOrigin,
                        self.image_origin)

    image_sample_distance = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set / Get the image_sample_distance that will be used for
        rendering. This is a copy of the value stored in the mapper. It
        is stored here for sharing between all mappers that are
        participating in the creation of this image.
        """
    )

    def _image_sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageSampleDistance,
                        self.image_sample_distance)

    image_viewport_size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _image_viewport_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageViewportSize,
                        self.image_viewport_size)

    z_buffer_origin = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _z_buffer_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZBufferOrigin,
                        self.z_buffer_origin)

    z_buffer_size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _z_buffer_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZBufferSize,
                        self.z_buffer_size)

    def _get_image(self):
        return self._vtk_obj.GetImage()
    image = traits.Property(_get_image, help=\
        """
        Get the internal storage for the image. It is a pointer to
        unsigned short with four components (RGBA) per pixel. This memory
        is allocated when the allocate_image method is called.
        """
    )

    def _get_use_z_buffer_max_value(self):
        return self._vtk_obj.GetUseZBufferMaxValue()
    use_z_buffer_max_value = traits.Property(_get_use_z_buffer_max_value, help=\
        """
        The use_z_buffer flag indicates whether the ZBuffer is in use. The
        ZBuffer is captured and used when intermix_intersecting_geometry is
        on in the mapper, and when there are props that have been
        rendered before the current volume.
        """
    )

    def _get_use_z_buffer_min_value(self):
        return self._vtk_obj.GetUseZBufferMinValue()
    use_z_buffer_min_value = traits.Property(_get_use_z_buffer_min_value, help=\
        """
        The use_z_buffer flag indicates whether the ZBuffer is in use. The
        ZBuffer is captured and used when intermix_intersecting_geometry is
        on in the mapper, and when there are props that have been
        rendered before the current volume.
        """
    )

    def _get_z_buffer(self):
        return self._vtk_obj.GetZBuffer()
    z_buffer = traits.Property(_get_z_buffer, help=\
        """
        Get the ZBuffer. The size of the ZBuffer should be specific with
        set_z_buffer_size, and allocate_z_buffer method should be called
        before getting the ZBuffer.
        """
    )

    def get_z_buffer_value(self, *args):
        """
        V.get_z_buffer_value(int, int) -> float
        C++: float GetZBufferValue(int x, int y)
        Get the ZBuffer value corresponding to location (x,y) where (x,y)
        are indexing into the image_in_use image. This must be converted to
        the zbuffer image coordinates. Nearest neighbor value is
        returned. If use_z_buffer is off, then 1.0 is always returned.
        """
        ret = self._wrap_call(self._vtk_obj.GetZBufferValue, *args)
        return ret

    def allocate_image(self):
        """
        V.allocate_image()
        C++: void AllocateImage()
        Call this method once the image_memory_size has been set the
        allocate the image. If an image already exists, it will be
        deleted first.
        """
        ret = self._vtk_obj.AllocateImage()
        return ret
        

    def allocate_z_buffer(self):
        """
        V.allocate_z_buffer()
        C++: void AllocateZBuffer()"""
        ret = self._vtk_obj.AllocateZBuffer()
        return ret
        

    def clear_image(self):
        """
        V.clear_image()
        C++: void ClearImage()
        Clear the image to (0,0,0,0) for each pixel.
        """
        ret = self._vtk_obj.ClearImage()
        return ret
        

    _updateable_traits_ = \
    (('use_z_buffer', 'GetUseZBuffer'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('image_in_use_size', 'GetImageInUseSize'), ('image_memory_size',
    'GetImageMemorySize'), ('image_origin', 'GetImageOrigin'),
    ('image_sample_distance', 'GetImageSampleDistance'),
    ('image_viewport_size', 'GetImageViewportSize'), ('z_buffer_origin',
    'GetZBufferOrigin'), ('z_buffer_size', 'GetZBufferSize'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'use_z_buffer',
    'image_in_use_size', 'image_memory_size', 'image_origin',
    'image_sample_distance', 'image_viewport_size', 'z_buffer_origin',
    'z_buffer_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FixedPointRayCastImage, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FixedPointRayCastImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_z_buffer'], [], ['image_in_use_size', 'image_memory_size',
            'image_origin', 'image_sample_distance', 'image_viewport_size',
            'z_buffer_origin', 'z_buffer_size']),
            title='Edit FixedPointRayCastImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FixedPointRayCastImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


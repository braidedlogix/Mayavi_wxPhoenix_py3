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


class ImageActor(ImageSlice):
    """
    ImageActor - draw an image in a rendered 3d scene
    
    Superclass: ImageSlice
    
    ImageActor is used to render an image in a 3d scene.  The image is
    placed at the origin of the image, and its size is controlled by the
    image dimensions and image spacing. The orientation of the image is
    orthogonal to one of the x-y-z axes depending on which plane the
    image is defined in.  This class has been mostly superseded by the
    ImageSlice class, which provides more functionality than
    ImageActor.
    
    @sa
    ImageData ImageSliceMapper ImageProperty
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageActor, obj, update, **traits)
    
    force_opaque = tvtk_base.false_bool_trait(help=\
        """
        Force the actor to be rendered during the opaque rendering pass.
        See also: force_translucent_on() to use translucent rendering pass.
        """
    )

    def _force_opaque_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForceOpaque,
                        self.force_opaque_)

    interpolate = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off linear interpolation of the image when rendering.
        More options are available in the Property of the image actor.
        """
    )

    def _interpolate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolate,
                        self.interpolate_)

    display_extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(0, -1, 0, -1, 0, -1), cols=3, help=\
        """
        The image extent is generally set explicitly, but if not set it
        will be determined from the input image data.
        """
    )

    def _display_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayExtent,
                        self.display_extent)

    opacity = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the object's opacity. 1.0 is totally opaque and 0.0 is
        completely transparent.
        """
    )

    def _opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOpacity,
                        self.opacity)

    z_slice = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the current slice number. The axis Z in ZSlice does not
        necessarily have any relation to the z axis of the data on disk.
        It is simply the axis orthogonal to the x,y, display plane.
        get_whole_z_max and Min are convenience methods for obtaining the
        number of slices that can be displayed. Again the number of
        slices is in reference to the display z axis, which is not
        necessarily the z axis on disk. (due to reformatting etc)
        """
    )

    def _z_slice_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZSlice,
                        self.z_slice)

    def _get_display_bounds(self):
        return self._vtk_obj.GetDisplayBounds()
    display_bounds = traits.Property(_get_display_bounds, help=\
        """
        Get the bounds of the data that is displayed by this image actor.
         If the transformation matrix for this actor is the identity
        matrix, this will return the same value as get_bounds.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the image data input for the image actor.  This is for
        backwards compatibility, for a proper pipeline connection you
        should use get_mapper()->_set_input_connection() instead.
        """
    )

    def _get_slice_number(self):
        return self._vtk_obj.GetSliceNumber()
    slice_number = traits.Property(_get_slice_number, help=\
        """
        Return the slice number (& min/max slice number) computed from
        the display extent.
        """
    )

    def _get_slice_number_max(self):
        return self._vtk_obj.GetSliceNumberMax()
    slice_number_max = traits.Property(_get_slice_number_max, help=\
        """
        Return the slice number (& min/max slice number) computed from
        the display extent.
        """
    )

    def _get_slice_number_min(self):
        return self._vtk_obj.GetSliceNumberMin()
    slice_number_min = traits.Property(_get_slice_number_min, help=\
        """
        Return the slice number (& min/max slice number) computed from
        the display extent.
        """
    )

    def _get_whole_z_max(self):
        return self._vtk_obj.GetWholeZMax()
    whole_z_max = traits.Property(_get_whole_z_max, help=\
        """
        Set/Get the current slice number. The axis Z in ZSlice does not
        necessarily have any relation to the z axis of the data on disk.
        It is simply the axis orthogonal to the x,y, display plane.
        get_whole_z_max and Min are convenience methods for obtaining the
        number of slices that can be displayed. Again the number of
        slices is in reference to the display z axis, which is not
        necessarily the z axis on disk. (due to reformatting etc)
        """
    )

    def _get_whole_z_min(self):
        return self._vtk_obj.GetWholeZMin()
    whole_z_min = traits.Property(_get_whole_z_min, help=\
        """
        Set/Get the current slice number. The axis Z in ZSlice does not
        necessarily have any relation to the z axis of the data on disk.
        It is simply the axis orthogonal to the x,y, display plane.
        get_whole_z_max and Min are convenience methods for obtaining the
        number of slices that can be displayed. Again the number of
        slices is in reference to the display z axis, which is not
        necessarily the z axis on disk. (due to reformatting etc)
        """
    )

    def set_input_data(self, *args):
        """
        V.set_input_data(ImageData)
        C++: virtual void SetInputData(ImageData *)
        Set/Get the image data input for the image actor.  This is for
        backwards compatibility, for a proper pipeline connection you
        should use get_mapper()->_set_input_connection() instead.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    _updateable_traits_ = \
    (('force_opaque', 'GetForceOpaque'), ('interpolate',
    'GetInterpolate'), ('force_translucent', 'GetForceTranslucent'),
    ('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('display_extent', 'GetDisplayExtent'),
    ('opacity', 'GetOpacity'), ('z_slice', 'GetZSlice'), ('orientation',
    'GetOrientation'), ('origin', 'GetOrigin'), ('position',
    'GetPosition'), ('scale', 'GetScale'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'force_opaque', 'force_translucent',
    'global_warning_display', 'interpolate', 'pickable', 'use_bounds',
    'visibility', 'display_extent', 'estimated_render_time', 'opacity',
    'orientation', 'origin', 'position', 'render_time_multiplier',
    'scale', 'z_slice'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['force_opaque', 'force_translucent', 'interpolate',
            'use_bounds', 'visibility'], [], ['display_extent',
            'estimated_render_time', 'opacity', 'orientation', 'origin',
            'position', 'render_time_multiplier', 'scale', 'z_slice']),
            title='Edit ImageActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


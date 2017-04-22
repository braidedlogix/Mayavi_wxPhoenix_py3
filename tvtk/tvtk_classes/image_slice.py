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


class ImageSlice(Prop3D):
    """
    ImageSlice - represents an image in a 3d scene
    
    Superclass: Prop3D
    
    ImageSlice is used to represent an image in a 3d scene.  It
    displays the image either as a slice or as a projection from the
    camera's perspective. Adjusting the position and orientation of the
    slice is done by adjusting the focal point and direction of the
    camera, or alternatively the slice can be set manually in
    ImageMapper3D. The lookup table and window/leve are set in
    ImageProperty. prop3d methods such as set_position() and
    rotate_wxyz() change the position and orientation of the data with
    respect to VTK world coordinates.@par Thanks: Thanks to David Gobbi
    at the Seaman Family MR Centre and Dept. of Clinical Neurosciences,
    Foothills Medical Centre, Calgary, for providing this class.
    @sa
    ImageMapper3D ImageProperty Prop3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageSlice, obj, update, **traits)
    
    force_translucent = tvtk_base.false_bool_trait(help=\
        """
        Force the actor to be treated as translucent.
        """
    )

    def _force_translucent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForceTranslucent,
                        self.force_translucent_)

    def _get_mapper(self):
        return wrap_vtk(self._vtk_obj.GetMapper())
    def _set_mapper(self, arg):
        old_val = self._get_mapper()
        self._wrap_call(self._vtk_obj.SetMapper,
                        deref_vtk(arg))
        self.trait_property_changed('mapper', old_val, arg)
    mapper = traits.Property(_get_mapper, _set_mapper, help=\
        """
        Set/Get the mapper.
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
        Set/Get the image display properties.
        """
    )

    def get_images(self, *args):
        """
        V.get_images(PropCollection)
        C++: void GetImages(PropCollection *)
        For some exporters and other other operations we must be able to
        collect all the actors, volumes, and images. These methods are
        used in that process.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetImages, *my_args)
        return ret

    def _get_max_x_bound(self):
        return self._vtk_obj.GetMaxXBound()
    max_x_bound = traits.Property(_get_max_x_bound, help=\
        """
        Get the bounds - either all six at once (xmin, xmax, ymin, ymax,
        zmin, zmax) or one at a time.
        """
    )

    def _get_max_y_bound(self):
        return self._vtk_obj.GetMaxYBound()
    max_y_bound = traits.Property(_get_max_y_bound, help=\
        """
        Get the bounds - either all six at once (xmin, xmax, ymin, ymax,
        zmin, zmax) or one at a time.
        """
    )

    def _get_max_z_bound(self):
        return self._vtk_obj.GetMaxZBound()
    max_z_bound = traits.Property(_get_max_z_bound, help=\
        """
        Get the bounds - either all six at once (xmin, xmax, ymin, ymax,
        zmin, zmax) or one at a time.
        """
    )

    def _get_min_x_bound(self):
        return self._vtk_obj.GetMinXBound()
    min_x_bound = traits.Property(_get_min_x_bound, help=\
        """
        Get the bounds - either all six at once (xmin, xmax, ymin, ymax,
        zmin, zmax) or one at a time.
        """
    )

    def _get_min_y_bound(self):
        return self._vtk_obj.GetMinYBound()
    min_y_bound = traits.Property(_get_min_y_bound, help=\
        """
        Get the bounds - either all six at once (xmin, xmax, ymin, ymax,
        zmin, zmax) or one at a time.
        """
    )

    def _get_min_z_bound(self):
        return self._vtk_obj.GetMinZBound()
    min_z_bound = traits.Property(_get_min_z_bound, help=\
        """
        Get the bounds - either all six at once (xmin, xmax, ymin, ymax,
        zmin, zmax) or one at a time.
        """
    )

    def render(self, *args):
        """
        V.render(Renderer)
        C++: virtual void Render(Renderer *)
        This causes the image and its mapper to be rendered. Note that a
        side effect of this method is that the pipeline will be updated.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Render, *my_args)
        return ret

    def set_stacked_image_pass(self, *args):
        """
        V.set_stacked_image_pass(int)
        C++: void SetStackedImagePass(int pass)
        For stacked image rendering, set the pass.  The first pass
        renders just the backing polygon, the second pass renders the
        image, and the third pass renders the depth buffer. Set to -1 to
        render all of these in the same pass.
        """
        ret = self._wrap_call(self._vtk_obj.SetStackedImagePass, *args)
        return ret

    def update(self):
        """
        V.update()
        C++: void Update()
        Update the rendering pipeline by updating the image_mapper
        """
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('force_translucent', 'GetForceTranslucent'), ('dragable',
    'GetDragable'), ('pickable', 'GetPickable'), ('use_bounds',
    'GetUseBounds'), ('visibility', 'GetVisibility'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('orientation', 'GetOrientation'), ('origin', 'GetOrigin'),
    ('position', 'GetPosition'), ('scale', 'GetScale'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'force_translucent', 'global_warning_display',
    'pickable', 'use_bounds', 'visibility', 'estimated_render_time',
    'orientation', 'origin', 'position', 'render_time_multiplier',
    'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageSlice, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageSlice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['force_translucent', 'use_bounds', 'visibility'], [],
            ['estimated_render_time', 'orientation', 'origin', 'position',
            'render_time_multiplier', 'scale']),
            title='Edit ImageSlice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageSlice properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


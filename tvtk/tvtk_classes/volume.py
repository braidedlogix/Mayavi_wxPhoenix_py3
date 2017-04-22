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


class Volume(Prop3D):
    """
    Volume - represents a volume (data & properties) in a rendered
    scene
    
    Superclass: Prop3D
    
    Volume is used to represent a volumetric entity in a rendering
    scene. It inherits functions related to the volume's position,
    orientation and origin from Prop3D. The volume maintains a
    reference to the volumetric data (i.e., the volume mapper). The
    volume also contains a reference to a volume property which contains
    all common volume rendering parameters.
    
    @sa
    AbstractVolumeMapper VolumeProperty Prop3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolume, obj, update, **traits)
    
    def _get_mapper(self):
        return wrap_vtk(self._vtk_obj.GetMapper())
    def _set_mapper(self, arg):
        old_val = self._get_mapper()
        self._wrap_call(self._vtk_obj.SetMapper,
                        deref_vtk(arg))
        self.trait_property_changed('mapper', old_val, arg)
    mapper = traits.Property(_get_mapper, _set_mapper, help=\
        """
        Set/Get the volume mapper.
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
        Set/Get the volume property.
        """
    )

    def _get_array_size(self):
        return self._vtk_obj.GetArraySize()
    array_size = traits.Property(_get_array_size, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS
        """
    )

    def _get_corrected_scalar_opacity_array(self):
        return self._vtk_obj.GetCorrectedScalarOpacityArray()
    corrected_scalar_opacity_array = traits.Property(_get_corrected_scalar_opacity_array, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS
        """
    )

    def _get_gradient_opacity_array(self):
        return self._vtk_obj.GetGradientOpacityArray()
    gradient_opacity_array = traits.Property(_get_gradient_opacity_array, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS
        """
    )

    def _get_gradient_opacity_constant(self):
        return self._vtk_obj.GetGradientOpacityConstant()
    gradient_opacity_constant = traits.Property(_get_gradient_opacity_constant, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS
        """
    )

    def _get_gray_array(self):
        return self._vtk_obj.GetGrayArray()
    gray_array = traits.Property(_get_gray_array, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS
        """
    )

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

    def _get_rgb_array(self):
        return self._vtk_obj.GetRGBArray()
    rgb_array = traits.Property(_get_rgb_array, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS
        """
    )

    def _get_scalar_opacity_array(self):
        return self._vtk_obj.GetScalarOpacityArray()
    scalar_opacity_array = traits.Property(_get_scalar_opacity_array, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS
        """
    )

    def update(self):
        """
        V.update()
        C++: void Update()
        Update the volume rendering pipeline by updating the volume
        mapper
        """
        ret = self._vtk_obj.Update()
        return ret
        

    def update_scalar_opacityfor_sample_size(self, *args):
        """
        V.update_scalar_opacityfor_sample_size(Renderer, float)
        C++: void UpdateScalarOpacityforSampleSize(Renderer *ren,
            float sample_distance)
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UpdateScalarOpacityforSampleSize, *my_args)
        return ret

    def update_transfer_functions(self, *args):
        """
        V.update_transfer_functions(Renderer)
        C++: void UpdateTransferFunctions(Renderer *ren)
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UpdateTransferFunctions, *my_args)
        return ret

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
            return super(Volume, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Volume properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_bounds', 'visibility'], [], ['estimated_render_time',
            'orientation', 'origin', 'position', 'render_time_multiplier',
            'scale']),
            title='Edit Volume properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Volume properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


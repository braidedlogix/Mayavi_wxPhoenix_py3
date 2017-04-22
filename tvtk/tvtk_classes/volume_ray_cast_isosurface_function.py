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

from tvtk.tvtk_classes.volume_ray_cast_function import VolumeRayCastFunction


class VolumeRayCastIsosurfaceFunction(VolumeRayCastFunction):
    """
    VolumeRayCastIsosurfaceFunction - An isosurface ray caster for
    volumes
    
    Superclass: VolumeRayCastFunction
    
    VolumeRayCastIsosurfaceFunction is a volume ray cast function that
    intersects a ray with an analytic isosurface in a scalar field. The
    color and shading parameters are defined in the VolumeProperty of
    the Volume, as well as the interpolation type to use when locating
    the surface (either a nearest neighbor approach or a tri-linear
    interpolation approach)
    
    @sa
    VolumeRayCastFunction VolumeRayCastMapper VolumeProperty
    VolumeRayCastCompositeFunction VolumeRayCastMIPFunction
    Volume VolumeProperty@deprecated
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeRayCastIsosurfaceFunction, obj, update, **traits)
    
    iso_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the value of iso_value.
        """
    )

    def _iso_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIsoValue,
                        self.iso_value)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('iso_value', 'GetIsoValue'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'iso_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeRayCastIsosurfaceFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeRayCastIsosurfaceFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['iso_value']),
            title='Edit VolumeRayCastIsosurfaceFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeRayCastIsosurfaceFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


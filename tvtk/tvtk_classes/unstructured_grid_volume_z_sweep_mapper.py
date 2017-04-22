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

from tvtk.tvtk_classes.unstructured_grid_volume_mapper import UnstructuredGridVolumeMapper


class UnstructuredGridVolumeZSweepMapper(UnstructuredGridVolumeMapper):
    """
    UnstructuredGridVolumeZSweepMapper - Unstructured grid volume
    mapper based the ZSweep Algorithm
    
    Superclass: UnstructuredGridVolumeMapper
    
    This is a volume mapper for unstructured grid implemented with the
    ZSweep algorithm. This is a software projective method.
    
    @sa
    VolumetMapper
    
    @par Background: The algorithm is described in the following paper:
    Ricardo Farias, Joseph S. B. Mitchell and Claudio T. Silva. ZSWEEP:
    An Efficient and Exact Projection Algorithm for Unstructured Volume
    Rendering. In 2000 Volume Visualization Symposium, pages 91--99.
    October 2000. http://www.cse.ogi.edu/~csilva/papers/volvis2000.pdf
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGridVolumeZSweepMapper, obj, update, **traits)
    
    auto_adjust_sample_distances = tvtk_base.true_bool_trait(help=\
        """
        If auto_adjust_sample_distances is on, the the image_sample_distance
        will be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
    )

    def _auto_adjust_sample_distances_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoAdjustSampleDistances,
                        self.auto_adjust_sample_distances_)

    intermix_intersecting_geometry = tvtk_base.true_bool_trait(help=\
        """
        If intermix_intersecting_geometry is turned on, the zbuffer will be
        captured and used to limit the traversal of the rays.
        """
    )

    def _intermix_intersecting_geometry_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntermixIntersectingGeometry,
                        self.intermix_intersecting_geometry_)

    image_sample_distance = traits.Trait(1.0, traits.Range(0.10000000149011612, 100.0, enter_set=True, auto_set=False), help=\
        """
        Sampling distance in the XY image dimensions. Default value of 1
        meaning 1 ray cast per pixel. If set to 0.5, 4 rays will be cast
        per pixel. If set to 2.0, 1 ray will be cast for every 4 (2 by 2)
        pixels.
        """
    )

    def _image_sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageSampleDistance,
                        self.image_sample_distance)

    max_pixel_list_size = traits.Int(64, enter_set=True, auto_set=False, help=\
        """
        Change the maximum size allowed for a pixel list. It is an
        advanced parameter.
        \pre positive_size: size>1
        """
    )

    def _max_pixel_list_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxPixelListSize,
                        self.max_pixel_list_size)

    maximum_image_sample_distance = traits.Trait(10.0, traits.Range(0.10000000149011612, 100.0, enter_set=True, auto_set=False), help=\
        """
        This is the maximum image sample distance allow when the image
        sample distance is being automatically adjusted
        """
    )

    def _maximum_image_sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumImageSampleDistance,
                        self.maximum_image_sample_distance)

    minimum_image_sample_distance = traits.Trait(1.0, traits.Range(0.10000000149011612, 100.0, enter_set=True, auto_set=False), help=\
        """
        This is the minimum image sample distance allow when the image
        sample distance is being automatically adjusted
        """
    )

    def _minimum_image_sample_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumImageSampleDistance,
                        self.minimum_image_sample_distance)

    def _get_ray_integrator(self):
        return wrap_vtk(self._vtk_obj.GetRayIntegrator())
    def _set_ray_integrator(self, arg):
        old_val = self._get_ray_integrator()
        self._wrap_call(self._vtk_obj.SetRayIntegrator,
                        deref_vtk(arg))
        self.trait_property_changed('ray_integrator', old_val, arg)
    ray_integrator = traits.Property(_get_ray_integrator, _set_ray_integrator, help=\
        """
        Set/Get the helper class for integrating rays.  If set to NULL, a
        default integrator will be assigned.
        """
    )

    def _get_auto_adjust_sample_distances_max_value(self):
        return self._vtk_obj.GetAutoAdjustSampleDistancesMaxValue()
    auto_adjust_sample_distances_max_value = traits.Property(_get_auto_adjust_sample_distances_max_value, help=\
        """
        If auto_adjust_sample_distances is on, the the image_sample_distance
        will be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
    )

    def _get_auto_adjust_sample_distances_min_value(self):
        return self._vtk_obj.GetAutoAdjustSampleDistancesMinValue()
    auto_adjust_sample_distances_min_value = traits.Property(_get_auto_adjust_sample_distances_min_value, help=\
        """
        If auto_adjust_sample_distances is on, the the image_sample_distance
        will be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
    )

    def _get_image_in_use_size(self):
        return self._vtk_obj.GetImageInUseSize()
    image_in_use_size = traits.Property(_get_image_in_use_size, help=\
        """
        
        """
    )

    def _get_image_origin(self):
        return self._vtk_obj.GetImageOrigin()
    image_origin = traits.Property(_get_image_origin, help=\
        """
        
        """
    )

    def _get_image_viewport_size(self):
        return self._vtk_obj.GetImageViewportSize()
    image_viewport_size = traits.Property(_get_image_viewport_size, help=\
        """
        
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input data
        """
    )

    def _get_intermix_intersecting_geometry_max_value(self):
        return self._vtk_obj.GetIntermixIntersectingGeometryMaxValue()
    intermix_intersecting_geometry_max_value = traits.Property(_get_intermix_intersecting_geometry_max_value, help=\
        """
        If intermix_intersecting_geometry is turned on, the zbuffer will be
        captured and used to limit the traversal of the rays.
        """
    )

    def _get_intermix_intersecting_geometry_min_value(self):
        return self._vtk_obj.GetIntermixIntersectingGeometryMinValue()
    intermix_intersecting_geometry_min_value = traits.Property(_get_intermix_intersecting_geometry_min_value, help=\
        """
        If intermix_intersecting_geometry is turned on, the zbuffer will be
        captured and used to limit the traversal of the rays.
        """
    )

    _updateable_traits_ = \
    (('auto_adjust_sample_distances', 'GetAutoAdjustSampleDistances'),
    ('intermix_intersecting_geometry', 'GetIntermixIntersectingGeometry'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('blend_mode',
    'GetBlendMode'), ('scalar_mode', 'GetScalarMode'),
    ('image_sample_distance', 'GetImageSampleDistance'),
    ('max_pixel_list_size', 'GetMaxPixelListSize'),
    ('maximum_image_sample_distance', 'GetMaximumImageSampleDistance'),
    ('minimum_image_sample_distance', 'GetMinimumImageSampleDistance'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_adjust_sample_distances', 'debug',
    'global_warning_display', 'intermix_intersecting_geometry',
    'release_data_flag', 'blend_mode', 'scalar_mode',
    'image_sample_distance', 'max_pixel_list_size',
    'maximum_image_sample_distance', 'minimum_image_sample_distance',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UnstructuredGridVolumeZSweepMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGridVolumeZSweepMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_adjust_sample_distances',
            'intermix_intersecting_geometry'], ['blend_mode', 'scalar_mode'],
            ['image_sample_distance', 'max_pixel_list_size',
            'maximum_image_sample_distance', 'minimum_image_sample_distance']),
            title='Edit UnstructuredGridVolumeZSweepMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGridVolumeZSweepMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


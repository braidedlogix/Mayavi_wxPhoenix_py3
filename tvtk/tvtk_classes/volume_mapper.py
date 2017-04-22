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

from tvtk.tvtk_classes.abstract_volume_mapper import AbstractVolumeMapper


class VolumeMapper(AbstractVolumeMapper):
    """
    VolumeMapper - Abstract class for a volume mapper
    
    Superclass: AbstractVolumeMapper
    
    VolumeMapper is the abstract definition of a volume mapper for
    regular rectilinear data (vtk_image_data).  Several  basic types of
    volume mappers are supported.
    
    @sa
    VolumeRayCastMapper VolumeTextureMapper2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeMapper, obj, update, **traits)
    
    cropping = tvtk_base.false_bool_trait(help=\
        """
        Turn On/Off orthogonal cropping. (Clipping planes are
        perpendicular to the coordinate axes.)
        """
    )

    def _cropping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCropping,
                        self.cropping_)

    blend_mode = traits.Trait('composite',
    tvtk_base.TraitRevPrefixMap({'composite': 0, 'additive': 4, 'average_intensity': 3, 'maximum_intensity': 1, 'minimum_intensity': 2}), help=\
        """
        Set/Get the blend mode. The default mode is Composite where the
        scalar values are sampled through the volume and composited in a
        front-to-back scheme through alpha blending. The final color and
        opacity is determined using the color and opacity transfer
        functions.
        
        Maximum and minimum intensity blend modes use the maximum and
        minimum scalar values, respectively,  along the sampling ray. The
        final color and opacity is determined by passing the resultant
        value through the color and opacity transfer functions.
        
        Additive blend mode accumulates scalar values by passing each
        value through the opacity transfer function and then adding up
        the product of the value and its opacity. In other words, the
        scalar values are scaled using the opacity transfer function and
        summed to derive the final color. Note that the resulting image
        is always grayscale i.e. aggregated values are not passed through
        the color transfer function. This is because the final value is a
        derived value and not a real data value along the sampling ray.
        
        Average intensity blend mode works similar to the additive blend
        mode where the scalar values are multiplied by opacity calculated
        from the opacity transfer function and then added. The additional
        step here is to divide the sum by the number of samples taken
        through the volume. One can control the scalar range by setting
        the average_ip_scalar_range ivar to disregard scalar values, not in
        the range of interest, from the average computation. As is the
        case with the additive intensity projection, the final image will
        always be grayscale i.e. the aggregated values are not passed
        through the color transfer function. This is because the
        resultant value is a derived value and not a real data value
        along the sampling ray.
        
        ote VolumeMapper::AVERAGE_INTENSITY_BLEND is only supported by
        the GPUVolumeRayCastMapper with the open_gl2 backend.
        \sa set_average_ip_scalar_range()
        """
    )

    def _blend_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBlendMode,
                        self.blend_mode_)

    cropping_region_flags = traits.Trait('sub_volume',
    tvtk_base.TraitRevPrefixMap({'sub_volume': 8192, 'cross': 4289552, 'fence': 49020602, 'inverted_cross': 129928175, 'inverted_fence': 85197125}), help=\
        """
        Set the flags for the cropping regions. The clipping planes
        divide the volume into 27 regions - there is one bit for each
        region. The regions start from the one containing voxel (0,0,0),
        moving along the x axis fastest, the y axis next, and the z axis
        slowest. These are represented from the lowest bit to bit number
        27 in the integer containing the flags. There are several
        convenience functions to set some common configurations -
        subvolume (the default), fence (between any of the clip plane
        pairs), inverted fence, cross (between any two of the clip plane
        pairs) and inverted cross.
        """
    )

    def _cropping_region_flags_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCroppingRegionFlags,
                        self.cropping_region_flags_)

    average_ip_scalar_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(-1e+299, 1e+299), cols=2, help=\
        """
        
        """
    )

    def _average_ip_scalar_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAverageIPScalarRange,
                        self.average_ip_scalar_range)

    def _get_cropping_max_value(self):
        return self._vtk_obj.GetCroppingMaxValue()
    cropping_max_value = traits.Property(_get_cropping_max_value, help=\
        """
        Turn On/Off orthogonal cropping. (Clipping planes are
        perpendicular to the coordinate axes.)
        """
    )

    def _get_cropping_min_value(self):
        return self._vtk_obj.GetCroppingMinValue()
    cropping_min_value = traits.Property(_get_cropping_min_value, help=\
        """
        Turn On/Off orthogonal cropping. (Clipping planes are
        perpendicular to the coordinate axes.)
        """
    )

    def _get_cropping_region_planes(self):
        return self._vtk_obj.GetCroppingRegionPlanes()
    cropping_region_planes = traits.Property(_get_cropping_region_planes, help=\
        """
        Set/Get the Cropping Region Planes ( xmin, xmax, ymin, ymax,
        zmin, zmax ) These planes are defined in volume coordinates -
        spacing and origin are considered.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input data
        """
    )

    def _get_voxel_cropping_region_planes(self):
        return self._vtk_obj.GetVoxelCroppingRegionPlanes()
    voxel_cropping_region_planes = traits.Property(_get_voxel_cropping_region_planes, help=\
        """
        Get the cropping region planes in voxels. Only valid during the
        rendering process
        """
    )

    def set_cropping_region_planes(self, *args):
        """
        V.set_cropping_region_planes(float, float, float, float, float,
            float)
        C++: void SetCroppingRegionPlanes(double, double, double, double,
            double, double)
        V.set_cropping_region_planes((float, float, float, float, float,
            float))
        C++: void SetCroppingRegionPlanes(double a[6])"""
        ret = self._wrap_call(self._vtk_obj.SetCroppingRegionPlanes, *args)
        return ret

    def set_input_data(self, *args):
        """
        V.set_input_data(ImageData)
        C++: virtual void SetInputData(ImageData *)
        V.set_input_data(DataSet)
        C++: virtual void SetInputData(DataSet *)
        Set/Get the input data
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    _updateable_traits_ = \
    (('cropping', 'GetCropping'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('blend_mode',
    'GetBlendMode'), ('cropping_region_flags', 'GetCroppingRegionFlags'),
    ('scalar_mode', 'GetScalarMode'), ('average_ip_scalar_range',
    'GetAverageIPScalarRange'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'cropping', 'debug', 'global_warning_display',
    'release_data_flag', 'blend_mode', 'cropping_region_flags',
    'scalar_mode', 'average_ip_scalar_range', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['cropping'], ['blend_mode', 'cropping_region_flags',
            'scalar_mode'], ['average_ip_scalar_range']),
            title='Edit VolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.image_mapper3d import ImageMapper3D


class ImageResliceMapper(ImageMapper3D):
    """
    ImageResliceMapper - map a slice of a ImageData to the screen
    
    Superclass: ImageMapper3D
    
    ImageResliceMapper will cut a 3d image with an abitrary slice
    plane and draw the results on the screen.  The slice can be set to
    automatically follow the camera, so that the camera controls the
    slicing.@par Thanks: Thanks to David Gobbi at the Seaman Family MR
    Centre and Dept. of Clinical Neurosciences, Foothills Medical Centre,
    Calgary, for providing this class.
    @sa
    ImageSlice ImageProperty ImageSliceMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageResliceMapper, obj, update, **traits)
    
    auto_adjust_image_quality = tvtk_base.true_bool_trait(help=\
        """
        Automatically reduce the rendering quality for greater speed when
        doing an interactive render.  This is on by default.
        """
    )

    def _auto_adjust_image_quality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoAdjustImageQuality,
                        self.auto_adjust_image_quality_)

    jump_to_nearest_slice = tvtk_base.false_bool_trait(help=\
        """
        When using slice_at_focal_point, this causes the slicing to occur at
        the closest slice to the focal point, instead of the default
        behavior where a new slice is interpolated between the original
        slices.  This flag is ignored if the slicing is oblique to the
        original slices.
        """
    )

    def _jump_to_nearest_slice_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetJumpToNearestSlice,
                        self.jump_to_nearest_slice_)

    resample_to_screen_pixels = tvtk_base.true_bool_trait(help=\
        """
        Resample the image directly to the screen pixels, instead of
        using a texture to scale the image after resampling.  This is
        slower and uses more memory, but provides high-quality results.
        It is On by default.
        """
    )

    def _resample_to_screen_pixels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResampleToScreenPixels,
                        self.resample_to_screen_pixels_)

    separate_window_level_operation = tvtk_base.true_bool_trait(help=\
        """
        Keep the color mapping stage distinct from the reslicing stage.
        This will improve the quality and possibly the speed of
        interactive window/level operations, but it uses more memory and
        might slow down interactive slicing operations.  On by default.
        """
    )

    def _separate_window_level_operation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSeparateWindowLevelOperation,
                        self.separate_window_level_operation_)

    slab_type = traits.Trait('mean',
    tvtk_base.TraitRevPrefixMap({'mean': 2, 'max': 1, 'min': 0, 'sum': 3}), help=\
        """
        The slab type, for thick slicing (default: Mean). The resulting
        view is a parallel projection through the volume.  This method
        can be used to generate a facsimile of a digitally-reconstructed
        radiograph or a minimum-intensity projection as long as
        perspective geometry is not required.  Note that the Sum mode
        provides an output with units of intensity times distance, while
        all other modes provide an output with units of intensity.
        """
    )

    def _slab_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSlabType,
                        self.slab_type_)

    image_sample_factor = traits.Trait(1, traits.Range(1, 16, enter_set=True, auto_set=False), help=\
        """
        Set the reslice sample frequency as in relation to the input
        image sample frequency.  The default value is 1, but higher
        values can be used to improve the results.  This is cheaper than
        turning on resample_to_screen_pixels.
        """
    )

    def _image_sample_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageSampleFactor,
                        self.image_sample_factor)

    def _get_interpolator(self):
        return wrap_vtk(self._vtk_obj.GetInterpolator())
    def _set_interpolator(self, arg):
        old_val = self._get_interpolator()
        self._wrap_call(self._vtk_obj.SetInterpolator,
                        deref_vtk(arg))
        self.trait_property_changed('interpolator', old_val, arg)
    interpolator = traits.Property(_get_interpolator, _set_interpolator, help=\
        """
        Set a custom interpolator.  This will only be used if the
        resample_to_screen_pixels option is on.
        """
    )

    slab_sample_factor = traits.Trait(2, traits.Range(1, 2, enter_set=True, auto_set=False), help=\
        """
        Set the number of slab samples to use as a factor of the number
        of input slices within the slab thickness.  The default value is
        2, but 1 will increase speed with very little loss of quality.
        """
    )

    def _slab_sample_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSlabSampleFactor,
                        self.slab_sample_factor)

    slab_thickness = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        The slab thickness, for thick slicing (default: zero)
        """
    )

    def _slab_thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSlabThickness,
                        self.slab_thickness)

    def _get_slice_plane(self):
        return wrap_vtk(self._vtk_obj.GetSlicePlane())
    def _set_slice_plane(self, arg):
        old_val = self._get_slice_plane()
        self._wrap_call(self._vtk_obj.SetSlicePlane,
                        deref_vtk(arg))
        self.trait_property_changed('slice_plane', old_val, arg)
    slice_plane = traits.Property(_get_slice_plane, _set_slice_plane, help=\
        """
        A plane that describes what slice of the input is being rendered
        by the mapper.  This plane is in world coordinates, not data
        coordinates.  Before using this plane, call Update or
        update_information to make sure the plane is up-to-date. These
        methods are automatically called by Render.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        The input data for this mapper.
        """
    )

    _updateable_traits_ = \
    (('auto_adjust_image_quality', 'GetAutoAdjustImageQuality'),
    ('jump_to_nearest_slice', 'GetJumpToNearestSlice'),
    ('resample_to_screen_pixels', 'GetResampleToScreenPixels'),
    ('separate_window_level_operation',
    'GetSeparateWindowLevelOperation'), ('background', 'GetBackground'),
    ('border', 'GetBorder'), ('slice_at_focal_point',
    'GetSliceAtFocalPoint'), ('slice_faces_camera',
    'GetSliceFacesCamera'), ('streaming', 'GetStreaming'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('slab_type',
    'GetSlabType'), ('image_sample_factor', 'GetImageSampleFactor'),
    ('slab_sample_factor', 'GetSlabSampleFactor'), ('slab_thickness',
    'GetSlabThickness'), ('number_of_threads', 'GetNumberOfThreads'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_adjust_image_quality', 'background',
    'border', 'debug', 'global_warning_display', 'jump_to_nearest_slice',
    'release_data_flag', 'resample_to_screen_pixels',
    'separate_window_level_operation', 'slice_at_focal_point',
    'slice_faces_camera', 'streaming', 'slab_type', 'image_sample_factor',
    'number_of_threads', 'progress_text', 'slab_sample_factor',
    'slab_thickness'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageResliceMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageResliceMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_adjust_image_quality', 'background', 'border',
            'jump_to_nearest_slice', 'resample_to_screen_pixels',
            'separate_window_level_operation', 'slice_at_focal_point',
            'slice_faces_camera', 'streaming'], ['slab_type'],
            ['image_sample_factor', 'number_of_threads', 'slab_sample_factor',
            'slab_thickness']),
            title='Edit ImageResliceMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageResliceMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


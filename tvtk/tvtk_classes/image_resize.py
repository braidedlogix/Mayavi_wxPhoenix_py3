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

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageResize(ThreadedImageAlgorithm):
    """
    ImageResize - High-quality image resizing filter
    
    Superclass: ThreadedImageAlgorithm
    
    ImageResize will magnify or shrink an image with interpolation and
    antialiasing.  The resizing is done with a 5-lobe Lanczos-windowed
    sinc filter that is bandlimited to the output sampling frequency in
    order to avoid aliasing when the image size is reduced.  This filter
    utilizes a O(n) algorithm to provide good effiency even though the
    filtering kernel is large.  The sinc interpolator can be turned off
    if nearest-neighbor interpolation is required, or it can be replaced
    with a different ImageInterpolator object.@par Thanks: Thanks to
    David Gobbi for contributing this class to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageResize, obj, update, **traits)
    
    border = tvtk_base.false_bool_trait(help=\
        """
        If Border is Off (the default), then the centers of each of the
        corner voxels will be considered to form the rectangular bounds
        of the image. This is the way that VTK normally computes image
        bounds.  If Border is On, then the image bounds will be defined
        by the outer corners of the voxels. This setting impacts how the
        resizing is done.  For example, if a magnification_factor of two
        is applied to a 256x256 image, the output image will be 512x512
        if Border is On, or 511x511 if Border is Off.
        """
    )

    def _border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorder,
                        self.border_)

    cropping = tvtk_base.false_bool_trait(help=\
        """
        Whether to crop the input image before resizing (Off by default).
         If this is On, then the cropping_region must be set.
        """
    )

    def _cropping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCropping,
                        self.cropping_)

    interpolate = tvtk_base.true_bool_trait(help=\
        """
        Turn interpolation on or off (by default, interpolation is on).
        """
    )

    def _interpolate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolate,
                        self.interpolate_)

    resize_method = traits.Trait('output_dimensions',
    tvtk_base.TraitRevPrefixMap({'output_dimensions': 0, 'magnification_factors': 2, 'output_spacing': 1}), help=\
        """
        The resizing method to use.  The default is to set the output
        image dimensions, and allow the filter to resize the image to
        these new dimensions.  It is also possible to resize the image by
        setting the output image spacing or by setting a magnification
        factor.
        """
    )

    def _resize_method_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResizeMethod,
                        self.resize_method_)

    cropping_region = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(0.0, 1.0, 0.0, 1.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _cropping_region_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCroppingRegion,
                        self.cropping_region)

    def _get_interpolator(self):
        return wrap_vtk(self._vtk_obj.GetInterpolator())
    def _set_interpolator(self, arg):
        old_val = self._get_interpolator()
        self._wrap_call(self._vtk_obj.SetInterpolator,
                        deref_vtk(arg))
        self.trait_property_changed('interpolator', old_val, arg)
    interpolator = traits.Property(_get_interpolator, _set_interpolator, help=\
        """
        Set the interpolator for resampling the data.
        """
    )

    magnification_factors = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _magnification_factors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMagnificationFactors,
                        self.magnification_factors)

    output_dimensions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(-1, -1, -1), cols=3, help=\
        """
        
        """
    )

    def _output_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputDimensions,
                        self.output_dimensions)

    output_spacing = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _output_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputSpacing,
                        self.output_spacing)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get a data object for one of the input port connections.  The use
        of this method is strongly discouraged, but some filters that
        were written a long time ago still use this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('border', 'GetBorder'), ('cropping', 'GetCropping'), ('interpolate',
    'GetInterpolate'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('resize_method', 'GetResizeMethod'), ('split_mode', 'GetSplitMode'),
    ('cropping_region', 'GetCroppingRegion'), ('magnification_factors',
    'GetMagnificationFactors'), ('output_dimensions',
    'GetOutputDimensions'), ('output_spacing', 'GetOutputSpacing'),
    ('desired_bytes_per_piece', 'GetDesiredBytesPerPiece'), ('enable_smp',
    'GetEnableSMP'), ('global_default_enable_smp',
    'GetGlobalDefaultEnableSMP'), ('minimum_piece_size',
    'GetMinimumPieceSize'), ('number_of_threads', 'GetNumberOfThreads'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'border', 'cropping', 'debug',
    'global_warning_display', 'interpolate', 'release_data_flag',
    'resize_method', 'split_mode', 'cropping_region',
    'desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
    'magnification_factors', 'minimum_piece_size', 'number_of_threads',
    'output_dimensions', 'output_spacing', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageResize, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageResize properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['border', 'cropping', 'interpolate'], ['resize_method',
            'split_mode'], ['cropping_region', 'desired_bytes_per_piece',
            'enable_smp', 'global_default_enable_smp', 'magnification_factors',
            'minimum_piece_size', 'number_of_threads', 'output_dimensions',
            'output_spacing']),
            title='Edit ImageResize properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageResize properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


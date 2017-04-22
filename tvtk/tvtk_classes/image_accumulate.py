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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ImageAccumulate(ImageAlgorithm):
    """
    ImageAccumulate - Generalized histograms up to 3 dimensions.
    
    Superclass: ImageAlgorithm
    
    ImageAccumulate - This filter divides component space into
    discrete bins.  It then counts the number of pixels associated with
    each bin. The dimensionality of the output depends on how many
    components the input pixels have. An input images with N components
    per pixels will result in an N-dimensional histogram, where N can be
    1, 2, or 3. The input can be any type, but the output is always int.
    Some statistics are computed on the pixel values at the same time.
    The set_stencil and reverse_stencil functions allow the statistics to
    be computed on an arbitrary portion of the input data. See the
    documentation for ImageStencilData for more information.
    
    This filter also supports ignoring pixels with value equal to 0.
    Using this option with ImageMask may result in results being
    slightly off since 0 could be a valid value from your input.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageAccumulate, obj, update, **traits)
    
    ignore_zero = tvtk_base.false_bool_trait(help=\
        """
        Should the data with value 0 be ignored? Initial value is false.
        """
    )

    def _ignore_zero_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIgnoreZero,
                        self.ignore_zero_)

    reverse_stencil = tvtk_base.false_bool_trait(help=\
        """
        Reverse the stencil. Initial value is false.
        """
    )

    def _reverse_stencil_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReverseStencil,
                        self.reverse_stencil_)

    component_extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(0, 255, 0, 0, 0, 0), cols=3, help=\
        """
        Set/Get - The component extent sets the number/extent of the
        bins. For a 1d histogram with 10 bins spanning the values 1000 to
        2000, this extent should be set to 0, 9, 0, 0, 0, 0. The extent
        specifies inclusive min/max values. This implies that the top
        extent should be set to the number of bins - 1. Initial value is
        (0,255,0,0,0,0)
        """
    )

    def _component_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponentExtent,
                        self.component_extent)

    component_origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _component_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponentOrigin,
                        self.component_origin)

    component_spacing = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _component_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponentSpacing,
                        self.component_spacing)

    def _get_ignore_zero_max_value(self):
        return self._vtk_obj.GetIgnoreZeroMaxValue()
    ignore_zero_max_value = traits.Property(_get_ignore_zero_max_value, help=\
        """
        Should the data with value 0 be ignored? Initial value is false.
        """
    )

    def _get_ignore_zero_min_value(self):
        return self._vtk_obj.GetIgnoreZeroMinValue()
    ignore_zero_min_value = traits.Property(_get_ignore_zero_min_value, help=\
        """
        Should the data with value 0 be ignored? Initial value is false.
        """
    )

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

    def _get_max(self):
        return self._vtk_obj.GetMax()
    max = traits.Property(_get_max, help=\
        """
        
        """
    )

    def _get_mean(self):
        return self._vtk_obj.GetMean()
    mean = traits.Property(_get_mean, help=\
        """
        
        """
    )

    def _get_min(self):
        return self._vtk_obj.GetMin()
    min = traits.Property(_get_min, help=\
        """
        
        """
    )

    def _get_reverse_stencil_max_value(self):
        return self._vtk_obj.GetReverseStencilMaxValue()
    reverse_stencil_max_value = traits.Property(_get_reverse_stencil_max_value, help=\
        """
        Reverse the stencil. Initial value is false.
        """
    )

    def _get_reverse_stencil_min_value(self):
        return self._vtk_obj.GetReverseStencilMinValue()
    reverse_stencil_min_value = traits.Property(_get_reverse_stencil_min_value, help=\
        """
        Reverse the stencil. Initial value is false.
        """
    )

    def _get_standard_deviation(self):
        return self._vtk_obj.GetStandardDeviation()
    standard_deviation = traits.Property(_get_standard_deviation, help=\
        """
        
        """
    )

    def _get_stencil(self):
        return wrap_vtk(self._vtk_obj.GetStencil())
    stencil = traits.Property(_get_stencil, help=\
        """
        Use a stencil to specify which voxels to accumulate.
        Backcompatible methods. It set and get the stencil on input port
        1. Initial value is NULL.
        """
    )

    def _get_voxel_count(self):
        return self._vtk_obj.GetVoxelCount()
    voxel_count = traits.Property(_get_voxel_count, help=\
        """
        Get the statistics information for the data. The values only make
        sense after the execution of the filter. Initial values are 0.
        """
    )

    def set_stencil_data(self, *args):
        """
        V.set_stencil_data(ImageStencilData)
        C++: void SetStencilData(ImageStencilData *stencil)
        Use a stencil to specify which voxels to accumulate.
        Backcompatible methods. It set and get the stencil on input port
        1. Initial value is NULL.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetStencilData, *my_args)
        return ret

    _updateable_traits_ = \
    (('ignore_zero', 'GetIgnoreZero'), ('reverse_stencil',
    'GetReverseStencil'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('component_extent', 'GetComponentExtent'), ('component_origin',
    'GetComponentOrigin'), ('component_spacing', 'GetComponentSpacing'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'ignore_zero',
    'release_data_flag', 'reverse_stencil', 'component_extent',
    'component_origin', 'component_spacing', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageAccumulate, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageAccumulate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['ignore_zero', 'reverse_stencil'], [], ['component_extent',
            'component_origin', 'component_spacing']),
            title='Edit ImageAccumulate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageAccumulate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


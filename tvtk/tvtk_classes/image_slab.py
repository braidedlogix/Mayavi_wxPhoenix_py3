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


class ImageSlab(ThreadedImageAlgorithm):
    """
    ImageSlab - combine image slices to form a slab image
    
    Superclass: ThreadedImageAlgorithm
    
    ImageSlab will combine all of the slices of an image to create a
    single slice.  The slices can be combined with the following
    operations: averaging, summation, minimum, maximum. If you require an
    arbitrary angle of projection, you can use ImageReslice.@par
    Thanks: Thanks to David Gobbi for contributing this class to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageSlab, obj, update, **traits)
    
    multi_slice_output = tvtk_base.false_bool_trait(help=\
        """
        Turn on multi-slice output.  Each slice of the output will be a
        projection through the specified range of input slices, e.g. if
        the slice_range is [0,3] then slice 'i' of the output will be a
        projection through slices 'i' through '3+i' of the input. This
        flag is off by default.
        """
    )

    def _multi_slice_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMultiSliceOutput,
                        self.multi_slice_output_)

    trapezoid_integration = tvtk_base.false_bool_trait(help=\
        """
        Use trapezoid integration for slab computation.  This weighs the
        first and last slices by half when doing sum and mean, as
        compared to the default midpoint integration that weighs all
        slices equally. It is off by default.
        """
    )

    def _trapezoid_integration_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTrapezoidIntegration,
                        self.trapezoid_integration_)

    operation = traits.Trait('mean',
    tvtk_base.TraitRevPrefixMap({'mean': 2, 'max': 1, 'min': 0, 'sum': 3}), help=\
        """
        Set the operation to use when combining slices.  The choices are
        "Mean", "Sum", "Min", "Max".  The default is "Mean".
        """
    )

    def _operation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOperation,
                        self.operation_)

    orientation = traits.Trait('z',
    tvtk_base.TraitRevPrefixMap({'z': 2, 'x': 0, 'y': 1}), help=\
        """
        Set the slice direction: zero for x, 1 for y, 2 for z. The
        default is the Z direction.
        """
    )

    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation_)

    def get_output_scalar_type(self):
        """
        V.get_output_scalar_type() -> int
        C++: int GetOutputScalarType()
        Set the output scalar type to float or double, to avoid potential
        overflow when doing a summation operation. The default is to use
        the scalar type of the input data, and clamp the output to the
        range of the input scalar type.
        """
        ret = self._vtk_obj.GetOutputScalarType()
        return ret
        

    def set_output_scalar_type_to_double(self):
        """
        V.set_output_scalar_type_to_double()
        C++: void SetOutputScalarTypeToDouble()
        Set the output scalar type to float or double, to avoid potential
        overflow when doing a summation operation. The default is to use
        the scalar type of the input data, and clamp the output to the
        range of the input scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToDouble()

    def set_output_scalar_type_to_float(self):
        """
        V.set_output_scalar_type_to_float()
        C++: void SetOutputScalarTypeToFloat()
        Set the output scalar type to float or double, to avoid potential
        overflow when doing a summation operation. The default is to use
        the scalar type of the input data, and clamp the output to the
        range of the input scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToFloat()

    def set_output_scalar_type_to_input_scalar_type(self):
        """
        V.set_output_scalar_type_to_input_scalar_type()
        C++: void SetOutputScalarTypeToInputScalarType()
        Set the output scalar type to float or double, to avoid potential
        overflow when doing a summation operation. The default is to use
        the scalar type of the input data, and clamp the output to the
        range of the input scalar type.
        """
        self._vtk_obj.SetOutputScalarTypeToInputScalarType()

    slice_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(-2147483648, 2147483647), cols=2, help=\
        """
        
        """
    )

    def _slice_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceRange,
                        self.slice_range)

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
    (('multi_slice_output', 'GetMultiSliceOutput'),
    ('trapezoid_integration', 'GetTrapezoidIntegration'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('operation',
    'GetOperation'), ('orientation', 'GetOrientation'), ('split_mode',
    'GetSplitMode'), ('slice_range', 'GetSliceRange'),
    ('desired_bytes_per_piece', 'GetDesiredBytesPerPiece'), ('enable_smp',
    'GetEnableSMP'), ('global_default_enable_smp',
    'GetGlobalDefaultEnableSMP'), ('minimum_piece_size',
    'GetMinimumPieceSize'), ('number_of_threads', 'GetNumberOfThreads'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'multi_slice_output', 'release_data_flag', 'trapezoid_integration',
    'operation', 'orientation', 'split_mode', 'desired_bytes_per_piece',
    'enable_smp', 'global_default_enable_smp', 'minimum_piece_size',
    'number_of_threads', 'progress_text', 'slice_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageSlab, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageSlab properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['multi_slice_output', 'trapezoid_integration'], ['operation',
            'orientation', 'split_mode'], ['desired_bytes_per_piece',
            'enable_smp', 'global_default_enable_smp', 'minimum_piece_size',
            'number_of_threads', 'slice_range']),
            title='Edit ImageSlab properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageSlab properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


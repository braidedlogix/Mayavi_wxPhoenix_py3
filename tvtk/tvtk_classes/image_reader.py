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

from tvtk.tvtk_classes.image_reader2 import ImageReader2


class ImageReader(ImageReader2):
    """
    ImageReader - Superclass of transformable binary file readers.
    
    Superclass: ImageReader2
    
    ImageReader provides methods needed to read a region from a file.
    It supports both transforms and masks on the input data, but as a
    result is more complicated and slower than its parent class
    ImageReader2.
    
    @sa
    BMPReader PNMReader TIFFReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageReader, obj, update, **traits)
    
    data_mask = traits.Int(4294967295, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Data mask.  The data mask is a simply integer whose
        bits are treated as a mask to the bits read from disk.  That is,
        the data mask is bitwise-and'ed to the numbers read from disk. 
        This ivar is stored as 64 bits, the largest mask you will need. 
        The mask will be truncated to the data size required to be read
        (using the least significant bits).
        """
    )

    def _data_mask_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataMask,
                        self.data_mask)

    data_voi = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(0, 0, 0, 0, 0, 0), cols=3, help=\
        """
        
        """
    )

    def _data_voi_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataVOI,
                        self.data_voi)

    scalar_array_name = traits.String('ImageFile', enter_set=True, auto_set=False, help=\
        """
        Set/get the scalar array name for this data set.
        """
    )

    def _scalar_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarArrayName,
                        self.scalar_array_name)

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        Set/Get transformation matrix to transform the data from slice
        space into world space. This matrix must be a permutation matrix.
        To qualify, the sums of the rows must be + or - 1.
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

    def compute_inverse_transformed_extent(self, *args):
        """
        V.compute_inverse_transformed_extent([int, int, int, int, int, int],
            [int, int, int, int, int, int])
        C++: void ComputeInverseTransformedExtent(int inExtent[6],
            int outExtent[6])"""
        ret = self._wrap_call(self._vtk_obj.ComputeInverseTransformedExtent, *args)
        return ret

    def compute_inverse_transformed_increments(self, *args):
        """
        V.compute_inverse_transformed_increments([int, int, int], [int, int,
            int])
        C++: void ComputeInverseTransformedIncrements(IdType inIncr[3],
             IdType outIncr[3])"""
        ret = self._wrap_call(self._vtk_obj.ComputeInverseTransformedIncrements, *args)
        return ret

    def open_and_seek_file(self, *args):
        """
        V.open_and_seek_file([int, int, int, int, int, int], int) -> int
        C++: int OpenAndSeekFile(int extent[6], int slice)"""
        ret = self._wrap_call(self._vtk_obj.OpenAndSeekFile, *args)
        return ret

    _updateable_traits_ = \
    (('file_lower_left', 'GetFileLowerLeft'), ('swap_bytes',
    'GetSwapBytes'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('data_byte_order', 'GetDataByteOrder'), ('data_mask', 'GetDataMask'),
    ('data_voi', 'GetDataVOI'), ('scalar_array_name',
    'GetScalarArrayName'), ('data_extent', 'GetDataExtent'),
    ('data_origin', 'GetDataOrigin'), ('data_spacing', 'GetDataSpacing'),
    ('file_dimensionality', 'GetFileDimensionality'), ('file_name',
    'GetFileName'), ('file_name_slice_offset', 'GetFileNameSliceOffset'),
    ('file_name_slice_spacing', 'GetFileNameSliceSpacing'),
    ('file_pattern', 'GetFilePattern'), ('file_prefix', 'GetFilePrefix'),
    ('header_size', 'GetHeaderSize'), ('memory_buffer_length',
    'GetMemoryBufferLength'), ('number_of_scalar_components',
    'GetNumberOfScalarComponents'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'file_lower_left',
    'global_warning_display', 'release_data_flag', 'swap_bytes',
    'data_byte_order', 'data_extent', 'data_mask', 'data_origin',
    'data_spacing', 'data_voi', 'file_dimensionality', 'file_name',
    'file_name_slice_offset', 'file_name_slice_spacing', 'file_pattern',
    'file_prefix', 'header_size', 'memory_buffer_length',
    'number_of_scalar_components', 'progress_text', 'scalar_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['file_lower_left', 'swap_bytes'], ['data_byte_order'],
            ['data_extent', 'data_mask', 'data_origin', 'data_spacing',
            'data_voi', 'file_dimensionality', 'file_name',
            'file_name_slice_offset', 'file_name_slice_spacing', 'file_pattern',
            'file_prefix', 'header_size', 'memory_buffer_length',
            'number_of_scalar_components', 'scalar_array_name']),
            title='Edit ImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


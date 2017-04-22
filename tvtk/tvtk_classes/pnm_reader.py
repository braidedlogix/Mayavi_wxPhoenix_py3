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

from tvtk.tvtk_classes.image_reader import ImageReader


class PNMReader(ImageReader):
    """
    PNMReader - read pnm (i.e., portable anymap) files
    
    Superclass: ImageReader
    
    PNMReader is a source object that reads pnm (portable anymap)
    files. This includes .pbm (bitmap), .pgm (grayscale), and .ppm
    (pixmap) files. (Currently this object only reads binary versions of
    these files.)
    
    PNMReader creates structured point datasets. The dimension of the
    dataset depends upon the number of files read. Reading a single file
    results in a 2d image, while reading more than one file results in a
    3d volume.
    
    To read a volume, files must be of the form "_file_name.<number>"
    (e.g., foo.ppm.0, foo.ppm.1, ...). You must also specify the
    data_extent.  The fifth and sixth values of the data_extent specify the
    beginning and ending files to read.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPNMReader, obj, update, **traits)
    
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
            return super(PNMReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PNMReader properties', scrollable=True, resizable=True,
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
            title='Edit PNMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PNMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


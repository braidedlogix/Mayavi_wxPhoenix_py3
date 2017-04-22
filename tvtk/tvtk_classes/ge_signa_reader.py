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

from tvtk.tvtk_classes.medical_image_reader2 import MedicalImageReader2


class GESignaReader(MedicalImageReader2):
    """
    GESignaReader - read GE Signa ximg files
    
    Superclass: MedicalImageReader2
    
    GESignaReader is a source object that reads some GE Signa ximg
    files It does support reading in pixel spacing, slice spacing and it
    computes an origin for the image in millimeters. It always produces
    greyscale unsigned short data and it supports reading in rectangular,
    packed, compressed, and packed&compressed. It does not read in slice
    orientation, or position right now. To use it you just need to
    specify a filename or a file prefix and pattern.
    
    @sa
    ImageReader2
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGESignaReader, obj, update, **traits)
    
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
    ('data_byte_order', 'GetDataByteOrder'), ('date', 'GetDate'),
    ('image_number', 'GetImageNumber'), ('modality', 'GetModality'),
    ('patient_id', 'GetPatientID'), ('patient_name', 'GetPatientName'),
    ('series', 'GetSeries'), ('study', 'GetStudy'), ('data_extent',
    'GetDataExtent'), ('data_origin', 'GetDataOrigin'), ('data_spacing',
    'GetDataSpacing'), ('file_dimensionality', 'GetFileDimensionality'),
    ('file_name', 'GetFileName'), ('file_name_slice_offset',
    'GetFileNameSliceOffset'), ('file_name_slice_spacing',
    'GetFileNameSliceSpacing'), ('file_pattern', 'GetFilePattern'),
    ('file_prefix', 'GetFilePrefix'), ('header_size', 'GetHeaderSize'),
    ('memory_buffer_length', 'GetMemoryBufferLength'),
    ('number_of_scalar_components', 'GetNumberOfScalarComponents'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'file_lower_left',
    'global_warning_display', 'release_data_flag', 'swap_bytes',
    'data_byte_order', 'data_extent', 'data_origin', 'data_spacing',
    'date', 'file_dimensionality', 'file_name', 'file_name_slice_offset',
    'file_name_slice_spacing', 'file_pattern', 'file_prefix',
    'header_size', 'image_number', 'memory_buffer_length', 'modality',
    'number_of_scalar_components', 'patient_id', 'patient_name',
    'progress_text', 'series', 'study'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GESignaReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GESignaReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['file_lower_left', 'swap_bytes'], ['data_byte_order'],
            ['data_extent', 'data_origin', 'data_spacing', 'date',
            'file_dimensionality', 'file_name', 'file_name_slice_offset',
            'file_name_slice_spacing', 'file_pattern', 'file_prefix',
            'header_size', 'image_number', 'memory_buffer_length', 'modality',
            'number_of_scalar_components', 'patient_id', 'patient_name', 'series',
            'study']),
            title='Edit GESignaReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GESignaReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


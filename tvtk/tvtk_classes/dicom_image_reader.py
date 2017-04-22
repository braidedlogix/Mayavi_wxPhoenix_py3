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


class DICOMImageReader(ImageReader2):
    """
    DICOMImageReader - Reads some DICOM images
    
    Superclass: ImageReader2
    
    DICOM (stands for Digital Imaging in COmmunications and Medicine) is
    a medical image file format widely used to exchange data, provided by
    various modalities.
    @warning
    This reader might eventually handle ACR-NEMA file (predecessor of the
    DICOM format for medical images). This reader does not handle
    encapsulated format, only plain raw file are handled. This reader
    also does not handle multi-frames DICOM datasets.
    @warning
    Internally DICOMParser assumes the x,y pixel spacing is stored in
    0028,0030 and that z spacing is stored in Slice Thickness (correct
    only when slice were acquired contiguous): 0018,0050. Which means
    this is only valid for some rare MR Image Storage
    
    @sa
    BMPReader PNMReader TIFFReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDICOMImageReader, obj, update, **traits)
    
    directory_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the directory name for the reader to look in for DICOM files.
        If this method is used, the reader will try to find all the DICOM
        files in a directory. It will select the subset corresponding to
        the first series UID it stumbles across and it will try to build
        an ordered volume from them based on the slice number. The volume
        building will be upgraded to something more sophisticated in the
        future.
        """
    )

    def _directory_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirectoryName,
                        self.directory_name)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set the filename for the file to read. If this method is used,
        the reader will only read a single file.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_bits_allocated(self):
        return self._vtk_obj.GetBitsAllocated()
    bits_allocated = traits.Property(_get_bits_allocated, help=\
        """
        Get the number of bits allocated for each pixel in the file.
        """
    )

    def _get_gantry_angle(self):
        return self._vtk_obj.GetGantryAngle()
    gantry_angle = traits.Property(_get_gantry_angle, help=\
        """
        Get the gantry angle for the last image processed.
        """
    )

    def _get_height(self):
        return self._vtk_obj.GetHeight()
    height = traits.Property(_get_height, help=\
        """
        Returns the image height.
        """
    )

    def _get_image_orientation_patient(self):
        return self._vtk_obj.GetImageOrientationPatient()
    image_orientation_patient = traits.Property(_get_image_orientation_patient, help=\
        """
        Get the (DICOM) directions cosines. It consist of the components
        of the first two vectors. The third vector needs to be computed
        to form an orthonormal basis.
        """
    )

    def _get_image_position_patient(self):
        return self._vtk_obj.GetImagePositionPatient()
    image_position_patient = traits.Property(_get_image_position_patient, help=\
        """
        Get the (DICOM) x,y,z coordinates of the first pixel in the image
        (upper left hand corner) of the last image processed by the
        DICOMParser
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

    def _get_number_of_components(self):
        return self._vtk_obj.GetNumberOfComponents()
    number_of_components = traits.Property(_get_number_of_components, help=\
        """
        Get the number of components of the image data for the last image
        processed.
        """
    )

    def _get_patient_name(self):
        return self._vtk_obj.GetPatientName()
    patient_name = traits.Property(_get_patient_name, help=\
        """
        Get the patient name for the last image processed.
        """
    )

    def _get_pixel_representation(self):
        return self._vtk_obj.GetPixelRepresentation()
    pixel_representation = traits.Property(_get_pixel_representation, help=\
        """
        Get the pixel representation of the last image processed by the
        DICOMParser. A zero is a unsigned quantity.  A one indicates a
        signed quantity
        """
    )

    def _get_pixel_spacing(self):
        return self._vtk_obj.GetPixelSpacing()
    pixel_spacing = traits.Property(_get_pixel_spacing, help=\
        """
        Returns the pixel spacing (in X, Y, Z). Note: if there is only
        one slice, the Z spacing is set to the slice thickness. If there
        is more than one slice, it is set to the distance between the
        first two slices.
        """
    )

    def _get_rescale_offset(self):
        return self._vtk_obj.GetRescaleOffset()
    rescale_offset = traits.Property(_get_rescale_offset, help=\
        """
        Get the rescale offset for the pixel data.
        """
    )

    def _get_rescale_slope(self):
        return self._vtk_obj.GetRescaleSlope()
    rescale_slope = traits.Property(_get_rescale_slope, help=\
        """
        Get the rescale slope for the pixel data.
        """
    )

    def _get_study_id(self):
        return self._vtk_obj.GetStudyID()
    study_id = traits.Property(_get_study_id, help=\
        """
        Get the Study ID for the last image processed.
        """
    )

    def _get_study_uid(self):
        return self._vtk_obj.GetStudyUID()
    study_uid = traits.Property(_get_study_uid, help=\
        """
        Get the study uid for the last image processed.
        """
    )

    def _get_transfer_syntax_uid(self):
        return self._vtk_obj.GetTransferSyntaxUID()
    transfer_syntax_uid = traits.Property(_get_transfer_syntax_uid, help=\
        """
        Get the transfer syntax UID for the last image processed.
        """
    )

    def _get_width(self):
        return self._vtk_obj.GetWidth()
    width = traits.Property(_get_width, help=\
        """
        Returns the image width.
        """
    )

    _updateable_traits_ = \
    (('file_lower_left', 'GetFileLowerLeft'), ('swap_bytes',
    'GetSwapBytes'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('data_byte_order', 'GetDataByteOrder'), ('directory_name',
    'GetDirectoryName'), ('file_name', 'GetFileName'), ('data_extent',
    'GetDataExtent'), ('data_origin', 'GetDataOrigin'), ('data_spacing',
    'GetDataSpacing'), ('file_dimensionality', 'GetFileDimensionality'),
    ('file_name_slice_offset', 'GetFileNameSliceOffset'),
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
    'data_byte_order', 'data_extent', 'data_origin', 'data_spacing',
    'directory_name', 'file_dimensionality', 'file_name',
    'file_name_slice_offset', 'file_name_slice_spacing', 'file_pattern',
    'file_prefix', 'header_size', 'memory_buffer_length',
    'number_of_scalar_components', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DICOMImageReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DICOMImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['file_lower_left', 'swap_bytes'], ['data_byte_order'],
            ['data_extent', 'data_origin', 'data_spacing', 'directory_name',
            'file_dimensionality', 'file_name', 'file_name_slice_offset',
            'file_name_slice_spacing', 'file_pattern', 'file_prefix',
            'header_size', 'memory_buffer_length',
            'number_of_scalar_components']),
            title='Edit DICOMImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DICOMImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


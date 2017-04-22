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


class NIFTIImageReader(ImageReader2):
    """
    NIFTIImageReader - Read n_if_ti-_1 and n_if_ti-_2 medical image files
    
    Superclass: ImageReader2
    
    This class reads NIFTI files, either in .nii format or as separate
    .img and .hdr files.  If two files are used, then they can be passed
    by using set_file_names() instead of set_file_name().  Files ending in
    .gz are decompressed on-the-fly while they are being read.  Files
    with complex numbers or vector dimensions will be read as
    multi-component images.  If a NIFTI file has a time dimension, then
    by default only the first image in the time series will be read, but
    the time_as_vector flag can be set to read the time steps as vector
    components.  Files in Analyze 7.5 format are also supported by this
    reader.@par Thanks: This class was contributed to VTK by the Calgary
    Image Processing and Analysis Centre (CIPAC).
    @sa
    NIFTIImageWriter, NIFTIImageHeader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkNIFTIImageReader, obj, update, **traits)
    
    planar_rgb = tvtk_base.false_bool_trait(help=\
        """
        Read planar RGB (separate R, G, and B planes), rather than packed
        RGB. The NIFTI format should always use packed RGB.  The Analyze
        format, however, was used to store both planar RGB and packed RGB
        depending on the software, without any indication in the header
        about which convention was being used.  Use this if you have a
        planar RGB file.
        """
    )

    def _planar_rgb_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlanarRGB,
                        self.planar_rgb_)

    time_as_vector = tvtk_base.false_bool_trait(help=\
        """
        Read the time dimension as scalar components (default: Off). If
        this is on, then each time point will be stored as a component in
        the image data.  If the file has both a time dimension and a
        vector dimension, then the number of components will be the
        product of these two dimensions, i.e. the components will store a
        sequence of vectors.
        """
    )

    def _time_as_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeAsVector,
                        self.time_as_vector_)

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

    def _get_nifti_header(self):
        return wrap_vtk(self._vtk_obj.GetNIFTIHeader())
    nifti_header = traits.Property(_get_nifti_header, help=\
        """
        Get the raw header information from the n_if_ti file.
        """
    )

    def _get_q_fac(self):
        return self._vtk_obj.GetQFac()
    q_fac = traits.Property(_get_q_fac, help=\
        """
        QFac gives the slice order in the NIFTI file versus the VTK
        image. If QFac is -1, then the VTK slice index J is related to
        the NIFTI slice index j by the equation J = (num_slices - j - 1).
         VTK requires the slices to be ordered so that the voxel indices
        (I,J,K) provide a right-handed coordinate system, whereas NIFTI
        does not.  Instead, NIFTI stores a factor called "qfac" in the
        header to signal when the (i,j,k) indices form a left-handed
        coordinate system.  QFac will only ever have values of +1 or -1.
        """
    )

    def _get_q_form_matrix(self):
        return wrap_vtk(self._vtk_obj.GetQFormMatrix())
    q_form_matrix = traits.Property(_get_q_form_matrix, help=\
        """
        Get a matrix that gives the "qform" orientation and offset for
        the data. If no qform matrix was stored in the file, the return
        value is NULL. This matrix will transform VTK data coordinates
        into the NIFTI oriented data coordinates, where +X points right,
        +Y points anterior (toward the front), and +Z points superior
        (toward the head). The qform matrix will always have a positive
        determinant. The offset that is stored in the matrix gives the
        position of the first pixel in the first slice of the VTK image
        data.  Note that if QFac is -1, then the first slice in the VTK
        image data is the last slice in the NIFTI file, and the Z offset
        will automatically be adjusted to compensate for this.
        """
    )

    def _get_rescale_intercept(self):
        return self._vtk_obj.GetRescaleIntercept()
    rescale_intercept = traits.Property(_get_rescale_intercept, help=\
        """
        
        """
    )

    def _get_rescale_slope(self):
        return self._vtk_obj.GetRescaleSlope()
    rescale_slope = traits.Property(_get_rescale_slope, help=\
        """
        Get the slope and intercept for rescaling the scalar values.
        These values allow calibration of the data to real values. Use
        the equation v = u*_rescale_slope + rescale_intercept. This directly
        returns the values stored in the scl_slope and scl_inter fields
        in the NIFTI header.
        """
    )

    def _get_s_form_matrix(self):
        return wrap_vtk(self._vtk_obj.GetSFormMatrix())
    s_form_matrix = traits.Property(_get_s_form_matrix, help=\
        """
        Get a matrix that gives the "sform" orientation and offset for
        the data. If no sform matrix was stored in the file, the return
        value is NULL. Like the qform matrix, this matrix will transform
        VTK data coordinates into a NIFTI coordinate system.  Unlike the
        qform matrix, the sform matrix can contain scaling information
        and can even (rarely) have a negative determinant, i.e. a flip. 
        This matrix is modified slightly as compared to the sform matrix
        stored in the NIFTI header: the pixdim pixel spacing is factored
        out.  Also, if QFac is -1, then the VTK slices are in reverse
        order as compared to the NIFTI slices, hence as compared to the
        sform matrix stored in the header, the third column of this
        matrix is multiplied by -1 and the Z offset is shifted to
        compensate for the fact that the last slice has become the first.
        """
    )

    def _get_time_dimension(self):
        return self._vtk_obj.GetTimeDimension()
    time_dimension = traits.Property(_get_time_dimension, help=\
        """
        Get the time dimension that was stored in the NIFTI header.
        """
    )

    def _get_time_spacing(self):
        return self._vtk_obj.GetTimeSpacing()
    time_spacing = traits.Property(_get_time_spacing, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('planar_rgb', 'GetPlanarRGB'), ('time_as_vector',
    'GetTimeAsVector'), ('file_lower_left', 'GetFileLowerLeft'),
    ('swap_bytes', 'GetSwapBytes'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('data_byte_order', 'GetDataByteOrder'), ('data_extent',
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
    'global_warning_display', 'planar_rgb', 'release_data_flag',
    'swap_bytes', 'time_as_vector', 'data_byte_order', 'data_extent',
    'data_origin', 'data_spacing', 'file_dimensionality', 'file_name',
    'file_name_slice_offset', 'file_name_slice_spacing', 'file_pattern',
    'file_prefix', 'header_size', 'memory_buffer_length',
    'number_of_scalar_components', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(NIFTIImageReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit NIFTIImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['file_lower_left', 'planar_rgb', 'swap_bytes',
            'time_as_vector'], ['data_byte_order'], ['data_extent', 'data_origin',
            'data_spacing', 'file_dimensionality', 'file_name',
            'file_name_slice_offset', 'file_name_slice_spacing', 'file_pattern',
            'file_prefix', 'header_size', 'memory_buffer_length',
            'number_of_scalar_components']),
            title='Edit NIFTIImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit NIFTIImageReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


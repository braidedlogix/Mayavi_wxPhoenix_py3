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

from tvtk.tvtk_classes.image_writer import ImageWriter


class NIFTIImageWriter(ImageWriter):
    """
    NIFTIImageWriter - Write n_if_ti-_1 and n_if_ti-_2 medical image files
    
    Superclass: ImageWriter
    
    This class writes NIFTI files, either in .nii format or as separate
    .img and .hdr files.  If told to write a file that ends in ".gz",
    then the writer will automatically compress the file with zlib.
    Images of type unsigned char that have 3 or 4 scalar components will
    automatically be written as RGB or RGBA respectively.  Images of type
    float or double that have 2 components will automatically be written
    as complex values.@par Thanks: This class was contributed to VTK by
    the Calgary Image Processing and Analysis Centre (CIPAC).
    @sa
    NIFTIImageReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkNIFTIImageWriter, obj, update, **traits)
    
    planar_rgb = tvtk_base.false_bool_trait(help=\
        """
        Write planar RGB (separate R, G, and B planes), rather than
        packed RGB. Use this option with extreme caution: the NIFTI
        standard requires RGB pixels to be packed.  The Analyze format,
        however, was used to store both planar RGB and packed RGB
        depending on the software, without any indication in the header
        about which convention was being used.
        """
    )

    def _planar_rgb_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlanarRGB,
                        self.planar_rgb_)

    description = traits.String('VTK7.1.0', enter_set=True, auto_set=False, help=\
        """
        Set a short description (max 80 chars) of how the file was
        produced. The default description is "VTKX.Y" where X.Y is the
        VTK version.
        """
    )

    def _description_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDescription,
                        self.description)

    def _get_nifti_header(self):
        return wrap_vtk(self._vtk_obj.GetNIFTIHeader())
    def _set_nifti_header(self, arg):
        old_val = self._get_nifti_header()
        self._wrap_call(self._vtk_obj.SetNIFTIHeader,
                        deref_vtk(arg))
        self.trait_property_changed('nifti_header', old_val, arg)
    nifti_header = traits.Property(_get_nifti_header, _set_nifti_header, help=\
        """
        Set the NIFTI header information to use when writing the file.
        The data dimensions and pixdim from the supplied header will be
        ignored.  Likewise, the QForm and SForm information in the
        supplied header will be ignored if you have called
        set_q_form_matrix() or set_s_form_matrix() to provide the orientation
        information for the file.
        """
    )

    nifti_version = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the version number for the n_if_ti file format to use. This can
        be 1, 2, or 0 (the default).  If set to zero, then it will save
        as n_if_ti version 1 unless set_nifti_header() provided header
        information from a n_if_ti version 2 file.
        """
    )

    def _nifti_version_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNIFTIVersion,
                        self.nifti_version)

    q_fac = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        The QFac sets the ordering of the slices in the NIFTI file. If
        QFac is -1, then the slice ordering in the file will be reversed
        as compared to VTK. Use with caution.
        """
    )

    def _q_fac_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQFac,
                        self.q_fac)

    def _get_q_form_matrix(self):
        return wrap_vtk(self._vtk_obj.GetQFormMatrix())
    def _set_q_form_matrix(self, arg):
        old_val = self._get_q_form_matrix()
        self._wrap_call(self._vtk_obj.SetQFormMatrix,
                        deref_vtk(arg))
        self.trait_property_changed('q_form_matrix', old_val, arg)
    q_form_matrix = traits.Property(_get_q_form_matrix, _set_q_form_matrix, help=\
        """
        
        """
    )

    rescale_intercept = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the slope and intercept for calibrating the scalar values.
        Other programs that read the NIFTI file can use the equation v =
        u*_rescale_slope + rescale_intercept to rescale the data to real
        values.  If both the slope and the intercept are zero, then the
        scl_slope and scl_intercept in the header info provided via
        set_nifti_header() are used instead.
        """
    )

    def _rescale_intercept_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRescaleIntercept,
                        self.rescale_intercept)

    rescale_slope = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the slope and intercept for calibrating the scalar values.
        Other programs that read the NIFTI file can use the equation v =
        u*_rescale_slope + rescale_intercept to rescale the data to real
        values.  If both the slope and the intercept are zero, then the
        scl_slope and scl_intercept in the header info provided via
        set_nifti_header() are used instead.
        """
    )

    def _rescale_slope_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRescaleSlope,
                        self.rescale_slope)

    def _get_s_form_matrix(self):
        return wrap_vtk(self._vtk_obj.GetSFormMatrix())
    def _set_s_form_matrix(self, arg):
        old_val = self._get_s_form_matrix()
        self._wrap_call(self._vtk_obj.SetSFormMatrix,
                        deref_vtk(arg))
        self.trait_property_changed('s_form_matrix', old_val, arg)
    s_form_matrix = traits.Property(_get_s_form_matrix, _set_s_form_matrix, help=\
        """
        
        """
    )

    time_dimension = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the time dimension to use in the NIFTI file (or zero if
        none). The number of components of the input data must be
        divisible by the time dimension if the time dimension is not set
        to zero.  The vector dimension will be set to the number of
        components divided by the time dimension.
        """
    )

    def _time_dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeDimension,
                        self.time_dimension)

    time_spacing = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the time dimension to use in the NIFTI file (or zero if
        none). The number of components of the input data must be
        divisible by the time dimension if the time dimension is not set
        to zero.  The vector dimension will be set to the number of
        components divided by the time dimension.
        """
    )

    def _time_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeSpacing,
                        self.time_spacing)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input object from the image pipeline.
        """
    )

    _updateable_traits_ = \
    (('planar_rgb', 'GetPlanarRGB'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('description',
    'GetDescription'), ('nifti_version', 'GetNIFTIVersion'), ('q_fac',
    'GetQFac'), ('rescale_intercept', 'GetRescaleIntercept'),
    ('rescale_slope', 'GetRescaleSlope'), ('time_dimension',
    'GetTimeDimension'), ('time_spacing', 'GetTimeSpacing'),
    ('file_dimensionality', 'GetFileDimensionality'), ('file_name',
    'GetFileName'), ('file_pattern', 'GetFilePattern'), ('file_prefix',
    'GetFilePrefix'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'planar_rgb',
    'release_data_flag', 'description', 'file_dimensionality',
    'file_name', 'file_pattern', 'file_prefix', 'nifti_version',
    'progress_text', 'q_fac', 'rescale_intercept', 'rescale_slope',
    'time_dimension', 'time_spacing'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(NIFTIImageWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit NIFTIImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['planar_rgb'], [], ['description', 'file_dimensionality',
            'file_name', 'file_pattern', 'file_prefix', 'nifti_version', 'q_fac',
            'rescale_intercept', 'rescale_slope', 'time_dimension',
            'time_spacing']),
            title='Edit NIFTIImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit NIFTIImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


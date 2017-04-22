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

from tvtk.tvtk_classes.object import Object


class NIFTIImageHeader(Object):
    """
    NIFTIImageHeader - Store n_if_ti header information.
    
    Superclass: Object
    
    This class stores the header of a n_if_ti file in a VTK-friendly
    format. By using this class, it is possible to specify the header
    information that will be stored in a file written by the
    NIFTIImageWriter.  Note that the SForm and QForm orientation
    information in this class will be ignored by the writer if an SForm
    and QForm have been explicitly set via the writer's set_s_form and
    set_q_form methods.  Also note that all info like Dim, pix_dim,
    data_type, etc. will be ignored by the writer because this information
    must instead be taken from the ImageData information.  Finally,
    note that the NIFTIImageWriter will ignore the Descrip field,
    since it has its own set_description method.@par Thanks: This class
    was contributed to VTK by the Calgary Image Processing and Analysis
    Centre (CIPAC).
    @sa
    NIFTIImageReader, NIFTIImageWriter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkNIFTIImageHeader, obj, update, **traits)
    
    aux_file = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Get an auxilliary file, e.g. a color table, that is associated
        with this data.  The length of the filename must be a maximum of
        24 characters, and it will be assumed to be in the same directory
        as the NIFTI file.
        """
    )

    def _aux_file_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAuxFile,
                        self.aux_file)

    cal_max = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get the calibrated range of the data, i.e. the values stored in
        the cal_min and cal_max fields in the header.
        """
    )

    def _cal_max_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCalMax,
                        self.cal_max)

    cal_min = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get the calibrated range of the data, i.e. the values stored in
        the cal_min and cal_max fields in the header.
        """
    )

    def _cal_min_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCalMin,
                        self.cal_min)

    descrip = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Get a null-terminated file descriptor, this usually gives the
        name of the software that wrote the file. It will have a maximum
        length of 80 characters.  Use ASCII to ensure compatibility with
        all NIFTI software, the NIFTI standard itself does not specify
        what encodings are permitted.
        """
    )

    def _descrip_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDescrip,
                        self.descrip)

    dim_info = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get a bitfield with extra information about the dimensions, it
        states which dimensions are the phase encode, frequency encode,
        and slice encode dimensions for MRI acquisitions.
        """
    )

    def _dim_info_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimInfo,
                        self.dim_info)

    intent_code = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get the NIFTI intent code.  This is an enumerated value in the
        NIFTI header that states what the data is intended to be used
        for.
        """
    )

    def _intent_code_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntentCode,
                        self.intent_code)

    intent_name = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Get the intent name.  This should match the intent code.
        """
    )

    def _intent_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntentName,
                        self.intent_name)

    intent_p1 = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get one of the NIFTI intent parameters.  The definition of these
        parameters varies according to the intent_code.
        """
    )

    def _intent_p1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntentP1,
                        self.intent_p1)

    intent_p2 = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get one of the NIFTI intent parameters.  The definition of these
        parameters varies according to the intent_code.
        """
    )

    def _intent_p2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntentP2,
                        self.intent_p2)

    intent_p3 = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get one of the NIFTI intent parameters.  The definition of these
        parameters varies according to the intent_code.
        """
    )

    def _intent_p3_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntentP3,
                        self.intent_p3)

    q_form_code = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get the QForm or SForm code.
        """
    )

    def _q_form_code_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQFormCode,
                        self.q_form_code)

    q_offset_x = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get information about the quaternion transformation.  Note that
        the NIFTIImageWriter ignores this part of the header if a
        quaternion has been set via
        NIFTIImageWriter::SetQFormMatrix().
        """
    )

    def _q_offset_x_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQOffsetX,
                        self.q_offset_x)

    q_offset_y = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get information about the quaternion transformation.  Note that
        the NIFTIImageWriter ignores this part of the header if a
        quaternion has been set via
        NIFTIImageWriter::SetQFormMatrix().
        """
    )

    def _q_offset_y_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQOffsetY,
                        self.q_offset_y)

    q_offset_z = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get information about the quaternion transformation.  Note that
        the NIFTIImageWriter ignores this part of the header if a
        quaternion has been set via
        NIFTIImageWriter::SetQFormMatrix().
        """
    )

    def _q_offset_z_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQOffsetZ,
                        self.q_offset_z)

    quatern_b = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get information about the quaternion transformation.  Note that
        the NIFTIImageWriter ignores this part of the header if a
        quaternion has been set via
        NIFTIImageWriter::SetQFormMatrix().
        """
    )

    def _quatern_b_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuaternB,
                        self.quatern_b)

    quatern_c = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get information about the quaternion transformation.  Note that
        the NIFTIImageWriter ignores this part of the header if a
        quaternion has been set via
        NIFTIImageWriter::SetQFormMatrix().
        """
    )

    def _quatern_c_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuaternC,
                        self.quatern_c)

    quatern_d = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get information about the quaternion transformation.  Note that
        the NIFTIImageWriter ignores this part of the header if a
        quaternion has been set via
        NIFTIImageWriter::SetQFormMatrix().
        """
    )

    def _quatern_d_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuaternD,
                        self.quatern_d)

    s_form_code = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get the QForm or SForm code.
        """
    )

    def _s_form_code_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSFormCode,
                        self.s_form_code)

    s_row_x = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _s_row_x_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSRowX,
                        self.s_row_x)

    s_row_y = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _s_row_y_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSRowY,
                        self.s_row_y)

    s_row_z = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _s_row_z_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSRowZ,
                        self.s_row_z)

    scl_inter = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get the scale and slope to apply to the data in order to get the
        real-valued data values.
        """
    )

    def _scl_inter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSclInter,
                        self.scl_inter)

    scl_slope = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get the scale and slope to apply to the data in order to get the
        real-valued data values.
        """
    )

    def _scl_slope_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSclSlope,
                        self.scl_slope)

    slice_code = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get the slice code for the data.
        """
    )

    def _slice_code_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceCode,
                        self.slice_code)

    slice_duration = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get the slice_duration and toffset from the header.
        """
    )

    def _slice_duration_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceDuration,
                        self.slice_duration)

    slice_end = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get the slice range for the data.
        """
    )

    def _slice_end_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceEnd,
                        self.slice_end)

    slice_start = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get the slice range for the data.
        """
    )

    def _slice_start_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceStart,
                        self.slice_start)

    t_offset = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Get the slice_duration and toffset from the header.
        """
    )

    def _t_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTOffset,
                        self.t_offset)

    xyzt_units = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get a bitfield that describes the units for the first 4 dims.
        """
    )

    def _xyzt_units_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXYZTUnits,
                        self.xyzt_units)

    def _get_bit_pix(self):
        return self._vtk_obj.GetBitPix()
    bit_pix = traits.Property(_get_bit_pix, help=\
        """
        Get the number of bits per pixel.
        """
    )

    def _get_data_type(self):
        return self._vtk_obj.GetDataType()
    data_type = traits.Property(_get_data_type, help=\
        """
        Get the data type.
        """
    )

    def get_dim(self, *args):
        """
        V.get_dim(int) -> int
        C++: TypeInt64 GetDim(int i)
        Get the nth dimension of the data, where get_dim(_0) returns the
        number of dimensions that are defined for the file.
        """
        ret = self._wrap_call(self._vtk_obj.GetDim, *args)
        return ret

    def _get_magic(self):
        return self._vtk_obj.GetMagic()
    magic = traits.Property(_get_magic, help=\
        """
        Get the magic number for the NIFTI file as a null-terminated
        string.
        """
    )

    def get_pix_dim(self, *args):
        """
        V.get_pix_dim(int) -> float
        C++: double GetPixDim(int i)
        Get the sample spacing in the nth dimension. If get_pix_dim(_0) is
        negative, then the quaternion for the qform describes the correct
        orientation only after the slice ordering has been reversed.
        """
        ret = self._wrap_call(self._vtk_obj.GetPixDim, *args)
        return ret

    def _get_vox_offset(self):
        return self._vtk_obj.GetVoxOffset()
    vox_offset = traits.Property(_get_vox_offset, help=\
        """
        Get the offset to the pixel data within the file.
        """
    )

    def deep_copy(self, *args):
        """
        V.deep_copy(NIFTIImageHeader)
        C++: void DeepCopy(NIFTIImageHeader *o)
        Make a copy of the header.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Initialize the header to default values.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('aux_file', 'GetAuxFile'), ('cal_max',
    'GetCalMax'), ('cal_min', 'GetCalMin'), ('descrip', 'GetDescrip'),
    ('dim_info', 'GetDimInfo'), ('intent_code', 'GetIntentCode'),
    ('intent_name', 'GetIntentName'), ('intent_p1', 'GetIntentP1'),
    ('intent_p2', 'GetIntentP2'), ('intent_p3', 'GetIntentP3'),
    ('q_form_code', 'GetQFormCode'), ('q_offset_x', 'GetQOffsetX'),
    ('q_offset_y', 'GetQOffsetY'), ('q_offset_z', 'GetQOffsetZ'),
    ('quatern_b', 'GetQuaternB'), ('quatern_c', 'GetQuaternC'),
    ('quatern_d', 'GetQuaternD'), ('s_form_code', 'GetSFormCode'),
    ('s_row_x', 'GetSRowX'), ('s_row_y', 'GetSRowY'), ('s_row_z',
    'GetSRowZ'), ('scl_inter', 'GetSclInter'), ('scl_slope',
    'GetSclSlope'), ('slice_code', 'GetSliceCode'), ('slice_duration',
    'GetSliceDuration'), ('slice_end', 'GetSliceEnd'), ('slice_start',
    'GetSliceStart'), ('t_offset', 'GetTOffset'), ('xyzt_units',
    'GetXYZTUnits'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'aux_file', 'cal_max', 'cal_min',
    'descrip', 'dim_info', 'intent_code', 'intent_name', 'intent_p1',
    'intent_p2', 'intent_p3', 'q_form_code', 'q_offset_x', 'q_offset_y',
    'q_offset_z', 'quatern_b', 'quatern_c', 'quatern_d', 's_form_code',
    's_row_x', 's_row_y', 's_row_z', 'scl_inter', 'scl_slope',
    'slice_code', 'slice_duration', 'slice_end', 'slice_start',
    't_offset', 'xyzt_units'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(NIFTIImageHeader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit NIFTIImageHeader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['aux_file', 'cal_max', 'cal_min', 'descrip',
            'dim_info', 'intent_code', 'intent_name', 'intent_p1', 'intent_p2',
            'intent_p3', 'q_form_code', 'q_offset_x', 'q_offset_y', 'q_offset_z',
            'quatern_b', 'quatern_c', 'quatern_d', 's_form_code', 's_row_x',
            's_row_y', 's_row_z', 'scl_inter', 'scl_slope', 'slice_code',
            'slice_duration', 'slice_end', 'slice_start', 't_offset',
            'xyzt_units']),
            title='Edit NIFTIImageHeader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit NIFTIImageHeader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


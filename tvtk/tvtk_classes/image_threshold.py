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


class ImageThreshold(ThreadedImageAlgorithm):
    """
    ImageThreshold - Flexible threshold
    
    Superclass: ThreadedImageAlgorithm
    
    ImageThreshold can do binary or continuous thresholding for lower,
    upper or a range of data.  The output data type may be different than
    the output, but defaults to the same type.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageThreshold, obj, update, **traits)
    
    replace_in = tvtk_base.false_bool_trait(help=\
        """
        Determines whether to replace the pixel in range with in_value
        """
    )

    def _replace_in_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReplaceIn,
                        self.replace_in_)

    replace_out = tvtk_base.false_bool_trait(help=\
        """
        Determines whether to replace the pixel out of range with
        out_value
        """
    )

    def _replace_out_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReplaceOut,
                        self.replace_out_)

    def get_output_scalar_type(self):
        """
        V.get_output_scalar_type() -> int
        C++: int GetOutputScalarType()
        Set the desired output scalar type to cast to
        """
        ret = self._vtk_obj.GetOutputScalarType()
        return ret
        

    def set_output_scalar_type(self, *args):
        """
        V.set_output_scalar_type(int)
        C++: void SetOutputScalarType(int a)
        Set the desired output scalar type to cast to
        """
        ret = self._wrap_call(self._vtk_obj.SetOutputScalarType, *args)
        return ret

    def set_output_scalar_type_to_double(self):
        """
        V.set_output_scalar_type_to_double()
        C++: void SetOutputScalarTypeToDouble()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToDouble()

    def set_output_scalar_type_to_float(self):
        """
        V.set_output_scalar_type_to_float()
        C++: void SetOutputScalarTypeToFloat()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToFloat()

    def set_output_scalar_type_to_int(self):
        """
        V.set_output_scalar_type_to_int()
        C++: void SetOutputScalarTypeToInt()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToInt()

    def set_output_scalar_type_to_long(self):
        """
        V.set_output_scalar_type_to_long()
        C++: void SetOutputScalarTypeToLong()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToLong()

    def set_output_scalar_type_to_short(self):
        """
        V.set_output_scalar_type_to_short()
        C++: void SetOutputScalarTypeToShort()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToShort()

    def set_output_scalar_type_to_signed_char(self):
        """
        V.set_output_scalar_type_to_signed_char()
        C++: void SetOutputScalarTypeToSignedChar()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToSignedChar()

    def set_output_scalar_type_to_unsigned_char(self):
        """
        V.set_output_scalar_type_to_unsigned_char()
        C++: void SetOutputScalarTypeToUnsignedChar()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedChar()

    def set_output_scalar_type_to_unsigned_int(self):
        """
        V.set_output_scalar_type_to_unsigned_int()
        C++: void SetOutputScalarTypeToUnsignedInt()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedInt()

    def set_output_scalar_type_to_unsigned_long(self):
        """
        V.set_output_scalar_type_to_unsigned_long()
        C++: void SetOutputScalarTypeToUnsignedLong()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedLong()

    def set_output_scalar_type_to_unsigned_short(self):
        """
        V.set_output_scalar_type_to_unsigned_short()
        C++: void SetOutputScalarTypeToUnsignedShort()
        Set the desired output scalar type to cast to
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedShort()

    in_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Replace the in range pixels with this value.
        """
    )

    def _in_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInValue,
                        self.in_value)

    out_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Replace the in range pixels with this value.
        """
    )

    def _out_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutValue,
                        self.out_value)

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

    def _get_lower_threshold(self):
        return self._vtk_obj.GetLowerThreshold()
    lower_threshold = traits.Property(_get_lower_threshold, help=\
        """
        Get the Upper and Lower thresholds.
        """
    )

    def _get_upper_threshold(self):
        return self._vtk_obj.GetUpperThreshold()
    upper_threshold = traits.Property(_get_upper_threshold, help=\
        """
        Get the Upper and Lower thresholds.
        """
    )

    def threshold_between(self, *args):
        """
        V.threshold_between(float, float)
        C++: void ThresholdBetween(double lower, double upper)
        The values in a range (inclusive) match
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdBetween, *args)
        return ret

    def threshold_by_lower(self, *args):
        """
        V.threshold_by_lower(float)
        C++: void ThresholdByLower(double thresh)
        The values less than or equal to the value match.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdByLower, *args)
        return ret

    def threshold_by_upper(self, *args):
        """
        V.threshold_by_upper(float)
        C++: void ThresholdByUpper(double thresh)
        The values greater than or equal to the value match.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdByUpper, *args)
        return ret

    _updateable_traits_ = \
    (('replace_in', 'GetReplaceIn'), ('replace_out', 'GetReplaceOut'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('split_mode',
    'GetSplitMode'), ('in_value', 'GetInValue'), ('out_value',
    'GetOutValue'), ('desired_bytes_per_piece',
    'GetDesiredBytesPerPiece'), ('enable_smp', 'GetEnableSMP'),
    ('global_default_enable_smp', 'GetGlobalDefaultEnableSMP'),
    ('minimum_piece_size', 'GetMinimumPieceSize'), ('number_of_threads',
    'GetNumberOfThreads'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'replace_in', 'replace_out', 'split_mode',
    'desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
    'in_value', 'minimum_piece_size', 'number_of_threads', 'out_value',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageThreshold, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageThreshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['replace_in', 'replace_out'], ['split_mode'],
            ['desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
            'in_value', 'minimum_piece_size', 'number_of_threads', 'out_value']),
            title='Edit ImageThreshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageThreshold properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


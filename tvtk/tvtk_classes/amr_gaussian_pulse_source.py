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

from tvtk.tvtk_classes.overlapping_amr_algorithm import OverlappingAMRAlgorithm


class AMRGaussianPulseSource(OverlappingAMRAlgorithm):
    """
    AMRGaussianPulseSource -  A source that generates sample AMR data
    with gaussian pulse field.
    
    Superclass: OverlappingAMRAlgorithm
    
    The user
     can control the refinement ratio as well as the pulse attributes
    such as
     the pulse origin, length and amplitude.
    
    @sa
     OverlappingAMR
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAMRGaussianPulseSource, obj, update, **traits)
    
    pulse_amplitude = traits.Float(0.0001, enter_set=True, auto_set=False, help=\
        """
        Set & Get macro for the pulse amplitude
        """
    )

    def _pulse_amplitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPulseAmplitude,
                        self.pulse_amplitude)

    pulse_origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _pulse_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPulseOrigin,
                        self.pulse_origin)

    pulse_width = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.5, 0.5, 0.5), cols=3, help=\
        """
        
        """
    )

    def _pulse_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPulseWidth,
                        self.pulse_width)

    def set_dimension(self, *args):
        """
        V.set_dimension(int)
        C++: void SetDimension(int a)
        Sets the dimension of the AMR dataset to generate
        """
        ret = self._wrap_call(self._vtk_obj.SetDimension, *args)
        return ret

    def set_number_of_levels(self, *args):
        """
        V.set_number_of_levels(int)
        C++: void SetNumberOfLevels(int a)
        Sets the number of levels to generate
        """
        ret = self._wrap_call(self._vtk_obj.SetNumberOfLevels, *args)
        return ret

    def set_refinement_ratio(self, *args):
        """
        V.set_refinement_ratio(int)
        C++: void SetRefinementRatio(int r)
        Set the refinement ratio
        """
        ret = self._wrap_call(self._vtk_obj.SetRefinementRatio, *args)
        return ret

    def set_root_spacing(self, *args):
        """
        V.set_root_spacing(float)
        C++: void SetRootSpacing(double h0)
        Set the root spacing
        """
        ret = self._wrap_call(self._vtk_obj.SetRootSpacing, *args)
        return ret

    def set_x_pulse_origin(self, *args):
        """
        V.set_x_pulse_origin(float)
        C++: void SetXPulseOrigin(double f)
        Set & Get macro for the pulse origin
        """
        ret = self._wrap_call(self._vtk_obj.SetXPulseOrigin, *args)
        return ret

    def set_x_pulse_width(self, *args):
        """
        V.set_x_pulse_width(float)
        C++: void SetXPulseWidth(double f)
        Set & Get macro for the pulse width
        """
        ret = self._wrap_call(self._vtk_obj.SetXPulseWidth, *args)
        return ret

    def set_y_pulse_origin(self, *args):
        """
        V.set_y_pulse_origin(float)
        C++: void SetYPulseOrigin(double f)
        Set & Get macro for the pulse origin
        """
        ret = self._wrap_call(self._vtk_obj.SetYPulseOrigin, *args)
        return ret

    def set_y_pulse_width(self, *args):
        """
        V.set_y_pulse_width(float)
        C++: void SetYPulseWidth(double f)
        Set & Get macro for the pulse width
        """
        ret = self._wrap_call(self._vtk_obj.SetYPulseWidth, *args)
        return ret

    def set_z_pulse_origin(self, *args):
        """
        V.set_z_pulse_origin(float)
        C++: void SetZPulseOrigin(double f)
        Set & Get macro for the pulse origin
        """
        ret = self._wrap_call(self._vtk_obj.SetZPulseOrigin, *args)
        return ret

    def set_z_pulse_width(self, *args):
        """
        V.set_z_pulse_width(float)
        C++: void SetZPulseWidth(double f)
        Set & Get macro for the pulse width
        """
        ret = self._wrap_call(self._vtk_obj.SetZPulseWidth, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pulse_amplitude', 'GetPulseAmplitude'), ('pulse_origin',
    'GetPulseOrigin'), ('pulse_width', 'GetPulseWidth'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'pulse_amplitude',
    'pulse_origin', 'pulse_width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AMRGaussianPulseSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AMRGaussianPulseSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['pulse_amplitude', 'pulse_origin', 'pulse_width']),
            title='Edit AMRGaussianPulseSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AMRGaussianPulseSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


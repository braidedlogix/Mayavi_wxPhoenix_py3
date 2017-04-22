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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class AMRCutPlane(MultiBlockDataSetAlgorithm):
    """
    AMRCutPlane -  A concrete instance of MultiBlockDataSet that
    provides functionality for cutting an AMR dataset (an instance of
    OverlappingAMR) with user supplied implicit plane function defined
    by a normal and center.
    
    Superclass: MultiBlockDataSetAlgorithm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAMRCutPlane, obj, update, **traits)
    
    use_native_cutter = tvtk_base.true_bool_trait(help=\
        """
        
        """
    )

    def _use_native_cutter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseNativeCutter,
                        self.use_native_cutter_)

    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        Set/Get a multiprocess controller for parallel processing. By
        default this parameter is set to NULL by the constructor.
        """
    )

    level_of_resolution = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Sets the level of resolution
        """
    )

    def _level_of_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLevelOfResolution,
                        self.level_of_resolution)

    def fill_input_port_information(self, *args):
        """
        V.fill_input_port_information(int, Information) -> int
        C++: virtual int FillInputPortInformation(int port,
            Information *info)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillInputPortInformation, *my_args)
        return ret

    def fill_output_port_information(self, *args):
        """
        V.fill_output_port_information(int, Information) -> int
        C++: virtual int FillOutputPortInformation(int port,
            Information *info)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillOutputPortInformation, *my_args)
        return ret

    def set_center(self, *args):
        """
        V.set_center(float, float, float)
        C++: void SetCenter(double, double, double)
        V.set_center((float, float, float))
        C++: void SetCenter(double a[3])"""
        ret = self._wrap_call(self._vtk_obj.SetCenter, *args)
        return ret

    def set_normal(self, *args):
        """
        V.set_normal(float, float, float)
        C++: void SetNormal(double, double, double)
        V.set_normal((float, float, float))
        C++: void SetNormal(double a[3])"""
        ret = self._wrap_call(self._vtk_obj.SetNormal, *args)
        return ret

    _updateable_traits_ = \
    (('use_native_cutter', 'GetUseNativeCutter'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('level_of_resolution',
    'GetLevelOfResolution'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'use_native_cutter', 'level_of_resolution',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AMRCutPlane, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AMRCutPlane properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_native_cutter'], [], ['level_of_resolution']),
            title='Edit AMRCutPlane properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AMRCutPlane properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


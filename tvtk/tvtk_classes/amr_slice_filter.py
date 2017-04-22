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


class AMRSliceFilter(OverlappingAMRAlgorithm):
    """
    AMRSliceFilter -  A concrete instance of
    OverlappingAMRAlgorithm which implements
     functionality for extracting slices from AMR data.
    
    Superclass: OverlappingAMRAlgorithm
    
    Unlike the conventional
     slice filter, the output of this filter is a 2-D AMR dataset itself.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAMRSliceFilter, obj, update, **traits)
    
    enable_prefetching = tvtk_base.true_bool_trait(help=\
        """
        Set/Get enable_prefetching property
        """
    )

    def _enable_prefetching_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnablePrefetching,
                        self.enable_prefetching_)

    forward_upstream = tvtk_base.true_bool_trait(help=\
        """
        Set/Get forward_upstream property
        """
    )

    def _forward_upstream_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForwardUpstream,
                        self.forward_upstream_)

    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        Set/Get a multiprocess controller for paralle processing. By
        default this parameter is set to NULL by the constructor.
        """
    )

    max_resolution = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the maximum resolution used in this instance.
        """
    )

    def _max_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxResolution,
                        self.max_resolution)

    normal = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Axis normal. There are only 3 acceptable values
        1-(X-Normal); 2-(Y-Normal); 3-(Z-Normal)
        """
    )

    def _normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormal,
                        self.normal)

    off_set_from_origin = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _off_set_from_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffSetFromOrigin,
                        self.off_set_from_origin)

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

    _updateable_traits_ = \
    (('enable_prefetching', 'GetEnablePrefetching'), ('forward_upstream',
    'GetForwardUpstream'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('max_resolution', 'GetMaxResolution'), ('normal', 'GetNormal'),
    ('off_set_from_origin', 'GetOffSetFromOrigin'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'enable_prefetching', 'forward_upstream',
    'global_warning_display', 'release_data_flag', 'max_resolution',
    'normal', 'off_set_from_origin', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AMRSliceFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AMRSliceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enable_prefetching', 'forward_upstream'], [],
            ['max_resolution', 'normal', 'off_set_from_origin']),
            title='Edit AMRSliceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AMRSliceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


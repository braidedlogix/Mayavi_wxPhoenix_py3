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

from tvtk.tvtk_classes.composite_data_probe_filter import CompositeDataProbeFilter


class PProbeFilter(CompositeDataProbeFilter):
    """
    PProbeFilter - probe dataset in parallel
    
    Superclass: CompositeDataProbeFilter
    
    This filter works correctly only if the whole geometry dataset (that
    specify the point locations used to probe input) is available on all
    nodes.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPProbeFilter, obj, update, **traits)
    
    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        Set and get the controller.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    _updateable_traits_ = \
    (('pass_partial_arrays', 'GetPassPartialArrays'),
    ('compute_tolerance', 'GetComputeTolerance'), ('pass_cell_arrays',
    'GetPassCellArrays'), ('pass_field_arrays', 'GetPassFieldArrays'),
    ('pass_point_arrays', 'GetPassPointArrays'), ('spatial_match',
    'GetSpatialMatch'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('tolerance',
    'GetTolerance'), ('valid_point_mask_array_name',
    'GetValidPointMaskArrayName'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_tolerance', 'debug',
    'global_warning_display', 'pass_cell_arrays', 'pass_field_arrays',
    'pass_partial_arrays', 'pass_point_arrays', 'release_data_flag',
    'spatial_match', 'progress_text', 'tolerance',
    'valid_point_mask_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PProbeFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_tolerance', 'pass_cell_arrays', 'pass_field_arrays',
            'pass_partial_arrays', 'pass_point_arrays', 'spatial_match'], [],
            ['tolerance', 'valid_point_mask_array_name']),
            title='Edit PProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


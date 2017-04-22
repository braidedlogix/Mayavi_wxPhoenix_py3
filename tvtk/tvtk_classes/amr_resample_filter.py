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


class AMRResampleFilter(MultiBlockDataSetAlgorithm):
    """
    AMRResampleFilter -  This filter is a concrete instance of
    MultiBlockDataSetAlgorithm and
     provides functionality for extracting portion of the AMR dataset,
    specified
     by a bounding box, in a uniform grid of the desired level of
    resolution.
    
    Superclass: MultiBlockDataSetAlgorithm
    
    The resulting uniform grid is stored in a MultiBlockDataSet where
    the
     number of blocks correspond to the number of processors utilized for
    the
     operation.
    
    @warning
     Data of the input AMR dataset is assumed to be cell-centered.
    
    @sa
     OverlappingAMR, UniformGrid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAMRResampleFilter, obj, update, **traits)
    
    bias_vector = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _bias_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBiasVector,
                        self.bias_vector)

    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        Set & Get macro for the multi-process controller
        """
    )

    demand_driven_mode = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set & Get macro to allow the filter to operate in both
        demand-driven and standard modes
        """
    )

    def _demand_driven_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDemandDrivenMode,
                        self.demand_driven_mode)

    max = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _max_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMax,
                        self.max)

    min = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _min_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMin,
                        self.min)

    number_of_partitions = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set & Get macro for the number of subdivisions
        """
    )

    def _number_of_partitions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPartitions,
                        self.number_of_partitions)

    number_of_samples = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(10, 10, 10), cols=3, help=\
        """
        
        """
    )

    def _number_of_samples_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSamples,
                        self.number_of_samples)

    transfer_to_nodes = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set & Get macro for the transfer_to_nodes flag
        """
    )

    def _transfer_to_nodes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTransferToNodes,
                        self.transfer_to_nodes)

    use_bias_vector = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Set & Get macro for the number of subdivisions
        """
    )

    def _use_bias_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseBiasVector,
                        self.use_bias_vector)

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
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('bias_vector',
    'GetBiasVector'), ('demand_driven_mode', 'GetDemandDrivenMode'),
    ('max', 'GetMax'), ('min', 'GetMin'), ('number_of_partitions',
    'GetNumberOfPartitions'), ('number_of_samples', 'GetNumberOfSamples'),
    ('transfer_to_nodes', 'GetTransferToNodes'), ('use_bias_vector',
    'GetUseBiasVector'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'bias_vector', 'demand_driven_mode', 'max',
    'min', 'number_of_partitions', 'number_of_samples', 'progress_text',
    'transfer_to_nodes', 'use_bias_vector'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AMRResampleFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AMRResampleFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['bias_vector', 'demand_driven_mode', 'max', 'min',
            'number_of_partitions', 'number_of_samples', 'transfer_to_nodes',
            'use_bias_vector']),
            title='Edit AMRResampleFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AMRResampleFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


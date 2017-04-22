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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class GradientFilter(DataSetAlgorithm):
    """
    GradientFilter - A general filter for gradient estimation.
    
    Superclass: DataSetAlgorithm
    
    Estimates the gradient of a field in a data set.  The gradient
    calculation is dependent on the input dataset type.  The created
    gradient array is of the same type as the array it is calculated from
    (e.g. point data or cell data) as well as data type (e.g. float,
    double).  At the boundary the gradient is not central differencing. 
    The output array has 3*number of components of the input data array. 
    The ordering for the output tuple will be {du/dx, du/dy, du/dz,
    dv/dx, dv/dy, dv/dz, dw/dx, dw/dy, dw/dz} for an input array {u, v,
    w}. There are also the options to additionally compute the vorticity
    and Q criterion of a vector field.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGradientFilter, obj, update, **traits)
    
    compute_divergence = tvtk_base.false_bool_trait(help=\
        """
        Add divergence to the output field data.  The name of the array
        will be divergence_array_name and will be the same type as the
        input array.  The input array must have 3 components in order to
        compute this. The default is off.
        """
    )

    def _compute_divergence_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeDivergence,
                        self.compute_divergence_)

    compute_gradient = tvtk_base.true_bool_trait(help=\
        """
        Add the gradient to the output field data.  The name of the array
        will be result_array_name and will be the same type as the input
        array. The default is on.
        """
    )

    def _compute_gradient_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeGradient,
                        self.compute_gradient_)

    compute_q_criterion = tvtk_base.false_bool_trait(help=\
        """
        Add Q-criterion to the output field data.  The name of the array
        will be q_criterion_array_name and will be the same type as the
        input array.  The input array must have 3 components in order to
        compute this.  Note that Q-citerion is a balance of the rate of
        vorticity and the rate of strain. The default is off.
        """
    )

    def _compute_q_criterion_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeQCriterion,
                        self.compute_q_criterion_)

    compute_vorticity = tvtk_base.false_bool_trait(help=\
        """
        Add voriticity/curl to the output field data.  The name of the
        array will be vorticity_array_name and will be the same type as the
        input array.  The input array must have 3 components in order to
        compute this. The default is off.
        """
    )

    def _compute_vorticity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeVorticity,
                        self.compute_vorticity_)

    faster_approximation = tvtk_base.false_bool_trait(help=\
        """
        When this flag is on (default is off), the gradient filter will
        provide a less accurate (but close) algorithm that performs fewer
        derivative calculations (and is therefore faster).  The error
        contains some smoothing of the output data and some possible
        errors on the boundary.  This parameter has no effect when
        performing the gradient of cell data. This only applies if the
        input grid is a UnstructuredGrid or a PolyData.
        """
    )

    def _faster_approximation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFasterApproximation,
                        self.faster_approximation_)

    divergence_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Get/Set the name of the divergence array to create. This is only
        used if compute_divergence is non-zero. If NULL (the default) then
        the output array will be named "Divergence".
        """
    )

    def _divergence_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDivergenceArrayName,
                        self.divergence_array_name)

    q_criterion_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Get/Set the name of the Q criterion array to create. This is only
        used if compute_q_criterion is non-zero. If NULL (the default) then
        the output array will be named "Q-criterion".
        """
    )

    def _q_criterion_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQCriterionArrayName,
                        self.q_criterion_array_name)

    result_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Get/Set the name of the gradient array to create.  This is only
        used if compute_gradient is non-zero. If NULL (the default) then
        the output array will be named "Gradients".
        """
    )

    def _result_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResultArrayName,
                        self.result_array_name)

    vorticity_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Get/Set the name of the vorticity array to create. This is only
        used if compute_vorticity is non-zero. If NULL (the default) then
        the output array will be named "Vorticity".
        """
    )

    def _vorticity_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVorticityArrayName,
                        self.vorticity_array_name)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def set_input_scalars(self, *args):
        """
        V.set_input_scalars(int, string)
        C++: virtual void SetInputScalars(int fieldAssociation,
            const char *name)
        V.set_input_scalars(int, int)
        C++: virtual void SetInputScalars(int fieldAssociation,
            int fieldAttributeType)
        These are basically a convenience method that calls
        set_input_array_to_process to set the array used as the input
        scalars.  The field_association comes from the
        DataObject::FieldAssocations enum.  The field_attribute_type
        comes from the DataSetAttributes::AttributeTypes enum.
        """
        ret = self._wrap_call(self._vtk_obj.SetInputScalars, *args)
        return ret

    _updateable_traits_ = \
    (('compute_divergence', 'GetComputeDivergence'), ('compute_gradient',
    'GetComputeGradient'), ('compute_q_criterion',
    'GetComputeQCriterion'), ('compute_vorticity', 'GetComputeVorticity'),
    ('faster_approximation', 'GetFasterApproximation'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('divergence_array_name',
    'GetDivergenceArrayName'), ('q_criterion_array_name',
    'GetQCriterionArrayName'), ('result_array_name',
    'GetResultArrayName'), ('vorticity_array_name',
    'GetVorticityArrayName'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_divergence', 'compute_gradient',
    'compute_q_criterion', 'compute_vorticity', 'debug',
    'faster_approximation', 'global_warning_display', 'release_data_flag',
    'divergence_array_name', 'progress_text', 'q_criterion_array_name',
    'result_array_name', 'vorticity_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GradientFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GradientFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_divergence', 'compute_gradient',
            'compute_q_criterion', 'compute_vorticity', 'faster_approximation'],
            [], ['divergence_array_name', 'q_criterion_array_name',
            'result_array_name', 'vorticity_array_name']),
            title='Edit GradientFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GradientFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


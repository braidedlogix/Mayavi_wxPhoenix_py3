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


class SampleImplicitFunctionFilter(DataSetAlgorithm):
    """
    SampleImplicitFunctionFilter - sample an implicit function over a
    dataset, generating scalar values and optional gradient vectors
    
    Superclass: DataSetAlgorithm
    
    SampleImplicitFunctionFilter is a filter that evaluates an
    implicit function and (optional) gradients at each point in an input
    DataSet. The output of the filter are new scalar values (the
    function values) and the optional vector (function gradient) array.
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    SampleFunction ImplicitModeller
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSampleImplicitFunctionFilter, obj, update, **traits)
    
    compute_gradients = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the computation of gradients.
        """
    )

    def _compute_gradients_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeGradients,
                        self.compute_gradients_)

    gradient_array_name = traits.String('Implicit gradients', enter_set=True, auto_set=False, help=\
        """
        Set/get the gradient array name for this data set. The initial
        value is "Implicit gradients".
        """
    )

    def _gradient_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGradientArrayName,
                        self.gradient_array_name)

    def _get_implicit_function(self):
        return wrap_vtk(self._vtk_obj.GetImplicitFunction())
    def _set_implicit_function(self, arg):
        old_val = self._get_implicit_function()
        self._wrap_call(self._vtk_obj.SetImplicitFunction,
                        deref_vtk(arg))
        self.trait_property_changed('implicit_function', old_val, arg)
    implicit_function = traits.Property(_get_implicit_function, _set_implicit_function, help=\
        """
        Specify the implicit function to use to generate data.
        """
    )

    scalar_array_name = traits.String('Implicit scalars', enter_set=True, auto_set=False, help=\
        """
        Set/get the scalar array name for this data set. The initial
        value is "Implicit scalars".
        """
    )

    def _scalar_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarArrayName,
                        self.scalar_array_name)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    _updateable_traits_ = \
    (('compute_gradients', 'GetComputeGradients'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('gradient_array_name',
    'GetGradientArrayName'), ('scalar_array_name', 'GetScalarArrayName'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_gradients', 'debug',
    'global_warning_display', 'release_data_flag', 'gradient_array_name',
    'progress_text', 'scalar_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SampleImplicitFunctionFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SampleImplicitFunctionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_gradients'], [], ['gradient_array_name',
            'scalar_array_name']),
            title='Edit SampleImplicitFunctionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SampleImplicitFunctionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


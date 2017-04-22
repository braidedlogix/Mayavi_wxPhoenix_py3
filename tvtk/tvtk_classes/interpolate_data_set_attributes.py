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


class InterpolateDataSetAttributes(DataSetAlgorithm):
    """
    InterpolateDataSetAttributes - interpolate scalars, vectors, etc.
    
    Superclass: DataSetAlgorithm
    
    and other dataset attributes
    
    InterpolateDataSetAttributes is a filter that interpolates data
    set attribute values between input data sets. The input to the filter
    must be datasets of the same type, same number of cells, and same
    number of points. The output of the filter is a data set of the same
    type as the input dataset and whose attribute values have been
    interpolated at the parametric value specified.
    
    The filter is used by specifying two or more input data sets (total
    of N), and a parametric value t (0 <= t <= N-1). The output will
    contain interpolated data set attributes common to all input data
    sets. (For example, if one input has scalars and vectors, and another
    has just scalars, then only scalars will be interpolated and output.)
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInterpolateDataSetAttributes, obj, update, **traits)
    
    t = traits.Trait(0.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Specify interpolation parameter t.
        """
    )

    def _t_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetT,
                        self.t)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def _get_input_list(self):
        return wrap_vtk(self._vtk_obj.GetInputList())
    input_list = traits.Property(_get_input_list, help=\
        """
        Return the list of inputs to this filter.
        """
    )

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('t', 'GetT'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 't'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InterpolateDataSetAttributes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InterpolateDataSetAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['t']),
            title='Edit InterpolateDataSetAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InterpolateDataSetAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


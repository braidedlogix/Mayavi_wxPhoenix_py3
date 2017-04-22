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

from tvtk.tvtk_classes.algorithm import Algorithm


class ResampleToImage(Algorithm):
    """
    ResampleToImage - sample dataset on a uniform grid
    
    Superclass: Algorithm
    
    PResampleToImage is a filter that resamples the input dataset on a
    uniform grid. It internally uses ProbeFilter to do the probing.
    @sa
    ProbeFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkResampleToImage, obj, update, **traits)
    
    use_input_bounds = tvtk_base.true_bool_trait(help=\
        """
        Set/Get if the filter should use Input bounds to sub-sample the
        data. By default it is set to 1.
        """
    )

    def _use_input_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseInputBounds,
                        self.use_input_bounds_)

    sampling_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(0.0, 1.0, 0.0, 1.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _sampling_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSamplingBounds,
                        self.sampling_bounds)

    sampling_dimensions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(10, 10, 10), cols=3, help=\
        """
        
        """
    )

    def _sampling_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSamplingDimensions,
                        self.sampling_dimensions)

    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    output = traits.Property(_get_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self):
        """
        V.get_output() -> ImageData
        C++: ImageData *GetOutput()
        Get the output data for this algorithm.
        """
        return wrap_vtk(self._vtk_obj.GetOutput())

    _updateable_traits_ = \
    (('use_input_bounds', 'GetUseInputBounds'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('sampling_bounds', 'GetSamplingBounds'),
    ('sampling_dimensions', 'GetSamplingDimensions'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'use_input_bounds', 'progress_text',
    'sampling_bounds', 'sampling_dimensions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ResampleToImage, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ResampleToImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_input_bounds'], [], ['sampling_bounds',
            'sampling_dimensions']),
            title='Edit ResampleToImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ResampleToImage properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


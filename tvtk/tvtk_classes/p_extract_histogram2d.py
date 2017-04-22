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

from tvtk.tvtk_classes.extract_histogram2d import ExtractHistogram2D


class PExtractHistogram2D(ExtractHistogram2D):
    """
    PExtractHistogram2D - compute a 2d histogram between two columns
     of an input Table in parallel.
    
    Superclass: ExtractHistogram2D
    
    This class does exactly the same this as ExtractHistogram2D,
     but does it in a multi-process environment.  After each node
     computes their own local histograms, this class does an all_reduce
     that distributes the sum of all local histograms onto each node.
    
    @sa
     ExtractHistogram2D
    
    @par Thanks:
     Developed by David Feng and Philippe Pebay at Sandia National
    Laboratories
    ----------------------------------------------------------------------
        --------
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPExtractHistogram2D, obj, update, **traits)
    
    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('swap_columns', 'GetSwapColumns'), ('use_custom_histogram_extents',
    'GetUseCustomHistogramExtents'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('scalar_type',
    'GetScalarType'), ('components_to_process', 'GetComponentsToProcess'),
    ('custom_histogram_extents', 'GetCustomHistogramExtents'),
    ('number_of_bins', 'GetNumberOfBins'), ('assess_option',
    'GetAssessOption'), ('derive_option', 'GetDeriveOption'),
    ('learn_option', 'GetLearnOption'), ('number_of_primary_tables',
    'GetNumberOfPrimaryTables'), ('test_option', 'GetTestOption'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'swap_columns', 'use_custom_histogram_extents',
    'scalar_type', 'assess_option', 'components_to_process',
    'custom_histogram_extents', 'derive_option', 'learn_option',
    'number_of_bins', 'number_of_primary_tables', 'progress_text',
    'test_option'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PExtractHistogram2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PExtractHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['swap_columns', 'use_custom_histogram_extents'],
            ['scalar_type'], ['assess_option', 'components_to_process',
            'custom_histogram_extents', 'derive_option', 'learn_option',
            'number_of_bins', 'number_of_primary_tables', 'test_option']),
            title='Edit PExtractHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PExtractHistogram2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


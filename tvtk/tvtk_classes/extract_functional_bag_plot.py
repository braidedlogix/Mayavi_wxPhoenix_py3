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

from tvtk.tvtk_classes.table_algorithm import TableAlgorithm


class ExtractFunctionalBagPlot(TableAlgorithm):
    """
    ExtractFunctionalBagPlot - From an input table containing series
    on port 0 and another table describing densities on port 1 (for
    instance obtained by applying filter 
    HighestDensityRegionsStatistics, this filter generates a table
    containing all t
    
    Superclass: TableAlgorithm
    
    he columns of the input port 0 plus two 2 components columns
    containing the bag series to be used by FunctionalBagPlot.
    
    @sa
    FunctionalBagPlot HighestDensityRegionsStatistics
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractFunctionalBagPlot, obj, update, **traits)
    
    def set_density_for_p50(self, *args):
        """
        V.set_density_for_p50(float)
        C++: void SetDensityForP50(double a)"""
        ret = self._wrap_call(self._vtk_obj.SetDensityForP50, *args)
        return ret

    def set_density_for_p_user(self, *args):
        """
        V.set_density_for_p_user(float)
        C++: void SetDensityForPUser(double a)
        Density value for the user defined quartile.
        """
        ret = self._wrap_call(self._vtk_obj.SetDensityForPUser, *args)
        return ret

    def set_p_user(self, *args):
        """
        V.set_p_user(int)
        C++: void SetPUser(int a)
        Density value for the user defined quartile.
        """
        ret = self._wrap_call(self._vtk_obj.SetPUser, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractFunctionalBagPlot, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractFunctionalBagPlot properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ExtractFunctionalBagPlot properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractFunctionalBagPlot properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


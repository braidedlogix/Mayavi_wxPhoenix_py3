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

from tvtk.tvtk_classes.plot3d import Plot3D


class PlotSurface(Plot3D):
    """
    PlotSurface - 3d surface plot.
    
    Superclass: Plot3D
    
    3d surface plot.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlotSurface, obj, update, **traits)
    
    def set_x_range(self, *args):
        """
        V.set_x_range(float, float)
        C++: void SetXRange(float min, float max)
        Set the range of the input data for the X dimension.  By default
        it is (1, number_of_columns).  Calling this method after
        set_input_data() results in recomputation of the plot's data. 
        Therefore, it is more efficient to call it before set_input_data()
        when possible.
        """
        ret = self._wrap_call(self._vtk_obj.SetXRange, *args)
        return ret

    def set_y_range(self, *args):
        """
        V.set_y_range(float, float)
        C++: void SetYRange(float min, float max)
        Set the range of the input data for the Y dimension.  By default
        it is (1, number_of_rows).  Calling this method after
        set_input_data() results in recomputation of the plot's data. 
        Therefore, it is more efficient to call it before set_input_data()
        when possible.
        """
        ret = self._wrap_call(self._vtk_obj.SetYRange, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('opacity', 'GetOpacity'), ('interactive',
    'GetInteractive'), ('visible', 'GetVisible'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'interactive', 'opacity',
    'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlotSurface, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PlotSurface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['interactive', 'opacity', 'visible']),
            title='Edit PlotSurface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlotSurface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


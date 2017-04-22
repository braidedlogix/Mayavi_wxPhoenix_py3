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

from tvtk.tvtk_classes.context_item import ContextItem


class ChartXYZ(ContextItem):
    """
    ChartXYZ - Factory class for drawing 3d XYZ charts.
    
    Superclass: ContextItem
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkChartXYZ, obj, update, **traits)
    
    def get_axis(self, *args):
        """
        V.get_axis(int) -> Axis
        C++: Axis *GetAxis(int axis)
        Get the x (0), y (1) or z (2) axis.
        """
        ret = self._wrap_call(self._vtk_obj.GetAxis, *args)
        return wrap_vtk(ret)

    def add_plot(self, *args):
        """
        V.add_plot(Plot3D) -> int
        C++: virtual IdType AddPlot(Plot3D *plot)
        Adds a plot to the chart.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddPlot, *my_args)
        return ret

    def clear_plots(self):
        """
        V.clear_plots()
        C++: void ClearPlots()
        Remove all the plots from this chart.
        """
        ret = self._vtk_obj.ClearPlots()
        return ret
        

    def recalculate_bounds(self):
        """
        V.recalculate_bounds()
        C++: void RecalculateBounds()
        Determine the XYZ bounds of the plots within this chart. This
        information is then used to set the range of the axes.
        """
        ret = self._vtk_obj.RecalculateBounds()
        return ret
        

    def recalculate_transform(self):
        """
        V.recalculate_transform()
        C++: void RecalculateTransform()
        Use this chart's Geometry to set the endpoints of its axes. This
        method also sets up a transformation that is used to properly
        render the data within the chart.
        """
        ret = self._vtk_obj.RecalculateTransform()
        return ret
        

    def set_angle(self, *args):
        """
        V.set_angle(float)
        C++: void SetAngle(double angle)
        Set the rotation angle for the chart (_auto_rotate mode only).
        """
        ret = self._wrap_call(self._vtk_obj.SetAngle, *args)
        return ret

    def set_annotation_link(self, *args):
        """
        V.set_annotation_link(AnnotationLink)
        C++: virtual void SetAnnotationLink(AnnotationLink *link)
        Set the AnnotationLink for the chart.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetAnnotationLink, *my_args)
        return ret

    def set_around_x(self, *args):
        """
        V.set_around_x(bool)
        C++: void SetAroundX(bool isX)
        Set whether or not we're rotating about the X axis.
        """
        ret = self._wrap_call(self._vtk_obj.SetAroundX, *args)
        return ret

    def set_auto_rotate(self, *args):
        """
        V.set_auto_rotate(bool)
        C++: void SetAutoRotate(bool b)
        Set whether or not we're using this chart to rotate on a timer.
        Default value is false.
        """
        ret = self._wrap_call(self._vtk_obj.SetAutoRotate, *args)
        return ret

    def set_decorate_axes(self, *args):
        """
        V.set_decorate_axes(bool)
        C++: void SetDecorateAxes(bool b)
        Set whether or not axes labels & tick marks should be drawn.
        Default value is true.
        """
        ret = self._wrap_call(self._vtk_obj.SetDecorateAxes, *args)
        return ret

    def set_fit_to_scene(self, *args):
        """
        V.set_fit_to_scene(bool)
        C++: void SetFitToScene(bool b)
        Set whether or not the chart should automatically resize itself
        to fill the scene.  Default value is true.
        """
        ret = self._wrap_call(self._vtk_obj.SetFitToScene, *args)
        return ret

    def set_geometry(self, *args):
        """
        V.set_geometry(Rectf)
        C++: void SetGeometry(const Rectf &bounds)
        Set the geometry in pixel coordinates (origin and width/height).
        This method also sets up the end points of the axes of the chart.
        For this reason, if you call set_around_x(), you should call
        set_geometry() afterwards.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGeometry, *my_args)
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
            return super(ChartXYZ, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ChartXYZ properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['interactive', 'opacity', 'visible']),
            title='Edit ChartXYZ properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ChartXYZ properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


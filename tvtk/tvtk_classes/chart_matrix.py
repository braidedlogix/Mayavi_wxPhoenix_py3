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

from tvtk.tvtk_classes.abstract_context_item import AbstractContextItem


class ChartMatrix(AbstractContextItem):
    """
    ChartMatrix - container for a matrix of charts.
    
    Superclass: AbstractContextItem
    
    This class contains a matrix of charts. These charts will be of type
    ChartXY by default, but this can be overridden. The class will
    manage their layout and object lifetime.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkChartMatrix, obj, update, **traits)
    
    def get_borders(self, *args):
        """
        V.get_borders([int, int, int, int])
        C++: virtual void GetBorders(int borders[4])
        Set/get the borders of the chart matrix (space in pixels around
        each chart).
        """
        ret = self._wrap_call(self._vtk_obj.GetBorders, *args)
        return ret

    def set_borders(self, *args):
        """
        V.set_borders(int, int, int, int)
        C++: virtual void SetBorders(int left, int bottom, int right,
            int top)
        Set/get the borders of the chart matrix (space in pixels around
        each chart).
        """
        ret = self._wrap_call(self._vtk_obj.SetBorders, *args)
        return ret

    def get_chart(self, *args):
        """
        V.get_chart(Vector2i) -> Chart
        C++: virtual Chart *GetChart(const Vector2i &position)
        Get the specified chart element, if the element does not exist
        NULL will be returned. If the chart element has not yet been
        allocated it will be at this point.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetChart, *my_args)
        return wrap_vtk(ret)

    def set_chart(self, *args):
        """
        V.set_chart(Vector2i, Chart) -> bool
        C++: virtual bool SetChart(const Vector2i &position,
            Chart *chart)
        Set the chart element, note that the chart matrix must be large
        enough to accommodate the element being set. Note that this class
        will take ownership of the chart object.
        \return false if the element cannot be set.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetChart, *my_args)
        return ret

    def get_chart_span(self, *args):
        """
        V.get_chart_span(Vector2i) -> Vector2i
        C++: virtual Vector2i GetChartSpan(const Vector2i &position)
        Get the span of the specified chart.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetChartSpan, *my_args)
        return wrap_vtk(ret)

    def set_chart_span(self, *args):
        """
        V.set_chart_span(Vector2i, Vector2i) -> bool
        C++: virtual bool SetChartSpan(const Vector2i &position,
            const Vector2i &span)
        Set the span of a chart in the matrix. This defaults to 1x1, and
        cannot exceed the remaining space in x or y.
        \return false If the span is not possible.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetChartSpan, *my_args)
        return ret

    def get_chart_index(self, *args):
        """
        V.get_chart_index(Vector2f) -> Vector2i
        C++: virtual Vector2i GetChartIndex(
            const Vector2f &position)
        Get the position of the chart in the matrix at the specified
        location. The position should be specified in scene coordinates.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetChartIndex, *my_args)
        return wrap_vtk(ret)

    def allocate(self):
        """
        V.allocate()
        C++: virtual void Allocate()
        Allocate the charts, this will cause any null chart to be
        allocated.
        """
        ret = self._vtk_obj.Allocate()
        return ret
        

    def clear_specific_resizes(self):
        """
        V.clear_specific_resizes()
        C++: virtual void ClearSpecificResizes()
        Set a specific resize that will move the bottom left point of a
        chart.
        """
        ret = self._vtk_obj.ClearSpecificResizes()
        return ret
        

    def set_border_bottom(self, *args):
        """
        V.set_border_bottom(int)
        C++: void SetBorderBottom(int value)
        Set/get the borders of the chart matrix (space in pixels around
        each chart).
        """
        ret = self._wrap_call(self._vtk_obj.SetBorderBottom, *args)
        return ret

    def set_border_left(self, *args):
        """
        V.set_border_left(int)
        C++: void SetBorderLeft(int value)
        Set/get the borders of the chart matrix (space in pixels around
        each chart).
        """
        ret = self._wrap_call(self._vtk_obj.SetBorderLeft, *args)
        return ret

    def set_border_right(self, *args):
        """
        V.set_border_right(int)
        C++: void SetBorderRight(int value)
        Set/get the borders of the chart matrix (space in pixels around
        each chart).
        """
        ret = self._wrap_call(self._vtk_obj.SetBorderRight, *args)
        return ret

    def set_border_top(self, *args):
        """
        V.set_border_top(int)
        C++: void SetBorderTop(int value)
        Set/get the borders of the chart matrix (space in pixels around
        each chart).
        """
        ret = self._wrap_call(self._vtk_obj.SetBorderTop, *args)
        return ret

    def set_gutter_x(self, *args):
        """
        V.set_gutter_x(float)
        C++: void SetGutterX(float value)
        Set the gutter that should be left between the charts in the
        matrix.
        """
        ret = self._wrap_call(self._vtk_obj.SetGutterX, *args)
        return ret

    def set_gutter_y(self, *args):
        """
        V.set_gutter_y(float)
        C++: void SetGutterY(float value)
        Set the gutter that should be left between the charts in the
        matrix.
        """
        ret = self._wrap_call(self._vtk_obj.SetGutterY, *args)
        return ret

    def set_specific_resize(self, *args):
        """
        V.set_specific_resize(Vector2i, Vector2f)
        C++: virtual void SetSpecificResize(const Vector2i &index,
            const Vector2f &resize)
        Set a specific resize that will move the bottom left point of a
        chart.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSpecificResize, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interactive', 'GetInteractive'),
    ('visible', 'GetVisible'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'interactive', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ChartMatrix, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ChartMatrix properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['interactive', 'visible']),
            title='Edit ChartMatrix properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ChartMatrix properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


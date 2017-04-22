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

from tvtk.tvtk_classes.chart import Chart


class ChartPie(Chart):
    """
    ChartPie - Factory class for drawing pie charts
    
    Superclass: Chart
    
    This class implements an pie chart.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkChartPie, obj, update, **traits)
    
    def _get_scene(self):
        return wrap_vtk(self._vtk_obj.GetScene())
    def _set_scene(self, arg):
        old_val = self._get_scene()
        self._wrap_call(self._vtk_obj.SetScene,
                        deref_vtk(arg))
        self.trait_property_changed('scene', old_val, arg)
    scene = traits.Property(_get_scene, _set_scene, help=\
        """
        Get the ContextScene for the item, always set for an item in a
        scene.
        """
    )

    show_legend = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Set whether the chart should draw a legend.
        """
    )

    def _show_legend_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowLegend,
                        self.show_legend)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('show_legend', 'GetShowLegend'),
    ('auto_size', 'GetAutoSize'), ('geometry', 'GetGeometry'),
    ('layout_strategy', 'GetLayoutStrategy'), ('point1', 'GetPoint1'),
    ('point2', 'GetPoint2'), ('render_empty', 'GetRenderEmpty'),
    ('selection_method', 'GetSelectionMethod'), ('selection_mode',
    'GetSelectionMode'), ('title', 'GetTitle'), ('opacity', 'GetOpacity'),
    ('interactive', 'GetInteractive'), ('visible', 'GetVisible'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'auto_size', 'geometry',
    'interactive', 'layout_strategy', 'opacity', 'point1', 'point2',
    'render_empty', 'selection_method', 'selection_mode', 'show_legend',
    'title', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ChartPie, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ChartPie properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['auto_size', 'geometry', 'interactive',
            'layout_strategy', 'opacity', 'point1', 'point2', 'render_empty',
            'selection_method', 'selection_mode', 'show_legend', 'title',
            'visible']),
            title='Edit ChartPie properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ChartPie properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


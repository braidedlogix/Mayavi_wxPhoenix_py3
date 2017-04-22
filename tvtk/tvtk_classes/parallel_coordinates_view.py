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

from tvtk.tvtk_classes.render_view import RenderView


class ParallelCoordinatesView(RenderView):
    """
    ParallelCoordinatesView - view to be used with
    ParallelCoordinatesRepresentation
    
    Superclass: RenderView
    
    This class manages interaction with the
    ParallelCoordinatesRepresentation.  There are two inspection
    modes: axis manipulation and line selection.  In axis manipulation
    mode, PC axes can be dragged and reordered with the LMB, axis ranges
    can be increased/decreased by dragging up/down with the LMB, and RMB
    controls zoom and pan.
    
    In line selection mode, there are three subclasses of selections:
    lasso, angle, and function selection.  Lasso selection lets the user
    brush a line and select all PC lines that pass nearby.  Angle
    selection lets the user draw a representative line between axes and
    select all lines that have similar orientation.  Function selection
    lets the user draw two  representative lines between a pair of axes
    and select all lines that match the linear interpolation of those
    lines.
    
    There are several self-explanatory operators for combining
    selections: ADD, SUBTRACT REPLACE, and INTERSECT.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParallelCoordinatesView, obj, update, **traits)
    
    brush_mode = traits.Trait('lasso',
    tvtk_base.TraitRevPrefixMap({'lasso': 0, 'angle': 1, 'axis_threshold': 3, 'function': 2}), help=\
        """
        
        """
    )

    def _brush_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBrushMode,
                        self.brush_mode_)

    brush_operator = traits.Trait('add',
    tvtk_base.TraitRevPrefixMap({'add': 0, 'intersect': 2, 'replace': 3, 'subtract': 1}), help=\
        """
        
        """
    )

    def _brush_operator_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBrushOperator,
                        self.brush_operator_)

    inspect_mode = traits.Trait('manipulate_axes',
    tvtk_base.TraitRevPrefixMap({'manipulate_axes': 0}), help=\
        """
        
        """
    )

    def _inspect_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInspectMode,
                        self.inspect_mode_)

    current_brush_class = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _current_brush_class_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCurrentBrushClass,
                        self.current_brush_class)

    maximum_number_of_brush_points = traits.Int(100, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _maximum_number_of_brush_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfBrushPoints,
                        self.maximum_number_of_brush_points)

    def set_inpsect_mode_to_select_data(self):
        """
        V.set_inpsect_mode_to_select_data()
        C++: void SetInpsectModeToSelectData()"""
        ret = self._vtk_obj.SetInpsectModeToSelectData()
        return ret
        

    _updateable_traits_ = \
    (('display_hover_text', 'GetDisplayHoverText'),
    ('render_on_mouse_move', 'GetRenderOnMouseMove'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('brush_mode', 'GetBrushMode'), ('brush_operator',
    'GetBrushOperator'), ('inspect_mode', 'GetInspectMode'),
    ('label_placement_mode', 'GetLabelPlacementMode'),
    ('label_render_mode', 'GetLabelRenderMode'), ('selection_mode',
    'GetSelectionMode'), ('current_brush_class', 'GetCurrentBrushClass'),
    ('maximum_number_of_brush_points', 'GetMaximumNumberOfBrushPoints'),
    ('icon_size', 'GetIconSize'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'display_hover_text', 'global_warning_display',
    'render_on_mouse_move', 'brush_mode', 'brush_operator',
    'inspect_mode', 'label_placement_mode', 'label_render_mode',
    'selection_mode', 'current_brush_class', 'icon_size',
    'maximum_number_of_brush_points'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParallelCoordinatesView, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ParallelCoordinatesView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['display_hover_text', 'render_on_mouse_move'], ['brush_mode',
            'brush_operator', 'inspect_mode', 'label_placement_mode',
            'label_render_mode', 'selection_mode'], ['current_brush_class',
            'icon_size', 'maximum_number_of_brush_points']),
            title='Edit ParallelCoordinatesView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParallelCoordinatesView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


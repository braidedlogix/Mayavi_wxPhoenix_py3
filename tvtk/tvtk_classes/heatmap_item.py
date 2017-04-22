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


class HeatmapItem(ContextItem):
    """
    HeatmapItem - A 2d graphics item for rendering a heatmap
    
    Superclass: ContextItem
    
    This item draws a heatmap as a part of a ContextScene.
    
    .SEE ALSO Table
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHeatmapItem, obj, update, **traits)
    
    cell_height = traits.Float(18.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the height of the cells in our heatmap. Default is 18
        pixels.
        """
    )

    def _cell_height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellHeight,
                        self.cell_height)

    cell_width = traits.Float(36.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the width of the cells in our heatmap. Default is 36
        pixels.
        """
    )

    def _cell_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellWidth,
                        self.cell_width)

    name_column = traits.String('name', enter_set=True, auto_set=False, help=\
        """
        Get/Set the name of the column that specifies the name of this
        table's rows.  By default, we assume this column will be named
        "name".  If no such column can be found, we then assume that the
        1st column in the table names the rows.
        """
    )

    def _name_column_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNameColumn,
                        self.name_column)

    orientation = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set which way the table should face within the visualization.
        """
    )

    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation)

    position = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 0.0), cols=2, help=\
        """
        
        """
    )

    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    def _get_table(self):
        return wrap_vtk(self._vtk_obj.GetTable())
    def _set_table(self, arg):
        old_val = self._get_table()
        self._wrap_call(self._vtk_obj.SetTable,
                        deref_vtk(arg))
        self.trait_property_changed('table', old_val, arg)
    table = traits.Property(_get_table, _set_table, help=\
        """
        Get the table that this item draws.
        """
    )

    def get_bounds(self, *args):
        """
        V.get_bounds([float, float, float, float])
        C++: virtual void GetBounds(double bounds[4])
        Get the bounds for this item as (Xmin,Xmax,Ymin,Ymax).
        """
        ret = self._wrap_call(self._vtk_obj.GetBounds, *args)
        return ret

    def _get_column_label_width(self):
        return self._vtk_obj.GetColumnLabelWidth()
    column_label_width = traits.Property(_get_column_label_width, help=\
        """
        Get the width of the largest row or column label drawn by this
        heatmap.
        """
    )

    def _get_position_vector(self):
        return wrap_vtk(self._vtk_obj.GetPositionVector())
    position_vector = traits.Property(_get_position_vector, help=\
        """
        Get position of the heatmap.
        """
    )

    def _get_row_label_width(self):
        return self._vtk_obj.GetRowLabelWidth()
    row_label_width = traits.Property(_get_row_label_width, help=\
        """
        Get the width of the largest row or column label drawn by this
        heatmap.
        """
    )

    def _get_row_names(self):
        return wrap_vtk(self._vtk_obj.GetRowNames())
    row_names = traits.Property(_get_row_names, help=\
        """
        Get the table that this item draws.
        """
    )

    def get_text_angle_for_orientation(self, *args):
        """
        V.get_text_angle_for_orientation(int) -> float
        C++: double GetTextAngleForOrientation(int orientation)
        Get the angle that row labels should be rotated for the
        correponding heatmap orientation.  For the default orientation
        (LEFT_TO_RIGHT), this is 0 degrees.
        """
        ret = self._wrap_call(self._vtk_obj.GetTextAngleForOrientation, *args)
        return ret

    def mark_row_as_blank(self, *args):
        """
        V.mark_row_as_blank(string)
        C++: void MarkRowAsBlank(std::string rowName)
        Mark a row as blank, meaning that no cells will be drawn for it.
        Used by TreeHeatmapItem to represent missing data.
        """
        ret = self._wrap_call(self._vtk_obj.MarkRowAsBlank, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('cell_height', 'GetCellHeight'),
    ('cell_width', 'GetCellWidth'), ('name_column', 'GetNameColumn'),
    ('orientation', 'GetOrientation'), ('position', 'GetPosition'),
    ('opacity', 'GetOpacity'), ('interactive', 'GetInteractive'),
    ('visible', 'GetVisible'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'cell_height', 'cell_width',
    'interactive', 'name_column', 'opacity', 'orientation', 'position',
    'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HeatmapItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HeatmapItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['cell_height', 'cell_width', 'interactive',
            'name_column', 'opacity', 'orientation', 'position', 'visible']),
            title='Edit HeatmapItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HeatmapItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


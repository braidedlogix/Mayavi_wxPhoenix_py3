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


class TreeHeatmapItem(ContextItem):
    """
    TreeHeatmapItem - A 2d graphics item for rendering a tree and an
    associated heatmap.
    
    Superclass: ContextItem
    
    This item draws a tree and a heatmap as a part of a ContextScene.
    The input tree's vertex data must contain at least two arrays. The
    first required array is a StringArray called "node name". This
    array corresponds to the first column of the input table. The second
    required array is a scalar array called "node weight". This array is
    used by TreeLayoutStrategy to set any particular node's distance
    from the root of the tree.
    
    The NewickTreeReader automatically initializes both of these
    required arrays in its output tree.
    
    .SEE ALSO DendrogramItem HeatmapItem Tree Table
    NewickTreeReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeHeatmapItem, obj, update, **traits)
    
    def _get_column_tree(self):
        return wrap_vtk(self._vtk_obj.GetColumnTree())
    def _set_column_tree(self, arg):
        old_val = self._get_column_tree()
        self._wrap_call(self._vtk_obj.SetColumnTree,
                        deref_vtk(arg))
        self.trait_property_changed('column_tree', old_val, arg)
    column_tree = traits.Property(_get_column_tree, _set_column_tree, help=\
        """
        Get the tree that represents the columns of the heatmap (if one
        has been set).
        """
    )

    def _get_dendrogram(self):
        return wrap_vtk(self._vtk_obj.GetDendrogram())
    def _set_dendrogram(self, arg):
        old_val = self._get_dendrogram()
        self._wrap_call(self._vtk_obj.SetDendrogram,
                        deref_vtk(arg))
        self.trait_property_changed('dendrogram', old_val, arg)
    dendrogram = traits.Property(_get_dendrogram, _set_dendrogram, help=\
        """
        Get/Set the dendrogram contained by this item.
        """
    )

    def _get_heatmap(self):
        return wrap_vtk(self._vtk_obj.GetHeatmap())
    def _set_heatmap(self, arg):
        old_val = self._get_heatmap()
        self._wrap_call(self._vtk_obj.SetHeatmap,
                        deref_vtk(arg))
        self.trait_property_changed('heatmap', old_val, arg)
    heatmap = traits.Property(_get_heatmap, _set_heatmap, help=\
        """
        Get/Set the heatmap contained by this item.
        """
    )

    orientation = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set which way the tree / heatmap should face within the
        visualization. The default is for both components to be drawn
        left to right.
        """
    )

    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation)

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

    def _get_tree(self):
        return wrap_vtk(self._vtk_obj.GetTree())
    def _set_tree(self, arg):
        old_val = self._get_tree()
        self._wrap_call(self._vtk_obj.SetTree,
                        deref_vtk(arg))
        self.trait_property_changed('tree', old_val, arg)
    tree = traits.Property(_get_tree, _set_tree, help=\
        """
        Get the tree that this item draws.
        """
    )

    tree_line_width = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set how wide the edges of the trees should be.  Default is
        one pixel.
        """
    )

    def _tree_line_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTreeLineWidth,
                        self.tree_line_width)

    def get_bounds(self, *args):
        """
        V.get_bounds([float, float, float, float])
        C++: void GetBounds(double bounds[4])
        Get the bounds of this item (x_min, x_max, y_min, Max) in pixel
        coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetBounds, *args)
        return ret

    def get_center(self, *args):
        """
        V.get_center([float, float])
        C++: void GetCenter(double center[2])
        Get the center point of this item in pixel coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetCenter, *args)
        return ret

    def _get_pruned_tree(self):
        return wrap_vtk(self._vtk_obj.GetPrunedTree())
    pruned_tree = traits.Property(_get_pruned_tree, help=\
        """
        Deprecated.  Use this->_get_dendrogram()->_get_pruned_tree() instead.
        """
    )

    def get_size(self, *args):
        """
        V.get_size([float, float])
        C++: void GetSize(double size[2])
        Get the size of this item in pixel coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.GetSize, *args)
        return ret

    def collapse_to_number_of_leaf_nodes(self, *args):
        """
        V.collapse_to_number_of_leaf_nodes(int)
        C++: void CollapseToNumberOfLeafNodes(unsigned int n)
        Collapse subtrees until there are only n leaf nodes left in the
        tree. The leaf nodes that remain are those that are closest to
        the root. Any subtrees that were collapsed prior to this function
        being called may be re-expanded.  Use this function instead of
        this->_get_dendrogram->_collapse_to_number_of_leaf_nodes(), as this
        function also handles the hiding of heatmap rows that correspond
        to newly collapsed subtrees.
        """
        ret = self._wrap_call(self._vtk_obj.CollapseToNumberOfLeafNodes, *args)
        return ret

    def reorder_table(self):
        """
        V.reorder_table()
        C++: void ReorderTable()
        Reorder the rows in the table so they match the order of the leaf
        nodes in our tree.
        """
        ret = self._vtk_obj.ReorderTable()
        return ret
        

    def reverse_table_columns(self):
        """
        V.reverse_table_columns()
        C++: void ReverseTableColumns()
        Reverse the order of the rows in our input table.  This is used
        to simplify the table layout for DOWN_TO_UP and UP_TO_DOWN
        orientations.
        """
        ret = self._vtk_obj.ReverseTableColumns()
        return ret
        

    def reverse_table_rows(self):
        """
        V.reverse_table_rows()
        C++: void ReverseTableRows()
        Reverse the order of the rows in our input table.  This is used
        to simplify the table layout for DOWN_TO_UP and RIGHT_TO_LEFT
        orientations.
        """
        ret = self._vtk_obj.ReverseTableRows()
        return ret
        

    def set_tree_color_array(self, *args):
        """
        V.set_tree_color_array(string)
        C++: void SetTreeColorArray(const char *arrayName)
        Deprecated.  Use this->_get_dendrogram()->_set_color_array(const char
        *array_name) instead.
        """
        ret = self._wrap_call(self._vtk_obj.SetTreeColorArray, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('orientation', 'GetOrientation'),
    ('tree_line_width', 'GetTreeLineWidth'), ('opacity', 'GetOpacity'),
    ('interactive', 'GetInteractive'), ('visible', 'GetVisible'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'interactive', 'opacity',
    'orientation', 'tree_line_width', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeHeatmapItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeHeatmapItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['interactive', 'opacity', 'orientation',
            'tree_line_width', 'visible']),
            title='Edit TreeHeatmapItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeHeatmapItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


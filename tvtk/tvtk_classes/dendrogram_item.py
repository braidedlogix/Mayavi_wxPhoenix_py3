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


class DendrogramItem(ContextItem):
    """
    DendrogramItem - A 2d graphics item for rendering a tree as a
    dendrogram
    
    Superclass: ContextItem
    
    Draw a tree as a dendrogram The input tree's vertex data must contain
    at least two arrays. The first required array is a StringArray
    called "node name". This array is used to label the leaf nodes of the
    tree. The second required array is a scalar array called "node
    weight". This array is used by TreeLayoutStrategy to set any
    particular node's distance from the root of the tree.
    
    The NewickTreeReader automatically initializes both of these
    required arrays in its output tree.
    
    .SEE ALSO Tree NewickTreeReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDendrogramItem, obj, update, **traits)
    
    display_number_of_collapsed_leaf_nodes = tvtk_base.true_bool_trait(help=\
        """
        Get/set whether or not the number of collapsed leaf nodes should
        be written inside the triangle representing a collapsed subtree. 
        Default is true.
        """
    )

    def _display_number_of_collapsed_leaf_nodes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayNumberOfCollapsedLeafNodes,
                        self.display_number_of_collapsed_leaf_nodes_)

    draw_labels = tvtk_base.true_bool_trait(help=\
        """
        Get/Set whether or not leaf nodes should be labeled by this
        class. Default is true.
        """
    )

    def _draw_labels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawLabels,
                        self.draw_labels_)

    extend_leaf_nodes = tvtk_base.false_bool_trait(help=\
        """
        Get/set whether or not leaf nodes should be extended so that they
        all line up vertically.  The default is to NOT extend leaf nodes.
         When extending leaf nodes, the extra length is drawn in grey so
        as to distinguish it from the actual length of the leaf node.
        """
    )

    def _extend_leaf_nodes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtendLeafNodes,
                        self.extend_leaf_nodes_)

    distance_array_name = traits.String('node weight', enter_set=True, auto_set=False, help=\
        """
        Get/Set the name of the array that specifies the distance of each
        vertex from the root (NOT the vertex's parent).  This array
        should be a part of the input tree's vertex_data.  By default,
        this value is "node weight", which is the name of the array
        created by NewickTreeReader.
        """
    )

    def _distance_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistanceArrayName,
                        self.distance_array_name)

    leaf_spacing = traits.Float(18.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the spacing between the leaf nodes in our dendrogram.
        Default is 18 pixels.
        """
    )

    def _leaf_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLeafSpacing,
                        self.leaf_spacing)

    line_width = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set how wide the edges of this dendrogram should be.  Default
        is one pixel.
        """
    )

    def _line_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineWidth,
                        self.line_width)

    orientation = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set which way the tree should face within the visualization.  The
        default is for the tree to be drawn left to right.
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

    vertex_name_array_name = traits.String('node name', enter_set=True, auto_set=False, help=\
        """
        Get/Set the name of a StringArray that specifies the names of
        the vertices of the input tree.  This array should be a part of
        the input tree's vertex_data.  By default, this value is "node
        name", which is the name of the array created by
        NewickTreeReader.
        """
    )

    def _vertex_name_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexNameArrayName,
                        self.vertex_name_array_name)

    def get_angle_for_orientation(self, *args):
        """
        V.get_angle_for_orientation(int) -> float
        C++: double GetAngleForOrientation(int orientation)
        Get the rotation angle (in degrees) that corresponds to the given
        tree orientation.  For the default orientation (LEFT_TO_RIGHT),
        this is 90 degrees.
        """
        ret = self._wrap_call(self._vtk_obj.GetAngleForOrientation, *args)
        return ret

    def get_bounds(self, *args):
        """
        V.get_bounds([float, float, float, float])
        C++: virtual void GetBounds(double bounds[4])
        Get the bounds for this item as (Xmin,Xmax,Ymin,Ymax). These
        bounds are only guaranteed to be accurate after Paint() or
        prepare_to_paint() has been called.
        """
        ret = self._wrap_call(self._vtk_obj.GetBounds, *args)
        return ret

    def _get_label_width(self):
        return self._vtk_obj.GetLabelWidth()
    label_width = traits.Property(_get_label_width, help=\
        """
        Get the width of the longest leaf node label.
        """
    )

    def get_position_of_vertex(self, *args):
        """
        V.get_position_of_vertex(string, [float, float]) -> bool
        C++: bool GetPositionOfVertex(std::string vertexName,
            double position[2])
        Find the position of the vertex with the specified name.  Store
        this information in the passed array.  Returns true if the vertex
        was found, false otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.GetPositionOfVertex, *args)
        return ret

    def _get_position_vector(self):
        return wrap_vtk(self._vtk_obj.GetPositionVector())
    position_vector = traits.Property(_get_position_vector, help=\
        """
        Get position of the dendrogram.
        """
    )

    def _get_pruned_tree(self):
        return wrap_vtk(self._vtk_obj.GetPrunedTree())
    pruned_tree = traits.Property(_get_pruned_tree, help=\
        """
        Get the collapsed tree
        """
    )

    def get_text_angle_for_orientation(self, *args):
        """
        V.get_text_angle_for_orientation(int) -> float
        C++: double GetTextAngleForOrientation(int orientation)
        Get the angle that vertex labels should be rotated for the
        correponding tree orientation.  For the default orientation
        (LEFT_TO_RIGHT), this is 0 degrees.
        """
        ret = self._wrap_call(self._vtk_obj.GetTextAngleForOrientation, *args)
        return ret

    def collapse_to_number_of_leaf_nodes(self, *args):
        """
        V.collapse_to_number_of_leaf_nodes(int)
        C++: void CollapseToNumberOfLeafNodes(unsigned int n)
        Collapse subtrees until there are only n leaf nodes left in the
        tree. The leaf nodes that remain are those that are closest to
        the root. Any subtrees that were collapsed prior to this function
        being called may be re-expanded.
        """
        ret = self._wrap_call(self._vtk_obj.CollapseToNumberOfLeafNodes, *args)
        return ret

    def compute_label_width(self, *args):
        """
        V.compute_label_width(Context2D)
        C++: void ComputeLabelWidth(Context2D *painter)
        Compute the width of the longest leaf node label.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeLabelWidth, *my_args)
        return ret

    def prepare_to_paint(self, *args):
        """
        V.prepare_to_paint(Context2D)
        C++: void PrepareToPaint(Context2D *painter)
        This function calls rebuild_buffers() if necessary. Once
        prepare_to_paint() has been called, get_bounds() is guaranteed to
        provide useful information.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PrepareToPaint, *my_args)
        return ret

    def set_color_array(self, *args):
        """
        V.set_color_array(string)
        C++: void SetColorArray(const char *arrayName)
        Indicate which array within the Tree's vertex_data should be used
        to color the tree.  The specified array must be a DoubleArray.
        By default, the tree will be drawn in black.
        """
        ret = self._wrap_call(self._vtk_obj.SetColorArray, *args)
        return ret

    _updateable_traits_ = \
    (('display_number_of_collapsed_leaf_nodes',
    'GetDisplayNumberOfCollapsedLeafNodes'), ('draw_labels',
    'GetDrawLabels'), ('extend_leaf_nodes', 'GetExtendLeafNodes'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('distance_array_name',
    'GetDistanceArrayName'), ('leaf_spacing', 'GetLeafSpacing'),
    ('line_width', 'GetLineWidth'), ('orientation', 'GetOrientation'),
    ('position', 'GetPosition'), ('vertex_name_array_name',
    'GetVertexNameArrayName'), ('opacity', 'GetOpacity'), ('interactive',
    'GetInteractive'), ('visible', 'GetVisible'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'display_number_of_collapsed_leaf_nodes', 'draw_labels',
    'extend_leaf_nodes', 'global_warning_display', 'distance_array_name',
    'interactive', 'leaf_spacing', 'line_width', 'opacity', 'orientation',
    'position', 'vertex_name_array_name', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DendrogramItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DendrogramItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['display_number_of_collapsed_leaf_nodes', 'draw_labels',
            'extend_leaf_nodes'], [], ['distance_array_name', 'interactive',
            'leaf_spacing', 'line_width', 'opacity', 'orientation', 'position',
            'vertex_name_array_name', 'visible']),
            title='Edit DendrogramItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DendrogramItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


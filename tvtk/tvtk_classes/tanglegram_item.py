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


class TanglegramItem(ContextItem):
    """
    TanglegramItem - Display two related trees
    
    Superclass: ContextItem
    
    This item draws two trees with connections between their leaf nodes.
    Use set_table() to specify what leaf nodes correspond to one another
    between the two trees.  See the documentation for this function for
    more details on how this table should be formatted.
    
    .SEE ALSO Tree Table DendrogramItem NewickTreeReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTanglegramItem, obj, update, **traits)
    
    correspondence_line_width = traits.Float(2.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set how wide the correspondence lines should be.  Default is
        two pixels.
        """
    )

    def _correspondence_line_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCorrespondenceLineWidth,
                        self.correspondence_line_width)

    label_size_difference = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        Get/Set how much larger the dendrogram labels should be compared
        to the vertex labels.  Because the vertex labels automatically
        resize based on zoom levels, this is a relative (not absolute)
        size.  Default value is 4 pts larger than the vertex labels.
        """
    )

    def _label_size_difference_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelSizeDifference,
                        self.label_size_difference)

    minimum_visible_font_size = traits.Int(8, enter_set=True, auto_set=False, help=\
        """
        Get/Set the smallest font size that is still considered legible.
        If the current zoom level requires our vertex labels to be
        smaller than this size the labels will not be drawn at all. 
        Default value is 8 pt.
        """
    )

    def _minimum_visible_font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumVisibleFontSize,
                        self.minimum_visible_font_size)

    orientation = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set which way the tanglegram should face within the
        visualization. The default is for tree #1 to be drawn left to
        right.
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
        Get/Set the table that describes the correspondences between the
        two trees.  The first column should contain the names of the leaf
        nodes from tree #1.  The columns of this table should be named
        after the leaf nodes of tree #2.  A non-zero cell should be used
        to create a connection between the two trees.  Different numbers
        in the table will result in connections being drawn in different
        colors.
        """
    )

    tree1_label = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Get/Set the label for tree #1.
        """
    )

    def _tree1_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTree1Label,
                        self.tree1_label)

    tree2_label = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Get/Set the label for tree #2.
        """
    )

    def _tree2_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTree2Label,
                        self.tree2_label)

    tree_line_width = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Get/Set how wide the edges of the trees should be.  Default is
        one pixel.
        """
    )

    def _tree_line_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTreeLineWidth,
                        self.tree_line_width)

    def set_tree1(self, *args):
        """
        V.set_tree1(Tree)
        C++: virtual void SetTree1(Tree *tree)
        Set the first tree
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTree1, *my_args)
        return ret

    def set_tree2(self, *args):
        """
        V.set_tree2(Tree)
        C++: virtual void SetTree2(Tree *tree)
        Set the second tree
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTree2, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('correspondence_line_width',
    'GetCorrespondenceLineWidth'), ('label_size_difference',
    'GetLabelSizeDifference'), ('minimum_visible_font_size',
    'GetMinimumVisibleFontSize'), ('orientation', 'GetOrientation'),
    ('tree1_label', 'GetTree1Label'), ('tree2_label', 'GetTree2Label'),
    ('tree_line_width', 'GetTreeLineWidth'), ('opacity', 'GetOpacity'),
    ('interactive', 'GetInteractive'), ('visible', 'GetVisible'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'correspondence_line_width',
    'interactive', 'label_size_difference', 'minimum_visible_font_size',
    'opacity', 'orientation', 'tree1_label', 'tree2_label',
    'tree_line_width', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TanglegramItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TanglegramItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['correspondence_line_width', 'interactive',
            'label_size_difference', 'minimum_visible_font_size', 'opacity',
            'orientation', 'tree1_label', 'tree2_label', 'tree_line_width',
            'visible']),
            title='Edit TanglegramItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TanglegramItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


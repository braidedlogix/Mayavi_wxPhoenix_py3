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

from tvtk.tvtk_classes.tree_algorithm import TreeAlgorithm


class TreeMapLayout(TreeAlgorithm):
    """
    TreeMapLayout - layout a Tree into a tree map
    
    Superclass: TreeAlgorithm
    
    TreeMapLayout assigns rectangular regions to each vertex in the
    tree, creating a tree map.  The data is added as a data array with
    four components per tuple representing the location and size of the
    rectangle using the format (Xmin, Xmax, Ymin, Ymax).
    
    This algorithm relies on a helper class to perform the actual layout.
    This helper class is a subclass of TreeMapLayoutStrategy.
    
    @par Thanks: Thanks to Brian Wylie and Ken Moreland from Sandia
    National Laboratories for help developing this class.
    
    @par Thanks: Tree map concept comes from: Shneiderman, B. 1992. Tree
    visualization with tree-maps: 2-d space-filling approach. ACM Trans.
    Graph. 11, 1 (Jan. 1992), 92-99.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeMapLayout, obj, update, **traits)
    
    def _get_layout_strategy(self):
        return wrap_vtk(self._vtk_obj.GetLayoutStrategy())
    def _set_layout_strategy(self, arg):
        old_val = self._get_layout_strategy()
        self._wrap_call(self._vtk_obj.SetLayoutStrategy,
                        deref_vtk(arg))
        self.trait_property_changed('layout_strategy', old_val, arg)
    layout_strategy = traits.Property(_get_layout_strategy, _set_layout_strategy, help=\
        """
        The strategy to use when laying out the tree map.
        """
    )

    rectangles_field_name = traits.String('area', enter_set=True, auto_set=False, help=\
        """
        The field name to use for storing the rectangles for each vertex.
        The rectangles are stored in a quadruple float array (min_x, max_x,
        min_y, max_y).
        """
    )

    def _rectangles_field_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRectanglesFieldName,
                        self.rectangles_field_name)

    def get_bounding_box(self, *args):
        """
        V.get_bounding_box(int, [float, ...])
        C++: void GetBoundingBox(IdType id, float *binfo)
        Return the min and max 2d points of the vertex's bounding box
        """
        ret = self._wrap_call(self._vtk_obj.GetBoundingBox, *args)
        return ret

    def find_vertex(self, *args):
        """
        V.find_vertex([float, float], [float, ...]) -> int
        C++: IdType FindVertex(float pnt[2], float *binfo=0)
        Returns the vertex id that contains pnt (or -1 if no one contains
        it)
        """
        ret = self._wrap_call(self._vtk_obj.FindVertex, *args)
        return ret

    def set_size_array_name(self, *args):
        """
        V.set_size_array_name(string)
        C++: virtual void SetSizeArrayName(const char *name)
        The array to use for the size of each vertex.
        """
        ret = self._wrap_call(self._vtk_obj.SetSizeArrayName, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('rectangles_field_name', 'GetRectanglesFieldName'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'rectangles_field_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeMapLayout, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeMapLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['rectangles_field_name']),
            title='Edit TreeMapLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeMapLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


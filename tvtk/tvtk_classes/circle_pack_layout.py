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


class CirclePackLayout(TreeAlgorithm):
    """
    CirclePackLayout - layout a Tree as a circle packing.
    
    Superclass: TreeAlgorithm
    
    CirclePackLayout assigns circle shaped regions to each vertex in
    the tree, creating a circle packing layout.  The data is added as a
    data array with three components per tuple representing the center
    and radius of the circle using the format (Xcenter, Ycenter, Radius).
    
    This algorithm relies on a helper class to perform the actual layout.
    This helper class is a subclass of CirclePackLayoutStrategy.
    
    An array by default called "size" can be attached to the input tree
    that specifies the size of each leaf node in the tree.  The filter
    will calculate the sizes of all interior nodes in the tree based on
    the sum of the leaf node sizes.  If no "size" array is given in the
    input Tree, a size of 1 is used for all leaf nodes to find the
    size of the interior nodes.
    
    @par Thanks: Thanks to Thomas Otahal from Sandia National
    Laboratories for help developing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCirclePackLayout, obj, update, **traits)
    
    circles_field_name = traits.String('circles', enter_set=True, auto_set=False, help=\
        """
        The field name to use for storing the circles for each vertex.
        The rectangles are stored in a triple float array (Xcenter,
        Ycenter, Radius). Default name is "circles"
        """
    )

    def _circles_field_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCirclesFieldName,
                        self.circles_field_name)

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

    def get_bounding_circle(self, *args):
        """
        V.get_bounding_circle(int, [float, ...])
        C++: void GetBoundingCircle(IdType id, double *cinfo)
        Return the Xcenter, Ycenter, and Radius of the vertex's bounding
        circle
        """
        ret = self._wrap_call(self._vtk_obj.GetBoundingCircle, *args)
        return ret

    def find_vertex(self, *args):
        """
        V.find_vertex([float, float], [float, ...]) -> int
        C++: IdType FindVertex(double pnt[2], double *cinfo=0)
        Returns the vertex id that contains pnt (or -1 if no one contains
        it) pnt[0] is x, and pnt[1] is y. If cinfo[3] is provided, then
        (Xcenter, Ycenter, Radius) of the circle containing pnt[2] will
        be returned.
        """
        ret = self._wrap_call(self._vtk_obj.FindVertex, *args)
        return ret

    def set_size_array_name(self, *args):
        """
        V.set_size_array_name(string)
        C++: virtual void SetSizeArrayName(const char *name)
        The array to use for the size of each vertex. Default name is
        "size".
        """
        ret = self._wrap_call(self._vtk_obj.SetSizeArrayName, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('circles_field_name', 'GetCirclesFieldName'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'circles_field_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CirclePackLayout, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CirclePackLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['circles_field_name']),
            title='Edit CirclePackLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CirclePackLayout properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


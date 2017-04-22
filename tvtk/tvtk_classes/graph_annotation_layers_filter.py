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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class GraphAnnotationLayersFilter(PolyDataAlgorithm):
    """
    GraphAnnotationLayersFilter - Produce filled convex hulls around
    subsets of vertices in a Graph.
    
    Superclass: PolyDataAlgorithm
    
    Produces a PolyData comprised of filled polygons of the convex
    hull of a cluster. Alternatively, you may choose to output bounding
    rectangles. Clusters with fewer than three vertices are artificially
    expanded to ensure visibility (see ConvexHull2D).
    
    The first input is a Graph with points, possibly set by passing
    the graph through GraphLayout (z-values are ignored). The second
    input is a AnnotationsLayer containing SelectionNodeS of vertex
    ids (the 'clusters' output of TulipReader for example).
    
    Setting outline_on() additionally produces outlines of the clusters on
    output port 1.
    
    Three arrays are added to the cells of the output: "Hull id"; "Hull
    name"; and "Hull color".
    
    Note: This filter operates in the x,y-plane and as such works best
    with an interactor style that does not allow camera rotation, such as
    InteractorStyleRubberBand2D.
    
    @sa
    Context2D
    
    @par Thanks: Thanks to Colin Myers, University of Leeds for providing
    this implementation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGraphAnnotationLayersFilter, obj, update, **traits)
    
    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def outline_off(self):
        """
        V.outline_off()
        C++: void OutlineOff()
        Produce outlines of the hulls on output port 1.
        """
        ret = self._vtk_obj.OutlineOff()
        return ret
        

    def outline_on(self):
        """
        V.outline_on()
        C++: void OutlineOn()
        Produce outlines of the hulls on output port 1.
        """
        ret = self._vtk_obj.OutlineOn()
        return ret
        

    def set_hull_shape_to_bounding_rectangle(self):
        """
        V.set_hull_shape_to_bounding_rectangle()
        C++: void SetHullShapeToBoundingRectangle()
        Set the shape of the hulls to bounding rectangle.
        """
        ret = self._vtk_obj.SetHullShapeToBoundingRectangle()
        return ret
        

    def set_hull_shape_to_convex_hull(self):
        """
        V.set_hull_shape_to_convex_hull()
        C++: void SetHullShapeToConvexHull()
        Set the shape of the hulls to convex hull. Default.
        """
        ret = self._vtk_obj.SetHullShapeToConvexHull()
        return ret
        

    def set_min_hull_size_in_display(self, *args):
        """
        V.set_min_hull_size_in_display(int)
        C++: void SetMinHullSizeInDisplay(int size)
        Set the minimum x,y-dimensions of each hull in pixels. You must
        also set a Renderer. Defaults to 1. Set to 0 to disable.
        """
        ret = self._wrap_call(self._vtk_obj.SetMinHullSizeInDisplay, *args)
        return ret

    def set_min_hull_size_in_world(self, *args):
        """
        V.set_min_hull_size_in_world(float)
        C++: void SetMinHullSizeInWorld(double size)
        Set the minimum x,y-dimensions of each hull in world coordinates.
        Defaults to 1.0. Set to 0.0 to disable.
        """
        ret = self._wrap_call(self._vtk_obj.SetMinHullSizeInWorld, *args)
        return ret

    def set_outline(self, *args):
        """
        V.set_outline(bool)
        C++: void SetOutline(bool b)
        Produce outlines of the hulls on output port 1.
        """
        ret = self._wrap_call(self._vtk_obj.SetOutline, *args)
        return ret

    def set_renderer(self, *args):
        """
        V.set_renderer(Renderer)
        C++: void SetRenderer(Renderer *renderer)
        Renderer needed for min_hull_size_in_display calculation. Not
        reference counted.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetRenderer, *my_args)
        return ret

    def set_scale_factor(self, *args):
        """
        V.set_scale_factor(float)
        C++: void SetScaleFactor(double scale)
        Scale each hull by the amount specified. Defaults to 1.0.
        """
        ret = self._wrap_call(self._vtk_obj.SetScaleFactor, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GraphAnnotationLayersFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GraphAnnotationLayersFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit GraphAnnotationLayersFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GraphAnnotationLayersFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


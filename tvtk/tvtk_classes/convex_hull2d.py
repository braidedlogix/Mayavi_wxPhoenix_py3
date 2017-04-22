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


class ConvexHull2D(PolyDataAlgorithm):
    """
    ConvexHull2D - Produce filled convex hulls around a set of points.
    
    Superclass: PolyDataAlgorithm
    
    Produces a PolyData comprised of a filled polygon of the convex
    hull of the input points. You may alternatively choose to output a
    bounding rectangle. Static methods are provided that calculate a
    (counter-clockwise) hull based on a set of input points.
    
    To help maintain the property of guaranteed visibilityhulls may be
    artificially scaled by setting min_hull_size_in_world. This is
    particularly helpful in the case that there are only one or two
    points as it avoids producing a degenerate polygon. This setting is
    also available as an argument to the static methods.
    
    Setting a Renderer on the filter enables the possibility to set
    min_hull_size_in_display to the desired number of display pixels to cover
    in each of the x- and y-dimensions.
    
    Setting outline_on() additionally produces an outline of the hull on
    output port 1.
    
    @attention This filter operates in the x,y-plane and as such works
    best with an interactor style that does not permit camera rotation
    such as InteractorStyleRubberBand2D.
    
    @par Thanks: Thanks to Colin Myers, University of Leeds for providing
    this implementation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkConvexHull2D, obj, update, **traits)
    
    outline = tvtk_base.false_bool_trait(help=\
        """
        Produce an outline (polyline) of the hull on output port 1.
        """
    )

    def _outline_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutline,
                        self.outline_)

    hull_shape = traits.Trait(1, traits.Range(0, 1, enter_set=True, auto_set=False), help=\
        """
        Set the shape of the hull to bounding_rectangle or convex_hull.
        """
    )

    def _hull_shape_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHullShape,
                        self.hull_shape)

    min_hull_size_in_display = traits.Trait(10, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the minimum x,y-dimensions of each hull in pixels. You must
        also set a Renderer. Defaults to 1. Set to 0 to disable.
        """
    )

    def _min_hull_size_in_display_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinHullSizeInDisplay,
                        self.min_hull_size_in_display)

    min_hull_size_in_world = traits.Trait(1.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set the minimum x,y-dimensions of each hull in world coordinates.
        Defaults to 1.0. Set to 0.0 to disable.
        """
    )

    def _min_hull_size_in_world_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinHullSizeInWorld,
                        self.min_hull_size_in_world)

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        Renderer needed for min_hull_size_in_display calculation. Not
        reference counted.
        """
    )

    scale_factor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Scale the hull by the amount specified. Defaults to 1.0.
        """
    )

    def _scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleFactor,
                        self.scale_factor)

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

    def calculate_bounding_rectangle(self, *args):
        """
        V.calculate_bounding_rectangle(Points, Points, float)
        C++: static void CalculateBoundingRectangle(Points *inPoints,
            Points *outPoints, double minimumHullSize=1.0)
        Convenience methods to calculate a convex hull from a set of
        PointS.
        """
        my_args = deref_array(args, [('vtkPoints', 'vtkPoints', 'float')])
        ret = self._wrap_call(self._vtk_obj.CalculateBoundingRectangle, *my_args)
        return ret

    def calculate_convex_hull(self, *args):
        """
        V.calculate_convex_hull(Points, Points, float)
        C++: static void CalculateConvexHull(Points *inPoints,
            Points *outPoints, double minimumHullSize=1.0)
        Convenience methods to calculate a convex hull from a set of
        PointS.
        """
        my_args = deref_array(args, [('vtkPoints', 'vtkPoints', 'float')])
        ret = self._wrap_call(self._vtk_obj.CalculateConvexHull, *my_args)
        return ret

    _updateable_traits_ = \
    (('outline', 'GetOutline'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('hull_shape',
    'GetHullShape'), ('min_hull_size_in_display',
    'GetMinHullSizeInDisplay'), ('min_hull_size_in_world',
    'GetMinHullSizeInWorld'), ('scale_factor', 'GetScaleFactor'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'outline',
    'release_data_flag', 'hull_shape', 'min_hull_size_in_display',
    'min_hull_size_in_world', 'progress_text', 'scale_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ConvexHull2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ConvexHull2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['outline'], [], ['hull_shape', 'min_hull_size_in_display',
            'min_hull_size_in_world', 'scale_factor']),
            title='Edit ConvexHull2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ConvexHull2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


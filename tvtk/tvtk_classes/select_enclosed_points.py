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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class SelectEnclosedPoints(DataSetAlgorithm):
    """
    SelectEnclosedPoints - mark points as to whether they are inside a
    closed surface
    
    Superclass: DataSetAlgorithm
    
    SelectEnclosedPoints is a filter that evaluates all the input
    points to determine whether they are in an enclosed surface. The
    filter produces a (0,1) mask (in the form of a DataArray) that
    indicates whether points are outside (mask value=0) or inside (mask
    value=1) a provided surface. (The name of the output DataArray is
    "_selected_points_array".)
    
    After running the filter, it is possible to query it as to whether a
    point is inside/outside by invoking the is_inside(pt_id) method.
    
    @warning
    The filter assumes that the surface is closed and manifold. A boolean
    flag can be set to force the filter to first check whether this is
    true. If false, all points will be marked outside. Note that if this
    check is not performed and the surface is not closed, the results are
    undefined.
    
    @warning
    This filter produces and output data array, but does not modify the
    input dataset. If you wish to extract cells or poinrs, various
    threshold filters are available (i.e., threshold the output array).
    
    @sa
    MaskPoints
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSelectEnclosedPoints, obj, update, **traits)
    
    check_surface = tvtk_base.false_bool_trait(help=\
        """
        Specify whether to check the surface for closure. If on, then the
        algorithm first checks to see if the surface is closed and
        manifold.
        """
    )

    def _check_surface_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCheckSurface,
                        self.check_surface_)

    inside_out = tvtk_base.false_bool_trait(help=\
        """
        By default, points inside the surface are marked inside or sent
        to the output. If inside_out is on, then the points outside the
        surface are marked inside.
        """
    )

    def _inside_out_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInsideOut,
                        self.inside_out_)

    tolerance = traits.Trait(0.001, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Specify the tolerance on the intersection. The tolerance is
        expressed as a fraction of the bounding box of the enclosing
        surface.
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def _get_surface(self):
        return wrap_vtk(self._vtk_obj.GetSurface())
    surface = traits.Property(_get_surface, help=\
        """
        Return a pointer to the enclosing surface.
        """
    )

    def complete(self):
        """
        V.complete()
        C++: void Complete()
        This is a backdoor that can be used to test many points for
        containment. First initialize the instance, then repeated calls
        to is_inside_surface() can be used without rebuilding the search
        structures. The complete method releases memory.
        """
        ret = self._vtk_obj.Complete()
        return ret
        

    def initialize(self, *args):
        """
        V.initialize(PolyData)
        C++: void Initialize(PolyData *surface)
        This is a backdoor that can be used to test many points for
        containment. First initialize the instance, then repeated calls
        to is_inside_surface() can be used without rebuilding the search
        structures. The complete method releases memory.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Initialize, *my_args)
        return ret

    def is_inside(self, *args):
        """
        V.is_inside(int) -> int
        C++: int IsInside(IdType inputPtId)
        Query an input point id as to whether it is inside or outside.
        Note that the result requires that the filter execute first.
        """
        ret = self._wrap_call(self._vtk_obj.IsInside, *args)
        return ret

    def is_inside_surface(self, *args):
        """
        V.is_inside_surface(float, float, float) -> int
        C++: int IsInsideSurface(double x, double y, double z)
        V.is_inside_surface([float, float, float]) -> int
        C++: int IsInsideSurface(double x[3])
        This is a backdoor that can be used to test many points for
        containment. First initialize the instance, then repeated calls
        to is_inside_surface() can be used without rebuilding the search
        structures. The complete method releases memory.
        """
        ret = self._wrap_call(self._vtk_obj.IsInsideSurface, *args)
        return ret

    def set_surface_connection(self, *args):
        """
        V.set_surface_connection(AlgorithmOutput)
        C++: void SetSurfaceConnection(AlgorithmOutput *algOutput)
        Set the surface to be used to test for containment. Two methods
        are provided: one directly for PolyData, and one for the
        output of a filter.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSurfaceConnection, *my_args)
        return ret

    def set_surface_data(self, *args):
        """
        V.set_surface_data(PolyData)
        C++: void SetSurfaceData(PolyData *pd)
        Set the surface to be used to test for containment. Two methods
        are provided: one directly for PolyData, and one for the
        output of a filter.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSurfaceData, *my_args)
        return ret

    _updateable_traits_ = \
    (('check_surface', 'GetCheckSurface'), ('inside_out', 'GetInsideOut'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('tolerance',
    'GetTolerance'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'check_surface', 'debug', 'global_warning_display',
    'inside_out', 'release_data_flag', 'progress_text', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SelectEnclosedPoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SelectEnclosedPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['check_surface', 'inside_out'], [], ['tolerance']),
            title='Edit SelectEnclosedPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SelectEnclosedPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


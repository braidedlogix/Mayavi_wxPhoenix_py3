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

from tvtk.tvtk_classes.graph_algorithm import GraphAlgorithm


class SplineGraphEdges(GraphAlgorithm):
    """
    SplineGraphEdges - subsample graph edges to make smooth curves
    
    Superclass: GraphAlgorithm
    
    SplineGraphEdges uses a Spline to make edges into nicely
    sampled splines. By default, the filter will use an optimized
    b-spline. Otherwise, it will use a custom Spline instance set by
    the user.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSplineGraphEdges, obj, update, **traits)
    
    number_of_subdivisions = traits.Int(20, enter_set=True, auto_set=False, help=\
        """
        The number of subdivisions in the spline.
        """
    )

    def _number_of_subdivisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSubdivisions,
                        self.number_of_subdivisions)

    def _get_spline(self):
        return wrap_vtk(self._vtk_obj.GetSpline())
    def _set_spline(self, arg):
        old_val = self._get_spline()
        self._wrap_call(self._vtk_obj.SetSpline,
                        deref_vtk(arg))
        self.trait_property_changed('spline', old_val, arg)
    spline = traits.Property(_get_spline, _set_spline, help=\
        """
        If spline_type is CUSTOM, uses this spline.
        """
    )

    spline_type = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Spline type used by the filter. BSPLINE (0) - Use optimized
        b-spline (default). CUSTOM (1) - Use spline set with set_spline.
        """
    )

    def _spline_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSplineType,
                        self.spline_type)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_subdivisions', 'GetNumberOfSubdivisions'), ('spline_type',
    'GetSplineType'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_subdivisions', 'progress_text',
    'spline_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SplineGraphEdges, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SplineGraphEdges properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['number_of_subdivisions', 'spline_type']),
            title='Edit SplineGraphEdges properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SplineGraphEdges properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


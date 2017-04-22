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

from tvtk.tvtk_classes.clean_poly_data import CleanPolyData


class QuantizePolyDataPoints(CleanPolyData):
    """
    QuantizePolyDataPoints - quantizes x,y,z coordinates of points
    
    Superclass: CleanPolyData
    
    QuantizePolyDataPoints is a subclass of CleanPolyData and
    inherits the functionality of CleanPolyData with the addition that
    it quantizes the point coordinates before inserting into the point
    list. The user should set QFactor to a positive value (0.25 by
    default) and all {x,y,z} coordinates will be quantized to that grain
    size.
    
    A tolerance of zero is expected, though positive values may be used,
    the quantization will take place before the tolerance is applied.
    
    @warning
    Merging points can alter topology, including introducing non-manifold
    forms. Handling of degenerate cells is controlled by switches in
    CleanPolyData.
    
    @warning
    If you wish to operate on a set of coordinates that has no cells, you
    must add a PolyVertex cell with all of the points to the poly_data
    (or use a VertexGlyphFilter) before using the CleanPolyData
    filter.
    
    @sa
    CleanPolyData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkQuantizePolyDataPoints, obj, update, **traits)
    
    q_factor = traits.Trait(0.25, traits.Range(1e-05, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Specify quantization grain size. Default is 0.25
        """
    )

    def _q_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQFactor,
                        self.q_factor)

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

    _updateable_traits_ = \
    (('convert_lines_to_points', 'GetConvertLinesToPoints'),
    ('convert_polys_to_lines', 'GetConvertPolysToLines'),
    ('convert_strips_to_polys', 'GetConvertStripsToPolys'),
    ('piece_invariant', 'GetPieceInvariant'), ('point_merging',
    'GetPointMerging'), ('tolerance_is_absolute',
    'GetToleranceIsAbsolute'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('q_factor',
    'GetQFactor'), ('absolute_tolerance', 'GetAbsoluteTolerance'),
    ('output_points_precision', 'GetOutputPointsPrecision'), ('tolerance',
    'GetTolerance'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'convert_lines_to_points',
    'convert_polys_to_lines', 'convert_strips_to_polys', 'debug',
    'global_warning_display', 'piece_invariant', 'point_merging',
    'release_data_flag', 'tolerance_is_absolute', 'absolute_tolerance',
    'output_points_precision', 'progress_text', 'q_factor', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(QuantizePolyDataPoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit QuantizePolyDataPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['convert_lines_to_points', 'convert_polys_to_lines',
            'convert_strips_to_polys', 'piece_invariant', 'point_merging',
            'tolerance_is_absolute'], [], ['absolute_tolerance',
            'output_points_precision', 'q_factor', 'tolerance']),
            title='Edit QuantizePolyDataPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit QuantizePolyDataPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


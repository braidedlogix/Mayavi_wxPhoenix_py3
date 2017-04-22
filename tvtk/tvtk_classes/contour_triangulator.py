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


class ContourTriangulator(PolyDataAlgorithm):
    """
    ContourTriangulator - Fill all 2d contours to create polygons
    
    Superclass: PolyDataAlgorithm
    
    ContourTriangulator will generate triangles to fill all of the 2d
    contours in its input.  The contours may be concave, and may even
    contain holes i.e. a contour may contain an internal contour that is
    wound in the opposite direction to indicate that it is a hole.
    @warning
    The triangulation of is done in O(n) time for simple convex inputs,
    but for non-convex inputs the worst-case time is O(n^2*m^2) where n
    is the number of points and m is the number of holes. The best
    triangulation algorithms, in contrast, are O(n log n). The resulting
    triangles may be quite narrow, the algorithm does not attempt to
    produce high-quality triangles.@par Thanks: Thanks to David Gobbi for
    contributing this class to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContourTriangulator, obj, update, **traits)
    
    triangulation_error_display = tvtk_base.false_bool_trait(help=\
        """
        Generate errors when the triangulation fails. Note that
        triangulation failures are often minor, because they involve tiny
        triangles that are too small to see.
        """
    )

    def _triangulation_error_display_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTriangulationErrorDisplay,
                        self.triangulation_error_display_)

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

    def _get_triangulation_error(self):
        return self._vtk_obj.GetTriangulationError()
    triangulation_error = traits.Property(_get_triangulation_error, help=\
        """
        Check if there was a triangulation failure in the last update.
        """
    )

    def triangulate_contours(self, *args):
        """
        V.triangulate_contours(PolyData, int, int, CellArray, (float,
             float, float)) -> int
        C++: static int TriangulateContours(PolyData *data,
            IdType firstLine, IdType numLines,
            CellArray *outputPolys, const double normal[3])
        Given some closed contour lines, create a triangle mesh that
        fills those lines.  The input lines must be single-segment lines,
        not polylines.  The input lines do not have to be in order. Only
        num_lines starting from first_line will be used.
        """
        my_args = deref_array(args, [('vtkPolyData', 'int', 'int', 'vtkCellArray', ('float', 'float', 'float'))])
        ret = self._wrap_call(self._vtk_obj.TriangulateContours, *my_args)
        return ret

    def triangulate_polygon(self, *args):
        """
        V.triangulate_polygon(IdList, Points, CellArray) -> int
        C++: static int TriangulatePolygon(IdList *polygon,
            Points *points, CellArray *triangles)
        A robust method for triangulating a polygon. It cleans up the
        polygon and then applies the ear-cut triangulation. A zero return
        value indicates that triangulation failed.
        """
        my_args = deref_array(args, [('vtkIdList', 'vtkPoints', 'vtkCellArray')])
        ret = self._wrap_call(self._vtk_obj.TriangulatePolygon, *my_args)
        return ret

    _updateable_traits_ = \
    (('triangulation_error_display', 'GetTriangulationErrorDisplay'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'triangulation_error_display', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContourTriangulator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ContourTriangulator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['triangulation_error_display'], [], []),
            title='Edit ContourTriangulator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContourTriangulator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


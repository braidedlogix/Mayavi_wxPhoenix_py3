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


class IntersectionPolyDataFilter(PolyDataAlgorithm):
    """
    IntersectionPolyDataFilter - IntersectionPolyDataFilter
    computes the intersection between two PolyData objects.
    
    Superclass: PolyDataAlgorithm
    
    The first output is a set of lines that marks the intersection of the
    input PolyData objects. This contains five different attached data
    arrays:
    
    surface_id: Point data array that contains information about the
    origin surface of each point
    
    input0_cell_id: Cell data array that contains the original cell ID
    number on the first input mesh
    
    input1_cell_id: Cell data array that contains the original cell ID
    number on the second input mesh
    
    new_cell0_id: Cell data array that contains information about which
    cells of the remeshed first input surface it touches (If split)
    
    new_cell1_id: Cell data array that contains information about which
    cells on the remeshed second input surface it touches (If split)
    
    The second and third outputs are the first and second input
    PolyData, respectively. Optionally, the two output PolyData can
    be split along the intersection lines by remeshing. Optionally, the
    surface can be cleaned and checked at the end of the remeshing. If
    the meshes are split, The output PolyDatas contain three possible
    data arrays:
    
    intersection_point: This is a boolean indicating whether or not the
    point is on the boundary of the two input objects
    
    bad_triangle: If the surface is cleaned and checked, this is a cell
    data array indicating whether or not the cell has edges with multiple
    neighbors A manifold surface will have 0 everywhere for this array!
    
    free_edge: If the surface is cleaned and checked, this is a cell data
    array indicating if the cell has any free edges. A watertight surface
    will have 0 everywhere for this array!
    
    Author: Adam Updegrove updega2@gmail.com
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkIntersectionPolyDataFilter, obj, update, **traits)
    
    check_input = tvtk_base.false_bool_trait(help=\
        """
        If on, the normals of the input will be checked. Default: OFF
        """
    )

    def _check_input_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCheckInput,
                        self.check_input_)

    check_mesh = tvtk_base.true_bool_trait(help=\
        """
        If on, the output remeshed surfaces will be checked for bad cells
        and free edges. Default: ON
        """
    )

    def _check_mesh_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCheckMesh,
                        self.check_mesh_)

    compute_intersection_point_array = tvtk_base.false_bool_trait(help=\
        """
        If on, the output split surfaces will contain information about
        which points are on the intersection of the two inputs. Default:
        ON
        """
    )

    def _compute_intersection_point_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeIntersectionPointArray,
                        self.compute_intersection_point_array_)

    split_first_output = tvtk_base.true_bool_trait(help=\
        """
        If on, the second output will be the first input mesh split by
        the intersection with the second input mesh. Defaults to on.
        """
    )

    def _split_first_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSplitFirstOutput,
                        self.split_first_output_)

    split_second_output = tvtk_base.true_bool_trait(help=\
        """
        If on, the third output will be the second input mesh split by
        the intersection with the first input mesh. Defaults to on.
        """
    )

    def _split_second_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSplitSecondOutput,
                        self.split_second_output_)

    tolerance = traits.Float(1e-06, enter_set=True, auto_set=False, help=\
        """
        The tolerance for geometric tests in the filter
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

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

    def _get_number_of_intersection_lines(self):
        return self._vtk_obj.GetNumberOfIntersectionLines()
    number_of_intersection_lines = traits.Property(_get_number_of_intersection_lines, help=\
        """
        Integer describing the number of intersection points and lines
        """
    )

    def _get_number_of_intersection_points(self):
        return self._vtk_obj.GetNumberOfIntersectionPoints()
    number_of_intersection_points = traits.Property(_get_number_of_intersection_points, help=\
        """
        Integer describing the number of intersection points and lines
        """
    )

    def _get_status(self):
        return self._vtk_obj.GetStatus()
    status = traits.Property(_get_status, help=\
        """
        Check the status of the filter after update. If the status is
        zero, there was an error in the operation. If status is one,
        everything went smoothly
        """
    )

    def clean_and_check_input(self, *args):
        """
        V.clean_and_check_input(PolyData, float)
        C++: static void CleanAndCheckInput(PolyData *pd,
            double tolerance)
        Function to clean and check the inputs
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CleanAndCheckInput, *my_args)
        return ret

    def clean_and_check_surface(self, *args):
        """
        V.clean_and_check_surface(PolyData, [float, float], float)
        C++: static void CleanAndCheckSurface(PolyData *pd,
            double stats[2], double tolerance)
        Function to clean and check the output surfaces for bad triangles
        and free edges
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CleanAndCheckSurface, *my_args)
        return ret

    def triangle_triangle_intersection(self, *args):
        """
        V.triangle_triangle_intersection([float, float, float], [float,
            float, float], [float, float, float], [float, float, float],
            [float, float, float], [float, float, float], int, [float,
            float, float], [float, float, float], [float, float], float)
            -> int
        C++: static int TriangleTriangleIntersection(double p1[3],
            double q1[3], double r1[3], double p2[3], double q2[3],
            double r2[3], int &coplanar, double pt1[3], double pt2[3],
            double surfaceid[2], double tolerance)
        Given two triangles defined by points (p1, q1, r1) and (p2, q2,
        r2), returns whether the two triangles intersect. If they do, the
        endpoints of the line forming the intersection are returned in
        pt1 and pt2. The parameter coplanar is set to 1 if the triangles
        are coplanar and 0 otherwise. The surfaceid array is filled with
        the surface on which the first and second intersection points
        resides, respectively. A geometric tolerance can be specified in
        the last argument.
        """
        ret = self._wrap_call(self._vtk_obj.TriangleTriangleIntersection, *args)
        return ret

    _updateable_traits_ = \
    (('check_input', 'GetCheckInput'), ('check_mesh', 'GetCheckMesh'),
    ('compute_intersection_point_array',
    'GetComputeIntersectionPointArray'), ('split_first_output',
    'GetSplitFirstOutput'), ('split_second_output',
    'GetSplitSecondOutput'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('tolerance',
    'GetTolerance'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'check_input', 'check_mesh',
    'compute_intersection_point_array', 'debug', 'global_warning_display',
    'release_data_flag', 'split_first_output', 'split_second_output',
    'progress_text', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(IntersectionPolyDataFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit IntersectionPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['check_input', 'check_mesh',
            'compute_intersection_point_array', 'split_first_output',
            'split_second_output'], [], ['tolerance']),
            title='Edit IntersectionPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit IntersectionPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


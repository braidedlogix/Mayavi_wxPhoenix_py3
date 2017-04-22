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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class Delaunay3D(UnstructuredGridAlgorithm):
    """
    Delaunay3D - create 3d Delaunay triangulation of input points
    
    Superclass: UnstructuredGridAlgorithm
    
    Delaunay3D is a filter that constructs a 3d Delaunay triangulation
    from a list of input points. These points may be represented by any
    dataset of type PointSet and subclasses. The output of the filter
    is an unstructured grid dataset. Usually the output is a tetrahedral
    mesh, but if a non-zero alpha distance value is specified (called the
    "alpha" value), then only tetrahedra, triangles, edges, and vertices
    laying within the alpha radius are output. In other words, non-zero
    alpha values may result in arbitrary combinations of tetrahedra,
    triangles, lines, and vertices. (The notion of alpha value is derived
    from Edelsbrunner's work on "alpha shapes".) Note that a modification
    to alpha shapes enables output of combinations of tetrahedra,
    triangles, lines, and/or verts (see the boolean ivars alpha_tets,
    alpha_tris, alpha_lines, alpha_verts).
    
    The 3d Delaunay triangulation is defined as the triangulation that
    satisfies the Delaunay criterion for n-dimensional simplexes (in this
    case n=3 and the simplexes are tetrahedra). This criterion states
    that a circumsphere of each simplex in a triangulation contains only
    the n+1 defining points of the simplex. (See text for more
    information.) While in two dimensions this translates into an
    "optimal" triangulation, this is not true in 3d, since a measurement
    for optimality in 3d is not agreed on.
    
    Delaunay triangulations are used to build topological structures from
    unorganized (or unstructured) points. The input to this filter is a
    list of points specified in 3d. (If you wish to create 2d
    triangulations see Delaunay2D.) The output is an unstructured
    grid.
    
    The Delaunay triangulation can be numerically sensitive. To prevent
    problems, try to avoid injecting points that will result in triangles
    with bad aspect ratios (1000:1 or greater). In practice this means
    inserting points that are "widely dispersed", and enables smooth
    transition of triangle sizes throughout the mesh. (You may even want
    to add extra points to create a better point distribution.) If
    numerical problems are present, you will see a warning message to
    this effect at the end of the triangulation process.
    
    @warning
    Points arranged on a regular lattice (termed degenerate cases) can be
    triangulated in more than one way (at least according to the Delaunay
    criterion). The choice of triangulation (as implemented by this
    algorithm) depends on the order of the input points. The first four
    points will form a tetrahedron; other degenerate points (relative to
    this initial tetrahedron) will not break it.
    
    @warning
    Points that are coincident (or nearly so) may be discarded by the
    algorithm.  This is because the Delaunay triangulation requires
    unique input points.  You can control the definition of coincidence
    with the "Tolerance" instance variable.
    
    @warning
    The output of the Delaunay triangulation is supposedly a convex hull.
    In certain cases this implementation may not generate the convex
    hull. This behavior can be controlled by the Offset instance
    variable. Offset is a multiplier used to control the size of the
    initial triangulation. The larger the offset value, the more likely
    you will generate a convex hull; and the more likely you are to see
    numerical problems.
    
    @warning
    The implementation of this algorithm varies from the 2d Delaunay
    algorithm (i.e., Delaunay2D) in an important way. When points are
    injected into the triangulation, the search for the enclosing
    tetrahedron is quite different. In the 3d case, the closest
    previously inserted point point is found, and then the connected
    tetrahedra are searched to find the containing one. (In 2d, a "walk"
    towards the enclosing triangle is performed.) If the triangulation is
    Delaunay, then an enclosing tetrahedron will be found. However, in
    degenerate cases an enclosing tetrahedron may not be found and the
    point will be rejected.
    
    @sa
    Delaunay2D GaussianSplatter UnstructuredGrid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDelaunay3D, obj, update, **traits)
    
    alpha_lines = tvtk_base.true_bool_trait(help=\
        """
        Boolean controls whether lines are output for non-zero alpha
        values.
        """
    )

    def _alpha_lines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlphaLines,
                        self.alpha_lines_)

    alpha_tets = tvtk_base.true_bool_trait(help=\
        """
        Boolean controls whether tetrahedra are output for non-zero alpha
        values.
        """
    )

    def _alpha_tets_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlphaTets,
                        self.alpha_tets_)

    alpha_tris = tvtk_base.true_bool_trait(help=\
        """
        Boolean controls whether triangles are output for non-zero alpha
        values.
        """
    )

    def _alpha_tris_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlphaTris,
                        self.alpha_tris_)

    alpha_verts = tvtk_base.true_bool_trait(help=\
        """
        Boolean controls whether vertices are output for non-zero alpha
        values.
        """
    )

    def _alpha_verts_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlphaVerts,
                        self.alpha_verts_)

    bounding_triangulation = tvtk_base.false_bool_trait(help=\
        """
        Boolean controls whether bounding triangulation points (and
        associated triangles) are included in the output. (These are
        introduced as an initial triangulation to begin the triangulation
        process. This feature is nice for debugging output.)
        """
    )

    def _bounding_triangulation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoundingTriangulation,
                        self.bounding_triangulation_)

    alpha = traits.Trait(0.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Specify alpha (or distance) value to control output of this
        filter.  For a non-zero alpha value, only verts, edges, faces, or
        tetra contained within the circumsphere (of radius alpha) will be
        output. Otherwise, only tetrahedra will be output. Note that the
        flags alpha_tets, alpha_tris, alpha_lines, and alpha_verts control
        whether these primitives are output when Alpha is non-zero. (By
        default all tets, triangles, lines and verts satisfying the alpha
        shape criterion are output.)
        """
    )

    def _alpha_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlpha,
                        self.alpha)

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Set / get a spatial locator for merging points. By default, an
        instance of PointLocator is used.
        """
    )

    offset = traits.Trait(2.5, traits.Range(2.5, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Specify a multiplier to control the size of the initial, bounding
        Delaunay triangulation.
        """
    )

    def _offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffset,
                        self.offset)

    output_points_precision = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set/get the desired precision for the output types. See the
        documentation for the Algorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

    tolerance = traits.Trait(0.001, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify a tolerance to control discarding of closely spaced
        points. This tolerance is specified as a fraction of the diagonal
        length of the bounding box of the points.
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
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def create_default_locator(self):
        """
        V.create_default_locator()
        C++: void CreateDefaultLocator()
        Create default locator. Used to create one when none is
        specified. The locator is used to eliminate "coincident" points.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

    def end_point_insertion(self):
        """
        V.end_point_insertion()
        C++: void EndPointInsertion()
        Invoke this method after all points have been inserted. The
        purpose of the method is to clean up internal data structures.
        Note that the (vtk_unstructured_grid *)Mesh returned from
        init_point_insertion() is NOT deleted, you still are responsible
        for cleaning that up.
        """
        ret = self._vtk_obj.EndPointInsertion()
        return ret
        

    def insert_point(self, *args):
        """
        V.insert_point(UnstructuredGrid, Points, int, [float, float,
            float], IdList)
        C++: void InsertPoint(UnstructuredGrid *Mesh,
            Points *points, IdType id, double x[3],
            IdList *holeTetras)
        This is a helper method used with init_point_insertion() to create
        tetrahedronalizations of points. Its purpose is to inject point
        at coordinates specified into tetrahedronalization. The point id
        is an index into the list of points in the mesh structure.  (See
        Delaunay3D::InitPointInsertion() for more information.)  When
        you have completed inserting points, traverse the mesh structure
        to extract desired tetrahedra (or tetra faces and edges).The
        hole_tetras id list lists all the tetrahedra that are deleted
        (invalid) in the mesh structure.
        """
        my_args = deref_array(args, [('vtkUnstructuredGrid', 'vtkPoints', 'int', ['float', 'float', 'float'], 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.InsertPoint, *my_args)
        return ret

    _updateable_traits_ = \
    (('alpha_lines', 'GetAlphaLines'), ('alpha_tets', 'GetAlphaTets'),
    ('alpha_tris', 'GetAlphaTris'), ('alpha_verts', 'GetAlphaVerts'),
    ('bounding_triangulation', 'GetBoundingTriangulation'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('alpha',
    'GetAlpha'), ('offset', 'GetOffset'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('tolerance', 'GetTolerance'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'alpha_lines', 'alpha_tets', 'alpha_tris',
    'alpha_verts', 'bounding_triangulation', 'debug',
    'global_warning_display', 'release_data_flag', 'alpha', 'offset',
    'output_points_precision', 'progress_text', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Delaunay3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Delaunay3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['alpha_lines', 'alpha_tets', 'alpha_tris', 'alpha_verts',
            'bounding_triangulation'], [], ['alpha', 'offset',
            'output_points_precision', 'tolerance']),
            title='Edit Delaunay3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Delaunay3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


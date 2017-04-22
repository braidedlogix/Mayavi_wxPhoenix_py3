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


class SmoothPolyDataFilter(PolyDataAlgorithm):
    """
    SmoothPolyDataFilter - adjust point positions using Laplacian
    smoothing
    
    Superclass: PolyDataAlgorithm
    
    SmoothPolyDataFilter is a filter that adjusts point coordinates
    using Laplacian smoothing. The effect is to "relax" the mesh, making
    the cells better shaped and the vertices more evenly distributed.
    Note that this filter operates on the lines, polygons, and triangle
    strips composing an instance of PolyData. Vertex or poly-vertex
    cells are never modified.
    
    The algorithm proceeds as follows. For each vertex v, a topological
    and geometric analysis is performed to determine which vertices are
    connected to v, and which cells are connected to v. Then, a
    connectivity array is constructed for each vertex. (The connectivity
    array is a list of lists of vertices that directly attach to each
    vertex.) Next, an iteration phase begins over all vertices. For each
    vertex v, the coordinates of v are modified according to an average
    of the connected vertices.  (A relaxation factor is available to
    control the amount of displacement of v).  The process repeats for
    each vertex. This pass over the list of vertices is a single
    iteration. Many iterations (generally around 20 or so) are repeated
    until the desired result is obtained.
    
    There are some special instance variables used to control the
    execution of this filter. (These ivars basically control what
    vertices can be smoothed, and the creation of the connectivity
    array.) The boundary_smoothing ivar enables/disables the smoothing
    operation on vertices that are on the "boundary" of the mesh. A
    boundary vertex is one that is surrounded by a semi-cycle of polygons
    (or used by a single line).
    
    Another important ivar is feature_edge_smoothing. If this ivar is
    enabled, then interior vertices are classified as either "simple", "interior
    edge", or "fixed", and smoothed differently. (Interior vertices are
    manifold vertices surrounded by a cycle of polygons; or used by two
    line cells.) The classification is based on the number of feature
    edges attached to v. A feature edge occurs when the angle between the
    two surface normals of a polygon sharing an edge is greater than the
    feature_angle ivar. Then, vertices used by no feature edges are
    classified "simple", vertices used by exactly two feature edges are
    classified "interior edge", and all others are "fixed" vertices.
    
    Once the classification is known, the vertices are smoothed
    differently. Corner (i.e., fixed) vertices are not smoothed at all.
    Simple vertices are smoothed as before (i.e., average of connected
    vertex coordinates). Interior edge vertices are smoothed only along
    their two connected edges, and only if the angle between the edges is
    less than the edge_angle ivar.
    
    The total smoothing can be controlled by using two ivars. The
    number_of_iterations is a cap on the maximum number of smoothing
    passes. The Convergence ivar is a limit on the maximum point motion.
    If the maximum motion during an iteration is less than Convergence,
    then the smoothing process terminates. (Convergence is expressed as a
    fraction of the diagonal of the bounding box.)
    
    There are two instance variables that control the generation of error
    data. If the ivar generate_error_scalars is on, then a scalar value
    indicating the distance of each vertex from its original position is
    computed. If the ivar generate_error_vectors is on, then a vector
    representing change in position is computed.
    
    Optionally you can further control the smoothing process by defining
    a second input: the Source. If defined, the input mesh is constrained
    to lie on the surface defined by the Source ivar.
    
    @warning
    The Laplacian operation reduces high frequency information in the
    geometry of the mesh. With excessive smoothing important details may
    be lost, and the surface may shrink towards the centroid. Enabling
    feature_edge_smoothing helps reduce this effect, but cannot entirely
    eliminate it. You may also wish to try WindowedSincPolyDataFilter.
    It does a better job of minimizing shrinkage.
    
    @sa
    WindowedSincPolyDataFilter Decimate DecimatePro
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSmoothPolyDataFilter, obj, update, **traits)
    
    boundary_smoothing = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the smoothing of vertices on the boundary of the
        mesh.
        """
    )

    def _boundary_smoothing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoundarySmoothing,
                        self.boundary_smoothing_)

    feature_edge_smoothing = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off smoothing along sharp interior edges.
        """
    )

    def _feature_edge_smoothing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFeatureEdgeSmoothing,
                        self.feature_edge_smoothing_)

    generate_error_scalars = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the generation of scalar distance values.
        """
    )

    def _generate_error_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateErrorScalars,
                        self.generate_error_scalars_)

    generate_error_vectors = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the generation of error vectors.
        """
    )

    def _generate_error_vectors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateErrorVectors,
                        self.generate_error_vectors_)

    convergence = traits.Trait(0.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify a convergence criterion for the iteration process.
        Smaller numbers result in more smoothing iterations.
        """
    )

    def _convergence_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConvergence,
                        self.convergence)

    edge_angle = traits.Trait(15.0, traits.Range(0.0, 180.0, enter_set=True, auto_set=False), help=\
        """
        Specify the edge angle to control smoothing along edges (either
        interior or boundary).
        """
    )

    def _edge_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEdgeAngle,
                        self.edge_angle)

    feature_angle = traits.Trait(45.0, traits.Range(0.0, 180.0, enter_set=True, auto_set=False), help=\
        """
        Specify the feature angle for sharp edge identification.
        """
    )

    def _feature_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFeatureAngle,
                        self.feature_angle)

    number_of_iterations = traits.Trait(20, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the number of iterations for Laplacian smoothing,
        """
    )

    def _number_of_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfIterations,
                        self.number_of_iterations)

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

    relaxation_factor = traits.Float(0.01, enter_set=True, auto_set=False, help=\
        """
        Specify the relaxation factor for Laplacian smoothing. As in all
        iterative methods, the stability of the process is sensitive to
        this parameter. In general, small relaxation factors and large
        numbers of iterations are more stable than larger relaxation
        factors and smaller numbers of iterations.
        """
    )

    def _relaxation_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRelaxationFactor,
                        self.relaxation_factor)

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

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    source = traits.Property(_get_source, help=\
        """
        Specify the source object which is used to constrain smoothing.
        The source defines a surface that the input (as it is smoothed)
        is constrained to lie upon.
        """
    )

    def set_source_data(self, *args):
        """
        V.set_source_data(PolyData)
        C++: void SetSourceData(PolyData *source)
        Specify the source object which is used to constrain smoothing.
        The source defines a surface that the input (as it is smoothed)
        is constrained to lie upon.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceData, *my_args)
        return ret

    _updateable_traits_ = \
    (('boundary_smoothing', 'GetBoundarySmoothing'),
    ('feature_edge_smoothing', 'GetFeatureEdgeSmoothing'),
    ('generate_error_scalars', 'GetGenerateErrorScalars'),
    ('generate_error_vectors', 'GetGenerateErrorVectors'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('convergence',
    'GetConvergence'), ('edge_angle', 'GetEdgeAngle'), ('feature_angle',
    'GetFeatureAngle'), ('number_of_iterations', 'GetNumberOfIterations'),
    ('output_points_precision', 'GetOutputPointsPrecision'),
    ('relaxation_factor', 'GetRelaxationFactor'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'boundary_smoothing', 'debug',
    'feature_edge_smoothing', 'generate_error_scalars',
    'generate_error_vectors', 'global_warning_display',
    'release_data_flag', 'convergence', 'edge_angle', 'feature_angle',
    'number_of_iterations', 'output_points_precision', 'progress_text',
    'relaxation_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SmoothPolyDataFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SmoothPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['boundary_smoothing', 'feature_edge_smoothing',
            'generate_error_scalars', 'generate_error_vectors'], [],
            ['convergence', 'edge_angle', 'feature_angle', 'number_of_iterations',
            'output_points_precision', 'relaxation_factor']),
            title='Edit SmoothPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SmoothPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


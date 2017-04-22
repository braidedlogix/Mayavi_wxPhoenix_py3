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


class UnstructuredGridQuadricDecimation(UnstructuredGridAlgorithm):
    """
    UnstructuredGridQuadricDecimation - reduce the number of
    tetrahedra in a mesh
    
    Superclass: UnstructuredGridAlgorithm
    
    UnstructuredGridQuadricDecimation is a class that simplifies
    tetrahedral meshes using randomized multiple choice edge collapses.
    The input to this filter is a UnstructuredGrid object with a
    single scalar field (specifying in the scalars_name attribute). Users
    can determine the size of the output mesh by either setting the value
    of target_reduction or number_of_tets_output. The boundary_weight can be
    set to control how well the mesh boundary should be preserved. The
    implementation uses Michael Garland's generalized Quadric Error
    Metrics, the Corner Table representation and the Standard Conjugate
    Gradient Method to order the edge collapse sequence.
    
    Instead of using the traditional priority queue, the algorithm uses a
    randomized approach to yield faster performance with comparable
    quality. At each step, a set of 8 random candidate edges are examined
    to select the best edge to collapse. This number can also be changed
    by users through number_of_candidates.
    
    For more information as well as the streaming version of this
    algorithm see:
    
    "Streaming Simplification of Tetrahedral Meshes" by H. T. Vo, S. P.
    Callahan, P. Lindstrom, V. Pascucci and C. T. Silva, IEEE
    Transactions on Visualization and Computer Graphics, 13(1):145-155,
    2007.
    
    @par Acknowledgments: This code was developed by Huy T. Vo under the
    supervision of Prof. Claudio T. Silva. The code also contains
    contributions from Peter Lindstrom and Steven P. Callahan.
    
    @par Acknowledgments: The work was supported by grants, contracts,
    and gifts from the National Science Foundation, the Department of
    Energy and IBM.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGridQuadricDecimation, obj, update, **traits)
    
    auto_add_candidates = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Enable(1)/Disable(0) the feature of temporarily doubling the
        number of candidates for each randomized set if the quadric error
        was significantly increased over the last edge collapse, i.e. if
        the ratio between the error difference and the last error is over
        some threshold. Basically, we are trying to make up for cases
        when random selection returns so many 'bad' edges. By doing this
        we can achieve a higher quality output with much less time than
        just double the number_of_candidates. Default is Enabled(1)
        """
    )

    def _auto_add_candidates_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoAddCandidates,
                        self.auto_add_candidates)

    auto_add_candidates_threshold = traits.Float(0.4, enter_set=True, auto_set=False, help=\
        """
        Set/Get the threshold that decides when to double the set size.
        Default is 0.4.
        """
    )

    def _auto_add_candidates_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoAddCandidatesThreshold,
                        self.auto_add_candidates_threshold)

    boundary_weight = traits.Float(100.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the weight of the boundary on the quadric metrics. The
        larger the number, the better the boundary is preserved.
        """
    )

    def _boundary_weight_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoundaryWeight,
                        self.boundary_weight)

    number_of_candidates = traits.Int(8, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of candidates selected for each randomized set
        before performing an edge collapse. Increasing this number can
        help producing higher quality output but it will be slower.
        Default is 8.
        """
    )

    def _number_of_candidates_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfCandidates,
                        self.number_of_candidates)

    number_of_edges_to_decimate = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the desired number of edge to collapse
        """
    )

    def _number_of_edges_to_decimate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfEdgesToDecimate,
                        self.number_of_edges_to_decimate)

    number_of_tets_output = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the desired number of tetrahedra to be outputed
        """
    )

    def _number_of_tets_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTetsOutput,
                        self.number_of_tets_output)

    scalars_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the scalar field name used for simplification
        """
    )

    def _scalars_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarsName,
                        self.scalars_name)

    target_reduction = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the desired reduction (expressed as a fraction of the
        original number of tetrehedra)
        """
    )

    def _target_reduction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetReduction,
                        self.target_reduction)

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

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('auto_add_candidates', 'GetAutoAddCandidates'),
    ('auto_add_candidates_threshold', 'GetAutoAddCandidatesThreshold'),
    ('boundary_weight', 'GetBoundaryWeight'), ('number_of_candidates',
    'GetNumberOfCandidates'), ('number_of_edges_to_decimate',
    'GetNumberOfEdgesToDecimate'), ('number_of_tets_output',
    'GetNumberOfTetsOutput'), ('scalars_name', 'GetScalarsName'),
    ('target_reduction', 'GetTargetReduction'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'auto_add_candidates',
    'auto_add_candidates_threshold', 'boundary_weight',
    'number_of_candidates', 'number_of_edges_to_decimate',
    'number_of_tets_output', 'progress_text', 'scalars_name',
    'target_reduction'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UnstructuredGridQuadricDecimation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGridQuadricDecimation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['auto_add_candidates', 'auto_add_candidates_threshold',
            'boundary_weight', 'number_of_candidates',
            'number_of_edges_to_decimate', 'number_of_tets_output',
            'scalars_name', 'target_reduction']),
            title='Edit UnstructuredGridQuadricDecimation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGridQuadricDecimation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class MaskPoints(PolyDataAlgorithm):
    """
    MaskPoints - selectively filter points
    
    Superclass: PolyDataAlgorithm
    
    MaskPoints is a filter that passes through points and point
    attributes from input dataset. (Other geometry is not passed
    through.) It is possible to mask every nth point, and to specify an
    initial offset to begin masking from. It is possible to also generate
    different random selections (jittered strides, real random samples,
    and spatially stratified random samples) from the input data. The
    filter can also generate vertices (topological primitives) as well as
    points. This is useful because vertices are rendered while points are
    not.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMaskPoints, obj, update, **traits)
    
    generate_vertices = tvtk_base.false_bool_trait(help=\
        """
        Generate output polydata vertices as well as points. A useful
        convenience method because vertices are drawn (they are topology)
        while points are not (they are geometry). By default this method
        is off.
        """
    )

    def _generate_vertices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateVertices,
                        self.generate_vertices_)

    proportional_maximum_number_of_points = tvtk_base.false_bool_trait(help=\
        """
        THIS ONLY WORKS WITH THE PARALLEL IMPLEMENTATION PMaskPoints
        RUNNING IN PARALLEL. NOTHING WILL CHANGE IF THIS IS NOT THE
        PARALLEL PMaskPoints. Determines whether maximum number of
        points is taken per processor (default) or if the maximum number
        of points is proportionally taken across processors (i.e., number
        of points per processor = points on a processor * maximum number
        of points / total points across all processors).  In the first
        case, the total number of points = maximum number of points *
        number of processors.  In the second case, the total number of
        points = maximum number of points.
        """
    )

    def _proportional_maximum_number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProportionalMaximumNumberOfPoints,
                        self.proportional_maximum_number_of_points_)

    random_mode = tvtk_base.false_bool_trait(help=\
        """
        Special flag causes randomization of point selection.
        """
    )

    def _random_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRandomMode,
                        self.random_mode_)

    single_vertex_per_cell = tvtk_base.false_bool_trait(help=\
        """
        When vertex generation is enabled, by default vertices are
        produced as multi-vertex cells (more than one per cell), if you
        wish to have a single vertex per cell, enable this flag.
        """
    )

    def _single_vertex_per_cell_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSingleVertexPerCell,
                        self.single_vertex_per_cell_)

    maximum_number_of_points = traits.Trait(9223372036854775807, traits.Range(0, 9223372036854775807, enter_set=True, auto_set=False), help=\
        """
        Limit the number of points that can be passed through (i.e., sets
        the output sample size).
        """
    )

    def _maximum_number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfPoints,
                        self.maximum_number_of_points)

    offset = traits.Trait(0, traits.Range(0, 9223372036854775807, enter_set=True, auto_set=False), help=\
        """
        Start sampling with this point. Ignored by certain random modes.
        """
    )

    def _offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffset,
                        self.offset)

    on_ratio = traits.Trait(2, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Turn on every nth point (strided sampling), ignored by random
        modes.
        """
    )

    def _on_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOnRatio,
                        self.on_ratio)

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

    random_mode_type = traits.Trait(0, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Special mode selector that switches between random mode types. 0
        - randomized strides: randomly strides through the data
        (default); fairly certain that this is not a statistically random
        sample because the output depends on the order of the input and
        the input points do not have an equal chance to appear in the
        output (plus Vitter's incremental random algorithms are more
        complex than this, while not a proof it is good indication this
        isn't a statistically random sample - the closest would be
        algorithm S) 1 - random sample: create a statistically random
        sample using Vitter's incremental algorithm D without A described
        in Vitter "Faster Mthods for Random Sampling", Communications of
        the ACM Volume 27, Issue 7, 1984 (_on_ratio and Offset are ignored)
        O(sample size) 2 - spatially stratified random sample: create a
        spatially stratified random sample using the first method
        described in Woodring et al. "In-situ Sampling of a Large-Scale
        Particle Simulation for Interactive Visualization and Analysis",
        Computer Graphics Forum, 2011 (_euro_vis 2011). (_on_ratio and Offset
        are ignored) O(N log N)
        """
    )

    def _random_mode_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRandomModeType,
                        self.random_mode_type)

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
    (('generate_vertices', 'GetGenerateVertices'),
    ('proportional_maximum_number_of_points',
    'GetProportionalMaximumNumberOfPoints'), ('random_mode',
    'GetRandomMode'), ('single_vertex_per_cell',
    'GetSingleVertexPerCell'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_number_of_points', 'GetMaximumNumberOfPoints'), ('offset',
    'GetOffset'), ('on_ratio', 'GetOnRatio'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('random_mode_type',
    'GetRandomModeType'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_vertices',
    'global_warning_display', 'proportional_maximum_number_of_points',
    'random_mode', 'release_data_flag', 'single_vertex_per_cell',
    'maximum_number_of_points', 'offset', 'on_ratio',
    'output_points_precision', 'progress_text', 'random_mode_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MaskPoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MaskPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_vertices', 'proportional_maximum_number_of_points',
            'random_mode', 'single_vertex_per_cell'], [],
            ['maximum_number_of_points', 'offset', 'on_ratio',
            'output_points_precision', 'random_mode_type']),
            title='Edit MaskPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MaskPoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


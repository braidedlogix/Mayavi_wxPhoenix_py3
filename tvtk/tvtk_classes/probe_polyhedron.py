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


class ProbePolyhedron(DataSetAlgorithm):
    """
    ProbePolyhedron - probe/interpolate data values in the interior,
    exterior or of the surface of a closed, manifold polyhedron
    
    Superclass: DataSetAlgorithm
    
    ProbePolyhedron is a filter that computes point attributes (e.g.,
    scalars, vectors, etc.) at specified point positions. The filter has
    two inputs: the Input and Source. The Source geometric structure is
    passed through the filter. The point attributes are computed at the
    Input point positions by interpolating into the source data. In this
    filter, the Source is always a closed, non-self-intersecting,
    polyhedral mesh. For example, we can compute data values on a plane
    (plane specified as Input) from a triangle mesh (e.g., output of
    marching cubes).
    
    This filter can be used to resample data from a mesh onto a different
    dataset type. For example, a polyhedral mesh (vtk_poly_data) can be
    probed with a volume (three-dimensional ImageData), and then
    volume rendering techniques can be used to visualize the results.
    Another example: a line or curve can be used to probe a mesh to
    produce x-y plots along that line or curve.
    
    @warning
    Note that cell data is not interpolated from the source. If you need
    cell data, you can always use PointDataToCellData and/or
    CellDataToPointData in various combinations.
    
    @warning
    Note that the filter interpolates from a mesh to points interior,
    exterior or on the surface of the mesh. This process is necessarily
    an approximation. Currently the approach of Mean Value Coordinates is
    used, but this filter may be extended in the future to use other
    methods.
    
    @sa
    ProbeFilter MeanValueCoordinatesInterpolator Polyhedron
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProbePolyhedron, obj, update, **traits)
    
    probe_cell_data = tvtk_base.false_bool_trait(help=\
        """
        Specify whether to probe (and hence produce) cell data. The
        interpolated point data of the source will produce the output
        cell data (output cells are passed from the input cells). Note
        that the probing of the input uses the centers of the cells as
        the probe position.
        """
    )

    def _probe_cell_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProbeCellData,
                        self.probe_cell_data_)

    probe_point_data = tvtk_base.true_bool_trait(help=\
        """
        Specify whether to probe (and hence produce) point data. The
        interpolated point data of the source will produce the output
        point data (output points are passed from the input points).
        """
    )

    def _probe_point_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProbePointData,
                        self.probe_point_data_)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    source = traits.Property(_get_source, help=\
        """
        Specify the point locations used to probe input. Any geometry can
        be used.
        """
    )

    def set_source_connection(self, *args):
        """
        V.set_source_connection(AlgorithmOutput)
        C++: void SetSourceConnection(AlgorithmOutput *algOutput)
        Specify the point locations used to probe input. Any geometry can
        be used. New style. Equivalent to set_input_connection(_1,
        alg_output).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceConnection, *my_args)
        return ret

    def set_source_data(self, *args):
        """
        V.set_source_data(PolyData)
        C++: void SetSourceData(PolyData *source)
        Specify the point locations used to probe input. Any geometry can
        be used.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceData, *my_args)
        return ret

    _updateable_traits_ = \
    (('probe_cell_data', 'GetProbeCellData'), ('probe_point_data',
    'GetProbePointData'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'probe_cell_data', 'probe_point_data', 'release_data_flag',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProbePolyhedron, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ProbePolyhedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['probe_cell_data', 'probe_point_data'], [], []),
            title='Edit ProbePolyhedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProbePolyhedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


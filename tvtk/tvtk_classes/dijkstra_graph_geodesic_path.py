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

from tvtk.tvtk_classes.graph_geodesic_path import GraphGeodesicPath


class DijkstraGraphGeodesicPath(GraphGeodesicPath):
    """
    DijkstraGraphGeodesicPath - Dijkstra algorithm to compute the
    graph geodesic.
    
    Superclass: GraphGeodesicPath
    
    Takes as input a polygonal mesh and performs a single source shortest
    path calculation. Dijkstra's algorithm is used. The implementation is
    similar to the one described in Introduction to Algorithms (Second
    Edition) by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest,
    and Cliff Stein, published by MIT Press and mc_graw-_hill. Some minor
    enhancement are added though. All vertices are not pushed on the heap
    at start, instead a front set is maintained. The heap is implemented
    as a binary heap. The output of the filter is a set of lines
    describing the shortest path from start_vertex to end_vertex.
    
    @warning
    The input polydata must have only triangle cells.
    
    @par Thanks: The class was contributed by Rasmus Paulsen.
    www.imm.dtu.dk/~rrp/VTK . Also thanks to Alexandre Gouaillard and
    Shoaib Ghias for bug fixes and enhancements.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDijkstraGraphGeodesicPath, obj, update, **traits)
    
    repel_path_from_vertices = tvtk_base.false_bool_trait(help=\
        """
        Use the input point to repel the path by assigning high costs.
        """
    )

    def _repel_path_from_vertices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRepelPathFromVertices,
                        self.repel_path_from_vertices_)

    stop_when_end_reached = tvtk_base.false_bool_trait(help=\
        """
        Stop when the end vertex is reached or calculate shortest path to
        all vertices
        """
    )

    def _stop_when_end_reached_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStopWhenEndReached,
                        self.stop_when_end_reached_)

    use_scalar_weights = tvtk_base.false_bool_trait(help=\
        """
        Use scalar values in the edge weight (experimental)
        """
    )

    def _use_scalar_weights_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseScalarWeights,
                        self.use_scalar_weights_)

    def _get_repel_vertices(self):
        return wrap_vtk(self._vtk_obj.GetRepelVertices())
    def _set_repel_vertices(self, arg):
        old_val = self._get_repel_vertices()
        my_arg = deref_array([arg], [['vtkPoints']])
        self._wrap_call(self._vtk_obj.SetRepelVertices,
                        my_arg[0])
        self.trait_property_changed('repel_vertices', old_val, arg)
    repel_vertices = traits.Property(_get_repel_vertices, _set_repel_vertices, help=\
        """
        Specify Points to use to repel the path from.
        """
    )

    def get_cumulative_weights(self, *args):
        """
        V.get_cumulative_weights(DoubleArray)
        C++: virtual void GetCumulativeWeights(DoubleArray *weights)
        Fill the array with the cumulative weights.
        """
        my_args = deref_array(args, [['vtkDoubleArray']])
        ret = self._wrap_call(self._vtk_obj.GetCumulativeWeights, *my_args)
        return ret

    def _get_id_list(self):
        return wrap_vtk(self._vtk_obj.GetIdList())
    id_list = traits.Property(_get_id_list, help=\
        """
        The vertex ids (of the input polydata) on the shortest path
        """
    )

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
    (('repel_path_from_vertices', 'GetRepelPathFromVertices'),
    ('stop_when_end_reached', 'GetStopWhenEndReached'),
    ('use_scalar_weights', 'GetUseScalarWeights'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('end_vertex', 'GetEndVertex'),
    ('start_vertex', 'GetStartVertex'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'repel_path_from_vertices',
    'stop_when_end_reached', 'use_scalar_weights', 'end_vertex',
    'progress_text', 'start_vertex'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DijkstraGraphGeodesicPath, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DijkstraGraphGeodesicPath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['repel_path_from_vertices', 'stop_when_end_reached',
            'use_scalar_weights'], [], ['end_vertex', 'start_vertex']),
            title='Edit DijkstraGraphGeodesicPath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DijkstraGraphGeodesicPath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


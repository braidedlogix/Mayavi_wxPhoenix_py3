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

from tvtk.tvtk_classes.point_set_algorithm import PointSetAlgorithm


class DeformPointSet(PointSetAlgorithm):
    """
    DeformPointSet - use a control polyhedron to deform an input
    PointSet
    
    Superclass: PointSetAlgorithm
    
    DeformPointSet is a filter that uses a control polyhdron to deform
    an input dataset of type PointSet. The control polyhedron (or
    mesh) must be a closed, manifold surface.
    
    The filter executes as follows. In initial pipeline execution, the
    control mesh and input PointSet are assumed in undeformed
    position, and an initial set of interpolation weights are computed
    for each point in the PointSet (one interpolation weight value for
    each point in the control mesh). The filter then stores these
    interpolation weights after filter execution. The next time the
    filter executes, assuming that the number of points/cells in the
    control mesh and PointSet have not changed, the points in the
    PointSet are recomputed based on the original weights. Hence if
    the control mesh has been deformed, it will in turn cause deformation
    in the PointSet. This can be used to animate or edit the geometry
    of the PointSet.
    
    @warning
    Note that a set of interpolation weights per point in the PointSet
    is maintained. The number of interpolation weights is the number of
    points in the control mesh. Hence keep the control mesh small in size
    or a n^2 data explostion will occur.
    
    @warning
    The filter maintains interpolation weights between executions (after
    the initial execution pass computes the interpolation weights). You
    can explicitly cause the filter to reinitialize by setting the
    initialize_weights boolean to true. By default, the filter will
    execute and then set initialize_weights to false.
    
    @warning
    This work was motivated by the work of Tao Ju et al in "Mesh Value
    Coordinates for Closed Triangular Meshes." The MVC algorithm is
    currently used to generate interpolation weights. However, in the
    future this filter may be extended to provide other interpolation
    functions.
    
    @warning
    A final note: point data and cell data are passed from the input to
    the output. Only the point coordinates of the input PointSet are
    modified.
    
    @sa
    MeanValueCoordinatesInterpolator ProbePolyhedron Polyhedron
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDeformPointSet, obj, update, **traits)
    
    initialize_weights = tvtk_base.false_bool_trait(help=\
        """
        Specify whether to regenerate interpolation weights or not.
        Initially the filter will reexecute no matter what this flag is
        set to (initial weights must be computed). Also, this flag is
        ignored if the number of input points/cells or the number of
        control mesh points/cells changes between executions. Thus flag
        is used to force reexecution and recomputation of weights.
        """
    )

    def _initialize_weights_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInitializeWeights,
                        self.initialize_weights_)

    def _get_control_mesh_data(self):
        return wrap_vtk(self._vtk_obj.GetControlMeshData())
    def _set_control_mesh_data(self, arg):
        old_val = self._get_control_mesh_data()
        self._wrap_call(self._vtk_obj.SetControlMeshData,
                        deref_vtk(arg))
        self.trait_property_changed('control_mesh_data', old_val, arg)
    control_mesh_data = traits.Property(_get_control_mesh_data, _set_control_mesh_data, help=\
        """
        Specify the control mesh to deform the input PointSet. The
        control mesh must be a closed, non-self-intersecting, manifold
        mesh.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        
        """
    )

    def set_control_mesh_connection(self, *args):
        """
        V.set_control_mesh_connection(AlgorithmOutput)
        C++: void SetControlMeshConnection(AlgorithmOutput *algOutput)
        Specify the point locations used to probe input. Any geometry can
        be used. New style. Equivalent to set_input_connection(_1,
        alg_output).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetControlMeshConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('initialize_weights', 'GetInitializeWeights'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'initialize_weights', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DeformPointSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DeformPointSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['initialize_weights'], [], []),
            title='Edit DeformPointSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DeformPointSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


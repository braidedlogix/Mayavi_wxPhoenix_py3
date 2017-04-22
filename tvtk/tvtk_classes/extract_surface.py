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


class ExtractSurface(PolyDataAlgorithm):
    """
    ExtractSurface - generate zero-crossing isosurface from truncated
    signed distance volume
    
    Superclass: PolyDataAlgorithm
    
    This filter extracts the zero-crossing isosurface from a truncated
    signed distance function TSDF. The TSDF is sampled across a volume,
    and is extracted using a modified version of the Flying Edges
    algorithm for increased speed, and to support multithreading. To use
    the filter, an input volume should be assigned, which may have
    special values indicating empty and/or unseen portions of the volume.
    These values are equal to +/- radius value of the signed distance
    function, and should be consistent with any filters used to generate
    the input volume (e.g., SignedDistance).
    
    The Flying Edges algorithm is modified to deal with the nature of the
    truncated, signed distance function. Being truncated, the distance
    function typically is not computed throughout the volume, rather the
    special data values "unseen" and/or "empty" maybe assigned to distant
    or bordering voxels. The implications of this are that this
    implementation may produce non-closed, non-manifold surfaces, which
    is what is needed to extract surfaces.
    
    More specifically, voxels may exist in one of three states: 1) within
    the TSDF, which extends +/-Radius from a generating geometry
    (typically a point cloud); 2) in the empty state, in which it is
    known that the surface does not exist; and 3) the unseen state, where
    a surface may exist but not enough information is known to be
    certain. Such situations arise, for example, when laser scanners
    generate point clouds, and the propagation of the laser beam "carves"
    out regions where no geometry exists (thereby defining empty space).
    Furthermore, areas in which the beam are occluded by geometry are
    known as "unseen" and the boundary between empty and unseen can be
    processed to produced a portion of the output isosurface (this is
    called hole filling).
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @warning
    
    Notes on the implementation:
    1. This is a lightly modified version of FlyingEdges3D. Some
       design goals included minimizing the impact on the FE algorithm,
       and not adding extra memory requirements.
    2. It presumes an isocontour value=0.0  (the zero crossing of a
       signed distance function).
    3. The major modifications are to the edge cases. In Flying Edges, a
       single byte represents the case of an edge, and within that byte
       only 2 bits are needed (the extra six bytes are not used). Here,
       these unused bytes are repurposed to represent the "state" of the
       edge, whether it is
    1) near to the TSDF; 2) in an empty state; or 3) unseen state.
    4. Since these now-used bits encode extra state information, masking
       and related methods are used to tease apart the edge cases from
       the edge state.
    5. Voxels with edges marked "empty" are not processed, i.e., no
       output triangle primitives are generated. Depending on whether
       hole filling is enabled, voxels with edges marked "unseen" may not
    be processed either.
    6. As a result of #1 and #5, and the desire to keep the
       implementation simple, it is possible to produce output points
       which are not attached to any output triangle. 
    
    @warning
    This algorithm loosely follows the most excellent paper by Curless
    and Levoy: "A Volumetric Method for Building Complex Models from
    Range Images."
    
    @sa
    SignedDistance FlyingEdges3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractSurface, obj, update, **traits)
    
    compute_gradients = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the computation of gradients. Gradient computation is
        fairly expensive in both time and storage. Note that if
        compute_normals is on, gradients will have to be calculated, but
        will not be stored in the output dataset. If the output data will
        be processed by filters that modify topology or geometry, it may
        be wise to turn Normals and Gradients off.
        """
    )

    def _compute_gradients_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeGradients,
                        self.compute_gradients_)

    compute_normals = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the computation of normals. Normal computation is fairly
        expensive in both time and storage. If the output data will be
        processed by filters that modify topology or geometry, it may be
        wise to turn Normals and Gradients off.
        """
    )

    def _compute_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeNormals,
                        self.compute_normals_)

    hole_filling = tvtk_base.false_bool_trait(help=\
        """
        Enable hole filling. This generates separating surfaces between
        the empty and unseen portions of the volume.
        """
    )

    def _hole_filling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHoleFilling,
                        self.hole_filling_)

    radius = traits.Trait(0.1, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Specify the radius of influence of the signed distance function.
        Data values (which are distances) that are greater than or equal
        to the radius (i.e., d >= Radius) are considered unseen voxels;
        those voxel data values d <= -Radius are considered empty voxels.
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

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
    (('compute_gradients', 'GetComputeGradients'), ('compute_normals',
    'GetComputeNormals'), ('hole_filling', 'GetHoleFilling'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('radius',
    'GetRadius'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_gradients', 'compute_normals', 'debug',
    'global_warning_display', 'hole_filling', 'release_data_flag',
    'progress_text', 'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractSurface, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractSurface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_gradients', 'compute_normals', 'hole_filling'], [],
            ['radius']),
            title='Edit ExtractSurface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractSurface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class FlyingEdgesPlaneCutter(PolyDataAlgorithm):
    """
    FlyingEdgesPlaneCutter - cut a volume with a plane and generate a
    polygonal cut surface
    
    Superclass: PolyDataAlgorithm
    
    FlyingEdgesPlaneCutter is a specialization of the flying_edges
    algorithm to cut a volume with a single plane. It is designed for
    performance and an exploratory, fast workflow.
    
    This algorithm is not only fast because it uses flying edges, but
    also because it plays some "tricks" during processing. For example,
    rather than evaluate the cut (plane) function on all volume points
    like Cutter and its ilk do, this algorithm intersects the volume
    x-edges against the plane to (potentially) generate the single
    intersection point. It then quickly classifies the voxel edges as
    above, below, or straddling the cut plane. Thus the number of plane
    evaluations is greatly reduced.
    
    For more information see FlyingEdges3D and/or the paper "Flying
    Edges: A High-Performance Scalable Isocontouring Algorithm" by
    Schroeder, Maynard, Geveci. Proc. of LDAV 2015. Chicago, IL.
    
    @warning
    This filter is specialized to 3d volumes. This implementation can
    produce degenerate triangles (i.e., zero-area triangles).
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    FlyingEdges2D FlyingEdges3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFlyingEdgesPlaneCutter, obj, update, **traits)
    
    compute_normals = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the computation of normals. The normal generated is
        simply the cut plane normal. By default this is disabled.
        """
    )

    def _compute_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeNormals,
                        self.compute_normals_)

    interpolate_attributes = tvtk_base.false_bool_trait(help=\
        """
        Indicate whether to interpolate other attribute data besides the
        input scalars (which are required). That is, as the isosurface is
        generated, interpolate all other point attribute data across
        intersected edges.
        """
    )

    def _interpolate_attributes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolateAttributes,
                        self.interpolate_attributes_)

    array_component = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get which component of the scalar array to contour on;
        defaults to 0.
        """
    )

    def _array_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayComponent,
                        self.array_component)

    def _get_plane(self):
        return wrap_vtk(self._vtk_obj.GetPlane())
    def _set_plane(self, arg):
        old_val = self._get_plane()
        self._wrap_call(self._vtk_obj.SetPlane,
                        deref_vtk(arg))
        self.trait_property_changed('plane', old_val, arg)
    plane = traits.Property(_get_plane, _set_plane, help=\
        """
        Specify the plane (an implicit function) to perform the cutting.
        The definition of the plane (its origin and normal) is controlled
        via this instance of Plane.
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
    (('compute_normals', 'GetComputeNormals'), ('interpolate_attributes',
    'GetInterpolateAttributes'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('array_component', 'GetArrayComponent'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_normals', 'debug',
    'global_warning_display', 'interpolate_attributes',
    'release_data_flag', 'array_component', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FlyingEdgesPlaneCutter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FlyingEdgesPlaneCutter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_normals', 'interpolate_attributes'], [],
            ['array_component']),
            title='Edit FlyingEdgesPlaneCutter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FlyingEdgesPlaneCutter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


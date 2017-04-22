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


class FlyingEdges3D(PolyDataAlgorithm):
    """
    FlyingEdges3D - generate isosurface from 3d image data (volume)
    
    Superclass: PolyDataAlgorithm
    
    FlyingEdges3D is a reference implementation of the 3d version of
    the flying edges algorithm. It is designed to be highly scalable
    (i.e., parallelizable) for large data. It implements certain
    performance optimizations including computational trimming to rapidly
    eliminate processing of data regions, packed bit representation of
    case table values, single edge intersection, elimination of point
    merging, and elimination of any reallocs (due to dynamic data
    insertion). Note that computational trimming is a method to reduce
    total computational cost in which partial computational results can
    be used to eliminate future computations.
    
    This is a four-pass algorithm. The first pass processes all x-edges
    and builds x-edge case values (which, when the four x-edges defining
    a voxel are combined, are equivalent to vertex-based case table
    except edge-based approaches are separable in support of parallel
    computing). Next x-voxel rows are processed to gather information
    from yz-edges (basically to count the number of y-z edge
    intersections and triangles generated). In the third pass a prefix
    sum is used to count and allocate memory for the output primitives.
    Finally in the fourth pass output primitives are generated into
    pre-allocated arrays. This implementation uses voxel cell axes (a
    x-y-z triad located at the voxel origin) to ensure that each edge is
    intersected at most one time. Note that this implementation also
    reuses the VTK Marching Cubes case table, although the vertex-based
    MC table is transformed into an edge-based table on object
    instantiation.
    
    See the paper "Flying Edges: A High-Performance Scalable
    Isocontouring Algorithm" by Schroeder, Maynard, Geveci. Proc. of LDAV
    2015. Chicago, IL.
    
    @warning
    This filter is specialized to 3d volumes. This implementation can
    produce degenerate triangles (i.e., zero-area triangles).
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    ContourFilter FlyingEdges2D SynchronizedTemplates3D
    MarchingCubes SMPFlyingEdges3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFlyingEdges3D, obj, update, **traits)
    
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

    compute_scalars = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the computation of scalars.
        """
    )

    def _compute_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeScalars,
                        self.compute_scalars_)

    interpolate_attributes = tvtk_base.false_bool_trait(help=\
        """
        Indicate whether to interpolate other attribute data. That is, as
        the isosurface is generated, interpolate all point attribute data
        across the edge. This is independent of scalar interpolation,
        which is controlled by the compute_scalars flag.
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

    number_of_contours = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the number of contours to place into the list. You only
        really need to use this method to reduce list size. The method
        set_value() will automatically increase list size as needed.
        """
    )

    def _number_of_contours_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfContours,
                        self.number_of_contours)

    def get_value(self, *args):
        """
        V.get_value(int) -> float
        C++: double GetValue(int i)
        Get the ith contour value.
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, float)
        C++: void SetValue(int i, double value)
        Set a particular contour value at contour number i. The index i
        ranges between 0<=i<_number_of_contours.
        """
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

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

    def _get_values(self):
        return self._vtk_obj.GetValues()
    values = traits.Property(_get_values, help=\
        """
        Get a pointer to an array of contour values. There will be
        get_number_of_contours() values in the list.
        """
    )

    def generate_values(self, *args):
        """
        V.generate_values(int, [float, float])
        C++: void GenerateValues(int numContours, double range[2])
        V.generate_values(int, float, float)
        C++: void GenerateValues(int numContours, double rangeStart,
            double rangeEnd)
        Generate num_contours equally spaced contour values between
        specified range. Contour values will include min/max range
        values.
        """
        ret = self._wrap_call(self._vtk_obj.GenerateValues, *args)
        return ret

    _updateable_traits_ = \
    (('compute_gradients', 'GetComputeGradients'), ('compute_normals',
    'GetComputeNormals'), ('compute_scalars', 'GetComputeScalars'),
    ('interpolate_attributes', 'GetInterpolateAttributes'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('array_component', 'GetArrayComponent'), ('number_of_contours',
    'GetNumberOfContours'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_gradients', 'compute_normals',
    'compute_scalars', 'debug', 'global_warning_display',
    'interpolate_attributes', 'release_data_flag', 'array_component',
    'number_of_contours', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FlyingEdges3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FlyingEdges3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_gradients', 'compute_normals', 'compute_scalars',
            'interpolate_attributes'], [], ['array_component',
            'number_of_contours']),
            title='Edit FlyingEdges3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FlyingEdges3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


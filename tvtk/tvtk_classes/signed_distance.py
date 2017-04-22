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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class SignedDistance(ImageAlgorithm):
    """
    SignedDistance - compute signed distances from an input point cloud
    
    Superclass: ImageAlgorithm
    
    SignedDistance is a filter that computes signed distances over a
    volume from an input point cloud. The input point cloud must have
    point normals defined, as well as an optional weighting function
    (e.g., probabilities that the point measurements are accurate). Once
    the signed distance function is computed, then the output volume may
    be isocontoured to extract a approximating surface to the point
    cloud.
    
    To use this filter, specify the input PolyData (which represents
    the point cloud); define the sampling volume; specify a radius (which
    limits the radius of influence of each point); and set an optional
    point locator (to accelerate proximity operations, a
    StaticPointLocator is used by default). Note that large radius
    values may have significant impact on performance. The volume is
    defined by specifying dimensions in the x-y-z directions, as well as
    a domain bounds. By default the model bounds are defined from the
    input points, but the user can also manually specify them.
    
    This filter has one other unusual capability: it is possible to
    append data in a sequence of operations to generate a single output.
    This is useful when you have multiple point clouds (e.g., possibly
    from multiple acqusition scans) and want to incrementally accumulate
    all the data. However, the user must be careful to either specify the
    Bounds or order the input such that the bounds of the first input
    completely contains all other input data.  This is because the
    geometry and topology of the output sampling volume cannot be changed
    after the initial Append operation.
    
    This algorithm loosely follows the most excellent paper by Curless
    and Levoy: "A Volumetric Method for Building Complex Models from
    Range Images." As described in this paper it may produce a signed
    distance volume that may contain the three data states for each
    voxel: near surface, empty, or unseen (see ExtractSurface for
    additional information). However, this algorithm has been extended to
    support different interpolation kernels as follows.
    
    (Kernel description TODO including supplied weights.)
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    ExtractSurface ImplicitModeller
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSignedDistance, obj, update, **traits)
    
    bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    dimensions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(256, 256, 256), cols=3, help=\
        """
        Set/Get the i-j-k dimensions on which to computer the distance
        function.
        """
    )

    def _dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimensions,
                        self.dimensions)

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Specify a point locator. By default a StaticPointLocator is
        used. The locator performs efficient searches to locate points
        surrounding a voxel (within the specified radius).
        """
    )

    radius = traits.Trait(0.1, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Set / get the radius of influence of each point. Smaller values
        generally improve performance markedly.
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
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get a data object for one of the input port connections.  The use
        of this method is strongly discouraged, but some filters that
        were written a long time ago still use this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def append(self, *args):
        """
        V.append(PolyData)
        C++: void Append(PolyData *input)
        Append a data set to the existing output. To use this function,
        you'll have to invoke the start_append() method before doing
        successive appends. It's also a good idea to specify the model
        bounds; otherwise the input model bounds is used. When you've
        finished appending, use the end_append() method.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Append, *my_args)
        return ret

    def end_append(self):
        """
        V.end_append()
        C++: void EndAppend()
        Method completes the append process.
        """
        ret = self._vtk_obj.EndAppend()
        return ret
        

    def start_append(self):
        """
        V.start_append()
        C++: void StartAppend()
        Initialize the filter for appending data. You must invoke the
        start_append() method before doing successive Appends(). It's also
        a good idea to manually specify the model bounds; otherwise the
        input bounds for the data will be used.
        """
        ret = self._vtk_obj.StartAppend()
        return ret
        

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('bounds',
    'GetBounds'), ('dimensions', 'GetDimensions'), ('radius',
    'GetRadius'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'bounds', 'dimensions', 'progress_text',
    'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SignedDistance, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SignedDistance properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['bounds', 'dimensions', 'radius']),
            title='Edit SignedDistance properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SignedDistance properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class VoxelGrid(PolyDataAlgorithm):
    """
    VoxelGrid - subsample points using uniform binning
    
    Superclass: PolyDataAlgorithm
    
    VoxelGrid is a filter that subsamples a point cloud based on a
    regular binning of space. Basically the algorithm operates by
    dividing space into a volume of M x N x O bins, and then for each bin
    averaging all of the points positions into a single representive
    point. Several strategies for computing the binning can be used: 1)
    manual configuration of a requiring specifying bin dimensions (the
    bounds are calculated from the data); 2) by explicit specification of
    the bin size in world coordinates (x-y-z lengths); and 3) an
    automatic process in which the user specifies an approximate, average
    number of points per bin and dimensions and bin size are computed
    automatically. (Note that under the hood a StaticPointLocator is
    used.)
    
    While any PointSet type can be provided as input, the output is
    represented by an explicit representation of points via a
    PolyData. This output polydata will populate its instance of
    Points, but no cells will be defined (i.e., no Vertex or
    PolyVertex are contained in the output).
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    StaticPointLocator PointCloudFilter QuadricClustering
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVoxelGrid, obj, update, **traits)
    
    configuration_style = traits.Trait('automatic',
    tvtk_base.TraitRevPrefixMap({'automatic': 2, 'leaf_size': 1, 'manual': 0}), help=\
        """
        Configure how the filter is to operate. The user can choose to
        manually specify the binning volume (by setting its dimensions
        via MANUAL style); or specify a leaf bin size in the x-y-z
        directions (SPECIFY_LEAF_SIZE); or in AUTOMATIC style, use a
        rough average number of points in each bin guide the bin size and
        binning volume dimensions. By default, AUTOMATIC configuration
        style is used.
        """
    )

    def _configuration_style_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConfigurationStyle,
                        self.configuration_style_)

    divisions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(50, 50, 50), cols=3, help=\
        """
        
        """
    )

    def _divisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDivisions,
                        self.divisions)

    def _get_kernel(self):
        return wrap_vtk(self._vtk_obj.GetKernel())
    def _set_kernel(self, arg):
        old_val = self._get_kernel()
        self._wrap_call(self._vtk_obj.SetKernel,
                        deref_vtk(arg))
        self.trait_property_changed('kernel', old_val, arg)
    kernel = traits.Property(_get_kernel, _set_kernel, help=\
        """
        Specify an interpolation kernel to combine the point attributes.
        By default a LinearKernel is used (i.e., average values). The
        interpolation kernel changes the basis of the interpolation.
        """
    )

    leaf_size = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _leaf_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLeafSize,
                        self.leaf_size)

    number_of_points_per_bin = traits.Trait(10, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the average number of points in each bin. Larger values
        result in higher rates of subsampling. This data member is used
        when the configuration style is set to AUTOMATIC. The class will
        automatically determine the binning dimensions in the x-y-z
        directions.
        """
    )

    def _number_of_points_per_bin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPointsPerBin,
                        self.number_of_points_per_bin)

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
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('configuration_style', 'GetConfigurationStyle'), ('divisions',
    'GetDivisions'), ('leaf_size', 'GetLeafSize'),
    ('number_of_points_per_bin', 'GetNumberOfPointsPerBin'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'configuration_style', 'divisions', 'leaf_size',
    'number_of_points_per_bin', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VoxelGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit VoxelGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['configuration_style'], ['divisions', 'leaf_size',
            'number_of_points_per_bin']),
            title='Edit VoxelGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VoxelGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


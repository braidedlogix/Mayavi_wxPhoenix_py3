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


class EuclideanClusterExtraction(PolyDataAlgorithm):
    """
    EuclideanClusterExtraction - perform segmentation based on
    geometric proximity and optional scalar threshold
    
    Superclass: PolyDataAlgorithm
    
    EuclideanClusterExtraction is a filter that extracts points that
    are in close geometric proximity, and optionally satisfies a scalar
    threshold criterion. (Points extracted in this way are referred to as
    clusters.) The filter works in one of five ways: 1) extract the
    largest cluster in the dataset; 2) extract specified cluster
    number(s); 3) extract all clusters containing specified point ids; 4)
    extract the cluster closest to a specified point; or 5) extract all
    clusters (which can be used for coloring the clusters).
    
    Note that geometric proximity is defined by setting the Radius
    instance variable. This variable defines a local sphere around each
    point; other points contained in this sphere are considered
    "connected" to the point. Setting this number too large will connect
    clusters that should not be; setting it too small will fragment the
    point cloud into myriad clusters. To accelerate the geometric
    proximity operations, a point locator may be specified. By default, a
    StaticPointLocator is used, but any AbstractPointLocator may be
    specified.
    
    The behavior of EuclideanClusterExtraction can be modified by
    turning on the boolean ivar scalar_connectivity. If this flag is on,
    the clustering algorithm is modified so that points are considered
    part of a cluster if they satisfy both the geometric proximity
    measure, and the points scalar values falls into the scalar range
    specified. This use of scalar_connectivity is particularly useful for
    data with intensity or color information, serving as a simple "connected
    segmentation" algorithm. For example, by using a seed point in a
    known cluster, clustering will pull out all points "representing" the
    local structure.
    
    @sa
    ConnectivityFilter PolyDataConnectivityFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEuclideanClusterExtraction, obj, update, **traits)
    
    color_clusters = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the coloring of connected clusters.
        """
    )

    def _color_clusters_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorClusters,
                        self.color_clusters_)

    scalar_connectivity = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off connectivity based on scalar value. If on, points are
        connected only if the are proximal AND the scalar value of a
        candiate point falls in the scalar range specified. Of course
        input point scalar data must be provided.
        """
    )

    def _scalar_connectivity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarConnectivity,
                        self.scalar_connectivity_)

    extraction_mode = traits.Trait('largest_cluster',
    tvtk_base.TraitRevPrefixMap({'largest_cluster': 3, 'all_clusters': 4, 'closest_point_cluster': 5, 'point_seeded_clusters': 1, 'specified_clusters': 2}), help=\
        """
        Control the extraction of connected surfaces.
        """
    )

    def _extraction_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtractionMode,
                        self.extraction_mode_)

    closest_point = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _closest_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClosestPoint,
                        self.closest_point)

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
        used. The locator performs efficient proximity searches near a
        specified interpolation position.
        """
    )

    radius = traits.Trait(0.0, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Specify the local search radius.
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    scalar_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 1.0), cols=2, help=\
        """
        
        """
    )

    def _scalar_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarRange,
                        self.scalar_range)

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

    def _get_number_of_extracted_clusters(self):
        return self._vtk_obj.GetNumberOfExtractedClusters()
    number_of_extracted_clusters = traits.Property(_get_number_of_extracted_clusters, help=\
        """
        Obtain the number of connected clusters. This value is valid only
        after filter execution.
        """
    )

    def add_seed(self, *args):
        """
        V.add_seed(int)
        C++: void AddSeed(IdType id)
        Add a seed id (point id). Note: ids are 0-offset.
        """
        ret = self._wrap_call(self._vtk_obj.AddSeed, *args)
        return ret

    def add_specified_cluster(self, *args):
        """
        V.add_specified_cluster(int)
        C++: void AddSpecifiedCluster(int id)
        Add a cluster id to extract. Note: ids are 0-offset.
        """
        ret = self._wrap_call(self._vtk_obj.AddSpecifiedCluster, *args)
        return ret

    def delete_seed(self, *args):
        """
        V.delete_seed(int)
        C++: void DeleteSeed(IdType id)
        Delete a seed id.a
        """
        ret = self._wrap_call(self._vtk_obj.DeleteSeed, *args)
        return ret

    def delete_specified_cluster(self, *args):
        """
        V.delete_specified_cluster(int)
        C++: void DeleteSpecifiedCluster(int id)
        Delete a cluster id to extract.
        """
        ret = self._wrap_call(self._vtk_obj.DeleteSpecifiedCluster, *args)
        return ret

    def initialize_seed_list(self):
        """
        V.initialize_seed_list()
        C++: void InitializeSeedList()
        Initialize the list of point ids used to seed clusters.
        """
        ret = self._vtk_obj.InitializeSeedList()
        return ret
        

    def initialize_specified_cluster_list(self):
        """
        V.initialize_specified_cluster_list()
        C++: void InitializeSpecifiedClusterList()
        Initialize the list of cluster ids to extract.
        """
        ret = self._vtk_obj.InitializeSpecifiedClusterList()
        return ret
        

    _updateable_traits_ = \
    (('color_clusters', 'GetColorClusters'), ('scalar_connectivity',
    'GetScalarConnectivity'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('extraction_mode', 'GetExtractionMode'), ('closest_point',
    'GetClosestPoint'), ('radius', 'GetRadius'), ('scalar_range',
    'GetScalarRange'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'color_clusters', 'debug',
    'global_warning_display', 'release_data_flag', 'scalar_connectivity',
    'extraction_mode', 'closest_point', 'progress_text', 'radius',
    'scalar_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EuclideanClusterExtraction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit EuclideanClusterExtraction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['color_clusters', 'scalar_connectivity'], ['extraction_mode'],
            ['closest_point', 'radius', 'scalar_range']),
            title='Edit EuclideanClusterExtraction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EuclideanClusterExtraction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


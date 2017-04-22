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


class PolyDataConnectivityFilter(PolyDataAlgorithm):
    """
    PolyDataConnectivityFilter - extract polygonal data based on
    geometric connectivity
    
    Superclass: PolyDataAlgorithm
    
    PolyDataConnectivityFilter is a filter that extracts cells that
    share common points and/or satisfy a scalar threshold criterion.
    (Such a group of cells is called a region.) The filter works in one
    of six ways: 1) extract the largest (most points) connected region in
    the dataset; 2) extract specified region numbers; 3) extract all
    regions sharing specified point ids; 4) extract all regions sharing
    specified cell ids; 5) extract the region closest to the specified
    point; or 6) extract all regions (used to color regions).
    
    This filter is specialized for polygonal data. This means it runs a
    bit faster and is easier to construct visualization networks that
    process polygonal data.
    
    The behavior of PolyDataConnectivityFilter can be modified by
    turning on the boolean ivar scalar_connectivity. If this flag is on,
    the connectivity algorithm is modified so that cells are considered
    connected only if 1) they are geometrically connected (share a point)
    and 2) the scalar values of the cell's points falls in the scalar
    range specified. If scalar_connectivity and full_scalar_connectivity is
    ON, all the cell's points must lie in the scalar range specified for
    the cell to qualify as being connected. If full_scalar_connectivity is
    OFF, any one of the cell's points may lie in the user specified
    scalar range for the cell to qualify as being connected.
    
    This use of scalar_connectivity is particularly useful for selecting
    cells for later processing.
    
    @sa
    ConnectivityFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyDataConnectivityFilter, obj, update, **traits)
    
    color_regions = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the coloring of connected regions.
        """
    )

    def _color_regions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorRegions,
                        self.color_regions_)

    full_scalar_connectivity = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the use of Fully connected scalar connectivity. This
        is off by default. The flag is used only if scalar_connectivity is
        on. If full_scalar_connectivity is ON, all the cell's points must
        lie in the scalar range specified for the cell to qualify as
        being connected. If full_scalar_connectivity is OFF, any one of the
        cell's points may lie in the user specified scalar range for the
        cell to qualify as being connected.
        """
    )

    def _full_scalar_connectivity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFullScalarConnectivity,
                        self.full_scalar_connectivity_)

    mark_visited_point_ids = tvtk_base.false_bool_trait(help=\
        """
        Mark visited point ids ? It may be useful to extract the visited
        point ids for use by a downstream filter. Default is OFF.
        """
    )

    def _mark_visited_point_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMarkVisitedPointIds,
                        self.mark_visited_point_ids_)

    scalar_connectivity = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off connectivity based on scalar value. If on, cells are
        connected only if they share points AND one of the cells scalar
        values falls in the scalar range specified.
        """
    )

    def _scalar_connectivity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarConnectivity,
                        self.scalar_connectivity_)

    extraction_mode = traits.Trait('largest_region',
    tvtk_base.TraitRevPrefixMap({'largest_region': 4, 'all_regions': 5, 'cell_seeded_regions': 2, 'closest_point_region': 6, 'point_seeded_regions': 1, 'specified_regions': 3}), help=\
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

    def _get_number_of_extracted_regions(self):
        return self._vtk_obj.GetNumberOfExtractedRegions()
    number_of_extracted_regions = traits.Property(_get_number_of_extracted_regions, help=\
        """
        Obtain the number of connected regions.
        """
    )

    def _get_region_sizes(self):
        return wrap_vtk(self._vtk_obj.GetRegionSizes())
    region_sizes = traits.Property(_get_region_sizes, help=\
        """
        Obtain the array containing the region sizes of the extracted
        regions
        """
    )

    def _get_visited_point_ids(self):
        return wrap_vtk(self._vtk_obj.GetVisitedPointIds())
    visited_point_ids = traits.Property(_get_visited_point_ids, help=\
        """
        Get the visited point ids. This is valid only if
        mark_visited_point_ids has been set.
        """
    )

    def add_seed(self, *args):
        """
        V.add_seed(int)
        C++: void AddSeed(int id)
        Add a seed id (point or cell id). Note: ids are 0-offset.
        """
        ret = self._wrap_call(self._vtk_obj.AddSeed, *args)
        return ret

    def add_specified_region(self, *args):
        """
        V.add_specified_region(int)
        C++: void AddSpecifiedRegion(int id)
        Add a region id to extract. Note: ids are 0-offset.
        """
        ret = self._wrap_call(self._vtk_obj.AddSpecifiedRegion, *args)
        return ret

    def delete_seed(self, *args):
        """
        V.delete_seed(int)
        C++: void DeleteSeed(int id)
        Delete a seed id (point or cell id). Note: ids are 0-offset.
        """
        ret = self._wrap_call(self._vtk_obj.DeleteSeed, *args)
        return ret

    def delete_specified_region(self, *args):
        """
        V.delete_specified_region(int)
        C++: void DeleteSpecifiedRegion(int id)
        Delete a region id to extract. Note: ids are 0-offset.
        """
        ret = self._wrap_call(self._vtk_obj.DeleteSpecifiedRegion, *args)
        return ret

    def initialize_seed_list(self):
        """
        V.initialize_seed_list()
        C++: void InitializeSeedList()
        Initialize list of point ids/cell ids used to seed regions.
        """
        ret = self._vtk_obj.InitializeSeedList()
        return ret
        

    def initialize_specified_region_list(self):
        """
        V.initialize_specified_region_list()
        C++: void InitializeSpecifiedRegionList()
        Initialize list of region ids to extract.
        """
        ret = self._vtk_obj.InitializeSpecifiedRegionList()
        return ret
        

    _updateable_traits_ = \
    (('color_regions', 'GetColorRegions'), ('full_scalar_connectivity',
    'GetFullScalarConnectivity'), ('mark_visited_point_ids',
    'GetMarkVisitedPointIds'), ('scalar_connectivity',
    'GetScalarConnectivity'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('extraction_mode', 'GetExtractionMode'), ('closest_point',
    'GetClosestPoint'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('scalar_range', 'GetScalarRange'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'color_regions', 'debug',
    'full_scalar_connectivity', 'global_warning_display',
    'mark_visited_point_ids', 'release_data_flag', 'scalar_connectivity',
    'extraction_mode', 'closest_point', 'output_points_precision',
    'progress_text', 'scalar_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyDataConnectivityFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyDataConnectivityFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['color_regions', 'full_scalar_connectivity',
            'mark_visited_point_ids', 'scalar_connectivity'], ['extraction_mode'],
            ['closest_point', 'output_points_precision', 'scalar_range']),
            title='Edit PolyDataConnectivityFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyDataConnectivityFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


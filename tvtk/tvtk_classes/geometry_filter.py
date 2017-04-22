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


class GeometryFilter(PolyDataAlgorithm):
    """
    GeometryFilter - extract geometry from data (or convert data to
    polygonal type)
    
    Superclass: PolyDataAlgorithm
    
    GeometryFilter is a general-purpose filter to extract geometry
    (and associated data) from any type of dataset. Geometry is obtained
    as follows: all 0d, 1d, and 2d cells are extracted. All 2d faces that
    are used by only one 3d cell (i.e., boundary faces) are extracted. It
    also is possible to specify conditions on point ids, cell ids, and on
    bounding box (referred to as "Extent") to control the extraction
    process.
    
    This filter also may be used to convert any type of data to polygonal
    type. The conversion process may be less than satisfactory for some
    3d datasets. For example, this filter will extract the outer surface
    of a volume or structured grid dataset. (For structured data you may
    want to use ImageDataGeometryFilter,
    StructuredGridGeometryFilter, ExtractUnstructuredGrid,
    RectilinearGridGeometryFilter, or ExtractVOI.)
    
    @warning
    When GeometryFilter extracts cells (or boundaries of cells) it
    will (by default) merge duplicate vertices. This may cause problems
    in some cases. For example, if you've run PolyDataNormals to
    generate normals, which may split meshes and create duplicate
    vertices, GeometryFilter will merge these points back together.
    Turn merging off to prevent this from occurring.
    
    @warning
    This filter assumes that the input dataset is composed of either: 0d
    cells OR 1d cells OR 2d and/or 3d cells. In other words, the input
    dataset cannot be a combination of different dimensional cells with
    the exception of 2d and 3d cells.
    
    @sa
    ImageDataGeometryFilter StructuredGridGeometryFilter
    ExtractGeometry ExtractVOI
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeometryFilter, obj, update, **traits)
    
    cell_clipping = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off selection of geometry by cell id.
        """
    )

    def _cell_clipping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellClipping,
                        self.cell_clipping_)

    extent_clipping = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off selection of geometry via bounding box.
        """
    )

    def _extent_clipping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtentClipping,
                        self.extent_clipping_)

    merging = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off merging of coincident points. Note that is merging is
        on, points with different point attributes (e.g., normals) are
        merged, which may cause rendering artifacts.
        """
    )

    def _merging_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMerging,
                        self.merging_)

    point_clipping = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off selection of geometry by point id.
        """
    )

    def _point_clipping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointClipping,
                        self.point_clipping_)

    cell_maximum = traits.Trait(9223372036854775807, traits.Range(0, 9223372036854775807, enter_set=True, auto_set=False), help=\
        """
        Specify the maximum cell id for point id selection.
        """
    )

    def _cell_maximum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellMaximum,
                        self.cell_maximum)

    cell_minimum = traits.Trait(0, traits.Range(0, 9223372036854775807, enter_set=True, auto_set=False), help=\
        """
        Specify the minimum cell id for point id selection.
        """
    )

    def _cell_minimum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellMinimum,
                        self.cell_minimum)

    extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(-1e+299, 1e+299, -1e+299, 1e+299, -1e+299, 1e+299), cols=3, help=\
        """
        Specify a (xmin,xmax, ymin,ymax, zmin,zmax) bounding box to clip
        data.
        """
    )

    def _extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtent,
                        self.extent)

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Set / get a spatial locator for merging points. By default an
        instance of MergePoints is used.
        """
    )

    point_maximum = traits.Trait(9223372036854775807, traits.Range(0, 9223372036854775807, enter_set=True, auto_set=False), help=\
        """
        Specify the maximum point id for point id selection.
        """
    )

    def _point_maximum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointMaximum,
                        self.point_maximum)

    point_minimum = traits.Trait(0, traits.Range(0, 9223372036854775807, enter_set=True, auto_set=False), help=\
        """
        Specify the minimum point id for point id selection.
        """
    )

    def _point_minimum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointMinimum,
                        self.point_minimum)

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

    def create_default_locator(self):
        """
        V.create_default_locator()
        C++: void CreateDefaultLocator()
        Create default locator. Used to create one when none is
        specified.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

    _updateable_traits_ = \
    (('cell_clipping', 'GetCellClipping'), ('extent_clipping',
    'GetExtentClipping'), ('merging', 'GetMerging'), ('point_clipping',
    'GetPointClipping'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('cell_maximum', 'GetCellMaximum'), ('cell_minimum',
    'GetCellMinimum'), ('extent', 'GetExtent'), ('point_maximum',
    'GetPointMaximum'), ('point_minimum', 'GetPointMinimum'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'cell_clipping', 'debug', 'extent_clipping',
    'global_warning_display', 'merging', 'point_clipping',
    'release_data_flag', 'cell_maximum', 'cell_minimum', 'extent',
    'point_maximum', 'point_minimum', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeometryFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['cell_clipping', 'extent_clipping', 'merging',
            'point_clipping'], [], ['cell_maximum', 'cell_minimum', 'extent',
            'point_maximum', 'point_minimum']),
            title='Edit GeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.unstructured_grid_base_algorithm import UnstructuredGridBaseAlgorithm


class UnstructuredGridGeometryFilter(UnstructuredGridBaseAlgorithm):
    """
    UnstructuredGridGeometryFilter - extract geometry from an
    unstructured grid
    
    Superclass: UnstructuredGridBaseAlgorithm
    
    UnstructuredGridGeometryFilter is a filter that extracts geometry
    (and associated data) from an unstructured grid. It differs from
    GeometryFilter by not tessellating higher order faces: 2d faces of
    quadratic 3d cells will be quadratic. A quadratic edge is extracted
    as a quadratic edge. For that purpose, the output of this filter is
    an unstructured grid, not a polydata. Also, the face of a voxel is a
    pixel, not a quad. Geometry is obtained as follows: all 0d, 1d, and
    2d cells are extracted. All 2d faces that are used by only one 3d
    cell (i.e., boundary faces) are extracted. It also is possible to
    specify conditions on point ids, cell ids, and on bounding box
    (referred to as "Extent") to control the extraction process.
    
    @warning
    When UnstructuredGridGeometryFilter extracts cells (or boundaries
    of cells) it will (by default) merge duplicate vertices. This may
    cause problems in some cases. Turn merging off to prevent this from
    occurring.
    
    @sa
    GeometryFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGridGeometryFilter, obj, update, **traits)
    
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

    pass_through_cell_ids = tvtk_base.false_bool_trait(help=\
        """
        If on, the output polygonal dataset will have a celldata array
        that holds the cell index of the original 3d cell that produced
        each output cell. This is useful for cell picking. The default is
        off to conserve memory. Note that pass_through_cell_ids will be
        ignored if use_strips is on, since in that case each tringle strip
        can represent more than on of the input cells.
        """
    )

    def _pass_through_cell_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassThroughCellIds,
                        self.pass_through_cell_ids_)

    pass_through_point_ids = tvtk_base.false_bool_trait(help=\
        """
        If on, the output polygonal dataset will have a celldata array
        that holds the cell index of the original 3d cell that produced
        each output cell. This is useful for cell picking. The default is
        off to conserve memory. Note that pass_through_cell_ids will be
        ignored if use_strips is on, since in that case each tringle strip
        can represent more than on of the input cells.
        """
    )

    def _pass_through_point_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassThroughPointIds,
                        self.pass_through_point_ids_)

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

    extent = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(6,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
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

    original_cell_ids_name = traits.String('vtkOriginalCellIds', enter_set=True, auto_set=False, help=\
        """
        If pass_through_cell_ids or pass_through_point_ids is on, then these
        ivars control the name given to the field in which the ids are
        written into.  If set to NULL, then OriginalCellIds or
        OriginalPointIds (the default) is used, respectively.
        """
    )

    def _original_cell_ids_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginalCellIdsName,
                        self.original_cell_ids_name)

    original_point_ids_name = traits.String('vtkOriginalPointIds', enter_set=True, auto_set=False, help=\
        """
        If pass_through_cell_ids or pass_through_point_ids is on, then these
        ivars control the name given to the field in which the ids are
        written into.  If set to NULL, then OriginalCellIds or
        OriginalPointIds (the default) is used, respectively.
        """
    )

    def _original_point_ids_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginalPointIdsName,
                        self.original_point_ids_name)

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
    'GetExtentClipping'), ('merging', 'GetMerging'),
    ('pass_through_cell_ids', 'GetPassThroughCellIds'),
    ('pass_through_point_ids', 'GetPassThroughPointIds'),
    ('point_clipping', 'GetPointClipping'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('cell_maximum', 'GetCellMaximum'),
    ('cell_minimum', 'GetCellMinimum'), ('original_cell_ids_name',
    'GetOriginalCellIdsName'), ('original_point_ids_name',
    'GetOriginalPointIdsName'), ('point_maximum', 'GetPointMaximum'),
    ('point_minimum', 'GetPointMinimum'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'cell_clipping', 'debug', 'extent_clipping',
    'global_warning_display', 'merging', 'pass_through_cell_ids',
    'pass_through_point_ids', 'point_clipping', 'release_data_flag',
    'cell_maximum', 'cell_minimum', 'original_cell_ids_name',
    'original_point_ids_name', 'point_maximum', 'point_minimum',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UnstructuredGridGeometryFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGridGeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['cell_clipping', 'extent_clipping', 'merging',
            'pass_through_cell_ids', 'pass_through_point_ids', 'point_clipping'],
            [], ['cell_maximum', 'cell_minimum', 'original_cell_ids_name',
            'original_point_ids_name', 'point_maximum', 'point_minimum']),
            title='Edit UnstructuredGridGeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGridGeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


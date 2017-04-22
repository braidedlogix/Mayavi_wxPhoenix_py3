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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class ExtractUnstructuredGrid(UnstructuredGridAlgorithm):
    """
    ExtractUnstructuredGrid - extract subset of unstructured grid
    geometry
    
    Superclass: UnstructuredGridAlgorithm
    
    ExtractUnstructuredGrid is a general-purpose filter to extract
    geometry (and associated data) from an unstructured grid dataset. The
    extraction process is controlled by specifying a range of point ids,
    cell ids, or a bounding box (referred to as "Extent"). Those cells
    laying within these regions are sent to the output. The user has the
    choice of merging coincident points (Merging is on) or using the
    original point set (Merging is off).
    
    @warning
    If merging is off, the input points are copied through to the output.
    This means unused points may be present in the output data. If
    merging is on, then coincident points with different point attribute
    values are merged.
    
    @sa
    ImageDataGeometryFilter StructuredGridGeometryFilter
    RectilinearGridGeometryFilter ExtractGeometry ExtractVOI
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractUnstructuredGrid, obj, update, **traits)
    
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

    merging = tvtk_base.false_bool_trait(help=\
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
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()"""
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
            return super(ExtractUnstructuredGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractUnstructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['cell_clipping', 'extent_clipping', 'merging',
            'point_clipping'], [], ['cell_maximum', 'cell_minimum', 'extent',
            'point_maximum', 'point_minimum']),
            title='Edit ExtractUnstructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractUnstructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


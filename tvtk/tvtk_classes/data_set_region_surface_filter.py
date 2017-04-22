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

from tvtk.tvtk_classes.data_set_surface_filter import DataSetSurfaceFilter


class DataSetRegionSurfaceFilter(DataSetSurfaceFilter):
    """
    DataSetRegionSurfaceFilter - Extract surface of materials.
    
    Superclass: DataSetSurfaceFilter
    
    This filter extracts surfaces of materials such that a surface could
    have a material on each side of it. It also stores a mapping of the
    original cells and their sides back to the original grid so that we
    can output boundary information for those cells given only surfaces.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataSetRegionSurfaceFilter, obj, update, **traits)
    
    interface_i_ds_name = traits.String('interface_ids', enter_set=True, auto_set=False, help=\
        """
        The name of the field array that has material interface type
        identifiers in it Default is "interface_ids"
        """
    )

    def _interface_i_ds_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterfaceIDsName,
                        self.interface_i_ds_name)

    material_i_ds_name = traits.String('material_ids', enter_set=True, auto_set=False, help=\
        """
        The name of the field array that has material type identifiers in
        it Default is "material_ids"
        """
    )

    def _material_i_ds_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaterialIDsName,
                        self.material_i_ds_name)

    material_pi_ds_name = traits.String('material_ancestors', enter_set=True, auto_set=False, help=\
        """
        The name of the output field array that records parent materials
        of each interface Default is "material_ancestors"
        """
    )

    def _material_pi_ds_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaterialPIDsName,
                        self.material_pi_ds_name)

    material_properties_name = traits.String('material_properties', enter_set=True, auto_set=False, help=\
        """
        The name of the field array that has characteristics of each
        material Default is "material_properties"
        """
    )

    def _material_properties_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaterialPropertiesName,
                        self.material_properties_name)

    region_array_name = traits.String('material', enter_set=True, auto_set=False, help=\
        """
        The name of the cell based array that we use to extract
        interfaces from Default is "Regions"
        """
    )

    def _region_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRegionArrayName,
                        self.region_array_name)

    single_sided = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Whether to return single sided material interfaces or double
        sided Default is single
        """
    )

    def _single_sided_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSingleSided,
                        self.single_sided)

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

    def record_orig_cell_id(self, *args):
        """
        V.record_orig_cell_id(int, int)
        C++: void RecordOrigCellId(IdType newIndex, IdType origId)"""
        ret = self._wrap_call(self._vtk_obj.RecordOrigCellId, *args)
        return ret

    _updateable_traits_ = \
    (('pass_through_cell_ids', 'GetPassThroughCellIds'),
    ('pass_through_point_ids', 'GetPassThroughPointIds'), ('use_strips',
    'GetUseStrips'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('interface_i_ds_name', 'GetInterfaceIDsName'), ('material_i_ds_name',
    'GetMaterialIDsName'), ('material_pi_ds_name', 'GetMaterialPIDsName'),
    ('material_properties_name', 'GetMaterialPropertiesName'),
    ('region_array_name', 'GetRegionArrayName'), ('single_sided',
    'GetSingleSided'), ('nonlinear_subdivision_level',
    'GetNonlinearSubdivisionLevel'), ('original_cell_ids_name',
    'GetOriginalCellIdsName'), ('original_point_ids_name',
    'GetOriginalPointIdsName'), ('piece_invariant', 'GetPieceInvariant'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'pass_through_cell_ids', 'pass_through_point_ids',
    'release_data_flag', 'use_strips', 'interface_i_ds_name',
    'material_i_ds_name', 'material_pi_ds_name',
    'material_properties_name', 'nonlinear_subdivision_level',
    'original_cell_ids_name', 'original_point_ids_name',
    'piece_invariant', 'progress_text', 'region_array_name',
    'single_sided'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataSetRegionSurfaceFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DataSetRegionSurfaceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['pass_through_cell_ids', 'pass_through_point_ids',
            'use_strips'], [], ['interface_i_ds_name', 'material_i_ds_name',
            'material_pi_ds_name', 'material_properties_name',
            'nonlinear_subdivision_level', 'original_cell_ids_name',
            'original_point_ids_name', 'piece_invariant', 'region_array_name',
            'single_sided']),
            title='Edit DataSetRegionSurfaceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataSetRegionSurfaceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


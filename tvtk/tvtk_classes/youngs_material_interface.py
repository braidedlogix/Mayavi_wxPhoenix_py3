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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class YoungsMaterialInterface(MultiBlockDataSetAlgorithm):
    """
    YoungsMaterialInterface - reconstructs material interfaces
    
    Superclass: MultiBlockDataSetAlgorithm
    
    Reconstructs material interfaces from a mesh containing mixed cells
    (where several materials are mixed) this implementation is based on
    the youngs algorithm, generalized to arbitrary cell types and works
    on both 2d and 3d meshes. the main advantage of the youngs algorithm
    is it guarantees the material volume correctness. for 2d meshes, the
    axis_symetric flag allows to switch between a pure 2d (planar)
    algorithm and an axis symetric 2d algorithm handling volumes of
    revolution.
    
    @par Thanks: This file is part of the generalized Youngs material
    interface reconstruction algorithm contributed by
    
    CEA/DIF - Commissariat a l'Energie Atomique, Centre DAM Ile-De-France
    
    BP12, F-91297 Arpajon, France.
    
    Implementation by Thierry Carrard (thierry.carrard@cea.fr)
    Modification by Philippe Pebay (philippe.pebay@kitware.com)
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkYoungsMaterialInterface, obj, update, **traits)
    
    axis_symetric = tvtk_base.false_bool_trait(help=\
        """
        Turns on/off axis_symetric computation of 2d interfaces. in axis
        symetric mode, 2d meshes are understood as volumes of revolution.
        """
    )

    def _axis_symetric_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisSymetric,
                        self.axis_symetric_)

    fill_material = tvtk_base.false_bool_trait(help=\
        """
        When fill_material is set to 1, the volume containing material is
        output and not only the interface surface.
        """
    )

    def _fill_material_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFillMaterial,
                        self.fill_material_)

    inverse_normal = tvtk_base.false_bool_trait(help=\
        """
        Set/Get wether the normal vector has to be flipped.
        """
    )

    def _inverse_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInverseNormal,
                        self.inverse_normal_)

    onion_peel = tvtk_base.false_bool_trait(help=\
        """
        Set/Get onion_peel flag. if this flag is on, the normal vector of
        the first material (which depends on material ordering) is used
        for all materials.
        """
    )

    def _onion_peel_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOnionPeel,
                        self.onion_peel_)

    reverse_material_order = tvtk_base.false_bool_trait(help=\
        """
        If this flag is on, material order in reversed. Otherwise,
        materials are sorted in ascending order depending on the given
        ordering array.
        """
    )

    def _reverse_material_order_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReverseMaterialOrder,
                        self.reverse_material_order_)

    use_all_blocks = tvtk_base.true_bool_trait(help=\
        """
        Set/Get whether all material blocks should be used, irrespective
        of the material block mapping.
        """
    )

    def _use_all_blocks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseAllBlocks,
                        self.use_all_blocks_)

    use_fraction_as_distance = tvtk_base.false_bool_trait(help=\
        """
        when use_fraction_as_distance is true, the volume fraction is
        interpreted as the distance of the cutting plane from the origin.
        in axis symetric mode, 2d meshes are understood as volumes of
        revolution.
        """
    )

    def _use_fraction_as_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseFractionAsDistance,
                        self.use_fraction_as_distance_)

    number_of_materials = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Sets/Gets the number of materials.
        """
    )

    def _number_of_materials_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfMaterials,
                        self.number_of_materials)

    volume_fraction_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.01, 0.99), cols=2, help=\
        """
        
        """
    )

    def _volume_fraction_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVolumeFractionRange,
                        self.volume_fraction_range)

    def _get_number_of_domains(self):
        return self._vtk_obj.GetNumberOfDomains()
    number_of_domains = traits.Property(_get_number_of_domains, help=\
        """
        Only meaningfull for LOVE software. returns the maximum number of
        blocks conatining the same material
        """
    )

    def add_material_block_mapping(self, *args):
        """
        V.add_material_block_mapping(int)
        C++: virtual void AddMaterialBlockMapping(int b)
        select blocks to be processed for each described material.
        """
        ret = self._wrap_call(self._vtk_obj.AddMaterialBlockMapping, *args)
        return ret

    def remove_all_material_block_mappings(self):
        """
        V.remove_all_material_block_mappings()
        C++: virtual void RemoveAllMaterialBlockMappings()
        select blocks to be processed for each described material.
        """
        ret = self._vtk_obj.RemoveAllMaterialBlockMappings()
        return ret
        

    def remove_all_materials(self):
        """
        V.remove_all_materials()
        C++: virtual void RemoveAllMaterials()
        Removes all meterials previously added.
        """
        ret = self._vtk_obj.RemoveAllMaterials()
        return ret
        

    def set_material_arrays(self, *args):
        """
        V.set_material_arrays(int, string, string, string, string, string)
        C++: virtual void SetMaterialArrays(int i, const char *volume,
            const char *normalX, const char *normalY, const char *normalZ,
             const char *ordering)
        V.set_material_arrays(int, string, string, string)
        C++: virtual void SetMaterialArrays(int i, const char *volume,
            const char *normal, const char *ordering)
        Set ith Material arrays to be used as volume fraction, interface
        normal and material ordering. Each parameter name a cell array.
        """
        ret = self._wrap_call(self._vtk_obj.SetMaterialArrays, *args)
        return ret

    def set_material_normal_array(self, *args):
        """
        V.set_material_normal_array(int, string)
        C++: virtual void SetMaterialNormalArray(int i,
            const char *normal)
        V.set_material_normal_array(string, string)
        C++: virtual void SetMaterialNormalArray(const char *volume,
            const char *normal)
        Set ith Material arrays to be used as volume fraction, interface
        normal and material ordering. Each parameter name a cell array.
        """
        ret = self._wrap_call(self._vtk_obj.SetMaterialNormalArray, *args)
        return ret

    def set_material_ordering_array(self, *args):
        """
        V.set_material_ordering_array(int, string)
        C++: virtual void SetMaterialOrderingArray(int i,
            const char *ordering)
        V.set_material_ordering_array(string, string)
        C++: virtual void SetMaterialOrderingArray(const char *volume,
            const char *ordering)
        Set ith Material arrays to be used as volume fraction, interface
        normal and material ordering. Each parameter name a cell array.
        """
        ret = self._wrap_call(self._vtk_obj.SetMaterialOrderingArray, *args)
        return ret

    def set_material_volume_fraction_array(self, *args):
        """
        V.set_material_volume_fraction_array(int, string)
        C++: virtual void SetMaterialVolumeFractionArray(int i,
            const char *volume)
        Set ith Material arrays to be used as volume fraction, interface
        normal and material ordering. Each parameter name a cell array.
        """
        ret = self._wrap_call(self._vtk_obj.SetMaterialVolumeFractionArray, *args)
        return ret

    _updateable_traits_ = \
    (('axis_symetric', 'GetAxisSymetric'), ('fill_material',
    'GetFillMaterial'), ('inverse_normal', 'GetInverseNormal'),
    ('onion_peel', 'GetOnionPeel'), ('reverse_material_order',
    'GetReverseMaterialOrder'), ('use_all_blocks', 'GetUseAllBlocks'),
    ('use_fraction_as_distance', 'GetUseFractionAsDistance'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_materials', 'GetNumberOfMaterials'),
    ('volume_fraction_range', 'GetVolumeFractionRange'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'axis_symetric', 'debug', 'fill_material',
    'global_warning_display', 'inverse_normal', 'onion_peel',
    'release_data_flag', 'reverse_material_order', 'use_all_blocks',
    'use_fraction_as_distance', 'number_of_materials', 'progress_text',
    'volume_fraction_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(YoungsMaterialInterface, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit YoungsMaterialInterface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['axis_symetric', 'fill_material', 'inverse_normal',
            'onion_peel', 'reverse_material_order', 'use_all_blocks',
            'use_fraction_as_distance'], [], ['number_of_materials',
            'volume_fraction_range']),
            title='Edit YoungsMaterialInterface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit YoungsMaterialInterface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


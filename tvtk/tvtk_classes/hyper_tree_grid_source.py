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

from tvtk.tvtk_classes.hyper_tree_grid_algorithm import HyperTreeGridAlgorithm


class HyperTreeGridSource(HyperTreeGridAlgorithm):
    """
    HyperTreeGridSource - Create a synthetic grid of hypertrees.
    
    Superclass: HyperTreeGridAlgorithm
    
    This class uses input parameters, most notably a string descriptor,
    to generate a HyperTreeGrid instance representing the
    corresponding tree-based AMR grid. This descriptor uses the following
    conventions, e.g., to describe a 1-D ternary subdivision with 2 root
    cells L0    L1        L2 RR  | .R. ... | ... For this tree:
     HTG:       .
              /   \
     L0:     .     .
            /|\   /|\
     L1:   c . c c c c
            /|\
     L2:   c c c The top level of the tree is not considered a grid level
    NB: For ease of legibility, white spaces are allowed and ignored.
    
    @par Thanks: This class was written by Philippe Pebay and Joachim
    Pouderoux, Kitware 2013 This work was supported in part by
    Commissariat a l'Energie Atomique (CEA/DIF)
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHyperTreeGridSource, obj, update, **traits)
    
    use_descriptor = tvtk_base.true_bool_trait(help=\
        """
        Set/get whether the descriptor string should be used. NB:
        Otherwise a quadric definition is expected. Default: true
        """
    )

    def _use_descriptor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseDescriptor,
                        self.use_descriptor_)

    use_material_mask = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether the material mask should be used. NB: This is
        only used when use_descriptor is ON Default: false
        """
    )

    def _use_material_mask_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseMaterialMask,
                        self.use_material_mask_)

    branch_factor = traits.Trait(2, traits.Range(2, 3, enter_set=True, auto_set=False), help=\
        """
        Set/Get the subdivision factor in the grid refinement scheme
        """
    )

    def _branch_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBranchFactor,
                        self.branch_factor)

    descriptor = traits.String('.', enter_set=True, auto_set=False, help=\
        """
        Set/Get the string used to describe the grid
        """
    )

    def _descriptor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDescriptor,
                        self.descriptor)

    def _get_descriptor_bits(self):
        return wrap_vtk(self._vtk_obj.GetDescriptorBits())
    def _set_descriptor_bits(self, arg):
        old_val = self._get_descriptor_bits()
        my_arg = deref_array([arg], [['vtkBitArray']])
        self._wrap_call(self._vtk_obj.SetDescriptorBits,
                        my_arg[0])
        self.trait_property_changed('descriptor_bits', old_val, arg)
    descriptor_bits = traits.Property(_get_descriptor_bits, _set_descriptor_bits, help=\
        """
        Set/Get the bitarray used to describe the grid
        """
    )

    dimension = traits.Trait(3, traits.Range(2, 3, enter_set=True, auto_set=False), help=\
        """
        Set/Get the dimensionality of the grid
        """
    )

    def _dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimension,
                        self.dimension)

    grid_scale = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _grid_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridScale,
                        self.grid_scale)

    grid_size = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(1, 1, 1), cols=3, help=\
        """
        
        """
    )

    def _grid_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridSize,
                        self.grid_size)

    material_mask = traits.String('0', enter_set=True, auto_set=False, help=\
        """
        Set/Get the string used to as a material mask
        """
    )

    def _material_mask_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaterialMask,
                        self.material_mask)

    def _get_material_mask_bits(self):
        return wrap_vtk(self._vtk_obj.GetMaterialMaskBits())
    def _set_material_mask_bits(self, arg):
        old_val = self._get_material_mask_bits()
        my_arg = deref_array([arg], [['vtkBitArray']])
        self._wrap_call(self._vtk_obj.SetMaterialMaskBits,
                        my_arg[0])
        self.trait_property_changed('material_mask_bits', old_val, arg)
    material_mask_bits = traits.Property(_get_material_mask_bits, _set_material_mask_bits, help=\
        """
        Set/Get the bitarray used as a material mask
        """
    )

    maximum_level = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the maximum number of levels of the hypertree.
        \pre positive_levels: levels>=1
        \post is_set: this->_get_levels()==levels
        """
    )

    def _maximum_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumLevel,
                        self.maximum_level)

    origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    def _get_quadric(self):
        return wrap_vtk(self._vtk_obj.GetQuadric())
    def _set_quadric(self, arg):
        old_val = self._get_quadric()
        self._wrap_call(self._vtk_obj.SetQuadric,
                        deref_vtk(arg))
        self.trait_property_changed('quadric', old_val, arg)
    quadric = traits.Property(_get_quadric, _set_quadric, help=\
        """
        Set/Get the quadric function
        """
    )

    quadric_coefficients = traits.Trait((traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined, traits.Undefined), traits.Array(shape=(10,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3), enter_set=True, auto_set=False, help=\
        """
        Helpers to set/get the 10 coefficients of the quadric function
        """
    )

    def _quadric_coefficients_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuadricCoefficients,
                        self.quadric_coefficients)

    transposed_root_indexing = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Specify whether indexing mode of grid root cells must be
        transposed to x-axis first, z-axis last, instead of the default
        z-axis first, k-axis last
        """
    )

    def _transposed_root_indexing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTransposedRootIndexing,
                        self.transposed_root_indexing)

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

    def convert_descriptor_string_to_bit_array(self, *args):
        """
        V.convert_descriptor_string_to_bit_array(string) -> BitArray
        C++: BitArray *ConvertDescriptorStringToBitArray(
            const std::string &)
        Helpers to convert string descriptors & mask to bit arrays
        """
        ret = self._wrap_call(self._vtk_obj.ConvertDescriptorStringToBitArray, *args)
        return wrap_vtk(ret)

    def convert_material_mask_string_to_bit_array(self, *args):
        """
        V.convert_material_mask_string_to_bit_array(string) -> BitArray
        C++: BitArray *ConvertMaterialMaskStringToBitArray(
            const std::string &)
        Helpers to convert string descriptors & mask to bit arrays
        """
        ret = self._wrap_call(self._vtk_obj.ConvertMaterialMaskStringToBitArray, *args)
        return wrap_vtk(ret)

    def set_indexing_mode_to_ijk(self):
        """
        V.set_indexing_mode_to_ijk()
        C++: void SetIndexingModeToIJK()
        Specify whether indexing mode of grid root cells must be
        transposed to x-axis first, z-axis last, instead of the default
        z-axis first, k-axis last
        """
        ret = self._vtk_obj.SetIndexingModeToIJK()
        return ret
        

    def set_indexing_mode_to_kji(self):
        """
        V.set_indexing_mode_to_kji()
        C++: void SetIndexingModeToKJI()
        Specify whether indexing mode of grid root cells must be
        transposed to x-axis first, z-axis last, instead of the default
        z-axis first, k-axis last
        """
        ret = self._vtk_obj.SetIndexingModeToKJI()
        return ret
        

    def set_level_zero_material_index(self, *args):
        """
        V.set_level_zero_material_index(IdTypeArray)
        C++: virtual void SetLevelZeroMaterialIndex(IdTypeArray *)
        Set the index array used to as a material mask
        """
        my_args = deref_array(args, [['vtkIdTypeArray']])
        ret = self._wrap_call(self._vtk_obj.SetLevelZeroMaterialIndex, *my_args)
        return ret

    _updateable_traits_ = \
    (('use_descriptor', 'GetUseDescriptor'), ('use_material_mask',
    'GetUseMaterialMask'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('branch_factor', 'GetBranchFactor'), ('descriptor', 'GetDescriptor'),
    ('dimension', 'GetDimension'), ('grid_scale', 'GetGridScale'),
    ('grid_size', 'GetGridSize'), ('material_mask', 'GetMaterialMask'),
    ('maximum_level', 'GetMaximumLevel'), ('origin', 'GetOrigin'),
    ('transposed_root_indexing', 'GetTransposedRootIndexing'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'use_descriptor', 'use_material_mask',
    'branch_factor', 'descriptor', 'dimension', 'grid_scale', 'grid_size',
    'material_mask', 'maximum_level', 'origin', 'progress_text',
    'transposed_root_indexing'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HyperTreeGridSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HyperTreeGridSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_descriptor', 'use_material_mask'], [], ['branch_factor',
            'descriptor', 'dimension', 'grid_scale', 'grid_size', 'material_mask',
            'maximum_level', 'origin', 'transposed_root_indexing']),
            title='Edit HyperTreeGridSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HyperTreeGridSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


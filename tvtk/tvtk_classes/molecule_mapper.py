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

from tvtk.tvtk_classes.mapper import Mapper


class MoleculeMapper(Mapper):
    """
    MoleculeMapper - Mapper that draws Molecule objects
    
    Superclass: Mapper
    
    MoleculeMapper uses glyphs (display lists) to quickly render a
    molecule.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMoleculeMapper, obj, update, **traits)
    
    render_atoms = tvtk_base.true_bool_trait(help=\
        """
        Get/Set whether or not to render atoms. Default: On.
        """
    )

    def _render_atoms_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRenderAtoms,
                        self.render_atoms_)

    render_bonds = tvtk_base.true_bool_trait(help=\
        """
        Get/Set whether or not to render bonds. Default: On.
        """
    )

    def _render_bonds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRenderBonds,
                        self.render_bonds_)

    render_lattice = tvtk_base.true_bool_trait(help=\
        """
        Get/Set whether or not to render the unit cell lattice, if
        present. Default: On.
        """
    )

    def _render_lattice_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRenderLattice,
                        self.render_lattice_)

    use_multi_cylinders_for_bonds = tvtk_base.true_bool_trait(help=\
        """
        Get/Set whether multicylinders will be used to represent multiple
        bonds. Default: On.
        """
    )

    def _use_multi_cylinders_for_bonds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseMultiCylindersForBonds,
                        self.use_multi_cylinders_for_bonds_)

    atomic_radius_type = traits.Trait('vdw_radius',
    tvtk_base.TraitRevPrefixMap({'vdw_radius': 1, 'covalent_radius': 0, 'custom_array_radius': 3, 'unit_radius': 2}), help=\
        """
        Get/Set the type of radius used to generate the atoms. Default:
        VDWRadius. If custom_array_radius is used, the vertex_data array
        named 'radii' is used for per-atom radii.
        """
    )

    def _atomic_radius_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAtomicRadiusType,
                        self.atomic_radius_type_)

    bond_color_mode = traits.Trait('discrete_by_atom',
    tvtk_base.TraitRevPrefixMap({'discrete_by_atom': 1, 'single_color': 0}), help=\
        """
        Get/Set the method by which bonds are colored.
        
        * If '_single_color' is used, all bonds will be the same color. Use
        * set_bond_color to set the rgb values used.
        
        * If '_discrete_by_atom' is selected, each bond is colored using the
        * same lookup table as the atoms at each end, with a sharp color
        * boundary at the bond center.
        """
    )

    def _bond_color_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBondColorMode,
                        self.bond_color_mode_)

    atomic_radius_scale_factor = traits.Float(0.30000001192092896, enter_set=True, auto_set=False, help=\
        """
        Get/Set the uniform scaling factor applied to the atoms. This is
        ignored when atomic_radius_type == custom_array_radius. Default: 0.3.
        """
    )

    def _atomic_radius_scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAtomicRadiusScaleFactor,
                        self.atomic_radius_scale_factor)

    bond_color = tvtk_base.vtk_color_trait((50, 50, 50), help=\
        """
        
        """
    )

    def _bond_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBondColor,
                        self.bond_color, False)

    bond_radius = traits.Float(0.07500000298023224, enter_set=True, auto_set=False, help=\
        """
        Get/Set the radius of the bond cylinders. Default: 0.075
        """
    )

    def _bond_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBondRadius,
                        self.bond_radius)

    lattice_color = tvtk_base.vtk_color_trait((255, 255, 255), help=\
        """
        
        """
    )

    def _lattice_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLatticeColor,
                        self.lattice_color, False)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get/Set the input Molecule.
        """
    )

    def get_selected_atoms(self, *args):
        """
        V.get_selected_atoms(Selection, IdTypeArray)
        C++: virtual void GetSelectedAtoms(Selection *selection,
            IdTypeArray *atomIds)
        Extract the ids atoms and/or bonds rendered by this molecule from
        a Selection object. The IdTypeArray
        """
        my_args = deref_array(args, [('vtkSelection', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.GetSelectedAtoms, *my_args)
        return ret

    def get_selected_atoms_and_bonds(self, *args):
        """
        V.get_selected_atoms_and_bonds(Selection, IdTypeArray,
            IdTypeArray)
        C++: virtual void GetSelectedAtomsAndBonds(
            Selection *selection, IdTypeArray *atomIds,
            IdTypeArray *bondIds)
        Extract the ids atoms and/or bonds rendered by this molecule from
        a Selection object. The IdTypeArray
        """
        my_args = deref_array(args, [('vtkSelection', 'vtkIdTypeArray', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.GetSelectedAtomsAndBonds, *my_args)
        return ret

    def get_selected_bonds(self, *args):
        """
        V.get_selected_bonds(Selection, IdTypeArray)
        C++: virtual void GetSelectedBonds(Selection *selection,
            IdTypeArray *bondIds)
        Extract the ids atoms and/or bonds rendered by this molecule from
        a Selection object. The IdTypeArray
        """
        my_args = deref_array(args, [('vtkSelection', 'vtkIdTypeArray')])
        ret = self._wrap_call(self._vtk_obj.GetSelectedBonds, *my_args)
        return ret

    def fill_input_port_information(self, *args):
        """
        V.fill_input_port_information(int, Information) -> int
        C++: virtual int FillInputPortInformation(int port,
            Information *info)
        Reimplemented from base class
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillInputPortInformation, *my_args)
        return ret

    def set_input_data(self, *args):
        """
        V.set_input_data(Molecule)
        C++: void SetInputData(Molecule *in)
        Get/Set the input Molecule.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    def use_ball_and_stick_settings(self):
        """
        V.use_ball_and_stick_settings()
        C++: void UseBallAndStickSettings()
        Set ivars to default ball-and-stick settings. This is equivalent
        to the following:
        - set_render_atoms( true )
        - set_render_bonds( true )
        - set_atomic_radius_type( VDWRadius )
        - set_atomic_radius_scale_factor( 0.3 )
        - set_bond_color_mode( discrete_by_atom )
        - set_use_multi_cylinders_for_bonds( true )
        - set_bond_radius( 0.075 )
        """
        ret = self._vtk_obj.UseBallAndStickSettings()
        return ret
        

    def use_fast_settings(self):
        """
        V.use_fast_settings()
        C++: void UseFastSettings()
        Set ivars to use fast settings that may be useful for rendering
        extremely large molecules where the overall shape is more
        important than the details of the atoms/bond. This is equivalent
        to the following:
        - set_render_atoms( true )
        - set_render_bonds( true )
        - set_atomic_radius_type( unit_radius )
        - set_atomic_radius_scale_factor( 0.60 )
        - set_bond_color_mode( single_color )
        - set_bond_color( 50, 50, 50 )
        - set_use_multi_cylinders_for_bonds( false )
        - set_bond_radius( 0.075 )
        """
        ret = self._vtk_obj.UseFastSettings()
        return ret
        

    def use_liquorice_stick_settings(self):
        """
        V.use_liquorice_stick_settings()
        C++: void UseLiquoriceStickSettings()
        Set ivars to default liquorice stick settings. This is equivalent
        to the following:
        - set_render_atoms( true )
        - set_render_bonds( true )
        - set_atomic_radius_type( unit_radius )
        - set_atomic_radius_scale_factor( 0.1 )
        - set_bond_color_mode( discrete_by_atom )
        - set_use_multi_cylinders_for_bonds( false )
        - set_bond_radius( 0.1 )
        """
        ret = self._vtk_obj.UseLiquoriceStickSettings()
        return ret
        

    def use_vdw_spheres_settings(self):
        """
        V.use_vdw_spheres_settings()
        C++: void UseVDWSpheresSettings()
        Set ivars to default van der Waals spheres settings. This is
        equivalent to the following:
        - set_render_atoms( true )
        - set_render_bonds( true )
        - set_atomic_radius_type( VDWRadius )
        - set_atomic_radius_scale_factor( 1.0 )
        - set_bond_color_mode( discrete_by_atom )
        - set_use_multi_cylinders_for_bonds( true )
        - set_bond_radius( 0.075 )
        """
        ret = self._vtk_obj.UseVDWSpheresSettings()
        return ret
        

    _updateable_traits_ = \
    (('render_atoms', 'GetRenderAtoms'), ('render_bonds',
    'GetRenderBonds'), ('render_lattice', 'GetRenderLattice'),
    ('use_multi_cylinders_for_bonds', 'GetUseMultiCylindersForBonds'),
    ('global_immediate_mode_rendering',
    'GetGlobalImmediateModeRendering'), ('immediate_mode_rendering',
    'GetImmediateModeRendering'), ('interpolate_scalars_before_mapping',
    'GetInterpolateScalarsBeforeMapping'), ('scalar_visibility',
    'GetScalarVisibility'), ('static', 'GetStatic'),
    ('use_lookup_table_scalar_range', 'GetUseLookupTableScalarRange'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('atomic_radius_type', 'GetAtomicRadiusType'), ('bond_color_mode',
    'GetBondColorMode'), ('color_mode', 'GetColorMode'),
    ('resolve_coincident_topology', 'GetResolveCoincidentTopology'),
    ('scalar_material_mode', 'GetScalarMaterialMode'), ('scalar_mode',
    'GetScalarMode'), ('atomic_radius_scale_factor',
    'GetAtomicRadiusScaleFactor'), ('bond_color', 'GetBondColor'),
    ('bond_radius', 'GetBondRadius'), ('lattice_color',
    'GetLatticeColor'), ('field_data_tuple_id', 'GetFieldDataTupleId'),
    ('force_compile_only', 'GetForceCompileOnly'), ('render_time',
    'GetRenderTime'), ('resolve_coincident_topology_polygon_offset_faces',
    'GetResolveCoincidentTopologyPolygonOffsetFaces'),
    ('resolve_coincident_topology_z_shift',
    'GetResolveCoincidentTopologyZShift'), ('scalar_range',
    'GetScalarRange'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_immediate_mode_rendering',
    'global_warning_display', 'immediate_mode_rendering',
    'interpolate_scalars_before_mapping', 'release_data_flag',
    'render_atoms', 'render_bonds', 'render_lattice', 'scalar_visibility',
    'static', 'use_lookup_table_scalar_range',
    'use_multi_cylinders_for_bonds', 'atomic_radius_type',
    'bond_color_mode', 'color_mode', 'resolve_coincident_topology',
    'scalar_material_mode', 'scalar_mode', 'atomic_radius_scale_factor',
    'bond_color', 'bond_radius', 'field_data_tuple_id',
    'force_compile_only', 'lattice_color', 'progress_text', 'render_time',
    'resolve_coincident_topology_polygon_offset_faces',
    'resolve_coincident_topology_z_shift', 'scalar_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MoleculeMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MoleculeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_immediate_mode_rendering', 'immediate_mode_rendering',
            'interpolate_scalars_before_mapping', 'render_atoms', 'render_bonds',
            'render_lattice', 'scalar_visibility', 'static',
            'use_lookup_table_scalar_range', 'use_multi_cylinders_for_bonds'],
            ['atomic_radius_type', 'bond_color_mode', 'color_mode',
            'resolve_coincident_topology', 'scalar_material_mode', 'scalar_mode'],
            ['atomic_radius_scale_factor', 'bond_color', 'bond_radius',
            'field_data_tuple_id', 'force_compile_only', 'lattice_color',
            'render_time', 'resolve_coincident_topology_polygon_offset_faces',
            'resolve_coincident_topology_z_shift', 'scalar_range']),
            title='Edit MoleculeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MoleculeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


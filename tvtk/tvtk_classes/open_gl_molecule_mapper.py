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

from tvtk.tvtk_classes.molecule_mapper import MoleculeMapper


class OpenGLMoleculeMapper(MoleculeMapper):
    """
    OpenGLMoleculeMapper - An accelerated class for rendering molecules
    
    Superclass: MoleculeMapper
    
    A MoleculeMapper that uses imposters to do the rendering. It uses
    OpenGLSphereMapper and OpenGLStickMapper to do the rendering.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLMoleculeMapper, obj, update, **traits)
    
    def _get_fast_atom_mapper(self):
        return wrap_vtk(self._vtk_obj.GetFastAtomMapper())
    fast_atom_mapper = traits.Property(_get_fast_atom_mapper, help=\
        """
        provide access to the underlying mappers
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get/Set the input Molecule.
        """
    )

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
            return super(OpenGLMoleculeMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLMoleculeMapper properties', scrollable=True, resizable=True,
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
            title='Edit OpenGLMoleculeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLMoleculeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


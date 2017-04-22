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

from tvtk.tvtk_classes.glyph3d_mapper import Glyph3DMapper


class OpenGLGlyph3DMapper(Glyph3DMapper):
    """
    OpenGLGlyph3DMapper - OpenGLGlyph3D on the GPU.
    
    Superclass: Glyph3DMapper
    
    Do the same job than Glyph3D but on the GPU. For this reason, it
    is a mapper not a PolyDataAlgorithm. Also, some methods of
    OpenGLGlyph3D don't make sense in OpenGLGlyph3DMapper:
    generate_point_ids, old-style set_source, point_ids_name, is_point_visible.
    
    @sa
    OpenGLGlyph3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLGlyph3DMapper, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input as a DataSet.  This method is overridden in the
        specialized mapper classes to return more specific data types.
        """
    )

    _updateable_traits_ = \
    (('clamping', 'GetClamping'), ('masking', 'GetMasking'),
    ('nested_display_lists', 'GetNestedDisplayLists'), ('orient',
    'GetOrient'), ('scaling', 'GetScaling'), ('source_indexing',
    'GetSourceIndexing'), ('use_selection_ids', 'GetUseSelectionIds'),
    ('global_immediate_mode_rendering',
    'GetGlobalImmediateModeRendering'), ('immediate_mode_rendering',
    'GetImmediateModeRendering'), ('interpolate_scalars_before_mapping',
    'GetInterpolateScalarsBeforeMapping'), ('scalar_visibility',
    'GetScalarVisibility'), ('static', 'GetStatic'),
    ('use_lookup_table_scalar_range', 'GetUseLookupTableScalarRange'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('orientation_mode', 'GetOrientationMode'), ('scale_mode',
    'GetScaleMode'), ('color_mode', 'GetColorMode'),
    ('resolve_coincident_topology', 'GetResolveCoincidentTopology'),
    ('scalar_material_mode', 'GetScalarMaterialMode'), ('scalar_mode',
    'GetScalarMode'), ('range', 'GetRange'), ('scale_factor',
    'GetScaleFactor'), ('selection_color_id', 'GetSelectionColorId'),
    ('field_data_tuple_id', 'GetFieldDataTupleId'), ('force_compile_only',
    'GetForceCompileOnly'), ('render_time', 'GetRenderTime'),
    ('resolve_coincident_topology_polygon_offset_faces',
    'GetResolveCoincidentTopologyPolygonOffsetFaces'),
    ('resolve_coincident_topology_z_shift',
    'GetResolveCoincidentTopologyZShift'), ('scalar_range',
    'GetScalarRange'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'clamping', 'debug',
    'global_immediate_mode_rendering', 'global_warning_display',
    'immediate_mode_rendering', 'interpolate_scalars_before_mapping',
    'masking', 'nested_display_lists', 'orient', 'release_data_flag',
    'scalar_visibility', 'scaling', 'source_indexing', 'static',
    'use_lookup_table_scalar_range', 'use_selection_ids', 'color_mode',
    'orientation_mode', 'resolve_coincident_topology',
    'scalar_material_mode', 'scalar_mode', 'scale_mode',
    'field_data_tuple_id', 'force_compile_only', 'progress_text', 'range',
    'render_time', 'resolve_coincident_topology_polygon_offset_faces',
    'resolve_coincident_topology_z_shift', 'scalar_range', 'scale_factor',
    'selection_color_id'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLGlyph3DMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLGlyph3DMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['clamping', 'global_immediate_mode_rendering',
            'immediate_mode_rendering', 'interpolate_scalars_before_mapping',
            'masking', 'nested_display_lists', 'orient', 'scalar_visibility',
            'scaling', 'source_indexing', 'static',
            'use_lookup_table_scalar_range', 'use_selection_ids'], ['color_mode',
            'orientation_mode', 'resolve_coincident_topology',
            'scalar_material_mode', 'scalar_mode', 'scale_mode'],
            ['field_data_tuple_id', 'force_compile_only', 'range', 'render_time',
            'resolve_coincident_topology_polygon_offset_faces',
            'resolve_coincident_topology_z_shift', 'scalar_range', 'scale_factor',
            'selection_color_id']),
            title='Edit OpenGLGlyph3DMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLGlyph3DMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.open_gl_poly_data_mapper import OpenGLPolyDataMapper


class OpenGLStickMapper(OpenGLPolyDataMapper):
    """
    OpenGLStickMapper - use imposters to draw cylinders
    
    Superclass: OpenGLPolyDataMapper
    
    poly_data_mapper that uses imposters to draw cylinders/sticks for
    ball/stick style molecular rendering. Supports picking.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLStickMapper, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Specify the input data to map.
        """
    )

    def set_orientation_array(self, *args):
        """
        V.set_orientation_array(string)
        C++: void SetOrientationArray(char *)
        Convenience method to set the array to orient with
        """
        ret = self._wrap_call(self._vtk_obj.SetOrientationArray, *args)
        return ret

    def set_scale_array(self, *args):
        """
        V.set_scale_array(string)
        C++: void SetScaleArray(char *)
        Convenience method to set the array to scale with.
        """
        ret = self._wrap_call(self._vtk_obj.SetScaleArray, *args)
        return ret

    def set_selection_id_array(self, *args):
        """
        V.set_selection_id_array(string)
        C++: void SetSelectionIdArray(char *)
        Convenience method to set the array to select with
        """
        ret = self._wrap_call(self._vtk_obj.SetSelectionIdArray, *args)
        return ret

    _updateable_traits_ = \
    (('global_immediate_mode_rendering',
    'GetGlobalImmediateModeRendering'), ('immediate_mode_rendering',
    'GetImmediateModeRendering'), ('interpolate_scalars_before_mapping',
    'GetInterpolateScalarsBeforeMapping'), ('scalar_visibility',
    'GetScalarVisibility'), ('static', 'GetStatic'),
    ('use_lookup_table_scalar_range', 'GetUseLookupTableScalarRange'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('color_mode',
    'GetColorMode'), ('resolve_coincident_topology',
    'GetResolveCoincidentTopology'), ('scalar_material_mode',
    'GetScalarMaterialMode'), ('scalar_mode', 'GetScalarMode'),
    ('cell_id_array_name', 'GetCellIdArrayName'),
    ('composite_id_array_name', 'GetCompositeIdArrayName'),
    ('fragment_shader_code', 'GetFragmentShaderCode'),
    ('geometry_shader_code', 'GetGeometryShaderCode'),
    ('point_id_array_name', 'GetPointIdArrayName'),
    ('populate_selection_settings', 'GetPopulateSelectionSettings'),
    ('process_id_array_name', 'GetProcessIdArrayName'),
    ('vertex_shader_code', 'GetVertexShaderCode'), ('ghost_level',
    'GetGhostLevel'), ('number_of_pieces', 'GetNumberOfPieces'),
    ('number_of_sub_pieces', 'GetNumberOfSubPieces'), ('piece',
    'GetPiece'), ('field_data_tuple_id', 'GetFieldDataTupleId'),
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
    'scalar_visibility', 'static', 'use_lookup_table_scalar_range',
    'color_mode', 'resolve_coincident_topology', 'scalar_material_mode',
    'scalar_mode', 'cell_id_array_name', 'composite_id_array_name',
    'field_data_tuple_id', 'force_compile_only', 'fragment_shader_code',
    'geometry_shader_code', 'ghost_level', 'number_of_pieces',
    'number_of_sub_pieces', 'piece', 'point_id_array_name',
    'populate_selection_settings', 'process_id_array_name',
    'progress_text', 'render_time',
    'resolve_coincident_topology_polygon_offset_faces',
    'resolve_coincident_topology_z_shift', 'scalar_range',
    'vertex_shader_code'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLStickMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLStickMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_immediate_mode_rendering', 'immediate_mode_rendering',
            'interpolate_scalars_before_mapping', 'scalar_visibility', 'static',
            'use_lookup_table_scalar_range'], ['color_mode',
            'resolve_coincident_topology', 'scalar_material_mode', 'scalar_mode'],
            ['cell_id_array_name', 'composite_id_array_name',
            'field_data_tuple_id', 'force_compile_only', 'fragment_shader_code',
            'geometry_shader_code', 'ghost_level', 'number_of_pieces',
            'number_of_sub_pieces', 'piece', 'point_id_array_name',
            'populate_selection_settings', 'process_id_array_name', 'render_time',
            'resolve_coincident_topology_polygon_offset_faces',
            'resolve_coincident_topology_z_shift', 'scalar_range',
            'vertex_shader_code']),
            title='Edit OpenGLStickMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLStickMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


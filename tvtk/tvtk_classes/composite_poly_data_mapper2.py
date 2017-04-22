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


class CompositePolyDataMapper2(OpenGLPolyDataMapper):
    """
    CompositePolyDataMapper2 - mapper for composite dataset consisting
    of polygonal data.
    
    Superclass: OpenGLPolyDataMapper
    
    CompositePolyDataMapper2 is similar to CompositePolyDataMapper
    except that instead of creating individual mapper for each block in
    the composite dataset, it iterates over the blocks internally.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCompositePolyDataMapper2, obj, update, **traits)
    
    def get_block_color(self, *args):
        """
        V.get_block_color(int) -> (float, ...)
        C++: double *GetBlockColor(unsigned int index)
        Set/get the color for a block given its flat index.
        """
        ret = self._wrap_call(self._vtk_obj.GetBlockColor, *args)
        return ret

    def set_block_color(self, *args):
        """
        V.set_block_color(int, [float, float, float])
        C++: void SetBlockColor(unsigned int index, double color[3])
        V.set_block_color(int, float, float, float)
        C++: void SetBlockColor(unsigned int index, double r, double g,
            double b)
        Set/get the color for a block given its flat index.
        """
        ret = self._wrap_call(self._vtk_obj.SetBlockColor, *args)
        return ret

    def get_block_opacity(self, *args):
        """
        V.get_block_opacity(int) -> float
        C++: double GetBlockOpacity(unsigned int index)
        Set/get the opacity for a block given its flat index.
        """
        ret = self._wrap_call(self._vtk_obj.GetBlockOpacity, *args)
        return ret

    def set_block_opacity(self, *args):
        """
        V.set_block_opacity(int, float)
        C++: void SetBlockOpacity(unsigned int index, double opacity)
        Set/get the opacity for a block given its flat index.
        """
        ret = self._wrap_call(self._vtk_obj.SetBlockOpacity, *args)
        return ret

    def get_block_visibility(self, *args):
        """
        V.get_block_visibility(int) -> bool
        C++: bool GetBlockVisibility(unsigned int index)
        Set/get the visibility for a block given its flat index.
        """
        ret = self._wrap_call(self._vtk_obj.GetBlockVisibility, *args)
        return ret

    def set_block_visibility(self, *args):
        """
        V.set_block_visibility(int, bool)
        C++: void SetBlockVisibility(unsigned int index, bool visible)
        Set/get the visibility for a block given its flat index.
        """
        ret = self._wrap_call(self._vtk_obj.SetBlockVisibility, *args)
        return ret

    def _get_composite_data_display_attributes(self):
        return wrap_vtk(self._vtk_obj.GetCompositeDataDisplayAttributes())
    def _set_composite_data_display_attributes(self, arg):
        old_val = self._get_composite_data_display_attributes()
        self._wrap_call(self._vtk_obj.SetCompositeDataDisplayAttributes,
                        deref_vtk(arg))
        self.trait_property_changed('composite_data_display_attributes', old_val, arg)
    composite_data_display_attributes = traits.Property(_get_composite_data_display_attributes, _set_composite_data_display_attributes, help=\
        """
        Set/get the composite data set attributes.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Specify the input data to map.
        """
    )

    def remove_block_color(self, *args):
        """
        V.remove_block_color(int)
        C++: void RemoveBlockColor(unsigned int index)
        Set/get the color for a block given its flat index.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveBlockColor, *args)
        return ret

    def remove_block_colors(self):
        """
        V.remove_block_colors()
        C++: void RemoveBlockColors()
        Set/get the color for a block given its flat index.
        """
        ret = self._vtk_obj.RemoveBlockColors()
        return ret
        

    def remove_block_opacities(self):
        """
        V.remove_block_opacities()
        C++: void RemoveBlockOpacities()
        Set/get the opacity for a block given its flat index.
        """
        ret = self._vtk_obj.RemoveBlockOpacities()
        return ret
        

    def remove_block_opacity(self, *args):
        """
        V.remove_block_opacity(int)
        C++: void RemoveBlockOpacity(unsigned int index)
        Set/get the opacity for a block given its flat index.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveBlockOpacity, *args)
        return ret

    def remove_block_visibilites(self):
        """
        V.remove_block_visibilites()
        C++: void RemoveBlockVisibilites()
        Set/get the visibility for a block given its flat index.
        """
        ret = self._vtk_obj.RemoveBlockVisibilites()
        return ret
        

    def remove_block_visibility(self, *args):
        """
        V.remove_block_visibility(int)
        C++: void RemoveBlockVisibility(unsigned int index)
        Set/get the visibility for a block given its flat index.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveBlockVisibility, *args)
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
            return super(CompositePolyDataMapper2, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CompositePolyDataMapper2 properties', scrollable=True, resizable=True,
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
            title='Edit CompositePolyDataMapper2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CompositePolyDataMapper2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


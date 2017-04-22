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

from tvtk.tvtk_classes.poly_data_mapper import PolyDataMapper


class OpenGLPolyDataMapper(PolyDataMapper):
    """
    OpenGLPolyDataMapper - poly_data_mapper using open_gl to render.
    
    Superclass: PolyDataMapper
    
    poly_data_mapper that uses a open_gl to do the actual rendering.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLPolyDataMapper, obj, update, **traits)
    
    cell_id_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        By default, this class uses the dataset's point and cell ids
        during rendering. However, one can override those by specifying
        cell and point data arrays to use instead. Currently, only
        IdType array is supported. Set to NULL string (default) to use
        the point ids instead.
        """
    )

    def _cell_id_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellIdArrayName,
                        self.cell_id_array_name)

    composite_id_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Generally, this class can render the composite id when iterating
        over composite datasets. However in some cases (as in AMR), the
        rendered structure may not correspond to the input data, in which
        case we need to provide a cell array that can be used to render
        in the composite id in selection passes. Set to NULL (default) to
        not override the composite id color set by CompositePainter if
        any. The array *MUST* be a cell array and of type
        UnsignedIntArray.
        """
    )

    def _composite_id_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCompositeIdArrayName,
                        self.composite_id_array_name)

    fragment_shader_code = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Allow the program to set the shader codes used directly instead
        of using the built in templates. Be aware, if set, this template
        will be used for all cases, primitive types, picking etc.
        """
    )

    def _fragment_shader_code_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFragmentShaderCode,
                        self.fragment_shader_code)

    geometry_shader_code = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Allow the program to set the shader codes used directly instead
        of using the built in templates. Be aware, if set, this template
        will be used for all cases, primitive types, picking etc.
        """
    )

    def _geometry_shader_code_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeometryShaderCode,
                        self.geometry_shader_code)

    point_id_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        By default, this class uses the dataset's point and cell ids
        during rendering. However, one can override those by specifying
        cell and point data arrays to use instead. Currently, only
        IdType array is supported. Set to NULL string (default) to use
        the point ids instead.
        """
    )

    def _point_id_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointIdArrayName,
                        self.point_id_array_name)

    populate_selection_settings = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _populate_selection_settings_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPopulateSelectionSettings,
                        self.populate_selection_settings)

    process_id_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        If this class should override the process id using a data-array,
        set this variable to the name of the array to use. It must be a
        point-array.
        """
    )

    def _process_id_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProcessIdArrayName,
                        self.process_id_array_name)

    vertex_shader_code = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Allow the program to set the shader codes used directly instead
        of using the built in templates. Be aware, if set, this template
        will be used for all cases, primitive types, picking etc.
        """
    )

    def _vertex_shader_code_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexShaderCode,
                        self.vertex_shader_code)

    def _get_have_apple_bug(self):
        return self._vtk_obj.GetHaveAppleBug()
    have_apple_bug = traits.Property(_get_have_apple_bug, help=\
        """
        Get the value of have_apple_bug
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Specify the input data to map.
        """
    )

    def _get_vbo(self):
        return wrap_vtk(self._vtk_obj.GetVBO())
    vbo = traits.Property(_get_vbo, help=\
        """
        Return the mapper's vertex buffer object.
        """
    )

    def add_shader_replacement(self, *args):
        """
        V.add_shader_replacement(Shader.Type, string, bool, string, bool)
        C++: void AddShaderReplacement(Shader::Type shaderType,
            std::string originalValue, bool replaceFirst,
            std::string replacementValue, bool replaceAll)
        This function enables you to apply your own substitutions to the
        shader creation process. The shader code in this class is created
        by applying a bunch of string replacements to a shader template.
        Using this function you can apply your own string replacements to
        add features you desire.
        """
        ret = self._wrap_call(self._vtk_obj.AddShaderReplacement, *args)
        return ret

    def clear_shader_replacement(self, *args):
        """
        V.clear_shader_replacement(Shader.Type, string, bool)
        C++: void ClearShaderReplacement(Shader::Type shaderType,
            std::string originalValue, bool replaceFirst)
        This function enables you to apply your own substitutions to the
        shader creation process. The shader code in this class is created
        by applying a bunch of string replacements to a shader template.
        Using this function you can apply your own string replacements to
        add features you desire.
        """
        ret = self._wrap_call(self._vtk_obj.ClearShaderReplacement, *args)
        return ret

    def force_have_apple_bug_off(self):
        """
        V.force_have_apple_bug_off()
        C++: void ForceHaveAppleBugOff()
        Override the normal test for the apple bug
        """
        ret = self._vtk_obj.ForceHaveAppleBugOff()
        return ret
        

    def force_have_apple_bug_on(self):
        """
        V.force_have_apple_bug_on()
        C++: void ForceHaveAppleBugOn()
        Override the normal test for the apple bug
        """
        ret = self._vtk_obj.ForceHaveAppleBugOn()
        return ret
        

    def render_edges(self, *args):
        """
        V.render_edges(Renderer, Actor)
        C++: virtual void RenderEdges(Renderer *ren, Actor *act)
        Implemented by sub classes. Actual rendering is done here.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderEdges, *my_args)
        return ret

    def render_piece_draw(self, *args):
        """
        V.render_piece_draw(Renderer, Actor)
        C++: virtual void RenderPieceDraw(Renderer *ren, Actor *act)
        Implemented by sub classes. Actual rendering is done here.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderPieceDraw, *my_args)
        return ret

    def render_piece_finish(self, *args):
        """
        V.render_piece_finish(Renderer, Actor)
        C++: virtual void RenderPieceFinish(Renderer *ren,
            Actor *act)
        Implemented by sub classes. Actual rendering is done here.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderPieceFinish, *my_args)
        return ret

    def render_piece_start(self, *args):
        """
        V.render_piece_start(Renderer, Actor)
        C++: virtual void RenderPieceStart(Renderer *ren,
            Actor *act)
        Implemented by sub classes. Actual rendering is done here.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderPieceStart, *my_args)
        return ret

    def set_vbo_shift_scale_method(self, *args):
        """
        V.set_vbo_shift_scale_method(int)
        C++: void SetVBOShiftScaleMethod(int m)
        A convenience method for enabling/disabling
        the VBO's shift+scale transform.
        """
        ret = self._wrap_call(self._vtk_obj.SetVBOShiftScaleMethod, *args)
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
            return super(OpenGLPolyDataMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLPolyDataMapper properties', scrollable=True, resizable=True,
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
            title='Edit OpenGLPolyDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLPolyDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


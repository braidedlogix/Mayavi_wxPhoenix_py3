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


class PointGaussianMapper(PolyDataMapper):
    """
    PointGaussianMapper - draw point_gaussians using imposters
    
    Superclass: PolyDataMapper
    
    An  mapper that uses imposters to draw gaussian splats or other
    shapes if custom shader code is set. Supports transparency and
    picking as well. It draws all the points and does not require cell
    arrays.  If cell arrays are provided it will only draw the points
    used by the Verts cell array. The shape of the imposter is a
    triangle.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointGaussianMapper, obj, update, **traits)
    
    emissive = tvtk_base.true_bool_trait(help=\
        """
        Treat the points/splats as emissive light sources. The default is
        true.
        """
    )

    def _emissive_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEmissive,
                        self.emissive_)

    opacity_array = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Method to set the optional opacity array.  If specified this
        array will be used to generate the opacity values.
        """
    )

    def _opacity_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOpacityArray,
                        self.opacity_array)

    opacity_table_size = traits.Int(1024, enter_set=True, auto_set=False, help=\
        """
        The size of the table used in computing opacities, used when
        converting a PiecewiseFunction to a table
        """
    )

    def _opacity_table_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOpacityTableSize,
                        self.opacity_table_size)

    def _get_scalar_opacity_function(self):
        return wrap_vtk(self._vtk_obj.GetScalarOpacityFunction())
    def _set_scalar_opacity_function(self, arg):
        old_val = self._get_scalar_opacity_function()
        self._wrap_call(self._vtk_obj.SetScalarOpacityFunction,
                        deref_vtk(arg))
        self.trait_property_changed('scalar_opacity_function', old_val, arg)
    scalar_opacity_function = traits.Property(_get_scalar_opacity_function, _set_scalar_opacity_function, help=\
        """
        Set/Get the optional opacity transfer function. This is only used
        when an opacity_array is also specified.
        """
    )

    scale_array = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Convenience method to set the array to scale with.
        """
    )

    def _scale_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleArray,
                        self.scale_array)

    scale_factor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the default scale factor of the point gaussians.  This
        defaults to 1.0. All radius computations will be scaled by the
        factor including the scale_array. If a PiecewideFunction is
        used the scaling happens prior to the function lookup. A scale
        factor of 0.0 indicates that the splats should be rendered as
        simple points.
        """
    )

    def _scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleFactor,
                        self.scale_factor)

    def _get_scale_function(self):
        return wrap_vtk(self._vtk_obj.GetScaleFunction())
    def _set_scale_function(self, arg):
        old_val = self._get_scale_function()
        self._wrap_call(self._vtk_obj.SetScaleFunction,
                        deref_vtk(arg))
        self.trait_property_changed('scale_function', old_val, arg)
    scale_function = traits.Property(_get_scale_function, _set_scale_function, help=\
        """
        Set/Get the optional scale transfer function. This is only used
        when a scale_array is also specified.
        """
    )

    scale_table_size = traits.Int(1024, enter_set=True, auto_set=False, help=\
        """
        The size of the table used in computing scale, used when
        converting a PiecewiseFunction to a table
        """
    )

    def _scale_table_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleTableSize,
                        self.scale_table_size)

    splat_shader_code = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Method to override the fragment shader code for the splat.  You
        can set this to draw other shapes. For the o_pen_gl2 backend some
        of the variables you can use and/or modify include, opacity - 0.0
        to 1.0 diffuse_color - vec3 ambient_color - vec3 offset_vcvs_output -
        vec2 offset in view coordinates from the splat center
        """
    )

    def _splat_shader_code_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSplatShaderCode,
                        self.splat_shader_code)

    triangle_scale = traits.Float(3.0, enter_set=True, auto_set=False, help=\
        """
        When drawing triangles as opposed too point mode (triangles are
        for splats shaders that are bigger than a pixel) this controls
        how large the triangle will be. By default it is large enough to
        contain a cicle of radius 3.0*scale which works well for gaussian
        splats as after 3.0 standard deviations the opacity is near zero.
        For custom shader codes a different value can be used. Generally
        you should use the lowest value you can as it will result in
        fewer fragments. For example if your custom shader only draws a
        disc of radius 1.0*scale, then set this to 1.0 to avoid sending
        many fragments to the shader that will just get discarded.
        """
    )

    def _triangle_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTriangleScale,
                        self.triangle_scale)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Specify the input data to map.
        """
    )

    _updateable_traits_ = \
    (('emissive', 'GetEmissive'), ('global_immediate_mode_rendering',
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
    ('opacity_array', 'GetOpacityArray'), ('opacity_table_size',
    'GetOpacityTableSize'), ('scale_array', 'GetScaleArray'),
    ('scale_factor', 'GetScaleFactor'), ('scale_table_size',
    'GetScaleTableSize'), ('splat_shader_code', 'GetSplatShaderCode'),
    ('triangle_scale', 'GetTriangleScale'), ('ghost_level',
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
    (['abort_execute', 'debug', 'emissive',
    'global_immediate_mode_rendering', 'global_warning_display',
    'immediate_mode_rendering', 'interpolate_scalars_before_mapping',
    'release_data_flag', 'scalar_visibility', 'static',
    'use_lookup_table_scalar_range', 'color_mode',
    'resolve_coincident_topology', 'scalar_material_mode', 'scalar_mode',
    'field_data_tuple_id', 'force_compile_only', 'ghost_level',
    'number_of_pieces', 'number_of_sub_pieces', 'opacity_array',
    'opacity_table_size', 'piece', 'progress_text', 'render_time',
    'resolve_coincident_topology_polygon_offset_faces',
    'resolve_coincident_topology_z_shift', 'scalar_range', 'scale_array',
    'scale_factor', 'scale_table_size', 'splat_shader_code',
    'triangle_scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointGaussianMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PointGaussianMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['emissive', 'global_immediate_mode_rendering',
            'immediate_mode_rendering', 'interpolate_scalars_before_mapping',
            'scalar_visibility', 'static', 'use_lookup_table_scalar_range'],
            ['color_mode', 'resolve_coincident_topology', 'scalar_material_mode',
            'scalar_mode'], ['field_data_tuple_id', 'force_compile_only',
            'ghost_level', 'number_of_pieces', 'number_of_sub_pieces',
            'opacity_array', 'opacity_table_size', 'piece', 'render_time',
            'resolve_coincident_topology_polygon_offset_faces',
            'resolve_coincident_topology_z_shift', 'scalar_range', 'scale_array',
            'scale_factor', 'scale_table_size', 'splat_shader_code',
            'triangle_scale']),
            title='Edit PointGaussianMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointGaussianMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.abstract_mapper3d import AbstractMapper3D


class Mapper(AbstractMapper3D):
    """
    Mapper - abstract class specifies interface to map data to
    graphics primitives
    
    Superclass: AbstractMapper3D
    
    Mapper is an abstract class to specify interface between data and
    graphics primitives. Subclasses of Mapper map data through a
    lookuptable and control the creation of rendering primitives that
    interface to the graphics library. The mapping can be controlled by
    supplying a lookup table and specifying a scalar range to map data
    through.
    
    There are several important control mechanisms affecting the behavior
    of this object. The scalar_visibility flag controls whether scalar
    data (if any) controls the color of the associated actor(s) that
    refer to the mapper. The scalar_mode ivar is used to determine whether
    scalar point data or cell data is used to color the object. By
    default, point data scalars are used unless there are none, in which
    cell scalars are used. Or you can explicitly control whether to use
    point or cell scalar data. Finally, the mapping of scalars through
    the lookup table varies depending on the setting of the color_mode
    flag. See the documentation for the appropriate methods for an
    explanation.
    
    Another important feature of this class is whether to use immediate
    mode rendering (_immediate_mode_rendering_on) or display list rendering
    (_immediate_mode_rendering_off). If display lists are used, a data
    structure is constructed (generally in the rendering library) which
    can then be rapidly traversed and rendered by the rendering library.
    The disadvantage of display lists is that they require additionally
    memory which may affect the performance of the system.
    
    Another important feature of the mapper is the ability to shift the
    z-buffer to resolve coincident topology. For example, if you'd like
    to draw a mesh with some edges a different color, and the edges lie
    on the mesh, this feature can be useful to get nice looking lines.
    (See the resolve_coincident_topology-related methods.)
    
    @sa
    DataSetMapper PolyDataMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMapper, obj, update, **traits)
    
    global_immediate_mode_rendering = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off flag to control whether data is rendered using
        immediate mode or note. Immediate mode rendering tends to be
        slower but it can handle larger datasets. The default value is
        immediate mode off. If you are having problems rendering a large
        dataset you might want to consider using immediate more
        rendering.
        """
    )

    def _global_immediate_mode_rendering_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobalImmediateModeRendering,
                        self.global_immediate_mode_rendering_)

    immediate_mode_rendering = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off flag to control whether data is rendered using
        immediate mode or note. Immediate mode rendering tends to be
        slower but it can handle larger datasets. The default value is
        immediate mode off. If you are having problems rendering a large
        dataset you might want to consider using immediate more
        rendering.
        """
    )

    def _immediate_mode_rendering_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImmediateModeRendering,
                        self.immediate_mode_rendering_)

    interpolate_scalars_before_mapping = tvtk_base.false_bool_trait(help=\
        """
        By default, vertex color is used to map colors to a surface.
        Colors are interpolated after being mapped. This option avoids
        color interpolation by using a one dimensional texture map for
        the colors.
        """
    )

    def _interpolate_scalars_before_mapping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolateScalarsBeforeMapping,
                        self.interpolate_scalars_before_mapping_)

    scalar_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off flag to control whether scalar data is used to color
        objects.
        """
    )

    def _scalar_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarVisibility,
                        self.scalar_visibility_)

    static = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off flag to control whether the mapper's data is static.
        Static data means that the mapper does not propagate updates down
        the pipeline, greatly decreasing the time it takes to update many
        mappers. This should only be used if the data never changes.
        """
    )

    def _static_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStatic,
                        self.static_)

    use_lookup_table_scalar_range = tvtk_base.false_bool_trait(help=\
        """
        Control whether the mapper sets the lookuptable range based on
        its own scalar_range, or whether it will use the lookup_table
        scalar_range regardless of it's own setting. By default the Mapper
        is allowed to set the lookup_table range, but users who are
        sharing lookup_tables between mappers/actors will probably wish to
        force the mapper to use the lookup_table unchanged.
        """
    )

    def _use_lookup_table_scalar_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseLookupTableScalarRange,
                        self.use_lookup_table_scalar_range_)

    color_mode = traits.Trait('default',
    tvtk_base.TraitRevPrefixMap({'default': 0, 'direct_scalars': 2, 'map_scalars': 1}), help=\
        """
        default (_color_mode_to_default), unsigned char scalars are treated
        as colors, and NOT mapped through the lookup table, while
        everything else is.  color_mode_to_direct_scalar extends
        color_mode_to_default such that all integer types are treated as
        colors with values in the range 0-255 and floating types are
        treated as colors with values in the range 0.0-1.0.  Setting
        color_mode_to_map_scalars means that all scalar data will be mapped
        through the lookup table.  (Note that for multi-component
        scalars, the particular component to use for mapping can be
        specified using the select_color_array() method.)
        """
    )

    def _color_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorMode,
                        self.color_mode_)

    resolve_coincident_topology = traits.Trait('polygon_offset',
    tvtk_base.TraitRevPrefixMap({'polygon_offset': 1, 'default': 0, 'off': 0, 'shift_z_buffer': 2}), help=\
        """
        Set/Get a global flag that controls whether coincident topology
        (e.g., a line on top of a polygon) is shifted to avoid z-buffer
        resolution (and hence rendering problems). If not off, there are
        two methods to choose from. polygon_offset uses graphics systems
        calls to shift polygons, but does not distinguish vertices and
        lines from one another. shift_z_buffer remaps the z-buffer to
        distinguish vertices, lines, and polygons, but does not always
        produce acceptable results. If you use the shift_z_buffer approach,
        you may also want to set the resolve_coincident_topology_z_shift
        value. (Note: not all mappers/graphics systems implement this
        functionality.)
        """
    )

    def _resolve_coincident_topology_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolveCoincidentTopology,
                        self.resolve_coincident_topology_)

    scalar_material_mode = traits.Trait('default',
    tvtk_base.TraitRevPrefixMap({'default': 0, 'ambient': 1, 'ambient_and_diffuse': 3, 'diffuse': 2}), help=\
        """
        Set/Get the light-model color mode.
        """
    )

    def _scalar_material_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarMaterialMode,
                        self.scalar_material_mode_)

    scalar_mode = traits.Trait('default',
    tvtk_base.TraitRevPrefixMap({'default': 0, 'use_cell_data': 2, 'use_cell_field_data': 4, 'use_field_data': 5, 'use_point_data': 1, 'use_point_field_data': 3}), help=\
        """
        Control how the filter works with scalar point data and cell
        attribute data.  By default (_scalar_mode_to_default), the filter
        will use point data, and if no point data is available, then cell
        data is used. Alternatively you can explicitly set the filter to
        use point data (_scalar_mode_to_use_point_data) or cell data
        (_scalar_mode_to_use_cell_data). You can also choose to get the scalars
        from an array in point field data (_scalar_mode_to_use_point_field_data)
        or cell field data (_scalar_mode_to_use_cell_field_data).  If scalars
        are coming from a field data array, you must call
        select_color_array before you call get_colors.
        """
    )

    def _scalar_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarMode,
                        self.scalar_mode_)

    field_data_tuple_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _field_data_tuple_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldDataTupleId,
                        self.field_data_tuple_id)

    force_compile_only = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Force compile only mode in case display lists are used
        (_immediate_mode_rendering is false). If immediate_mode_rendering is
        true, no rendering happens. Changing the value of this flag does
        not change modified time of the mapper. Initial value is false.
        This can be used by another rendering class which also uses
        display lists (call of display lists can be nested but not their
        creation.) There is no good reason to expose it to wrappers.
        """
    )

    def _force_compile_only_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForceCompileOnly,
                        self.force_compile_only)

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Specify a lookup table for the mapper to use.
        """
    )

    def get_relative_coincident_topology_line_offset_parameters(self, *args):
        """
        V.get_relative_coincident_topology_line_offset_parameters(float, float)
        C++: void GetRelativeCoincidentTopologyLineOffsetParameters(
            double &factor, double &units)
        Used to set the line offset values relative to the global Used
        when resolve_coincident_topology is set to polygon_offset.
        """
        ret = self._wrap_call(self._vtk_obj.GetRelativeCoincidentTopologyLineOffsetParameters, *args)
        return ret

    def set_relative_coincident_topology_line_offset_parameters(self, *args):
        """
        V.set_relative_coincident_topology_line_offset_parameters(float, float)
        C++: void SetRelativeCoincidentTopologyLineOffsetParameters(
            double factor, double units)
        Used to set the line offset values relative to the global Used
        when resolve_coincident_topology is set to polygon_offset.
        """
        ret = self._wrap_call(self._vtk_obj.SetRelativeCoincidentTopologyLineOffsetParameters, *args)
        return ret

    def get_relative_coincident_topology_point_offset_parameter(self, *args):
        """
        V.get_relative_coincident_topology_point_offset_parameter(float)
        C++: void GetRelativeCoincidentTopologyPointOffsetParameter(
            double &units)
        Used to set the point offset value relative to the global Used
        when resolve_coincident_topology is set to polygon_offset.
        """
        ret = self._wrap_call(self._vtk_obj.GetRelativeCoincidentTopologyPointOffsetParameter, *args)
        return ret

    def set_relative_coincident_topology_point_offset_parameter(self, *args):
        """
        V.set_relative_coincident_topology_point_offset_parameter(float)
        C++: void SetRelativeCoincidentTopologyPointOffsetParameter(
            double units)
        Used to set the point offset value relative to the global Used
        when resolve_coincident_topology is set to polygon_offset.
        """
        ret = self._wrap_call(self._vtk_obj.SetRelativeCoincidentTopologyPointOffsetParameter, *args)
        return ret

    def get_relative_coincident_topology_polygon_offset_parameters(self, *args):
        """
        V.get_relative_coincident_topology_polygon_offset_parameters(float,
            float)
        C++: void GetRelativeCoincidentTopologyPolygonOffsetParameters(
            double &factor, double &units)
        Used to set the polygon offset values relative to the global Used
        when resolve_coincident_topology is set to polygon_offset.
        """
        ret = self._wrap_call(self._vtk_obj.GetRelativeCoincidentTopologyPolygonOffsetParameters, *args)
        return ret

    def set_relative_coincident_topology_polygon_offset_parameters(self, *args):
        """
        V.set_relative_coincident_topology_polygon_offset_parameters(float,
            float)
        C++: void SetRelativeCoincidentTopologyPolygonOffsetParameters(
            double factor, double units)
        Used to set the polygon offset values relative to the global Used
        when resolve_coincident_topology is set to polygon_offset.
        """
        ret = self._wrap_call(self._vtk_obj.SetRelativeCoincidentTopologyPolygonOffsetParameters, *args)
        return ret

    render_time = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        This instance variable is used by LODActor to determine which
        mapper to use.  It is an estimate of the time necessary to
        render. Setting the render time does not modify the mapper.
        """
    )

    def _render_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRenderTime,
                        self.render_time)

    def get_resolve_coincident_topology_line_offset_parameters(self, *args):
        """
        V.get_resolve_coincident_topology_line_offset_parameters(float, float)
        C++: static void GetResolveCoincidentTopologyLineOffsetParameters(
            double &factor, double &units)
        Used to set the line offset scale factor and units. Used when
        resolve_coincident_topology is set to polygon_offset. These are
        global variables.
        """
        ret = self._wrap_call(self._vtk_obj.GetResolveCoincidentTopologyLineOffsetParameters, *args)
        return ret

    def set_resolve_coincident_topology_line_offset_parameters(self, *args):
        """
        V.set_resolve_coincident_topology_line_offset_parameters(float, float)
        C++: static void SetResolveCoincidentTopologyLineOffsetParameters(
            double factor, double units)
        Used to set the line offset scale factor and units. Used when
        resolve_coincident_topology is set to polygon_offset. These are
        global variables.
        """
        ret = self._wrap_call(self._vtk_obj.SetResolveCoincidentTopologyLineOffsetParameters, *args)
        return ret

    def get_resolve_coincident_topology_point_offset_parameter(self, *args):
        """
        V.get_resolve_coincident_topology_point_offset_parameter(float)
        C++: static void GetResolveCoincidentTopologyPointOffsetParameter(
            double &units)
        Used to set the point offset value Used when
        resolve_coincident_topology is set to polygon_offset. These are
        global variables.
        """
        ret = self._wrap_call(self._vtk_obj.GetResolveCoincidentTopologyPointOffsetParameter, *args)
        return ret

    def set_resolve_coincident_topology_point_offset_parameter(self, *args):
        """
        V.set_resolve_coincident_topology_point_offset_parameter(float)
        C++: static void SetResolveCoincidentTopologyPointOffsetParameter(
            double units)
        Used to set the point offset value Used when
        resolve_coincident_topology is set to polygon_offset. These are
        global variables.
        """
        ret = self._wrap_call(self._vtk_obj.SetResolveCoincidentTopologyPointOffsetParameter, *args)
        return ret

    resolve_coincident_topology_polygon_offset_faces = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Used when resolve_coincident_topology is set to polygon_offset. The
        polygon offset can be applied either to the solid polygonal faces
        or the lines/vertices. When set (default), the offset is applied
        to the faces otherwise it is applied to lines and vertices. This
        is a global variable.
        """
    )

    def _resolve_coincident_topology_polygon_offset_faces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolveCoincidentTopologyPolygonOffsetFaces,
                        self.resolve_coincident_topology_polygon_offset_faces)

    def get_resolve_coincident_topology_polygon_offset_parameters(self, *args):
        """
        V.get_resolve_coincident_topology_polygon_offset_parameters(float,
            float)
        C++: static void GetResolveCoincidentTopologyPolygonOffsetParameters(
            double &factor, double &units)
        Used to set the polygon offset scale factor and units. Used when
        resolve_coincident_topology is set to polygon_offset. These are
        global variables.
        """
        ret = self._wrap_call(self._vtk_obj.GetResolveCoincidentTopologyPolygonOffsetParameters, *args)
        return ret

    def set_resolve_coincident_topology_polygon_offset_parameters(self, *args):
        """
        V.set_resolve_coincident_topology_polygon_offset_parameters(float,
            float)
        C++: static void SetResolveCoincidentTopologyPolygonOffsetParameters(
            double factor, double units)
        Used to set the polygon offset scale factor and units. Used when
        resolve_coincident_topology is set to polygon_offset. These are
        global variables.
        """
        ret = self._wrap_call(self._vtk_obj.SetResolveCoincidentTopologyPolygonOffsetParameters, *args)
        return ret

    resolve_coincident_topology_z_shift = traits.Float(0.01, enter_set=True, auto_set=False, help=\
        """
        Used to set the z-shift if resolve_coincident_topology is set to
        shift_z_buffer. This is a global variable.
        """
    )

    def _resolve_coincident_topology_z_shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolveCoincidentTopologyZShift,
                        self.resolve_coincident_topology_z_shift)

    scalar_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 1.0), cols=2, help=\
        """
        
        """
    )

    def _scalar_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarRange,
                        self.scalar_range)

    def _get_array_access_mode(self):
        return self._vtk_obj.GetArrayAccessMode()
    array_access_mode = traits.Property(_get_array_access_mode, help=\
        """
        
        """
    )

    def _get_array_component(self):
        return self._vtk_obj.GetArrayComponent()
    array_component = traits.Property(_get_array_component, help=\
        """
        
        """
    )

    def _get_array_id(self):
        return self._vtk_obj.GetArrayId()
    array_id = traits.Property(_get_array_id, help=\
        """
        
        """
    )

    def _get_array_name(self):
        return self._vtk_obj.GetArrayName()
    array_name = traits.Property(_get_array_name, help=\
        """
        Get the array name or number and component to color by.
        """
    )

    def get_coincident_topology_line_offset_parameters(self, *args):
        """
        V.get_coincident_topology_line_offset_parameters(float, float)
        C++: void GetCoincidentTopologyLineOffsetParameters(
            double &factor, double &units)
        Get the net paramters for handlig coincident topology obtained by
        summing the global values with the relative values.
        """
        ret = self._wrap_call(self._vtk_obj.GetCoincidentTopologyLineOffsetParameters, *args)
        return ret

    def get_coincident_topology_point_offset_parameter(self, *args):
        """
        V.get_coincident_topology_point_offset_parameter(float)
        C++: void GetCoincidentTopologyPointOffsetParameter(double &units)
        Get the net paramters for handlig coincident topology obtained by
        summing the global values with the relative values.
        """
        ret = self._wrap_call(self._vtk_obj.GetCoincidentTopologyPointOffsetParameter, *args)
        return ret

    def get_coincident_topology_polygon_offset_parameters(self, *args):
        """
        V.get_coincident_topology_polygon_offset_parameters(float, float)
        C++: void GetCoincidentTopologyPolygonOffsetParameters(
            double &factor, double &units)
        Get the net paramters for handlig coincident topology obtained by
        summing the global values with the relative values.
        """
        ret = self._wrap_call(self._vtk_obj.GetCoincidentTopologyPolygonOffsetParameters, *args)
        return ret

    def _get_color_coordinates(self):
        return wrap_vtk(self._vtk_obj.GetColorCoordinates())
    color_coordinates = traits.Property(_get_color_coordinates, help=\
        """
        Provide read access to the color texture coordinate array
        """
    )

    def _get_color_map_colors(self):
        return wrap_vtk(self._vtk_obj.GetColorMapColors())
    color_map_colors = traits.Property(_get_color_map_colors, help=\
        """
        Provide read access to the color array
        """
    )

    def _get_color_texture_map(self):
        return wrap_vtk(self._vtk_obj.GetColorTextureMap())
    color_texture_map = traits.Property(_get_color_texture_map, help=\
        """
        Provide read access to the color texture array
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input as a DataSet.  This method is overridden in the
        specialized mapper classes to return more specific data types.
        """
    )

    def _get_input_as_data_set(self):
        return wrap_vtk(self._vtk_obj.GetInputAsDataSet())
    input_as_data_set = traits.Property(_get_input_as_data_set, help=\
        """
        Get the input to this mapper as a DataSet, instead of as a
        more specialized data type that the subclass may return from
        get_input().  This method is provided for use in the wrapper
        languages, C++ programmers should use get_input() instead.
        """
    )

    def _get_is_opaque(self):
        return self._vtk_obj.GetIsOpaque()
    is_opaque = traits.Property(_get_is_opaque, help=\
        """
        Returns if the mapper does not expect to have translucent
        geometry. This may happen when using color_mode is set to not map
        scalars i.e. render the scalar array directly as colors and the
        scalar array has opacity i.e. alpha component.  Default
        implementation simply returns true. Note that even if this method
        returns true, an actor may treat the geometry as translucent
        since a constant translucency is set on the property, for
        example.
        """
    )

    def _get_supports_selection(self):
        return self._vtk_obj.GetSupportsSelection()
    supports_selection = traits.Property(_get_supports_selection, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS Used by
        HardwareSelector to determine if the prop supports hardware
        selection.
        """
    )

    def can_use_texture_map_for_coloring(self, *args):
        """
        V.can_use_texture_map_for_coloring(DataObject) -> int
        C++: virtual int CanUseTextureMapForColoring(DataObject *input)
        Returns if we can use texture maps for scalar coloring. Note this
        doesn't say we "will" use scalar coloring. It says, if we do use
        scalar coloring, we will use a texture. When rendering multiblock
        datasets, if any 2 blocks provide different lookup tables for the
        scalars, then also we cannot use textures. This case can be
        handled if required.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CanUseTextureMapForColoring, *my_args)
        return ret

    def clear_color_arrays(self):
        """
        V.clear_color_arrays()
        C++: void ClearColorArrays()
        Call to force a rebuild of color result arrays on next
        map_scalars. Necessary when using arrays in the case of multiblock
        data.
        """
        ret = self._vtk_obj.ClearColorArrays()
        return ret
        

    def clear_invertible_color(self):
        """
        V.clear_invertible_color()
        C++: void ClearInvertibleColor()
        Used internally by ValuePass.
        """
        ret = self._vtk_obj.ClearInvertibleColor()
        return ret
        

    def color_by_array_component(self, *args):
        """
        V.color_by_array_component(int, int)
        C++: void ColorByArrayComponent(int arrayNum, int component)
        V.color_by_array_component(string, int)
        C++: void ColorByArrayComponent(const char *arrayName,
            int component)
        Legacy: These methods used to be used to specify the array
        component. It is better to do this in the lookup table.
        """
        ret = self._wrap_call(self._vtk_obj.ColorByArrayComponent, *args)
        return ret

    def color_to_value(self, *args):
        """
        V.color_to_value([int, ...], float, float, float)
        C++: static void ColorToValue(unsigned char *color, double min,
            double scale, double &value)
        Convert an RGB triplet to a floating point value.
        """
        ret = self._wrap_call(self._vtk_obj.ColorToValue, *args)
        return ret

    def create_default_lookup_table(self):
        """
        V.create_default_lookup_table()
        C++: virtual void CreateDefaultLookupTable()
        Create default lookup table. Generally used to create one when
        none is available with the scalar data.
        """
        ret = self._vtk_obj.CreateDefaultLookupTable()
        return ret
        

    def map_scalars(self, *args):
        """
        V.map_scalars(float) -> UnsignedCharArray
        C++: virtual UnsignedCharArray *MapScalars(double alpha)
        V.map_scalars(float, int) -> UnsignedCharArray
        C++: virtual UnsignedCharArray *MapScalars(double alpha,
            int &cellFlag)
        V.map_scalars(DataSet, float) -> UnsignedCharArray
        C++: virtual UnsignedCharArray *MapScalars(DataSet *input,
            double alpha)
        V.map_scalars(DataSet, float, int) -> UnsignedCharArray
        C++: virtual UnsignedCharArray *MapScalars(DataSet *input,
            double alpha, int &cellFlag)
        Map the scalars (if there are any scalars and scalar_visibility is
        on) through the lookup table, returning an unsigned char RGBA
        array. This is typically done as part of the rendering process.
        The alpha parameter allows the blending of the scalars with an
        additional alpha (typically which comes from a Actor, etc.)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MapScalars, *my_args)
        return wrap_vtk(ret)

    def render(self, *args):
        """
        V.render(Renderer, Actor)
        C++: virtual void Render(Renderer *ren, Actor *a)
        Method initiates the mapping process. Generally sent by the actor
        as each frame is rendered.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Render, *my_args)
        return ret

    def select_color_array(self, *args):
        """
        V.select_color_array(int)
        C++: void SelectColorArray(int arrayNum)
        V.select_color_array(string)
        C++: void SelectColorArray(const char *arrayName)
        When scalar_mode is set to use_point_field_data or use_cell_field_data,
        you can specify which array to use for coloring using these
        methods. The lookup table will decide how to convert vectors to
        colors.
        """
        ret = self._wrap_call(self._vtk_obj.SelectColorArray, *args)
        return ret

    def use_invertible_color_for(self, *args):
        """
        V.use_invertible_color_for(DataObject, int, int, int, string, int,
             [float, ...])
        C++: void UseInvertibleColorFor(DataObject *input,
            int scalarMode, int arrayAccessMode, int arrayId,
            const char *arrayName, int arrayComponent,
            double *scalarRange)
        V.use_invertible_color_for(int, int, int, string, int, [float, ...])
        C++: void UseInvertibleColorFor(int scalarMode,
            int arrayAccessMode, int arrayId, const char *arrayName,
            int arrayComponent, double *scalarRange)
        Used internally by ValuePass
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UseInvertibleColorFor, *my_args)
        return ret

    def value_to_color(self, *args):
        """
        V.value_to_color(float, float, float, [int, ...])
        C++: static void ValueToColor(double value, double min,
            double scale, unsigned char *color)
        Convert a floating point value to an RGB triplet.
        """
        ret = self._wrap_call(self._vtk_obj.ValueToColor, *args)
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
    (['abort_execute', 'debug', 'global_immediate_mode_rendering',
    'global_warning_display', 'immediate_mode_rendering',
    'interpolate_scalars_before_mapping', 'release_data_flag',
    'scalar_visibility', 'static', 'use_lookup_table_scalar_range',
    'color_mode', 'resolve_coincident_topology', 'scalar_material_mode',
    'scalar_mode', 'field_data_tuple_id', 'force_compile_only',
    'progress_text', 'render_time',
    'resolve_coincident_topology_polygon_offset_faces',
    'resolve_coincident_topology_z_shift', 'scalar_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Mapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Mapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_immediate_mode_rendering', 'immediate_mode_rendering',
            'interpolate_scalars_before_mapping', 'scalar_visibility', 'static',
            'use_lookup_table_scalar_range'], ['color_mode',
            'resolve_coincident_topology', 'scalar_material_mode', 'scalar_mode'],
            ['field_data_tuple_id', 'force_compile_only', 'render_time',
            'resolve_coincident_topology_polygon_offset_faces',
            'resolve_coincident_topology_z_shift', 'scalar_range']),
            title='Edit Mapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Mapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


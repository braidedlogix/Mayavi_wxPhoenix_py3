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


class PolyDataMapper(Mapper):
    """
    PolyDataMapper - map PolyData to graphics primitives
    
    Superclass: Mapper
    
    PolyDataMapper is a class that maps polygonal data (i.e.,
    PolyData) to graphics primitives. PolyDataMapper serves as a
    superclass for device-specific poly data mappers, that actually do
    the mapping to the rendering/graphics hardware/software.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyDataMapper, obj, update, **traits)
    
    ghost_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of ghost cells to return.
        """
    )

    def _ghost_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGhostLevel,
                        self.ghost_level)

    number_of_pieces = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        If you want only a part of the data, specify by setting the
        piece.
        """
    )

    def _number_of_pieces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPieces,
                        self.number_of_pieces)

    number_of_sub_pieces = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        If you want only a part of the data, specify by setting the
        piece.
        """
    )

    def _number_of_sub_pieces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSubPieces,
                        self.number_of_sub_pieces)

    piece = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        If you want only a part of the data, specify by setting the
        piece.
        """
    )

    def _piece_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPiece,
                        self.piece)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Specify the input data to map.
        """
    )

    def map_data_array_to_multi_texture_attribute(self, *args):
        """
        V.map_data_array_to_multi_texture_attribute(int, string, int, int)
        C++: virtual void MapDataArrayToMultiTextureAttribute(int unit,
            const char *dataArrayName, int fieldAssociation,
            int componentno=-1)"""
        ret = self._wrap_call(self._vtk_obj.MapDataArrayToMultiTextureAttribute, *args)
        return ret

    def map_data_array_to_vertex_attribute(self, *args):
        """
        V.map_data_array_to_vertex_attribute(string, string, int, int)
        C++: virtual void MapDataArrayToVertexAttribute(
            const char *vertexAttributeName, const char *dataArrayName,
            int fieldAssociation, int componentno=-1)
        Select a data array from the point/cell data and map it to a
        generic vertex attribute. vertex_attribute_name is the name of the
        vertex attribute. data_array_name is the name of the data array.
        field_association indicates when the data array is a point data
        array or cell data array (vtk_data_object::_field__association__points
        or (vtk_data_object::_field__association__cells). componentno
        indicates which component from the data array must be passed as
        the attribute. If -1, then all components are passed.
        """
        ret = self._wrap_call(self._vtk_obj.MapDataArrayToVertexAttribute, *args)
        return ret

    def remove_all_vertex_attribute_mappings(self):
        """
        V.remove_all_vertex_attribute_mappings()
        C++: virtual void RemoveAllVertexAttributeMappings()
        Remove all vertex attributes.
        """
        ret = self._vtk_obj.RemoveAllVertexAttributeMappings()
        return ret
        

    def remove_vertex_attribute_mapping(self, *args):
        """
        V.remove_vertex_attribute_mapping(string)
        C++: virtual void RemoveVertexAttributeMapping(
            const char *vertexAttributeName)
        Remove a vertex attribute mapping.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveVertexAttributeMapping, *args)
        return ret

    def render_piece(self, *args):
        """
        V.render_piece(Renderer, Actor)
        C++: virtual void RenderPiece(Renderer *ren, Actor *act)
        Implemented by sub classes. Actual rendering is done here.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RenderPiece, *my_args)
        return ret

    def set_input_data(self, *args):
        """
        V.set_input_data(PolyData)
        C++: void SetInputData(PolyData *in)
        Specify the input data to map.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
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
    ('ghost_level', 'GetGhostLevel'), ('number_of_pieces',
    'GetNumberOfPieces'), ('number_of_sub_pieces',
    'GetNumberOfSubPieces'), ('piece', 'GetPiece'),
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
    'ghost_level', 'number_of_pieces', 'number_of_sub_pieces', 'piece',
    'progress_text', 'render_time',
    'resolve_coincident_topology_polygon_offset_faces',
    'resolve_coincident_topology_z_shift', 'scalar_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyDataMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_immediate_mode_rendering', 'immediate_mode_rendering',
            'interpolate_scalars_before_mapping', 'scalar_visibility', 'static',
            'use_lookup_table_scalar_range'], ['color_mode',
            'resolve_coincident_topology', 'scalar_material_mode', 'scalar_mode'],
            ['field_data_tuple_id', 'force_compile_only', 'ghost_level',
            'number_of_pieces', 'number_of_sub_pieces', 'piece', 'render_time',
            'resolve_coincident_topology_polygon_offset_faces',
            'resolve_coincident_topology_z_shift', 'scalar_range']),
            title='Edit PolyDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyDataMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


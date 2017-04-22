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

from tvtk.tvtk_classes.mapper2d import Mapper2D


class PolyDataMapper2D(Mapper2D):
    """
    PolyDataMapper2D - draw PolyData onto the image plane
    
    Superclass: Mapper2D
    
    PolyDataMapper2D is a mapper that renders 3d polygonal data
    (vtk_poly_data) onto the 2d image plane (i.e., the renderer's
    viewport). By default, the 3d data is transformed into 2d data by
    ignoring the z-coordinate of the 3d points in PolyData, and taking
    the x-y values as local display values (i.e., pixel coordinates).
    Alternatively, you can provide a Coordinate object that will
    transform the data into local display coordinates (use the
    Coordinate::SetCoordinateSystem() methods to indicate which
    coordinate system you are transforming the data from).
    
    @sa
    Mapper2D Actor2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyDataMapper2D, obj, update, **traits)
    
    scalar_visibility = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off flag to control whether scalar data is used to color
        objects.
        """
    )

    def _scalar_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarVisibility,
                        self.scalar_visibility_)

    transform_coordinate_use_double = tvtk_base.false_bool_trait(help=\
        """
        Specify whether or not rounding to integers the transformed
        points when transform_coordinate is set. By default, it does not
        use double precision.
        """
    )

    def _transform_coordinate_use_double_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTransformCoordinateUseDouble,
                        self.transform_coordinate_use_double_)

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
        Control how the scalar data is mapped to colors.  By default
        (_color_mode_to_default), unsigned char scalars are treated as
        colors, and NOT mapped through the lookup table, while everything
        else is. color_mode_to_direct_scalar extends color_mode_to_default such
        that all integer types are treated as colors with values in the
        range 0-255 and floating types are treated as colors with values
        in the range 0.0-1.0. Setting color_mode_to_map_scalars means that
        all scalar data will be mapped through the lookup table.  (Note
        that for multi-component scalars, the particular component to use
        for mapping can be specified using the color_by_array_component()
        method.)
        """
    )

    def _color_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorMode,
                        self.color_mode_)

    scalar_mode = traits.Trait('default',
    tvtk_base.TraitRevPrefixMap({'default': 0, 'use_cell_data': 2, 'use_cell_field_data': 4, 'use_point_data': 1, 'use_point_field_data': 3}), help=\
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
        color_by_array_component before you call get_colors.
        """
    )

    def _scalar_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarMode,
                        self.scalar_mode_)

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

    scalar_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 1.0), cols=2, help=\
        """
        
        """
    )

    def _scalar_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarRange,
                        self.scalar_range)

    def _get_transform_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetTransformCoordinate())
    def _set_transform_coordinate(self, arg):
        old_val = self._get_transform_coordinate()
        self._wrap_call(self._vtk_obj.SetTransformCoordinate,
                        deref_vtk(arg))
        self.trait_property_changed('transform_coordinate', old_val, arg)
    transform_coordinate = traits.Property(_get_transform_coordinate, _set_transform_coordinate, help=\
        """
        Specify a Coordinate object to be used to transform the
        PolyData point coordinates. By default (no Coordinate
        specified), the point coordinates are taken as viewport
        coordinates (pixels in the viewport into which the mapper is
        rendering).
        """
    )

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

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set the input to the mapper.
        """
    )

    def color_by_array_component(self, *args):
        """
        V.color_by_array_component(int, int)
        C++: void ColorByArrayComponent(int arrayNum, int component)
        V.color_by_array_component(string, int)
        C++: void ColorByArrayComponent(char *arrayName, int component)
        Choose which component of which field data array to color by.
        """
        ret = self._wrap_call(self._vtk_obj.ColorByArrayComponent, *args)
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
        C++: UnsignedCharArray *MapScalars(double alpha)
        Map the scalars (if there are any scalars and scalar_visibility is
        on) through the lookup table, returning an unsigned char RGBA
        array. This is typically done as part of the rendering process.
        The alpha parameter allows the blending of the scalars with an
        additional alpha (typically which comes from a Actor, etc.)
        """
        ret = self._wrap_call(self._vtk_obj.MapScalars, *args)
        return wrap_vtk(ret)

    def set_input_data(self, *args):
        """
        V.set_input_data(PolyData)
        C++: void SetInputData(PolyData *in)
        Set the input to the mapper.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    _updateable_traits_ = \
    (('scalar_visibility', 'GetScalarVisibility'),
    ('transform_coordinate_use_double',
    'GetTransformCoordinateUseDouble'), ('use_lookup_table_scalar_range',
    'GetUseLookupTableScalarRange'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('color_mode',
    'GetColorMode'), ('scalar_mode', 'GetScalarMode'), ('scalar_range',
    'GetScalarRange'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'scalar_visibility',
    'transform_coordinate_use_double', 'use_lookup_table_scalar_range',
    'color_mode', 'scalar_mode', 'progress_text', 'scalar_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyDataMapper2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyDataMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['scalar_visibility', 'transform_coordinate_use_double',
            'use_lookup_table_scalar_range'], ['color_mode', 'scalar_mode'],
            ['scalar_range']),
            title='Edit PolyDataMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyDataMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


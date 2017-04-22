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

from tvtk.tvtk_classes.scalars_to_colors import ScalarsToColors


class LookupTable(ScalarsToColors):
    """
    LookupTable - map scalar values into colors via a lookup table
    
    Superclass: ScalarsToColors
    
    LookupTable is an object that is used by mapper objects to map
    scalar values into RGBA (red-green-blue-alpha transparency) color
    specification, or RGBA into scalar values. The color table can be
    created by direct insertion of color values, or by specifying a hue,
    saturation, value, and alpha range and generating a table.
    
    A special color for na_n values in the data can be specified via
    set_nan_color(). In addition, a color for data values below the lookup
    table range minimum can be specified with set_below_range_color(), and
    that color will be used for values below the range minimum when
    use_below_range_color is on.  Likewise, a color for data values above
    the lookup table range maximum can be specified with
    set_above_range_color(), and it is used when use_above_range_color is on.
    
    This class behaves differently depending on how indexed_lookup is set.
    When true, LookupTable enters a mode for representing categorical
    color maps. By setting indexed_lookup to true, you indicate that the
    annotated values are the only valid values for which entries in the
    color table should be returned. The colors in the lookup Table are
    assigned to annotated values by taking the modulus of their index in
    the list of annotations. indexed_lookup changes the behavior of
    get_index, which in turn changes the way map_scalars_through_table2
    behaves; when indexed_lookup is true, map_scalars_through_table2 will
    search for scalar values in annotated_values and use the resulting
    index to determine the color. If a scalar value is not present in
    annotated_values, then nan_color will be used.
    
    @warning
    You need to explicitly call Build() when constructing the LUT by
    hand.
    
    @sa
    LogLookupTable WindowLevelLookupTable
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLookupTable, obj, update, **traits)
    
    use_above_range_color = tvtk_base.false_bool_trait(help=\
        """
        Set whether the below range color should be used.
        """
    )

    def _use_above_range_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseAboveRangeColor,
                        self.use_above_range_color_)

    use_below_range_color = tvtk_base.false_bool_trait(help=\
        """
        Set whether the below range color should be used.
        """
    )

    def _use_below_range_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseBelowRangeColor,
                        self.use_below_range_color_)

    ramp = traits.Trait('s_curve',
    tvtk_base.TraitRevPrefixMap({'s_curve': 1, 'linear': 0, 'sqrt': 2}), help=\
        """
        Set the shape of the table ramp to either linear or S-curve. The
        default is S-curve, which tails off gradually at either end. The
        equation used for the S-curve is y = (sin((x - 1/2)*pi) + 1)/2,
        while the equation for the linear ramp is simply y = x.  For an
        S-curve greyscale ramp, you should set number_of_table_values to 402
        (which is 256*pi/2) to provide room for the tails of the ramp.
        The equation for the SQRT is y = sqrt(x).
        """
    )

    def _ramp_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRamp,
                        self.ramp_)

    scale = traits.Trait('linear',
    tvtk_base.TraitRevPrefixMap({'linear': 0, 'log10': 1}), help=\
        """
        Set the type of scale to use, linear or logarithmic.  The default
        is linear.  If the scale is logarithmic, then the table_range must
        not cross the value zero.
        """
    )

    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale_)

    above_range_color = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(1.0, 1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _above_range_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAboveRangeColor,
                        self.above_range_color)

    alpha_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(1.0, 1.0), cols=2, help=\
        """
        
        """
    )

    def _alpha_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlphaRange,
                        self.alpha_range)

    below_range_color = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, 0.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _below_range_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBelowRangeColor,
                        self.below_range_color)

    hue_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 0.66667), cols=2, help=\
        """
        
        """
    )

    def _hue_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHueRange,
                        self.hue_range)

    nan_color = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.5, 0.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _nan_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNanColor,
                        self.nan_color)

    number_of_colors = traits.Trait(256, traits.Range(2, 9223372036854775807, enter_set=True, auto_set=False), help=\
        """
        Set the number of colors in the lookup table.  Use
        set_number_of_table_values() instead, it can be used both before and
        after the table has been built whereas set_number_of_colors() has no
        effect after the table has been built.
        """
    )

    def _number_of_colors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfColors,
                        self.number_of_colors)

    number_of_table_values = traits.Int(256, enter_set=True, auto_set=False, help=\
        """
        Specify the number of values (i.e., colors) in the lookup table.
        """
    )

    def _number_of_table_values_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfTableValues,
                        self.number_of_table_values)

    range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 1.0), cols=2, help=\
        """
        Sets/Gets the range of scalars which will be mapped.  This is a
        duplicate of get/_set_table_range.
        """
    )

    def _range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRange,
                        self.range)

    saturation_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(1.0, 1.0), cols=2, help=\
        """
        
        """
    )

    def _saturation_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSaturationRange,
                        self.saturation_range)

    def _get_table(self):
        return wrap_vtk(self._vtk_obj.GetTable())
    def _set_table(self, arg):
        old_val = self._get_table()
        my_arg = deref_array([arg], [['vtkUnsignedCharArray']])
        self._wrap_call(self._vtk_obj.SetTable,
                        my_arg[0])
        self.trait_property_changed('table', old_val, arg)
    table = traits.Property(_get_table, _set_table, help=\
        """
        Set/Get the internal table array that is used to map the scalars
        to colors.  The table array is an unsigned char array with 4
        components representing RGBA.
        """
    )

    table_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 1.0), cols=2, help=\
        """
        Set/Get the minimum/maximum scalar values for scalar mapping.
        Scalar values less than minimum range value are clamped to
        minimum range value. Scalar values greater than maximum range
        value are clamped to maximum range value.
        
        * The table_range values are only used when indexed_lookup is
          false.
        """
    )

    def _table_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTableRange,
                        self.table_range)

    def get_table_value(self, *args):
        """
        V.get_table_value(int) -> (float, float, float, float)
        C++: double *GetTableValue(IdType id)
        V.get_table_value(int, [float, float, float, float])
        C++: void GetTableValue(IdType id, double rgba[4])
        Return a rgba color value for the given index into the lookup
        table. Color components are expressed as [0,1] double values.
        """
        ret = self._wrap_call(self._vtk_obj.GetTableValue, *args)
        return ret

    def set_table_value(self, *args):
        """
        V.set_table_value(int, [float, float, float, float])
        C++: virtual void SetTableValue(IdType indx, double rgba[4])
        V.set_table_value(int, float, float, float, float)
        C++: virtual void SetTableValue(IdType indx, double r,
            double g, double b, double a=1.0)
        Directly load color into lookup table. Use [0,1] double values
        for color component specification. Make sure that you've either
        used the Build() method or used set_number_of_table_values() prior to
        using this method.
        """
        ret = self._wrap_call(self._vtk_obj.SetTableValue, *args)
        return ret

    value_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(1.0, 1.0), cols=2, help=\
        """
        
        """
    )

    def _value_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValueRange,
                        self.value_range)

    def get_color_as_unsigned_chars(self, *args):
        """
        V.get_color_as_unsigned_chars((float, float, float, float), [int, int,
             int, int])
        C++: static void GetColorAsUnsignedChars(const double colorIn[4],
            unsigned char colorOut[4])
        Cast a double color in a type T color. color_in and color_out are
        expected to be RGBA[4] and color_in to be in [0.0, 1.0]
        """
        ret = self._wrap_call(self._vtk_obj.GetColorAsUnsignedChars, *args)
        return ret

    def get_index(self, *args):
        """
        V.get_index(float) -> int
        C++: virtual IdType GetIndex(double v)
        Return the table index associated with a particular value.
        
        * Do not use this function when indexed_lookup is true:
        * in that case, the set of values v may take on is exactly the
          integers
        * from 0 to get_number_of_table_values() - 1;
        * and v serves directly as an index into table_values.
        """
        ret = self._wrap_call(self._vtk_obj.GetIndex, *args)
        return ret

    def get_log_range(self, *args):
        """
        V.get_log_range((float, float), [float, float])
        C++: static void GetLogRange(const double range[2],
            double log_range[2])
        Returns the log of range in log_range. There is a little more to
        this than simply taking the log10 of the two range values: we do
        conversion of negative ranges to positive ranges, and conversion
        of zero to a 'very small number'.
        """
        ret = self._wrap_call(self._vtk_obj.GetLogRange, *args)
        return ret

    def _get_nan_color_as_unsigned_chars(self):
        return self._vtk_obj.GetNanColorAsUnsignedChars()
    nan_color_as_unsigned_chars = traits.Property(_get_nan_color_as_unsigned_chars, help=\
        """
        Return the nan_color as a pointer to 4 unsigned chars. This will
        overwrite any data returned by previous calls to map_value.
        """
    )

    def get_pointer(self, *args):
        """
        V.get_pointer(int) -> (int, ...)
        C++: unsigned char *GetPointer(const IdType id)
        Get pointer to color table data. Format is array of unsigned char
        r-g-b-a-r-g-b-a...
        """
        ret = self._wrap_call(self._vtk_obj.GetPointer, *args)
        return ret

    def allocate(self, *args):
        """
        V.allocate(int, int) -> int
        C++: int Allocate(int sz=256, int ext=256)
        Allocate a color table of specified size.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def apply_log_scale(self, *args):
        """
        V.apply_log_scale(float, (float, float), (float, float)) -> float
        C++: static double ApplyLogScale(double v, const double range[2],
            const double log_range[2])
        Apply log to value, with appropriate constraints.
        """
        ret = self._wrap_call(self._vtk_obj.ApplyLogScale, *args)
        return ret

    def build_special_colors(self):
        """
        V.build_special_colors()
        C++: void BuildSpecialColors()
        Copies the "special" colors into the given table.
        """
        ret = self._vtk_obj.BuildSpecialColors()
        return ret
        

    def force_build(self):
        """
        V.force_build()
        C++: virtual void ForceBuild()
        Force the lookup table to regenerate from hue, saturation, value,
        and alpha min/max values.  Table is built from a linear ramp of
        each value.  force_build() is useful if a lookup table has been
        defined manually (using set_table_value) and then an application
        decides to rebuild the lookup table using the implicit process.
        """
        ret = self._vtk_obj.ForceBuild()
        return ret
        

    def write_pointer(self, *args):
        """
        V.write_pointer(int, int) -> (int, ...)
        C++: unsigned char *WritePointer(const IdType id,
            const int number)
        Get pointer to data. Useful for direct writes into object. max_id
        is bumped by number (and memory allocated if necessary). Id is
        the location you wish to write into; number is the number of rgba
        values to write.
        
        * \warning If you modify the table data via the pointer returned
          by this
        * member function, you must call
          LookupTable::BuildSpecialColors()
        * afterwards to ensure that the special colors (below/above range
        and na_n
        * value) are up-to-date.
        """
        ret = self._wrap_call(self._vtk_obj.WritePointer, *args)
        return ret

    _updateable_traits_ = \
    (('use_above_range_color', 'GetUseAboveRangeColor'),
    ('use_below_range_color', 'GetUseBelowRangeColor'), ('indexed_lookup',
    'GetIndexedLookup'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('ramp', 'GetRamp'), ('scale',
    'GetScale'), ('vector_mode', 'GetVectorMode'), ('above_range_color',
    'GetAboveRangeColor'), ('alpha_range', 'GetAlphaRange'),
    ('below_range_color', 'GetBelowRangeColor'), ('hue_range',
    'GetHueRange'), ('nan_color', 'GetNanColor'), ('number_of_colors',
    'GetNumberOfColors'), ('number_of_table_values',
    'GetNumberOfTableValues'), ('range', 'GetRange'), ('saturation_range',
    'GetSaturationRange'), ('table_range', 'GetTableRange'),
    ('value_range', 'GetValueRange'), ('alpha', 'GetAlpha'),
    ('vector_component', 'GetVectorComponent'), ('vector_size',
    'GetVectorSize'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'indexed_lookup',
    'use_above_range_color', 'use_below_range_color', 'ramp', 'scale',
    'vector_mode', 'above_range_color', 'alpha', 'alpha_range',
    'below_range_color', 'hue_range', 'nan_color', 'number_of_colors',
    'number_of_table_values', 'range', 'saturation_range', 'table_range',
    'value_range', 'vector_component', 'vector_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LookupTable, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit LookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['indexed_lookup', 'use_above_range_color',
            'use_below_range_color'], ['ramp', 'scale', 'vector_mode'],
            ['above_range_color', 'alpha', 'alpha_range', 'below_range_color',
            'hue_range', 'nan_color', 'number_of_colors',
            'number_of_table_values', 'range', 'saturation_range', 'table_range',
            'value_range', 'vector_component', 'vector_size']),
            title='Edit LookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


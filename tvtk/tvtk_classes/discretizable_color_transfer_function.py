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

from tvtk.tvtk_classes.color_transfer_function import ColorTransferFunction


class DiscretizableColorTransferFunction(ColorTransferFunction):
    """
    DiscretizableColorTransferFunction - a combination of
    ColorTransferFunction and LookupTable.
    
    Superclass: ColorTransferFunction
    
    This is a cross between a ColorTransferFunction and a
    LookupTable selectively combining the functionality of both. This
    class is a ColorTransferFunction allowing users to specify the RGB
    control points that control the color transfer function. At the same
    time, by setting_discretize to 1 (true), one can force the transfer
    function to only have_number_of_values discrete colors.
    
    When indexed_lookup is true, this class behaves differently. The
    annotated values are considered to the be only valid values for which
    entries in the color table should be returned. The colors for
    annotated values are those specified using add_indexed_colors.
    Typically, there must be at least as many indexed colors specified as
    the annotations. For backwards compatibility, if no indexed-colors
    are specified, the colors in the lookup Table are assigned to
    annotated values by taking the modulus of their index in the list of
    annotations. If a scalar value is not present in annotated_values,
    then nan_color will be used.
    
    NOTE: One must call Build() after making any changes to the points in
    the color_transfer_function to ensure that the discrete and
    non-discrete versions match up.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDiscretizableColorTransferFunction, obj, update, **traits)
    
    discretize = tvtk_base.false_bool_trait(help=\
        """
        Set if the values are to be mapped after discretization. The
        number of discrete values is set by using set_number_of_values().
        Not set by default, i.e. color value is determined by
        interpolating at the scalar value.
        """
    )

    def _discretize_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiscretize,
                        self.discretize_)

    enable_opacity_mapping = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable the usage of the scalar opacity function.
        """
    )

    def _enable_opacity_mapping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableOpacityMapping,
                        self.enable_opacity_mapping_)

    alpha = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify an additional opacity (alpha) value to blend with. Values
        != 1 modify the resulting color consistent with the requested
        form of the output. This is typically used by an actor in order
        to blend its opacity. Overridden to pass the alpha to the
        internal LookupTable.
        """
    )

    def _alpha_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlpha,
                        self.alpha)

    def get_indexed_color(self, *args):
        """
        V.get_indexed_color(int, [float, float, float, float])
        C++: virtual void GetIndexedColor(IdType i, double rgba[4])
        Get the "indexed color" assigned to an index.
        
        * The index is used in indexed_lookup mode to assign colors to
          annotations (in the order
        * the annotations were set).
        * Subclasses must implement this and interpret how to treat the
          index.
        * LookupTable simply returns get_table_value( index %
          this->_get_number_of_table_values()).
        * ColorTransferFunction returns the color assocated with node
          index % this->_get_size().
        
        * Note that implementations *must* set the opacity (alpha)
          component of the color, even if they
        * do not provide opacity values in their colormaps. In that case,
        alpha = 1 should be used.
        """
        ret = self._wrap_call(self._vtk_obj.GetIndexedColor, *args)
        return ret

    def set_indexed_color(self, *args):
        """
        V.set_indexed_color(int, (float, float, float))
        C++: void SetIndexedColor(unsigned int index, const double rgb[3])
        V.set_indexed_color(int, float, float, float)
        C++: void SetIndexedColor(unsigned int index, double r, double g,
            double b)
        Add colors to use when indexed_lookup is true._set_indexed_color()
        will automatically call set_number_of_indexed_colors(index+_1) if the
        current number of indexed colors is not sufficient for the
        specified index and all will be initialized to the RGB values
        passed to this call.
        """
        ret = self._wrap_call(self._vtk_obj.SetIndexedColor, *args)
        return ret

    nan_color = tvtk_base.vtk_color_trait((0.5, 0.0, 0.0), help=\
        """
        Set the color to use when a na_n (not a number) is encountered. 
        This is an RGB 3-tuple color of doubles in the range [0, 1].
        Overridden to pass the nan_color to the internal LookupTable.
        """
    )

    def _nan_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNanColor,
                        self.nan_color, False)

    number_of_indexed_colors = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of indexed colors. These are used when
        indexed_lookup is true. If no indexed colors are specified, for
        backwards compatibility, this class reverts to using the
        RGBPoints for colors.
        """
    )

    def _number_of_indexed_colors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfIndexedColors,
                        self.number_of_indexed_colors)

    number_of_values = traits.Int(256, enter_set=True, auto_set=False, help=\
        """
        Set the number of values i.e. colors to be generated in the
        discrete lookup table. This has no effect if Discretize is off.
        The default is 256.
        """
    )

    def _number_of_values_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfValues,
                        self.number_of_values)

    def _get_scalar_opacity_function(self):
        return wrap_vtk(self._vtk_obj.GetScalarOpacityFunction())
    def _set_scalar_opacity_function(self, arg):
        old_val = self._get_scalar_opacity_function()
        self._wrap_call(self._vtk_obj.SetScalarOpacityFunction,
                        deref_vtk(arg))
        self.trait_property_changed('scalar_opacity_function', old_val, arg)
    scalar_opacity_function = traits.Property(_get_scalar_opacity_function, _set_scalar_opacity_function, help=\
        """
        Set/get the opacity function to use.
        """
    )

    use_log_scale = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set if log scale must be used while mapping scalars to
        colors. The default is 0.
        """
    )

    def _use_log_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseLogScale,
                        self.use_log_scale)

    def _get_rgb_points(self):
        return self._vtk_obj.GetRGBPoints()
    rgb_points = traits.Property(_get_rgb_points, help=\
        """
        Returns the (x, r, g, b) values as an array.
        ColorTransferFunction::GetDataPointer(). Retained for
        backwards compatibility.\deprecated Use get_data_pointer() instead.
        """
    )

    _updateable_traits_ = \
    (('discretize', 'GetDiscretize'), ('enable_opacity_mapping',
    'GetEnableOpacityMapping'), ('allow_duplicate_scalars',
    'GetAllowDuplicateScalars'), ('clamping', 'GetClamping'), ('hsv_wrap',
    'GetHSVWrap'), ('use_above_range_color', 'GetUseAboveRangeColor'),
    ('use_below_range_color', 'GetUseBelowRangeColor'), ('indexed_lookup',
    'GetIndexedLookup'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('color_space', 'GetColorSpace'),
    ('scale', 'GetScale'), ('vector_mode', 'GetVectorMode'), ('alpha',
    'GetAlpha'), ('nan_color', 'GetNanColor'),
    ('number_of_indexed_colors', 'GetNumberOfIndexedColors'),
    ('number_of_values', 'GetNumberOfValues'), ('use_log_scale',
    'GetUseLogScale'), ('above_range_color', 'GetAboveRangeColor'),
    ('below_range_color', 'GetBelowRangeColor'), ('range', 'GetRange'),
    ('vector_component', 'GetVectorComponent'), ('vector_size',
    'GetVectorSize'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['allow_duplicate_scalars', 'clamping', 'debug', 'discretize',
    'enable_opacity_mapping', 'global_warning_display', 'hsv_wrap',
    'indexed_lookup', 'use_above_range_color', 'use_below_range_color',
    'color_space', 'scale', 'vector_mode', 'above_range_color', 'alpha',
    'below_range_color', 'nan_color', 'number_of_indexed_colors',
    'number_of_values', 'range', 'use_log_scale', 'vector_component',
    'vector_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DiscretizableColorTransferFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DiscretizableColorTransferFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['allow_duplicate_scalars', 'clamping', 'discretize',
            'enable_opacity_mapping', 'hsv_wrap', 'indexed_lookup',
            'use_above_range_color', 'use_below_range_color'], ['color_space',
            'scale', 'vector_mode'], ['above_range_color', 'alpha',
            'below_range_color', 'nan_color', 'number_of_indexed_colors',
            'number_of_values', 'range', 'use_log_scale', 'vector_component',
            'vector_size']),
            title='Edit DiscretizableColorTransferFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DiscretizableColorTransferFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


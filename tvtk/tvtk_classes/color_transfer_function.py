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


class ColorTransferFunction(ScalarsToColors):
    """
    ColorTransferFunction - Defines a transfer function for mapping a
    property to an RGB color value.
    
    Superclass: ScalarsToColors
    
    ColorTransferFunction is a color mapping in RGB or HSV space that
    uses piecewise hermite functions to allow interpolation that can be
    piecewise constant, piecewise linear, or somewhere in-between (a
    modified piecewise hermite function that squishes the function
    according to a sharpness parameter). The function also allows for the
    specification of the midpoint (the place where the function reaches
    the average of the two bounding nodes) as a normalize distance
    between nodes. See the description of class PiecewiseFunction for
    an explanation of midpoint and sharpness.
    
    @sa
    PiecewiseFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkColorTransferFunction, obj, update, **traits)
    
    allow_duplicate_scalars = tvtk_base.false_bool_trait(help=\
        """
        Toggle whether to allow duplicate scalar values in the color
        transfer function (off by default).
        """
    )

    def _allow_duplicate_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllowDuplicateScalars,
                        self.allow_duplicate_scalars_)

    clamping = tvtk_base.true_bool_trait(help=\
        """
        Sets/gets whether clamping is used. If on, scalar values below
        the lower range value set for the transfer function will be
        mapped to the first node color, and scalar values above the upper
        range value set for the transfer function will be mapped to the
        last node color. If off, values outside the range are mapped to
        black.
        """
    )

    def _clamping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClamping,
                        self.clamping_)

    hsv_wrap = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        or Diverging.  In HSV mode, if HSVWrap is on, it will take the
        shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of LookupTable).  Diverging is a special mode
        where colors will pass through white when interpolating between
        two saturated colors.
        """
    )

    def _hsv_wrap_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHSVWrap,
                        self.hsv_wrap_)

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

    color_space = traits.Trait('rgb',
    tvtk_base.TraitRevPrefixMap({'rgb': 0, 'diverging': 3, 'hsv': 1, 'lab': 2}), help=\
        """
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        or Diverging.  In HSV mode, if HSVWrap is on, it will take the
        shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of LookupTable).  Diverging is a special mode
        where colors will pass through white when interpolating between
        two saturated colors.
        """
    )

    def _color_space_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorSpace,
                        self.color_space_)

    scale = traits.Trait('linear',
    tvtk_base.TraitRevPrefixMap({'linear': 0, 'log10': 1}), help=\
        """
        Set the type of scale to use, linear or logarithmic.  The default
        is linear.  If the scale is logarithmic, and the range contains
        zero, the color mapping will be linear.
        """
    )

    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale_)

    above_range_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )

    def _above_range_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAboveRangeColor,
                        self.above_range_color, False)

    below_range_color = tvtk_base.vtk_color_trait((0.0, 0.0, 0.0), help=\
        """
        
        """
    )

    def _below_range_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBelowRangeColor,
                        self.below_range_color, False)

    nan_color = tvtk_base.vtk_color_trait((0.5, 0.0, 0.0), help=\
        """
        
        """
    )

    def _nan_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNanColor,
                        self.nan_color, False)

    def get_node_value(self, *args):
        """
        V.get_node_value(int, [float, float, float, float, float, float])
            -> int
        C++: int GetNodeValue(int index, double val[6])
        For the node specified by index, set/get the location (X), R, G,
        and B values, midpoint, and sharpness values at the node.
        """
        ret = self._wrap_call(self._vtk_obj.GetNodeValue, *args)
        return ret

    def set_node_value(self, *args):
        """
        V.set_node_value(int, [float, float, float, float, float, float])
            -> int
        C++: int SetNodeValue(int index, double val[6])
        For the node specified by index, set/get the location (X), R, G,
        and B values, midpoint, and sharpness values at the node.
        """
        ret = self._wrap_call(self._vtk_obj.SetNodeValue, *args)
        return ret

    range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 0.0), cols=2, help=\
        """
        Sets/Gets the range of scalars that will be mapped.
        """
    )

    def _range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRange,
                        self.range)

    def get_blue_value(self, *args):
        """
        V.get_blue_value(float) -> float
        C++: double GetBlueValue(double x)
        Get the color components individually.
        """
        ret = self._wrap_call(self._vtk_obj.GetBlueValue, *args)
        return ret

    def _get_clamping_max_value(self):
        return self._vtk_obj.GetClampingMaxValue()
    clamping_max_value = traits.Property(_get_clamping_max_value, help=\
        """
        Sets/gets whether clamping is used. If on, scalar values below
        the lower range value set for the transfer function will be
        mapped to the first node color, and scalar values above the upper
        range value set for the transfer function will be mapped to the
        last node color. If off, values outside the range are mapped to
        black.
        """
    )

    def _get_clamping_min_value(self):
        return self._vtk_obj.GetClampingMinValue()
    clamping_min_value = traits.Property(_get_clamping_min_value, help=\
        """
        Sets/gets whether clamping is used. If on, scalar values below
        the lower range value set for the transfer function will be
        mapped to the first node color, and scalar values above the upper
        range value set for the transfer function will be mapped to the
        last node color. If off, values outside the range are mapped to
        black.
        """
    )

    def _get_data_pointer(self):
        return self._vtk_obj.GetDataPointer()
    data_pointer = traits.Property(_get_data_pointer, help=\
        """
        Returns a pointer to an array of all node values in an
        interleaved array with the layout [X1, R1, G1, B1, X2, R2, G2,
        B2, ..., Xn, Rn, Gn, Bn] where n is the number of nodes defining
        the transfer function. The returned pointer points to an array
        that is managed by this class, so callers should not free it.
        """
    )

    def get_green_value(self, *args):
        """
        V.get_green_value(float) -> float
        C++: double GetGreenValue(double x)
        Get the color components individually.
        """
        ret = self._wrap_call(self._vtk_obj.GetGreenValue, *args)
        return ret

    def get_red_value(self, *args):
        """
        V.get_red_value(float) -> float
        C++: double GetRedValue(double x)
        Get the color components individually.
        """
        ret = self._wrap_call(self._vtk_obj.GetRedValue, *args)
        return ret

    def _get_size(self):
        return self._vtk_obj.GetSize()
    size = traits.Property(_get_size, help=\
        """
        How many nodes define this function?
        """
    )

    def get_table(self, *args):
        """
        V.get_table(float, float, int, [float, ...])
        C++: void GetTable(double x1, double x2, int n, double *table)
        V.get_table(float, float, int) -> (int, ...)
        C++: const unsigned char *GetTable(double x1, double x2, int n)
        Fills in a table of n colors mapped from values mapped with even
        spacing between x1 and x2, inclusive.
        
        * Note that get_table ignores indexed_lookup
        """
        ret = self._wrap_call(self._vtk_obj.GetTable, *args)
        return ret

    def add_hsv_point(self, *args):
        """
        V.add_hsv_point(float, float, float, float) -> int
        C++: int AddHSVPoint(double x, double h, double s, double v)
        V.add_hsv_point(float, float, float, float, float, float) -> int
        C++: int AddHSVPoint(double x, double h, double s, double v,
            double midpoint, double sharpness)
        Add/Remove a point to/from the function defined in RGB or HSV
        Return the index of the point (0 based), or -1 on error. See the
        description of class PiecewiseFunction for an explanation of
        midpoint and sharpness.
        """
        ret = self._wrap_call(self._vtk_obj.AddHSVPoint, *args)
        return ret

    def add_hsv_segment(self, *args):
        """
        V.add_hsv_segment(float, float, float, float, float, float, float,
            float)
        C++: void AddHSVSegment(double x1, double h1, double s1,
            double v1, double x2, double h2, double s2, double v2)
        Add two points to the function and remove all the points between
        them
        """
        ret = self._wrap_call(self._vtk_obj.AddHSVSegment, *args)
        return ret

    def add_rgb_point(self, *args):
        """
        V.add_rgb_point(float, float, float, float) -> int
        C++: int AddRGBPoint(double x, double r, double g, double b)
        V.add_rgb_point(float, float, float, float, float, float) -> int
        C++: int AddRGBPoint(double x, double r, double g, double b,
            double midpoint, double sharpness)
        Add/Remove a point to/from the function defined in RGB or HSV
        Return the index of the point (0 based), or -1 on error. See the
        description of class PiecewiseFunction for an explanation of
        midpoint and sharpness.
        """
        ret = self._wrap_call(self._vtk_obj.AddRGBPoint, *args)
        return ret

    def add_rgb_segment(self, *args):
        """
        V.add_rgb_segment(float, float, float, float, float, float, float,
            float)
        C++: void AddRGBSegment(double x1, double r1, double g1,
            double b1, double x2, double r2, double g2, double b2)
        Add two points to the function and remove all the points between
        them
        """
        ret = self._wrap_call(self._vtk_obj.AddRGBSegment, *args)
        return ret

    def adjust_range(self, *args):
        """
        V.adjust_range([float, float]) -> int
        C++: int AdjustRange(double range[2])
        Remove all points out of the new range, and make sure there is a
        point at each end of that range. Returns 1 on success, 0
        otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.AdjustRange, *args)
        return ret

    def build_function_from_table(self, *args):
        """
        V.build_function_from_table(float, float, int, [float, ...])
        C++: void BuildFunctionFromTable(double x1, double x2, int size,
            double *table)
        Construct a color transfer function from a table. Unlike
        fill_from_data_pointer(), the table parameter's layout is assumed to
        be [R1, G1, B1, R2, G2, B2, ..., Rn, Gn, Bn], and it is assumed
        to be a block of memory of size [3*size]. After calling this
        method, the function range will be [x1, x2], the function will
        have size nodes, and function values will be regularly spaced
        between x1 and x2.
        """
        ret = self._wrap_call(self._vtk_obj.BuildFunctionFromTable, *args)
        return ret

    def estimate_min_number_of_samples(self, *args):
        """
        V.estimate_min_number_of_samples(float, float) -> int
        C++: int EstimateMinNumberOfSamples(double const &x1,
            double const &x2)
        Estimates the minimum size of a table such that it would
        correctly sample this function. The returned value should be
        passed as parameter 'n' when calling get_table().
        """
        ret = self._wrap_call(self._vtk_obj.EstimateMinNumberOfSamples, *args)
        return ret

    def fill_from_data_pointer(self, *args):
        """
        V.fill_from_data_pointer(int, [float, ...])
        C++: void FillFromDataPointer(int n, double *ptr)
        Defines the nodes from an array ptr with the layout [X1, R1, G1,
        B1, X2, R2, G2, B2, ..., Xn, Rn, Gn, Bn] where n is the number of
        nodes.
        """
        ret = self._wrap_call(self._vtk_obj.FillFromDataPointer, *args)
        return ret

    def remove_all_points(self):
        """
        V.remove_all_points()
        C++: void RemoveAllPoints()
        Remove all points
        """
        ret = self._vtk_obj.RemoveAllPoints()
        return ret
        

    def remove_point(self, *args):
        """
        V.remove_point(float) -> int
        C++: int RemovePoint(double x)
        Add/Remove a point to/from the function defined in RGB or HSV
        Return the index of the point (0 based), or -1 on error. See the
        description of class PiecewiseFunction for an explanation of
        midpoint and sharpness.
        """
        ret = self._wrap_call(self._vtk_obj.RemovePoint, *args)
        return ret

    def shallow_copy(self, *args):
        """
        V.shallow_copy(ColorTransferFunction)
        C++: void ShallowCopy(ColorTransferFunction *f)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    _updateable_traits_ = \
    (('allow_duplicate_scalars', 'GetAllowDuplicateScalars'), ('clamping',
    'GetClamping'), ('hsv_wrap', 'GetHSVWrap'), ('use_above_range_color',
    'GetUseAboveRangeColor'), ('use_below_range_color',
    'GetUseBelowRangeColor'), ('indexed_lookup', 'GetIndexedLookup'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('color_space', 'GetColorSpace'),
    ('scale', 'GetScale'), ('vector_mode', 'GetVectorMode'),
    ('above_range_color', 'GetAboveRangeColor'), ('below_range_color',
    'GetBelowRangeColor'), ('nan_color', 'GetNanColor'), ('range',
    'GetRange'), ('alpha', 'GetAlpha'), ('vector_component',
    'GetVectorComponent'), ('vector_size', 'GetVectorSize'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['allow_duplicate_scalars', 'clamping', 'debug',
    'global_warning_display', 'hsv_wrap', 'indexed_lookup',
    'use_above_range_color', 'use_below_range_color', 'color_space',
    'scale', 'vector_mode', 'above_range_color', 'alpha',
    'below_range_color', 'nan_color', 'range', 'vector_component',
    'vector_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ColorTransferFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ColorTransferFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['allow_duplicate_scalars', 'clamping', 'hsv_wrap',
            'indexed_lookup', 'use_above_range_color', 'use_below_range_color'],
            ['color_space', 'scale', 'vector_mode'], ['above_range_color',
            'alpha', 'below_range_color', 'nan_color', 'range',
            'vector_component', 'vector_size']),
            title='Edit ColorTransferFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ColorTransferFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


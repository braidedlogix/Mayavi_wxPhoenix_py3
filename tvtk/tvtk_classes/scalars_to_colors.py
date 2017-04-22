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

from tvtk.tvtk_classes.object import Object


class ScalarsToColors(Object):
    """
    ScalarsToColors - Superclass for mapping scalar values to colors
    
    Superclass: Object
    
    ScalarsToColors is a general-purpose base class for objects that
    convert scalars to colors. This include LookupTable classes and
    color transfer functions.  By itself, this class will simply rescale
    the scalars.
    
    The scalar-to-color mapping can be augmented with an additional
    uniform alpha blend. This is used, for example, to blend a Actor's
    opacity with the lookup table values.
    
    Specific scalar values may be annotated with text strings that will
    be included in color legends using set_annotations,
    set_annotation,_get_number_of_annotated_values, get_annotated_value,
    get_annotation,_remove_annotation, and reset_annotations.
    
    This class also has a method for indicating that the set of annotated
    values form a categorical color map; by setting \a indexed_lookup to
    true, you indicate that the annotated values are the only valid
    values for which entries in the color table should be returned. In
    this mode, subclasses should then assign colors to annotated values
    by taking the modulus of an annotated value's index in the list of
    annotations with the number of colors in the table.
    
    @sa
    LookupTable ColorTransferFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScalarsToColors, obj, update, **traits)
    
    indexed_lookup = tvtk_base.false_bool_trait(help=\
        """
        Set/get whether the lookup table is for categorical or ordinal
        data. The default is ordinal data; values not present in the
        lookup table will be assigned an interpolated color.
        
        * When categorical data is present, only values in the lookup
          table will be
        * considered valid; all other values will be assigned nan_color.
        """
    )

    def _indexed_lookup_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIndexedLookup,
                        self.indexed_lookup_)

    vector_mode = traits.Trait('component',
    tvtk_base.TraitRevPrefixMap({'component': 1, 'magnitude': 0, 'rgb_colors': 2}), help=\
        """
        Change mode that maps vectors by magnitude vs. component. If the
        mode is "RGBColors", then the vectors components are scaled to
        the range and passed directly as the colors.
        """
    )

    def _vector_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorMode,
                        self.vector_mode_)

    alpha = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify an additional opacity (alpha) value to blend with. Values
        != 1 modify the resulting color consistent with the requested
        form of the output. This is typically used by an actor in order
        to blend its opacity. Value is clamped between 0 and 1.
        """
    )

    def _alpha_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlpha,
                        self.alpha)

    def get_annotation(self, *args):
        """
        V.get_annotation(int) -> string
        C++: StdString GetAnnotation(IdType idx)
        Return the annotation at a particular index in the list of
        annotations.
        """
        ret = self._wrap_call(self._vtk_obj.GetAnnotation, *args)
        return ret

    def set_annotation(self, *args):
        """
        V.set_annotation(Variant, string) -> int
        C++: virtual IdType SetAnnotation(Variant value,
            StdString annotation)
        V.set_annotation(string, string) -> int
        C++: virtual IdType SetAnnotation(StdString value,
            StdString annotation)
        Add a new entry (or change an existing entry) to the list of
        annotated values. Returns the index of value in the list of
        annotations.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetAnnotation, *my_args)
        return ret

    def get_annotations(self):
        """
        V.get_annotations() -> StringArray
        C++: StringArray *GetAnnotations()
        Set a list of discrete values, either as a categorical set of
        values (when indexed_lookup is true) or as a set of annotations to
        add to a scalar array (when indexed_lookup is false). The two
        arrays must both either be NULL or of the same length or the call
        will be ignored.
        
        * Note that these arrays are deep copied rather than being used
          directly
        * in order to support the use case where edits are made. If the
        * values and annotations arrays were held by this class then each
        * call to map scalar values to colors would require us to check
          the MTime
        * of the arrays.
        """
        ret = wrap_vtk(self._vtk_obj.GetAnnotations())
        return ret
        

    def set_annotations(self, *args):
        """
        V.set_annotations(AbstractArray, StringArray)
        C++: virtual void SetAnnotations(AbstractArray *values,
            StringArray *annotations)
        Set a list of discrete values, either as a categorical set of
        values (when indexed_lookup is true) or as a set of annotations to
        add to a scalar array (when indexed_lookup is false). The two
        arrays must both either be NULL or of the same length or the call
        will be ignored.
        
        * Note that these arrays are deep copied rather than being used
          directly
        * in order to support the use case where edits are made. If the
        * values and annotations arrays were held by this class then each
        * call to map scalar values to colors would require us to check
          the MTime
        * of the arrays.
        """
        my_args = deref_array(args, [('vtkAbstractArray', 'vtkStringArray')])
        ret = self._wrap_call(self._vtk_obj.SetAnnotations, *my_args)
        return ret

    range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 255.0), cols=2, help=\
        """
        Sets/Gets the range of scalars that will be mapped.
        """
    )

    def _range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRange,
                        self.range)

    vector_component = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        If the mapper does not select which component of a vector to map
        to colors, you can specify it here.
        """
    )

    def _vector_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorComponent,
                        self.vector_component)

    vector_size = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        When mapping vectors, consider only the number of components
        selected by vector_size to be part of the vector, and ignore any
        other components.  Set to -1 to map all components.  If this is
        not set to -1, then you can use set_vector_component to set which
        scalar component will be the first component in the vector to be
        mapped.
        """
    )

    def _vector_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorSize,
                        self.vector_size)

    def get_annotated_value(self, *args):
        """
        V.get_annotated_value(int) -> Variant
        C++: Variant GetAnnotatedValue(IdType idx)
        Return the annotated value at a particular index in the list of
        annotations.
        """
        ret = self._wrap_call(self._vtk_obj.GetAnnotatedValue, *args)
        return wrap_vtk(ret)

    def get_annotated_value_index(self, *args):
        """
        V.get_annotated_value_index(Variant) -> int
        C++: IdType GetAnnotatedValueIndex(Variant val)
        Return the index of the given value in the list of annotated
        values (or -1 if not present).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetAnnotatedValueIndex, *my_args)
        return ret

    def get_annotated_value_index_internal(self, *args):
        """
        V.get_annotated_value_index_internal(Variant) -> int
        C++: IdType GetAnnotatedValueIndexInternal(Variant &val)
        Look up an index into the array of annotations given a value.
        Does no pointer checks. Returns -1 when val not present.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetAnnotatedValueIndexInternal, *my_args)
        return ret

    def _get_annotated_values(self):
        return wrap_vtk(self._vtk_obj.GetAnnotatedValues())
    annotated_values = traits.Property(_get_annotated_values, help=\
        """
        Set a list of discrete values, either as a categorical set of
        values (when indexed_lookup is true) or as a set of annotations to
        add to a scalar array (when indexed_lookup is false). The two
        arrays must both either be NULL or of the same length or the call
        will be ignored.
        
        * Note that these arrays are deep copied rather than being used
          directly
        * in order to support the use case where edits are made. If the
        * values and annotations arrays were held by this class then each
        * call to map scalar values to colors would require us to check
          the MTime
        * of the arrays.
        """
    )

    def get_annotation_color(self, *args):
        """
        V.get_annotation_color(Variant, [float, float, float, float])
        C++: virtual void GetAnnotationColor(const Variant &val,
            double rgba[4])
        Obtain the color associated with a particular annotated value (or
        nan_color if unmatched).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetAnnotationColor, *my_args)
        return ret

    def get_color(self, *args):
        """
        V.get_color(float, [float, float, float])
        C++: virtual void GetColor(double v, double rgb[3])
        V.get_color(float) -> (float, float, float)
        C++: double *GetColor(double v)
        Map one value through the lookup table and store the color as an
        RGB array of doubles between 0 and 1 in the rgb argument.
        """
        ret = self._wrap_call(self._vtk_obj.GetColor, *args)
        return ret

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

    def get_luminance(self, *args):
        """
        V.get_luminance(float) -> float
        C++: double GetLuminance(double x)
        Map one value through the lookup table and return the luminance
        0.3*red + 0.59*green + 0.11*blue as a double between 0 and 1.
        Returns the luminance value for the specified scalar value.
        """
        ret = self._wrap_call(self._vtk_obj.GetLuminance, *args)
        return ret

    def _get_number_of_annotated_values(self):
        return self._vtk_obj.GetNumberOfAnnotatedValues()
    number_of_annotated_values = traits.Property(_get_number_of_annotated_values, help=\
        """
        Return the annotated value at a particular index in the list of
        annotations.
        """
    )

    def _get_number_of_available_colors(self):
        return self._vtk_obj.GetNumberOfAvailableColors()
    number_of_available_colors = traits.Property(_get_number_of_available_colors, help=\
        """
        Get the number of available colors for mapping to.
        """
    )

    def get_opacity(self, *args):
        """
        V.get_opacity(float) -> float
        C++: virtual double GetOpacity(double v)
        Map one value through the lookup table and return the alpha value
        (the opacity) as a double between 0 and 1. This implementation
        always returns 1.
        """
        ret = self._wrap_call(self._vtk_obj.GetOpacity, *args)
        return ret

    def build(self):
        """
        V.build()
        C++: virtual void Build()
        Perform any processing required (if any) before processing
        scalars. Default implementation does nothing.
        """
        ret = self._vtk_obj.Build()
        return ret
        

    def deep_copy(self, *args):
        """
        V.deep_copy(ScalarsToColors)
        C++: virtual void DeepCopy(ScalarsToColors *o)
        Copy the contents from another object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def is_opaque(self):
        """
        V.is_opaque() -> int
        C++: virtual int IsOpaque()
        Return true if all of the values defining the mapping have an
        opacity equal to 1. Default implementation return true.
        """
        ret = self._vtk_obj.IsOpaque()
        return ret
        

    def map_scalars(self, *args):
        """
        V.map_scalars(DataArray, int, int) -> UnsignedCharArray
        C++: virtual UnsignedCharArray *MapScalars(
            DataArray *scalars, int colorMode, int component)
        V.map_scalars(AbstractArray, int, int) -> UnsignedCharArray
        C++: virtual UnsignedCharArray *MapScalars(
            AbstractArray *scalars, int colorMode, int component)
        Internal methods that map a data array into a 4-component,
        unsigned char RGBA array. The color mode determines the behavior
        of mapping. If VTK_COLOR_MODE_DEFAULT is set, then unsigned char
        data arrays are treated as colors (and converted to RGBA if
        necessary); If VTK_COLOR_MODE_DIRECT_SCALARS is set, then all
        arrays are treated as colors (integer types are clamped in the
        range 0-255, floating point arrays are clamped in the range
        0.0-1.0. Note 'char' does not have enough values to represent a
        color so mapping this type is considered an error); otherwise,
        the data is mapped through this instance of scalars_to_colors. The
        component argument is used for data arrays with more than one
        component; it indicates which component to use to do the
        blending.  When the component argument is -1, then the this
        object uses its own selected technique to change a vector into a
        scalar to map.
        """
        my_args = deref_array(args, [('vtkDataArray', 'int', 'int'), ('vtkAbstractArray', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.MapScalars, *my_args)
        return wrap_vtk(ret)

    def map_scalars_through_table(self, *args):
        """
        V.map_scalars_through_table(DataArray, [int, ...], int)
        C++: void MapScalarsThroughTable(DataArray *scalars,
            unsigned char *output, int outputFormat)
        V.map_scalars_through_table(DataArray, [int, ...])
        C++: void MapScalarsThroughTable(DataArray *scalars,
            unsigned char *output)
        V.map_scalars_through_table(void, [int, ...], int, int, int, int)
        C++: void MapScalarsThroughTable(void *input,
            unsigned char *output, int inputDataType, int numberOfValues,
            int inputIncrement, int outputFormat)
        Map a set of scalars through the lookup table in a single
        operation. This method ignores the vector_mode and the
        vector_component. The output format can be set to VTK_RGBA (4
        components), VTK_RGB (3 components), VTK_LUMINANCE (1 component,
        greyscale), or VTK_LUMINANCE_ALPHA (2 components) If not
        supplied, the output format defaults to RGBA.
        """
        my_args = deref_array(args, [('vtkDataArray', ['int', Ellipsis], 'int'), ('vtkDataArray', ['int', Ellipsis]), ('void', ['int', Ellipsis], 'int', 'int', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.MapScalarsThroughTable, *my_args)
        return ret

    def map_scalars_through_table2(self, *args):
        """
        V.map_scalars_through_table2(void, [int, ...], int, int, int, int)
        C++: virtual void MapScalarsThroughTable2(void *input,
            unsigned char *output, int inputDataType, int numberOfValues,
            int inputIncrement, int outputFormat)
        An internal method typically not used in applications.  This
        should be a protected function, but it must be kept public for
        backwards compatibility.  Never call this method directly.
        """
        ret = self._wrap_call(self._vtk_obj.MapScalarsThroughTable2, *args)
        return ret

    def map_value(self, *args):
        """
        V.map_value(float) -> (int, ...)
        C++: virtual unsigned char *MapValue(double v)
        Map one value through the lookup table and return a color defined
        as a RGBA unsigned char tuple (4 bytes).
        """
        ret = self._wrap_call(self._vtk_obj.MapValue, *args)
        return ret

    def map_vectors_through_table(self, *args):
        """
        V.map_vectors_through_table(void, [int, ...], int, int, int, int,
            int, int)
        C++: void MapVectorsThroughTable(void *input,
            unsigned char *output, int inputDataType, int numberOfValues,
            int inputIncrement, int outputFormat, int vectorComponent,
            int vectorSize)
        V.map_vectors_through_table(void, [int, ...], int, int, int, int)
        C++: void MapVectorsThroughTable(void *input,
            unsigned char *output, int inputDataType, int numberOfValues,
            int inputIncrement, int outputFormat)
        Map vectors through the lookup table.  Unlike
        map_scalars_through_table, this method will use the vector_mode to
        decide how to map vectors. The output format can be set to
        VTK_RGBA (4 components), VTK_RGB (3 components), VTK_LUMINANCE (1
        component, greyscale), or VTK_LUMINANCE_ALPHA (2 components)
        """
        ret = self._wrap_call(self._vtk_obj.MapVectorsThroughTable, *args)
        return ret

    def remove_annotation(self, *args):
        """
        V.remove_annotation(Variant) -> bool
        C++: virtual bool RemoveAnnotation(Variant value)
        Remove an existing entry from the list of annotated values.
        
        * Returns true when the entry was actually removed (i.e., it
          existed before the call).
        * Otherwise, returns false.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveAnnotation, *my_args)
        return ret

    def reset_annotations(self):
        """
        V.reset_annotations()
        C++: virtual void ResetAnnotations()
        Remove all existing values and their annotations.
        """
        ret = self._vtk_obj.ResetAnnotations()
        return ret
        

    def using_log_scale(self):
        """
        V.using_log_scale() -> int
        C++: virtual int UsingLogScale()
        This should return 1 is the subclass is using log scale for
        mapping scalars to colors. Default implementation always returns
        0.
        """
        ret = self._vtk_obj.UsingLogScale()
        return ret
        

    _updateable_traits_ = \
    (('indexed_lookup', 'GetIndexedLookup'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('vector_mode',
    'GetVectorMode'), ('alpha', 'GetAlpha'), ('range', 'GetRange'),
    ('vector_component', 'GetVectorComponent'), ('vector_size',
    'GetVectorSize'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'indexed_lookup', 'vector_mode',
    'alpha', 'range', 'vector_component', 'vector_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScalarsToColors, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ScalarsToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['indexed_lookup'], ['vector_mode'], ['alpha', 'range',
            'vector_component', 'vector_size']),
            title='Edit ScalarsToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScalarsToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


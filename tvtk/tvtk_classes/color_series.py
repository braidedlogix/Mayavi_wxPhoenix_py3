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


class ColorSeries(Object):
    """
    ColorSeries - stores a list of colors.
    
    Superclass: Object
    
    The ColorSeries stores palettes of colors. There are several
    default palettes (or schemes) available and functions to control
    several aspects of what colors are returned. In essence a color
    scheme is set and then the number of colors and individual color
    values may be requested.
    
    It is also possible to add schemes beyond the default palettes.
    Whenever set_color_scheme is called with a string for which no palette
    already exists, a new, empty palette is created. You may then use
    set_number_of_colors and set_color to populate the palette. You may not
    extend default palettes by calling functions that alter a scheme; if
    called while a predefined palette is in use, they will create a new
    non-default scheme and populate it with the current palette before
    continuing.
    
    The "Brewer" palettes are courtesy of Cynthia A. Brewer (Dept. of
    Geography, Pennsylvania State University) and present under the
    Apache License. See the source code for details.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkColorSeries, obj, update, **traits)
    
    def get_color(self, *args):
        """
        V.get_color(int) -> Color3ub
        C++: Color3ub GetColor(int index)
        Get the color at the specified index. If the index is out of
        range then black will be returned.
        """
        ret = self._wrap_call(self._vtk_obj.GetColor, *args)
        return wrap_vtk(ret)

    def set_color(self, *args):
        """
        V.set_color(int, Color3ub)
        C++: virtual void SetColor(int index, const Color3ub &color)
        Set the color at the specified index. Does nothing if the index
        is out of range.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetColor, *my_args)
        return ret

    color_scheme = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the color scheme that should be used. The variant of this
        function that takes an integer should pass a number from those in
        the enum, or a value returned by the string variant. The variant
        that accepts a string returns the integer index of the resulting
        palette (whether it already existed or is newly-created).
        """
    )

    def _color_scheme_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorScheme,
                        self.color_scheme)

    color_scheme_name = traits.String('Spectrum', enter_set=True, auto_set=False, help=\
        """
        Set the name of the current color scheme
        """
    )

    def _color_scheme_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorSchemeName,
                        self.color_scheme_name)

    number_of_colors = traits.Int(7, enter_set=True, auto_set=False, help=\
        """
        Set the number of colors to be stored in a non-default color
        scheme. Calling this function on a predefined color scheme will
        cause the scheme to be duplicated to a new custom scheme.
        """
    )

    def _number_of_colors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfColors,
                        self.number_of_colors)

    def get_color_repeating(self, *args):
        """
        V.get_color_repeating(int) -> Color3ub
        C++: Color3ub GetColorRepeating(int index)
        Get the color at the specified index. If the index is out of
        range then the call wraps around, i.e. uses the mod operator.
        """
        ret = self._wrap_call(self._vtk_obj.GetColorRepeating, *args)
        return wrap_vtk(ret)

    def _get_number_of_color_schemes(self):
        return self._vtk_obj.GetNumberOfColorSchemes()
    number_of_color_schemes = traits.Property(_get_number_of_color_schemes, help=\
        """
        Return the number of schemes currently defined.
        """
    )

    def add_color(self, *args):
        """
        V.add_color(Color3ub)
        C++: virtual void AddColor(const Color3ub &color)
        Adds the color to the end of the list.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddColor, *my_args)
        return ret

    def build_lookup_table(self, *args):
        """
        V.build_lookup_table(LookupTable, int)
        C++: void BuildLookupTable(LookupTable *lkup,
            int lutIndexing=ColorSeries::CATEGORICAL)
        Populate a lookup table with all the colors in the current
        scheme.
        
        * The default behavior is to return categorical data. Set
          lut_indexing
        * to ORDINAL to return ordinal data. Any other value for
          lut_indexing
        * is treated as CATEGORICAL.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.BuildLookupTable, *my_args)
        return ret

    def clear_colors(self):
        """
        V.clear_colors()
        C++: virtual void ClearColors()
        Clears the list of colors.
        """
        ret = self._vtk_obj.ClearColors()
        return ret
        

    def create_lookup_table(self, *args):
        """
        V.create_lookup_table(int) -> LookupTable
        C++: LookupTable *CreateLookupTable(
            int lutIndexing=ColorSeries::CATEGORICAL)
        Create a new lookup table with all the colors in the current
        scheme.
        
        * The caller is responsible for deleting the table after use.
        
        * The default behavior is to return categorical data. Set
          lut_indexing
        * to ORDINAL to return ordinal data. Any other value for
          lut_indexing
        * is treated as CATEGORICAL.
        """
        ret = self._wrap_call(self._vtk_obj.CreateLookupTable, *args)
        return wrap_vtk(ret)

    def deep_copy(self, *args):
        """
        V.deep_copy(ColorSeries)
        C++: virtual void DeepCopy(ColorSeries *chartColors)
        Make a deep copy of the supplied object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def insert_color(self, *args):
        """
        V.insert_color(int, Color3ub)
        C++: virtual void InsertColor(int index, const Color3ub &color)
        Inserts the color at the specified index in the list.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InsertColor, *my_args)
        return ret

    def remove_color(self, *args):
        """
        V.remove_color(int)
        C++: virtual void RemoveColor(int index)
        Removes the color at the specified index in the list.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveColor, *args)
        return ret

    def set_color_scheme_by_name(self, *args):
        """
        V.set_color_scheme_by_name(string) -> int
        C++: virtual int SetColorSchemeByName(
            const StdString &schemeName)
        Set the color scheme that should be used. The variant of this
        function that takes an integer should pass a number from those in
        the enum, or a value returned by the string variant. The variant
        that accepts a string returns the integer index of the resulting
        palette (whether it already existed or is newly-created).
        """
        ret = self._wrap_call(self._vtk_obj.SetColorSchemeByName, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('color_scheme', 'GetColorScheme'),
    ('color_scheme_name', 'GetColorSchemeName'), ('number_of_colors',
    'GetNumberOfColors'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'color_scheme',
    'color_scheme_name', 'number_of_colors'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ColorSeries, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ColorSeries properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['color_scheme', 'color_scheme_name',
            'number_of_colors']),
            title='Edit ColorSeries properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ColorSeries properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


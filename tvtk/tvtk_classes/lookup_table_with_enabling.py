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

from tvtk.tvtk_classes.lookup_table import LookupTable


class LookupTableWithEnabling(LookupTable):
    """
    LookupTableWithEnabling - A lookup table that allows for an
    optional array to be provided that specifies which scalars to
    "enable" and which to "disable".
    
    Superclass: LookupTable
    
    LookupTableWithEnabling "disables" or "grays out" output colors
    based on whether the given value in enabled_array is "0" or not.
    
    @warning
    You must set the enabled_array before map_scalars() is called. Indices
    of enabled_array must map directly to those of the array passed to
    map_scalars().
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLookupTableWithEnabling, obj, update, **traits)
    
    def _get_enabled_array(self):
        return wrap_vtk(self._vtk_obj.GetEnabledArray())
    def _set_enabled_array(self, arg):
        old_val = self._get_enabled_array()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetEnabledArray,
                        my_arg[0])
        self.trait_property_changed('enabled_array', old_val, arg)
    enabled_array = traits.Property(_get_enabled_array, _set_enabled_array, help=\
        """
        This must be set before map_scalars() is called. Indices of this
        array must map directly to those in the scalars array passed to
        map_scalars(). Values of 0 in the array indicate the color should
        be desaturatated.
        """
    )

    def disable_color(self, *args):
        """
        V.disable_color(int, int, int, [int, ...], [int, ...], [int, ...])
        C++: virtual void DisableColor(unsigned char r, unsigned char g,
            unsigned char b, unsigned char *rd, unsigned char *gd,
            unsigned char *bd)
        A convenience method for taking a color and desaturating it.
        """
        ret = self._wrap_call(self._vtk_obj.DisableColor, *args)
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
            return super(LookupTableWithEnabling, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit LookupTableWithEnabling properties', scrollable=True, resizable=True,
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
            title='Edit LookupTableWithEnabling properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LookupTableWithEnabling properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


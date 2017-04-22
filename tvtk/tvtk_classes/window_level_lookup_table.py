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


class WindowLevelLookupTable(LookupTable):
    """
    WindowLevelLookupTable - map scalar values into colors or colors
    to scalars; generate color table
    
    Superclass: LookupTable
    
    WindowLevelLookupTable is an object that is used by mapper objects
    to map scalar values into rgba (red-green-blue-alpha transparency)
    color specification, or rgba into scalar values. The color table can
    be created by direct insertion of color values, or by specifying a
    window and level. Window / Level is used in medical imaging to
    specify a linear greyscale ramp. The Level is the center of the ramp.
     The Window is the width of the ramp.
    
    @warning
    WindowLevelLookupTable is a reference counted object. Therefore,
    you should always use operator "new" to construct new objects. This
    procedure will avoid memory problems (see text).
    
    @sa
    LogLookupTable
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWindowLevelLookupTable, obj, update, **traits)
    
    inverse_video = tvtk_base.false_bool_trait(help=\
        """
        Set inverse video on or off.  You can achieve the same effect by
        switching the minimum_table_value and the maximum_table_value.
        """
    )

    def _inverse_video_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInverseVideo,
                        self.inverse_video_)

    level = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set the Level for the lookup table.  The level is the average of
        table_range[_0] and table_range[_1].
        """
    )

    def _level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLevel,
                        self.level)

    maximum_table_value = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(1.0, 1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _maximum_table_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumTableValue,
                        self.maximum_table_value)

    minimum_table_value = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, 0.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _minimum_table_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumTableValue,
                        self.minimum_table_value)

    window = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the window for the lookup table.  The window is the
        difference between table_range[_0] and table_range[_1].
        """
    )

    def _window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWindow,
                        self.window)

    _updateable_traits_ = \
    (('inverse_video', 'GetInverseVideo'), ('use_above_range_color',
    'GetUseAboveRangeColor'), ('use_below_range_color',
    'GetUseBelowRangeColor'), ('indexed_lookup', 'GetIndexedLookup'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('ramp', 'GetRamp'), ('scale',
    'GetScale'), ('vector_mode', 'GetVectorMode'), ('level', 'GetLevel'),
    ('maximum_table_value', 'GetMaximumTableValue'),
    ('minimum_table_value', 'GetMinimumTableValue'), ('window',
    'GetWindow'), ('above_range_color', 'GetAboveRangeColor'),
    ('alpha_range', 'GetAlphaRange'), ('below_range_color',
    'GetBelowRangeColor'), ('hue_range', 'GetHueRange'), ('nan_color',
    'GetNanColor'), ('number_of_colors', 'GetNumberOfColors'),
    ('number_of_table_values', 'GetNumberOfTableValues'), ('range',
    'GetRange'), ('saturation_range', 'GetSaturationRange'),
    ('table_range', 'GetTableRange'), ('value_range', 'GetValueRange'),
    ('alpha', 'GetAlpha'), ('vector_component', 'GetVectorComponent'),
    ('vector_size', 'GetVectorSize'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'indexed_lookup',
    'inverse_video', 'use_above_range_color', 'use_below_range_color',
    'ramp', 'scale', 'vector_mode', 'above_range_color', 'alpha',
    'alpha_range', 'below_range_color', 'hue_range', 'level',
    'maximum_table_value', 'minimum_table_value', 'nan_color',
    'number_of_colors', 'number_of_table_values', 'range',
    'saturation_range', 'table_range', 'value_range', 'vector_component',
    'vector_size', 'window'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WindowLevelLookupTable, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit WindowLevelLookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['indexed_lookup', 'inverse_video', 'use_above_range_color',
            'use_below_range_color'], ['ramp', 'scale', 'vector_mode'],
            ['above_range_color', 'alpha', 'alpha_range', 'below_range_color',
            'hue_range', 'level', 'maximum_table_value', 'minimum_table_value',
            'nan_color', 'number_of_colors', 'number_of_table_values', 'range',
            'saturation_range', 'table_range', 'value_range', 'vector_component',
            'vector_size', 'window']),
            title='Edit WindowLevelLookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WindowLevelLookupTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class ImageProperty(Object):
    """
    ImageProperty - image display properties
    
    Superclass: Object
    
    ImageProperty is an object that allows control of the display of
    an image slice.@par Thanks: Thanks to David Gobbi at the Seaman
    Family MR Centre and Dept. of Clinical Neurosciences, Foothills
    Medical Centre, Calgary, for providing this class.
    @sa
    Image ImageMapper3D ImageSliceMapper ImageResliceMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageProperty, obj, update, **traits)
    
    backing = tvtk_base.false_bool_trait(help=\
        """
        Use an opaque backing polygon, which will be visible where the
        image is translucent.  When images are in a stack, the backing
        polygons for all images will be drawn before any of the images in
        the stack, in order to allow the images in the stack to be
        composited.
        """
    )

    def _backing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBacking,
                        self.backing_)

    checkerboard = tvtk_base.false_bool_trait(help=\
        """
        Make a checkerboard pattern where the black squares are
        transparent. The pattern is aligned with the camera, and centered
        by default.
        """
    )

    def _checkerboard_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCheckerboard,
                        self.checkerboard_)

    use_lookup_table_scalar_range = tvtk_base.false_bool_trait(help=\
        """
        Use the range that is set in the lookup table, instead of setting
        the range from the Window/Level settings. This is off by default.
        """
    )

    def _use_lookup_table_scalar_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseLookupTableScalarRange,
                        self.use_lookup_table_scalar_range_)

    interpolation_type = traits.Trait('linear',
    tvtk_base.TraitRevPrefixMap({'linear': 1, 'cubic': 2, 'nearest': 0}), help=\
        """
        The interpolation type (default: nearest neighbor).
        """
    )

    def _interpolation_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolationType,
                        self.interpolation_type_)

    ambient = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        The ambient lighting coefficient.  The default is 1.0.
        """
    )

    def _ambient_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAmbient,
                        self.ambient)

    backing_color = tvtk_base.vtk_color_trait((0.0, 0.0, 0.0), help=\
        """
        
        """
    )

    def _backing_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackingColor,
                        self.backing_color, False)

    checkerboard_offset = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 0.0), cols=2, help=\
        """
        
        """
    )

    def _checkerboard_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCheckerboardOffset,
                        self.checkerboard_offset)

    checkerboard_spacing = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(10.0, 10.0), cols=2, help=\
        """
        
        """
    )

    def _checkerboard_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCheckerboardSpacing,
                        self.checkerboard_spacing)

    color_level = traits.Float(127.5, enter_set=True, auto_set=False, help=\
        """
        The level value for window/level.
        """
    )

    def _color_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorLevel,
                        self.color_level)

    color_window = traits.Float(255.0, enter_set=True, auto_set=False, help=\
        """
        The window value for window/level.
        """
    )

    def _color_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorWindow,
                        self.color_window)

    diffuse = traits.Trait(0.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        The diffuse lighting coefficient.  The default is 0.0.
        """
    )

    def _diffuse_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiffuse,
                        self.diffuse)

    layer_number = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the layer number.  This is ignored unless the image is part
        of a ImageStack.  The default layer number is zero.
        """
    )

    def _layer_number_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLayerNumber,
                        self.layer_number)

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Specify a lookup table for the data.  If the data is to be
        displayed as greyscale, or if the input data is already RGB,
        there is no need to set a lookup table.
        """
    )

    opacity = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        The opacity of the image, where 1.0 is opaque and 0.0 is
        transparent.  If the image has an alpha component, then the alpha
        component will be multiplied by this value.
        """
    )

    def _opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOpacity,
                        self.opacity)

    def deep_copy(self, *args):
        """
        V.deep_copy(ImageProperty)
        C++: void DeepCopy(ImageProperty *p)
        Assign one property to another.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    _updateable_traits_ = \
    (('backing', 'GetBacking'), ('checkerboard', 'GetCheckerboard'),
    ('use_lookup_table_scalar_range', 'GetUseLookupTableScalarRange'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interpolation_type',
    'GetInterpolationType'), ('ambient', 'GetAmbient'), ('backing_color',
    'GetBackingColor'), ('checkerboard_offset', 'GetCheckerboardOffset'),
    ('checkerboard_spacing', 'GetCheckerboardSpacing'), ('color_level',
    'GetColorLevel'), ('color_window', 'GetColorWindow'), ('diffuse',
    'GetDiffuse'), ('layer_number', 'GetLayerNumber'), ('opacity',
    'GetOpacity'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['backing', 'checkerboard', 'debug', 'global_warning_display',
    'use_lookup_table_scalar_range', 'interpolation_type', 'ambient',
    'backing_color', 'checkerboard_offset', 'checkerboard_spacing',
    'color_level', 'color_window', 'diffuse', 'layer_number', 'opacity'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageProperty, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['backing', 'checkerboard', 'use_lookup_table_scalar_range'],
            ['interpolation_type'], ['ambient', 'backing_color',
            'checkerboard_offset', 'checkerboard_spacing', 'color_level',
            'color_window', 'diffuse', 'layer_number', 'opacity']),
            title='Edit ImageProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


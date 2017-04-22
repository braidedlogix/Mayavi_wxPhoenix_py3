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


class VolumeProperty(Object):
    """
    VolumeProperty - represents the common properties for rendering a
    volume.
    
    Superclass: Object
    
    VolumeProperty is used to represent common properties associated
    with volume rendering. This includes properties for determining the
    type of interpolation to use when sampling a volume, the color of a
    volume, the scalar opacity of a volume, the gradient opacity of a
    volume, and the shading parameters of a volume.
    
    When the scalar opacity or the gradient opacity of a volume is not
    set, then the function is defined to be a constant value of 1.0. When
    a scalar and gradient opacity are both set simultaneously, then the
    opacity is defined to be the product of the scalar opacity and
    gradient opacity transfer functions.
    
    Most properties can be set per "component" for volume mappers that
    support multiple independent components. If you are using 2 component
    data as LV or 4 component data as RGBV (as specified in the mapper)
    only the first scalar opacity and gradient opacity transfer functions
    will be used (and all color functions will be ignored). Omitting the
    index parameter on the Set/Get methods will access index = 0.
    
    @sa
    PiecewiseFunction ColorTransferFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeProperty, obj, update, **traits)
    
    disable_gradient_opacity = tvtk_base.false_bool_trait(help=\
        """
        Enable/Disable the gradient opacity function for the given
        component. If set to true, any call to get_gradient_opacity() will
        return a default function for this component. Note that the
        gradient opacity function is still stored, it is not set or reset
        and can be retrieved using get_stored_gradient_opacity().
        """
    )

    def _disable_gradient_opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisableGradientOpacity,
                        self.disable_gradient_opacity_)

    independent_components = tvtk_base.true_bool_trait(help=\
        """
        Does the data have independent components, or do some define
        color only? If independent_components is On (the default) then
        each component will be independently passed through a lookup
        table to determine RGBA, shaded. Some volume Mappers can handle 1
        to 4 component unsigned char or unsigned short data (see each
        mapper header file to determine functionality). If
        independent_components is Off, then you must have either 2 or 4
        component data. For 2 component data, the first is passed through
        the first color transfer function and the second component is
        passed through the first scalar opacity (and gradient opacity)
        transfer function. Normals will be generated off of the second
        component. When using gradient based opacity modulation, the
        gradients are computed off of the second component. For 4
        component data, the first three will directly represent RGB (no
        lookup table). The fourth component will be passed through the
        first scalar opacity transfer function for opacity and first
        gradient opacity transfer function for gradient based opacity
        modulation. Normals will be generated from the fourth component.
        When using gradient based opacity modulation, the gradients are
        computed off of the fourth component.
        """
    )

    def _independent_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIndependentComponents,
                        self.independent_components_)

    shade = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the shading of a volume. If shading is turned off, then
        the mapper for the volume will not perform shading calculations.
        If shading is turned on, the mapper may perform shading
        calculations - in some cases shading does not apply (for example,
        in a maximum intensity projection) and therefore shading will not
        be performed even if this flag is on. For a compositing type of
        mapper, turning shading off is generally the same as setting
        ambient=1, diffuse=0, specular=0. Shading can be independently
        turned on/off per component.
        
        ote Shading is only supported for
        VolumeMapper::COMPOSITE_BLEND. For minimum and maximum
        intensity blend modes, there is not necessarily one unique
        location along the ray through the volume where that minimum or
        maximum occurs. For average and additive blend modes, the value
        being visualized does not represent a location in the volume but
        rather a statistical measurement along the ray traversing through
        the volume, and hence shading is not applicable.
        \sa VolumeMapper::BlendModes
        """
    )

    def _shade_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShade,
                        self.shade_)

    interpolation_type = traits.Trait('nearest',
    tvtk_base.TraitRevPrefixMap({'nearest': 0, 'linear': 1}), help=\
        """
        Set the interpolation type for sampling a volume. Initial value
        is VTK_NEAREST_INTERPOLATION.
        """
    )

    def _interpolation_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolationType,
                        self.interpolation_type_)

    ambient = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the ambient lighting coefficient.
        """
    )

    def _ambient_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAmbient,
                        self.ambient)

    def get_component_weight(self, *args):
        """
        V.get_component_weight(int) -> float
        C++: virtual double GetComponentWeight(int index)
        Set/Get the scalar component weights. Clamped between the range
        of (0.0, 1.0)
        """
        ret = self._wrap_call(self._vtk_obj.GetComponentWeight, *args)
        return ret

    def set_component_weight(self, *args):
        """
        V.set_component_weight(int, float)
        C++: virtual void SetComponentWeight(int index, double value)
        Set/Get the scalar component weights. Clamped between the range
        of (0.0, 1.0)
        """
        ret = self._wrap_call(self._vtk_obj.SetComponentWeight, *args)
        return ret

    diffuse = traits.Float(0.7, enter_set=True, auto_set=False, help=\
        """
        Set/Get the diffuse lighting coefficient.
        """
    )

    def _diffuse_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiffuse,
                        self.diffuse)

    def get_gradient_opacity(self, *args):
        """
        V.get_gradient_opacity(int) -> PiecewiseFunction
        C++: PiecewiseFunction *GetGradientOpacity(int index)
        V.get_gradient_opacity() -> PiecewiseFunction
        C++: PiecewiseFunction *GetGradientOpacity()
        Get the gradient magnitude opacity transfer function for the
        given component. If no transfer function has been set for this
        component, a default one is created and returned. This default
        function is always returned if disable_gradient_opacity is On for
        that component.
        """
        ret = self._wrap_call(self._vtk_obj.GetGradientOpacity, *args)
        return wrap_vtk(ret)

    def set_gradient_opacity(self, *args):
        """
        V.set_gradient_opacity(int, PiecewiseFunction)
        C++: void SetGradientOpacity(int index,
            PiecewiseFunction *function)
        V.set_gradient_opacity(PiecewiseFunction)
        C++: void SetGradientOpacity(PiecewiseFunction *function)
        Set the opacity of a volume to an opacity transfer function based
        on gradient magnitude for the given component.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGradientOpacity, *my_args)
        return ret

    def get_scalar_opacity(self, *args):
        """
        V.get_scalar_opacity(int) -> PiecewiseFunction
        C++: PiecewiseFunction *GetScalarOpacity(int index)
        V.get_scalar_opacity() -> PiecewiseFunction
        C++: PiecewiseFunction *GetScalarOpacity()
        Get the scalar opacity transfer function for the given component.
        If no transfer function has been set for this component, a
        default one is created and returned.
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarOpacity, *args)
        return wrap_vtk(ret)

    def set_scalar_opacity(self, *args):
        """
        V.set_scalar_opacity(int, PiecewiseFunction)
        C++: void SetScalarOpacity(int index,
            PiecewiseFunction *function)
        V.set_scalar_opacity(PiecewiseFunction)
        C++: void SetScalarOpacity(PiecewiseFunction *function)
        Set the opacity of a volume to an opacity transfer function based
        on scalar value for the component indicated by index.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetScalarOpacity, *my_args)
        return ret

    scalar_opacity_unit_distance = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the unit distance on which the scalar opacity transfer
        function is defined. By default this is 1.0, meaning that over a
        distance of 1.0 units, a given opacity (from the transfer
        function) is accumulated. This is adjusted for the actual
        sampling distance during rendering.
        """
    )

    def _scalar_opacity_unit_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarOpacityUnitDistance,
                        self.scalar_opacity_unit_distance)

    specular = traits.Float(0.2, enter_set=True, auto_set=False, help=\
        """
        Set/Get the specular lighting coefficient.
        """
    )

    def _specular_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpecular,
                        self.specular)

    specular_power = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the specular power.
        """
    )

    def _specular_power_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpecularPower,
                        self.specular_power)

    def _get_color_channels(self):
        return self._vtk_obj.GetColorChannels()
    color_channels = traits.Property(_get_color_channels, help=\
        """
        Get the number of color channels in the transfer function for the
        given component.
        """
    )

    def _get_gradient_opacity_m_time(self):
        return wrap_vtk(self._vtk_obj.GetGradientOpacityMTime())
    gradient_opacity_m_time = traits.Property(_get_gradient_opacity_m_time, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE Get the
        time that the gradient opacity transfer function was set
        """
    )

    def _get_gray_transfer_function(self):
        return wrap_vtk(self._vtk_obj.GetGrayTransferFunction())
    gray_transfer_function = traits.Property(_get_gray_transfer_function, help=\
        """
        Get the gray transfer function. If no transfer function has been
        set for this component, a default one is created and returned.
        """
    )

    def _get_gray_transfer_function_m_time(self):
        return wrap_vtk(self._vtk_obj.GetGrayTransferFunctionMTime())
    gray_transfer_function_m_time = traits.Property(_get_gray_transfer_function_m_time, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE Get the
        time that the gray_transfer_function was set
        """
    )

    def _get_independent_components_max_value(self):
        return self._vtk_obj.GetIndependentComponentsMaxValue()
    independent_components_max_value = traits.Property(_get_independent_components_max_value, help=\
        """
        Does the data have independent components, or do some define
        color only? If independent_components is On (the default) then
        each component will be independently passed through a lookup
        table to determine RGBA, shaded. Some volume Mappers can handle 1
        to 4 component unsigned char or unsigned short data (see each
        mapper header file to determine functionality). If
        independent_components is Off, then you must have either 2 or 4
        component data. For 2 component data, the first is passed through
        the first color transfer function and the second component is
        passed through the first scalar opacity (and gradient opacity)
        transfer function. Normals will be generated off of the second
        component. When using gradient based opacity modulation, the
        gradients are computed off of the second component. For 4
        component data, the first three will directly represent RGB (no
        lookup table). The fourth component will be passed through the
        first scalar opacity transfer function for opacity and first
        gradient opacity transfer function for gradient based opacity
        modulation. Normals will be generated from the fourth component.
        When using gradient based opacity modulation, the gradients are
        computed off of the fourth component.
        """
    )

    def _get_independent_components_min_value(self):
        return self._vtk_obj.GetIndependentComponentsMinValue()
    independent_components_min_value = traits.Property(_get_independent_components_min_value, help=\
        """
        Does the data have independent components, or do some define
        color only? If independent_components is On (the default) then
        each component will be independently passed through a lookup
        table to determine RGBA, shaded. Some volume Mappers can handle 1
        to 4 component unsigned char or unsigned short data (see each
        mapper header file to determine functionality). If
        independent_components is Off, then you must have either 2 or 4
        component data. For 2 component data, the first is passed through
        the first color transfer function and the second component is
        passed through the first scalar opacity (and gradient opacity)
        transfer function. Normals will be generated off of the second
        component. When using gradient based opacity modulation, the
        gradients are computed off of the second component. For 4
        component data, the first three will directly represent RGB (no
        lookup table). The fourth component will be passed through the
        first scalar opacity transfer function for opacity and first
        gradient opacity transfer function for gradient based opacity
        modulation. Normals will be generated from the fourth component.
        When using gradient based opacity modulation, the gradients are
        computed off of the fourth component.
        """
    )

    def _get_rgb_transfer_function(self):
        return wrap_vtk(self._vtk_obj.GetRGBTransferFunction())
    rgb_transfer_function = traits.Property(_get_rgb_transfer_function, help=\
        """
        Get the RGB transfer function for the given component. If no
        transfer function has been set for this component, a default one
        is created and returned.
        """
    )

    def _get_rgb_transfer_function_m_time(self):
        return wrap_vtk(self._vtk_obj.GetRGBTransferFunctionMTime())
    rgb_transfer_function_m_time = traits.Property(_get_rgb_transfer_function_m_time, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE Get the
        time that the rgb_transfer_function was set
        """
    )

    def _get_scalar_opacity_m_time(self):
        return wrap_vtk(self._vtk_obj.GetScalarOpacityMTime())
    scalar_opacity_m_time = traits.Property(_get_scalar_opacity_m_time, help=\
        """
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE Get the
        time that the scalar opacity transfer function was set.
        """
    )

    def _get_stored_gradient_opacity(self):
        return wrap_vtk(self._vtk_obj.GetStoredGradientOpacity())
    stored_gradient_opacity = traits.Property(_get_stored_gradient_opacity, help=\
        """
        Enable/Disable the gradient opacity function for the given
        component. If set to true, any call to get_gradient_opacity() will
        return a default function for this component. Note that the
        gradient opacity function is still stored, it is not set or reset
        and can be retrieved using get_stored_gradient_opacity().
        """
    )

    def deep_copy(self, *args):
        """
        V.deep_copy(VolumeProperty)
        C++: void DeepCopy(VolumeProperty *p)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def has_gradient_opacity(self, *args):
        """
        V.has_gradient_opacity(int) -> bool
        C++: bool HasGradientOpacity(int index=0)
        Check whether or not we have the gradient opacity. Checking
        gradient opacity via get_disable_gradient_opacity or
        get_gradient_opacity will not work as in the former case, 
        get_disable_gradient_opacity returns false by default and in the
        later case, a default gradient opacity will be created.
        """
        ret = self._wrap_call(self._vtk_obj.HasGradientOpacity, *args)
        return ret

    def set_color(self, *args):
        """
        V.set_color(int, PiecewiseFunction)
        C++: void SetColor(int index, PiecewiseFunction *function)
        V.set_color(PiecewiseFunction)
        C++: void SetColor(PiecewiseFunction *function)
        V.set_color(int, ColorTransferFunction)
        C++: void SetColor(int index, ColorTransferFunction *function)
        V.set_color(ColorTransferFunction)
        C++: void SetColor(ColorTransferFunction *function)
        Set the color of a volume to a gray level transfer function for
        the component indicated by index. This will set the color
        channels for this component to 1.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetColor, *my_args)
        return ret

    def update_m_times(self):
        """
        V.update_m_times()
        C++: void UpdateMTimes()
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE
        update_m_times performs a Modified() on all time_stamps. This is
        used by Volume when the property is set, so that any other
        object that might have been caching information for the property
        will rebuild.
        """
        ret = self._vtk_obj.UpdateMTimes()
        return ret
        

    _updateable_traits_ = \
    (('disable_gradient_opacity', 'GetDisableGradientOpacity'),
    ('independent_components', 'GetIndependentComponents'), ('shade',
    'GetShade'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interpolation_type',
    'GetInterpolationType'), ('ambient', 'GetAmbient'), ('diffuse',
    'GetDiffuse'), ('scalar_opacity_unit_distance',
    'GetScalarOpacityUnitDistance'), ('specular', 'GetSpecular'),
    ('specular_power', 'GetSpecularPower'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'disable_gradient_opacity', 'global_warning_display',
    'independent_components', 'shade', 'interpolation_type', 'ambient',
    'diffuse', 'scalar_opacity_unit_distance', 'specular',
    'specular_power'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeProperty, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['disable_gradient_opacity', 'independent_components', 'shade'],
            ['interpolation_type'], ['ambient', 'diffuse',
            'scalar_opacity_unit_distance', 'specular', 'specular_power']),
            title='Edit VolumeProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


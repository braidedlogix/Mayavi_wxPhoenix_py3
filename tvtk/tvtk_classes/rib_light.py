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

from tvtk.tvtk_classes.light import Light


class RIBLight(Light):
    """
    RIBLight - RIP Light
    
    Superclass: Light
    
    RIBLight is a subclass of Light that allows the user to specify
    light source shaders and shadow casting lights for use with
    render_man.
    
    @sa
    RIBExporter RIBProperty
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRIBLight, obj, update, **traits)
    
    shadows = tvtk_base.false_bool_trait(help=\
        """
        
        """
    )

    def _shadows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShadows,
                        self.shadows_)

    _updateable_traits_ = \
    (('shadows', 'GetShadows'), ('positional', 'GetPositional'),
    ('switch', 'GetSwitch'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('light_type',
    'GetLightType'), ('ambient_color', 'GetAmbientColor'),
    ('attenuation_values', 'GetAttenuationValues'), ('cone_angle',
    'GetConeAngle'), ('diffuse_color', 'GetDiffuseColor'), ('exponent',
    'GetExponent'), ('focal_point', 'GetFocalPoint'), ('intensity',
    'GetIntensity'), ('position', 'GetPosition'), ('shadow_attenuation',
    'GetShadowAttenuation'), ('specular_color', 'GetSpecularColor'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'positional', 'shadows',
    'switch', 'light_type', 'ambient_color', 'attenuation_values',
    'cone_angle', 'diffuse_color', 'exponent', 'focal_point', 'intensity',
    'position', 'shadow_attenuation', 'specular_color'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RIBLight, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RIBLight properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['positional', 'shadows', 'switch'], ['light_type'],
            ['ambient_color', 'attenuation_values', 'cone_angle', 'diffuse_color',
            'exponent', 'focal_point', 'intensity', 'position',
            'shadow_attenuation', 'specular_color']),
            title='Edit RIBLight properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RIBLight properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


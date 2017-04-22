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


class OpenGLLight(Light):
    """
    OpenGLLight - open_gl light
    
    Superclass: Light
    
    OpenGLLight is a concrete implementation of the abstract class
    Light. OpenGLLight interfaces to the open_gl rendering library.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLLight, obj, update, **traits)
    
    _updateable_traits_ = \
    (('positional', 'GetPositional'), ('switch', 'GetSwitch'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('light_type', 'GetLightType'), ('ambient_color', 'GetAmbientColor'),
    ('attenuation_values', 'GetAttenuationValues'), ('cone_angle',
    'GetConeAngle'), ('diffuse_color', 'GetDiffuseColor'), ('exponent',
    'GetExponent'), ('focal_point', 'GetFocalPoint'), ('intensity',
    'GetIntensity'), ('position', 'GetPosition'), ('shadow_attenuation',
    'GetShadowAttenuation'), ('specular_color', 'GetSpecularColor'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'positional', 'switch',
    'light_type', 'ambient_color', 'attenuation_values', 'cone_angle',
    'diffuse_color', 'exponent', 'focal_point', 'intensity', 'position',
    'shadow_attenuation', 'specular_color'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLLight, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLLight properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['positional', 'switch'], ['light_type'], ['ambient_color',
            'attenuation_values', 'cone_angle', 'diffuse_color', 'exponent',
            'focal_point', 'intensity', 'position', 'shadow_attenuation',
            'specular_color']),
            title='Edit OpenGLLight properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLLight properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


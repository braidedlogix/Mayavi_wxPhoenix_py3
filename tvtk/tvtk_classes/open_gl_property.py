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

from tvtk.tvtk_classes.property import Property


class OpenGLProperty(Property):
    """
    OpenGLProperty - open_gl property
    
    Superclass: Property
    
    OpenGLProperty is a concrete implementation of the abstract class
    Property. OpenGLProperty interfaces to the open_gl rendering
    library.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLProperty, obj, update, **traits)
    
    _updateable_traits_ = \
    (('backface_culling', 'GetBackfaceCulling'), ('edge_visibility',
    'GetEdgeVisibility'), ('frontface_culling', 'GetFrontfaceCulling'),
    ('lighting', 'GetLighting'), ('render_lines_as_tubes',
    'GetRenderLinesAsTubes'), ('render_points_as_spheres',
    'GetRenderPointsAsSpheres'), ('shading', 'GetShading'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('interpolation', 'GetInterpolation'), ('representation',
    'GetRepresentation'), ('ambient', 'GetAmbient'), ('ambient_color',
    'GetAmbientColor'), ('color', 'GetColor'), ('diffuse', 'GetDiffuse'),
    ('diffuse_color', 'GetDiffuseColor'), ('edge_color', 'GetEdgeColor'),
    ('line_stipple_pattern', 'GetLineStipplePattern'),
    ('line_stipple_repeat_factor', 'GetLineStippleRepeatFactor'),
    ('line_width', 'GetLineWidth'), ('opacity', 'GetOpacity'),
    ('point_size', 'GetPointSize'), ('specular', 'GetSpecular'),
    ('specular_color', 'GetSpecularColor'), ('specular_power',
    'GetSpecularPower'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['backface_culling', 'debug', 'edge_visibility', 'frontface_culling',
    'global_warning_display', 'lighting', 'render_lines_as_tubes',
    'render_points_as_spheres', 'shading', 'interpolation',
    'representation', 'ambient', 'ambient_color', 'color', 'diffuse',
    'diffuse_color', 'edge_color', 'line_stipple_pattern',
    'line_stipple_repeat_factor', 'line_width', 'opacity', 'point_size',
    'specular', 'specular_color', 'specular_power'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLProperty, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['backface_culling', 'edge_visibility', 'frontface_culling',
            'lighting', 'render_lines_as_tubes', 'render_points_as_spheres',
            'shading'], ['interpolation', 'representation'], ['ambient',
            'ambient_color', 'color', 'diffuse', 'diffuse_color', 'edge_color',
            'line_stipple_pattern', 'line_stipple_repeat_factor', 'line_width',
            'opacity', 'point_size', 'specular', 'specular_color',
            'specular_power']),
            title='Edit OpenGLProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class RIBProperty(Property):
    """
    RIBProperty - RIP Property
    
    Superclass: Property
    
    RIBProperty is a subclass of Property that allows the user to
    specify named shaders for use with render_man. Both surface and
    displacement shaders can be specified. Parameters for the shaders can
    be declared and set.
    
    @sa
    RIBExporter RIBLight
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRIBProperty, obj, update, **traits)
    
    surface_shader_uses_default_parameters = tvtk_base.true_bool_trait(help=\
        """
        If true (default) the surface shader uses the usual shader
        parameters: Ka - Ambient amount Kd - Diffuse amount Ks - Specular
        amount Roughness specular_color Additional surface shader
        parameters can be added with the set/_add_surface_shader_parameter
        methods. If false, all surface shader parameters must be
        specified
        """
    )

    def _surface_shader_uses_default_parameters_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSurfaceShaderUsesDefaultParameters,
                        self.surface_shader_uses_default_parameters_)

    displacement_shader = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify the name of a displacement shader.
        """
    )

    def _displacement_shader_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplacementShader,
                        self.displacement_shader)

    surface_shader = traits.String('plastic', enter_set=True, auto_set=False, help=\
        """
        Specify the name of a surface shader.
        """
    )

    def _surface_shader_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSurfaceShader,
                        self.surface_shader)

    def _get_declarations(self):
        return self._vtk_obj.GetDeclarations()
    declarations = traits.Property(_get_declarations, help=\
        """
        Get variable declarations
        """
    )

    def _get_displacement_shader_parameters(self):
        return self._vtk_obj.GetDisplacementShaderParameters()
    displacement_shader_parameters = traits.Property(_get_displacement_shader_parameters, help=\
        """
        Get parameters.
        """
    )

    def _get_parameters(self):
        return self._vtk_obj.GetParameters()
    parameters = traits.Property(_get_parameters, help=\
        """
        Get parameters.
        """
    )

    def _get_surface_shader_parameters(self):
        return self._vtk_obj.GetSurfaceShaderParameters()
    surface_shader_parameters = traits.Property(_get_surface_shader_parameters, help=\
        """
        Get parameters.
        """
    )

    def add_displacement_shader_parameter(self, *args):
        """
        V.add_displacement_shader_parameter(string, string)
        C++: void AddDisplacementShaderParameter(const char *parameter,
            const char *value)
        Specify parameter values for displacement shader parameters
        """
        ret = self._wrap_call(self._vtk_obj.AddDisplacementShaderParameter, *args)
        return ret

    def add_parameter(self, *args):
        """
        V.add_parameter(string, string)
        C++: void AddParameter(const char *parameter, const char *value)
        Specify parameter values for variables. DEPRECATED: use
        (_set/_add)_surface_shader_parameter instead.
        """
        ret = self._wrap_call(self._vtk_obj.AddParameter, *args)
        return ret

    def add_surface_shader_parameter(self, *args):
        """
        V.add_surface_shader_parameter(string, string)
        C++: void AddSurfaceShaderParameter(const char *parameter,
            const char *value)
        Specify parameter values for surface shader parameters
        """
        ret = self._wrap_call(self._vtk_obj.AddSurfaceShaderParameter, *args)
        return ret

    def add_variable(self, *args):
        """
        V.add_variable(string, string)
        C++: void AddVariable(const char *variable,
            const char *declaration)
        Specify declarations for variables..
        """
        ret = self._wrap_call(self._vtk_obj.AddVariable, *args)
        return ret

    def set_displacement_shader_parameter(self, *args):
        """
        V.set_displacement_shader_parameter(string, string)
        C++: void SetDisplacementShaderParameter(const char *parameter,
            const char *value)
        Specify parameter values for displacement shader parameters
        """
        ret = self._wrap_call(self._vtk_obj.SetDisplacementShaderParameter, *args)
        return ret

    def set_parameter(self, *args):
        """
        V.set_parameter(string, string)
        C++: void SetParameter(const char *parameter, const char *value)
        Specify parameter values for variables. DEPRECATED: use
        (_set/_add)_surface_shader_parameter instead.
        """
        ret = self._wrap_call(self._vtk_obj.SetParameter, *args)
        return ret

    def set_surface_shader_parameter(self, *args):
        """
        V.set_surface_shader_parameter(string, string)
        C++: void SetSurfaceShaderParameter(const char *parameter,
            const char *value)
        Specify parameter values for surface shader parameters
        """
        ret = self._wrap_call(self._vtk_obj.SetSurfaceShaderParameter, *args)
        return ret

    def set_variable(self, *args):
        """
        V.set_variable(string, string)
        C++: void SetVariable(const char *variable,
            const char *declaration)
        Specify declarations for variables..
        """
        ret = self._wrap_call(self._vtk_obj.SetVariable, *args)
        return ret

    _updateable_traits_ = \
    (('surface_shader_uses_default_parameters',
    'GetSurfaceShaderUsesDefaultParameters'), ('backface_culling',
    'GetBackfaceCulling'), ('edge_visibility', 'GetEdgeVisibility'),
    ('frontface_culling', 'GetFrontfaceCulling'), ('lighting',
    'GetLighting'), ('render_lines_as_tubes', 'GetRenderLinesAsTubes'),
    ('render_points_as_spheres', 'GetRenderPointsAsSpheres'), ('shading',
    'GetShading'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interpolation', 'GetInterpolation'),
    ('representation', 'GetRepresentation'), ('displacement_shader',
    'GetDisplacementShader'), ('surface_shader', 'GetSurfaceShader'),
    ('ambient', 'GetAmbient'), ('ambient_color', 'GetAmbientColor'),
    ('color', 'GetColor'), ('diffuse', 'GetDiffuse'), ('diffuse_color',
    'GetDiffuseColor'), ('edge_color', 'GetEdgeColor'),
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
    'render_points_as_spheres', 'shading',
    'surface_shader_uses_default_parameters', 'interpolation',
    'representation', 'ambient', 'ambient_color', 'color', 'diffuse',
    'diffuse_color', 'displacement_shader', 'edge_color',
    'line_stipple_pattern', 'line_stipple_repeat_factor', 'line_width',
    'opacity', 'point_size', 'specular', 'specular_color',
    'specular_power', 'surface_shader'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RIBProperty, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RIBProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['backface_culling', 'edge_visibility', 'frontface_culling',
            'lighting', 'render_lines_as_tubes', 'render_points_as_spheres',
            'shading', 'surface_shader_uses_default_parameters'],
            ['interpolation', 'representation'], ['ambient', 'ambient_color',
            'color', 'diffuse', 'diffuse_color', 'displacement_shader',
            'edge_color', 'line_stipple_pattern', 'line_stipple_repeat_factor',
            'line_width', 'opacity', 'point_size', 'specular', 'specular_color',
            'specular_power', 'surface_shader']),
            title='Edit RIBProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RIBProperty properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class ParametricFunctionSource(PolyDataAlgorithm):
    """
    ParametricFunctionSource - tessellate parametric functions
    
    Superclass: PolyDataAlgorithm
    
    This class tessellates parametric functions. The user must specify
    how many points in the parametric coordinate directions are required
    (i.e., the resolution), and the mode to use to generate scalars.
    
    @par Thanks: Andrew Maclean andrew.amaclean@gmail.com for creating
    and contributing the class.
    
    @sa
    ParametricFunction
    
    @sa
    Implementation of parametrics for 1d lines: ParametricSpline
    
    @sa
    Subclasses of ParametricFunction implementing non-orentable
    surfaces: ParametricBoy ParametricCrossCap
    ParametricFigure8Klein ParametricKlein ParametricMobius
    ParametricRoman
    
    @sa
    Subclasses of ParametricFunction implementing orientable surfaces:
    ParametricConicSpiral ParametricDini ParametricEllipsoid
    ParametricEnneper ParametricRandomHills
    ParametricSuperEllipsoid ParametricSuperToroid
    ParametricTorus
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParametricFunctionSource, obj, update, **traits)
    
    generate_normals = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the generation of normals. This is on by default. Note
        that this is only applicable to parametric surfaces whose
        parametric dimension is 2.
        """
    )

    def _generate_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateNormals,
                        self.generate_normals_)

    generate_texture_coordinates = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the generation of texture coordinates. This is off by
        default. Note that this is only applicable to parametric surfaces
        whose parametric dimension is 2. Note that texturing may fail in
        some cases.
        """
    )

    def _generate_texture_coordinates_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateTextureCoordinates,
                        self.generate_texture_coordinates_)

    scalar_mode = traits.Trait('none',
    tvtk_base.TraitRevPrefixMap({'none': 0, 'distance': 12, 'function_defined': 13, 'modulus': 6, 'phase': 7, 'quadrant': 8, 'u': 1, 'u0': 3, 'u0v0': 5, 'v': 2, 'v0': 4, 'x': 9, 'y': 10, 'z': 11}), help=\
        """
        Get/Set the mode used for the scalar data. See SCALAR_MODE for a
        description of the types of scalars generated.
        """
    )

    def _scalar_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarMode,
                        self.scalar_mode_)

    output_points_precision = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get the desired precision for the output points. See the
        documentation for the Algorithm::Precision enum for an
        explanation of the available precision settings.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

    def _get_parametric_function(self):
        return wrap_vtk(self._vtk_obj.GetParametricFunction())
    def _set_parametric_function(self, arg):
        old_val = self._get_parametric_function()
        self._wrap_call(self._vtk_obj.SetParametricFunction,
                        deref_vtk(arg))
        self.trait_property_changed('parametric_function', old_val, arg)
    parametric_function = traits.Property(_get_parametric_function, _set_parametric_function, help=\
        """
        Specify the parametric function to use to generate the
        tessellation.
        """
    )

    u_resolution = traits.Trait(50, traits.Range(2, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of subdivisions / tessellations in the u
        parametric direction. Note that the number of tessellant points
        in the u direction is the UResolution + 1.
        """
    )

    def _u_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUResolution,
                        self.u_resolution)

    v_resolution = traits.Trait(50, traits.Range(2, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of subdivisions / tessellations in the v
        parametric direction. Note that the number of tessellant points
        in the v direction is the VResolution + 1.
        """
    )

    def _v_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVResolution,
                        self.v_resolution)

    w_resolution = traits.Trait(50, traits.Range(2, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of subdivisions / tessellations in the w
        parametric direction. Note that the number of tessellant points
        in the w direction is the WResolution + 1.
        """
    )

    def _w_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWResolution,
                        self.w_resolution)

    def _get_generate_normals_max_value(self):
        return self._vtk_obj.GetGenerateNormalsMaxValue()
    generate_normals_max_value = traits.Property(_get_generate_normals_max_value, help=\
        """
        Set/Get the generation of normals. This is on by default. Note
        that this is only applicable to parametric surfaces whose
        parametric dimension is 2.
        """
    )

    def _get_generate_normals_min_value(self):
        return self._vtk_obj.GetGenerateNormalsMinValue()
    generate_normals_min_value = traits.Property(_get_generate_normals_min_value, help=\
        """
        Set/Get the generation of normals. This is on by default. Note
        that this is only applicable to parametric surfaces whose
        parametric dimension is 2.
        """
    )

    def _get_generate_texture_coordinates_max_value(self):
        return self._vtk_obj.GetGenerateTextureCoordinatesMaxValue()
    generate_texture_coordinates_max_value = traits.Property(_get_generate_texture_coordinates_max_value, help=\
        """
        Set/Get the generation of texture coordinates. This is off by
        default. Note that this is only applicable to parametric surfaces
        whose parametric dimension is 2. Note that texturing may fail in
        some cases.
        """
    )

    def _get_generate_texture_coordinates_min_value(self):
        return self._vtk_obj.GetGenerateTextureCoordinatesMinValue()
    generate_texture_coordinates_min_value = traits.Property(_get_generate_texture_coordinates_min_value, help=\
        """
        Set/Get the generation of texture coordinates. This is off by
        default. Note that this is only applicable to parametric surfaces
        whose parametric dimension is 2. Note that texturing may fail in
        some cases.
        """
    )

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('generate_normals', 'GetGenerateNormals'),
    ('generate_texture_coordinates', 'GetGenerateTextureCoordinates'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('scalar_mode',
    'GetScalarMode'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('u_resolution', 'GetUResolution'),
    ('v_resolution', 'GetVResolution'), ('w_resolution',
    'GetWResolution'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_normals',
    'generate_texture_coordinates', 'global_warning_display',
    'release_data_flag', 'scalar_mode', 'output_points_precision',
    'progress_text', 'u_resolution', 'v_resolution', 'w_resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParametricFunctionSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ParametricFunctionSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_normals', 'generate_texture_coordinates'],
            ['scalar_mode'], ['output_points_precision', 'u_resolution',
            'v_resolution', 'w_resolution']),
            title='Edit ParametricFunctionSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParametricFunctionSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class TubeFilter(PolyDataAlgorithm):
    """
    TubeFilter - filter that generates tubes around lines
    
    Superclass: PolyDataAlgorithm
    
    TubeFilter is a filter that generates a tube around each input
    line. The tubes are made up of triangle strips and rotate around the
    tube with the rotation of the line normals. (If no normals are
    present, they are computed automatically.) The radius of the tube can
    be set to vary with scalar or vector value. If the radius varies with
    scalar value the radius is linearly adjusted. If the radius varies
    with vector value, a mass flux preserving variation is used. The
    number of sides for the tube also can be specified. You can also
    specify which of the sides are visible. This is useful for generating
    interesting striping effects. Other options include the ability to
    cap the tube and generate texture coordinates. Texture coordinates
    can be used with an associated texture map to create interesting
    effects such as marking the tube with stripes corresponding to length
    or time.
    
    This filter is typically used to create thick or dramatic lines.
    Another common use is to combine this filter with StreamTracer to
    generate streamtubes.
    
    @warning
    The number of tube sides must be greater than 3. If you wish to use
    fewer sides (i.e., a ribbon), use RibbonFilter.
    
    @warning
    The input line must not have duplicate points, or normals at points
    that are parallel to the incoming/outgoing line segments. (Duplicate
    points can be removed with CleanPolyData.) If a line does not meet
    this criteria, then that line is not tubed.
    
    @sa
    RibbonFilter StreamTracer
    
    @par Thanks: Michael Finch for absolute scalar radius
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTubeFilter, obj, update, **traits)
    
    capping = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off whether to cap the ends with polygons. Initial value
        is off.
        """
    )

    def _capping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCapping,
                        self.capping_)

    sides_share_vertices = tvtk_base.true_bool_trait(help=\
        """
        Set a boolean to control whether tube sides should share
        vertices. This creates independent strips, with constant normals
        so the tube is always faceted in appearance.
        """
    )

    def _sides_share_vertices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSidesShareVertices,
                        self.sides_share_vertices_)

    use_default_normal = tvtk_base.false_bool_trait(help=\
        """
        Set a boolean to control whether to use default normals.
        default_normal_on is set.
        """
    )

    def _use_default_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseDefaultNormal,
                        self.use_default_normal_)

    generate_t_coords = traits.Trait('off',
    tvtk_base.TraitRevPrefixMap({'off': 0, 'normalized_length': 1, 'use_length': 2, 'use_scalars': 3}), help=\
        """
        Control whether and how texture coordinates are produced. This is
        useful for striping the tube with length textures, etc. If you
        use scalars to create the texture, the scalars are assumed to be
        monotonically increasing (or decreasing).
        """
    )

    def _generate_t_coords_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateTCoords,
                        self.generate_t_coords_)

    vary_radius = traits.Trait('vary_radius_off',
    tvtk_base.TraitRevPrefixMap({'vary_radius_off': 0, 'vary_radius_by_absolute_scalar': 3, 'vary_radius_by_scalar': 1, 'vary_radius_by_vector': 2}), help=\
        """
        Turn on/off the variation of tube radius with scalar value.
        """
    )

    def _vary_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVaryRadius,
                        self.vary_radius_)

    default_normal = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _default_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultNormal,
                        self.default_normal)

    number_of_sides = traits.Trait(3, traits.Range(3, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the number of sides for the tube. At a minimum, number of
        sides is 3.
        """
    )

    def _number_of_sides_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSides,
                        self.number_of_sides)

    offset = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Control the striping of the tubes. The offset sets the first tube
        side that is visible. Offset is generally used with on_ratio to
        create nifty striping effects.
        """
    )

    def _offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOffset,
                        self.offset)

    on_ratio = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Control the striping of the tubes. If on_ratio is greater than 1,
        then every nth tube side is turned on, beginning with the Offset
        side.
        """
    )

    def _on_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOnRatio,
                        self.on_ratio)

    output_points_precision = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set/get the desired precision for the output types. See the
        documentation for the Algorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

    radius = traits.Trait(0.5, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set the minimum tube radius (minimum because the tube radius may
        vary).
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    radius_factor = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set the maximum tube radius in terms of a multiple of the minimum
        radius.
        """
    )

    def _radius_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadiusFactor,
                        self.radius_factor)

    texture_length = traits.Trait(1.0, traits.Range(1e-06, 2147483647.0, enter_set=True, auto_set=False), help=\
        """
        Control the conversion of units during the texture coordinates
        calculation. The texture_length indicates what length (whether
        calculated from scalars or length) is mapped to the [0,1) texture
        space.
        """
    )

    def _texture_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureLength,
                        self.texture_length)

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
    (('capping', 'GetCapping'), ('sides_share_vertices',
    'GetSidesShareVertices'), ('use_default_normal',
    'GetUseDefaultNormal'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('generate_t_coords', 'GetGenerateTCoords'), ('vary_radius',
    'GetVaryRadius'), ('default_normal', 'GetDefaultNormal'),
    ('number_of_sides', 'GetNumberOfSides'), ('offset', 'GetOffset'),
    ('on_ratio', 'GetOnRatio'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('radius', 'GetRadius'),
    ('radius_factor', 'GetRadiusFactor'), ('texture_length',
    'GetTextureLength'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'capping', 'debug', 'global_warning_display',
    'release_data_flag', 'sides_share_vertices', 'use_default_normal',
    'generate_t_coords', 'vary_radius', 'default_normal',
    'number_of_sides', 'offset', 'on_ratio', 'output_points_precision',
    'progress_text', 'radius', 'radius_factor', 'texture_length'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TubeFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TubeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['capping', 'sides_share_vertices', 'use_default_normal'],
            ['generate_t_coords', 'vary_radius'], ['default_normal',
            'number_of_sides', 'offset', 'on_ratio', 'output_points_precision',
            'radius', 'radius_factor', 'texture_length']),
            title='Edit TubeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TubeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


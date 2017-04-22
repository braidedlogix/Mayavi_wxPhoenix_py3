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


class GlyphSource2D(PolyDataAlgorithm):
    """
    GlyphSource2D - create 2d glyphs represented by PolyData
    
    Superclass: PolyDataAlgorithm
    
    GlyphSource2D can generate a family of 2d glyphs each of which
    lies in the x-y plane (i.e., the z-coordinate is zero). The class is
    a helper class to be used with Glyph2D and XYPlotActor.
    
    To use this class, specify the glyph type to use and its attributes.
    Attributes include its position (i.e., center point), scale, color,
    and whether the symbol is filled or not (a polygon or closed line
    sequence). You can also put a short line through the glyph running
    from -x to +x (the glyph looks like it's on a line), or a cross.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGlyphSource2D, obj, update, **traits)
    
    cross = tvtk_base.false_bool_trait(help=\
        """
        Specify whether a cross is drawn as part of the glyph. (This is
        in addition to the glyph. If the glyph type is set to "Cross"
        there is no need to enable this flag.)
        """
    )

    def _cross_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCross,
                        self.cross_)

    dash = tvtk_base.false_bool_trait(help=\
        """
        Specify whether a short line segment is drawn through the glyph.
        (This is in addition to the glyph. If the glyph type is set to
        "Dash" there is no need to enable this flag.)
        """
    )

    def _dash_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDash,
                        self.dash_)

    filled = tvtk_base.true_bool_trait(help=\
        """
        Specify whether the glyph is filled (a polygon) or not (a closed
        polygon defined by line segments). This only applies to 2d closed
        glyphs.
        """
    )

    def _filled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilled,
                        self.filled_)

    glyph_type = traits.Trait('vertex',
    tvtk_base.TraitRevPrefixMap({'vertex': 1, 'arrow': 9, 'circle': 7, 'cross': 3, 'dash': 2, 'diamond': 8, 'edge_arrow': 12, 'hooked_arrow': 11, 'none': 0, 'square': 6, 'thick_arrow': 10, 'thick_cross': 4, 'triangle': 5}), help=\
        """
        Specify the type of glyph to generate.
        """
    )

    def _glyph_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlyphType,
                        self.glyph_type_)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )

    def _color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColor,
                        self.color, False)

    output_points_precision = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get the desired precision for the output points.
        Algorithm::SINGLE_PRECISION - Output single-precision floating
        point. Algorithm::DOUBLE_PRECISION - Output double-precision
        floating point.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

    resolution = traits.Trait(8, traits.Range(3, 1024, enter_set=True, auto_set=False), help=\
        """
        Specify the number of points that form the circular glyph.
        """
    )

    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

    rotation_angle = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Specify an angle (in degrees) to rotate the glyph around the
        z-axis. Using this ivar, it is possible to generate rotated
        glyphs (e.g., crosses, arrows, etc.)
        """
    )

    def _rotation_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRotationAngle,
                        self.rotation_angle)

    scale = traits.Trait(1.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set the scale of the glyph. Note that the glyphs are designed to
        fit in the (1,1) rectangle.
        """
    )

    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale)

    scale2 = traits.Trait(1.5, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set the scale of optional portions of the glyph (e.g., the dash
        and cross is dash_on() and cross_on()).
        """
    )

    def _scale2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale2,
                        self.scale2)

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
    (('cross', 'GetCross'), ('dash', 'GetDash'), ('filled', 'GetFilled'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('glyph_type',
    'GetGlyphType'), ('center', 'GetCenter'), ('color', 'GetColor'),
    ('output_points_precision', 'GetOutputPointsPrecision'),
    ('resolution', 'GetResolution'), ('rotation_angle',
    'GetRotationAngle'), ('scale', 'GetScale'), ('scale2', 'GetScale2'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'cross', 'dash', 'debug', 'filled',
    'global_warning_display', 'release_data_flag', 'glyph_type', 'center',
    'color', 'output_points_precision', 'progress_text', 'resolution',
    'rotation_angle', 'scale', 'scale2'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GlyphSource2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GlyphSource2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['cross', 'dash', 'filled'], ['glyph_type'], ['center', 'color',
            'output_points_precision', 'resolution', 'rotation_angle', 'scale',
            'scale2']),
            title='Edit GlyphSource2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GlyphSource2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.button_source import ButtonSource


class RectangularButtonSource(ButtonSource):
    """
    RectangularButtonSource - create a rectangular button
    
    Superclass: ButtonSource
    
    RectangularButtonSource creates a rectangular shaped button with
    texture coordinates suitable for application of a texture map. This
    provides a way to make nice looking 3d buttons. The buttons are
    represented as PolyData that includes texture coordinates and
    normals. The button lies in the x-y plane.
    
    To use this class you must define its width, height and length. These
    measurements are all taken with respect to the shoulder of the
    button. The shoulder is defined as follows. Imagine a box sitting on
    the floor. The distance from the floor to the top of the box is the
    depth; the other directions are the length (x-direction) and height
    (y-direction). In this particular widget the box can have a smaller
    bottom than top. The ratio in size between bottom and top is called
    the box ratio (by default=1.0). The ratio of the texture region to
    the shoulder region is the texture ratio. And finally the texture
    region may be out of plane compared to the shoulder. The texture
    height ratio controls this.
    
    @sa
    ButtonSource EllipticalButtonSource
    
    @warning
    The button is defined in the x-y plane. Use
    TransformPolyDataFilter or Glyph3D to orient the button in a
    different direction.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRectangularButtonSource, obj, update, **traits)
    
    box_ratio = traits.Trait(1.1, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the ratio of the bottom of the button with the shoulder
        region. Numbers greater than one produce buttons with a wider
        bottom than shoulder; ratios less than one produce buttons that
        have a wider shoulder than bottom.
        """
    )

    def _box_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoxRatio,
                        self.box_ratio)

    depth = traits.Trait(0.05, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the depth of the button (the z-eliipsoid axis length).
        """
    )

    def _depth_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepth,
                        self.depth)

    height = traits.Trait(0.5, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the height of the button.
        """
    )

    def _height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeight,
                        self.height)

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

    texture_height_ratio = traits.Trait(0.95, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the ratio of the height of the texture region to the
        shoulder height. Values greater than 1.0 yield convex buttons
        with the texture region raised above the shoulder. Values less
        than 1.0 yield concave buttons with the texture region below the
        shoulder.
        """
    )

    def _texture_height_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureHeightRatio,
                        self.texture_height_ratio)

    texture_ratio = traits.Trait(0.9, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the ratio of the texture region to the shoulder region.
        This number must be 0<=tr<=1. If the texture style is to fit the
        image, then satisfying the texture ratio may only be possible in
        one of the two directions (length or width) depending on the
        dimensions of the texture.
        """
    )

    def _texture_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureRatio,
                        self.texture_ratio)

    width = traits.Trait(0.5, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the width of the button.
        """
    )

    def _width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWidth,
                        self.width)

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
    (('two_sided', 'GetTwoSided'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('texture_style', 'GetTextureStyle'), ('box_ratio', 'GetBoxRatio'),
    ('depth', 'GetDepth'), ('height', 'GetHeight'),
    ('output_points_precision', 'GetOutputPointsPrecision'),
    ('texture_height_ratio', 'GetTextureHeightRatio'), ('texture_ratio',
    'GetTextureRatio'), ('width', 'GetWidth'), ('center', 'GetCenter'),
    ('shoulder_texture_coordinate', 'GetShoulderTextureCoordinate'),
    ('texture_dimensions', 'GetTextureDimensions'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'two_sided', 'texture_style', 'box_ratio',
    'center', 'depth', 'height', 'output_points_precision',
    'progress_text', 'shoulder_texture_coordinate', 'texture_dimensions',
    'texture_height_ratio', 'texture_ratio', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RectangularButtonSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RectangularButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['two_sided'], ['texture_style'], ['box_ratio', 'center',
            'depth', 'height', 'output_points_precision',
            'shoulder_texture_coordinate', 'texture_dimensions',
            'texture_height_ratio', 'texture_ratio', 'width']),
            title='Edit RectangularButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RectangularButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


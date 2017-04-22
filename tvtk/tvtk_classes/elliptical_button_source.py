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


class EllipticalButtonSource(ButtonSource):
    """
    EllipticalButtonSource - create a ellipsoidal-shaped button
    
    Superclass: ButtonSource
    
    EllipticalButtonSource creates a ellipsoidal shaped button with
    texture coordinates suitable for application of a texture map. This
    provides a way to make nice looking 3d buttons. The buttons are
    represented as PolyData that includes texture coordinates and
    normals. The button lies in the x-y plane.
    
    To use this class you must define the major and minor axes lengths of
    an ellipsoid (expressed as width (x), height (y) and depth (z)). The
    button has a rectangular mesh region in the center with texture
    coordinates that range smoothly from (0,1). (This flat region is
    called the texture region.) The outer, curved portion of the button
    (called the shoulder) has texture coordinates set to a user specified
    value (by default (0,0). (This results in coloring the button curve
    the same color as the (s,t) location of the texture map.) The
    resolution in the radial direction, the texture region, and the
    shoulder region must also be set. The button can be moved by
    specifying an origin.
    
    @sa
    ButtonSource RectangularButtonSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEllipticalButtonSource, obj, update, **traits)
    
    circumferential_resolution = traits.Trait(4, traits.Range(4, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the resolution of the button in the circumferential
        direction.
        """
    )

    def _circumferential_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCircumferentialResolution,
                        self.circumferential_resolution)

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
        Set/Get the height of the button (the y-ellipsoid axis length *
        2).
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

    radial_ratio = traits.Trait(1.1, traits.Range(1.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the radial ratio. This is the measure of the radius of
        the outer ellipsoid to the inner ellipsoid of the button. The
        outer ellipsoid is the boundary of the button defined by the
        height and width. The inner ellipsoid circumscribes the texture
        region. Larger radial_ratio's cause the button to be more rounded
        (and the texture region to be smaller); smaller ratios produce
        sharply curved shoulders with a larger texture region.
        """
    )

    def _radial_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadialRatio,
                        self.radial_ratio)

    shoulder_resolution = traits.Trait(2, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the resolution of the texture in the radial direction in
        the shoulder region.
        """
    )

    def _shoulder_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShoulderResolution,
                        self.shoulder_resolution)

    texture_resolution = traits.Trait(2, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the resolution of the texture in the radial direction in
        the texture region.
        """
    )

    def _texture_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureResolution,
                        self.texture_resolution)

    width = traits.Trait(0.5, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get the width of the button (the x-ellipsoid axis length *
        2).
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
    ('texture_style', 'GetTextureStyle'), ('circumferential_resolution',
    'GetCircumferentialResolution'), ('depth', 'GetDepth'), ('height',
    'GetHeight'), ('output_points_precision', 'GetOutputPointsPrecision'),
    ('radial_ratio', 'GetRadialRatio'), ('shoulder_resolution',
    'GetShoulderResolution'), ('texture_resolution',
    'GetTextureResolution'), ('width', 'GetWidth'), ('center',
    'GetCenter'), ('shoulder_texture_coordinate',
    'GetShoulderTextureCoordinate'), ('texture_dimensions',
    'GetTextureDimensions'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'two_sided', 'texture_style', 'center',
    'circumferential_resolution', 'depth', 'height',
    'output_points_precision', 'progress_text', 'radial_ratio',
    'shoulder_resolution', 'shoulder_texture_coordinate',
    'texture_dimensions', 'texture_resolution', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EllipticalButtonSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit EllipticalButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['two_sided'], ['texture_style'], ['center',
            'circumferential_resolution', 'depth', 'height',
            'output_points_precision', 'radial_ratio', 'shoulder_resolution',
            'shoulder_texture_coordinate', 'texture_dimensions',
            'texture_resolution', 'width']),
            title='Edit EllipticalButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EllipticalButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


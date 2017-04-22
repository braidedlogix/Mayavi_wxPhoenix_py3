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


class ButtonSource(PolyDataAlgorithm):
    """
    ButtonSource - abstract class for creating various button types
    
    Superclass: PolyDataAlgorithm
    
    ButtonSource is an abstract class that defines an API for creating
    "button-like" objects in VTK. A button is a geometry with a
    rectangular region that can be textured. The button is divided into
    two regions: the texture region and the shoulder region. The points
    in both regions are assigned texture coordinates. The texture region
    has texture coordinates consistent with the image to be placed on it.
     All points in the shoulder regions are assigned a texture coordinate
    specified by the user.  In this way the shoulder region can be
    colored by the texture.
    
    Creating a ButtonSource requires specifying its center point.
    (Subclasses have other attributes that must be set to control the
    shape of the button.) You must also specify how to control the shape
    of the texture region; i.e., whether to size the texture region
    proportional to the texture dimensions or whether to size the texture
    region proportional to the button. Also, buttons can be created
    single sided are mirrored to create two-sided buttons.
    
    @sa
    EllipticalButtonSource RectangularButtonSource
    
    @warning
    The button is defined in the x-y plane. Use
    TransformPolyDataFilter or Glyph3D to orient the button in a
    different direction.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkButtonSource, obj, update, **traits)
    
    two_sided = tvtk_base.false_bool_trait(help=\
        """
        Indicate whether the button is single or double sided. A double
        sided button can be viewed from two sides...it looks sort of like
        a "pill." A single-sided button is meant to viewed from a single
        side; it looks like a "clam-shell."
        """
    )

    def _two_sided_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTwoSided,
                        self.two_sided_)

    texture_style = traits.Trait('proportional',
    tvtk_base.TraitRevPrefixMap({'proportional': 1, 'fit_image': 0}), help=\
        """
        Set/Get the style of the texture region: whether to size it
        according to the x-y dimensions of the texture, or whether to
        make the texture region proportional to the width/height of the
        button.
        """
    )

    def _texture_style_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureStyle,
                        self.texture_style_)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    shoulder_texture_coordinate = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 0.0), cols=2, help=\
        """
        
        """
    )

    def _shoulder_texture_coordinate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShoulderTextureCoordinate,
                        self.shoulder_texture_coordinate)

    texture_dimensions = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(100, 100), cols=2, help=\
        """
        
        """
    )

    def _texture_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureDimensions,
                        self.texture_dimensions)

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
    ('texture_style', 'GetTextureStyle'), ('center', 'GetCenter'),
    ('shoulder_texture_coordinate', 'GetShoulderTextureCoordinate'),
    ('texture_dimensions', 'GetTextureDimensions'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'two_sided', 'texture_style', 'center',
    'progress_text', 'shoulder_texture_coordinate', 'texture_dimensions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ButtonSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['two_sided'], ['texture_style'], ['center',
            'shoulder_texture_coordinate', 'texture_dimensions']),
            title='Edit ButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ButtonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


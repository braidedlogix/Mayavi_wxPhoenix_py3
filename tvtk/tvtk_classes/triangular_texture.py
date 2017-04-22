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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class TriangularTexture(ImageAlgorithm):
    """
    TriangularTexture - generate 2d triangular texture map
    
    Superclass: ImageAlgorithm
    
    TriangularTexture is a filter that generates a 2d texture map
    based on the paper "Opacity-modulating Triangular Textures for Irregular
    Surfaces," by Penny Rheingans, IEEE Visualization '96, pp. 219-225.
    The textures assume texture coordinates of (0,0), (1.0) and (.5,
    sqrt(3)/2). The sequence of texture values is the same along each
    edge of the triangular texture map. So, the assignment order of
    texture coordinates is arbitrary.
    
    @sa
    TriangularTCoords
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTriangularTexture, obj, update, **traits)
    
    scale_factor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set a Scale Factor.
        """
    )

    def _scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleFactor,
                        self.scale_factor)

    texture_pattern = traits.Trait(1, traits.Range(1, 3, enter_set=True, auto_set=False), help=\
        """
        Set the texture pattern. 1 = opaque at centroid (default) 2 =
        opaque at vertices 3 = opaque in rings around vertices
        """
    )

    def _texture_pattern_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTexturePattern,
                        self.texture_pattern)

    x_size = traits.Int(64, enter_set=True, auto_set=False, help=\
        """
        Set the X texture map dimension. Default is 64.
        """
    )

    def _x_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXSize,
                        self.x_size)

    y_size = traits.Int(64, enter_set=True, auto_set=False, help=\
        """
        Set the Y texture map dimension. Default is 64.
        """
    )

    def _y_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYSize,
                        self.y_size)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get a data object for one of the input port connections.  The use
        of this method is strongly discouraged, but some filters that
        were written a long time ago still use this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('scale_factor', 'GetScaleFactor'), ('texture_pattern',
    'GetTexturePattern'), ('x_size', 'GetXSize'), ('y_size', 'GetYSize'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'scale_factor',
    'texture_pattern', 'x_size', 'y_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TriangularTexture, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TriangularTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['scale_factor', 'texture_pattern', 'x_size',
            'y_size']),
            title='Edit TriangularTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TriangularTexture properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


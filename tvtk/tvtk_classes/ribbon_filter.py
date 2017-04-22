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


class RibbonFilter(PolyDataAlgorithm):
    """
    RibbonFilter - create oriented ribbons from lines defined in
    polygonal dataset
    
    Superclass: PolyDataAlgorithm
    
    RibbonFilter is a filter to create oriented ribbons from lines
    defined in polygonal dataset. The orientation of the ribbon is along
    the line segments and perpendicular to "projected" line normals.
    Projected line normals are the original line normals projected to be
    perpendicular to the local line segment. An offset angle can be
    specified to rotate the ribbon with respect to the normal.
    
    @warning
    The input line must not have duplicate points, or normals at points
    that are parallel to the incoming/outgoing line segments. (Duplicate
    points can be removed with CleanPolyData.) If a line does not meet
    this criteria, then that line is not tubed.
    
    @sa
    TubeFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRibbonFilter, obj, update, **traits)
    
    use_default_normal = tvtk_base.false_bool_trait(help=\
        """
        Set a boolean to control whether to use default normals. The
        default is Off
        """
    )

    def _use_default_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseDefaultNormal,
                        self.use_default_normal_)

    vary_width = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the variation of ribbon width with scalar value. The
        default is Off
        """
    )

    def _vary_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVaryWidth,
                        self.vary_width_)

    generate_t_coords = traits.Trait('off',
    tvtk_base.TraitRevPrefixMap({'off': 0, 'normalized_length': 1, 'use_length': 2, 'use_scalars': 3}), help=\
        """
        Control whether and how texture coordinates are produced. This is
        useful for striping the ribbon with time textures, etc.
        """
    )

    def _generate_t_coords_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateTCoords,
                        self.generate_t_coords_)

    angle = traits.Trait(0.0, traits.Range(0.0, 360.0, enter_set=True, auto_set=False), help=\
        """
        Set the offset angle of the ribbon from the line normal. (The
        angle is expressed in degrees.) The default is 0.0
        """
    )

    def _angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAngle,
                        self.angle)

    default_normal = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _default_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultNormal,
                        self.default_normal)

    texture_length = traits.Trait(1.0, traits.Range(1e-06, 2147483647.0, enter_set=True, auto_set=False), help=\
        """
        Control the conversion of units during the texture coordinates
        calculation. The texture_length indicates what length (whether
        calculated from scalars or length) is mapped to the [0,1) texture
        space. The default is 1.0
        """
    )

    def _texture_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureLength,
                        self.texture_length)

    width = traits.Trait(0.5, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set the "half" width of the ribbon. If the width is allowed to
        vary, this is the minimum width. The default is 0.5
        """
    )

    def _width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWidth,
                        self.width)

    width_factor = traits.Float(2.0, enter_set=True, auto_set=False, help=\
        """
        Set the maximum ribbon width in terms of a multiple of the
        minimum width. The default is 2.0
        """
    )

    def _width_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWidthFactor,
                        self.width_factor)

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
    (('use_default_normal', 'GetUseDefaultNormal'), ('vary_width',
    'GetVaryWidth'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('generate_t_coords', 'GetGenerateTCoords'), ('angle', 'GetAngle'),
    ('default_normal', 'GetDefaultNormal'), ('texture_length',
    'GetTextureLength'), ('width', 'GetWidth'), ('width_factor',
    'GetWidthFactor'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'use_default_normal', 'vary_width',
    'generate_t_coords', 'angle', 'default_normal', 'progress_text',
    'texture_length', 'width', 'width_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RibbonFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RibbonFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_default_normal', 'vary_width'], ['generate_t_coords'],
            ['angle', 'default_normal', 'texture_length', 'width',
            'width_factor']),
            title='Edit RibbonFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RibbonFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class TextureMapToPlane(DataSetAlgorithm):
    """
    TextureMapToPlane - generate texture coordinates by mapping points
    to plane
    
    Superclass: DataSetAlgorithm
    
    TextureMapToPlane is a filter that generates 2d texture
    coordinates by mapping input dataset points onto a plane. The plane
    can either be user specified or generated automatically. (A least
    squares method is used to generate the plane automatically.)
    
    There are two ways you can specify the plane. The first is to provide
    a plane normal. In this case the points are projected to a plane, and
    the points are then mapped into the user specified s-t coordinate
    range. For more control, you can specify a plane with three points:
    an origin and two points defining the two axes of the plane. (This is
    compatible with the PlaneSource.) Using the second method, the
    SRange and TRange vectors are ignored, since the presumption is that
    the user does not want to scale the texture coordinates; and you can
    adjust the origin and axes points to achieve the texture coordinate
    scaling you need. Note also that using the three point method the
    axes do not have to be orthogonal.
    
    @sa
     PlaneSource TextureMapToCylinder TextureMapToSphere
    ThresholdTextureCoords
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextureMapToPlane, obj, update, **traits)
    
    automatic_plane_generation = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off automatic plane generation.
        """
    )

    def _automatic_plane_generation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutomaticPlaneGeneration,
                        self.automatic_plane_generation_)

    normal = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormal,
                        self.normal)

    origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    point1 = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _point1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1,
                        self.point1)

    point2 = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _point2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2,
                        self.point2)

    s_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 1.0), cols=2, help=\
        """
        
        """
    )

    def _s_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSRange,
                        self.s_range)

    t_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 1.0), cols=2, help=\
        """
        
        """
    )

    def _t_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTRange,
                        self.t_range)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    _updateable_traits_ = \
    (('automatic_plane_generation', 'GetAutomaticPlaneGeneration'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('normal',
    'GetNormal'), ('origin', 'GetOrigin'), ('point1', 'GetPoint1'),
    ('point2', 'GetPoint2'), ('s_range', 'GetSRange'), ('t_range',
    'GetTRange'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'automatic_plane_generation', 'debug',
    'global_warning_display', 'release_data_flag', 'normal', 'origin',
    'point1', 'point2', 'progress_text', 's_range', 't_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextureMapToPlane, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TextureMapToPlane properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic_plane_generation'], [], ['normal', 'origin',
            'point1', 'point2', 's_range', 't_range']),
            title='Edit TextureMapToPlane properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextureMapToPlane properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


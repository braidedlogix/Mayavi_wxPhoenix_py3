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


class TransformTextureCoords(DataSetAlgorithm):
    """
    TransformTextureCoords - transform (scale, rotate, translate)
    texture coordinates
    
    Superclass: DataSetAlgorithm
    
    TransformTextureCoords is a filter that operates on texture
    coordinates. It ingests any type of dataset, and outputs a dataset of
    the same type. The filter lets you scale, translate, and rotate
    texture coordinates. For example, by using the the Scale ivar, you
    can shift texture coordinates that range from (0->1) to range from
    (0->10) (useful for repeated patterns).
    
    The filter operates on texture coordinates of dimension 1->3. The
    texture coordinates are referred to as r-s-t. If the texture map is
    two dimensional, the t-coordinate (and operations on the
    t-coordinate) are ignored.
    
    @sa
    TextureMapToPlane  TextureMapToCylinder TextureMapToSphere
    ThresholdTextureCoords Texture
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTransformTextureCoords, obj, update, **traits)
    
    flip_r = tvtk_base.false_bool_trait(help=\
        """
        Boolean indicates whether the texture map should be flipped
        around the s-axis. Note that the flips occur around the texture
        origin.
        """
    )

    def _flip_r_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFlipR,
                        self.flip_r_)

    flip_s = tvtk_base.false_bool_trait(help=\
        """
        Boolean indicates whether the texture map should be flipped
        around the s-axis. Note that the flips occur around the texture
        origin.
        """
    )

    def _flip_s_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFlipS,
                        self.flip_s_)

    flip_t = tvtk_base.false_bool_trait(help=\
        """
        Boolean indicates whether the texture map should be flipped
        around the t-axis. Note that the flips occur around the texture
        origin.
        """
    )

    def _flip_t_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFlipT,
                        self.flip_t_)

    origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.5, 0.5, 0.5), cols=3, help=\
        """
        
        """
    )

    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    position = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    scale = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def add_position(self, *args):
        """
        V.add_position(float, float, float)
        C++: void AddPosition(double deltaR, double deltaS, double deltaT)
        V.add_position([float, float, float])
        C++: void AddPosition(double deltaPosition[3])
        Incrementally change the position of the texture map (i.e., does
        a translate or shift of the texture coordinates).
        """
        ret = self._wrap_call(self._vtk_obj.AddPosition, *args)
        return ret

    _updateable_traits_ = \
    (('flip_r', 'GetFlipR'), ('flip_s', 'GetFlipS'), ('flip_t',
    'GetFlipT'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('origin',
    'GetOrigin'), ('position', 'GetPosition'), ('scale', 'GetScale'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'flip_r', 'flip_s', 'flip_t',
    'global_warning_display', 'release_data_flag', 'origin', 'position',
    'progress_text', 'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TransformTextureCoords, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TransformTextureCoords properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['flip_r', 'flip_s', 'flip_t'], [], ['origin', 'position',
            'scale']),
            title='Edit TransformTextureCoords properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TransformTextureCoords properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


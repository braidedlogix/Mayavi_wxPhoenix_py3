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


class RotationalExtrusionFilter(PolyDataAlgorithm):
    """
    RotationalExtrusionFilter - sweep polygonal data creating "skirt"
    from free edges and lines, and lines from vertices
    
    Superclass: PolyDataAlgorithm
    
    RotationalExtrusionFilter is a modeling filter. It takes polygonal
    data as input and generates polygonal data on output. The input
    dataset is swept around the z-axis to create new polygonal
    primitives. These primitives form a "skirt" or swept surface. For
    example, sweeping a line results in a cylindrical shell, and sweeping
    a circle creates a torus.
    
    There are a number of control parameters for this filter. You can
    control whether the sweep of a 2d object (i.e., polygon or triangle
    strip) is capped with the generating geometry via the "Capping"
    instance variable. Also, you can control the angle of rotation, and
    whether translation along the z-axis is performed along with the
    rotation. (Translation is useful for creating "springs".) You also
    can adjust the radius of the generating geometry using the
    "_delta_rotation" instance variable.
    
    The skirt is generated by locating certain topological features. Free
    edges (edges of polygons or triangle strips only used by one polygon
    or triangle strips) generate surfaces. This is true also of lines or
    polylines. Vertices generate lines.
    
    This filter can be used to model axisymmetric objects like cylinders,
    bottles, and wine glasses; or translational/rotational symmetric
    objects like springs or corkscrews.
    
    @warning
    If the object sweeps 360 degrees, radius does not vary, and the
    object does not translate, capping is not performed. This is because
    the cap is unnecessary.
    
    @warning
    Some polygonal objects have no free edges (e.g., sphere). When swept,
    this will result in two separate surfaces if capping is on, or no
    surface if capping is off.
    
    @sa
    LinearExtrusionFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRotationalExtrusionFilter, obj, update, **traits)
    
    capping = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the capping of the skirt.
        """
    )

    def _capping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCapping,
                        self.capping_)

    angle = traits.Float(360.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get angle of rotation.
        """
    )

    def _angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAngle,
                        self.angle)

    delta_radius = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get change in radius during sweep process.
        """
    )

    def _delta_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeltaRadius,
                        self.delta_radius)

    resolution = traits.Trait(12, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get resolution of sweep operation. Resolution controls the
        number of intermediate node points.
        """
    )

    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

    translation = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get total amount of translation along the z-axis.
        """
    )

    def _translation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslation,
                        self.translation)

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
    (('capping', 'GetCapping'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('angle',
    'GetAngle'), ('delta_radius', 'GetDeltaRadius'), ('resolution',
    'GetResolution'), ('translation', 'GetTranslation'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'capping', 'debug', 'global_warning_display',
    'release_data_flag', 'angle', 'delta_radius', 'progress_text',
    'resolution', 'translation'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RotationalExtrusionFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RotationalExtrusionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['capping'], [], ['angle', 'delta_radius', 'resolution',
            'translation']),
            title='Edit RotationalExtrusionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RotationalExtrusionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


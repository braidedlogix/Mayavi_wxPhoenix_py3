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


class ArcSource(PolyDataAlgorithm):
    """
    ArcSource - create a circular arc
    
    Superclass: PolyDataAlgorithm
    
    ArcSource is a source object that creates an arc defined by two
    endpoints and a center. The number of segments composing the polyline
    is controlled by setting the object resolution. Alternatively, one
    can use a better API (that does not allow for inconsistent nor
    ambiguous inputs), using a starting point (polar vector, measured
    from the arc's center), a normal to the plane of the arc, and an
    angle defining the arc length. Since the default API remains the
    original one, in order to use the improved API, one must switch the
    use_normal_and_angle flag to TRUE.
    
    The development of an improved, consistent API (based on point,
    normal, and angle) was supported by CEA/DIF - Commissariat a
    l'Energie Atomique, Centre DAM Ile-De-France, BP12, F-91297 Arpajon,
    France, and implemented by Philippe Pebay, Kitware SAS 2012.
    
    @sa
    EllipseArcSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkArcSource, obj, update, **traits)
    
    negative = tvtk_base.false_bool_trait(help=\
        """
        By default the arc spans the shortest angular sector point1 and
        point2. By setting this to true, the longest angular sector is
        used instead (i.e. the negative coterminal angle to the shortest
        one). Note: This is only used when use_normal_and_angle is OFF.
        False by default.
        """
    )

    def _negative_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNegative,
                        self.negative_)

    use_normal_and_angle = tvtk_base.false_bool_trait(help=\
        """
        Activate the API based on a normal vector, a starting point
        (polar vector) and an angle defining the arc length. The previous
        API (which remains the default) allows for inputs that are
        inconsistent (when Point1 and Point2 are not equidistant from
        Center) or ambiguous (when Point1, Point2, and Center are
        aligned). Note: false by default.
        """
    )

    def _use_normal_and_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseNormalAndAngle,
                        self.use_normal_and_angle_)

    angle = traits.Trait(90.0, traits.Range(-360.0, 360.0, enter_set=True, auto_set=False), help=\
        """
        Arc length (in degrees), beginning at the polar vector. The
        direction is counterclockwise by default; a negative value draws
        the arc in the clockwise direction. Note: This is only used when
        use_normal_and_angle is ON.
        """
    )

    def _angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAngle,
                        self.angle)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    normal = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormal,
                        self.normal)

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

    point1 = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.5, 0.0), cols=3, help=\
        """
        
        """
    )

    def _point1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1,
                        self.point1)

    point2 = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.5, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _point2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2,
                        self.point2)

    polar_vector = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _polar_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPolarVector,
                        self.polar_vector)

    resolution = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Define the number of segments of the polyline that draws the arc.
        Note: if the resolution is set to 1 (the default value), the arc
        is drawn as a straight line.
        """
    )

    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

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
    (('negative', 'GetNegative'), ('use_normal_and_angle',
    'GetUseNormalAndAngle'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('angle',
    'GetAngle'), ('center', 'GetCenter'), ('normal', 'GetNormal'),
    ('output_points_precision', 'GetOutputPointsPrecision'), ('point1',
    'GetPoint1'), ('point2', 'GetPoint2'), ('polar_vector',
    'GetPolarVector'), ('resolution', 'GetResolution'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'negative',
    'release_data_flag', 'use_normal_and_angle', 'angle', 'center',
    'normal', 'output_points_precision', 'point1', 'point2',
    'polar_vector', 'progress_text', 'resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ArcSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ArcSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['negative', 'use_normal_and_angle'], [], ['angle', 'center',
            'normal', 'output_points_precision', 'point1', 'point2',
            'polar_vector', 'resolution']),
            title='Edit ArcSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ArcSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


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


class EllipseArcSource(PolyDataAlgorithm):
    """
    EllipseArcSource - create an elliptical arc
    
    Superclass: PolyDataAlgorithm
    
    EllipseArcSource is a source object that creates an elliptical arc
    defined by a normal, a center and the major radius vector. You can
    define an angle to draw only a section of the ellipse. The number of
    segments composing the polyline is controlled by setting the object
    resolution.
    
    @sa
    ArcSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEllipseArcSource, obj, update, **traits)
    
    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    major_radius_vector = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _major_radius_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMajorRadiusVector,
                        self.major_radius_vector)

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
        point, This is the default. Algorithm::DOUBLE_PRECISION -
        Output double-precision floating point.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

    ratio = traits.Trait(1.0, traits.Range(0.001, 100.0, enter_set=True, auto_set=False), help=\
        """
        Set the ratio of the ellipse, i.e. the ratio b/a _ b: minor
        radius; a: major radius default is 1.
        """
    )

    def _ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRatio,
                        self.ratio)

    resolution = traits.Trait(100, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Divide line into resolution number of pieces. Note: if Resolution
        is set to 1 the arc is a straight line. Default is 100.
        """
    )

    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

    segment_angle = traits.Trait(90.0, traits.Range(0.0, 360.0, enter_set=True, auto_set=False), help=\
        """
        Angular sector occupied by the arc, beginning at Start Angle
        Default is 90.
        """
    )

    def _segment_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSegmentAngle,
                        self.segment_angle)

    start_angle = traits.Trait(0.0, traits.Range(-360.0, 360.0, enter_set=True, auto_set=False), help=\
        """
        Set the start angle. The angle where the plot begins. Default is
        0.
        """
    )

    def _start_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartAngle,
                        self.start_angle)

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
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('center',
    'GetCenter'), ('major_radius_vector', 'GetMajorRadiusVector'),
    ('normal', 'GetNormal'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('ratio', 'GetRatio'), ('resolution',
    'GetResolution'), ('segment_angle', 'GetSegmentAngle'),
    ('start_angle', 'GetStartAngle'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'center', 'major_radius_vector', 'normal',
    'output_points_precision', 'progress_text', 'ratio', 'resolution',
    'segment_angle', 'start_angle'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EllipseArcSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit EllipseArcSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['center', 'major_radius_vector', 'normal',
            'output_points_precision', 'ratio', 'resolution', 'segment_angle',
            'start_angle']),
            title='Edit EllipseArcSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EllipseArcSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


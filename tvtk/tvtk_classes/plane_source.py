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


class PlaneSource(PolyDataAlgorithm):
    """
    PlaneSource - create an array of quadrilaterals located in a plane
    
    Superclass: PolyDataAlgorithm
    
    PlaneSource creates an m x n array of quadrilaterals arranged as a
    regular tiling in a plane. The plane is defined by specifying an
    origin point, and then two other points that, together with the
    origin, define two axes for the plane. These axes do not have to be
    orthogonal - so you can create a parallelogram. (The axes must not be
    parallel.) The resolution of the plane (i.e., number of subdivisions)
    is controlled by the ivars XResolution and YResolution.
    
    By default, the plane is centered at the origin and perpendicular to
    the z-axis, with width and height of length 1 and resolutions set to
    1.
    
    There are three convenience methods that allow you to easily move the
    plane.  The first, set_normal(), allows you to specify the plane
    normal. The effect of this method is to rotate the plane around the
    center of the plane, aligning the plane normal with the specified
    normal. The rotation is about the axis defined by the cross product
    of the current normal with the new normal. The second, set_center(),
    translates the center of the plane to the specified center point. The
    third method, Push(), allows you to translate the plane along the
    plane normal by the distance specified. (Negative Push values
    translate the plane in the negative normal direction.)  Note that the
    set_normal(), set_center() and Push() methods modify the Origin,
    Point1, and/or Point2 instance variables.
    
    @warning
    The normal to the plane will point in the direction of the cross
    product of the first axis (Origin->Point1) with the second
    (Origin->Point2). This also affects the normals to the generated
    polygons.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlaneSource, obj, update, **traits)
    
    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set/Get the center of the plane. Works in conjunction with the
        plane normal to position the plane. Don't use this method to
        define the plane. Instead, use it to move the plane to a new
        center point.
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    normal = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 1.0), cols=3, help=\
        """
        Set/Get the plane normal. Works in conjunction with the plane
        center to orient the plane. Don't use this method to define the
        plane. Instead, use it to rotate the plane around the current
        center point.
        """
    )

    def _normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormal,
                        self.normal)

    origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(-0.5, -0.5, 0.0), cols=3, help=\
        """
        
        """
    )

    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

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

    point1 = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.5, -0.5, 0.0), cols=3, help=\
        """
        Specify a point defining the first axis of the plane.
        """
    )

    def _point1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1,
                        self.point1)

    point2 = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(-0.5, 0.5, 0.0), cols=3, help=\
        """
        Specify a point defining the second axis of the plane.
        """
    )

    def _point2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2,
                        self.point2)

    def get_resolution(self, *args):
        """
        V.get_resolution(int, int)
        C++: void GetResolution(int &xR, int &yR)
        Set the number of x-y subdivisions in the plane.
        """
        ret = self._wrap_call(self._vtk_obj.GetResolution, *args)
        return ret

    def set_resolution(self, *args):
        """
        V.set_resolution(int, int)
        C++: void SetResolution(const int xR, const int yR)
        Set the number of x-y subdivisions in the plane.
        """
        ret = self._wrap_call(self._vtk_obj.SetResolution, *args)
        return ret

    x_resolution = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Specify the resolution of the plane along the first axes.
        """
    )

    def _x_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXResolution,
                        self.x_resolution)

    y_resolution = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Specify the resolution of the plane along the second axes.
        """
    )

    def _y_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYResolution,
                        self.y_resolution)

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

    def push(self, *args):
        """
        V.push(float)
        C++: void Push(double distance)
        Translate the plane in the direction of the normal by the
        distance specified.  Negative values move the plane in the
        opposite direction.
        """
        ret = self._wrap_call(self._vtk_obj.Push, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('center',
    'GetCenter'), ('normal', 'GetNormal'), ('origin', 'GetOrigin'),
    ('output_points_precision', 'GetOutputPointsPrecision'), ('point1',
    'GetPoint1'), ('point2', 'GetPoint2'), ('x_resolution',
    'GetXResolution'), ('y_resolution', 'GetYResolution'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'center', 'normal', 'origin',
    'output_points_precision', 'point1', 'point2', 'progress_text',
    'x_resolution', 'y_resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlaneSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PlaneSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['center', 'normal', 'origin',
            'output_points_precision', 'point1', 'point2', 'x_resolution',
            'y_resolution']),
            title='Edit PlaneSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlaneSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


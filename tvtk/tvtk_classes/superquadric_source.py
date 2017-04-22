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


class SuperquadricSource(PolyDataAlgorithm):
    """
    SuperquadricSource - create a polygonal superquadric centered at
    the origin
    
    Superclass: PolyDataAlgorithm
    
    SuperquadricSource creates a superquadric (represented by
    polygons) of specified size centered at the origin. The alignment of
    the axis of the superquadric along one of the global axes can be
    specified. The resolution (polygonal discretization) in both the
    latitude (phi) and longitude (theta) directions can be specified.
    Roundness parameters (_phi_roundness and theta_roundness) control the
    shape of the superquadric.  The Toroidal boolean controls whether a
    toroidal superquadric is produced.  If so, the Thickness parameter
    controls the thickness of the toroid:  0 is the thinnest allowable
    toroid, and 1 has a minimum sized hole.  The Scale parameters allow
    the superquadric to be scaled in x, y, and z (normal vectors are
    correctly generated in any case).  The Size parameter controls size
    of the superquadric.
    
    This code is based on "Rigid physically based superquadrics", A. H.
    Barr, in "Graphics Gems III", David Kirk, ed., Academic Press, 1992.
    
    @warning
    Resolution means the number of latitude or longitude lines for a
    complete superquadric. The resolution parameters are rounded to the
    nearest 4 in phi and 8 in theta.
    
    @warning
    Texture coordinates are not equally distributed around all
    superquadrics.
    
    @warning
    The Size and Thickness parameters control coefficients of
    superquadric generation, and may do not exactly describe the size of
    the superquadric.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSuperquadricSource, obj, update, **traits)
    
    toroidal = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether or not the superquadric is toroidal (1) or
        ellipsoidal (0). Initial value is 0.
        """
    )

    def _toroidal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetToroidal,
                        self.toroidal_)

    axis_of_symmetry = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get axis of symmetry for superquadric (x axis: 0, y axis: 1,
        z axis: 2). Initial value is 1.
        """
    )

    def _axis_of_symmetry_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxisOfSymmetry,
                        self.axis_of_symmetry)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

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

    phi_resolution = traits.Int(16, enter_set=True, auto_set=False, help=\
        """
        Set the number of points in the latitude direction. Initial value
        is 16.
        """
    )

    def _phi_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhiResolution,
                        self.phi_resolution)

    phi_roundness = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get Superquadric north/south roundness. Values range from 0
        (rectangular) to 1 (circular) to higher orders. Initial value is
        1.0.
        """
    )

    def _phi_roundness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhiRoundness,
                        self.phi_roundness)

    scale = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale)

    size = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get Superquadric isotropic size. Initial value is 0.5;
        """
    )

    def _size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSize,
                        self.size)

    theta_resolution = traits.Int(16, enter_set=True, auto_set=False, help=\
        """
        Set the number of points in the longitude direction. Initial
        value is 16.
        """
    )

    def _theta_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThetaResolution,
                        self.theta_resolution)

    theta_roundness = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get Superquadric east/west roundness. Values range from 0
        (rectangular) to 1 (circular) to higher orders. Initial value is
        1.0.
        """
    )

    def _theta_roundness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThetaRoundness,
                        self.theta_roundness)

    thickness = traits.Trait(0.3333, traits.Range(0.0001, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get Superquadric ring thickness (toroids only). Changing
        thickness maintains the outside diameter of the toroid. Initial
        value is 0.3333.
        """
    )

    def _thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThickness,
                        self.thickness)

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

    def set_x_axis_of_symmetry(self):
        """
        V.set_x_axis_of_symmetry()
        C++: void SetXAxisOfSymmetry()
        Set/Get axis of symmetry for superquadric (x axis: 0, y axis: 1,
        z axis: 2). Initial value is 1.
        """
        ret = self._vtk_obj.SetXAxisOfSymmetry()
        return ret
        

    def set_y_axis_of_symmetry(self):
        """
        V.set_y_axis_of_symmetry()
        C++: void SetYAxisOfSymmetry()
        Set/Get axis of symmetry for superquadric (x axis: 0, y axis: 1,
        z axis: 2). Initial value is 1.
        """
        ret = self._vtk_obj.SetYAxisOfSymmetry()
        return ret
        

    def set_z_axis_of_symmetry(self):
        """
        V.set_z_axis_of_symmetry()
        C++: void SetZAxisOfSymmetry()
        Set/Get axis of symmetry for superquadric (x axis: 0, y axis: 1,
        z axis: 2). Initial value is 1.
        """
        ret = self._vtk_obj.SetZAxisOfSymmetry()
        return ret
        

    _updateable_traits_ = \
    (('toroidal', 'GetToroidal'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('axis_of_symmetry', 'GetAxisOfSymmetry'), ('center', 'GetCenter'),
    ('output_points_precision', 'GetOutputPointsPrecision'),
    ('phi_resolution', 'GetPhiResolution'), ('phi_roundness',
    'GetPhiRoundness'), ('scale', 'GetScale'), ('size', 'GetSize'),
    ('theta_resolution', 'GetThetaResolution'), ('theta_roundness',
    'GetThetaRoundness'), ('thickness', 'GetThickness'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'toroidal', 'axis_of_symmetry', 'center',
    'output_points_precision', 'phi_resolution', 'phi_roundness',
    'progress_text', 'scale', 'size', 'theta_resolution',
    'theta_roundness', 'thickness'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SuperquadricSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SuperquadricSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['toroidal'], [], ['axis_of_symmetry', 'center',
            'output_points_precision', 'phi_resolution', 'phi_roundness', 'scale',
            'size', 'theta_resolution', 'theta_roundness', 'thickness']),
            title='Edit SuperquadricSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SuperquadricSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


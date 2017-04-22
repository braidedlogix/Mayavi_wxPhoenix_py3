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


class TexturedSphereSource(PolyDataAlgorithm):
    """
    TexturedSphereSource - create a sphere centered at the origin
    
    Superclass: PolyDataAlgorithm
    
    TexturedSphereSource creates a polygonal sphere of specified
    radius centered at the origin. The resolution (polygonal
    discretization) in both the latitude (phi) and longitude (theta)
    directions can be specified. It also is possible to create partial
    sphere by specifying maximum phi and theta angles.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTexturedSphereSource, obj, update, **traits)
    
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

    phi = traits.Trait(0.0, traits.Range(0.0, 180.0, enter_set=True, auto_set=False), help=\
        """
        Set the maximum latitude angle (0 is at north pole).
        """
    )

    def _phi_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhi,
                        self.phi)

    phi_resolution = traits.Trait(8, traits.Range(4, 1024, enter_set=True, auto_set=False), help=\
        """
        Set the number of points in the latitude direction.
        """
    )

    def _phi_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhiResolution,
                        self.phi_resolution)

    radius = traits.Trait(0.5, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set radius of sphere.
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    theta = traits.Trait(0.0, traits.Range(0.0, 360.0, enter_set=True, auto_set=False), help=\
        """
        Set the maximum longitude angle.
        """
    )

    def _theta_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTheta,
                        self.theta)

    theta_resolution = traits.Trait(8, traits.Range(4, 1024, enter_set=True, auto_set=False), help=\
        """
        Set the number of points in the longitude direction.
        """
    )

    def _theta_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThetaResolution,
                        self.theta_resolution)

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
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('output_points_precision', 'GetOutputPointsPrecision'), ('phi',
    'GetPhi'), ('phi_resolution', 'GetPhiResolution'), ('radius',
    'GetRadius'), ('theta', 'GetTheta'), ('theta_resolution',
    'GetThetaResolution'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'output_points_precision', 'phi',
    'phi_resolution', 'progress_text', 'radius', 'theta',
    'theta_resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TexturedSphereSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TexturedSphereSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['output_points_precision', 'phi', 'phi_resolution',
            'radius', 'theta', 'theta_resolution']),
            title='Edit TexturedSphereSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TexturedSphereSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


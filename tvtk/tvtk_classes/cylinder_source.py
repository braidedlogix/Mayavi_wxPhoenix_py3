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


class CylinderSource(PolyDataAlgorithm):
    """
    CylinderSource - generate a cylinder centered at origin
    
    Superclass: PolyDataAlgorithm
    
    CylinderSource creates a polygonal cylinder centered at Center;
    The axis of the cylinder is aligned along the global y-axis. The
    height and radius of the cylinder can be specified, as well as the
    number of sides. It is also possible to control whether the cylinder
    is open-ended or capped. If you have the end points of the cylinder,
    you should use a LineSource followed by a TubeFilter instead of
    the CylinderSource.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCylinderSource, obj, update, **traits)
    
    capping = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off whether to cap cylinder with polygons. Initial value
        is true.
        """
    )

    def _capping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCapping,
                        self.capping_)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    height = traits.Trait(1.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set the height of the cylinder. Initial value is 1.
        """
    )

    def _height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeight,
                        self.height)

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

    radius = traits.Trait(0.5, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set the radius of the cylinder. Initial value is 0.5
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    resolution = traits.Trait(6, traits.Range(2, 512, enter_set=True, auto_set=False), help=\
        """
        Set the number of facets used to define cylinder. Initial value
        is 6.
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
    (('capping', 'GetCapping'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('center',
    'GetCenter'), ('height', 'GetHeight'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('radius', 'GetRadius'), ('resolution',
    'GetResolution'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'capping', 'debug', 'global_warning_display',
    'release_data_flag', 'center', 'height', 'output_points_precision',
    'progress_text', 'radius', 'resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CylinderSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CylinderSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['capping'], [], ['center', 'height', 'output_points_precision',
            'radius', 'resolution']),
            title='Edit CylinderSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CylinderSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


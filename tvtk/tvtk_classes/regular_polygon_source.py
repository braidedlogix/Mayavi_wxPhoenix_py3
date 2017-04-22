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


class RegularPolygonSource(PolyDataAlgorithm):
    """
    RegularPolygonSource - create a regular, n-sided polygon and/or
    polyline
    
    Superclass: PolyDataAlgorithm
    
    RegularPolygonSource is a source object that creates a single
    n-sided polygon and/or polyline. The polygon is centered at a
    specified point, orthogonal to a specified normal, and with a
    circumscribing radius set by the user. The user can also specify the
    number of sides of the polygon ranging from [3,N].
    
    This object can be used for seeding streamlines or defining regions
    for clipping/cutting.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRegularPolygonSource, obj, update, **traits)
    
    generate_polygon = tvtk_base.true_bool_trait(help=\
        """
        Control whether a polygon is produced. By default,
        generate_polygon is enabled.
        """
    )

    def _generate_polygon_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePolygon,
                        self.generate_polygon_)

    generate_polyline = tvtk_base.true_bool_trait(help=\
        """
        Control whether a polyline is produced. By default,
        generate_polyline is enabled.
        """
    )

    def _generate_polyline_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePolyline,
                        self.generate_polyline_)

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

    number_of_sides = traits.Trait(6, traits.Range(3, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the number of sides of the polygon. By default, the
        number of sides is set to six.
        """
    )

    def _number_of_sides_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSides,
                        self.number_of_sides)

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

    radius = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the radius of the polygon. By default, the radius is set
        to 0.5.
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

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
    (('generate_polygon', 'GetGeneratePolygon'), ('generate_polyline',
    'GetGeneratePolyline'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('center',
    'GetCenter'), ('normal', 'GetNormal'), ('number_of_sides',
    'GetNumberOfSides'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('radius', 'GetRadius'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_polygon', 'generate_polyline',
    'global_warning_display', 'release_data_flag', 'center', 'normal',
    'number_of_sides', 'output_points_precision', 'progress_text',
    'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RegularPolygonSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RegularPolygonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_polygon', 'generate_polyline'], [], ['center',
            'normal', 'number_of_sides', 'output_points_precision', 'radius']),
            title='Edit RegularPolygonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RegularPolygonSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


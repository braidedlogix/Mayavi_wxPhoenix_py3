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


class PointSource(PolyDataAlgorithm):
    """
    PointSource - create a random cloud of points
    
    Superclass: PolyDataAlgorithm
    
    PointSource is a source object that creates a user-specified
    number of points within a specified radius about a specified center
    point. By default location of the points is random within the sphere.
    It is also possible to generate random points only on the surface of
    the sphere. The output poly_data has the specified number of points
    and 1 cell - a PolyVertex containing all of the points.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointSource, obj, update, **traits)
    
    distribution = traits.Trait('uniform',
    tvtk_base.TraitRevPrefixMap({'uniform': 1, 'shell': 0}), help=\
        """
        Specify the distribution to use.  The default is a uniform
        distribution.  The shell distribution produces random points on
        the surface of the sphere, none in the interior.
        """
    )

    def _distribution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistribution,
                        self.distribution_)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    number_of_points = traits.Trait(10, traits.Range(1, 9223372036854775807, enter_set=True, auto_set=False), help=\
        """
        Set the number of points to generate.
        """
    )

    def _number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPoints,
                        self.number_of_points)

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
        Set the radius of the point cloud.  If you are generating a
        Gaussian distribution, then this is the standard deviation for
        each of x, y, and z.
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    def _get_random_sequence(self):
        return wrap_vtk(self._vtk_obj.GetRandomSequence())
    def _set_random_sequence(self, arg):
        old_val = self._get_random_sequence()
        self._wrap_call(self._vtk_obj.SetRandomSequence,
                        deref_vtk(arg))
        self.trait_property_changed('random_sequence', old_val, arg)
    random_sequence = traits.Property(_get_random_sequence, _set_random_sequence, help=\
        """
        Set/Get a random sequence generator. By default, the generator in
        Math is used to maintain backwards compatibility.
        """
    )

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
    ('distribution', 'GetDistribution'), ('center', 'GetCenter'),
    ('number_of_points', 'GetNumberOfPoints'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('radius', 'GetRadius'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'distribution', 'center', 'number_of_points',
    'output_points_precision', 'progress_text', 'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PointSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['distribution'], ['center', 'number_of_points',
            'output_points_precision', 'radius']),
            title='Edit PointSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


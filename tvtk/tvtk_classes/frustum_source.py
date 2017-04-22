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


class FrustumSource(PolyDataAlgorithm):
    """
    FrustumSource - create a polygonal representation of a frustum
    
    Superclass: PolyDataAlgorithm
    
    FrustumSource creates a frustum defines by a set of planes. The
    frustum is represented with four-sided polygons. It is possible to
    specify extra lines to better visualize the field of view.
    
    @par Usage: Typical use consists of 3 steps:
    1. get the planes coefficients from a Camera with
       Camera::GetFrustumPlanes()
    2. initialize the planes with Planes::SetFrustumPlanes() with the
       planes coefficients
    3. pass the Planes to a FrustumSource.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFrustumSource, obj, update, **traits)
    
    show_lines = tvtk_base.true_bool_trait(help=\
        """
        Tells if some extra lines will be generated. Initial value is
        true.
        """
    )

    def _show_lines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShowLines,
                        self.show_lines_)

    lines_length = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Length of the extra lines. This a stricly positive value. Initial
        value is 1.0.
        """
    )

    def _lines_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLinesLength,
                        self.lines_length)

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

    def _get_planes(self):
        return wrap_vtk(self._vtk_obj.GetPlanes())
    def _set_planes(self, arg):
        old_val = self._get_planes()
        self._wrap_call(self._vtk_obj.SetPlanes,
                        deref_vtk(arg))
        self.trait_property_changed('planes', old_val, arg)
    planes = traits.Property(_get_planes, _set_planes, help=\
        """
        Return the 6 planes defining the frustum. Initial value is NULL.
        The 6 planes are defined in this order:
        left,right,bottom,top,far,near. If Planes==NULL or if
        planes->_get_number_of_planes()!=_6 when request_data() is called, an
        error message will be emitted and request_data() will return right
        away.
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
    (('show_lines', 'GetShowLines'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('lines_length', 'GetLinesLength'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'show_lines', 'lines_length',
    'output_points_precision', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FrustumSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FrustumSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['show_lines'], [], ['lines_length',
            'output_points_precision']),
            title='Edit FrustumSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FrustumSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


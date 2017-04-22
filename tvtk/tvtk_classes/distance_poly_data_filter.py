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


class DistancePolyDataFilter(PolyDataAlgorithm):
    """
    DistancePolyDataFilter - Computes the signed distance from one
    PolyData to another.
    
    Superclass: PolyDataAlgorithm
    
    The signed distance to the second input is computed at every point in
    the first input using ImplicitPolyDataDistance. Optionally, the
    signed distance to the first input at every point in the second input
    can be computed. This may be enabled by calling
    compute_second_distance_on().
    
    If the signed distance is not desired, the unsigned distance can be
    computed by calling signed_distance_off(). The signed distance field
    may be negated by calling negate_distance_on();
    
    This code was contributed in the VTK Journal paper: "Boolean Operations on Surfaces in VTK Without External
    Libraries" by Cory Quammen, Chris Weigle C., Russ Taylor
    http://hdl.handle.net/10380/3262
    http://www.midasjournal.org/browse/publication/797
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDistancePolyDataFilter, obj, update, **traits)
    
    compute_second_distance = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable computation of a second output poly data with the
        distance from the first poly data at each point. Defaults to on.
        """
    )

    def _compute_second_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeSecondDistance,
                        self.compute_second_distance_)

    negate_distance = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable negation of the distance values. Defaults to off.
        Has no effect if signed_distance is off.
        """
    )

    def _negate_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNegateDistance,
                        self.negate_distance_)

    signed_distance = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable computation of the signed distance between the
        first poly data and the second poly data. Defaults to on.
        """
    )

    def _signed_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSignedDistance,
                        self.signed_distance_)

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

    def _get_second_distance_output(self):
        return wrap_vtk(self._vtk_obj.GetSecondDistanceOutput())
    second_distance_output = traits.Property(_get_second_distance_output, help=\
        """
        Get the second output, which is a copy of the second input with
        an additional distance scalar field. Note this will return a
        valid data object only after this->Update() is called.
        """
    )

    _updateable_traits_ = \
    (('compute_second_distance', 'GetComputeSecondDistance'),
    ('negate_distance', 'GetNegateDistance'), ('signed_distance',
    'GetSignedDistance'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_second_distance', 'debug',
    'global_warning_display', 'negate_distance', 'release_data_flag',
    'signed_distance', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DistancePolyDataFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DistancePolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_second_distance', 'negate_distance',
            'signed_distance'], [], []),
            title='Edit DistancePolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DistancePolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


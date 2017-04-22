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


class SubPixelPositionEdgels(PolyDataAlgorithm):
    """
    SubPixelPositionEdgels - adjust edgel locations based on gradients.
    
    Superclass: PolyDataAlgorithm
    
    SubPixelPositionEdgels is a filter that takes a series of linked
    edgels (digital curves) and gradient maps as input. It then adjusts
    the edgel locations based on the gradient data. Specifically, the
    algorithm first determines the neighboring gradient magnitudes of an
    edgel using simple interpolation of its neighbors. It then fits the
    following three data points: negative gradient direction gradient
    magnitude, edgel gradient magnitude and positive gradient direction
    gradient magnitude to a quadratic function. It then solves this
    quadratic to find the maximum gradient location along the gradient
    orientation.  It then modifies the edgels location along the gradient
    orientation to the calculated maximum location. This algorithm does
    not adjust an edgel in the direction orthogonal to its gradient
    vector.
    
    @sa
    ImageData ImageGradient LinkEdgels
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSubPixelPositionEdgels, obj, update, **traits)
    
    target_flag = tvtk_base.false_bool_trait(help=\
        """
        These methods can make the positioning look for a target scalar
        value instead of looking for a maximum.
        """
    )

    def _target_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetFlag,
                        self.target_flag_)

    target_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        These methods can make the positioning look for a target scalar
        value instead of looking for a maximum.
        """
    )

    def _target_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetValue,
                        self.target_value)

    def _get_grad_maps(self):
        return wrap_vtk(self._vtk_obj.GetGradMaps())
    grad_maps = traits.Property(_get_grad_maps, help=\
        """
        Set/Get the gradient data for doing the position adjustments.
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

    def set_grad_maps_data(self, *args):
        """
        V.set_grad_maps_data(StructuredPoints)
        C++: void SetGradMapsData(StructuredPoints *gm)
        Set/Get the gradient data for doing the position adjustments.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGradMapsData, *my_args)
        return ret

    _updateable_traits_ = \
    (('target_flag', 'GetTargetFlag'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('target_value', 'GetTargetValue'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'target_flag', 'progress_text', 'target_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SubPixelPositionEdgels, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SubPixelPositionEdgels properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['target_flag'], [], ['target_value']),
            title='Edit SubPixelPositionEdgels properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SubPixelPositionEdgels properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


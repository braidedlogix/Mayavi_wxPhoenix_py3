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

from tvtk.tvtk_classes.generic_subdivision_error_metric import GenericSubdivisionErrorMetric


class SmoothErrorMetric(GenericSubdivisionErrorMetric):
    """
    SmoothErrorMetric - Objects that compute geometry-based error
    during cell tessellation according to some max angle.
    
    Superclass: GenericSubdivisionErrorMetric
    
    It is a concrete error metric, based on a geometric criterium: a max
    angle between the chord passing through the midpoint and one of the
    endpoints and the other chord passing through the midpoint and the
    other endpoint of the edge. It is related to the flatness of an edge.
    
    @sa
    GenericCellTessellator GenericSubdivisionErrorMetric
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSmoothErrorMetric, obj, update, **traits)
    
    angle_tolerance = traits.Float(90.1, enter_set=True, auto_set=False, help=\
        """
        Set the flatness threshold with an angle in degrees. Internally
        compute the cosine. value is supposed to be in ]90,180[, if not
        it is clamped in [90.1,179.9]. For instance 178  will give better
        result than 150.
        """
    )

    def _angle_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAngleTolerance,
                        self.angle_tolerance)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('angle_tolerance', 'GetAngleTolerance'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'angle_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SmoothErrorMetric, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SmoothErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['angle_tolerance']),
            title='Edit SmoothErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SmoothErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


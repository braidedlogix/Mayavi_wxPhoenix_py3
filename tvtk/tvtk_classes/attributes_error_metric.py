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


class AttributesErrorMetric(GenericSubdivisionErrorMetric):
    """
    AttributesErrorMetric - Objects that compute attribute-based error
    during cell tessellation.
    
    Superclass: GenericSubdivisionErrorMetric
    
    It is a concrete error metric, based on an attribute criterium: the
    variation of the active attribute/component value from a linear ramp
    
    @sa
    GenericCellTessellator GenericSubdivisionErrorMetric
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAttributesErrorMetric, obj, update, **traits)
    
    absolute_attribute_tolerance = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set the absolute attribute accuracy to `value'. See
        get_absolute_attribute_tolerance() for details. It is particularly
        useful when some concrete implementation of GenericAttribute
        does not support get_range() request, called internally in
        set_attribute_tolerance(). It may happen when the implementation
        support higher order attributes but cannot compute the range.
        \pre valid_range_value: value>0
        """
    )

    def _absolute_attribute_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAbsoluteAttributeTolerance,
                        self.absolute_attribute_tolerance)

    attribute_tolerance = traits.Float(0.1, enter_set=True, auto_set=False, help=\
        """
        Set the relative attribute accuracy to `value'. See
        get_attribute_tolerance() for details.
        \pre valid_range_value: value>0 && value<1
        """
    )

    def _attribute_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAttributeTolerance,
                        self.attribute_tolerance)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('absolute_attribute_tolerance',
    'GetAbsoluteAttributeTolerance'), ('attribute_tolerance',
    'GetAttributeTolerance'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'absolute_attribute_tolerance',
    'attribute_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AttributesErrorMetric, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AttributesErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['absolute_attribute_tolerance',
            'attribute_tolerance']),
            title='Edit AttributesErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AttributesErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


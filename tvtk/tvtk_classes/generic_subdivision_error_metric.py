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

from tvtk.tvtk_classes.object import Object


class GenericSubdivisionErrorMetric(Object):
    """
    GenericSubdivisionErrorMetric - Objects that compute error during
    cell tessellation.
    
    Superclass: Object
    
    Objects of that class answer the following question during the cell
    subdivision: "does the edge need to be subdivided?" through
    requires_edge_subdivision(). The answer depends on the criterium
    actually used in the subclass of this abstract class: a
    geometric-based error metric (variation of edge from a straight
    line), an attribute-based error metric (variation of the active
    attribute/component value from a linear ramp) , a view-depend error
    metric, ... Cell subdivision is performed in the context of the
    adaptor framework: higher-order, or complex cells, are automatically
    tessellated into simplices so that they can be processed with
    conventional visualization algorithms.
    
    @sa
    GenericCellTessellator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericSubdivisionErrorMetric, obj, update, **traits)
    
    def _get_data_set(self):
        return wrap_vtk(self._vtk_obj.GetDataSet())
    def _set_data_set(self, arg):
        old_val = self._get_data_set()
        self._wrap_call(self._vtk_obj.SetDataSet,
                        deref_vtk(arg))
        self.trait_property_changed('data_set', old_val, arg)
    data_set = traits.Property(_get_data_set, _set_data_set, help=\
        """
        Set/Get the dataset to be tessellated.
        """
    )

    def _get_generic_cell(self):
        return wrap_vtk(self._vtk_obj.GetGenericCell())
    def _set_generic_cell(self, arg):
        old_val = self._get_generic_cell()
        self._wrap_call(self._vtk_obj.SetGenericCell,
                        deref_vtk(arg))
        self.trait_property_changed('generic_cell', old_val, arg)
    generic_cell = traits.Property(_get_generic_cell, _set_generic_cell, help=\
        """
        The cell that the edge belongs to.
        """
    )

    def get_error(self, *args):
        """
        V.get_error([float, ...], [float, ...], [float, ...], float)
            -> float
        C++: virtual double GetError(double *leftPoint, double *midPoint,
            double *rightPoint, double alpha)
        Return the error at the mid-point. The type of error depends on
        the state of the concrete error metric. For instance, it can
        return an absolute or relative error metric. See
        requires_edge_subdivision() for a description of the arguments.
        \pre left_point_exists: left_point!=_0
        \pre mid_point_exists: mid_point!=_0
        \pre right_point_exists: right_point!=_0
        \pre clamped_alpha: alpha>0 && alpha<1
        \pre valid_size:
            sizeof(left_point)=sizeof(mid_point)=sizeof(right_point)
        =_get_attribute_collection()->_get_number_of_point_centered_components()+_6
        \post positive_result: result>=0
        """
        ret = self._wrap_call(self._vtk_obj.GetError, *args)
        return ret

    def requires_edge_subdivision(self, *args):
        """
        V.requires_edge_subdivision([float, ...], [float, ...], [float,
            ...], float) -> int
        C++: virtual int RequiresEdgeSubdivision(double *leftPoint,
            double *midPoint, double *rightPoint, double alpha)
        Does the edge need to be subdivided according to the implemented
        computation? The edge is defined by its `left_point' and its
        `right_point'. `left_point', `mid_point' and `right_point' have to be
        initialized before calling requires_edge_subdivision(). Their
        format is global coordinates, parametric coordinates and point
        centered attributes: xyx rst abc de... `alpha' is the normalized
        abscissa of the midpoint along the edge. (close to 0 means close
        to the left point, close to 1 means close to the right point)
        \pre left_point_exists: left_point!=_0
        \pre mid_point_exists: mid_point!=_0
        \pre right_point_exists: right_point!=_0
        \pre clamped_alpha: alpha>0 && alpha<1
        \pre valid_size:
            sizeof(left_point)=sizeof(mid_point)=sizeof(right_point)
        =_get_attribute_collection()->_get_number_of_point_centered_components()+_6
        """
        ret = self._wrap_call(self._vtk_obj.RequiresEdgeSubdivision, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericSubdivisionErrorMetric, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericSubdivisionErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit GenericSubdivisionErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericSubdivisionErrorMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


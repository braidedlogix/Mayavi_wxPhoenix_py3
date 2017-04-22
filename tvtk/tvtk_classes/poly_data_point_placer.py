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

from tvtk.tvtk_classes.point_placer import PointPlacer


class PolyDataPointPlacer(PointPlacer):
    """
    PolyDataPointPlacer - Base class to place points given constraints
    on polygonal data
    
    Superclass: PointPlacer
    
    PolyDataPointPlacer is a base class to place points on the surface
    of polygonal data.
    
    @par Usage: The actors that render polygonal data and wish to be
    considered for placement by this placer are added to the list
    asplacer->_add_prop( poly_data_actor );
    
    @sa
    PolygonalSurfacePointPlacer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyDataPointPlacer, obj, update, **traits)
    
    def _get_number_of_props(self):
        return self._vtk_obj.GetNumberOfProps()
    number_of_props = traits.Property(_get_number_of_props, help=\
        """
        
        """
    )

    def _get_prop_picker(self):
        return wrap_vtk(self._vtk_obj.GetPropPicker())
    prop_picker = traits.Property(_get_prop_picker, help=\
        """
        Get the Prop picker.
        """
    )

    def add_prop(self, *args):
        """
        V.add_prop(Prop)
        C++: virtual void AddProp(Prop *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddProp, *my_args)
        return ret

    def has_prop(self, *args):
        """
        V.has_prop(Prop) -> int
        C++: int HasProp(Prop *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HasProp, *my_args)
        return ret

    def remove_all_props(self):
        """
        V.remove_all_props()
        C++: virtual void RemoveAllProps()"""
        ret = self._vtk_obj.RemoveAllProps()
        return ret
        

    def remove_view_prop(self, *args):
        """
        V.remove_view_prop(Prop)
        C++: virtual void RemoveViewProp(Prop *prop)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveViewProp, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('pixel_tolerance', 'GetPixelTolerance'),
    ('world_tolerance', 'GetWorldTolerance'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pixel_tolerance',
    'world_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyDataPointPlacer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyDataPointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['pixel_tolerance', 'world_tolerance']),
            title='Edit PolyDataPointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyDataPointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


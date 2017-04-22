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


class CellCentersPointPlacer(PointPlacer):
    """
    CellCentersPointPlacer - Snaps points at the center of a cell
    
    Superclass: PointPlacer
    
    CellCentersPointPlacer is a class to snap points on the center of
    cells. The class has 3 modes. In the parametric_center mode, it snaps
    points to the parametric center of the cell (see Cell). In
    cell_points_mean mode, points are snapped to the mean of the points in
    the cell. In 'None' mode, no snapping is performed. The computed
    world position is the picked position within the cell.
    
    @par Usage: The actors that render data and wish to be considered for
    placement by this placer are added to the list asplacer->_add_prop(
    actor );
    
    @sa
    PointPlacer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellCentersPointPlacer, obj, update, **traits)
    
    mode = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Modes to change the point placement. Parametric center picks the
        parametric center within the cell. cell_points_mean picks the
        average of all points in the cell. When the mode is None, the
        input point is passed through unmodified. Default is
        cell_points_mean.
        """
    )

    def _mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMode,
                        self.mode)

    def _get_cell_picker(self):
        return wrap_vtk(self._vtk_obj.GetCellPicker())
    cell_picker = traits.Property(_get_cell_picker, help=\
        """
        Get the Prop picker.
        """
    )

    def _get_number_of_props(self):
        return self._vtk_obj.GetNumberOfProps()
    number_of_props = traits.Property(_get_number_of_props, help=\
        """
        
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
    'GetGlobalWarningDisplay'), ('mode', 'GetMode'), ('pixel_tolerance',
    'GetPixelTolerance'), ('world_tolerance', 'GetWorldTolerance'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'mode', 'pixel_tolerance',
    'world_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CellCentersPointPlacer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CellCentersPointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['mode', 'pixel_tolerance', 'world_tolerance']),
            title='Edit CellCentersPointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellCentersPointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            


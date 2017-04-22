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

from tvtk.tvtk_classes.abstract_interpolated_velocity_field import AbstractInterpolatedVelocityField


class AMRInterpolatedVelocityField(AbstractInterpolatedVelocityField):
    """
    AMRInterpolatedVelocityField - A concrete class for obtaining
     the interpolated velocity values at a point in AMR data.
    
    Superclass: AbstractInterpolatedVelocityField
    
    The main functionality supported here is the point location inside
    OverlappingAMR data set.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAMRInterpolatedVelocityField, obj, update, **traits)
    
    last_cell_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _last_cell_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLastCellId,
                        self.last_cell_id)

    def get_last_data_set(self):
        """
        V.get_last_data_set() -> DataSet
        C++: DataSet *GetLastDataSet()"""
        ret = wrap_vtk(self._vtk_obj.GetLastDataSet())
        return ret
        

    def set_last_data_set(self, *args):
        """
        V.set_last_data_set(int, int) -> bool
        C++: bool SetLastDataSet(int level, int id)"""
        ret = self._wrap_call(self._vtk_obj.SetLastDataSet, *args)
        return ret

    def _get_amr_data_set(self):
        return wrap_vtk(self._vtk_obj.GetAmrDataSet())
    amr_data_set = traits.Property(_get_amr_data_set, help=\
        """
        
        """
    )

    def get_last_data_set_location(self, *args):
        """
        V.get_last_data_set_location(int, int) -> bool
        C++: bool GetLastDataSetLocation(unsigned int &level,
            unsigned int &id)"""
        ret = self._wrap_call(self._vtk_obj.GetLastDataSetLocation, *args)
        return ret

    def find_grid(self, *args):
        """
        V.find_grid([float, float, float], OverlappingAMR, int, int)
            -> bool
        C++: static bool FindGrid(double q[3], OverlappingAMR *amrds,
            unsigned int &level, unsigned int &gridId)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FindGrid, *my_args)
        return ret

    def set_amr_data(self, *args):
        """
        V.set_amr_data(OverlappingAMR)
        C++: void SetAMRData(OverlappingAMR *amr)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetAMRData, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('last_cell_id', 'GetLastCellId'),
    ('caching', 'GetCaching'), ('force_surface_tangent_vector',
    'GetForceSurfaceTangentVector'), ('normalize_vector',
    'GetNormalizeVector'), ('surface_dataset', 'GetSurfaceDataset'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'caching',
    'force_surface_tangent_vector', 'last_cell_id', 'normalize_vector',
    'surface_dataset'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AMRInterpolatedVelocityField, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AMRInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['caching', 'force_surface_tangent_vector',
            'last_cell_id', 'normalize_vector', 'surface_dataset']),
            title='Edit AMRInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AMRInterpolatedVelocityField properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

